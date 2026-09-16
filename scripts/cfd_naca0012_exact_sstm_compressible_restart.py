"""Build the predeclared exact-SSTm incompressible-to-compressible rung."""

from __future__ import annotations

import argparse
import json
import math
import os
import shutil
import tempfile
from pathlib import Path

import numpy as np

from cfd_flat_plate_case import field, foam_header
from cfd_naca0012_map_fields import latest_time, parse_internal_field, replace_internal_field
from cfd_naca0012_stock_sst_restart import reset_field_location, sha256


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "cfd" / "naca0012-exact-sstm-compressible-from-incompressible-plan-v1.json"
IMAGE_PROVENANCE = ROOT / "cfd" / "sstm-exact-production-dual-image-provenance.json"
METHOD = "exact-sstm-incompressible-to-compressible-relative-diagnostic"
COPIED_FIELDS = ("U", "k", "omega", "nut")


def _write_compressible_files(staging: Path, plan: dict, pressure_values: np.ndarray) -> None:
    thermo = plan["declared_changes"]["thermodynamics"]
    pressure = thermo["pressure_pa"]
    temperature = thermo["temperature_k"]
    speed = thermo["velocity_m_s"]
    rho_inf = thermo["density_kg_m3"]
    cp = thermo["cp_j_kg_k"]
    molecular_weight = thermo["molecular_weight_kg_kmol"]
    sutherland_as = thermo["sutherland_as"]
    sutherland_temperature = thermo["sutherland_temperature_k"]

    empty = "type empty;"
    field(
        staging / "0" / "p",
        "[1 -1 -2 0 0 0 0]",
        f"{pressure:.15g}",
        {
            "airfoil": "type zeroGradient;",
            "farfield": f"type freestreamPressure;\nfreestreamValue uniform {pressure:.15g};",
            "front": empty,
            "back": empty,
        },
    )
    pressure_path = staging / "0" / "p"
    pressure_path.write_text(
        replace_internal_field(pressure_path.read_text(), "scalar", pressure_values)
    )
    field(
        staging / "0" / "T",
        "[0 0 0 1 0 0 0]",
        f"{temperature:.15g}",
        {
            "airfoil": "type zeroGradient;",
            "farfield": (
                f"type inletOutlet;\ninletValue uniform {temperature:.15g};\n"
                f"value uniform {temperature:.15g};"
            ),
            "front": empty,
            "back": empty,
        },
    )
    field(
        staging / "0" / "alphat",
        "[1 -1 -1 0 0 0 0]",
        "0",
        {
            "airfoil": "type compressible::alphatWallFunction;\nvalue uniform 0;",
            "farfield": "type calculated;\nvalue uniform 0;",
            "front": empty,
            "back": empty,
        },
    )

    constant = staging / "constant"
    system = staging / "system"
    (constant / "thermophysicalProperties").write_text(
        foam_header("dictionary", "constant", "thermophysicalProperties")
        + "thermoType\n{\n type hePsiThermo;\n mixture pureMixture;\n"
        + " transport sutherlandPr;\n thermo hConst;\n equationOfState perfectGas;\n"
        + " specie specie;\n energy sensibleInternalEnergy;\n}\n"
        + "mixture\n{\n specie\n {\n"
        + f"  molWeight {molecular_weight:.15g};\n }}\n"
        + f" thermodynamics\n {{\n  Cp {cp:.15g};\n  Hf 0;\n }}\n"
        + " transport\n {\n"
        + f"  As {sutherland_as:.15g};\n  Ts {sutherland_temperature:.15g};\n"
        + f"  Pr {thermo['molecular_prandtl']:.15g};\n }}\n}}\n"
    )
    (constant / "turbulenceProperties").write_text(
        foam_header("dictionary", "constant", "turbulenceProperties")
        + "simulationType RAS;\nRAS\n{\n"
        + " RASModel TmrSSTmExactProduction;\n turbulence on;\n printCoeffs on;\n"
        + " gamma1 0.5531666666666668;\n gamma2 0.4403546666666667;\n"
        + f" c1 20;\n Prt {thermo['turbulent_prandtl']:.15g};\n}}\n"
    )
    (system / "controlDict").write_text(
        foam_header("dictionary", "system", "controlDict")
        + "libs (\"libTmrSSTmCompressible.so\" \"libTmrSSTmKOnlyLimiterCompressible.so\" "
        + "\"libTmrSSTmExactProductionCompressible.so\" \"libSutherlandPrTransport.so\");\n"
        + "application rhoSimpleFoam;\nstartFrom startTime;\nstartTime 0;\n"
        + "stopAt endTime;\nendTime 5000;\ndeltaT 1;\nwriteControl timeStep;\n"
        + "writeInterval 500;\npurgeWrite 2;\nwriteFormat ascii;\nwritePrecision 10;\n"
        + "writeCompression off;\ntimeFormat general;\ntimePrecision 8;\n"
        + "runTimeModifiable false;\nfunctions\n{\n coefficients\n {\n  type forceCoeffs;\n"
        + "  libs (forces);\n  patches (airfoil);\n  rho rho;\n"
        + f"  rhoInf {rho_inf:.15g};\n  pRef {pressure:.15g};\n"
        + "  CofR (0.25 0 0);\n  liftDir (0 1 0);\n  dragDir (1 0 0);\n"
        + "  pitchAxis (0 0 1);\n"
        + f"  magUInf {speed:.15g};\n  lRef 1;\n  Aref 0.01;\n"
        + "  writeControl timeStep;\n  writeInterval 1;\n  log true;\n }\n}\n"
    )
    (system / "fvOptions").write_text(
        foam_header("dictionary", "system", "fvOptions")
        + "limitT\n{\n type limitTemperature;\n min 250;\n max 350;\n selectionMode all;\n}\n"
    )
    (system / "fvSchemes").write_text(
        foam_header("dictionary", "system", "fvSchemes")
        + "ddtSchemes { default steadyState; }\n"
        + "gradSchemes { default Gauss linear; limited cellLimited Gauss linear 1; "
        + "grad(U) $limited; grad(k) $limited; grad(omega) $limited; }\n"
        + "divSchemes { default none; div(phi,U) bounded Gauss linearUpwind grad(U); "
        + "energy bounded Gauss linearUpwind default; div(phi,e) $energy; "
        + "div(phi,K) $energy; div(phi,Ekp) $energy; turbulence bounded Gauss upwind; "
        + "div(phi,k) $turbulence; div(phi,omega) $turbulence; div(phid,p) Gauss upwind; "
        + "div((phi|interpolate(rho)),p) bounded Gauss upwind; "
        + "div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear; }\n"
        + "laplacianSchemes { default Gauss linear corrected; }\n"
        + "interpolationSchemes { default linear; }\n"
        + "snGradSchemes { default corrected; }\nwallDist { method meshWave; }\n"
    )
    (system / "fvSolution").write_text(
        foam_header("dictionary", "system", "fvSolution")
        + "solvers\n{\n p { solver GAMG; smoother GaussSeidel; tolerance 1e-7; relTol 0.01; }\n"
        + ' "(U|k|omega|e)" { solver PBiCGStab; preconditioner DILU; '
        + "tolerance 1e-7; relTol 0.01; }\n}\n"
        + "SIMPLE { nNonOrthogonalCorrectors 0; pMinFactor 0.1; pMaxFactor 2; }\n"
        + "relaxationFactors\n{\n fields { p 0.15; rho 0.01; }\n"
        + ' equations { U 0.35; e 0.35; "(k|omega)" 0.35; }\n}\n'
    )


