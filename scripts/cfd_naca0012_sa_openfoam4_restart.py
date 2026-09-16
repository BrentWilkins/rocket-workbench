"""Create the predeclared OpenFOAM Foundation v4 SA lineage screen."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from cfd_naca0012_sa_freestream_restart import FIELDS, latest_time, sha256


METHOD = "same-grid documented-SA OpenFOAM Foundation v4 lineage screen"
PLAN_SHA256 = "38d43843791eb822b613441392d79d9532a33d522eb5a8b72c30a23ca3c04c12"
IMAGE_REFERENCE = (
    "openfoam/openfoam4-paraview50@"
    "sha256:a9cde0fffd6dee35f1d6fac0494d8595850aa8063005997a75c8430666f6c230"
)
IMAGE_ID = "sha256:e644ef04fd37619f48c2226f2aa9496bcaec2716546671e09ad37d9d850f7e36"


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def restart(source: Path, source_audit: Path, target: Path, plan: Path) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    plan = plan.resolve(strict=True)
    if sha256(plan) != PLAN_SHA256:
        raise ValueError("OpenFOAM v4 lineage plan checksum mismatch")
    if target.exists():
        raise FileExistsError(target)

    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    source_execution = json.loads((source / "execution.json").read_text())
    source_audit_data = json.loads(source_audit.read_text())
    if not source_execution or not all(
        stage.get("stage_passed") for stage in source_execution
    ):
        raise ValueError("Source execution did not pass")
    if source_audit_data.get("case_spec_sha256") != sha256(source_spec_path):
        raise ValueError("Source audit does not match source specification")
    if source_spec.get("conditions", {}).get("nu_tilda_m2_s") != 3.432e-05:
        raise ValueError("Source is not the documented ratio-4 case")

    source_time = latest_time(source)
    target.mkdir(parents=True)
    shutil.copytree(source / "constant", target / "constant")
    shutil.copytree(source / "system", target / "system")
    initial = target / "0"
    initial.mkdir()

    field_records = {}
    for name in FIELDS:
        source_field = source_time / name
        target_field = initial / name
        shutil.copyfile(source_field, target_field)
        field_records[name] = {
            "source_sha256": sha256(source_field),
            "restart_sha256_before_adapter": sha256(target_field),
        }

    u_path = initial / "U"
    u_path.write_text(
        replace_once(
            u_path.read_text(),
            "type            freestreamVelocity;",
            "type            freestream;",
        )
    )
    field_records["U"]["restart_sha256"] = sha256(u_path)
    for name in ("p", "nuTilda", "nut"):
        field_records[name]["restart_sha256"] = sha256(initial / name)

    control_dict_path = target / "system" / "controlDict"
    control_dict = replace_once(
        control_dict_path.read_text(), "endTime 5000;", "endTime 1000;"
    )
    control_dict = replace_once(
        control_dict, "libs (forces);", 'libs ("libforces.so");'
    )
    control_dict_path.write_text(control_dict)

    fv_solution_path = target / "system" / "fvSolution"
    fv_solution_path.write_text(
        replace_once(
            fv_solution_path.read_text(),
            "    nNonOrthogonalCorrectors 0;\n}",
            "    nNonOrthogonalCorrectors 0;\n    pRefCell 0;\n    pRefValue 0;\n}",
        )
    )

    provenance = target / "provenance"
    provenance.mkdir()
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)

    spec_path = target / "benchmark-spec.json"
    spec = dict(source_spec)
    spec["numerics"] = dict(source_spec["numerics"])
    spec["numerics"]["iterations"] = 1000
    spec["model_mapping"] = dict(source_spec["model_mapping"])
    spec["model_mapping"].update(
        {
            "distribution": "OpenFOAM Foundation",
            "version": "4.1",
            "source_commit": "d214c8dfd5ba56dd442bae186fd4fb50dd35c338",
            "image_reference": IMAGE_REFERENCE,
            "image_id": IMAGE_ID,
        }
    )
    spec["initialization"] = {
        "method": METHOD,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_case_spec_sha256": sha256(source_spec_path),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "fields": field_records,
        "physics_or_numerics_changed": True,
    }
    spec["mechanism_test"] = {
        "name": "OpenFOAM_solver_and_SA_lineage",
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "before": {"distribution": "OpenCFD", "version": "v2512"},
        "after": {"distribution": "OpenFOAM Foundation", "version": "4.1"},
        "additional_iterations": 1000,
        "compatibility_adapters": [
            {
                "file": "0/U",
                "before": "type            freestreamVelocity;",
                "after": "type            freestream;",
                "reason": "Foundation v4 name for the equivalent mixed freestream vector boundary condition",
            },
            {
                "file": "system/controlDict",
                "before": "libs (forces);",
                "after": "libs (\"libforces.so\");",
                "reason": "Foundation v4 force function-object library name",
            },
            {
                "file": "system/fvSolution",
                "before": "implicit pressure gauge selection",
                "after": "pRefCell 0; pRefValue 0;",
                "reason": "Foundation v4 requires an explicit arbitrary pressure gauge; gradients and forces are unchanged",
            },
        ],
        "only_solver_and_model_lineage_changed": True,
    }
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")

    record = {
        "stage": METHOD,
        "stage_passed": True,
        "method": METHOD,
        "physics_or_numerics_changed": True,
        "target_case": str(target),
        "target_case_spec_sha256": sha256(spec_path),
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "control_dict_sha256": sha256(control_dict_path),
        "fv_schemes_sha256": sha256(target / "system" / "fvSchemes"),
        "fv_solution_sha256": sha256(fv_solution_path),
        "turbulence_properties_sha256": sha256(
            target / "constant" / "turbulenceProperties"
        ),
        **spec["initialization"],
    }
    (target / "sa-continuation-execution.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(restart(args.source, args.source_audit, args.target, args.plan)))


if __name__ == "__main__":
    main()
