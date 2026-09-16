"""Crop a converged full-domain NACA solution onto retained structured rows."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

import numpy as np

from cfd_naca0012_map_fields import (
    FIELDS,
    latest_time,
    parse_internal_field,
    replace_internal_field,
)


METHOD = "structured retained-row full-to-reduced-domain restart"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def restart(source: Path, source_audit: Path, target: Path) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve(strict=True)
    if (target / "execution.json").exists():
        raise ValueError("Refusing already executed target")
    record_path = target / "domain-restart-execution.json"
    if record_path.exists():
        raise FileExistsError(record_path)

    source_spec = json.loads((source / "benchmark-spec.json").read_text())
    target_spec_path = target / "benchmark-spec.json"
    target_spec = json.loads(target_spec_path.read_text())
    source_execution = json.loads((source / "execution.json").read_text())
    audit = json.loads(source_audit.resolve(strict=True).read_text())
    if not source_execution or not all(
        stage.get("stage_passed") for stage in source_execution
    ):
        raise ValueError("Source execution did not pass")
    if (
        Path(audit.get("case", "")).resolve() != source
        or not audit.get("coarse_preflight_passed")
        or not audit.get("solver_residual_gate")
        or not audit.get("long_window_trend_gate")
    ):
        raise ValueError("Source audit does not match or pass")
    invariant_keys = (
        "benchmark",
        "conditions",
        "model_mapping",
        "wall_treatment",
        "convection_scheme",
    )
    mismatch = {
        key: (source_spec.get(key), target_spec.get(key))
        for key in invariant_keys
        if source_spec.get(key) != target_spec.get(key)
    }
    if mismatch:
        raise ValueError(f"Domain-restart invariants differ: {sorted(mismatch)}")

    with np.load(source / "tmr-naca0012-grid.npz") as data:
        source_x = data["x"]
        source_y = data["y"]
    with np.load(target / "tmr-naca0012-grid.npz") as data:
        target_x = data["x"]
        target_y = data["y"]
    if source_x.shape[1] != target_x.shape[1]:
        raise ValueError("Source and target streamwise dimensions differ")
    if not 2 < target_x.shape[0] < source_x.shape[0]:
        raise ValueError("Target must remove at least one outer structured row")
    if not (
        np.array_equal(target_x, source_x[: target_x.shape[0]])
        and np.array_equal(target_y, source_y[: target_y.shape[0]])
    ):
        raise ValueError("Target coordinates are not an exact source-grid prefix")

    source_cells = (source_x.shape[0] - 1) * (source_x.shape[1] - 1)
    target_cells = (target_x.shape[0] - 1) * (target_x.shape[1] - 1)
    source_time = latest_time(source)
    staged: dict[str, dict] = {}
    for name in FIELDS:
        source_field = source_time / name
        target_field = target / "0" / name
        kind, values = parse_internal_field(source_field.read_text(), source_cells)
        cropped = values[:target_cells]
        if cropped.shape[0] != target_cells or not np.all(np.isfinite(cropped)):
            raise ValueError(f"Invalid cropped field {name}")
        staging = target / "0" / f".{name}.domain-restart"
        staging.write_text(replace_internal_field(target_field.read_text(), kind, cropped))
        staged[name] = {
            "source_sha256": sha256(source_field),
            "restart_sha256": sha256(staging),
            "source_cells": source_cells,
            "restart_cells": target_cells,
        }
    for name in FIELDS:
        (target / "0" / f".{name}.domain-restart").replace(target / "0" / name)

    provenance = target / "provenance"
    provenance.mkdir(exist_ok=False)
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    record = {
        "stage": METHOD,
        "stage_passed": True,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "source_grid_dimensions": list(source_x.shape[::-1]),
        "target_grid_dimensions": list(target_x.shape[::-1]),
        "fields": staged,
    }
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    target_spec["initialization"] = {
        "method": METHOD,
        **{key: value for key, value in record.items() if key != "stage"},
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
