"""Localize documented-SA pressure and skin-friction differences from NASA CFL3D."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import vector_list
from cfd_naca0012_case import archive_grid


CP_SHA256 = "2f1231eba6a7da0e988a6954ac34f2f420ff59a5e24fca331110f980cd881dd2"
CF_SHA256 = "e7372151e535d3f89c2eb8b8260a1e69e6b6681bb33aacdd677967ad5403ba5e"
GRID_SHA256 = "b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def numeric_pairs_before_next_zone(path: Path) -> np.ndarray:
    text = path.read_text()
    first_zone = re.search(r"(?im)^zone[^\n]*\n", text)
    if first_zone is None:
        raise ValueError(f"No data zone in {path}")
    remainder = text[first_zone.end() :]
    next_zone = re.search(r"(?im)^zone[^\n]*$", remainder)
    if next_zone is not None:
        remainder = remainder[: next_zone.start()]
    pairs = []
    for line in remainder.splitlines():
        values = line.split()
        if len(values) == 2:
            try:
                pairs.append((float(values[0]), float(values[1])))
            except ValueError:
                continue
    result = np.asarray(pairs)
    if result.ndim != 2 or result.shape[1] != 2:
        raise ValueError(f"Unexpected reference data in {path}")
    return result


def internal_scalar_values(path: Path) -> np.ndarray:
    match = re.search(
        r"internalField\s+nonuniform\s+List<scalar>\s+(\d+)\s*\((.*?)\)\s*;",
        path.read_text(),
        re.DOTALL,
    )
    if match is None:
        raise ValueError(f"No nonuniform internal scalar values in {path}")
    values = np.fromstring(match.group(2), sep=" ")
    if values.size != int(match.group(1)):
        raise ValueError(f"Internal scalar count mismatch in {path}")
    return values


def profile_error(x: np.ndarray, values: np.ndarray, reference: np.ndarray) -> dict:
    order = np.argsort(reference[:, 0])
    ref = np.interp(x, reference[order, 0], reference[order, 1])
    keep = (x >= 0.01) & (x <= 0.98)
    error = values[keep] - ref[keep]
    return {
        "comparison_points": int(keep.sum()),
        "mean_signed_difference": float(error.mean()),
        "rms_difference": float(np.sqrt(np.mean(error**2))),
        "maximum_absolute_difference": float(np.max(np.abs(error))),
        "mean_openfoam": float(values[keep].mean()),
        "mean_reference": float(ref[keep].mean()),
    }


def drag_components(case: Path, window: int = 100) -> dict:
    execution = json.loads((case / "execution.json").read_text())
    matches = [
        (index, stage)
        for index, stage in enumerate(execution)
        if "simpleFoam" in stage.get("stage", "")
    ]
    if len(matches) != 1:
        raise ValueError("Expected exactly one simpleFoam execution stage")
    index, stage = matches[0]
    log_path = case / f"{index}-{stage['stage'].split()[0]}.log"
    rows = np.asarray(
        [
            tuple(float(value) for value in match)
            for match in re.findall(
                r"(?m)^\s*Cd:\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+"
                r"([0-9.eE+-]+)\s+([0-9.eE+-]+)\s*$",
                log_path.read_text(),
            )
        ]
    )
    if rows.shape[0] < window or rows.shape[1] != 4:
        raise ValueError("Insufficient force-component history")
    mean = rows[-window:].mean(axis=0)
    return {
        "log": str(log_path),
        "log_sha256": sha256(log_path),
        "window": window,
        "last_window_mean": {
            name: float(value)
            for name, value in zip(
                ("total", "pressure", "viscous", "internal"), mean, strict=True
            )
        },
    }


def audit(
    case: Path,
    force_audit: Path,
    shear_output: Path,
    benchmark_data: Path,
) -> dict:
    case = case.resolve(strict=True)
    force_audit = force_audit.resolve(strict=True)
    shear_output = shear_output.resolve(strict=True)
    benchmark_data = benchmark_data.resolve(strict=True)
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    forces = json.loads(force_audit.read_text())
    shear_execution_path = shear_output / "execution.json"
    shear_execution = json.loads(shear_execution_path.read_text())

    if Path(forces["case"]).resolve() != case:
        raise ValueError("Force audit belongs to a different case")
    if Path(shear_execution["case"]).resolve() != case:
        raise ValueError("Wall-shear output belongs to a different case")
    if not shear_execution.get("stage_passed"):
        raise ValueError("Wall-shear post-processing did not pass")
    if shear_execution["case_spec_sha256"] != sha256(spec_path):
        raise ValueError("Wall-shear source specification hash mismatch")

    cp_path = benchmark_data / "n0012cp_cfl3d_sa.dat"
    cf_path = benchmark_data / "n0012cf_cfl3d_sa.dat"
    grid_path = benchmark_data / "naca0012-grids.zip"
    expected = ((cp_path, CP_SHA256), (cf_path, CF_SHA256), (grid_path, GRID_SHA256))
    for path, digest in expected:
        if sha256(path) != digest:
            raise ValueError(f"Benchmark SHA-256 mismatch: {path.name}")

    x_grid, y_grid, grid_provenance = archive_grid(grid_path, 897)
    wall_start = 3 * (897 - 1) // 14
    wall_end = 897 - 1 - wall_start
    x_wall = 0.5 * (
        x_grid[0, wall_start:wall_end] + x_grid[0, wall_start + 1 : wall_end + 1]
    )
    y_wall = 0.5 * (
        y_grid[0, wall_start:wall_end] + y_grid[0, wall_start + 1 : wall_end + 1]
    )

    source_time = float(shear_execution["source_time"])
    final_time = str(int(source_time)) if source_time.is_integer() else str(source_time)
    pressure_internal = internal_scalar_values(case / final_time / "p")
    pressure = pressure_internal[wall_start:wall_end]
    shear = vector_list((shear_output / "wallShearStress").read_text(), "airfoil")
    if pressure.size != 512 or shear.shape != (512, 3):
        raise ValueError("Expected 512 pressure and wall-shear values")
    speed = float(spec["conditions"]["speed_m_s"])
    dynamic_pressure_kinematic = 0.5 * speed**2
    cp = pressure / dynamic_pressure_kinematic
    cf = np.linalg.norm(shear[:, :2], axis=1) / dynamic_pressure_kinematic

    cp_reference = numeric_pairs_before_next_zone(cp_path)
    cf_reference = numeric_pairs_before_next_zone(cf_path)
    if cp_reference.shape != (513, 2) or cf_reference.shape != (255, 2):
        raise ValueError("Unexpected NASA SA alpha-zero reference shape")

    lower = slice(0, 256)
    upper = slice(256, 512)
    pressure_result = {
        "lower_surface": profile_error(x_wall[lower], cp[lower], cp_reference),
        "upper_surface": profile_error(x_wall[upper], cp[upper], cp_reference),
    }
    friction_result = profile_error(x_wall[upper], cf[upper], cf_reference)
    dx_wall = np.diff(x_grid[0, wall_start : wall_end + 1])
    dy_wall = np.diff(y_grid[0, wall_start : wall_end + 1])
    ds_wall = np.hypot(dx_wall, dy_wall)
    cp_order = np.argsort(cp_reference[:, 0])
    nasa_cp_on_faces = np.interp(
        x_wall, cp_reference[cp_order, 0], cp_reference[cp_order, 1]
    )
    cf_order = np.argsort(cf_reference[:, 0])
    nasa_viscous_cd = 2.0 * np.trapezoid(
        cf_reference[cf_order, 1], cf_reference[cf_order, 0]
    )
    nasa_pressure_cd = float(np.sum(nasa_cp_on_faces * dy_wall))
    openfoam_pressure_cd = float(np.sum(cp * dy_wall))
    openfoam_viscous_cd = float(
        np.sum(-shear[:, 0] * ds_wall) / dynamic_pressure_kinematic
    )
    reference_total_cd = float(spec["reference"]["alpha_0_cd"])

    return {
        "scope": "Diagnostic alpha-zero Cp and Cf localization for documented-SA control",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "force_audit": str(force_audit),
        "force_audit_sha256": sha256(force_audit),
        "force_gate_1_passed": bool(forces.get("gate_1_passed")),
        "wall_shear_execution": str(shear_execution_path),
        "wall_shear_execution_sha256": sha256(shear_execution_path),
        "wall_shear_field_sha256": sha256(shear_output / "wallShearStress"),
        "references": {
            "cp": {"path": str(cp_path), "sha256": CP_SHA256},
            "cf": {"path": str(cf_path), "sha256": CF_SHA256},
            "grid": {"path": str(grid_path), "sha256": GRID_SHA256},
        },
        "grid_member": grid_provenance,
        "comparison_region_x_over_c": [0.01, 0.98],
        "wall_center_y_symmetry_max_abs": float(
            np.max(np.abs(y_wall[:256] + y_wall[:255:-1]))
        ),
        "pressure_coefficient": pressure_result,
        "skin_friction_coefficient_upper_surface": friction_result,
        "integrated_drag_localization": {
            "openfoam_final": {
                "pressure_cd": openfoam_pressure_cd,
                "viscous_cd": openfoam_viscous_cd,
                "total_cd": openfoam_pressure_cd + openfoam_viscous_cd,
            },
            "nasa_cfl3d_reconstructed_from_profiles": {
                "pressure_cd": nasa_pressure_cd,
                "viscous_cd": nasa_viscous_cd,
                "total_cd": nasa_pressure_cd + nasa_viscous_cd,
            },
            "nasa_cfl3d_tabulated_total_cd": reference_total_cd,
            "openfoam_minus_nasa_profile_components": {
                "pressure_cd": openfoam_pressure_cd - nasa_pressure_cd,
                "viscous_cd": openfoam_viscous_cd - nasa_viscous_cd,
                "total_cd": (
                    openfoam_pressure_cd
                    + openfoam_viscous_cd
                    - reference_total_cd
                ),
            },
            "method": (
                "Pressure integrates Cp*dy on the identical closed airfoil grid; "
                "viscous OpenFOAM drag integrates wallShearStress_x*ds and NASA "
                "drag integrates the symmetric upper-surface Cf profile twice."
            ),
        },
        "drag_components": drag_components(case),
        "comparison_status": "diagnostic_not_acceptance",
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--force-audit", required=True, type=Path)
    parser.add_argument("--shear-output", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(
        args.case, args.force_audit, args.shear_output, args.benchmark_data
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-sa-profile-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