def build(source: Path, source_audit: Path, target: Path, plan_path: Path = PLAN) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    plan_path = plan_path.resolve(strict=True)
    if target.exists():
        raise FileExistsError(target)
    plan = json.loads(plan_path.read_text())
    audit = json.loads(source_audit.read_text())
    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    if source != Path(plan["source"]["case"]).resolve():
        raise ValueError("Source case does not match compressible plan")
    if sha256(source_spec_path) != plan["source"]["case_spec_sha256"]:
        raise ValueError("Source case specification does not match compressible plan")
    if source_audit != Path(plan["source"]["audit"]).resolve():
        raise ValueError("Source audit path does not match compressible plan")
    if sha256(source_audit) != plan["source"]["audit_sha256"]:
        raise ValueError("Source audit does not match compressible plan")
    if audit.get("diagnostic_numerics_passed") is not True:
        raise ValueError("Exact incompressible source entry gate did not pass")
    if Path(audit.get("case", "")).resolve() != source:
        raise ValueError("Source audit covers a different case")
    if audit.get("case_spec_sha256") != sha256(source_spec_path):
        raise ValueError("Source audit does not cover current specification")
    execution = json.loads((source / "execution.json").read_text())
    if not execution or not all(stage.get("stage_passed") is True for stage in execution):
        raise ValueError("Source execution did not complete cleanly")
    expected_mapping = {
        "solver": "simpleFoam",
        "ras_model": "TmrSSTmExactProduction",
        "variant": "tmr-sstm-exact-production-v2512-source-audited",
        "runtime_library": "libTmrSSTmExactProduction.so",
        "image_id": plan["execution"]["image_id"],
    }
    if source_spec.get("model_mapping") != expected_mapping:
        raise ValueError("Source does not use the declared exact incompressible model")
    if sha256(IMAGE_PROVENANCE) != plan["execution"]["image_provenance_sha256"]:
        raise ValueError("Image provenance changed after plan declaration")

    thermo = plan["declared_changes"]["thermodynamics"]
    gas_constant = 8314.46261815324 / thermo["molecular_weight_kg_kmol"]
    calculated_temperature = (thermo["velocity_m_s"] / thermo["mach"]) ** 2 / (
        thermo["gamma"] * gas_constant
    )
    calculated_density = thermo["pressure_pa"] / (gas_constant * calculated_temperature)
    calculated_mu = calculated_density * thermo["kinematic_viscosity_m2_s"]
    calculated_as = calculated_mu * (
        calculated_temperature + thermo["sutherland_temperature_k"]
    ) / calculated_temperature**1.5
    for observed, expected, label in (
        (calculated_temperature, thermo["temperature_k"], "temperature"),
        (calculated_density, thermo["density_kg_m3"], "density"),
        (calculated_mu, thermo["dynamic_viscosity_pa_s"], "viscosity"),
        (calculated_as, thermo["sutherland_as"], "Sutherland As"),
    ):
        if not math.isclose(observed, expected, rel_tol=1e-12, abs_tol=1e-15):
            raise ValueError(f"Declared {label} is inconsistent")

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-", dir=target.parent))
    try:
        (staging / "0").mkdir()
        (staging / "constant").mkdir()
        (staging / "system").mkdir()
        shutil.copytree(source / "constant" / "polyMesh", staging / "constant" / "polyMesh")
        source_time = latest_time(source)
        field_records = {}
        for name in COPIED_FIELDS:
            source_field = source_time / name
            target_field = staging / "0" / name
            target_field.write_text(reset_field_location(source_field.read_text()))
            field_records[name] = {
                "source_sha256": sha256(source_field),
                "target_sha256": sha256(target_field),
            }
        cells = (source_spec["grid_dimensions"][0] - 1) * (
            source_spec["grid_dimensions"][1] - 1
        )
        pressure_kind, pressure_values = parse_internal_field(
            (source_time / "p").read_text(), cells
        )
        if pressure_kind != "scalar":
            raise ValueError("Source pressure is not scalar")
        pressure_values = thermo["pressure_pa"] + thermo["density_kg_m3"] * pressure_values
        _write_compressible_files(staging, plan, pressure_values)
        shutil.copyfile(source / "system" / "decomposeParDict", staging / "system" / "decomposeParDict")

        provenance = staging / "provenance"
        provenance.mkdir()
        implementation_snapshot = provenance / Path(__file__).name
        plan_snapshot = provenance / plan_path.name
        image_snapshot = provenance / IMAGE_PROVENANCE.name
        shutil.copyfile(Path(__file__), implementation_snapshot)
        shutil.copyfile(plan_path, plan_snapshot)
        shutil.copyfile(IMAGE_PROVENANCE, image_snapshot)
        mesh_hashes = {
            f"constant/polyMesh/{name}": sha256(source / "constant" / "polyMesh" / name)
            for name in ("boundary", "faces", "neighbour", "owner", "points")
        }
        target_spec = json.loads(json.dumps(source_spec))
        target_spec["scope"] = "Exact NASA SSTm compressible relative diagnostic downstream of failed Gate 1"
        target_spec["conditions"] = {
            "angle_of_attack_deg": 0.0,
            "speed_m_s": thermo["velocity_m_s"],
            "mach": thermo["mach"],
            "reynolds_number": thermo["density_kg_m3"] * thermo["velocity_m_s"] / thermo["dynamic_viscosity_pa_s"],
            "pressure_pa": thermo["pressure_pa"],
            "temperature_k": thermo["temperature_k"],
            "density_kg_m3": thermo["density_kg_m3"],
            "dynamic_viscosity_pa_s": thermo["dynamic_viscosity_pa_s"],
            "kinematic_viscosity_m2_s": thermo["kinematic_viscosity_m2_s"],
            "transport_model": "exact-sutherland-pr072",
            "openfoam_transport_model": "sutherlandPr",
            "molecular_prandtl": thermo["molecular_prandtl"],
            "turbulent_prandtl": thermo["turbulent_prandtl"],
        }
        target_spec["numerics"] = {
            "iterations": 5000,
            "velocity_convection": "bounded Gauss linearUpwind grad(U)",
            "energy_convection": "bounded Gauss linearUpwind default",
            "k_convection": "bounded Gauss upwind",
            "omega_convection": "bounded Gauss upwind",
            "relaxation": {"p": 0.15, "rho": 0.01, "U": 0.35, "e": 0.35, "k": 0.35, "omega": 0.35},
        }
        target_spec["model_mapping"] = {
            "solver": "rhoSimpleFoam",
            "runtime_model": "TmrSSTmExactProduction",
            "variant": "tmr-sstm-exact-production-v2512-source-audited",
            "runtime_library": "libTmrSSTmExactProductionCompressible.so",
            "transport_library": "libSutherlandPrTransport.so",
            "image_id": plan["execution"]["image_id"],
        }
        target_spec["initialization"] = {
            "method": METHOD,
            "source_case": str(source),
            "source_time": float(source_time.name),
            "source_audit": str(source_audit),
            "source_audit_sha256": sha256(source_audit),
            "copied_fields": field_records,
            "pressure_mapping": "p_abs = p_inf + rho_inf*p_kinematic",
            "new_fields": ["T", "alphat"],
        }
        target_spec["change_control"] = {
            "plan": str(plan_path),
            "plan_sha256": sha256(plan_path),
            "implementation_snapshot": str(target / "provenance" / implementation_snapshot.name),
            "implementation_sha256": sha256(implementation_snapshot),
            "image_provenance": str(IMAGE_PROVENANCE),
            "image_provenance_sha256": sha256(IMAGE_PROVENANCE),
            "copied_mesh_sha256": mesh_hashes,
            "declared_change": "incompressible simpleFoam to matched compressible rhoSimpleFoam closure only",
        }
        target_spec["strict_gate_4_status"] = "blocked_by_failed_gate_1"
        target_spec["accepted_for_rocket"] = False
        (staging / "benchmark-spec.json").write_text(json.dumps(target_spec, indent=2) + "\n")
        (staging / "compressible-restart-execution.json").write_text(
            json.dumps(
                {
                    "stage": METHOD,
                    "stage_passed": True,
                    "source_case": str(source),
                    "source_time": float(source_time.name),
                    "source_audit": str(source_audit),
                    "source_audit_sha256": sha256(source_audit),
                    "plan_sha256": sha256(plan_path),
                    "target_case_spec_sha256": sha256(staging / "benchmark-spec.json"),
                },
                indent=2,
            )
            + "\n"
        )
        os.replace(staging, target)
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise
    return json.loads((target / "benchmark-spec.json").read_text())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--plan", type=Path, default=PLAN)
    args = parser.parse_args()
    print(json.dumps(build(args.source, args.source_audit, args.target, args.plan), indent=2))


if __name__ == "__main__":
    main()
