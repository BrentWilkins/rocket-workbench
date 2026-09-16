"""Create the predeclared stock-SST turbulence-upwind remediation case."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import tempfile
from pathlib import Path

from cfd_naca0012_map_fields import latest_time
from cfd_naca0012_stock_sst_restart import reset_field_location, sha256


PLAN = (
    Path(__file__).resolve().parents[1]
    / "cfd"
    / "naca0012-stock-sst-turbulence-upwind-remediation-plan-v1.json"
)
METHOD = "stock-sst-turbulence-upwind-symmetry-remediation"
FIELDS = ("U", "p", "k", "omega", "nut")
COPIED_FILES = (
    "constant/transportProperties",
    "constant/turbulenceProperties",
    "system/controlDict",
    "system/decomposeParDict",
    "system/fvSolution",
)
POLYMESH_FILES = ("boundary", "faces", "neighbour", "owner", "points")


def _replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one {old!r} entry")
    return text.replace(old, new)


def build(source: Path, source_audit: Path, target: Path) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)

    plan = json.loads(PLAN.read_text())
    spec_path = source / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    declared_source = plan["source"]

    if sha256(spec_path) != declared_source["case_spec_sha256"]:
        raise ValueError("Source case specification does not match the plan")
    if sha256(source_audit) != declared_source["audit_sha256"]:
        raise ValueError("Source audit does not match the plan")
    if Path(audit.get("case", "")).resolve() != source:
        raise ValueError("Source audit refers to a different case")
    for name, expected in declared_source["required_state"].items():
        actual = (
            audit.get("bounded_k_diagnostic", {}).get("occurrences")
            if name == "bounded_k_occurrences"
            else audit.get(name)
        )
        if actual != expected:
            raise ValueError(f"Source audit prerequisite {name} is {actual!r}, expected {expected!r}")
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not complete cleanly")
    if spec.get("model_mapping", {}).get("ras_model") != "kOmegaSST":
        raise ValueError("Source is not packaged stock kOmegaSST")
    if spec.get("model_mapping", {}).get("solver") != "simpleFoam":
        raise ValueError("Source is not the incompressible solver path")

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-", dir=target.parent))
    try:
        (staging / "constant").mkdir()
        (staging / "system").mkdir()
        shutil.copytree(source / "constant" / "polyMesh", staging / "constant" / "polyMesh")
        copied_hashes: dict[str, str] = {}
        for relative in COPIED_FILES:
            shutil.copyfile(source / relative, staging / relative)
            copied_hashes[relative] = sha256(source / relative)
        for name in POLYMESH_FILES:
            relative = f"constant/polyMesh/{name}"
            copied_hashes[relative] = sha256(source / relative)

        source_time = latest_time(source)
        (staging / "0").mkdir()
        field_records = {}
        for name in FIELDS:
            source_field = source_time / name
            target_field = staging / "0" / name
            target_field.write_text(reset_field_location(source_field.read_text()))
            field_records[name] = {
                "source": str(source_field),
                "source_sha256": sha256(source_field),
                "target_sha256": sha256(target_field),
            }

        schemes_path = staging / "system" / "fvSchemes"
        shutil.copyfile(source / "system" / "fvSchemes", schemes_path)
        schemes = schemes_path.read_text()
        schemes = _replace_once(
            schemes,
            "div(phi,k) bounded Gauss linearUpwind grad(k);",
            "div(phi,k) bounded Gauss upwind;",
        )
        schemes = _replace_once(
            schemes,
            "div(phi,omega) bounded Gauss linearUpwind grad(omega);",
            "div(phi,omega) bounded Gauss upwind;",
        )
        schemes_path.write_text(schemes)

        control_path = staging / "system" / "controlDict"
        control = control_path.read_text()
        control, count = re.subn(r"endTime\s+[0-9.]+;", "endTime 5000;", control, count=1)
        if count != 1:
            raise ValueError("Could not set the declared 5000-iteration horizon")
        control_path.write_text(control)

        provenance = staging / "provenance"
        provenance.mkdir()
        implementation_snapshot = provenance / Path(__file__).name
        plan_snapshot = provenance / PLAN.name
        shutil.copyfile(Path(__file__), implementation_snapshot)
        shutil.copyfile(PLAN, plan_snapshot)

        target_spec = json.loads(json.dumps(spec))
        target_spec["scope"] = "Stock-SST turbulence-upwind symmetry remediation downstream of failed Gate 1"
        target_spec["numerics"]["k_convection"] = "bounded Gauss upwind"
        target_spec["numerics"]["omega_convection"] = "bounded Gauss upwind"
        target_spec.pop("continuation", None)
        target_spec["remediation"] = {
            "local_iterations": 5000,
            "cumulative_stock_sst_iterations": 15000,
            "changed_terms": ["div(phi,k)", "div(phi,omega)"],
        }
        target_spec["initialization"] = {
            "method": METHOD,
            "source_case": str(source),
            "source_time": float(source_time.name),
            "source_audit": str(source_audit),
            "source_audit_sha256": sha256(source_audit),
            "fields": field_records,
        }
        target_spec["change_control"] = {
            "plan": str(PLAN),
            "plan_sha256": sha256(PLAN),
            "implementation": implementation_snapshot.name,
            "implementation_sha256": sha256(implementation_snapshot),
            "copied_source_file_sha256": copied_hashes,
            "source_fvSchemes_sha256": sha256(source / "system" / "fvSchemes"),
            "target_fvSchemes_sha256": sha256(schemes_path),
            "declared_change": "k and omega convection from bounded linearUpwind to bounded upwind only",
        }
        target_spec["strict_gate_2_status"] = "blocked_by_failed_gate_1"
        target_spec["accepted_for_rocket"] = False
        (staging / "benchmark-spec.json").write_text(json.dumps(target_spec, indent=2) + "\n")
        record = {
            "stage": METHOD,
            "stage_passed": True,
            "source_case": str(source),
            "source_time": float(source_time.name),
            "source_audit": str(source_audit),
            "source_audit_sha256": sha256(source_audit),
            "plan_sha256": sha256(PLAN),
            "target_case_spec_sha256": sha256(staging / "benchmark-spec.json"),
        }
        (staging / "stock-sst-upwind-restart-execution.json").write_text(
            json.dumps(record, indent=2) + "\n"
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
    parser.add_argument("--target", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.source, args.source_audit, args.target), indent=2))


if __name__ == "__main__":
    main()
