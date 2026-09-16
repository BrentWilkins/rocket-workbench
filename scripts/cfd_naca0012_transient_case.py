"""Generate a bounded rhoPimpleFoam diagnostic from a sealed steady NACA case."""

import argparse
import json
from pathlib import Path

from cfd_naca0012_case import generate


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one {label} block, found {text.count(old)}")
    return text.replace(old, new)


def transform_case(output: Path, flow_through_times: float) -> dict:
    spec_path = output / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    speed = float(spec["conditions"]["speed_m_s"])
    chord = float(spec["conditions"]["chord_m"])
    convective_time = chord / speed
    end_time = flow_through_times * convective_time
    initial_delta_t = min(1e-5, end_time / 1000)
    max_delta_t = min(1e-4, end_time / 100)

    control_path = output / "system" / "controlDict"
    control = control_path.read_text()
    control = replace_once(
        control, "application rhoSimpleFoam;", "application rhoPimpleFoam;", "solver"
    )
    control = replace_once(control, "endTime 1;", f"endTime {end_time:.15g};", "end time")
    control = replace_once(
        control,
        "deltaT 1;\nwriteControl timeStep;\nwriteInterval 100;",
        f"deltaT {initial_delta_t:.15g};\n"
        "adjustTimeStep yes;\nmaxCo 0.5;\n"
        f"maxDeltaT {max_delta_t:.15g};\n"
        "writeControl adjustableRunTime;\n"
        f"writeInterval {end_time:.15g};",
        "time controls",
    )
    control_path.write_text(control)

    schemes_path = output / "system" / "fvSchemes"
    schemes = replace_once(
        schemes_path.read_text(),
        "ddtSchemes { default steadyState; }",
        "ddtSchemes { default Euler; }",
        "time scheme",
    )
    schemes = replace_once(
        schemes,
        "div(phid,p) Gauss upwind;",
        "div(phid,p) Gauss upwind; div(phiv,p) Gauss upwind;",
        "transient pressure convection scheme",
    )
    schemes_path.write_text(schemes)

    solution_path = output / "system" / "fvSolution"
    solution = solution_path.read_text()
    solution = replace_once(
        solution,
        '"(U|k|omega|e)"',
        '"(rho|U|k|omega|e)"',
        "transient density solver pattern",
    )
    solution = replace_once(
        solution,
        " p { solver GAMG; smoother GaussSeidel; tolerance 1e-7; relTol 0.01; }\n",
        " p { solver GAMG; smoother GaussSeidel; tolerance 1e-7; relTol 0.01; }\n"
        " pFinal { $p; relTol 0; }\n",
        "final pressure solver insertion point",
    )
    solution = replace_once(
        solution,
        " \"(rho|U|k|omega|e)\" { solver PBiCGStab; preconditioner DILU; tolerance 1e-7; relTol 0.01; }\n",
        " \"(rho|U|k|omega|e)\" { solver PBiCGStab; preconditioner DILU; tolerance 1e-7; relTol 0.01; }\n"
        " \"(rho|U|k|omega|e)Final\" { $U; relTol 0; }\n",
        "final transported-field solver insertion point",
    )
    solution = replace_once(
        solution,
        "SIMPLE\n{\n nNonOrthogonalCorrectors 0;\n"
        " pMinFactor 0.1;\n pMaxFactor 2;\n}\n"
        "relaxationFactors\n{\n fields { p 0.2; rho 0.01; }\n"
        ' equations { U 0.1; e 0.1; "(k|omega)" 0.3; }\n}\n',
        "PIMPLE\n{\n nOuterCorrectors 2;\n nCorrectors 2;\n"
        " nNonOrthogonalCorrectors 0;\n momentumPredictor yes;\n"
        " transonic no;\n pMinFactor 0.1;\n pMaxFactor 2;\n}\n",
        "algorithm controls",
    )
    solution_path.write_text(solution)

    spec["model_mapping"]["solver"] = "rhoPimpleFoam"
    spec["solver_controls"] = {
        "algorithm": "PIMPLE",
        "outer_correctors": 2,
        "pressure_correctors": 2,
        "equation_under_relaxation": "none",
    }
    spec["time_integration"] = {
        "role": "diagnostic_after_steady_solver_nonconvergence",
        "scheme": "Euler",
        "flow_through_times": flow_through_times,
        "convective_time_s": convective_time,
        "end_time_s": end_time,
        "initial_delta_t_s": initial_delta_t,
        "maximum_delta_t_s": max_delta_t,
        "maximum_courant_number": 0.5,
        "pimple_outer_correctors": 2,
        "pimple_pressure_correctors": 2,
    }
    spec["accepted_for_rocket"] = False
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")
    return spec


def generate_transient(
    archive: Path, parent: Path, output: Path, flow_through_times: float
) -> dict:
    if flow_through_times <= 0:
        raise ValueError("flow_through_times must be positive")
    parent_spec = json.loads((parent / "benchmark-spec.json").read_text())
    generate(
        archive,
        output,
        int(parent_spec["grid_dimensions"][0]),
        float(parent_spec["conditions"]["angle_of_attack_deg"]),
        1,
        parent_spec["convection_scheme"],
        parent,
    )
    return transform_case(output, flow_through_times)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grid-archive", required=True, type=Path)
    parser.add_argument("--parent", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--flow-through-times", required=True, type=float)
    args = parser.parse_args()
    result = generate_transient(
        args.grid_archive, args.parent, args.output, args.flow_through_times
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
