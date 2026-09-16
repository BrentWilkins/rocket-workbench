"""Quantify NACA 0012 SSTm versus stock k-omega SST sensitivity fail-closed."""

import argparse
import hashlib
import json
from pathlib import Path


COEFFICIENTS = ("Cd", "Cl", "CmPitch")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_run(case: Path, audit_dir: Path) -> dict:
    case = case.resolve(strict=True)
    audit_path = (audit_dir / "naca0012-force-audit.json").resolve(strict=True)
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    audit = json.loads(audit_path.read_text())
    if Path(audit.get("case", "")).resolve() != case:
        raise ValueError("Audit does not identify its case")
    required_gates = (
        "conditions_gate",
        "runtime_and_execution_gate",
        "mapped_initialization_provenance_gate",
        "settling_gate",
        "long_window_trend_gate",
        "solver_residual_gate",
        "zero_angle_symmetry_gate",
        "coarse_preflight_passed",
    )
    if not all(audit.get(key) is True for key in required_gates):
        raise ValueError("Sensitivity input audit did not pass all required gates")
    if not (
        audit.get("model_configuration_gate") is True
        or audit.get("sstm_model_configuration_gate") is True
    ):
        raise ValueError("Sensitivity input model configuration did not pass")
    return {
        "case": case,
        "spec": spec,
        "spec_path": spec_path,
        "audit": audit,
        "audit_path": audit_path,
    }


def study(
    baseline_case: Path,
    baseline_audit: Path,
    candidate_case: Path,
    candidate_audit: Path,
) -> dict:
    baseline = load_run(baseline_case, baseline_audit)
    candidate = load_run(candidate_case, candidate_audit)
    invariant_keys = (
        "benchmark",
        "grid_dimensions",
        "conditions",
        "wall_treatment",
        "convection_scheme",
    )
    mismatch = {
        key: (baseline["spec"].get(key), candidate["spec"].get(key))
        for key in invariant_keys
        if baseline["spec"].get(key) != candidate["spec"].get(key)
    }
    if mismatch:
        raise ValueError(f"Model sensitivity invariants differ: {sorted(mismatch)}")
    baseline_model = baseline["spec"]["model_mapping"]["variant"]
    candidate_model = candidate["spec"]["model_mapping"]["variant"]
    if baseline_model != "tmr-sstm-v2512-source-map":
        raise ValueError("Baseline must use source-mapped TMR SSTm")
    if candidate_model != "openfoam-v2512-komegaSST-default-coefficients":
        raise ValueError("Candidate must use stock OpenFOAM kOmegaSST")

    changes = {}
    for name in COEFFICIENTS:
        baseline_value = baseline["audit"]["last_window_mean"][name]
        candidate_value = candidate["audit"]["last_window_mean"][name]
        signed = candidate_value - baseline_value
        changes[name] = {
            "baseline": baseline_value,
            "candidate": candidate_value,
            "signed_change": signed,
            "absolute_change": abs(signed),
        }
    return {
        "benchmark": baseline["spec"]["benchmark"],
        "grid_dimensions": baseline["spec"]["grid_dimensions"],
        "angle_of_attack_deg": baseline["spec"]["conditions"][
            "angle_of_attack_deg"
        ],
        "baseline": {
            "case": str(baseline["case"]),
            "model": baseline_model,
            "spec_sha256": sha256(baseline["spec_path"]),
            "audit_sha256": sha256(baseline["audit_path"]),
        },
        "candidate": {
            "case": str(candidate["case"]),
            "model": candidate_model,
            "spec_sha256": sha256(candidate["spec_path"]),
            "audit_sha256": sha256(candidate["audit_path"]),
        },
        "coefficient_change": changes,
        "decision_rule": "report_only_no_post_hoc_pass_threshold",
        "turbulence_model_sensitivity_characterized": True,
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
    result = study(
        args.baseline_case,
        args.baseline_audit,
        args.candidate_case,
        args.candidate_audit,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-model-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
