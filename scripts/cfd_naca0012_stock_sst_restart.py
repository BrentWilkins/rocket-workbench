"""Create a direct, fail-closed SA-to-stock-SST NACA 0012 diagnostic case."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import tempfile
from pathlib import Path

from cfd_flat_plate_case import field, foam_header
from cfd_naca0012_case import (
    TMR_K_OVER_A2,
    TMR_OMEGA_MU_OVER_RHO_A2,
    archive_grid,
    mesh_lists,
)
from cfd_naca0012_map_fields import latest_time


PLAN = Path(__file__).resolve().parents[1] / "cfd" / "naca0012-stock-sst-relative-diagnostic-plan.json"
METHOD = "direct-sa-to-stock-sst-relative-diagnostic"
SST_REFERENCE_CD = 0.0080937292380
SST_REFERENCE_CL = -0.76275807991e-05
SST_REFERENCE_SHA256 = "373dc142018816628b7b53ad278327db731162988ba35a166cd9fdc131a7fd7a"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one {label} entry, found {text.count(old)}")
    return text.replace(old, new)


def reset_field_location(text: str) -> str:
    updated, count = re.subn(r'location\s+"[^"]+";', 'location "0";', text, count=1)
    if count != 1:
        raise ValueError("Source solution field does not have one FoamFile location")
    return updated


def _copy_case_skeleton(source: Path, target: Path) -> dict[str, str]:
    (target / "constant").mkdir(parents=True)
    (target / "system").mkdir()
    shutil.copytree(source / "constant" / "polyMesh", target / "constant" / "polyMesh")
    copied = {}
    for relative in (
        "constant/transportProperties",
        "system/controlDict",
        "system/decomposeParDict",
        "system/fvSchemes",
        "system/fvSolution",
    ):
        source_file = source / relative
        target_file = target / relative
        shutil.copyfile(source_file, target_file)
        copied[relative] = sha256(source_file)
    for name in ("boundary", "faces", "neighbour", "owner", "points"):
        copied[f"constant/polyMesh/{name}"] = sha256(source / "constant" / "polyMesh" / name)
    return copied


def build(
    source: Path,
    source_audit: Path,
    grid_archive: Path,
    target: Path,
    iterations: int = 5000,
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    grid_archive = grid_archive.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)
    if iterations != 5000:
        raise ValueError("This predeclared diagnostic requires exactly 5000 iterations")

    plan = json.loads(PLAN.read_text())
    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    declared_source = plan["source"]
    if sha256(source_spec_path) != declared_source["case_spec_sha256"]:
        raise ValueError("Source case specification does not match the predeclared plan")
    if sha256(source_audit) != declared_source["audit_sha256"]:
        raise ValueError("Source audit does not match the predeclared plan")
    if Path(audit.get("case", "")).resolve() != source:
        raise ValueError("Source audit refers to a different case")
    for gate in (
        "provenance_gate",
        "runtime_and_execution_gate",
        "model_configuration_gate",
        "settling_gate",
        "long_window_trend_gate",
    ):
        if audit.get(gate) is not True:
            raise ValueError(f"Source prerequisite {gate} did not pass")
    if audit.get("gate_1_passed") is not False:
        raise ValueError("This diagnostic is declared specifically downstream of failed Gate 1")
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not complete cleanly")
    expected_model = {
        "solver": "simpleFoam",
        "ras_model": "SpalartAllmaras",
        "runtime_library": None,
        "image_id": plan["execution"]["image_id"],
    }
    if source_spec.get("model_mapping") != expected_model:
        raise ValueError("Source is not the declared stock OpenFOAM SA control")
    if source_spec.get("grid_dimensions") != [897, 257]:
        raise ValueError("Source is not the declared 897x257 grid")

    x, y, grid_provenance = archive_grid(grid_archive, 897)
    if grid_provenance != source_spec.get("source"):
        raise ValueError("Grid archive provenance differs from the source case")
    _, _, _, wall_distance, _ = mesh_lists(x, y)
    if len(wall_distance) != source_spec["mesh"]["airfoil_faces"]:
        raise ValueError("Reconstructed wall-distance count differs from source mesh")

    conditions = source_spec["conditions"]
    speed = float(conditions["speed_m_s"])
    mach = float(conditions["mach"])
    nu = float(conditions["kinematic_viscosity_m2_s"])
    acoustic_speed = speed / mach
    k_inf = TMR_K_OVER_A2 * acoustic_speed**2
    omega_inf = TMR_OMEGA_MU_OVER_RHO_A2 * acoustic_speed**2 / nu
    nut_inf = k_inf / omega_inf
    omega_wall = 10.0 * 6.0 * nu / (0.075 * wall_distance**2)
    wall_values = "\n".join(f"{value:.15g}" for value in omega_wall)

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-", dir=target.parent))
    try:
        copied_hashes = _copy_case_skeleton(source, staging)
        source_time = latest_time(source)
        (staging / "0").mkdir()
        initialized_fields = {}
        for name in ("U", "p"):
            source_field = source_time / name
            target_field = staging / "0" / name
            target_field.write_text(reset_field_location(source_field.read_text()))
            initialized_fields[name] = {
                "source": str(source_field),
                "source_sha256": sha256(source_field),
                "target_sha256": sha256(target_field),
            }

        empty = "type empty;"
        scalar_farfield = lambda value: (
            "type freestream;\n"
            f"freestreamValue uniform {value:.15g};\n"
            f"value uniform {value:.15g};"
        )
        field(
            staging / "0" / "k",
            "[0 2 -2 0 0 0 0]",
            f"{k_inf:.15g}",
            {
                "airfoil": "type fixedValue; value uniform 0;",
                "farfield": scalar_farfield(k_inf),
                "front": empty,
                "back": empty,
            },
        )
        field(
            staging / "0" / "omega",
            "[0 0 -1 0 0 0 0]",
            f"{omega_inf:.15g}",
            {
                "airfoil": (
                    "type fixedValue;\n"
                    "value nonuniform List<scalar>\n"
                    f"{len(omega_wall)}\n(\n{wall_values}\n);"
                ),
                "farfield": scalar_farfield(omega_inf),
                "front": empty,
                "back": empty,
            },
        )
        field(
            staging / "0" / "nut",
            "[0 2 -1 0 0 0 0]",
            f"{nut_inf:.15g}",
            {
                "airfoil": "type fixedValue; value uniform 0;",
                "farfield": scalar_farfield(nut_inf),
                "front": empty,
                "back": empty,
            },
        )

        turbulence = (
            foam_header("dictionary", "constant", "turbulenceProperties")
            + "simulationType RAS;\n"
            + "RAS\n{\n"
            + " RASModel kOmegaSST;\n"
            + " turbulence on;\n"
            + " printCoeffs on;\n"
            + "}\n"
        )
        (staging / "constant" / "turbulenceProperties").write_text(turbulence)

        schemes_path = staging / "system" / "fvSchemes"
        schemes = schemes_path.read_text()
        schemes = replace_once(
            schemes,
            "div(phi,nuTilda) bounded Gauss linearUpwind grad(nuTilda);",
            "div(phi,k) bounded Gauss linearUpwind grad(k);\n"
            " div(phi,omega) bounded Gauss linearUpwind grad(omega);",
            "nuTilda convection",
        )
        schemes_path.write_text(schemes)

        solution_path = staging / "system" / "fvSolution"
        solution = solution_path.read_text()
        solution = replace_once(
            solution,
            "nuTilda { solver smoothSolver; smoother GaussSeidel; nSweeps 2; tolerance 1e-9; relTol 0.01; }",
            '"(k|omega)" { solver smoothSolver; smoother GaussSeidel; nSweeps 2; tolerance 1e-9; relTol 0.01; }',
            "nuTilda linear solver",
        )
        solution = replace_once(
            solution,
            "nuTilda 0.35;",
            '"(k|omega)" 0.35;',
            "nuTilda relaxation",
        )
        solution_path.write_text(solution)

        control_path = staging / "system" / "controlDict"
        control = control_path.read_text()
        control, count = re.subn(r"endTime\s+[0-9.]+;", f"endTime {iterations};", control, count=1)
        if count != 1:
            raise ValueError("Could not set one controlDict endTime")
        control_path.write_text(control)

        provenance = staging / "provenance"
        provenance.mkdir()
        implementation_snapshot = provenance / Path(__file__).name
        plan_snapshot = provenance / PLAN.name
        shutil.copyfile(Path(__file__), implementation_snapshot)
        shutil.copyfile(PLAN, plan_snapshot)

        target_spec = json.loads(json.dumps(source_spec))
        target_spec["scope"] = "Relative diagnostic downstream of failed Gate 1; not a passed Gate 2"
        target_spec.pop("continuation", None)
        target_spec.pop("mechanism_test", None)
        target_spec["model_mapping"] = {
            "solver": "simpleFoam",
            "ras_model": "kOmegaSST",
            "variant": "openfoam-v2512-kOmegaSST-default-coefficients",
            "runtime_library": None,
            "image_id": plan["execution"]["image_id"],
        }
        target_spec["conditions"].update(
            {
                "freestream_k_over_acoustic_speed_squared": TMR_K_OVER_A2,
                "freestream_omega_mu_over_rho_acoustic_speed_squared": TMR_OMEGA_MU_OVER_RHO_A2,
                "k_m2_s2": k_inf,
                "omega_s-1": omega_inf,
                "nut_m2_s": nut_inf,
            }
        )
        target_spec["conditions"].pop("nu_tilda_m2_s", None)
        target_spec["numerics"].pop("nu_tilda_convection", None)
        target_spec["numerics"]["k_convection"] = "bounded Gauss linearUpwind grad(k)"
        target_spec["numerics"]["omega_convection"] = "bounded Gauss linearUpwind grad(omega)"
        target_spec["numerics"]["iterations"] = iterations
        target_spec["numerics"]["relaxation"].pop("nuTilda", None)
        target_spec["numerics"]["relaxation"].update({"k": 0.35, "omega": 0.35})
        target_spec["wall_treatment"] = {
            "k": "fixedValue zero",
            "omega": "TMR factor-10 fixedValue per wall face",
            "nut": "fixedValue zero",
        }
        target_spec["reference"] = {
            "file": "n0012clcd_cfl3d_sst.dat",
            "sha256": SST_REFERENCE_SHA256,
            "alpha_0_cd": SST_REFERENCE_CD,
            "alpha_0_cl": SST_REFERENCE_CL,
        }
        target_spec["initialization"] = {
            "method": METHOD,
            "source_case": str(source),
            "source_time": float(source_time.name),
            "source_audit": str(source_audit),
            "source_audit_sha256": sha256(source_audit),
            "source_gate_1_passed": False,
            "copied_solution_fields": initialized_fields,
            "new_turbulence_fields": ["k", "omega", "nut"],
        }
        target_spec["change_control"] = {
            "plan": str(PLAN),
            "plan_sha256": sha256(PLAN),
            "implementation_snapshot": str(target / "provenance" / implementation_snapshot.name),
            "implementation_sha256": sha256(implementation_snapshot),
            "copied_source_file_sha256": copied_hashes,
            "declared_change": "SpalartAllmaras/nuTilda to stock kOmegaSST/k/omega/nut only",
        }
        target_spec["strict_gate_2_status"] = "blocked_by_failed_gate_1"
        target_spec["accepted_for_rocket"] = False
        (staging / "benchmark-spec.json").write_text(json.dumps(target_spec, indent=2) + "\n")
        (staging / "stock-sst-restart-execution.json").write_text(
            json.dumps(
                {
                    "stage": METHOD,
                    "stage_passed": True,
                    "source_case": str(source),
                    "source_time": float(source_time.name),
                    "source_audit": str(source_audit),
                    "plan_sha256": sha256(PLAN),
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
    parser.add_argument("--grid-archive", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--iterations", type=int, default=5000)
    args = parser.parse_args()
    result = build(
        args.source,
        args.source_audit,
        args.grid_archive,
        args.target,
        args.iterations,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
