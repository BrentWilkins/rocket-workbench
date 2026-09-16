"""Audit the direct SA-to-stock-SST NACA 0012 relative diagnostic."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np

from cfd_naca0012_force_audit import coefficient_history, long_window_trend
from cfd_flat_plate_model_audit import close_enough, coefficient_block


PLAN = Path(__file__).resolve().parents[1] / "cfd" / "naca0012-stock-sst-relative-diagnostic-plan.json"
EXPECTED_IMAGE_ID = "sha256:02a68093f2f25f07137cc5aafc20c96a0f26cb0f91aefb879ad1911a75ce6267"
REFERENCE_SHA256 = "373dc142018816628b7b53ad278327db731162988ba35a166cd9fdc131a7fd7a"
STOCK_SST_COEFFICIENTS = {
    "alphaK1": 0.85,
    "alphaK2": 1.0,
    "alphaOmega1": 0.5,
    "alphaOmega2": 0.856,
    "gamma1": 0.5555555556,
    "gamma2": 0.44,
    "beta1": 0.075,
    "beta2": 0.0828,
    "betaStar": 0.09,
    "a1": 0.31,
    "b1": 1.0,
    "c1": 10.0,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def cfl3d_reference(path: Path) -> dict:
    if sha256(path) != REFERENCE_SHA256:
        raise ValueError("NASA CFL3D SST coefficient reference checksum mismatch")
    rows = []
    for line in path.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith(("#", "variables")):
            rows.append([float(value) for value in line.split()])
    matches = [row for row in rows if row[0] == 0.0]
    if len(matches) != 1:
        raise ValueError("Expected one zero-angle CFL3D SST row")
    alpha, cl, cd = matches[0]
    return {"alpha_deg": alpha, "Cl": cl, "Cd": cd, "sha256": REFERENCE_SHA256}


def residuals(log: str, window: int = 100) -> tuple[dict, dict, bool]:
    histories = {}
    for name in ("p", "Ux", "Uy", "k", "omega"):
        pattern = re.compile(rf"Solving for {name}, Initial residual = ([0-9.eE+-]+)")
        histories[name] = [float(value) for value in pattern.findall(log)]
    missing = [name for name, values in histories.items() if len(values) < window]
    if missing:
        raise ValueError(f"Need at least {window} residual samples for {missing}")
    final = {name: values[-1] for name, values in histories.items()}
    recent_max = {name: max(values[-window:]) for name, values in histories.items()}
    passed = all(value <= 1e-5 for value in recent_max.values())
    return final, recent_max, passed


def _solver_stage(case: Path, execution: list[dict]) -> tuple[dict, Path]:
    matches = [
        (index, stage)
        for index, stage in enumerate(execution)
        if "simpleFoam" in stage.get("stage", "")
    ]
    if len(matches) != 1:
        raise ValueError("Expected exactly one simpleFoam execution stage")
    index, stage = matches[0]
    log_path = case / f"{index}-{stage['stage'].split()[0]}.log"
    return stage, log_path


def normalized_location(text: str) -> str:
    updated, count = re.subn(r'location\s+"[^"]+";', 'location "0";', text, count=1)
    if count != 1:
        raise ValueError("Expected exactly one field location")
    return updated


def audit(case: Path, benchmark_data: Path, window: int = 100) -> dict:
    case = case.resolve(strict=True)
    benchmark_data = benchmark_data.resolve(strict=True)
    plan = json.loads(PLAN.read_text())
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    execution = json.loads((case / "execution.json").read_text())
    image = json.loads((case / "image.json").read_text())
    restart = json.loads((case / "stock-sst-restart-execution.json").read_text())
    solver_stage, log_path = _solver_stage(case, execution)
    log = log_path.read_text()

    expected_model = {
        "solver": "simpleFoam",
        "ras_model": "kOmegaSST",
        "variant": "openfoam-v2512-kOmegaSST-default-coefficients",
        "runtime_library": None,
        "image_id": EXPECTED_IMAGE_ID,
    }
    printed_coefficients = coefficient_block(log, "RAS")
    stock_coefficients_gate = all(
        name in printed_coefficients and close_enough(printed_coefficients[name], expected)
        for name, expected in STOCK_SST_COEFFICIENTS.items()
    )
    model_configuration_gate = (
        spec.get("model_mapping") == expected_model
        and "Selecting RAS turbulence model kOmegaSST" in log
        and stock_coefficients_gate
        and re.search(r"\bF3\s+false;", log) is not None
        and re.search(r"\bdecayControl\s+false;", log) is not None
        and "RASModel kOmegaSST;" in (case / "constant" / "turbulenceProperties").read_text()
        and not (case / "0" / "nuTilda").exists()
        and all((case / "0" / name).is_file() for name in ("k", "omega", "nut"))
    )

    change = spec.get("change_control", {})
    source_case = Path(spec.get("initialization", {}).get("source_case", ""))
    source_audit = Path(spec.get("initialization", {}).get("source_audit", ""))
    implementation = Path(change.get("implementation_snapshot", ""))
    copied = change.get("copied_source_file_sha256", {})
    immutable_files = {
        "constant/transportProperties",
        "system/controlDict",
        "system/decomposeParDict",
    }
    copied_invariants_gate = all(
        source_case.joinpath(relative).is_file()
        and case.joinpath(relative).is_file()
        and sha256(source_case / relative) == digest
        and sha256(case / relative) == digest
        for relative, digest in copied.items()
        if relative.startswith("constant/polyMesh/") or relative in immutable_files
    )
    schemes = (case / "system" / "fvSchemes").read_text()
    reversed_schemes = schemes.replace(
        "div(phi,k) bounded Gauss linearUpwind grad(k);\n"
        " div(phi,omega) bounded Gauss linearUpwind grad(omega);",
        "div(phi,nuTilda) bounded Gauss linearUpwind grad(nuTilda);",
    )
    solution = (case / "system" / "fvSolution").read_text()
    reversed_solution = solution.replace(
        '"(k|omega)" { solver smoothSolver; smoother GaussSeidel; nSweeps 2; tolerance 1e-9; relTol 0.01; }',
        "nuTilda { solver smoothSolver; smoother GaussSeidel; nSweeps 2; tolerance 1e-9; relTol 0.01; }",
    ).replace('"(k|omega)" 0.35;', "nuTilda 0.35;")
    required_numerics_only_gate = (
        reversed_schemes == (source_case / "system" / "fvSchemes").read_text()
        and reversed_solution == (source_case / "system" / "fvSolution").read_text()
    )
    source_time = spec["initialization"]["source_time"]
    source_time_name = str(int(source_time)) if float(source_time).is_integer() else str(source_time)
    copied_flow_fields_gate = all(
        (case / "0" / name).read_text()
        == normalized_location((source_case / source_time_name / name).read_text())
        for name in ("U", "p")
    )
    provenance_gate = (
        restart.get("stage_passed") is True
        and restart.get("stage") == plan["name"]
        and restart.get("plan_sha256") == sha256(PLAN)
        and restart.get("target_case_spec_sha256") == sha256(spec_path)
        and change.get("plan_sha256") == sha256(PLAN)
        and implementation.is_file()
        and change.get("implementation_sha256") == sha256(implementation)
        and source_audit.is_file()
        and spec["initialization"].get("source_audit_sha256") == sha256(source_audit)
        and spec["initialization"].get("source_gate_1_passed") is False
        and spec.get("strict_gate_2_status") == "blocked_by_failed_gate_1"
        and copied_invariants_gate
        and required_numerics_only_gate
        and copied_flow_fields_gate
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
        raise ValueError("Need at least 500 force samples for the declared trend gate")
    finite_force_history_gate = bool(np.isfinite(values).all())
    iteration_horizon_gate = bool(values[-1, indices["Time"]] == 5000)
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
    bounding_pattern = re.compile(
        r"bounding k, min: ([0-9.eE+-]+) max: ([0-9.eE+-]+) average: ([0-9.eE+-]+)"
    )
    bounding_rows = [tuple(float(value) for value in row) for row in bounding_pattern.findall(log)]
    bounding_diagnostic = {
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
    }
    symmetry_gate = abs(means["Cl"]) <= 0.004 and abs(means["CmPitch"]) <= 0.0002

    reference = cfl3d_reference(benchmark_data / "n0012clcd_cfl3d_sst.dat")
    delta_reference = means["Cd"] - reference["Cd"]
    force_agreement_gate = abs(delta_reference) <= 0.0002
    source_names, source_values = coefficient_history(source_case)
    source_indices = {name: index for index, name in enumerate(source_names)}
    source_mean_cd = float(np.mean(source_values[-window:, source_indices["Cd"]]))
    delta_source = means["Cd"] - source_mean_cd

    diagnostic_numerics_passed = all(
        (
            provenance_gate,
            runtime_gate,
            model_configuration_gate,
            finite_force_history_gate,
            iteration_horizon_gate,
            settling_gate,
            trend_gate,
            residual_gate,
            symmetry_gate,
        )
    )
    return {
        "schema_version": 1,
        "scope": "Direct SA-to-stock-SST relative diagnostic downstream of failed Gate 1",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "plan": str(PLAN),
        "plan_sha256": sha256(PLAN),
        "provenance_gate": provenance_gate,
        "copied_mesh_and_transport_gate": copied_invariants_gate,
        "required_numerics_only_gate": required_numerics_only_gate,
        "copied_sa_velocity_and_pressure_gate": copied_flow_fields_gate,
        "runtime_and_execution_gate": runtime_gate,
        "model_configuration_gate": model_configuration_gate,
        "stock_sst_coefficients": printed_coefficients,
        "stock_sst_coefficients_gate": stock_coefficients_gate,
        "finite_force_history_gate": finite_force_history_gate,
        "iteration_horizon_gate": iteration_horizon_gate,
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
        "bounded_k_diagnostic": bounding_diagnostic,
        "zero_angle_symmetry_gate": symmetry_gate,
        "cfl3d_sst_reference": reference,
        "openfoam_minus_cfl3d_sst_cd": delta_reference,
        "force_agreement_gate": force_agreement_gate,
        "source_sa_mean_cd": source_mean_cd,
        "stock_sst_minus_source_sa_cd": delta_source,
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
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = audit(args.case, args.benchmark_data, args.window)
    args.output.mkdir(parents=True)
    output = args.output / "naca0012-stock-sst-diagnostic-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
