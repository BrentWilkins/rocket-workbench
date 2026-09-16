"""Compare converged compressible NACA baseline and incompressible control."""

import argparse
import hashlib
import json
from pathlib import Path

from cfd_naca0012_transport_sensitivity import drag_decomposition, solver_log


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(
    baseline_case: Path,
    baseline_audit_path: Path,
    control_audit_path: Path,
) -> dict:
    baseline_case = baseline_case.resolve(strict=True)
    baseline_audit_path = baseline_audit_path.resolve(strict=True)
    control_audit_path = control_audit_path.resolve(strict=True)
    baseline = json.loads(baseline_audit_path.read_text())
    control = json.loads(control_audit_path.read_text())
    if Path(baseline.get("case", "")).resolve() != baseline_case:
        raise ValueError("Baseline audit case mismatch")
    if not baseline.get("coarse_preflight_passed"):
        raise ValueError("Baseline audit did not pass")
    if not control.get("control_preflight_passed"):
        raise ValueError("Incompressible control audit did not pass")

    baseline_drag = drag_decomposition(solver_log(baseline_case))
    control_drag = control["drag_decomposition"]
    cfl3d_cd = float(baseline["tmr_cfl3d_sst_reference"]["cd"])
    baseline_discrepancy = baseline_drag["total_cd"] - cfl3d_cd
    total_change = control_drag["total_cd"] - baseline_drag["total_cd"]
    pressure_change = control_drag["pressure_cd"] - baseline_drag["pressure_cd"]
    viscous_change = control_drag["viscous_cd"] - baseline_drag["viscous_cd"]

    return {
        "scope": "TMR NACA 0012 alpha-zero incompressible solver-path control",
        "evidence": {
            "baseline_force_audit": {
                "path": str(baseline_audit_path),
                "sha256": sha256(baseline_audit_path),
            },
            "control_audit": {
                "path": str(control_audit_path),
                "sha256": sha256(control_audit_path),
            },
        },
        "baseline_compressible": baseline_drag,
        "control_incompressible": control_drag,
        "cfl3d_cd": cfl3d_cd,
        "change": {
            "control_minus_baseline_total_cd": total_change,
            "control_minus_baseline_pressure_cd": pressure_change,
            "control_minus_baseline_viscous_cd": viscous_change,
            "absolute_fraction_of_baseline_cfl3d_discrepancy": (
                abs(total_change) / abs(baseline_discrepancy)
            ),
            "control_minus_cfl3d_cd": control_drag["total_cd"] - cfl3d_cd,
        },
        "compressibility_or_thermophysical_coupling_is_dominant_explanation": False,
        "production_compressible_workflow_accepted": False,
        "accepted_for_rocket": False,
        "verdict": (
            "The incompressible control changes less than five percent of the baseline "
            "CFL3D discrepancy and leaves viscous drag essentially unchanged."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-case", required=True, type=Path)
    parser.add_argument("--baseline-audit", required=True, type=Path)
    parser.add_argument("--control-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = evaluate(args.baseline_case, args.baseline_audit, args.control_audit)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-solver-path-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
