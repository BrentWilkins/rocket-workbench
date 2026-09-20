"""Publish the complete nominal payload grid and its decision plots.

Input JSON files are local OpenRocket screen results. The generated CSV and SVGs
are portable report evidence; they do not replace the per-case run artifacts.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "rocket-workbench-payload-sweep"
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


BODIES = (500.0, 530.0, 560.0)
NOSES = (40.0, 50.0, 60.0, 70.0)
SPANS = (45.0, 50.0, 53.65384615384615, 55.0, 65.0)
SHAPES = ("conical", "ogive", "ellipsoid")
MOTORS = ("D12-5", "E12-6")
COLORS = {"conical": "#c9512c", "ogive": "#188b76", "ellipsoid": "#4b72ad"}
MARKERS = {500.0: "o", 530.0: "s", 560.0: "^"}
FIELDS = (
    "body_mm", "nose_mm", "nose_shape", "span_mm", "fin_root_mm", "motor",
    "wind_m_s", "launch_mass_g", "loaded_cg_mm", "apogee_m", "guide_m_s",
    "stability_cal", "deployment_m_s", "descent_m_s", "drift_m", "status",
)


def load_grid(paths: list[Path]) -> list[dict]:
    rows = []
    seen = set()
    for path in paths:
        for source in json.loads(path.read_text()):
            row = dict(source)
            row.setdefault("fin_root_mm", 65.0)
            key = tuple(row.get(field) for field in
                        ("body_mm", "nose_mm", "span_mm", "nose_shape", "fin_root_mm", "motor", "wind_m_s"))
            if key in seen:
                raise ValueError(f"Duplicate grid point {key} in {path}")
            seen.add(key)
            rows.append(row)
    expected = {
        (body, nose, span, shape, 65.0, motor, 4.0)
        for body in BODIES for nose in NOSES for span in SPANS
        for shape in SHAPES for motor in MOTORS
    }
    if seen != expected:
        raise ValueError(f"Incomplete nominal grid: {len(expected - seen)} missing, {len(seen - expected)} unexpected")
    if any(row["status"] != "completed" for row in rows):
        raise ValueError("All D/E grid points must have completed OpenRocket flights")
    return sorted(rows, key=lambda row: (
        row["motor"], row["body_mm"], row["nose_shape"], row["nose_mm"], row["span_mm"]
    ))


def short_listed(row: dict) -> bool:
    """A design target for comparison, not a flight-clearance declaration."""
    return (row["stability_cal"] >= 1.5 and row["guide_m_s"] >= 12
            and row["deployment_m_s"] <= 10 and row["descent_m_s"] <= 6)


def nose_profiles(output: Path) -> None:
    from rocket_workbench.nose import radius_at

    fig, axes = plt.subplots(1, 3, figsize=(8.2, 4), sharex=True, sharey=True)
    for ax, (shape, length) in zip(axes, (("conical", 50), ("ogive", 40), ("ellipsoid", 40)), strict=True):
        stations = [length * index / 200 for index in range(201)]
        radii = [radius_at(shape, x, length, 20.8) for x in stations]
        heights = [length - x for x in stations]
        ax.fill_betweenx(heights, [-r for r in radii], radii, color=COLORS[shape], alpha=0.2)
        ax.plot(radii, heights, color=COLORS[shape], lw=2)
        ax.plot([-r for r in radii], heights, color=COLORS[shape], lw=2)
        ax.plot([-20.8, 20.8], [0, 0], color="#555555", lw=1)
        ax.set(title=f"{length} mm {shape}", aspect="equal", xlim=(-25, 25), ylim=(-2, 54))
        ax.set_xticks([])
        ax.grid(axis="y", alpha=0.2)
    axes[0].set_ylabel("Height above body tube (mm)")
    fig.suptitle("Nose profiles at the same 41.6 mm base diameter")
    fig.tight_layout(rect=(0, 0, 1, 0.9))
    fig.savefig(output, metadata={"Date": None})
    fig.savefig(output.with_suffix(".png"), dpi=160)
    plt.close(fig)


def tradeoff(rows: list[dict], output: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12.8, 5.4), sharex=True)
    for ax, motor in zip(axes, MOTORS, strict=True):
        subset = [row for row in rows if row["motor"] == motor]
        for row in subset:
            eligible = short_listed(row)
            ax.scatter(row["stability_cal"], row["apogee_m"],
                       color=COLORS[row["nose_shape"]] if eligible else "#c9cdd0",
                       marker=MARKERS[row["body_mm"]], s=31 if eligible else 15,
                       alpha=0.8 if eligible else 0.5, zorder=3 if eligible else 1)
        for nose, shape, color, label, offset in (
            (50, "conical", "#111111", "current print", (-84, -24)),
            (40, "ogive", "#b78300", "40 mm ogive candidate", (9, 8)),
        ):
            row = next(row for row in subset if row["body_mm"] == 500
                       and row["nose_mm"] == nose and row["nose_shape"] == shape
                       and abs(row["span_mm"] - 53.65384615384615) < 1e-3)
            ax.scatter(row["stability_cal"], row["apogee_m"], marker="*", s=180,
                       color=color, edgecolor="white", linewidth=0.6, zorder=5)
            ax.annotate(label, (row["stability_cal"], row["apogee_m"]),
                        xytext=offset, textcoords="offset points", fontsize=8,
                        color=color, arrowprops=dict(arrowstyle="-", color=color, lw=0.8))
        ax.axvline(1.5, color="#777777", ls="--", lw=1)
        ax.set(title=motor, xlabel="Minimum ascent stability (calibers)")
        ax.grid(alpha=0.25)
    axes[0].set_ylabel("Apogee at 4 m/s wind (m)")
    legend = [Line2D([0], [0], marker="o", color="none", markerfacecolor=color,
                     markeredgecolor="none", label=shape, markersize=7)
              for shape, color in COLORS.items()]
    legend += [Line2D([0], [0], marker=marker, color="none", markerfacecolor="#777777",
                      label=f"{body:g} mm body", markersize=7)
               for body, marker in MARKERS.items()]
    legend.append(Line2D([0], [0], marker="o", color="none", markerfacecolor="#c9cdd0",
                         label="below 1.5 cal or other screen target", markersize=7))
    fig.legend(handles=legend, loc="lower center", ncol=7, fontsize=8,
               bbox_to_anchor=(0.5, 0.005))
    fig.suptitle("Nominal passive payload: altitude versus stability")
    fig.text(0.5, 0.08, "Gray points miss a comparison target. Geometry and masses remain provisional; not flight clearance.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.15, 1, 0.95))
    fig.savefig(output, metadata={"Date": None})
    fig.savefig(output.with_suffix(".png"), dpi=160)
    plt.close(fig)


def nose_span_map(rows: list[dict], output: Path) -> None:
    """E12 apogee at each geometry, with symbols for insufficient stability."""
    fig, axes = plt.subplots(3, 3, figsize=(11.5, 9.8), sharex=True, sharey=True)
    e_rows = [row for row in rows if row["motor"] == "E12-6"]
    lo = min(row["apogee_m"] for row in e_rows)
    hi = max(row["apogee_m"] for row in e_rows)
    image = None
    for i, body in enumerate(BODIES):
        for j, shape in enumerate(SHAPES):
            ax = axes[i, j]
            lookup = {(row["nose_mm"], row["span_mm"]): row for row in e_rows
                      if row["body_mm"] == body and row["nose_shape"] == shape}
            values = [[lookup[(nose, span)]["apogee_m"] for nose in NOSES] for span in SPANS]
            image = ax.imshow(values, origin="lower", cmap="viridis", vmin=lo, vmax=hi,
                              aspect="auto")
            for yi, span in enumerate(SPANS):
                for xi, nose in enumerate(NOSES):
                    row = lookup[(nose, span)]
                    if row["stability_cal"] < 1.5:
                        ax.text(xi, yi, "×", ha="center", va="center", fontsize=16,
                                color="white", fontweight="bold")
            if i == 0:
                ax.set_title(shape.title())
            if j == 0:
                ax.set_ylabel(f"{body:g} mm body\nFin span (mm)")
            ax.set_xticks(range(len(NOSES)), [f"{nose:g}" for nose in NOSES])
            ax.set_yticks(range(len(SPANS)), [f"{span:.2f}".rstrip("0").rstrip(".") for span in SPANS])
            if i == 2:
                ax.set_xlabel("Nose length (mm)")
    colorbar_axis = fig.add_axes((0.89, 0.14, 0.022, 0.73))
    fig.colorbar(image, cax=colorbar_axis, label="E12-6 apogee at 4 m/s wind (m)")
    fig.suptitle("E12-6 geometry grid — × indicates <1.5 cal stability", y=0.995)
    fig.text(0.5, 0.01, "Current print: 500 mm body, 50 mm conical nose, 53.65 mm fin span. Stability is a target, not a flight clearance.",
             ha="center", fontsize=8)
    fig.subplots_adjust(left=0.09, right=0.87, top=0.93, bottom=0.09, wspace=0.12, hspace=0.15)
    fig.savefig(output, metadata={"Date": None})
    fig.savefig(output.with_suffix(".png"), dpi=160)
    plt.close(fig)


def c11_mass_screen(rows: list[dict], anchor_path: Path, output: Path) -> float:
    """Transfer the verified C11-D12 motor mass delta across identical dry designs."""
    anchors = json.loads(anchor_path.read_text())
    if len(anchors) != 1:
        raise ValueError("C11 anchor must have exactly one direct mass calculation")
    anchor = anchors[0]
    match = next(row for row in rows if row["body_mm"] == anchor["body_mm"]
                 and row["nose_mm"] == anchor["nose_mm"]
                 and row["nose_shape"] == anchor["nose_shape"]
                 and row["span_mm"] == anchor["span_mm"]
                 and row["motor"] == "D12-5")
    if abs(anchor["dry_mass_g"] - match["dry_mass_g"]) > 1e-6:
        raise ValueError("C11 and D12 anchor dry masses differ; cannot transfer motor mass")
    if anchor["motor_liftoff_limit_g"] != 170 or not anchor["status"].startswith("excluded"):
        raise ValueError("Unexpected C11 direct anchor outcome")
    delta = match["launch_mass_g"] - anchor["launch_mass_g"]
    c_rows = []
    for row in rows:
        if row["motor"] != "D12-5":
            continue
        c_rows.append({
            "body_mm": row["body_mm"], "nose_mm": row["nose_mm"],
            "nose_shape": row["nose_shape"], "span_mm": row["span_mm"],
            "inferred_c11_launch_mass_g": row["launch_mass_g"] - delta,
            "manufacturer_limit_g": anchor["motor_liftoff_limit_g"],
            "within_limit": row["launch_mass_g"] - delta <= anchor["motor_liftoff_limit_g"],
        })
    if len(c_rows) != 180 or any(row["within_limit"] for row in c_rows):
        raise ValueError("C11 mass exclusion does not cover the complete nominal geometry grid")
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=c_rows[0].keys())
        writer.writeheader()
        writer.writerows(c_rows)
    return min(row["inferred_c11_launch_mass_g"] for row in c_rows)


def sensitivity(upper: Path, finish5: Path, output: Path) -> list[dict]:
    fields = ("finish_allowance_g",) + FIELDS
    rows = []
    for finish, path in ((3, upper), (5, finish5)):
        for row in json.loads(path.read_text()):
            if row["status"] != "completed":
                raise ValueError(f"Incomplete upper-mass case in {path}")
            rows.append(dict(row, finish_allowance_g=finish))
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def robustness(rows: list[dict], output: Path) -> None:
    """Show the two margins that matter most for finished, current-span builds."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.7))
    cases = ((50.0, "conical", "current 50 mm cone", "#111111"),
             (40.0, "ogive", "40 mm ogive candidate", "#b78300"))
    for nose, shape, label, color in cases:
        relevant = [row for row in rows if row["body_mm"] == 500
                    and row["nose_mm"] == nose and row["nose_shape"] == shape]
        x = (3, 5)
        e_max = [max(row["deployment_m_s"] for row in relevant
                     if row["finish_allowance_g"] == finish and row["motor"] == "E12-6")
                 for finish in x]
        d_min = [min(row["guide_m_s"] for row in relevant
                     if row["finish_allowance_g"] == finish and row["motor"] == "D12-5")
                 for finish in x]
        axes[0].plot(x, e_max, "o-", color=color, label=label)
        axes[1].plot(x, d_min, "o-", color=color, label=label)
    axes[0].axhline(10, ls="--", color="#888888", label="10 m/s screen limit")
    axes[1].axhline(12, ls="--", color="#888888", label="12 m/s screen limit")
    axes[0].set(title="E12-6: fastest deployment", ylabel="Deployment speed (m/s)")
    axes[1].set(title="D12-5: slowest rod departure", ylabel="Guide departure speed (m/s)")
    for ax in axes:
        ax.set(xlabel="Provisional collar finish allowance (g)", xticks=[3, 5])
        ax.grid(alpha=0.25)
        ax.legend(fontsize=8)
    fig.suptitle("Upper other-mass estimate, 0/2/4 m/s winds; 500 mm body, current fin collar")
    fig.text(0.5, 0.015, "These are narrow modeled margins. Actual assembly mass/CG, chute behavior and effective guide travel remain unverified.",
             ha="center", fontsize=8)
    fig.tight_layout(rect=(0, 0.06, 1, 0.92))
    fig.savefig(output, metadata={"Date": None})
    fig.savefig(output.with_suffix(".png"), dpi=160)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grid", type=Path, nargs="+", required=True,
                        help="One or more comparison JSON files covering the complete nominal grid")
    parser.add_argument("--upper", type=Path, required=True)
    parser.add_argument("--finish5", type=Path, required=True)
    parser.add_argument("--c11-anchor", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = load_grid(args.grid)
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "nominal-grid.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    c_min = c11_mass_screen(rows, args.c11_anchor, args.output / "c11-mass-screen.csv")
    upper_rows = sensitivity(args.upper, args.finish5,
                             args.output / "upper-mass-sensitivity.csv")
    root_rows = json.loads(args.root.read_text())
    if len(root_rows) != 6 or any(row["status"] != "completed" for row in root_rows):
        raise ValueError("Root-chord sensitivity must contain six completed cases")
    with (args.output / "root-chord-sensitivity.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(root_rows)
    (args.output / "provenance.json").write_text(json.dumps({
        "inputs": [{"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                   for path in (*args.grid, args.upper, args.finish5, args.c11_anchor, args.root)],
        "rows": len(rows), "wind_m_s": 4,
        "c11_mass_delta_method": "D12-5 model mass minus direct C11-3 model mass at identical geometry and dry mass",
        "minimum_inferred_c11_launch_mass_g": c_min,
        "interpretation": "Nominal actual-logger OpenRocket screen; not flight clearance",
    }, indent=2) + "\n")
    tradeoff(rows, args.output / "altitude-stability.svg")
    nose_profiles(args.output / "nose-profiles.svg")
    nose_span_map(rows, args.output / "e12-geometry-map.svg")
    robustness(upper_rows, args.output / "finished-mass-margins.svg")
    print(f"Published {len(rows)} D/E cases to {args.output}")


if __name__ == "__main__":
    main()
