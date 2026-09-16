"""Create a provenance-pinned continuation of the NACA 0012 SA control."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path


FIELDS = ("U", "p", "nuTilda", "nut")
METHOD = "same-grid documented-SA convergence continuation"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def latest_time(case: Path) -> Path:
    candidates = []
    for path in case.iterdir():
        if not path.is_dir():
            continue
        try:
            value = float(path.name)
        except ValueError:
            continue
        candidates.append((value, path))
    if not candidates:
        raise ValueError(f"No reconstructed solution times in {case}")
    return max(candidates)[1]


def continue_case(source: Path, source_audit: Path, target: Path) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)

    spec_path = source / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    execution = json.loads((source / "execution.json").read_text())
    audit = json.loads(source_audit.read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not pass")
    if spec.get("benchmark") != "TMR 2D NACA 0012":
        raise ValueError("Source is not the pinned NACA 0012 benchmark")
    if spec.get("model_mapping", {}).get("ras_model") != "SpalartAllmaras":
        raise ValueError("Source is not the documented Spalart-Allmaras control")
    if audit.get("case_spec_sha256") != sha256(spec_path):
        raise ValueError("Source audit does not match the source case specification")
    if audit.get("gate_1_passed") is not False:
        raise ValueError("Continuation is reserved for a failed Gate 1 audit")
    if audit.get("long_window_trend_gate") or audit.get("solver_residual_gate"):
        raise ValueError("Source did not fail the expected iterative-convergence gates")

    source_time = latest_time(source)
    target.mkdir(parents=True)
    shutil.copytree(source / "constant", target / "constant")
    shutil.copytree(source / "system", target / "system")
    initial = target / "0"
    initial.mkdir()
    field_records = {}
    for name in FIELDS:
        source_field = source_time / name
        if not source_field.is_file():
            raise ValueError(f"Missing reconstructed continuation field {source_field}")
        target_field = initial / name
        shutil.copyfile(source_field, target_field)
        field_records[name] = {
            "source": str(source_field),
            "source_sha256": sha256(source_field),
            "restart_sha256": sha256(target_field),
        }

    provenance = target / "provenance"
    provenance.mkdir()
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    continuation = {
        "method": METHOD,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_case_spec_sha256": sha256(spec_path),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "fields": field_records,
        "physics_or_numerics_changed": False,
    }
    continued_spec = dict(spec)
    continued_spec["initialization"] = continuation
    continued_spec["continuation"] = {
        "additional_iterations": spec["numerics"]["iterations"],
        "cumulative_iterations": float(source_time.name)
        + spec["numerics"]["iterations"],
    }
    target_spec = target / "benchmark-spec.json"
    target_spec.write_text(json.dumps(continued_spec, indent=2) + "\n")
    record = {
        "stage": METHOD,
        "stage_passed": True,
        "target_case": str(target),
        "target_case_spec_sha256": sha256(target_spec),
        **continuation,
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
    args = parser.parse_args()
    print(json.dumps(continue_case(args.source, args.source_audit, args.target)))


if __name__ == "__main__":
    main()
