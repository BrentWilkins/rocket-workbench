"""Audit the predeclared stock-SST turbulence-upwind remediation."""

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
from cfd_naca0012_stock_sst_restart import reset_field_location
from cfd_naca0012_stock_sst_upwind_restart import (
    FIELDS,
    METHOD,
    PLAN,
    _replace_once,
)


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


def audit(case: Path, benchmark_data: Path, window: int = 100) -> dict:
    case = case.resolve(strict=True)
    benchmark_data = benchmark_data.resolve(strict=True)
    plan = json.loads(PLAN.read_text())
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    execution = json.loads((case / "execution.json").read_text())
    image = json.loads((case / "image.json").read_text())
    record = json.loads((case / "stock-sst-upwind-restart-execution.json").read_text())

    source = Path(spec["initialization"]["source_case"]).resolve(strict=True)
    source_audit_path = Path(spec["initialization"]["source_audit"]).resolve(strict=True)
    source_audit = json.loads(source_audit_path.read_text())
    source_spec_path = source / "benchmark-spec.json"

    required_state_gate = all(
        (
            source_audit.get("bounded_k_diagnostic", {}).get("occurrences")
            if name == "bounded_k_occurrences"
            else source_audit.get(name)
        )
        == expected
        for name, expected in plan["source"]["required_state"].items()
    )
    copied = spec["change_control"]["copied_source_file_sha256"]
    copied_invariants_gate = all(
        source.joinpath(relative).is_file()
        and case.joinpath(relative).is_file()
        and sha256(source / relative) == expected
        and sha256(case / relative) == expected
        for relative, expected in copied.items()
    )
    copied_fields_gate = all(
        sha256(source / entry["source"].split(str(source) + "/", 1)[-1])
        == entry["source_sha256"]
        and sha256(case / "0" / name) == entry["target_sha256"]
        and (case / "0" / name).read_text()
        == reset_field_location(Path(entry["source"]).read_text())
        for name, entry in spec["initialization"]["fields"].items()
        if name in FIELDS
    ) and set(spec["initialization"]["fields"]) == set(FIELDS)

    source_schemes = (source / "system" / "fvSchemes").read_text()
    expected_schemes = _replace_once(
        source_schemes,
        "div(phi,k) bounded Gauss linearUpwind grad(k);",
        "div(phi,k) bounded Gauss upwind;",
    )
    expected_schemes = _replace_once(
        expected_schemes,
        "div(phi,omega) bounded Gauss linearUpwind grad(omega);",
        "div(phi,omega) bounded Gauss upwind;",
    )
    target_schemes = (case / "system" / "fvSchemes").read_text()
    scheme_change_gate = (
        target_schemes == expected_schemes
        and spec["numerics"].get("k_convection") == "bounded Gauss upwind"
        and spec["numerics"].get("omega_convection") == "bounded Gauss upwind"
        and spec["numerics"].get("velocity_convection")
        == "bounded Gauss linearUpwind grad(U)"
        and spec["change_control"].get("source_fvSchemes_sha256")
        == sha256(source / "system" / "fvSchemes")
        and spec["change_control"].get("target_fvSchemes_sha256")
        == sha256(case / "system" / "fvSchemes")
    )

    implementation = case / "provenance" / spec["change_control"]["implementation"]
    provenance_gate = (
        sha256(source_spec_path) == plan["source"]["case_spec_sha256"]
        and sha256(source_audit_path) == plan["source"]["audit_sha256"]
        and Path(source_audit.get("case", "")).resolve() == source
        and required_state_gate
        and record.get("stage") == METHOD
        and record.get("stage_passed") is True
        and record.get("source_audit_sha256") == sha256(source_audit_path)
        and record.get("plan_sha256") == sha256(PLAN)
        and record.get("target_case_spec_sha256") == sha256(spec_path)
        and implementation.is_file()
        and sha256(implementation) == spec["change_control"].get("implementation_sha256")
        and copied_invariants_gate
        and copied_fields_gate
        and scheme_change_gate
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
        and all(
            stage.get("resource_limits") == {"cpus": 12.0, "memory": "24g"}
            for stage in execution
        )
        and image.get("Id") == EXPECTED_IMAGE_ID
        and solver_stage.get("returncode") == 0
    )

    names, values = coefficient_history(case)
    indices = {name: index for index, name in enumerate(names)}
    if len(values) < max(window, 500):
        raise ValueError("Need at least 500 force samples for declared gates")
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
        name: max(0.001, 0.01 * abs(means[name])) for name in means
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
    source_means = {
        name: float(np.mean(source_values[-window:, source_indices[name]]))
        for name in ("Cd", "Cl", "CmPitch")
    }

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
        "scope": "Stock-SST turbulence-upwind symmetry remediation downstream of failed Gate 1",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "plan": str(PLAN),
        "plan_sha256": sha256(PLAN),
        "source_case": str(source),
        "source_audit": str(source_audit_path),
        "source_audit_sha256": sha256(source_audit_path),
        "source_required_state_gate": required_state_gate,
        "provenance_gate": provenance_gate,
        "copied_invariants_gate": copied_invariants_gate,
        "copied_solution_fields_gate": copied_fields_gate,
        "scheme_change_only_gate": scheme_change_gate,
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
        "upwind_minus_source": {
            name: means[name] - source_means[name] for name in means
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
        "remediation_passed": diagnostic_numerics_passed,
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
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = audit(args.case, args.benchmark_data, args.window)
    args.output.mkdir(parents=True)
    output = args.output / "naca0012-stock-sst-upwind-remediation-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
