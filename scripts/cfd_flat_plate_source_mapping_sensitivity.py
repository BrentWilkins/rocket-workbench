"""Compare partial coefficient mapping with the v2512 source-mapped SSTm model."""

import argparse
import json
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import numeric_pairs
from cfd_flat_plate_numerical_study import compare_cf, interpolate_cf, load_run


def invariant_signature(run: dict) -> dict:
    spec = run["spec"]
    return {
        key: spec[key]
        for key in (
            "benchmark", "conditions", "mesh", "domain", "boundary_conditions",
            "omega_wall_treatment", "convection_scheme", "solver_controls",
        )
    } | {
        "coordinate_payload_sha256": spec["source"]["coordinate_payload_sha256"],
    }


def study(
    partial_case: Path,
    partial_audit: Path,
    source_case: Path,
    source_audit: Path,
    data: Path,
    plan: Path,
) -> dict:
    partial = load_run(partial_case, partial_audit)
    source = load_run(source_case, source_audit)
    if invariant_signature(partial) != invariant_signature(source):
        raise ValueError("Source-mapping sensitivity cases differ outside turbulence model")
    if partial["spec"]["model_mapping"]["variant"] != "tmr-sstm-flatplate-partial-map":
        raise ValueError("Baseline is not the partial SSTm coefficient map")
    if source["spec"]["model_mapping"]["variant"] != "tmr-sstm-v2512-source-map":
        raise ValueError("Candidate is not the v2512 source-mapped SSTm model")

    plan_data = json.loads(plan.read_text())
    benchmark = next(
        item for item in plan_data["benchmarks"] if item["id"] == "tmr-2dzp-flat-plate"
    )
    target_retheta = np.asarray(
        benchmark["predeclared_numerical_screen"]["mesh"]
        ["comparison_reynolds_theta_points"],
        dtype=float,
    )
    typical = numeric_pairs(data / "retheta_variation_typical.dat")
    target_x = np.interp(target_retheta, typical[:, 1], typical[:, 0])
    comparison = compare_cf(
        interpolate_cf(partial, target_x),
        interpolate_cf(source, target_x),
        np.inf,
    )
    comparison.pop("screen_limit")
    comparison.pop("screen_passed")

    return {
        "comparison": "partial SSTm coefficient map versus v2512 source-mapped SSTm",
        "partial_case": partial["case"],
        "source_mapped_case": source["case"],
        "partial_case_spec_sha256": partial["case_spec_sha256"],
        "source_case_spec_sha256": source["case_spec_sha256"],
        "partial_audit_sha256": partial["audit_sha256"],
        "source_audit_sha256": source["audit_sha256"],
        "retheta_points": target_retheta.tolist(),
        "x_points_m": target_x.tolist(),
        "cf_change": comparison,
        "decision_rule": (
            "Report without a pass threshold. Small change cannot substitute for the "
            "source/image provenance audit or independent benchmark gates."
        ),
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partial-case", required=True, type=Path)
    parser.add_argument("--partial-audit", required=True, type=Path)
    parser.add_argument("--source-case", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = study(
        args.partial_case, args.partial_audit,
        args.source_case, args.source_audit,
        args.benchmark_data, args.plan,
    )
    (args.output / "flat-plate-source-mapping-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
