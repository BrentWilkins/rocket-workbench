"""Audit the documented OpenFOAM/NASA Spalart-Allmaras NACA 0012 control."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np

from cfd_naca0012_force_audit import coefficient_history, long_window_trend
from cfd_naca0012_sa_control_case import IMAGE_ID


REFERENCE_SHA256 = "b07afec6ce3ae4bf2f2d1a1d53785fde0a5ca68481a0d4186aa92754d811944e"
FOUNDATION_V4_IMAGE_ID = (
    "sha256:e644ef04fd37619f48c2226f2aa9496bcaec2716546671e09ad37d9d850f7e36"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def residual_gate(log: str, window: int = 100) -> tuple[dict, dict, bool]:
    patterns = {
        name: re.compile(rf"Solving for {name}, Initial residual = ([0-9.eE+-]+)")
        for name in ("p", "Ux", "Uy", "nuTilda")
    }
    histories = {
        name: [float(value) for value in pattern.findall(log)]
        for name, pattern in patterns.items()
    }
    missing = [name for name, values in histories.items() if len(values) < window]
    if missing:
        raise ValueError(f"Need at least {window} residual samples for {missing}")
    final = {name: values[-1] for name, values in histories.items()}
    recent_max = {name: max(values[-window:]) for name, values in histories.items()}
    passed = all(value <= 1e-5 for value in final.values()) and all(
        value <= 1e-4 for value in recent_max.values()
    )
    return final, recent_max, passed


def cfl3d_reference(path: Path) -> dict:
    if sha256(path) != REFERENCE_SHA256:
        raise ValueError("NASA CFL3D SA coefficient reference checksum mismatch")
    rows = []
    for line in path.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith(("#", "variables")):
            continue
        rows.append([float(value) for value in line.split()])
    matches = [row for row in rows if row[0] == 0.0]
    if len(matches) != 1:
        raise ValueError("Expected exactly one zero-angle CFL3D SA row")
    alpha, cl, cd = matches[0]
    return {"alpha_deg": alpha, "cl": cl, "cd": cd, "sha256": REFERENCE_SHA256}


def audit(case: Path, benchmark_data: Path, window: int = 100) -> dict:
    case = case.resolve(strict=True)
    benchmark_data = benchmark_data.resolve(strict=True)
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    execution = json.loads((case / "execution.json").read_text())
    image = json.loads((case / "image.json").read_text())
    solver_stages = [
        (index, stage)
        for index, stage in enumerate(execution)
        if "simpleFoam" in stage.get("stage", "")
    ]
    if len(solver_stages) != 1:
        raise ValueError("Expected exactly one simpleFoam execution stage")
    solver_index, solver_stage = solver_stages[0]
    log_path = case / f"{solver_index}-{solver_stage['stage'].split()[0]}.log"
    log = log_path.read_text()

    initialization = spec.get("initialization")
    restart_provenance_gate = True
    if initialization is not None:
        record_path = case / "sa-continuation-execution.json"
        record = json.loads(record_path.read_text())
        snapshot = Path(initialization["implementation_snapshot"])
        source_audit = Path(initialization["source_audit"])
        method = initialization.get("method")
        exact_continuation = (
            method == "same-grid documented-SA convergence continuation"
            and initialization.get("physics_or_numerics_changed") is False
        )
        damping_test = (
            method == "same-grid documented-SA half-relaxation mechanism test"
            and initialization.get("physics_or_numerics_changed") is True
        )
        serial_test = (
            method == "same-grid documented-SA serial-execution mechanism test"
            and initialization.get("physics_or_numerics_changed") is False
        )
        ratio_test = (
            method == "same-grid documented-SA freestream-ratio sensitivity"
            and initialization.get("physics_or_numerics_changed") is True
        )
        ft2_test = (
            method == "same-grid exact standard-SA ft2 sensitivity"
            and initialization.get("physics_or_numerics_changed") is True
        )
        nonorthogonal_test = (
            method == "same-grid documented-SA non-orthogonal-corrector screen"
            and initialization.get("physics_or_numerics_changed") is True
        )
        foundation_v4_test = (
            method == "same-grid documented-SA OpenFOAM Foundation v4 lineage screen"
            and initialization.get("physics_or_numerics_changed") is True
        )
        common_provenance = (
            record.get("stage_passed") is True
            and sha256(snapshot) == initialization.get("implementation_sha256")
            and sha256(source_audit) == initialization.get("source_audit_sha256")
            and all(
                sha256(case / "0" / name) == metadata["restart_sha256"]
                for name, metadata in initialization["fields"].items()
            )
        )
        mechanism_provenance = True
        if damping_test:
            mechanism = spec.get("mechanism_test", {})
            mechanism_snapshot = Path(mechanism["implementation_snapshot"])
            plan = Path(mechanism["plan"])
            mechanism_provenance = (
                mechanism.get("only_numerical_relaxation_changed") is True
                and sha256(mechanism_snapshot)
                == mechanism.get("implementation_sha256")
                and sha256(plan) == mechanism.get("plan_sha256")
                and sha256(case / "system" / "fvSolution")
                == record.get("fv_solution_sha256")
            )
        if serial_test:
            mechanism = spec.get("mechanism_test", {})
            mechanism_snapshot = Path(mechanism["implementation_snapshot"])
            plan = Path(mechanism["plan"])
            mechanism_provenance = (
                mechanism.get("only_execution_decomposition_changed") is True
                and mechanism.get("after", {}).get("mpi_ranks") == 1
                and sha256(mechanism_snapshot)
                == mechanism.get("implementation_sha256")
                and sha256(plan) == mechanism.get("plan_sha256")
                and sha256(case / "system" / "controlDict")
                == record.get("control_dict_sha256")
            )
        if ratio_test:
            mechanism = spec.get("mechanism_test", {})
            mechanism_snapshot = Path(mechanism["implementation_snapshot"])
            plan = Path(mechanism["plan"])
            mechanism_provenance = (
                mechanism.get("only_farfield_nuTilda_changed") is True
                and mechanism.get("before", {}).get("nuTilda_to_nu_ratio") == 4.0
                and mechanism.get("after", {}).get("nuTilda_to_nu_ratio") == 3.0
                and mechanism.get("model_ft2") is False
                and sha256(mechanism_snapshot)
                == mechanism.get("implementation_sha256")
                and sha256(plan) == mechanism.get("plan_sha256")
                and sha256(case / "0" / "nuTilda")
                == record.get("nuTilda_restart_sha256")
            )
        if ft2_test:
            mechanism = spec.get("mechanism_test", {})
            mechanism_snapshot = Path(mechanism["implementation_snapshot"])
            plan = Path(mechanism["plan"])
            mechanism_provenance = (
                mechanism.get("only_ft2_switch_changed") is True
                and mechanism.get("before", {}).get("ft2") is False
                and mechanism.get("after", {}).get("ft2") is True
                and mechanism.get("nuTilda_to_nu_ratio") == 3.0
                and sha256(mechanism_snapshot)
                == mechanism.get("implementation_sha256")
                and sha256(plan) == mechanism.get("plan_sha256")
                and sha256(case / "constant" / "turbulenceProperties")
                == record.get("turbulence_properties_sha256")
            )
        if nonorthogonal_test:
            mechanism = spec.get("mechanism_test", {})
            mechanism_snapshot = Path(mechanism["implementation_snapshot"])
            plan = Path(mechanism["plan"])
            mechanism_provenance = (
                mechanism.get("only_nNonOrthogonalCorrectors_changed") is True
                and mechanism.get("before", {}).get("nNonOrthogonalCorrectors") == 0
                and mechanism.get("after", {}).get("nNonOrthogonalCorrectors") == 4
                and mechanism.get("additional_iterations") == 1000
                and sha256(mechanism_snapshot)
                == mechanism.get("implementation_sha256")
                and sha256(plan) == mechanism.get("plan_sha256")
                and sha256(case / "system" / "fvSolution")
                == record.get("fv_solution_sha256")
                and sha256(case / "system" / "controlDict")
                == record.get("control_dict_sha256")
            )
        if foundation_v4_test:
            mechanism = spec.get("mechanism_test", {})
            mechanism_snapshot = Path(mechanism["implementation_snapshot"])
            plan = Path(mechanism["plan"])
            mechanism_provenance = (
                mechanism.get("only_solver_and_model_lineage_changed") is True
                and mechanism.get("before", {}).get("version") == "v2512"
                and mechanism.get("after", {}).get("version") == "4.1"
                and mechanism.get("additional_iterations") == 1000
                and len(mechanism.get("compatibility_adapters", [])) == 3
                and sha256(mechanism_snapshot)
                == mechanism.get("implementation_sha256")
                and sha256(plan) == mechanism.get("plan_sha256")
                and sha256(case / "system" / "controlDict")
                == record.get("control_dict_sha256")
                and sha256(case / "system" / "fvSchemes")
                == record.get("fv_schemes_sha256")
                and sha256(case / "system" / "fvSolution")
                == record.get("fv_solution_sha256")
                and sha256(case / "constant" / "turbulenceProperties")
                == record.get("turbulence_properties_sha256")
            )
        restart_provenance_gate = (
            common_provenance
            and (
                exact_continuation
                or damping_test
                or serial_test
                or ratio_test
                or ft2_test
                or nonorthogonal_test
                or foundation_v4_test
            )
            and mechanism_provenance
        )

    provenance_gate = (
        spec.get("benchmark") == "TMR 2D NACA 0012"
        and spec.get("source", {}).get("archive_sha256")
        == "b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4"
        and spec.get("grid_dimensions") == [897, 257]
        and spec.get("reference", {}).get("sha256") == REFERENCE_SHA256
    )
    expected_execution_stages = (
        2
        if spec.get("mechanism_test", {}).get("after", {}).get("mpi_ranks") == 1
        else 4
    )
    expected_image_id = (
        FOUNDATION_V4_IMAGE_ID if initialization is not None and foundation_v4_test else IMAGE_ID
    )
    runtime_gate = (
        spec.get("model_mapping", {}).get("solver") == "simpleFoam"
        and spec.get("model_mapping", {}).get("ras_model") == "SpalartAllmaras"
        and spec.get("model_mapping", {}).get("runtime_library") is None
        and spec.get("model_mapping", {}).get("image_id") == expected_image_id
        and image.get("Id") == expected_image_id
        and len(execution) == expected_execution_stages
        and all(stage.get("stage_passed") for stage in execution)
    )
    model_gate = all(
        re.search(pattern, log)
        for pattern in (
            r"Selecting incompressible transport model Newtonian",
            r"Selecting RAS turbulence model SpalartAllmaras",
            r"sigmaNut\s+0\.66666",
            r"Cv1\s+7\.1",
        )
    )
    if spec.get("mechanism_test", {}).get("name") == "SpalartAllmaras_ft2_switch":
        model_gate = model_gate and "ft2 term: active" in log

    columns, values = coefficient_history(case)
    indices = {name: columns.index(name) for name in ("Time", "Cd", "Cl", "CmPitch")}
    if len(values) < max(window, 500):
        raise ValueError("Need at least 500 coefficient samples")
    tail = values[-window:]
    means = {
        name: float(tail[:, indices[name]].mean()) for name in ("Cd", "Cl", "CmPitch")
    }
    peak_to_peak = {
        name: float(np.ptp(tail[:, indices[name]]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    projected, trend_limits, trend_gate = long_window_trend(values, indices, 0.0, 500)
    final_residuals, recent_max_residuals, equations_gate = residual_gate(log, window)
    reference = cfl3d_reference(benchmark_data / "n0012clcd_cfl3d_sa.dat")
    differences = {
        "cd": means["Cd"] - reference["cd"],
        "cl": means["Cl"] - reference["cl"],
    }
    limits = spec["acceptance_limits"]
    symmetry_gate = (
        abs(means["Cl"]) <= limits["absolute_cl"]
        and abs(means["CmPitch"]) <= limits["absolute_cm_quarter_chord"]
    )
    force_agreement_gate = abs(differences["cd"]) <= limits["absolute_cd_vs_cfl3d"]
    settling_gate = all(value <= 0.01 for value in peak_to_peak.values())
    passed = all(
        (
            provenance_gate,
            restart_provenance_gate,
            runtime_gate,
            model_gate,
            equations_gate,
            trend_gate,
            settling_gate,
            symmetry_gate,
            force_agreement_gate,
        )
    )
    return {
        "scope": "Gate 1 documented OpenFOAM/NASA Spalart-Allmaras control",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "provenance_gate": provenance_gate,
        "restart_provenance_gate": restart_provenance_gate,
        "runtime_and_execution_gate": runtime_gate,
        "model_configuration_gate": bool(model_gate),
        "last_window_mean": means,
        "last_window_peak_to_peak": peak_to_peak,
        "settling_gate": settling_gate,
        "projected_change_over_500_iterations": projected,
        "trend_absolute_limits": trend_limits,
        "long_window_trend_gate": trend_gate,
        "solver_initial_residuals_final": final_residuals,
        "solver_initial_residuals_last_100_max": recent_max_residuals,
        "solver_residual_gate": equations_gate,
        "cfl3d_sa_reference": reference,
        "openfoam_minus_cfl3d": differences,
        "zero_angle_symmetry_gate": symmetry_gate,
        "force_agreement_gate": force_agreement_gate,
        "gate_1_passed": passed,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.case, args.benchmark_data)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-sa-control-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
