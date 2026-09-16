"""Compare a full TMR flat-plate domain with an inner-grid-preserving truncation."""

import argparse
import json
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import numeric_pairs
from cfd_flat_plate_numerical_study import compare_cf, interpolate_cf, load_run


def preserved_inner_grid(full_case: Path, reduced_case: Path) -> bool:
    full = np.load(full_case / "tmr-grid.npz")
    reduced = np.load(reduced_case / "tmr-grid.npz")
    rows, columns = reduced["x"].shape
    return bool(
        columns == full["x"].shape[1]
        and rows < full["x"].shape[0]
        and np.array_equal(reduced["x"], full["x"][:rows])
        and np.array_equal(reduced["y"], full["y"][:rows])
    )


def domain_metadata(run: dict) -> dict:
    declared = run["spec"].get("domain")
    if declared is not None:
        return declared
    grid = np.load(Path(run["case"]) / "tmr-grid.npz")
    top = grid["y"][-1]
    return {
        "requested_top_y_m": None,
        "selected_top_y_min_m": float(top.min()),
        "selected_top_y_mean_m": float(top.mean()),
        "selected_top_y_max_m": float(top.max()),
        "original_rows": int(grid["y"].shape[0]),
        "retained_rows": int(grid["y"].shape[0]),
        "metadata_source": "derived_from_retained_coordinates_for_legacy_case",
    }


def study(
    full_case: Path,
    full_audit: Path,
    reduced_case: Path,
    reduced_audit: Path,
    data: Path,
    plan: Path,
) -> dict:
    full = load_run(full_case, full_audit)
    reduced = load_run(reduced_case, reduced_audit)
    invariant_keys = (
        "benchmark", "conditions", "model_mapping", "convection_scheme",
        "boundary_conditions", "omega_wall_treatment", "solver_controls",
    )
    if any(full["spec"][key] != reduced["spec"][key] for key in invariant_keys):
        raise ValueError("Domain cases differ in a non-domain benchmark input")
    if full["spec"]["source"]["archive_member"] != reduced["spec"]["source"][
        "archive_member"
    ]:
        raise ValueError("Domain cases were not derived from the same source grid")
    if not preserved_inner_grid(full_case, reduced_case):
        raise ValueError("Reduced domain does not exactly preserve the full domain's inner rows")
    if not full["result"]["iterative_1e-7_screen"] or not reduced["result"][
        "iterative_1e-7_screen"
    ]:
        raise ValueError("Both domain cases must pass the iterative residual screen")

    plan_data = json.loads(plan.read_text())
    benchmark = next(
        item for item in plan_data["benchmarks"] if item["id"] == "tmr-2dzp-flat-plate"
    )
    numerical = benchmark["predeclared_numerical_screen"]
    targets = np.asarray(
        numerical["mesh"]["comparison_reynolds_theta_points"], dtype=float
    )
    typical = numeric_pairs(data / "retheta_variation_typical.dat")
    target_x = np.interp(targets, typical[:, 1], typical[:, 0])
    limit = float(numerical["domain"]["maximum_cf_relative_change"])
    comparison = compare_cf(
        interpolate_cf(full, target_x), interpolate_cf(reduced, target_x), limit
    )
    return {
        "full_case": str(full_case),
        "reduced_case": str(reduced_case),
        "source_member": full["spec"]["source"]["archive_member"],
        "inner_grid_exactly_preserved": True,
        "full_domain": domain_metadata(full),
        "reduced_domain": domain_metadata(reduced),
        "target_retheta": [float(value) for value in targets],
        "cf_comparison": comparison,
        "domain_screen_passed": bool(comparison["screen_passed"]),
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-case", required=True, type=Path)
    parser.add_argument("--full-audit", required=True, type=Path)
    parser.add_argument("--reduced-case", required=True, type=Path)
    parser.add_argument("--reduced-audit", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = study(
        args.full_case,
        args.full_audit,
        args.reduced_case,
        args.reduced_audit,
        args.benchmark_data,
        args.plan,
    )
    (args.output / "flat-plate-domain-study.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
