"""Summarize the documented-SA, ratio-3, and exact standard-SA ladder."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_audit(path: Path) -> tuple[Path, dict, dict]:
    path = path.resolve(strict=True)
    audit = json.loads(path.read_text())
    case = Path(audit["case"]).resolve(strict=True)
    spec_path = case / "benchmark-spec.json"
    if audit["case_spec_sha256"] != sha256(spec_path):
        raise ValueError(f"Audit/specification mismatch: {path}")
    if not all(
        audit.get(key)
        for key in (
            "provenance_gate",
            "restart_provenance_gate",
            "runtime_and_execution_gate",
            "model_configuration_gate",
        )
    ):
        raise ValueError(f"Audit provenance/runtime gate failed: {path}")
    return path, audit, json.loads(spec_path.read_text())


def row(path: Path, audit: dict, label: str) -> dict:
    reference = audit["cfl3d_sa_reference"]
    means = audit["last_window_mean"]
    return {
        "label": label,
        "audit": str(path),
        "audit_sha256": sha256(path),
        "mean": means,
        "openfoam_minus_cfl3d": audit["openfoam_minus_cfl3d"],
        "relative_cd_difference_percent": (
            100.0 * audit["openfoam_minus_cfl3d"]["cd"] / reference["cd"]
        ),
        "final_initial_residuals": audit["solver_initial_residuals_final"],
        "gates": {
            key: audit[key]
            for key in (
                "settling_gate",
                "long_window_trend_gate",
                "solver_residual_gate",
                "zero_angle_symmetry_gate",
                "force_agreement_gate",
                "gate_1_passed",
            )
        },
    }


def compare(baseline_path: Path, ratio_path: Path, standard_path: Path) -> dict:
    baseline_path, baseline, baseline_spec = load_audit(baseline_path)
    ratio_path, ratio, ratio_spec = load_audit(ratio_path)
    standard_path, standard, standard_spec = load_audit(standard_path)
    ratio_mechanism = ratio_spec.get("mechanism_test", {})
    standard_mechanism = standard_spec.get("mechanism_test", {})
    ladder_provenance_gate = (
        ratio_mechanism.get("only_farfield_nuTilda_changed") is True
        and ratio_mechanism.get("before", {}).get("nuTilda_to_nu_ratio") == 4.0
        and ratio_mechanism.get("after", {}).get("nuTilda_to_nu_ratio") == 3.0
        and standard_mechanism.get("only_ft2_switch_changed") is True
        and standard_mechanism.get("before", {}).get("ft2") is False
        and standard_mechanism.get("after", {}).get("ft2") is True
        and standard_mechanism.get("nuTilda_to_nu_ratio") == 3.0
        and Path(ratio_spec["initialization"]["source_case"]).resolve()
        == Path(baseline["case"]).resolve()
        and Path(standard_spec["initialization"]["source_case"]).resolve()
        == Path(ratio["case"]).resolve()
    )
    baseline_row = row(baseline_path, baseline, "documented_ratio4_noft2")
    ratio_row = row(ratio_path, ratio, "ratio3_noft2")
    standard_row = row(standard_path, standard, "ratio3_standard_sa_ft2")
    fields = ("Cd", "Cl", "CmPitch")
    return {
        "scope": "One-change-at-a-time Spalart-Allmaras parity ladder",
        "ladder_provenance_gate": ladder_provenance_gate,
        "variants": [baseline_row, ratio_row, standard_row],
        "one_change_deltas": {
            "ratio3_minus_ratio4_at_noft2": {
                name: ratio["last_window_mean"][name]
                - baseline["last_window_mean"][name]
                for name in fields
            },
            "ft2_true_minus_false_at_ratio3": {
                name: standard["last_window_mean"][name]
                - ratio["last_window_mean"][name]
                for name in fields
            },
        },
        "exact_standard_sa_gate_1_passed": standard["gate_1_passed"],
        "accepted_for_rocket": bool(
            ladder_provenance_gate and standard["gate_1_passed"]
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-audit", required=True, type=Path)
    parser.add_argument("--ratio-audit", required=True, type=Path)
    parser.add_argument("--standard-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = compare(args.baseline_audit, args.ratio_audit, args.standard_audit)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-sa-variant-comparison.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
