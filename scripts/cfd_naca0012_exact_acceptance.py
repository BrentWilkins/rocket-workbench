"""Compute fail-closed zero-angle acceptance for the corrected SSTm workflow."""

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.resolve(strict=True).read_text())


def evidence(path: Path) -> dict:
    return {"path": str(path), "sha256": sha256(path)}


def evaluate(force_path: Path, refresh_path: Path, model_path: Path) -> dict:
    force = load(force_path)
    refresh = load(refresh_path)
    model = load(model_path)

    if not force.get("coarse_preflight_passed"):
        raise ValueError("Corrected-model force baseline did not pass diagnostic gates")
    if not model.get("candidate", {}).get("all_diagnostic_solver_gates_passed"):
        raise ValueError("Corrected SSTm equation-parity candidate did not pass")

    grid = refresh["finest_pair_grid"]
    scheme = refresh["scheme"]
    wall = refresh["near_wall"]
    domain = refresh["domain"]
    gates = {
        "baseline_force_preflight": True,
        "exact_sstm_equation_parity": True,
        "finest_pair_grid_independence": bool(grid["gate"]),
        "scheme_independence": bool(scheme["gate"]),
        "wall_resolved_y_plus": bool(wall["gate"]),
        "domain_sensitivity": bool(domain["gate"]),
    }

    experiment = force["ladson_tripped_experiment"]
    discrepancy = abs(float(experiment["cfd_minus_mean_cd"]))
    iterative = max(
        0.5 * float(force["last_window_peak_to_peak"]["Cd"]),
        abs(float(force["projected_change_over_trend_window"]["Cd"])),
    )
    components = {
        "experimental_repeatability": 0.0002,
        "finest_pair_discretization": grid["coefficient_change"]["Cd"][
            "absolute_change"
        ],
        "scheme": scheme["coefficient_change"]["Cd"]["absolute_change"],
        "iterative": iterative,
        "digitization": 0.000005,
        "full_predeclared_domain_budget_granted_despite_failed_domain_gate": 0.0002,
    }
    allowance = sum(components.values())
    agreement = discrepancy <= allowance

    return {
        "scope": "tmr-naca0012-zero-angle-external-body-corrected-sstm",
        "input_evidence": {
            "force_audit": evidence(force_path),
            "corrected_model_numerical_refresh": evidence(refresh_path),
            "sstm_equation_parity": evidence(model_path),
        },
        "cfd_mean_cd": force["last_window_mean"]["Cd"],
        "ladson_tripped_mean_cd": experiment["mean_cd"],
        "absolute_cd_discrepancy": discrepancy,
        "conservative_cd_allowance_components": components,
        "conservative_cd_allowance_total": allowance,
        "discrepancy_excess_over_allowance": discrepancy - allowance,
        "numerical_gates": gates,
        "all_numerical_gates_passed": all(gates.values()),
        "zero_angle_drag_agreement_within_allowance": agreement,
        "zero_angle_benchmark_accepted": all(gates.values()) and agreement,
        "accepted_for_rocket": False,
        "decision": (
            "Corrected-model grid, scheme, wall, and iterative checks pass, but "
            "the reduced-domain residual gate fails and drag exceeds even the "
            "conservative allowance that grants the full domain-change budget."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force-audit", required=True, type=Path)
    parser.add_argument("--numerical-refresh", required=True, type=Path)
    parser.add_argument("--model-sensitivity", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    result = evaluate(args.force_audit, args.numerical_refresh, args.model_sensitivity)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-exact-acceptance.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
