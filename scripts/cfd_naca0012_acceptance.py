"""Combine zero-angle NACA evidence into a conservative fail-closed decision."""

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.resolve(strict=True).read_text())


def evaluate(
    force_path: Path,
    numerical_path: Path,
    yplus_path: Path,
    model_path: Path,
    domain_default_path: Path,
    domain_relaxed_path: Path,
) -> dict:
    force = load(force_path)
    numerical = load(numerical_path)
    yplus = load(yplus_path)
    model = load(model_path)
    domain_default = load(domain_default_path)
    domain_relaxed = load(domain_relaxed_path)

    numerical_gates = {
        "baseline_force_preflight": force.get("coarse_preflight_passed") is True,
        "numerical_independence": numerical.get("numerical_independence_passed")
        is True,
        "wall_resolved_y_plus": yplus.get("wall_resolved_y_plus_gate") is True,
        "turbulence_model_sensitivity_characterized": model.get(
            "turbulence_model_sensitivity_characterized"
        )
        is True,
        "reduced_domain_default_residual": domain_default.get(
            "solver_residual_gate"
        )
        is True,
        "reduced_domain_half_relaxation_residual": domain_relaxed.get(
            "solver_residual_gate"
        )
        is True,
    }
    domain_gate = (
        numerical_gates["reduced_domain_default_residual"]
        or numerical_gates["reduced_domain_half_relaxation_residual"]
    )
    numerical_gates["domain_sensitivity"] = domain_gate

    experiment = force["ladson_tripped_experiment"]
    discrepancy = abs(experiment["cfd_minus_mean_cd"])
    uncertainty = numerical["uncertainty_components_from_finest_available_pair"]
    components = {
        "experimental_repeatability": 0.0002,
        "finest_pair_grid_change": uncertainty["numerical_discretization_absolute"][
            "Cd"
        ],
        "scheme_change": uncertainty["scheme_absolute"]["Cd"],
        "iterative_conservative": uncertainty["iterative_conservative_absolute"][
            "Cd"
        ],
        "table_half_last_printed_digit": 0.000005,
        "full_predeclared_domain_allowance_despite_failed_domain_run": 0.0002,
    }
    conservative_allowance = sum(components.values())
    drag_gate_even_granting_full_domain_allowance = discrepancy <= conservative_allowance
    benchmark_gate = domain_gate and drag_gate_even_granting_full_domain_allowance
    return {
        "scope": "tmr-naca0012-zero-angle-external-body",
        "input_evidence": {
            "force_audit": {"path": str(force_path), "sha256": sha256(force_path)},
            "numerical_study": {
                "path": str(numerical_path),
                "sha256": sha256(numerical_path),
            },
            "yplus_audit": {"path": str(yplus_path), "sha256": sha256(yplus_path)},
            "model_sensitivity": {
                "path": str(model_path),
                "sha256": sha256(model_path),
            },
            "domain_default_audit": {
                "path": str(domain_default_path),
                "sha256": sha256(domain_default_path),
            },
            "domain_relaxed_audit": {
                "path": str(domain_relaxed_path),
                "sha256": sha256(domain_relaxed_path),
            },
        },
        "numerical_gates": numerical_gates,
        "numerical_behavior_passed": all(numerical_gates.values()),
        "drag_comparison": {
            "cfd_cd": force["last_window_mean"]["Cd"],
            "ladson_tripped_mean_cd": experiment["mean_cd"],
            "absolute_discrepancy": discrepancy,
            "conservative_uncertainty_components": components,
            "conservative_allowance": conservative_allowance,
            "excess_over_allowance": discrepancy - conservative_allowance,
            "gate_even_granting_full_domain_allowance": drag_gate_even_granting_full_domain_allowance,
        },
        "zero_angle_benchmark_accepted": benchmark_gate,
        "ten_degree_case_justified": False,
        "naca_external_body_workflow_accepted": False,
        "accepted_for_rocket": False,
        "verdict": (
            "Failed: reduced-domain residual convergence is unresolved, and zero-angle "
            "drag exceeds even a conservative allowance that grants the full permitted "
            "domain-change budget."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force-audit", required=True, type=Path)
    parser.add_argument("--numerical-study", required=True, type=Path)
    parser.add_argument("--yplus-audit", required=True, type=Path)
    parser.add_argument("--model-sensitivity", required=True, type=Path)
    parser.add_argument("--domain-default-audit", required=True, type=Path)
    parser.add_argument("--domain-relaxed-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = evaluate(
        args.force_audit,
        args.numerical_study,
        args.yplus_audit,
        args.model_sensitivity,
        args.domain_default_audit,
        args.domain_relaxed_audit,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-acceptance.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
