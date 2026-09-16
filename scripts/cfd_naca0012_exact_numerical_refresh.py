"""Consolidate corrected-SSTm NACA grid, scheme, wall, and domain evidence."""

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


def evaluate(
    plan_path: Path,
    grid_path: Path,
    scheme_path: Path,
    yplus_path: Path,
    domain_audit_path: Path,
    pressure_path: Path,
) -> dict:
    plan = load(plan_path)
    grid = load(grid_path)
    scheme = load(scheme_path)
    yplus = load(yplus_path)
    domain = load(domain_audit_path)
    pressure = load(pressure_path)

    if not plan.get("declared_before_candidate_execution"):
        raise ValueError("Numerical refresh was not predeclared")
    if not grid.get("finest_pair_grid_independence_gate"):
        raise ValueError("Corrected-model finest-pair gate did not pass")
    if not scheme.get("scheme_independence_gate"):
        raise ValueError("Corrected-model scheme gate did not pass")
    if not yplus.get("wall_resolved_y_plus_gate"):
        raise ValueError("Corrected-model wall-resolution gate did not pass")
    if domain.get("coarse_preflight_passed"):
        raise ValueError("Expected preserved reduced-domain residual failure")
    if domain.get("solver_initial_residuals_last_100_max", {}).get("e", 0) <= 1e-5:
        raise ValueError("Reduced-domain failure is not explained by energy residual")

    return {
        "scope": "corrected NASA TMR SSTm numerical-independence refresh",
        "predeclared_plan": evidence(plan_path),
        "finest_pair_grid": {
            "evidence": evidence(grid_path),
            "coefficient_change": grid["coefficient_change"],
            "gate": True,
        },
        "scheme": {
            "evidence": evidence(scheme_path),
            "coefficient_change": scheme["coefficient_change"],
            "gate": True,
        },
        "near_wall": {
            "evidence": evidence(yplus_path),
            "airfoil_y_plus": yplus["airfoil_y_plus"],
            "maximum_limit": yplus["wall_resolved_maximum_y_plus_limit"],
            "gate": True,
        },
        "domain": {
            "evidence": evidence(domain_audit_path),
            "solver_residual_gate": False,
            "final_energy_initial_residual": domain["solver_initial_residuals_final"]["e"],
            "final_100_max_energy_initial_residual": domain[
                "solver_initial_residuals_last_100_max"
            ]["e"],
            "raw_nonadmissible_mean": domain["last_window_mean"],
            "coefficient_difference_withheld": True,
            "gate": False,
        },
        "cfl3d_pressure_diagnostic": {
            "evidence": evidence(pressure_path),
            "surfaces": pressure["cfl3d_sst_diagnostic"]["surfaces"],
            "experimental_comparison_performed": pressure[
                "experimental_cp_comparison_performed"
            ],
        },
        "status": "finest_pair_scheme_and_wall_pass_domain_residual_gate_failed",
        "numerical_independence_passed": False,
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--grid", required=True, type=Path)
    parser.add_argument("--scheme", required=True, type=Path)
    parser.add_argument("--yplus", required=True, type=Path)
    parser.add_argument("--domain-audit", required=True, type=Path)
    parser.add_argument("--pressure", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    result = evaluate(
        args.plan,
        args.grid,
        args.scheme,
        args.yplus,
        args.domain_audit,
        args.pressure,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-exact-numerical-refresh.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
