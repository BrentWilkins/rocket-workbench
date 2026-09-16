"""Create the predeclared exact standard-SA ft2 sensitivity case."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from cfd_naca0012_sa_freestream_restart import FIELDS, latest_time, sha256


METHOD = "same-grid exact standard-SA ft2 sensitivity"
PLAN_SHA256 = "b7b5be6cec6f31eb3f9fbefb2f8d6f80a1bf9a51ae35107ab520e03747796410"


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
        raise ValueError("Standard-SA ft2 plan checksum mismatch")
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
        raise ValueError("Source audit does not match source case specification")
    mechanism = source_spec.get("mechanism_test", {})
    if mechanism.get("after", {}).get("nuTilda_to_nu_ratio") != 3.0:
        raise ValueError("Source is not the pinned ratio-3 SA case")
    if mechanism.get("model_ft2") is not False:
        raise ValueError("Source is not the no-ft2 case")

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
            "source": str(source_field),
            "source_sha256": sha256(source_field),
            "restart_sha256": sha256(target_field),
        }

    turbulence_path = target / "constant" / "turbulenceProperties"
    turbulence = replace_once(
        turbulence_path.read_text(),
        "    printCoeffs on;\n}",
        "    printCoeffs on;\n"
        "    SpalartAllmarasCoeffs\n"
        "    {\n"
        "        ft2 true;\n"
        "    }\n"
        "}",
    )
    turbulence_path.write_text(turbulence)

    provenance = target / "provenance"
    provenance.mkdir()
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    spec_path = target / "benchmark-spec.json"
    spec = dict(source_spec)
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
        "name": "SpalartAllmaras_ft2_switch",
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "before": {"ft2": False},
        "after": {"ft2": True},
        "default_coefficients": {"Ct3": 1.2, "Ct4": 0.5},
        "only_ft2_switch_changed": True,
        "nuTilda_to_nu_ratio": 3.0,
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
        "turbulence_properties_sha256": sha256(turbulence_path),
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
