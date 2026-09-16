"""Generate the documented OpenFOAM/NASA NACA 0012 Spalart-Allmaras control."""

import argparse
import json
from pathlib import Path

from cfd_flat_plate_case import field, foam_header
from cfd_naca0012_case import archive_grid, write_mesh


SPEED_M_S = 51.4815
KINEMATIC_VISCOSITY_M2_S = 8.58e-6
NU_TILDA_M2_S = 3.432e-5
NUT_M2_S = 8.58e-6
REFERENCE_CD_ALPHA_0 = 0.0081924676041
REFERENCE_CL_ALPHA_0 = -6.8553224298e-6
IMAGE_ID = "sha256:02a68093f2f25f07137cc5aafc20c96a0f26cb0f91aefb879ad1911a75ce6267"


def generate(grid_archive: Path, output: Path, iterations: int = 5000) -> dict:
    if output.exists():
        raise FileExistsError(output)
    if iterations < 500:
        raise ValueError("At least 500 iterations are required for the force trend gate")
    x, y, grid_provenance = archive_grid(grid_archive.resolve(strict=True), 897)
    output.mkdir(parents=True)
    mesh = write_mesh(output, x, y)
    mesh.pop("wall_distances_m")
    (output / "0").mkdir()

    empty = "type empty;"
    velocity = f"({SPEED_M_S:.15g} 0 0)"
    field(
        output / "0" / "U",
        "[0 1 -1 0 0 0 0]",
        velocity,
        {
            "airfoil": "type noSlip;",
            "farfield": (
                "type freestreamVelocity;\n"
                f"freestreamValue uniform {velocity};\n"
                f"value uniform {velocity};"
            ),
            "front": empty,
            "back": empty,
        },
        cls="volVectorField",
    )
    field(
        output / "0" / "p",
        "[0 2 -2 0 0 0 0]",
        "0",
        {
            "airfoil": "type zeroGradient;",
            "farfield": (
                "type freestreamPressure;\n"
                "freestreamValue uniform 0;\n"
                "value uniform 0;"
            ),
            "front": empty,
            "back": empty,
        },
    )
    field(
        output / "0" / "nuTilda",
        "[0 2 -1 0 0 0 0]",
        f"{NU_TILDA_M2_S:.15g}",
        {
            "airfoil": "type fixedValue;\nvalue uniform 0;",
            "farfield": (
                "type freestream;\n"
                f"freestreamValue uniform {NU_TILDA_M2_S:.15g};\n"
                f"value uniform {NU_TILDA_M2_S:.15g};"
            ),
            "front": empty,
            "back": empty,
        },
    )
    field(
        output / "0" / "nut",
        "[0 2 -1 0 0 0 0]",
        f"{NUT_M2_S:.15g}",
        {
            "airfoil": "type fixedValue;\nvalue uniform 0;",
            "farfield": (
                "type freestream;\n"
                f"freestreamValue uniform {NUT_M2_S:.15g};\n"
                f"value uniform {NUT_M2_S:.15g};"
            ),
            "front": empty,
            "back": empty,
        },
    )

    constant = output / "constant"
    system = output / "system"
    system.mkdir()
    (constant / "transportProperties").write_text(
        foam_header("dictionary", "constant", "transportProperties")
        + "transportModel Newtonian;\n"
        + f"nu [0 2 -1 0 0 0 0] {KINEMATIC_VISCOSITY_M2_S:.15g};\n"
    )
    (constant / "turbulenceProperties").write_text(
        foam_header("dictionary", "constant", "turbulenceProperties")
        + "simulationType RAS;\n"
        + "RAS\n{\n"
        + "    RASModel SpalartAllmaras;\n"
        + "    turbulence on;\n"
        + "    printCoeffs on;\n"
        + "}\n"
    )
    (system / "controlDict").write_text(
        foam_header("dictionary", "system", "controlDict")
        + "application simpleFoam;\n"
        + "startFrom startTime;\nstartTime 0;\nstopAt endTime;\n"
        + f"endTime {iterations};\ndeltaT 1;\n"
        + "writeControl timeStep;\nwriteInterval 500;\npurgeWrite 2;\n"
        + "writeFormat ascii;\nwritePrecision 10;\nwriteCompression off;\n"
        + "timeFormat general;\ntimePrecision 8;\nrunTimeModifiable false;\n"
        + "functions\n{\n"
        + "    coefficients\n    {\n"
        + "        type forceCoeffs;\n        libs (forces);\n"
        + "        patches (airfoil);\n        rho rhoInf;\n        rhoInf 1;\n"
        + "        CofR (0.25 0 0);\n        liftDir (0 1 0);\n"
        + "        dragDir (1 0 0);\n        pitchAxis (0 0 1);\n"
        + f"        magUInf {SPEED_M_S:.15g};\n"
        + "        lRef 1;\n        Aref 0.01;\n"
        + "        writeControl timeStep;\n        writeInterval 1;\n"
        + "        log true;\n    }\n}\n"
    )
    (system / "fvSchemes").write_text(
        foam_header("dictionary", "system", "fvSchemes")
        + "ddtSchemes { default steadyState; }\n"
        + "gradSchemes { default Gauss linear; }\n"
        + "divSchemes\n{\n"
        + "    default none;\n"
        + "    div(phi,U) bounded Gauss linearUpwind grad(U);\n"
        + "    div(phi,nuTilda) bounded Gauss linearUpwind grad(nuTilda);\n"
        + "    div((nuEff*dev2(T(grad(U))))) Gauss linear;\n"
        + "}\n"
        + "laplacianSchemes { default Gauss linear corrected; }\n"
        + "interpolationSchemes { default linear; }\n"
        + "snGradSchemes { default corrected; }\n"
        + "wallDist { method meshWave; }\n"
    )
    (system / "fvSolution").write_text(
        foam_header("dictionary", "system", "fvSolution")
        + "solvers\n{\n"
        + "    p { solver GAMG; tolerance 1e-8; relTol 0.01; smoother GaussSeidel; }\n"
        + "    U { solver smoothSolver; smoother GaussSeidel; nSweeps 2; tolerance 1e-9; relTol 0.01; }\n"
        + "    nuTilda { solver smoothSolver; smoother GaussSeidel; nSweeps 2; tolerance 1e-9; relTol 0.01; }\n"
        + "}\n"
        + "SIMPLE\n{\n    nNonOrthogonalCorrectors 0;\n}\n"
        + "relaxationFactors\n{\n"
        + "    fields { p 0.3; }\n"
        + "    equations { U 0.7; nuTilda 0.7; }\n"
        + "}\n"
    )
    (system / "decomposeParDict").write_text(
        foam_header("dictionary", "system", "decomposeParDict")
        + "numberOfSubdomains 12;\nmethod scotch;\n"
    )

    spec = {
        "benchmark": "TMR 2D NACA 0012",
        "scope": "Gate 1 of the NACA 0012 model and solver validation ladder",
        "documentation_url": "https://doc.openfoam.com/2606/examples/verification-validation/turbulent/naca0012/",
        "source": grid_provenance,
        "grid_dimensions": list(x.shape[::-1]),
        "mesh": mesh,
        "conditions": {
            "angle_of_attack_deg": 0.0,
            "speed_m_s": SPEED_M_S,
            "kinematic_viscosity_m2_s": KINEMATIC_VISCOSITY_M2_S,
            "reynolds_number": SPEED_M_S / KINEMATIC_VISCOSITY_M2_S,
            "mach": 0.15,
            "nu_tilda_m2_s": NU_TILDA_M2_S,
            "nut_m2_s": NUT_M2_S,
        },
        "model_mapping": {
            "solver": "simpleFoam",
            "ras_model": "SpalartAllmaras",
            "runtime_library": None,
            "image_id": IMAGE_ID,
        },
        "numerics": {
            "velocity_convection": "bounded Gauss linearUpwind grad(U)",
            "nu_tilda_convection": "bounded Gauss linearUpwind grad(nuTilda)",
            "iterations": iterations,
        },
        "force_coefficient_convention": {
            "rho_inf_kg_m3": 1.0,
            "reference_area_m2": 0.01,
            "reference_length_m": 1.0,
            "moment_center_m": [0.25, 0.0, 0.0],
        },
        "reference": {
            "file": "n0012clcd_cfl3d_sa.dat",
            "sha256": "b07afec6ce3ae4bf2f2d1a1d53785fde0a5ca68481a0d4186aa92754d811944e",
            "alpha_0_cd": REFERENCE_CD_ALPHA_0,
            "alpha_0_cl": REFERENCE_CL_ALPHA_0,
        },
        "acceptance_limits": {
            "absolute_cd_vs_cfl3d": 0.0002,
            "absolute_cl": 0.004,
            "absolute_cm_quarter_chord": 0.0002,
        },
        "accepted_for_rocket": False,
    }
    (output / "benchmark-spec.json").write_text(json.dumps(spec, indent=2) + "\n")
    return spec


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--grid-archive", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--iterations", type=int, default=5000)
    args = parser.parse_args()
    print(json.dumps(generate(args.grid_archive, args.output, args.iterations)))


if __name__ == "__main__":
    main()
