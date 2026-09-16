"""Audit the predeclared unchanged stock-SST convergence continuation."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np

from cfd_flat_plate_model_audit import close_enough, coefficient_block
from cfd_naca0012_force_audit import coefficient_history, long_window_trend
from cfd_naca0012_stock_sst_audit import (
    EXPECTED_IMAGE_ID,
    STOCK_SST_COEFFICIENTS,
    cfl3d_reference,
    residuals,
    sha256,
)
from cfd_naca0012_stock_sst_continue import METHOD
from cfd_naca0012_stock_sst_restart import reset_field_location


PLAN = Path(__file__).resolve().parents[1] / "cfd" / "naca0012-stock-sst-continuation-plan.json"


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
    record = json.loads((case / "stock-sst-continuation-execution.json").read_text())
    source = Path(spec["initialization"]["source_case"])
    source_audit_path = Path(spec["initialization"]["source_audit"])
    source_audit = json.loads(source_audit_path.read_text())
    source_spec_path = source / "benchmark-spec.json"
    expected_source_audit_sha256 = plan["source"].get("audit_sha256")
    source_plan_gate = (
        source.resolve() == Path(plan["source"]["case"]).resolve()
        and source_audit_path.resolve() == Path(plan["source"]["audit"]).resolve()
        and (
            expected_source_audit_sha256 is None
            or sha256(source_audit_path) == expected_source_audit_sha256
        )
    )

    trigger_prerequisites = all(
        source_audit.get(gate) is True for gate in plan["trigger"]["required_true"]
    )
    convergence_names = (
        "settling_gate",
        "long_window_trend_gate",
        "solver_residual_gate",
        "zero_angle_symmetry_gate",
    )
    source_trigger_failure = any(source_audit.get(gate) is False for gate in convergence_names)
    trigger_gate = source_plan_gate and trigger_prerequisites and source_trigger_failure

    copied = spec["change_control"]["copied_source_file_sha256"]
    copied_dictionaries_and_mesh_gate = all(
        source.joinpath(relative).is_file()
        and case.joinpath(relative).is_file()
        and sha256(source / relative) == expected
        and sha256(case / relative) == expected
        for relative, expected in copied.items()
    )
    source_time = spec["initialization"]["source_time"]
    source_time_name = str(int(source_time)) if float(source_time).is_integer() else str(source_time)
    copied_fields_gate = all(
        (case / "0" / name).read_text()
        == reset_field_location((source / source_time_name / name).read_text())
        for name in ("U", "p", "k", "omega", "nut")
    )
    implementation = Path(spec["change_control"]["implementation_snapshot"])
    provenance_gate = (
        trigger_gate
        and record.get("stage_passed") is True
        and record.get("stage") == METHOD
        and record.get("source_audit_sha256") == sha256(source_audit_path)
        and record.get("plan_sha256") == sha256(plan_path)
        and record.get("target_case_spec_sha256") == sha256(spec_path)
        and sha256(source_spec_path) == plan["source"]["case_spec_sha256"]
        and spec["initialization"].get("physics_or_numerics_changed") is False
        and spec["change_control"].get("declared_change")
        == "none; unchanged convergence continuation"
        and implementation.is_file()
        and sha256(implementation) == spec["change_control"].get("implementation_sha256")
        and copied_dictionaries_and_mesh_gate
        and copied_fields_gate
    )

    solver_stage, log_path = _solver_stage(case, execution)
    log = log_path.read_text()
    printed_coefficients = coefficient_block(log, "RAS")
    coefficient_gate = all(
        name in printed_coefficients and close_enough(printed_coefficients[name], expected)
        for name, expected in STOCK_SST_COEFFICIENTS.items()
    )
    expected_model = {
        "solver": "simpleFoam",
        "ras_model": "kOmegaSST",
        "variant": "openfoam-v2512-kOmegaSST-default-coefficients",
        "runtime_library": None,
        "image_id": EXPECTED_IMAGE_ID,
    }
    model_gate = (
        spec.get("model_mapping") == expected_model
        and "Selecting RAS turbulence model kOmegaSST" in log
        and coefficient_gate
        and re.search(r"\bF3\s+false;", log) is not None
        and re.search(r"\bdecayControl\s+false;", log) is not None
    )
    runtime_gate = (
        len(execution) == 4
        and all(stage.get("stage_passed") is True for stage in execution)
        and all(stage.get("network_disabled") is True for stage in execution)
        and all(stage.get("image_id") == EXPECTED_IMAGE_ID for stage in execution)
        and all(stage.get("mpi_ranks") == 12 for stage in execution)
        and all(stage.get("resource_limits") == {"cpus": 12.0, "memory": "24g"} for stage in execution)
        and image.get("Id") == EXPECTED_IMAGE_ID
        and solver_stage.get("returncode") == 0
    )

    names, values = coefficient_history(case)
    indices = {name: index for index, name in enumerate(names)}
    if len(values) < max(window, 500):
        raise ValueError("Need at least 500 force samples for the declared gates")
    finite_gate = bool(np.isfinite(values).all())
    horizon_gate = bool(values[-1, indices["Time"]] == 5000)
    means = {
        name: float(np.mean(values[-window:, indices[name]]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    ranges = {
        name: float(np.ptp(values[-window:, indices[name]]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    settling_limits = {
        name: max(0.001, 0.01 * abs(means[name]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    settling_gate = all(ranges[name] <= settling_limits[name] for name in ranges)
    projected, trend_limits, trend_gate = long_window_trend(values, indices, 0.0, 500)
    final_residuals, residual_max, residual_gate = residuals(log, window)
    symmetry_gate = abs(means["Cl"]) <= 0.004 and abs(means["CmPitch"]) <= 0.0002

    reference = cfl3d_reference(benchmark_data / "n0012clcd_cfl3d_sst.dat")
    delta_reference = means["Cd"] - reference["Cd"]
    force_agreement_gate = abs(delta_reference) <= 0.0002
    source_names, source_values = coefficient_history(source)
    source_indices = {name: index for index, name in enumerate(source_names)}
    source_mean_cd = float(np.mean(source_values[-window:, source_indices["Cd"]]))
    source_last = {
        name: float(source_values[-1, source_indices[name]])
        for name in ("Cd", "Cl", "CmPitch")
    }
    continuation_first = {
        name: float(values[0, indices[name]]) for name in ("Cd", "Cl", "CmPitch")
    }
    initialization_jump = {
        name: continuation_first[name] - source_last[name]
        for name in ("Cd", "Cl", "CmPitch")
    }

    bounding_pattern = re.compile(
        r"bounding k, min: ([0-9.eE+-]+) max: ([0-9.eE+-]+) average: ([0-9.eE+-]+)"
    )
    bounding_rows = [tuple(float(value) for value in row) for row in bounding_pattern.findall(log)]
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
        "scope": "Unchanged stock-SST convergence continuation downstream of failed Gate 1",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "plan": str(plan_path),
        "plan_sha256": sha256(plan_path),
        "source_case": str(source),
        "source_audit": str(source_audit_path),
        "source_audit_sha256": sha256(source_audit_path),
        "source_plan_gate": source_plan_gate,
        "source_trigger_gate": trigger_gate,
        "provenance_gate": provenance_gate,
        "copied_dictionaries_and_mesh_gate": copied_dictionaries_and_mesh_gate,
        "copied_solution_fields_gate": copied_fields_gate,
        "runtime_and_execution_gate": runtime_gate,
        "model_configuration_gate": model_gate,
        "stock_sst_coefficients": printed_coefficients,
        "stock_sst_coefficients_gate": coefficient_gate,
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
        "solver_initial_residuals_last_100_max": residual_max,
        "solver_residual_gate": residual_gate,
        "zero_angle_symmetry_gate": symmetry_gate,
        "cfl3d_sst_reference": reference,
        "openfoam_minus_cfl3d_sst_cd": delta_reference,
        "force_agreement_gate": force_agreement_gate,
        "source_stock_sst_mean_cd": source_mean_cd,
        "continuation_minus_source_stock_sst_cd": means["Cd"] - source_mean_cd,
        "initialization_force_jump": {
            "classification": "report_only",
            "source_last": source_last,
            "continuation_first": continuation_first,
            "difference": initialization_jump,
        },
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
        "strict_gate_2_passed": False,
        "strict_gate_2_status": "blocked_by_failed_gate_1",
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
    output = args.output / "naca0012-stock-sst-continuation-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
