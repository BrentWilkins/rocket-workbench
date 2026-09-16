"""Audit the predeclared stock-SST to exact-SSTm incompressible rung."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np

from cfd_flat_plate_model_audit import close_enough, coefficient_block
from cfd_naca0012_exact_sstm_incompressible_restart import (
    FIELDS,
    IMAGE_PROVENANCE,
    METHOD,
    PLAN,
    add_runtime_libraries,
)
from cfd_naca0012_force_audit import coefficient_history, long_window_trend
from cfd_naca0012_map_fields import latest_time
from cfd_naca0012_stock_sst_audit import cfl3d_reference, residuals, sha256
from cfd_naca0012_stock_sst_restart import reset_field_location


def _solver_stage(case: Path, execution: list[dict]) -> tuple[dict, Path]:
    matches = [
        (index, stage)
        for index, stage in enumerate(execution)
        if "simpleFoam" in stage.get("stage", "")
    ]
    if len(matches) != 1:
        raise ValueError("Expected exactly one simpleFoam execution stage")
    index, stage = matches[0]
    return stage, case / f"{index}-{stage['stage'].split()[0]}.log"


def audit(
    case: Path,
    benchmark_data: Path,
    window: int = 100,
    plan_path: Path = PLAN,
) -> dict:
    case = case.resolve(strict=True)
    benchmark_data = benchmark_data.resolve(strict=True)
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    execution = json.loads((case / "execution.json").read_text())
    image = json.loads((case / "image.json").read_text())
    record = json.loads((case / "exact-sstm-restart-execution.json").read_text())
    source = Path(spec["initialization"]["source_case"]).resolve(strict=True)
    source_audit_path = Path(spec["initialization"]["source_audit"]).resolve(strict=True)
    source_audit = json.loads(source_audit_path.read_text())
    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())

    source_gate = all(
        (
            source == Path(plan["source"]["case"]).resolve(),
            sha256(source_spec_path) == plan["source"]["case_spec_sha256"],
            source_audit_path == Path(plan["source"]["required_audit"]).resolve(),
            sha256(source_audit_path) == plan["source"]["audit_sha256"],
            Path(source_audit.get("case", "")).resolve() == source,
            source_audit.get("case_spec_sha256") == sha256(source_spec_path),
            source_audit.get("diagnostic_numerics_passed") is True,
            all(
                stage.get("stage_passed") is True
                for stage in json.loads((source / "execution.json").read_text())
            ),
        )
    )

    copied = spec["change_control"]["copied_source_file_sha256"]
    invariant_paths = [relative for relative in copied if relative != "system/controlDict"]
    copied_invariants_gate = all(
        source.joinpath(relative).is_file()
        and case.joinpath(relative).is_file()
        and sha256(source / relative) == copied[relative]
        and sha256(case / relative) == copied[relative]
        for relative in invariant_paths
    )
    source_control = (source / "system" / "controlDict").read_text()
    control_gate = all(
        (
            sha256(source / "system" / "controlDict")
            == copied["system/controlDict"],
            (case / "system" / "controlDict").read_text()
            == add_runtime_libraries(source_control),
        )
    )
    source_time = latest_time(source)
    copied_fields_gate = all(
        (case / "0" / name).read_text()
        == reset_field_location((source_time / name).read_text())
        for name in FIELDS
    )

    change = spec["change_control"]
    implementation = Path(change["implementation_snapshot"])
    plan_snapshot = case / "provenance" / plan_path.name
    image_provenance_snapshot = case / "provenance" / IMAGE_PROVENANCE.name
    construction_gate = all(
        (
            record.get("stage") == METHOD,
            record.get("stage_passed") is True,
            record.get("source_audit_sha256") == sha256(source_audit_path),
            record.get("plan_sha256") == sha256(plan_path),
            record.get("target_case_spec_sha256") == sha256(spec_path),
            change.get("plan_sha256") == sha256(plan_path),
            change.get("image_provenance_sha256") == sha256(IMAGE_PROVENANCE),
            implementation.is_file(),
            change.get("implementation_sha256") == sha256(implementation),
            plan_snapshot.is_file(),
            sha256(plan_snapshot) == sha256(plan_path),
            image_provenance_snapshot.is_file(),
            sha256(image_provenance_snapshot) == sha256(IMAGE_PROVENANCE),
            change.get("declared_change")
            == "stock kOmegaSST to source-audited TmrSSTmExactProduction only",
        )
    )
    provenance_gate = all(
        (
            source_gate,
            copied_invariants_gate,
            control_gate,
            copied_fields_gate,
            construction_gate,
        )
    )

    solver_stage, log_path = _solver_stage(case, execution)
    log = log_path.read_text()
    expected_image_id = plan["execution"]["image_id"]
    runtime_gate = all(
        (
            len(execution) == 4,
            all(stage.get("stage_passed") is True for stage in execution),
            all(stage.get("network_disabled") is True for stage in execution),
            all(stage.get("image_id") == expected_image_id for stage in execution),
            all(stage.get("mpi_ranks") == 12 for stage in execution),
            all(
                stage.get("resource_limits") == {"cpus": 12.0, "memory": "24g"}
                for stage in execution
            ),
            image.get("Id") == expected_image_id,
            solver_stage.get("returncode") == 0,
        )
    )

    expected_mapping = {
        "solver": "simpleFoam",
        "ras_model": "TmrSSTmExactProduction",
        "variant": "tmr-sstm-exact-production-v2512-source-audited",
        "runtime_library": "libTmrSSTmExactProduction.so",
        "image_id": expected_image_id,
    }
    coefficients = coefficient_block(log, "RAS")
    required_coefficients = plan["declared_changes"]["required_coefficients"]
    coefficient_gate = all(
        close_enough(coefficients.get(name), expected)
        for name, expected in required_coefficients.items()
    )
    model_gate = all(
        (
            spec.get("model_mapping") == expected_mapping,
            "Selecting RAS turbulence model TmrSSTmExactProduction" in log,
            coefficient_gate,
            re.search(r"(?m)^libs .*libTmrSSTmExactProduction\.so", (case / "system" / "controlDict").read_text())
            is not None,
        )
    )

    names, values = coefficient_history(case)
    if len(values) < 500:
        raise ValueError("Need at least 500 exact-SSTm force samples")
    indices = {name: index for index, name in enumerate(names)}
    finite_gate = bool(np.isfinite(values).all())
    horizon_gate = bool(values[-1, indices["Time"]] >= 5000)
    tail = values[-window:]
    means = {
        name: float(np.mean(tail[:, indices[name]]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    ranges = {
        name: float(np.ptp(tail[:, indices[name]]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    settling_limits = {
        name: max(0.001, 0.01 * abs(means[name]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    settling_gate = all(ranges[name] <= settling_limits[name] for name in ranges)
    projected, trend_limits, trend_gate = long_window_trend(values, indices, 0.0, 500)
    final_residuals, recent_max_residuals, residual_gate = residuals(log, window)
    symmetry_gate = abs(means["Cl"]) <= 0.004 and abs(means["CmPitch"]) <= 0.0002
    reference = cfl3d_reference(benchmark_data / "n0012clcd_cfl3d_sst.dat")
    delta_reference = means["Cd"] - reference["Cd"]
    force_agreement_gate = abs(delta_reference) <= 0.0002
    source_names, source_values = coefficient_history(source)
    source_indices = {name: index for index, name in enumerate(source_names)}
    source_mean_cd = float(np.mean(source_values[-window:, source_indices["Cd"]]))
    delta_source = means["Cd"] - source_mean_cd
    bounding_pattern = re.compile(
        r"bounding k, min: ([0-9.eE+-]+) max: ([0-9.eE+-]+) average: ([0-9.eE+-]+)"
    )
    bounding_rows = [
        tuple(float(value) for value in row) for row in bounding_pattern.findall(log)
    ]
    diagnostic_numerics_passed = all(
        (
            provenance_gate,
            runtime_gate,
            model_gate,
            finite_gate,
            horizon_gate,
            settling_gate,
            trend_gate,
            residual_gate,
            symmetry_gate,
        )
    )
    return {
        "schema_version": 1,
        "scope": "Exact NASA SSTm incompressible relative diagnostic downstream of failed Gate 1",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "plan": str(plan_path),
        "plan_sha256": sha256(plan_path),
        "source_case": str(source),
        "source_audit": str(source_audit_path),
        "source_audit_sha256": sha256(source_audit_path),
        "source_gate": source_gate,
        "copied_invariants_gate": copied_invariants_gate,
        "control_library_only_gate": control_gate,
        "copied_solution_fields_gate": copied_fields_gate,
        "construction_provenance_gate": construction_gate,
        "provenance_gate": provenance_gate,
        "runtime_and_execution_gate": runtime_gate,
        "model_configuration_gate": model_gate,
        "exact_sstm_coefficients": coefficients,
        "exact_sstm_coefficients_gate": coefficient_gate,
        "finite_force_history_gate": finite_gate,
        "iteration_horizon_gate": horizon_gate,
        "last_window": window,
        "last_window_mean": means,
        "last_window_peak_to_peak": ranges,
        "settling_limits": settling_limits,
        "settling_gate": settling_gate,
        "projected_change_over_500_iterations": projected,
        "trend_absolute_limits": trend_limits,
        "long_window_trend_gate": trend_gate,
        "solver_initial_residuals_final": final_residuals,
        "solver_initial_residuals_last_100_max": recent_max_residuals,
        "solver_residual_gate": residual_gate,
        "zero_angle_symmetry_gate": symmetry_gate,
        "cfl3d_sst_reference": reference,
        "openfoam_minus_cfl3d_sst_cd": delta_reference,
        "force_agreement_gate": force_agreement_gate,
        "source_stock_sst_mean_cd": source_mean_cd,
        "exact_sstm_minus_stock_sst_cd": delta_source,
        "bounded_k_diagnostic": {
            "classification": "post_hoc_report_only_not_an_acceptance_gate",
            "occurrences": len(bounding_rows),
            "worst_minimum_k": min((row[0] for row in bounding_rows), default=None),
            "final": (
                {
                    "minimum_k": bounding_rows[-1][0],
                    "maximum_k": bounding_rows[-1][1],
                    "mean_k": bounding_rows[-1][2],
                }
                if bounding_rows
                else None
            ),
        },
        "diagnostic_numerics_passed": diagnostic_numerics_passed,
        "strict_gate_3_passed": False,
        "strict_gate_3_status": "blocked_by_failed_gate_1",
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--window", type=int, default=100)
    parser.add_argument("--plan", type=Path, default=PLAN)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = audit(args.case, args.benchmark_data, args.window, args.plan)
    args.output.mkdir(parents=True)
    output = args.output / "naca0012-exact-sstm-incompressible-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
