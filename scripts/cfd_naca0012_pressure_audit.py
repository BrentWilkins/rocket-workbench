"""Extract wall Cp from a retained TMR NACA 0012 case without mismatching experiments."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np


CFL3D_CP_SHA256 = "378f9dcd058ffbe900081f213ee5c7e24dfaec0d6a9e02f366f96e8d76bf179d"


def final_time(case: Path) -> Path:
    times = [
        (float(path.name), path)
        for path in case.iterdir()
        if path.is_dir() and re.fullmatch(r"\d+(?:\.\d+)?", path.name)
    ]
    if not times:
        raise ValueError("No reconstructed solution time found")
    return max(times)[1]


def internal_scalars(path: Path) -> np.ndarray:
    match = re.search(
        r"internalField\s+nonuniform\s+List<scalar>\s+(\d+)\s*\((.*?)\)\s*;",
        path.read_text(),
        re.DOTALL,
    )
    if not match:
        raise ValueError(f"Cannot parse nonuniform scalar field {path}")
    values = np.fromstring(match.group(2), sep=" ")
    if len(values) != int(match.group(1)):
        raise ValueError(f"Scalar count mismatch in {path}")
    return values


def audit(case: Path, benchmark_data: Path) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    conditions = spec["conditions"]
    grid = np.load(case / "tmr-naca0012-grid.npz")
    x = grid["x"]
    y = grid["y"]
    ni = x.shape[1]
    wake_edges = 3 * (ni - 1) // 14
    wall_start = wake_edges
    wall_end = ni - 1 - wake_edges
    pressure = internal_scalars(final_time(case) / "p")
    if len(pressure) != (x.shape[0] - 1) * (ni - 1):
        raise ValueError("Pressure field and structured-grid cell count differ")
    owners = np.arange(wall_start, wall_end)
    surface_x = 0.5 * (x[0, wall_start:wall_end] + x[0, wall_start + 1:wall_end + 1])
    surface_y = 0.5 * (y[0, wall_start:wall_end] + y[0, wall_start + 1:wall_end + 1])
    p_wall = pressure[owners]
    q_inf = (
        0.5
        * conditions["density_kg_m3"]
        * conditions["speed_m_s"] ** 2
    )
    cp = (p_wall - conditions["pressure_pa"]) / q_inf
    if not np.all(np.isfinite(cp)):
        raise ValueError("Non-finite wall Cp")
    half = len(cp) // 2
    symmetry = None
    if conditions["angle_of_attack_deg"] == 0.0:
        symmetry = {
            "maximum_paired_absolute_cp_difference": float(
                np.max(np.abs(cp[:half] - cp[half:][::-1]))
            ),
            "diagnostic_only": True,
        }
    retained_pressure_files = {
        "CP_Gregory_expdata.dat": "Re=2.88 million; not the M=0.15 Re=6 million force case",
        "CP_Ladson.dat": "M=0.3 and free transition; not the M=0.15 tripped force case",
    }
    missing = [
        name for name in retained_pressure_files
        if not (benchmark_data / name).is_file()
    ]
    if missing:
        raise ValueError(f"Missing retained pressure references: {missing}")
    profile = [
        {
            "x_over_c": float(px),
            "y_over_c": float(py),
            "cp": float(value),
            "surface": "lower" if index < half else "upper",
        }
        for index, (px, py, value) in enumerate(zip(surface_x, surface_y, cp, strict=True))
    ]
    cfl3d_path = benchmark_data / "n0012cp_cfl3d_sst.dat"
    digest = hashlib.sha256(cfl3d_path.read_bytes()).hexdigest()
    if digest != CFL3D_CP_SHA256:
        raise ValueError("CFL3D pressure reference SHA-256 mismatch")
    cfl3d = np.loadtxt(cfl3d_path, skiprows=8, max_rows=513)
    if cfl3d.shape != (513, 2):
        raise ValueError("Unexpected alpha-zero CFL3D pressure zone")
    cfl3d_surfaces = {
        "lower": cfl3d[:257],
        "upper": cfl3d[256:],
    }
    cfl3d_diagnostic = {}
    for name, selector in {
        "lower": np.arange(len(cp)) < half,
        "upper": np.arange(len(cp)) >= half,
    }.items():
        comparison = selector & (surface_x >= 0.01) & (surface_x <= 0.98)
        reference = cfl3d_surfaces[name]
        order = np.argsort(reference[:, 0])
        reference_cp = np.interp(
            surface_x[comparison], reference[order, 0], reference[order, 1]
        )
        error = cp[comparison] - reference_cp
        cfl3d_diagnostic[name] = {
            "comparison_points": int(comparison.sum()),
            "mean_signed_cp_difference": float(error.mean()),
            "rms_cp_difference": float(np.sqrt(np.mean(error**2))),
            "maximum_absolute_cp_difference": float(np.max(np.abs(error))),
        }
    return {
        "case": str(case),
        "solution_time": final_time(case).name,
        "wall_faces": len(cp),
        "cp_minimum": float(cp.min()),
        "cp_maximum": float(cp.max()),
        "zero_angle_paired_symmetry": symmetry,
        "profile": profile,
        "cfl3d_sst_diagnostic": {
            "reference": str(cfl3d_path),
            "reference_sha256": digest,
            "comparison_region_x_over_c": [0.01, 0.98],
            "surfaces": cfl3d_diagnostic,
            "status": "diagnostic_same_grid_and_conditions_not_experimental_acceptance",
        },
        "retained_pressure_data_condition_review": retained_pressure_files,
        "experimental_cp_comparison_performed": False,
        "comparison_status": (
            "withheld_until_separate_cases_match_each_pressure_dataset_condition"
        ),
        "pressure_benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.case, args.benchmark_data)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-pressure-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in result.items()
                if key != "profile"
            }
        )
    )


if __name__ == "__main__":
    main()
