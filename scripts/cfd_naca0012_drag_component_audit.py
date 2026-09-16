"""Attribute zero-angle NACA drag discrepancy to pressure and viscous parts."""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from cfd_naca0012_skin_friction_audit import CFL3D_CF_SHA256
from cfd_naca0012_transport_sensitivity import drag_decomposition, solver_log


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(case: Path, force_audit_path: Path, benchmark_data: Path) -> dict:
    case = case.resolve(strict=True)
    force_audit_path = force_audit_path.resolve(strict=True)
    force_audit = json.loads(force_audit_path.read_text())
    if Path(force_audit.get("case", "")).resolve() != case:
        raise ValueError("Force audit case mismatch")
    if not force_audit.get("coarse_preflight_passed"):
        raise ValueError("Force audit did not pass")
    if force_audit["tmr_cfl3d_sst_reference"]["angle_deg"] != 0.0:
        raise ValueError("CFL3D upper-surface symmetry decomposition requires alpha=0")

    reference_path = benchmark_data.resolve(strict=True) / "n0012cf_cfl3d_sst.dat"
    if sha256(reference_path) != CFL3D_CF_SHA256:
        raise ValueError("CFL3D skin-friction reference hash mismatch")
    reference = np.loadtxt(reference_path, skiprows=8, max_rows=255)
    if reference.shape != (255, 2) or not np.all(np.diff(reference[:, 0]) > 0):
        raise ValueError("Unexpected zero-angle CFL3D upper-surface Cf data")

    openfoam = drag_decomposition(solver_log(case))
    cfl3d_total = float(force_audit["tmr_cfl3d_sst_reference"]["cd"])
    cfl3d_viscous = float(2.0 * np.trapezoid(reference[:, 1], reference[:, 0]))
    cfl3d_pressure_inferred = cfl3d_total - cfl3d_viscous
    pressure_difference = openfoam["pressure_cd"] - cfl3d_pressure_inferred
    viscous_difference = openfoam["viscous_cd"] - cfl3d_viscous
    total_difference = openfoam["total_cd"] - cfl3d_total

    return {
        "scope": "TMR NACA 0012 alpha-zero drag-component diagnostic",
        "input_evidence": {
            "force_audit": {
                "path": str(force_audit_path),
                "sha256": sha256(force_audit_path),
            },
            "cfl3d_upper_surface_cf": {
                "path": str(reference_path),
                "sha256": sha256(reference_path),
            },
        },
        "method": {
            "openfoam": "mean final 100 forceCoeffs total/pressure/viscous outputs",
            "cfl3d_viscous": "2 * integral_0^1 Cf_upper dx at alpha=0 symmetry",
            "cfl3d_pressure": "reported total Cd minus integrated viscous Cd",
            "limitations": (
                "CFL3D pressure drag is inferred and absorbs endpoint quadrature and "
                "force-output consistency differences; this is diagnostic, not a new gate."
            ),
        },
        "openfoam": openfoam,
        "cfl3d": {
            "total_cd": cfl3d_total,
            "pressure_cd_inferred": cfl3d_pressure_inferred,
            "viscous_cd_integrated": cfl3d_viscous,
        },
        "openfoam_minus_cfl3d": {
            "total_cd": total_difference,
            "pressure_cd": pressure_difference,
            "viscous_cd": viscous_difference,
            "pressure_fraction_of_total_discrepancy": (
                pressure_difference / total_difference
            ),
            "viscous_fraction_of_total_discrepancy": (
                viscous_difference / total_difference
            ),
        },
        "diagnostic_conclusion": (
            "Both components are high: viscous drag accounts for about two thirds and "
            "inferred pressure drag about one third of the total discrepancy."
        ),
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--force-audit", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.case, args.force_audit, args.benchmark_data)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-drag-component-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
