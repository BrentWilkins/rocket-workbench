"""Create an audit-pinned same-grid restart for NACA scheme sensitivity."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from cfd_naca0012_map_fields import FIELDS, latest_time


METHOD = "same-grid scheme-sensitivity restart"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def restart(source: Path, source_audit: Path, target: Path) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve(strict=True)
    if (target / "execution.json").exists():
        raise ValueError("Refusing to initialize an already executed target")
    if (target / "scheme-restart-execution.json").exists():
        raise FileExistsError(target / "scheme-restart-execution.json")
    source_spec = json.loads((source / "benchmark-spec.json").read_text())
    target_spec_path = target / "benchmark-spec.json"
    target_spec = json.loads(target_spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    source_execution = json.loads((source / "execution.json").read_text())
    if not source_execution or not all(stage.get("stage_passed") for stage in source_execution):
        raise ValueError("Source execution did not pass")
    if (
        Path(audit.get("case", "")).resolve() != source
        or not audit.get("coarse_preflight_passed")
        or not audit.get("solver_residual_gate")
        or not audit.get("long_window_trend_gate")
    ):
        raise ValueError("Source audit does not match or pass")
    invariant_keys = ("benchmark", "grid_dimensions", "conditions", "model_mapping")
    mismatch = {
        key: (source_spec.get(key), target_spec.get(key))
        for key in invariant_keys
        if source_spec.get(key) != target_spec.get(key)
    }
    if mismatch:
        raise ValueError(f"Scheme-restart invariants differ: {sorted(mismatch)}")
    if source_spec.get("convection_scheme") != "linear-upwind-velocity":
        raise ValueError("Scheme restart source must use linear-upwind velocity")
    if target_spec.get("convection_scheme") not in {
        "first-order-upwind",
        "limited-linear",
        "lust-blended",
    }:
        raise ValueError("Scheme restart target must use an approved comparison scheme")
    source_time = latest_time(source)
    numeric_target_times = []
    for item in target.iterdir():
        if item.is_dir():
            try:
                numeric_target_times.append(float(item.name))
            except ValueError:
                pass
    if numeric_target_times != [0.0]:
        raise ValueError("Target must contain only its generated zero-time directory")

    field_records = {}
    for name in FIELDS:
        source_field = source_time / name
        target_field = target / "0" / name
        if not source_field.is_file() or source_field.is_symlink() or target_field.is_symlink():
            raise ValueError(f"Invalid field path for {name}")
        field_records[name] = {"source_sha256": sha256(source_field)}
    for name in FIELDS:
        source_field = source_time / name
        target_field = target / "0" / name
        shutil.copyfile(source_field, target_field)
        field_records[name]["restart_sha256"] = sha256(target_field)

    provenance = target / "provenance"
    provenance.mkdir(exist_ok=False)
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    implementation_digest = sha256(snapshot)
    record = {
        "stage": METHOD,
        "stage_passed": True,
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": implementation_digest,
        "source_read_only": True,
    }
    (target / "scheme-restart-execution.json").write_text(json.dumps(record, indent=2) + "\n")
    target_spec["initialization"] = {
        "method": METHOD,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": implementation_digest,
        "source_convection_scheme": source_spec["convection_scheme"],
        "target_convection_scheme": target_spec["convection_scheme"],
        "fields": field_records,
    }
    target_spec_path.write_text(json.dumps(target_spec, indent=2) + "\n")
    return target_spec["initialization"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(restart(args.source, args.source_audit, args.target), indent=2))


if __name__ == "__main__":
    main()
