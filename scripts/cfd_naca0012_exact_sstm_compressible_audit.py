"""Audit the matched exact-SSTm incompressible-to-compressible rung."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

import numpy as np

from cfd_flat_plate_model_audit import close_enough, coefficient_block
from cfd_naca0012_exact_sstm_compressible_restart import (
    COPIED_FIELDS,
    IMAGE_PROVENANCE,
    METHOD,
    PLAN,
)
from cfd_naca0012_force_audit import coefficient_history, long_window_trend
from cfd_naca0012_map_fields import latest_time, parse_internal_field
from cfd_naca0012_stock_sst_audit import cfl3d_reference, sha256
from cfd_naca0012_stock_sst_restart import reset_field_location


def _solver_stage(case: Path, execution: list[dict]) -> tuple[dict, Path]:
    matches = [
        (index, stage)
        for index, stage in enumerate(execution)
        if "rhoSimpleFoam" in stage.get("stage", "")
    ]
    if len(matches) != 1:
        raise ValueError("Expected exactly one rhoSimpleFoam execution stage")
    index, stage = matches[0]
    return stage, case / f"{index}-{stage['stage'].split()[0]}.log"


def compressible_residuals(log: str, window: int = 100) -> tuple[dict, dict, bool]:
    fields = ("p", "Ux", "Uy", "e", "k", "omega")
    histories = {name: [] for name in fields}
    pattern = re.compile(
        r"Solving (?:for )?(p|Ux|Uy|e|k|omega), Initial residual = ([0-9.eE+-]+)"
    )
    for name, value in pattern.findall(log):
        histories[name].append(float(value))
    missing = [name for name, values in histories.items() if len(values) < window]
    if missing:
        raise ValueError(f"Need at least {window} residual samples for {missing}")
    final = {name: values[-1] for name, values in histories.items()}
    recent_max = {name: max(values[-window:]) for name, values in histories.items()}
    return final, recent_max, all(value <= 1e-5 for value in recent_max.values())


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
    record = json.loads((case / "compressible-restart-execution.json").read_text())
    source = Path(spec["initialization"]["source_case"]).resolve(strict=True)
    source_audit_path = Path(spec["initialization"]["source_audit"]).resolve(strict=True)
    source_audit = json.loads(source_audit_path.read_text())
    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    source_gate = all(
        (
            source == Path(plan["source"]["case"]).resolve(),
            sha256(source_spec_path) == plan["source"]["case_spec_sha256"],
            source_audit_path == Path(plan["source"]["audit"]).resolve(),
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

    mesh_hashes = spec["change_control"]["copied_mesh_sha256"]
    copied_mesh_gate = all(
        source.joinpath(relative).is_file()
        and case.joinpath(relative).is_file()
        and sha256(source / relative) == expected
        and sha256(case / relative) == expected
        for relative, expected in mesh_hashes.items()
    )
    source_time = latest_time(source)
    copied_fields_gate = all(
        (case / "0" / name).read_text()
        == reset_field_location((source_time / name).read_text())
        for name in COPIED_FIELDS
    )

    thermo = plan["declared_changes"]["thermodynamics"]
    cells = (spec["grid_dimensions"][0] - 1) * (spec["grid_dimensions"][1] - 1)
    source_p_kind, source_p = parse_internal_field((source_time / "p").read_text(), cells)
    target_p_kind, target_p = parse_internal_field((case / "0" / "p").read_text(), cells)
    pressure_mapping_gate = all(
        (
            source_p_kind == "scalar",
            target_p_kind == "scalar",
            np.allclose(
                target_p,
                thermo["pressure_pa"] + thermo["density_kg_m3"] * source_p,
                rtol=1e-12,
                atol=1e-8,
            ),
        )
    )
    gas_constant = 8314.46261815324 / thermo["molecular_weight_kg_kmol"]
    calculated_temperature = (thermo["velocity_m_s"] / thermo["mach"]) ** 2 / (
        thermo["gamma"] * gas_constant
    )
    calculated_density = thermo["pressure_pa"] / (gas_constant * calculated_temperature)
    calculated_mu = calculated_density * thermo["kinematic_viscosity_m2_s"]
    calculated_as = calculated_mu * (
        calculated_temperature + thermo["sutherland_temperature_k"]
    ) / calculated_temperature**1.5
    calculated_reynolds = (
        calculated_density * thermo["velocity_m_s"] / calculated_mu
    )
    derived_thermo_gate = all(
        math.isclose(observed, expected, rel_tol=1e-12, abs_tol=1e-15)
        for observed, expected in (
            (calculated_temperature, thermo["temperature_k"]),
            (calculated_density, thermo["density_kg_m3"]),
            (calculated_mu, thermo["dynamic_viscosity_pa_s"]),
            (calculated_as, thermo["sutherland_as"]),
            (calculated_reynolds, source_spec["conditions"]["reynolds_number"]),
        )
    )
    thermophysical = (case / "constant" / "thermophysicalProperties").read_text()
    thermo_dictionary_gate = all(
        re.search(pattern, thermophysical) is not None
        for pattern in (
            r"transport\s+sutherlandPr;",
            r"equationOfState\s+perfectGas;",
            r"energy\s+sensibleInternalEnergy;",
            rf"molWeight\s+{thermo['molecular_weight_kg_kmol']:.15g};",
            rf"Cp\s+{thermo['cp_j_kg_k']:.15g};",
            rf"As\s+{thermo['sutherland_as']:.15g};",
            rf"Ts\s+{thermo['sutherland_temperature_k']:.15g};",
            rf"Pr\s+{thermo['molecular_prandtl']:.15g};",
        )
    )
    conditions_gate = all(
        math.isclose(spec["conditions"][key], expected, rel_tol=1e-12, abs_tol=1e-15)
        for key, expected in (
            ("speed_m_s", thermo["velocity_m_s"]),
            ("mach", thermo["mach"]),
            ("reynolds_number", calculated_reynolds),
            ("pressure_pa", thermo["pressure_pa"]),
            ("temperature_k", thermo["temperature_k"]),
            ("density_kg_m3", thermo["density_kg_m3"]),
            ("dynamic_viscosity_pa_s", thermo["dynamic_viscosity_pa_s"]),
            ("kinematic_viscosity_m2_s", thermo["kinematic_viscosity_m2_s"]),
        )
    )
    thermodynamic_mapping_gate = all(
        (
            pressure_mapping_gate,
            derived_thermo_gate,
            thermo_dictionary_gate,
            conditions_gate,
        )
    )

    change = spec["change_control"]
    implementation = Path(change["implementation_snapshot"])
    plan_snapshot = case / "provenance" / plan_path.name
    image_snapshot = case / "provenance" / IMAGE_PROVENANCE.name
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
            image_snapshot.is_file(),
            sha256(image_snapshot) == sha256(IMAGE_PROVENANCE),
            change.get("declared_change")
            == "incompressible simpleFoam to matched compressible rhoSimpleFoam closure only",
        )
    )
    provenance_gate = all(
        (
            source_gate,
            copied_mesh_gate,
            copied_fields_gate,
            thermodynamic_mapping_gate,
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
        "solver": "rhoSimpleFoam",
        "runtime_model": "TmrSSTmExactProduction",
        "variant": "tmr-sstm-exact-production-v2512-source-audited",
        "runtime_library": "libTmrSSTmExactProductionCompressible.so",
        "transport_library": "libSutherlandPrTransport.so",
        "image_id": expected_image_id,
    }
    coefficients = coefficient_block(log, "RAS")
    coefficient_gate = all(
        close_enough(coefficients.get(name), expected)
        for name, expected in (
            ("gamma1", 0.5531666666666668),
            ("gamma2", 0.4403546666666667),
            ("c1", 20.0),
            ("Prt", thermo["turbulent_prandtl"]),
        )
    )
    model_gate = all(
        (
            spec.get("model_mapping") == expected_mapping,
            "Selecting RAS turbulence model TmrSSTmExactProduction" in log,
            re.search(r"transport\s+sutherlandPr;", log) is not None,
            coefficient_gate,
        )
    )

    names, values = coefficient_history(case)
    if len(values) < 500:
        raise ValueError("Need at least 500 compressible force samples")
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
    final_residuals, recent_max_residuals, residual_gate = compressible_residuals(log, window)
    symmetry_gate = abs(means["Cl"]) <= 0.004 and abs(means["CmPitch"]) <= 0.0002
    reference = cfl3d_reference(benchmark_data / "n0012clcd_cfl3d_sst.dat")
    delta_reference = means["Cd"] - reference["Cd"]
    force_agreement_gate = abs(delta_reference) <= 0.0002
    source_names, source_values = coefficient_history(source)
    source_indices = {name: index for index, name in enumerate(source_names)}
    source_mean_cd = float(np.mean(source_values[-window:, source_indices["Cd"]]))
    delta_source = means["Cd"] - source_mean_cd
    limiter_rows = [
        (
            kind,
            int(cells_limited),
            float(percent),
            float(limit_value),
            float(extreme),
        )
        for kind, cells_limited, percent, limit_value, extreme in re.findall(
            r"Type=(Lower|Upper), LimitedCells=(\d+), CellsPercent=([0-9.eE+-]+), "
            r"T(?:min|max)=([0-9.eE+-]+), UnlimitedT(?:min|max)=([0-9.eE+-]+)",
            log,
        )
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
        "scope": "Matched exact NASA SSTm compressible relative diagnostic downstream of failed Gate 1",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "plan": str(plan_path),
        "plan_sha256": sha256(plan_path),
        "source_case": str(source),
        "source_audit": str(source_audit_path),
        "source_audit_sha256": sha256(source_audit_path),
        "source_gate": source_gate,
        "copied_mesh_gate": copied_mesh_gate,
        "copied_solution_fields_gate": copied_fields_gate,
        "pressure_mapping_gate": pressure_mapping_gate,
        "derived_thermodynamics_gate": derived_thermo_gate,
        "thermophysical_dictionary_gate": thermo_dictionary_gate,
        "conditions_gate": conditions_gate,
        "thermodynamic_mapping_gate": thermodynamic_mapping_gate,
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
        "source_incompressible_exact_sstm_mean_cd": source_mean_cd,
        "compressible_minus_incompressible_cd": delta_source,
        "temperature_limiter_diagnostic": {
            "classification": "post_hoc_report_only_not_an_acceptance_gate",
            "rows_parsed": len(limiter_rows),
            "final_200_all_zero_limited_cells": bool(limiter_rows)
            and all(row[1] == 0 for row in limiter_rows[-200:]),
        },
        "diagnostic_numerics_passed": diagnostic_numerics_passed,
        "strict_gate_4_passed": False,
        "strict_gate_4_status": "blocked_by_failed_gate_1",
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
    output = args.output / "naca0012-exact-sstm-compressible-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
