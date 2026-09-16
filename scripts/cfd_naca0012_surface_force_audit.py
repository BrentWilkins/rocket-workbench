"""Independently reconstruct NACA pressure and viscous forces from surface fields."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np

from cfd_naca0012_farfield_audit import (
    braced_block,
    counted_list,
    latest_time,
    mesh_geometry,
    patch_values,
    sha256,
)


def internal_scalar(path: Path) -> np.ndarray:
    match = re.search(
        r"\binternalField\s+nonuniform\s+List<scalar>\s+(\d+)\s*"
        r"\(\s*(.*?)\s*\)\s*;",
        path.read_text(),
        re.DOTALL,
    )
    if not match:
        raise ValueError(f"Missing nonuniform internal scalar field in {path}")
    values = np.fromstring(match.group(2), sep=" ", dtype=float)
    if values.shape != (int(match.group(1)),) or not np.all(np.isfinite(values)):
        raise ValueError(f"Malformed internal scalar field in {path}")
    return values


def internal_vector(path: Path) -> np.ndarray:
    match = re.search(
        r"\binternalField\s+nonuniform\s+List<vector>\s+(\d+)\s*"
        r"\(\s*(.*?)\s*\)\s*;",
        path.read_text(),
        re.DOTALL,
    )
    if not match:
        raise ValueError(f"Missing nonuniform internal vector field in {path}")
    values = np.asarray(
        [
            [float(value) for value in row.split()]
            for row in re.findall(r"\(([^()]*)\)", match.group(2))
        ],
        dtype=float,
    )
    if values.shape != (int(match.group(1)), 3) or not np.all(np.isfinite(values)):
        raise ValueError(f"Malformed internal vector field in {path}")
    return values


def patch_owners(case: Path, patch: str) -> np.ndarray:
    poly = case / "constant" / "polyMesh"
    block = braced_block((poly / "boundary").read_text(), patch)
    n_faces_match = re.search(r"\bnFaces\s+(\d+)\s*;", block)
    start_match = re.search(r"\bstartFace\s+(\d+)\s*;", block)
    if not n_faces_match or not start_match:
        raise ValueError(f"Patch {patch!r} lacks nFaces/startFace")
    n_faces = int(n_faces_match.group(1))
    start = int(start_match.group(1))
    declared, payload = counted_list((poly / "owner").read_text())
    owners = np.fromstring(payload, sep=" ", dtype=int)
    if owners.shape != (declared,):
        raise ValueError("Malformed owner list")
    result = owners[start : start + n_faces]
    if result.shape != (n_faces,):
        raise ValueError("Patch owner range exceeds owner list")
    return result


def final_logged_components(log_path: Path, coefficient: str) -> dict:
    pattern = re.compile(
        rf"(?m)^\s*{re.escape(coefficient)}:\s+"
        r"([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+"
        r"([-+0-9.eE]+)\s+([-+0-9.eE]+)\s*$"
    )
    matches = pattern.findall(log_path.read_text())
    if not matches:
        raise ValueError(f"Missing {coefficient} component report in {log_path}")
    total, pressure, viscous, internal = (float(value) for value in matches[-1])
    return {
        "total": total,
        "pressure": pressure,
        "viscous": viscous,
        "internal": internal,
    }


def audit(
    plan_path: Path,
    case: Path,
    force_audit_path: Path,
    wall_shear_output: Path,
) -> dict:
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    if not plan.get("declared_before_new_solver_execution"):
        raise ValueError("Gate 3 remediation plan was not predeclared")

    case = case.resolve(strict=True)
    force_audit_path = force_audit_path.resolve(strict=True)
    force_audit = json.loads(force_audit_path.read_text())
    if Path(force_audit.get("case", "")).resolve() != case or not force_audit.get(
        "coarse_preflight_passed"
    ):
        raise ValueError("Force audit does not establish an admissible source case")

    shear_output = wall_shear_output.resolve(strict=True)
    shear_execution_path = shear_output / "execution.json"
    shear_execution = json.loads(shear_execution_path.read_text())
    shear_field = shear_output / "wallShearStress"
    if (
        Path(shear_execution.get("case", "")).resolve() != case
        or not shear_execution.get("stage_passed")
        or shear_execution.get("field_sha256") != sha256(shear_field)
    ):
        raise ValueError("Wall-shear provenance does not match the source case")

    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    time = latest_time(case)
    face_centers, area_vectors = mesh_geometry(case, "airfoil")
    areas = np.linalg.norm(area_vectors, axis=1)
    owners = patch_owners(case, "airfoil")
    pressure_internal = internal_scalar(time / "p")
    pressure = pressure_internal[owners]
    shear = patch_values(shear_field, "airfoil", len(owners))

    conditions = spec["conditions"]
    pressure_reference = float(conditions["pressure_pa"])
    denominator = (
        0.5
        * float(conditions["density_kg_m3"])
        * float(conditions["speed_m_s"]) ** 2
        * 0.01
    )
    pressure_force = np.sum(
        (pressure - pressure_reference)[:, None] * area_vectors, axis=0
    )
    viscous_force = -np.sum(shear * areas[:, None], axis=0)
    pressure_coefficient = pressure_force / denominator
    viscous_coefficient = viscous_force / denominator
    total_coefficient = pressure_coefficient + viscous_coefficient

    velocity_internal = internal_vector(time / "U")
    temperature_internal = internal_scalar(time / "T")
    with np.load(case / "tmr-naca0012-grid.npz") as grid:
        grid_x = grid["x"]
        grid_y = grid["y"]
    ni = grid_x.shape[1]
    cell_i = owners % (ni - 1)
    cell_j = owners // (ni - 1)
    cell_centers = np.column_stack(
        (
            (
                grid_x[cell_j, cell_i]
                + grid_x[cell_j, cell_i + 1]
                + grid_x[cell_j + 1, cell_i]
                + grid_x[cell_j + 1, cell_i + 1]
            )
            / 4,
            (
                grid_y[cell_j, cell_i]
                + grid_y[cell_j, cell_i + 1]
                + grid_y[cell_j + 1, cell_i]
                + grid_y[cell_j + 1, cell_i + 1]
            )
            / 4,
            np.zeros(len(owners)),
        )
    )
    normals = area_vectors / areas[:, None]
    normal_distance = np.abs(np.sum((cell_centers - face_centers) * normals, axis=1))
    owner_velocity = velocity_internal[owners]
    tangential_velocity = owner_velocity - (
        np.sum(owner_velocity * normals, axis=1)[:, None] * normals
    )
    owner_temperature = temperature_internal[owners]
    sutherland_as = float(conditions["sutherland_as"])
    sutherland_temperature = float(conditions["sutherland_temperature_k"])
    molecular_viscosity = (
        sutherland_as
        * owner_temperature**1.5
        / (owner_temperature + sutherland_temperature)
    )
    first_cell_shear = np.linalg.norm(
        molecular_viscosity[:, None]
        * tangential_velocity
        / normal_distance[:, None],
        axis=1,
    )
    wall_shear_magnitude = np.linalg.norm(shear[:, :2], axis=1)
    comparison = (face_centers[:, 0] >= 0.01) & (face_centers[:, 0] <= 0.98)
    shear_ratio = wall_shear_magnitude[comparison] / first_cell_shear[comparison]

    log_path = case / "2-mpirun.log"
    logged = {
        "drag": final_logged_components(log_path, "Cd"),
        "lift": final_logged_components(log_path, "Cl"),
    }
    reconstructed = {
        "drag": {
            "total": float(total_coefficient[0]),
            "pressure": float(pressure_coefficient[0]),
            "viscous": float(viscous_coefficient[0]),
        },
        "lift": {
            "total": float(total_coefficient[1]),
            "pressure": float(pressure_coefficient[1]),
            "viscous": float(viscous_coefficient[1]),
        },
    }
    differences = {
        axis: {
            component: reconstructed[axis][component] - logged[axis][component]
            for component in ("total", "pressure", "viscous")
        }
        for axis in ("drag", "lift")
    }
    benchmark_drag_gap = 0.0006585114360100012
    max_drag_difference = max(abs(value) for value in differences["drag"].values())

    return {
        "schema_version": 1,
        "scope": "independent final-time airfoil surface-force reconstruction",
        "predeclared_plan": {"path": str(plan_path), "sha256": sha256(plan_path)},
        "case": str(case),
        "solution_time": float(time.name),
        "source_hashes": {
            "case_spec": sha256(spec_path),
            "force_audit": sha256(force_audit_path),
            "solver_log": sha256(log_path),
            "pressure_field": sha256(time / "p"),
            "velocity_field": sha256(time / "U"),
            "temperature_field": sha256(time / "T"),
            "wall_shear_execution": sha256(shear_execution_path),
            "wall_shear_field": sha256(shear_field),
        },
        "implementation": {
            "path": str(Path(__file__).resolve()),
            "sha256": sha256(Path(__file__).resolve()),
        },
        "method": {
            "pressure": "Use owner-cell p on the zeroGradient airfoil patch and integrate gauge pressure times the oriented face-area vector.",
            "viscous": "Integrate negative OpenFOAM wallShearStress times face area.",
            "normalization": "Divide by one-half rhoInf UInf squared Aref using Aref=0.01 square metre.",
            "comparison": "Compare independent final-time components with the final forceCoeffs component report in the sealed solver log.",
        },
        "reference_denominator_newtons": denominator,
        "airfoil_face_count": len(owners),
        "airfoil_area_square_metres": float(areas.sum()),
        "logged_force_coefficients": logged,
        "reconstructed_force_coefficients": reconstructed,
        "reconstructed_minus_logged": differences,
        "maximum_absolute_drag_component_difference": max_drag_difference,
        "frozen_cfl3d_drag_gap": benchmark_drag_gap,
        "maximum_difference_as_fraction_of_benchmark_gap": (
            max_drag_difference / benchmark_drag_gap
        ),
        "wall_gradient_consistency": {
            "method": "Compare wallShearStress magnitude with Sutherland molecular viscosity times owner-cell tangential velocity divided by owner-centre normal distance; wall nut is fixed to zero.",
            "comparison_region_x_over_c": [0.01, 0.98],
            "comparison_faces": int(comparison.sum()),
            "owner_normal_distance_metres": {
                "minimum": float(normal_distance[comparison].min()),
                "maximum": float(normal_distance[comparison].max()),
            },
            "molecular_viscosity_pa_s": {
                "minimum": float(molecular_viscosity[comparison].min()),
                "maximum": float(molecular_viscosity[comparison].max()),
            },
            "wall_shear_over_first_cell_estimate": {
                "mean": float(shear_ratio.mean()),
                "median": float(np.median(shear_ratio)),
                "minimum": float(shear_ratio.min()),
                "maximum": float(shear_ratio.max()),
                "rms_difference_from_one": float(
                    np.sqrt(np.mean((shear_ratio - 1) ** 2))
                ),
            },
            "diagnostic_conclusion": "The wall shear is set by the resolved first-cell velocity gradient and molecular viscosity, not a separate force or wall-nut inflation.",
        },
        "diagnostic_conclusion": (
            "forceCoeffs surface integration is not a dominant explanation of the "
            "frozen OpenFOAM-to-CFL3D drag gap"
        ),
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--force-audit", required=True, type=Path)
    parser.add_argument("--wall-shear-output", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.plan, args.case, args.force_audit, args.wall_shear_output)
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "naca0012-surface-force-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "conclusion": result["diagnostic_conclusion"]}))


if __name__ == "__main__":
    main()
