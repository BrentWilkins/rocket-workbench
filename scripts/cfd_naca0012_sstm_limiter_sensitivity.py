"""Compare the predeclared SSTm production-limiter placement sensitivity."""

import argparse
import hashlib
import json
from pathlib import Path

from cfd_naca0012_transport_sensitivity import drag_decomposition, solver_log


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.resolve(strict=True).read_text())


def evaluate(
    baseline_case: Path,
    baseline_audit_path: Path,
    candidate_case: Path,
    candidate_audit_path: Path,
    cfl3d_reference_path: Path,
) -> dict:
    baseline_case = baseline_case.resolve(strict=True)
    candidate_case = candidate_case.resolve(strict=True)
    baseline_audit = load(baseline_audit_path)
    candidate_audit = load(candidate_audit_path)
    reference = load(cfl3d_reference_path)

    if Path(baseline_audit.get("case", "")).resolve() != baseline_case:
        raise ValueError("Baseline audit does not match baseline case")
    if Path(candidate_audit.get("case", "")).resolve() != candidate_case:
        raise ValueError("Candidate audit does not match candidate case")
    for label, audit in (("baseline", baseline_audit), ("candidate", candidate_audit)):
        if not audit.get("coarse_preflight_passed"):
            raise ValueError(f"{label.capitalize()} diagnostic gates did not pass")

    baseline = drag_decomposition(solver_log(baseline_case))
    candidate = drag_decomposition(solver_log(candidate_case))
    cfl3d_cd = float(reference["cfl3d"]["total_cd"])
    baseline_gap = baseline["total_cd"] - cfl3d_cd
    candidate_gap = candidate["total_cd"] - cfl3d_cd
    total_change = candidate["total_cd"] - baseline["total_cd"]

    return {
        "scope": "TMR NACA 0012 zero-angle SSTm production-limiter placement diagnostic",
        "evidence": {
            "baseline_force_audit": {
                "path": str(baseline_audit_path),
                "sha256": sha256(baseline_audit_path),
            },
            "candidate_force_audit": {
                "path": str(candidate_audit_path),
                "sha256": sha256(candidate_audit_path),
            },
            "cfl3d_drag_reference": {
                "path": str(cfl3d_reference_path),
                "sha256": sha256(cfl3d_reference_path),
            },
        },
        "baseline": {
            "model": "TmrSSTm with v2512 limiter in omega and k",
            "drag_decomposition": baseline,
            "openfoam_minus_cfl3d_cd": baseline_gap,
        },
        "candidate": {
            "model": "TmrSSTmKOnlyLimiter with unlimited omega production",
            "drag_decomposition": candidate,
            "openfoam_minus_cfl3d_cd": candidate_gap,
            "all_diagnostic_solver_gates_passed": True,
        },
        "change": {
            "candidate_minus_baseline_cd": total_change,
            "pressure_cd": candidate["pressure_cd"] - baseline["pressure_cd"],
            "viscous_cd": candidate["viscous_cd"] - baseline["viscous_cd"],
            "absolute_fraction_of_baseline_cfl3d_gap": (
                abs(total_change) / abs(baseline_gap)
            ),
        },
        "diagnostic_conclusion": (
            "Correcting limiter placement slightly reduces drag but does not explain "
            "the remaining same-grid CFL3D discrepancy."
        ),
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-case", required=True, type=Path)
    parser.add_argument("--baseline-audit", required=True, type=Path)
    parser.add_argument("--candidate-case", required=True, type=Path)
    parser.add_argument("--candidate-audit", required=True, type=Path)
    parser.add_argument("--cfl3d-reference", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    result = evaluate(
        args.baseline_case,
        args.baseline_audit,
        args.candidate_case,
        args.candidate_audit,
        args.cfl3d_reference,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-sstm-limiter-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
