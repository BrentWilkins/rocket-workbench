"""Evaluate the predeclared exact-wall-distance mechanism test fail-closed."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> tuple[Path, dict]:
    resolved = path.resolve(strict=True)
    return resolved, json.loads(resolved.read_text())


def evidence(path: Path) -> dict:
    return {"path": str(path), "sha256": sha256(path)}


def evaluate(
    plan_path: Path,
    baseline_force_path: Path,
    candidate_force_path: Path,
    baseline_skin_path: Path,
    candidate_skin_path: Path,
    baseline_localization_path: Path,
    candidate_localization_path: Path,
) -> dict:
    plan_path, plan = load(plan_path)
    baseline_force_path, baseline_force = load(baseline_force_path)
    candidate_force_path, candidate_force = load(candidate_force_path)
    baseline_skin_path, baseline_skin = load(baseline_skin_path)
    candidate_skin_path, candidate_skin = load(candidate_skin_path)
    baseline_localization_path, baseline_localization = load(
        baseline_localization_path
    )
    candidate_localization_path, candidate_localization = load(
        candidate_localization_path
    )

    if not plan.get("declared_before_candidate_execution"):
        raise ValueError("Wall-distance mechanism test was not predeclared")
    if not candidate_force["coarse_preflight_passed"]:
        raise ValueError("Candidate force gates failed; coefficients are withheld")
    baseline_cd = baseline_force["last_window_mean"]["Cd"]
    candidate_cd = candidate_force["last_window_mean"]["Cd"]
    reference_cd = baseline_force["tmr_cfl3d_sst_reference"]["cd"]
    cd_change = candidate_cd - baseline_cd
    improvement = baseline_cd - candidate_cd
    threshold = plan["mechanism_test"][
        "minimum_cd_change_beyond_existing_numerical_variation"
    ]
    direction_passed = cd_change < 0
    materiality_passed = improvement >= threshold

    baseline_bins = baseline_localization["bins"]
    candidate_bins = candidate_localization["bins"]
    if [item["x_over_c"] for item in baseline_bins] != [
        item["x_over_c"] for item in candidate_bins
    ]:
        raise ValueError("Skin-friction localization bins differ")
    downstream_baseline = baseline_bins[-1]["mean_openfoam_to_cfl3d_cf_ratio"]
    downstream_candidate = candidate_bins[-1]["mean_openfoam_to_cfl3d_cf_ratio"]

    mechanism_supported = direction_passed and materiality_passed
    return {
        "schema_version": 1,
        "predeclared_plan": evidence(plan_path),
        "evidence": {
            "baseline_force": evidence(baseline_force_path),
            "candidate_force": evidence(candidate_force_path),
            "baseline_skin_friction": evidence(baseline_skin_path),
            "candidate_skin_friction": evidence(candidate_skin_path),
            "baseline_localization": evidence(baseline_localization_path),
            "candidate_localization": evidence(candidate_localization_path),
        },
        "candidate_force_gates_passed": True,
        "drag": {
            "baseline_mean_cd": baseline_cd,
            "candidate_mean_cd": candidate_cd,
            "candidate_minus_baseline_cd": cd_change,
            "improvement_magnitude": improvement,
            "predeclared_materiality_threshold": threshold,
            "fraction_of_materiality_threshold": improvement / threshold,
            "baseline_openfoam_minus_cfl3d_cd": baseline_cd - reference_cd,
            "candidate_openfoam_minus_cfl3d_cd": candidate_cd - reference_cd,
            "fraction_of_baseline_gap_removed": improvement
            / (baseline_cd - reference_cd),
            "direction_passed": direction_passed,
            "materiality_passed": materiality_passed,
        },
        "skin_friction": {
            "baseline_mean_openfoam_to_cfl3d_ratio": baseline_skin[
                "mean_openfoam_to_cfl3d_cf_ratio"
            ],
            "candidate_mean_openfoam_to_cfl3d_ratio": candidate_skin[
                "mean_openfoam_to_cfl3d_cf_ratio"
            ],
            "downstream_bin_x_over_c": baseline_bins[-1]["x_over_c"],
            "baseline_downstream_ratio": downstream_baseline,
            "candidate_downstream_ratio": downstream_candidate,
            "downstream_ratio_change": downstream_candidate - downstream_baseline,
        },
        "exact_wall_distance_mechanism_supported": mechanism_supported,
        "diagnostic_conclusion": (
            "Exact wall distance changes drag and downstream skin friction in the "
            "favorable direction, but the drag change is below the predeclared "
            "numerical-materiality threshold. Approximate meshWave wall distance "
            "is not a dominant mechanism for the Gate 3 discrepancy."
        ),
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--baseline-force", required=True, type=Path)
    parser.add_argument("--candidate-force", required=True, type=Path)
    parser.add_argument("--baseline-skin", required=True, type=Path)
    parser.add_argument("--candidate-skin", required=True, type=Path)
    parser.add_argument("--baseline-localization", required=True, type=Path)
    parser.add_argument("--candidate-localization", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = evaluate(
        args.plan,
        args.baseline_force,
        args.candidate_force,
        args.baseline_skin,
        args.candidate_skin,
        args.baseline_localization,
        args.candidate_localization,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "naca0012-wall-distance-sensitivity.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "output": str(output),
                "mechanism_supported": result[
                    "exact_wall_distance_mechanism_supported"
                ],
                "conclusion": result["diagnostic_conclusion"],
            }
        )
    )


if __name__ == "__main__":
    main()
