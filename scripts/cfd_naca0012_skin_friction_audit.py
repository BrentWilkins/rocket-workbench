"""Compare sealed OpenFOAM NACA wall shear with hash-pinned CFL3D SST Cf."""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import vector_list


CFL3D_CF_SHA256 = "d8001cd09d0c573de63475f8e0e02a2a989216133af74b84876eba5c328da8be"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(
    case: Path, force_audit: Path, shear_output: Path, benchmark_data: Path
) -> dict:
    case = case.resolve(strict=True)
    force_audit = force_audit.resolve(strict=True)
    shear_output = shear_output.resolve(strict=True)
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    forces = json.loads(force_audit.read_text())
    execution_path = shear_output / "execution.json"
    execution = json.loads(execution_path.read_text())
    field_path = shear_output / "wallShearStress"
    if Path(forces.get("case", "")).resolve() != case or not forces.get(
        "coarse_preflight_passed"
    ):
        raise ValueError("Force audit does not match or pass")
    if (
        Path(execution.get("case", "")).resolve() != case
        or not execution.get("stage_passed")
        or execution.get("case_spec_sha256") != sha256(spec_path)
        or execution.get("field_sha256") != sha256(field_path)
    ):
        raise ValueError("Wall-shear execution provenance did not pass")

    reference_path = benchmark_data.resolve(strict=True) / "n0012cf_cfl3d_sst.dat"
    if sha256(reference_path) != CFL3D_CF_SHA256:
        raise ValueError("CFL3D skin-friction reference SHA-256 mismatch")
    reference = np.loadtxt(reference_path, skiprows=8, max_rows=255)
    if reference.shape != (255, 2) or not np.all(np.diff(reference[:, 0]) > 0):
        raise ValueError("Unexpected alpha-zero CFL3D skin-friction zone")

    with np.load(case / "tmr-naca0012-grid.npz") as data:
        x = data["x"]
        y = data["y"]
    ni = x.shape[1]
    wake_edges = 3 * (ni - 1) // 14
    wall_end = ni - 1 - wake_edges
    x_center = 0.5 * (x[0, wake_edges:wall_end] + x[0, wake_edges + 1 : wall_end + 1])
    y_center = 0.5 * (y[0, wake_edges:wall_end] + y[0, wake_edges + 1 : wall_end + 1])
    shear = vector_list(field_path.read_text(), "airfoil")
    if shear.shape != (len(x_center), 3):
        raise ValueError("Wall-shear patch size does not match airfoil faces")
    conditions = spec["conditions"]
    dynamic_pressure = (
        0.5
        * conditions["density_kg_m3"]
        * conditions["speed_m_s"] ** 2
    )
    cf = np.linalg.norm(shear[:, :2], axis=1) / dynamic_pressure
    upper = y_center > 0
    comparison = upper & (x_center >= 0.01) & (x_center <= 0.98)
    reference_cf = np.interp(x_center[comparison], reference[:, 0], reference[:, 1])
    error = cf[comparison] - reference_cf
    ratio = cf[comparison] / reference_cf
    profile = [
        {
            "x_over_c": float(x_value),
            "openfoam_cf": float(cf_value),
            "cfl3d_cf": float(reference_value),
            "difference": float(error_value),
        }
        for x_value, cf_value, reference_value, error_value in zip(
            x_center[comparison], cf[comparison], reference_cf, error, strict=True
        )
    ]
    return {
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "force_audit": str(force_audit),
        "force_audit_sha256": sha256(force_audit),
        "wall_shear_execution": str(execution_path),
        "wall_shear_execution_sha256": sha256(execution_path),
        "wall_shear_field_sha256": sha256(field_path),
        "cfl3d_reference": str(reference_path),
        "cfl3d_reference_sha256": CFL3D_CF_SHA256,
        "comparison_region_x_over_c": [0.01, 0.98],
        "trailing_edge_exclusion_basis": "CFL3D source warns of high numerical error near the trailing edge",
        "comparison_points": int(comparison.sum()),
        "mean_signed_cf_difference": float(error.mean()),
        "rms_cf_difference": float(np.sqrt(np.mean(error**2))),
        "maximum_absolute_cf_difference": float(np.max(np.abs(error))),
        "mean_openfoam_to_cfl3d_cf_ratio": float(ratio.mean()),
        "profile": profile,
        "diagnostic_conclusion": "OpenFOAM SSTm wall skin friction is systematically higher than CFL3D SST over the retained chord region.",
        "comparison_status": "diagnostic_not_an_experimental_acceptance",
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
    result = audit(args.case, args.force_audit, args.shear_output, args.benchmark_data)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-skin-friction-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
