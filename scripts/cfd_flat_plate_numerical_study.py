"""Compare retained TMR flat-plate grids and convection schemes fail-closed."""

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import numeric_pairs


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_run(case: Path, audit_dir: Path) -> dict:
    spec_path = case / "benchmark-spec.json"
    audit_path = audit_dir / "flat-plate-audit.json"
    spec = json.loads(spec_path.read_text())
    result = json.loads(audit_path.read_text())
    profiles = result["profiles"]
    return {
        "case": str(case),
        "audit": str(audit_dir),
        "case_spec_sha256": sha256(spec_path),
        "audit_sha256": sha256(audit_path),
        "spec": spec,
        "result": result,
        "x": np.asarray([row["x_m"] for row in profiles]),
        "cf": np.asarray([row["Cf"] for row in profiles]),
    }


def invariant_signature(run: dict, include_scheme: bool) -> dict:
    spec = run["spec"]
    signature = {
        "benchmark": spec["benchmark"],
        "archive_sha256": spec["source"]["archive_sha256"],
        "conditions": spec["conditions"],
        "model_mapping": spec["model_mapping"],
        "omega_wall_treatment": spec["omega_wall_treatment"]["variant"],
        "boundary_conditions": spec.get("boundary_conditions"),
        "solver_controls": spec.get("solver_controls"),
        "domain_extent": {
            key: spec.get("domain", {}).get(key)
            for key in (
                "requested_top_y_m", "selected_top_y_min_m",
                "selected_top_y_mean_m", "selected_top_y_max_m",
            )
        },
    }
    if include_scheme:
        signature["convection_scheme"] = spec["convection_scheme"]
    return signature


def compare_cf(first: np.ndarray, second: np.ndarray, limit: float) -> dict:
    relative = np.abs(second - first) / np.abs(second)
    return {
        "mean_relative_change": float(relative.mean()),
        "maximum_relative_change": float(relative.max()),
        "pointwise_relative_change": [float(value) for value in relative],
        "screen_limit": limit,
        "screen_passed": bool(np.all(relative <= limit + 1e-12)),
    }


def interpolate_cf(run: dict, target_x: np.ndarray) -> np.ndarray:
    if target_x.min() < run["x"].min() or target_x.max() > run["x"].max():
        raise ValueError(f"Target stations exceed profile support for {run['case']}")
    return np.interp(target_x, run["x"], run["cf"])


def study(
    grids: list[tuple[Path, Path]],
    scheme_baseline: tuple[Path, Path] | None,
    scheme_candidate: tuple[Path, Path] | None,
    data: Path,
    plan: Path,
) -> dict:
    plan_data = json.loads(plan.read_text())
    benchmark = next(
        item for item in plan_data["benchmarks"] if item["id"] == "tmr-2dzp-flat-plate"
    )
    numerical = benchmark["predeclared_numerical_screen"]
    target_retheta = np.asarray(
        numerical["mesh"]["comparison_reynolds_theta_points"], dtype=float
    )
    typical = numeric_pairs(data / "retheta_variation_typical.dat")
    target_x = np.interp(target_retheta, typical[:, 1], typical[:, 0])

    grid_runs = sorted(
        (load_run(case, audit) for case, audit in grids),
        key=lambda run: run["spec"]["mesh"]["cells"],
    )
    if len(grid_runs) < 3:
        raise ValueError("At least three systematically refined grids are required")
    signatures = [invariant_signature(run, include_scheme=True) for run in grid_runs]
    if any(signature != signatures[0] for signature in signatures[1:]):
        raise ValueError("Grid cases differ in a non-mesh benchmark input")
    if any(not run["result"]["iterative_1e-7_screen"] for run in grid_runs):
        raise ValueError("Every grid must pass the iterative residual screen")

    sampled = [interpolate_cf(run, target_x) for run in grid_runs]
    grid_comparisons = []
    mesh_limit = float(
        numerical["mesh"]["maximum_medium_to_fine_cf_relative_change"]
    )
    for coarse, fine, coarse_cf, fine_cf in zip(
        grid_runs[:-1], grid_runs[1:], sampled[:-1], sampled[1:], strict=True
    ):
        comparison = compare_cf(coarse_cf, fine_cf, mesh_limit)
        comparison.update(
            {
                "coarse_cells": coarse["spec"]["mesh"]["cells"],
                "fine_cells": fine["spec"]["mesh"]["cells"],
                "cell_count_ratio": fine["spec"]["mesh"]["cells"]
                / coarse["spec"]["mesh"]["cells"],
            }
        )
        grid_comparisons.append(comparison)

    result = {
        "benchmark": benchmark["id"],
        "target_retheta": [float(value) for value in target_retheta],
        "target_x_m": [float(value) for value in target_x],
        "grid_runs": [
            {
                key: run[key]
                for key in ("case", "audit", "case_spec_sha256", "audit_sha256")
            }
            | {
                "dimensions": run["spec"]["grid_dimensions"],
                "points": run["spec"]["mesh"]["points"],
                "cells": run["spec"]["mesh"]["cells"],
            }
            for run in grid_runs
        ],
        "grid_comparisons": grid_comparisons,
        "mesh_screen_passed": bool(grid_comparisons[-1]["screen_passed"]),
        "gci_claimed": False,
        "gci_reason": "Only direct differences are reported; asymptotic behavior is not assumed.",
    }

    if (scheme_baseline is None) != (scheme_candidate is None):
        raise ValueError("Both scheme baseline and candidate must be supplied together")
    if scheme_baseline is not None and scheme_candidate is not None:
        baseline = load_run(*scheme_baseline)
        candidate = load_run(*scheme_candidate)
        if invariant_signature(baseline, include_scheme=False) != invariant_signature(
            candidate, include_scheme=False
        ):
            raise ValueError("Scheme cases differ in a non-scheme benchmark input")
        if baseline["spec"]["mesh"] != candidate["spec"]["mesh"]:
            raise ValueError("Scheme cases do not use the same mesh")
        if not baseline["result"]["iterative_1e-7_screen"] or not candidate["result"][
            "iterative_1e-7_screen"
        ]:
            raise ValueError("Both scheme cases must pass the iterative residual screen")
        scheme_limit = float(
            numerical["scheme"][
                "maximum_first_order_to_linear_upwind_velocity_cf_relative_change"
            ]
        )
        scheme_result = compare_cf(
            interpolate_cf(baseline, target_x),
            interpolate_cf(candidate, target_x),
            scheme_limit,
        )
        scheme_result.update(
            {
                "baseline": baseline["spec"]["convection_scheme"],
                "candidate": candidate["spec"]["convection_scheme"],
                "baseline_case": baseline["case"],
                "candidate_case": candidate["case"],
            }
        )
        result["scheme_comparison"] = scheme_result
        result["scheme_screen_passed"] = bool(scheme_result["screen_passed"])
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grid", nargs=2, action="append", required=True, metavar=("CASE", "AUDIT"))
    parser.add_argument("--scheme-baseline", nargs=2, metavar=("CASE", "AUDIT"))
    parser.add_argument("--scheme-candidate", nargs=2, metavar=("CASE", "AUDIT"))
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = study(
        [(Path(case), Path(audit)) for case, audit in args.grid],
        tuple(Path(value) for value in args.scheme_baseline)
        if args.scheme_baseline
        else None,
        tuple(Path(value) for value in args.scheme_candidate)
        if args.scheme_candidate
        else None,
        args.benchmark_data,
        args.plan,
    )
    (args.output / "flat-plate-numerical-study.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
