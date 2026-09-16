"""Create a same-grid simpleFoam control from a converged rhoSimpleFoam case."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from cfd_flat_plate_case import field
from cfd_naca0012_map_fields import latest_time, parse_internal_field, replace_internal_field


METHOD = "same-grid compressible-to-incompressible solver control restart"
FIELDS = ("U", "k", "omega", "nut")
IMAGE_ID = "sha256:e83f84b5ab244104c47ee342489d3fdce78d5d82158fc37b686f499b7af07656"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def restart(
    source: Path, source_audit: Path, target: Path, iterations: int
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)
    if iterations < 500:
        raise ValueError("At least 500 iterations are required for the trend gate")
    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not pass")
    if (
        Path(audit.get("case", "")).resolve() != source
        or not audit.get("coarse_preflight_passed")
    ):
        raise ValueError("Source force audit did not pass")

    conditions = source_spec["conditions"]
    rho_inf = float(conditions["density_kg_m3"])
    p_inf = float(conditions["pressure_pa"])
    nu_inf = float(conditions["dynamic_viscosity_pa_s"]) / rho_inf

    target.mkdir(parents=True)
    constant = target / "constant"
    constant.mkdir()
    shutil.copytree(source / "constant" / "polyMesh", constant / "polyMesh")
    turbulence = (source / "constant" / "turbulenceProperties").read_text()
    turbulence = replace_once(turbulence, " Prt 0.90;", "")
    (constant / "turbulenceProperties").write_text(turbulence)
    (constant / "transportProperties").write_text(
        "FoamFile\n{\n version 2.0;\n format ascii;\n class dictionary;\n"
        " location \"constant\";\n object transportProperties;\n}\n"
        f"transportModel Newtonian;\nnu [0 2 -1 0 0 0 0] {nu_inf:.15g};\n"
    )

    shutil.copytree(source / "system", target / "system")
    (target / "system" / "fvOptions").write_text(
        "FoamFile\n{\n version 2.0;\n format ascii;\n class dictionary;\n"
        " location \"system\";\n object fvOptions;\n}\n"
    )
    control_path = target / "system" / "controlDict"
    control = control_path.read_text()
    control = replace_once(control, "application rhoSimpleFoam;", "application simpleFoam;")
    control = replace_once(
        control, 'libs ("libTmrSSTmCompressible.so");', 'libs ("libTmrSSTm.so");'
    )
    control = replace_once(control, "endTime 6000;", f"endTime {iterations};")
    control = replace_once(control, " rho rho;", " rho rhoInf;")
    control = replace_once(control, " pRef 101325;", " pRef 0;")
    control_path.write_text(control)

    fv_solution_path = target / "system" / "fvSolution"
    fv_solution = fv_solution_path.read_text()
    fv_solution = replace_once(fv_solution, '"(U|k|omega|e)"', '"(U|k|omega)"')
    fv_solution = replace_once(fv_solution, " rho 0.01;", "")
    fv_solution = replace_once(fv_solution, " e 0.1;", "")
    fv_solution_path.write_text(fv_solution)
    fv_schemes_path = target / "system" / "fvSchemes"
    fv_schemes = fv_schemes_path.read_text()
    fv_schemes = replace_once(
        fv_schemes,
        "div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear;",
        "div((nuEff*dev2(T(grad(U))))) Gauss linear;",
    )
    fv_schemes_path.write_text(fv_schemes)

    source_time = latest_time(source)
    initial = target / "0"
    initial.mkdir()
    fields = {}
    for name in FIELDS:
        source_field = source_time / name
        target_field = initial / name
        shutil.copyfile(source_field, target_field)
        fields[name] = {
            "source_sha256": sha256(source_field),
            "restart_sha256": sha256(target_field),
        }

    pressure_kind, pressure_values = parse_internal_field(
        (source_time / "p").read_text(), int(source_spec["mesh"]["cells"])
    )
    absolute_pressure = pressure_values[:, 0]
    kinematic_pressure = (absolute_pressure - p_inf) / rho_inf
    p_path = initial / "p"
    field(
        p_path,
        "[0 2 -2 0 0 0 0]",
        "0",
        {
            "airfoil": "type zeroGradient;",
            "farfield": "type freestreamPressure; freestreamValue uniform 0; value uniform 0;",
            "front": "type empty;",
            "back": "type empty;",
        },
    )
    p_path.write_text(
        replace_internal_field(
            p_path.read_text(), pressure_kind, kinematic_pressure[:, None]
        )
    )
    fields["p"] = {
        "source_sha256": sha256(source_time / "p"),
        "restart_sha256": sha256(p_path),
        "transform": "(p_absolute - p_inf) / rho_inf",
    }

    shutil.copyfile(source / "tmr-naca0012-grid.npz", target / "tmr-naca0012-grid.npz")
    provenance = target / "provenance"
    provenance.mkdir()
    implementation_snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), implementation_snapshot)
    initialization = {
        "method": METHOD,
        "stage_passed": True,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(implementation_snapshot),
        "implementation_sha256": sha256(implementation_snapshot),
        "fields": fields,
    }
    spec = dict(source_spec)
    spec["iterations"] = iterations
    spec["model_mapping"] = dict(source_spec["model_mapping"])
    spec["model_mapping"].update(
        {
            "solver": "simpleFoam",
            "runtime_library": "libTmrSSTm.so",
            "image_id": IMAGE_ID,
        }
    )
    spec["conditions"] = dict(conditions)
    spec["conditions"].update(
        {
            "mach": 0.0,
            "transport_model": "constant-kinematic-viscosity",
            "kinematic_viscosity_m2_s": nu_inf,
        }
    )
    spec["solver_path_control"] = {
        "method": METHOD,
        "production_solver": "rhoSimpleFoam",
        "control_solver": "simpleFoam",
        "purpose": "diagnostic only; cannot accept production compressible workflow",
    }
    spec["initialization"] = initialization
    spec_path = target / "benchmark-spec.json"
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")
    record = {
        "stage": METHOD,
        **initialization,
        "target_case": str(target),
        "target_case_spec_sha256": sha256(spec_path),
    }
    (target / "incompressible-restart-execution.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--iterations", type=int, default=1500)
    args = parser.parse_args()
    print(json.dumps(restart(args.source, args.source_audit, args.target, args.iterations)))


if __name__ == "__main__":
    main()
