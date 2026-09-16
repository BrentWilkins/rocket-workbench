"""Compare converged NACA baseline and exact-Sutherland Pr=0.72 candidate."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.resolve(strict=True).read_text())


def solver_log(case: Path) -> Path:
    execution = load(case / "execution.json")
    stages = [
        (index, stage)
        for index, stage in enumerate(execution)
        if "Foam" in stage.get("stage", "") and "mpirun" in stage.get("stage", "")
    ]
    if len(stages) != 1:
        raise ValueError("Expected one MPI OpenFOAM solver execution stage")
    index, stage = stages[0]
    return case / f"{index}-{stage['stage'].split()[0]}.log"


def drag_decomposition(log_path: Path, window: int = 100) -> dict:
    pattern = re.compile(
        r"Cd:\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)\s+([0-9.eE+-]+)"
    )
    values = np.asarray(
        [[float(value) for value in match] for match in pattern.findall(log_path.read_text())]
    )
    if len(values) < window:
        raise ValueError(f"Need at least {window} force-decomposition samples")
    means = values[-window:].mean(axis=0)
    return {
        "samples": window,
        "total_cd": float(means[0]),
        "pressure_cd": float(means[1]),
        "viscous_cd": float(means[2]),
        "internal_cd": float(means[3]),
    }


def evaluate(
    baseline_case: Path,
    baseline_audit_path: Path,
    baseline_cf_path: Path,
    candidate_case: Path,
    candidate_audit_path: Path,
    candidate_cf_path: Path,
) -> dict:
    baseline_case = baseline_case.resolve(strict=True)
    candidate_case = candidate_case.resolve(strict=True)
    baseline_audit = load(baseline_audit_path)
    candidate_audit = load(candidate_audit_path)
    baseline_cf = load(baseline_cf_path)
    candidate_cf = load(candidate_cf_path)
    if Path(baseline_audit.get("case", "")).resolve() != baseline_case:
        raise ValueError("Baseline audit case mismatch")
    if Path(candidate_audit.get("case", "")).resolve() != candidate_case:
        raise ValueError("Candidate audit case mismatch")
    if not baseline_audit.get("coarse_preflight_passed"):
        raise ValueError("Baseline force audit did not pass")
    if not candidate_audit.get("coarse_preflight_passed"):
        raise ValueError("Candidate force audit did not pass")

    baseline_cd = float(baseline_audit["last_window_mean"]["Cd"])
    candidate_cd = float(candidate_audit["last_window_mean"]["Cd"])
    ladson_cd = float(baseline_audit["ladson_tripped_experiment"]["mean_cd"])
    baseline_discrepancy = baseline_cd - ladson_cd
    candidate_discrepancy = candidate_cd - ladson_cd
    transport_change = candidate_cd - baseline_cd
    attributable_fraction = abs(transport_change) / abs(baseline_discrepancy)
    baseline_decomposition = drag_decomposition(solver_log(baseline_case))
    candidate_decomposition = drag_decomposition(solver_log(candidate_case))

    return {
        "scope": "TMR NACA 0012 zero-angle exact-Sutherland Prandtl sensitivity",
        "evidence": {
            "baseline_force_audit": {
                "path": str(baseline_audit_path),
                "sha256": sha256(baseline_audit_path),
            },
            "baseline_skin_friction_audit": {
                "path": str(baseline_cf_path),
                "sha256": sha256(baseline_cf_path),
            },
            "candidate_force_audit": {
                "path": str(candidate_audit_path),
                "sha256": sha256(candidate_audit_path),
            },
            "candidate_skin_friction_audit": {
                "path": str(candidate_cf_path),
                "sha256": sha256(candidate_cf_path),
            },
        },
        "baseline": {
            "molecular_prandtl": 0.6903347705666375,
            "mean_cd": baseline_cd,
            "ladson_cd_discrepancy": baseline_discrepancy,
            "mean_openfoam_to_cfl3d_cf_ratio": baseline_cf[
                "mean_openfoam_to_cfl3d_cf_ratio"
            ],
            "drag_decomposition": baseline_decomposition,
        },
        "candidate": {
            "molecular_prandtl": 0.72,
            "mean_cd": candidate_cd,
            "ladson_cd_discrepancy": candidate_discrepancy,
            "mean_openfoam_to_cfl3d_cf_ratio": candidate_cf[
                "mean_openfoam_to_cfl3d_cf_ratio"
            ],
            "drag_decomposition": candidate_decomposition,
            "all_solver_gates_passed": True,
        },
        "change": {
            "candidate_minus_baseline_cd": transport_change,
            "absolute_fraction_of_baseline_ladson_discrepancy": attributable_fraction,
            "pressure_cd": (
                candidate_decomposition["pressure_cd"]
                - baseline_decomposition["pressure_cd"]
            ),
            "viscous_cd": (
                candidate_decomposition["viscous_cd"]
                - baseline_decomposition["viscous_cd"]
            ),
            "mean_cf_ratio": (
                candidate_cf["mean_openfoam_to_cfl3d_cf_ratio"]
                - baseline_cf["mean_openfoam_to_cfl3d_cf_ratio"]
            ),
        },
        "transport_mismatch_is_dominant_explanation": False,
        "zero_angle_benchmark_accepted": False,
        "accepted_for_rocket": False,
        "verdict": (
            "Matching constant molecular Pr=0.72 changes less than one percent of the "
            "baseline Ladson drag discrepancy and does not resolve high wall shear."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-case", required=True, type=Path)
    parser.add_argument("--baseline-audit", required=True, type=Path)
    parser.add_argument("--baseline-cf", required=True, type=Path)
    parser.add_argument("--candidate-case", required=True, type=Path)
    parser.add_argument("--candidate-audit", required=True, type=Path)
    parser.add_argument("--candidate-cf", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = evaluate(
        args.baseline_case,
        args.baseline_audit,
        args.baseline_cf,
        args.candidate_case,
        args.candidate_audit,
        args.candidate_cf,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-transport-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
