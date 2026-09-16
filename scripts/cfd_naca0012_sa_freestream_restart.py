"""Create the predeclared documented-SA freestream-ratio sensitivity case."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

METHOD = "same-grid documented-SA freestream-ratio sensitivity"
PLAN_SHA256 = "748da34089fda521e26c3da3b1ebf17fb2033baaf1a2852db82554248d4b56b5"
FIELDS = ("U", "p", "nuTilda", "nut")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def latest_time(case: Path) -> Path:
    candidates = []
    for path in case.iterdir():
        if path.is_dir():
            try:
                candidates.append((float(path.name), path))
            except ValueError:
                continue
    if not candidates:
        raise ValueError(f"No numeric time directories in {case}")
    return max(candidates)[1]


def restart(source: Path, source_audit: Path, target: Path, plan: Path) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    plan = plan.resolve(strict=True)
    if sha256(plan) != PLAN_SHA256:
        raise ValueError("SA freestream-ratio plan checksum mismatch")
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
    if source_spec.get("model_mapping", {}).get("ras_model") != "SpalartAllmaras":
        raise ValueError("Source is not the documented SA control")

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

    provenance = target / "provenance"
    provenance.mkdir()

    field_path = target / "0" / "nuTilda"
    field = replace_once(
        field_path.read_text(),
        "freestreamValue uniform 3.432e-05;",
        "freestreamValue uniform 2.574e-05;",
    )
    field_path.write_text(field)

    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    spec_path = target / "benchmark-spec.json"
    spec = dict(source_spec)
    field_records["nuTilda"]["restart_sha256"] = sha256(field_path)
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
    spec["conditions"]["nu_tilda_m2_s"] = 2.574e-05
    spec["mechanism_test"] = {
        "name": "farfield_nuTilda_to_nu_ratio",
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "before": {"nuTilda_to_nu_ratio": 4.0, "nuTilda_m2_s": 3.432e-05},
        "after": {"nuTilda_to_nu_ratio": 3.0, "nuTilda_m2_s": 2.574e-05},
        "only_farfield_nuTilda_changed": True,
        "model_ft2": False,
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
            "nuTilda_restart_sha256": sha256(field_path),
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
    print(
        json.dumps(
            restart(args.source, args.source_audit, args.target, args.plan)
        )
    )


if __name__ == "__main__":
    main()
