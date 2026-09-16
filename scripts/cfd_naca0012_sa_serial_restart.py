"""Create the predeclared serial-execution SA mechanism test."""

import argparse
import json
import shutil
from pathlib import Path

from cfd_naca0012_sa_control_continue import FIELDS, latest_time, sha256


METHOD = "same-grid documented-SA serial-execution mechanism test"
PLAN_SHA256 = "cb009af63a54c9b18602e8c5efce8a354055cc44a6361f25349cacd7e01b78b1"


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def restart(source: Path, source_audit: Path, target: Path, plan: Path) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    plan = plan.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)
    if sha256(plan) != PLAN_SHA256:
        raise ValueError("SA serial plan checksum mismatch")

    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    execution = json.loads((source / "execution.json").read_text())
    audit = json.loads(source_audit.read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not pass")
    if source_spec.get("model_mapping", {}).get("ras_model") != "SpalartAllmaras":
        raise ValueError("Source is not the documented Spalart-Allmaras control")
    if audit.get("case_spec_sha256") != sha256(source_spec_path):
        raise ValueError("Source audit does not match the source specification")
    if audit.get("gate_1_passed") is not False:
        raise ValueError("Serial diagnostic requires a failed Gate 1 source")
    if audit.get("long_window_trend_gate") is not True:
        raise ValueError("Source force trend must pass before decomposition isolation")
    if audit.get("solver_residual_gate") is not False:
        raise ValueError("Source residual gate must be the remaining numerical failure")

    source_time = latest_time(source)
    target.mkdir(parents=True)
    shutil.copytree(source / "constant", target / "constant")
    shutil.copytree(source / "system", target / "system")
    control_path = target / "system" / "controlDict"
    control_path.write_text(
        replace_once(control_path.read_text(), "endTime 5000;", "endTime 1000;")
    )
    initial = target / "0"
    initial.mkdir()
    fields = {}
    for name in FIELDS:
        source_field = source_time / name
        if not source_field.is_file():
            raise ValueError(f"Missing reconstructed continuation field {source_field}")
        target_field = initial / name
        shutil.copyfile(source_field, target_field)
        fields[name] = {
            "source": str(source_field),
            "source_sha256": sha256(source_field),
            "restart_sha256": sha256(target_field),
        }

    provenance = target / "provenance"
    provenance.mkdir()
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    initialization = {
        "method": METHOD,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_case_spec_sha256": sha256(source_spec_path),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "fields": fields,
        "physics_or_numerics_changed": False,
    }
    spec = dict(source_spec)
    spec["initialization"] = initialization
    spec["numerics"] = dict(source_spec["numerics"])
    spec["numerics"]["iterations"] = 1000
    spec["mechanism_test"] = {
        "name": "scotch_12_rank_to_serial_execution",
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "before": {"mpi_ranks": 12, "decomposition": "Scotch"},
        "after": {"mpi_ranks": 1, "decomposition": "none"},
        "only_execution_decomposition_changed": True,
    }
    spec_path = target / "benchmark-spec.json"
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")
    record = {
        "stage": METHOD,
        "stage_passed": True,
        "target_case": str(target),
        "target_case_spec_sha256": sha256(spec_path),
        **initialization,
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "control_dict_sha256": sha256(control_path),
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
