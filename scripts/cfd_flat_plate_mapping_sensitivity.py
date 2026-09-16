"""Quantify default-to-TMR-mapped SST changes without treating similarity as equivalence."""

import argparse
import json
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import numeric_pairs
from cfd_flat_plate_numerical_study import compare_cf, interpolate_cf, load_run


def study(
    default_case: Path,
    default_audit: Path,
    mapped_case: Path,
    mapped_audit: Path,
    data: Path,
    plan: Path,
) -> dict:
    default = load_run(default_case, default_audit)
    mapped = load_run(mapped_case, mapped_audit)
    invariant_keys = ("benchmark", "conditions", "convection_scheme", "mesh")
    if any(default["spec"][key] != mapped["spec"][key] for key in invariant_keys):
        raise ValueError("Mapping-sensitivity cases differ outside model/wall mapping")
    if default["spec"]["source"]["coordinate_payload_sha256"] != mapped["spec"][
        "source"
    ]["coordinate_payload_sha256"]:
        raise ValueError("Mapping-sensitivity cases do not use the same source coordinates")
    default_mapping = default["spec"]["model_mapping"]
    mapped_mapping = mapped["spec"]["model_mapping"]
    default_variant = (
        default_mapping.get("variant")
        if isinstance(default_mapping, dict)
        else "legacy-openfoam-default"
    )
    if default_variant not in ("openfoam-default", "legacy-openfoam-default"):
        raise ValueError("Baseline is not the OpenFOAM-default mapping")
    mapped_variants = {
        "tmr-sst-vm-flatplate-equivalent",  # legacy retained label
        "tmr-sstm-flatplate-partial-map",
    }
    if not isinstance(mapped_mapping, dict) or mapped_mapping.get("variant") not in mapped_variants:
        raise ValueError("Candidate is not a coefficient-mapped TMR SSTm flat-plate case")
    if not default["result"]["iterative_1e-7_screen"] or not mapped["result"][
        "iterative_1e-7_screen"
    ]:
        raise ValueError("Both mapping cases must pass iterative convergence")

    plan_data = json.loads(plan.read_text())
    benchmark = next(
        item for item in plan_data["benchmarks"] if item["id"] == "tmr-2dzp-flat-plate"
    )
    targets = np.asarray(
        benchmark["predeclared_numerical_screen"]["mesh"][
            "comparison_reynolds_theta_points"
        ],
        dtype=float,
    )
    typical = numeric_pairs(data / "retheta_variation_typical.dat")
    target_x = np.interp(targets, typical[:, 1], typical[:, 0])
    # Infinite limit makes this a measurement only; the plan explicitly defines no pass gate.
    comparison = compare_cf(
        interpolate_cf(default, target_x), interpolate_cf(mapped, target_x), np.inf
    )
    comparison.pop("screen_limit")
    comparison.pop("screen_passed")
    return {
        "default_case": str(default_case),
        "mapped_case": str(mapped_case),
        "default_model_mapping": default_variant,
        "mapped_model_mapping": mapped_mapping["variant"],
        "default_omega_wall": default["spec"]["omega_wall_treatment"]["variant"],
        "mapped_omega_wall": mapped["spec"]["omega_wall_treatment"]["variant"],
        "target_retheta": [float(value) for value in targets],
        "cf_change": comparison,
        "acceptance_threshold": None,
        "interpretation": (
            "Sensitivity only. Similarity cannot establish equation equivalence, and the partial "
            "map cannot govern benchmark acceptance until remaining SSTm differences are resolved."
        ),
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--default-case", required=True, type=Path)
    parser.add_argument("--default-audit", required=True, type=Path)
    parser.add_argument("--mapped-case", required=True, type=Path)
    parser.add_argument("--mapped-audit", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = study(
        args.default_case,
        args.default_audit,
        args.mapped_case,
        args.mapped_audit,
        args.benchmark_data,
        args.plan,
    )
    (args.output / "flat-plate-mapping-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
