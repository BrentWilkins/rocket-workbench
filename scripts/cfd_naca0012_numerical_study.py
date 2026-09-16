"""Quantify NACA 0012 grid, scheme, and iterative force uncertainty."""

import argparse
import hashlib
import json
import math
from pathlib import Path


COEFFICIENTS = ("Cd", "Cl", "CmPitch")


def independence_limits(angle_deg: float) -> dict[str, float]:
    alpha = math.radians(angle_deg)
    return {
        "Cd": 0.0002,
        "Cl": 0.004 * abs(math.cos(alpha)) + 0.0002 * abs(math.sin(alpha)),
        "CmPitch": 0.0002,
    }


def within_limits(changes: dict[str, float], limits: dict[str, float]) -> bool:
    return all(changes[name] <= limits[name] for name in COEFFICIENTS)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(case: Path, audit: Path) -> dict:
    spec_path = case / "benchmark-spec.json"
    audit_path = audit / "naca0012-force-audit.json"
    spec = json.loads(spec_path.read_text())
    result = json.loads(audit_path.read_text())
    if not result["coarse_preflight_passed"]:
        raise ValueError(f"Input preflight did not pass: {case}")
    if "convection_scheme" not in spec:
        schemes = (case / "system" / "fvSchemes").read_text()
        if "div(phi,U) bounded Gauss upwind;" in schemes:
            spec["convection_scheme"] = "first-order-upwind"
        elif "div(phi,U) bounded Gauss linearUpwind grad(U);" in schemes:
            spec["convection_scheme"] = "linear-upwind-velocity"
        else:
            raise ValueError(f"Cannot infer retained convection scheme: {case}")
    return {
        "case": str(case),
        "audit": str(audit),
        "spec": spec,
        "result": result,
        "spec_sha256": sha256(spec_path),
        "audit_sha256": sha256(audit_path),
    }


def invariant(run: dict, include_scheme: bool) -> dict:
    spec = run["spec"]
    signature = {
        "benchmark": spec["benchmark"],
        "angle": spec["conditions"]["angle_of_attack_deg"],
        "mach": spec["conditions"]["mach"],
        "reynolds": spec["conditions"]["reynolds_number_chord"],
        "model_mapping": spec["model_mapping"],
        "wall_treatment": spec["wall_treatment"],
    }
    if include_scheme:
        signature["convection_scheme"] = spec["convection_scheme"]
    return signature


def differences(first: dict, second: dict) -> dict:
    a = first["result"]["last_window_mean"]
    b = second["result"]["last_window_mean"]
    return {
        name: {
            "signed_change": b[name] - a[name],
            "absolute_change": abs(b[name] - a[name]),
        }
        for name in COEFFICIENTS
    }


def study(
    grids: list[tuple[Path, Path]],
    baseline: tuple[Path, Path] | None,
    candidate: tuple[Path, Path] | None,
) -> dict:
    if len(grids) < 3:
        raise ValueError("At least three systematically nested grids are required")
    runs = sorted(
        (load(case, audit) for case, audit in grids),
        key=lambda run: run["spec"]["mesh"]["cells"],
    )
    signatures = [invariant(run, True) for run in runs]
    if any(signature != signatures[0] for signature in signatures[1:]):
        raise ValueError("Grid-study invariants differ")
    cell_counts = [run["spec"]["mesh"]["cells"] for run in runs]
    if any(second <= first for first, second in zip(cell_counts, cell_counts[1:])):
        raise ValueError("Grid cell counts are not strictly increasing")
    comparisons = [
        {
            "coarse_cells": first["spec"]["mesh"]["cells"],
            "fine_cells": second["spec"]["mesh"]["cells"],
            "coefficient_change": differences(first, second),
        }
        for first, second in zip(runs, runs[1:])
    ]

    scheme = None
    if (baseline is None) != (candidate is None):
        raise ValueError("Scheme baseline and candidate must be supplied together")
    if baseline and candidate:
        baseline_run = load(*baseline)
        candidate_run = load(*candidate)
        if invariant(baseline_run, False) != invariant(candidate_run, False):
            raise ValueError("Scheme-study invariants differ")
        if (
            baseline_run["spec"]["grid_dimensions"]
            != candidate_run["spec"]["grid_dimensions"]
        ):
            raise ValueError("Scheme study must use one grid")
        scheme = {
            "baseline": baseline_run["spec"]["convection_scheme"],
            "candidate": candidate_run["spec"]["convection_scheme"],
            "coefficient_change": differences(baseline_run, candidate_run),
            "baseline_case": baseline_run["case"],
            "candidate_case": candidate_run["case"],
        }

    finest = runs[-1]
    iterative_half_range = {
        name: 0.5 * finest["result"]["last_window_peak_to_peak"][name]
        for name in COEFFICIENTS
    }
    iterative_projected_drift = {
        name: finest["result"]["projected_change_over_trend_window"][name]
        for name in COEFFICIENTS
    }
    iterative = {
        name: max(iterative_half_range[name], iterative_projected_drift[name])
        for name in COEFFICIENTS
    }
    discretization = {
        name: comparisons[-1]["coefficient_change"][name]["absolute_change"]
        for name in COEFFICIENTS
    }
    scheme_uncertainty = (
        {
            name: scheme["coefficient_change"][name]["absolute_change"]
            for name in COEFFICIENTS
        }
        if scheme
        else None
    )
    limits = independence_limits(signatures[0]["angle"])
    grid_independence = within_limits(discretization, limits)
    scheme_independence = (
        within_limits(scheme_uncertainty, limits)
        if scheme_uncertainty is not None
        else False
    )
    return {
        "benchmark": "tmr-naca0012-external-body",
        "angle_of_attack_deg": signatures[0]["angle"],
        "grid_runs": [
            {
                key: run[key]
                for key in ("case", "audit", "spec_sha256", "audit_sha256")
            }
            | {
                "grid_dimensions": run["spec"]["grid_dimensions"],
                "cells": run["spec"]["mesh"]["cells"],
            }
            for run in runs
        ],
        "grid_comparisons": comparisons,
        "gci_claimed": False,
        "gci_reason": "Direct nested-grid differences only; asymptotic behavior is not assumed.",
        "scheme_comparison": scheme,
        "uncertainty_components_from_finest_available_pair": {
            "numerical_discretization_absolute": discretization,
            "scheme_absolute": scheme_uncertainty,
            "iterative_half_range_absolute": iterative_half_range,
            "iterative_projected_trend_absolute": iterative_projected_drift,
            "iterative_conservative_absolute": iterative,
        },
        "independence_absolute_limits_from_experimental_repeatability": limits,
        "finest_pair_grid_independence_gate": grid_independence,
        "scheme_independence_gate": scheme_independence,
        "numerical_independence_passed": grid_independence and scheme_independence,
        "numerical_uncertainty_quantified": scheme is not None,
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grid", nargs=2, action="append", required=True, metavar=("CASE", "AUDIT"))
    parser.add_argument("--scheme-baseline", nargs=2, metavar=("CASE", "AUDIT"))
    parser.add_argument("--scheme-candidate", nargs=2, metavar=("CASE", "AUDIT"))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = study(
        [(Path(case), Path(audit)) for case, audit in args.grid],
        tuple(map(Path, args.scheme_baseline)) if args.scheme_baseline else None,
        tuple(map(Path, args.scheme_candidate)) if args.scheme_candidate else None,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-numerical-study.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
