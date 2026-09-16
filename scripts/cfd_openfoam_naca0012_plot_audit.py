"""Recover the alpha-zero OpenFOAM drag marker from the hash-pinned official plot."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

from cfd_naca0012_sa_control_audit import cfl3d_reference


PLOT_SHA256 = "94003df0353e2c2056fcfb1f733ce7ab0aa4848196c4d36770f74804818df512"
NASA_SHA256 = "b07afec6ce3ae4bf2f2d1a1d53785fde0a5ca68481a0d4186aa92754d811944e"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def components(mask: np.ndarray) -> list[list[tuple[int, int]]]:
    height, width = mask.shape
    unseen = {(x, y) for y, x in np.argwhere(mask)}
    found = []
    while unseen:
        seed = unseen.pop()
        pending = [seed]
        component = [seed]
        while pending:
            x, y = pending.pop()
            for point in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= point[0] < width and 0 <= point[1] < height and point in unseen:
                    unseen.remove(point)
                    pending.append(point)
                    component.append(point)
        found.append(component)
    return found


def audit(plot: Path, nasa_reference: Path, standard_audit: Path) -> dict:
    plot = plot.resolve(strict=True)
    nasa_reference = nasa_reference.resolve(strict=True)
    standard_audit = standard_audit.resolve(strict=True)
    if sha256(plot) != PLOT_SHA256:
        raise ValueError("Official OpenFOAM plot checksum mismatch")
    if sha256(nasa_reference) != NASA_SHA256:
        raise ValueError("NASA SA coefficient checksum mismatch")

    pixels = np.asarray(Image.open(plot).convert("RGB"))
    black = np.max(pixels, axis=2) < 50
    horizontal = [
        y for y in range(10, 340) if int(black[y, 150:575].sum()) >= 400
    ]
    vertical = [
        x for x in range(140, 580) if int(black[20:330, x].sum()) >= 290
    ]
    if horizontal != [25, 320] or vertical != [162, 564]:
        raise ValueError("Official plot-axis pixel bounds changed")
    y_top, y_bottom = horizontal
    x_left, x_right = vertical

    axis = {
        "alpha_min_deg": -5.0,
        "alpha_max_deg": 20.0,
        "cd_min": 0.0,
        "cd_max": 0.03,
    }
    alpha_zero_x = x_left + (0.0 - axis["alpha_min_deg"]) * (
        x_right - x_left
    ) / (axis["alpha_max_deg"] - axis["alpha_min_deg"])
    x_lo = int(round(alpha_zero_x)) - 8
    x_hi = int(round(alpha_zero_x)) + 9
    roi = black[y_top + 1 : y_bottom, x_lo:x_hi]
    candidates = []
    for component in components(roi):
        xs = [point[0] + x_lo for point in component]
        ys = [point[1] + y_top + 1 for point in component]
        width = max(xs) - min(xs) + 1
        height = max(ys) - min(ys) + 1
        if len(component) >= 25 and 5 <= width <= 10 and 5 <= height <= 10:
            candidates.append((component, xs, ys))
    if len(candidates) != 1:
        raise ValueError("Could not uniquely identify alpha-zero OpenFOAM marker")
    component, xs, ys = candidates[0]
    marker_x = float(np.mean(xs))
    marker_y = float(np.mean(ys))
    plotted_cd = axis["cd_max"] - (marker_y - y_top) * (
        axis["cd_max"] - axis["cd_min"]
    ) / (y_bottom - y_top)
    one_pixel_cd = (axis["cd_max"] - axis["cd_min"]) / (y_bottom - y_top)

    nasa = cfl3d_reference(nasa_reference)
    standard = json.loads(standard_audit.read_text())
    standard_cd = float(standard["last_window_mean"]["Cd"])
    nasa_cd = float(nasa["cd"])
    plot_minus_nasa = plotted_cd - nasa_cd
    standard_minus_plot = standard_cd - plotted_cd
    original_force_limit = 0.0002

    return {
        "scope": "Raster recovery of official OpenFOAM alpha-zero drag marker",
        "plot": str(plot),
        "plot_sha256": PLOT_SHA256,
        "plot_source_commit": "4b7889154eb5ed4aaffb4d269055083c364a8286",
        "standard_sa_audit": str(standard_audit),
        "standard_sa_audit_sha256": sha256(standard_audit),
        "image_size_pixels": [int(pixels.shape[1]), int(pixels.shape[0])],
        "axis_pixel_bounds": {
            "left": x_left,
            "right": x_right,
            "top": y_top,
            "bottom": y_bottom,
        },
        "axis_values": axis,
        "marker": {
            "pixel_count": len(component),
            "bounds": [int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys))],
            "center": [marker_x, marker_y],
            "recovered_cd": plotted_cd,
            "conservative_raster_uncertainty_cd": one_pixel_cd,
        },
        "nasa_cfl3d_sa_cd": nasa_cd,
        "official_plot_minus_nasa_cd": plot_minus_nasa,
        "official_plot_consistent_with_nasa_at_raster_resolution": (
            abs(plot_minus_nasa) <= one_pixel_cd
        ),
        "rocket_workbench_exact_standard_sa_cd": standard_cd,
        "rocket_workbench_minus_official_plot_cd": standard_minus_plot,
        "original_force_agreement_limit": original_force_limit,
        "rocket_workbench_consistent_with_official_plot_gate": (
            abs(standard_minus_plot) <= original_force_limit
        ),
        "interpretation": (
            "The official raster places its alpha-zero OpenFOAM marker at the NASA "
            "CFL3D value within one-pixel resolution, while the reproduced exact "
            "standard-SA result remains outside the predeclared force tolerance."
        ),
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plot", required=True, type=Path)
    parser.add_argument("--nasa-reference", required=True, type=Path)
    parser.add_argument("--standard-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.plot, args.nasa_reference, args.standard_audit)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "openfoam-naca0012-plot-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
