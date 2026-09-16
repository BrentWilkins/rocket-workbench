"""Create the predeclared SA non-orthogonal-corrector screen case."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from cfd_naca0012_sa_freestream_restart import FIELDS, latest_time, sha256


METHOD = "same-grid documented-SA non-orthogonal-corrector screen"
PLAN_SHA256 = "a4ca0b1382e35c5356680e96135c23876a8f2fe5242032f51a739814b12b8354"


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
        raise ValueError("Non-orthogonal-corrector screen plan checksum mismatch")
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
    mechanism = source_spec.get("mechanism_test", {})
    if mechanism.get("name") != "uniform_half_scale_SIMPLE_under_relaxation":
        raise ValueError("Source is not the declared settled half-relaxation case")
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
            "restart_sha256": sha256(target_field),
        }

    fv_solution_path = target / "system" / "fvSolution"
    fv_solution = replace_once(
        fv_solution_path.read_text(),
        "nNonOrthogonalCorrectors 0;",
        "nNonOrthogonalCorrectors 4;",
    )
    fv_solution_path.write_text(fv_solution)

    control_dict_path = target / "system" / "controlDict"
    control_dict = replace_once(
        control_dict_path.read_text(), "endTime 5000;", "endTime 1000;"
    )
    control_dict_path.write_text(control_dict)

    provenance = target / "provenance"
    provenance.mkdir()
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)

    spec_path = target / "benchmark-spec.json"
    spec = dict(source_spec)
    spec["numerics"] = dict(source_spec["numerics"])
    spec["numerics"]["iterations"] = 1000
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
        "name": "SIMPLE_nNonOrthogonalCorrectors",
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "before": {"nNonOrthogonalCorrectors": 0},
        "after": {"nNonOrthogonalCorrectors": 4},
        "additional_iterations": 1000,
        "only_nNonOrthogonalCorrectors_changed": True,
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
        "fv_solution_sha256": sha256(fv_solution_path),
        "control_dict_sha256": sha256(control_dict_path),
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
