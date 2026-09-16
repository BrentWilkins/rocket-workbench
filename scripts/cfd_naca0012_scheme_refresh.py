"""Audit the predeclared corrected-SSTm fine-grid scheme sensitivity."""

import argparse
import json
import math
from pathlib import Path

from cfd_naca0012_finest_pair_refresh import COEFFICIENTS, load, sha256


def evaluate(
    baseline_case: Path,
    baseline_audit_path: Path,
    candidate_case: Path,
    candidate_audit_path: Path,
) -> dict:
    baseline_spec, baseline_audit = load(baseline_case, baseline_audit_path)
    candidate_spec, candidate_audit = load(candidate_case, candidate_audit_path)

    if baseline_spec.get("grid_dimensions") != [897, 257]:
        raise ValueError("Baseline is not the declared fine grid")
    if candidate_spec.get("grid_dimensions") != [897, 257]:
        raise ValueError("Candidate is not the declared fine grid")
    if baseline_spec.get("convection_scheme") != "linear-upwind-velocity":
        raise ValueError("Baseline is not linear-upwind")
    if candidate_spec.get("convection_scheme") != "lust-blended":
        raise ValueError("Candidate is not LUST")

    for label, spec in (("baseline", baseline_spec), ("candidate", candidate_spec)):
        model = spec.get("model_mapping", {})
        conditions = spec.get("conditions", {})
        if model.get("variant") != "tmr-sstm-exact-production":
            raise ValueError(f"{label} model mismatch")
        if conditions.get("transport_model") != "exact-sutherland-pr072":
            raise ValueError(f"{label} transport mismatch")
        if conditions.get("molecular_prandtl") != 0.72:
            raise ValueError(f"{label} molecular Prandtl mismatch")

    angle = math.radians(float(baseline_spec["conditions"]["angle_of_attack_deg"]))
    limits = {
        "Cd": 0.0002,
        "Cl": 0.004 * abs(math.cos(angle)) + 0.0002 * abs(math.sin(angle)),
        "CmPitch": 0.0002,
    }
    changes = {
        name: {
            "signed_change": (
                candidate_audit["last_window_mean"][name]
                - baseline_audit["last_window_mean"][name]
            ),
            "absolute_change": abs(
                candidate_audit["last_window_mean"][name]
                - baseline_audit["last_window_mean"][name]
            ),
        }
        for name in COEFFICIENTS
    }
    passed = all(changes[name]["absolute_change"] <= limits[name] for name in COEFFICIENTS)

    return {
        "scope": "corrected NASA TMR SSTm fine-grid LUST sensitivity",
        "baseline": {
            "case": str(baseline_case),
            "audit": str(baseline_audit_path),
            "audit_sha256": sha256(baseline_audit_path),
            "scheme": "linear-upwind-velocity",
            "mean": baseline_audit["last_window_mean"],
        },
        "candidate": {
            "case": str(candidate_case),
            "audit": str(candidate_audit_path),
            "audit_sha256": sha256(candidate_audit_path),
            "scheme": "lust-blended",
            "relaxation_scale_from_baseline": 0.5,
            "mean": candidate_audit["last_window_mean"],
        },
        "coefficient_change": changes,
        "absolute_limits_from_experimental_repeatability": limits,
        "scheme_independence_gate": passed,
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-case", required=True, type=Path)
    parser.add_argument("--baseline-audit", required=True, type=Path)
    parser.add_argument("--candidate-case", required=True, type=Path)
    parser.add_argument("--candidate-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    result = evaluate(
        args.baseline_case,
        args.baseline_audit,
        args.candidate_case,
        args.candidate_audit,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-scheme-refresh.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
