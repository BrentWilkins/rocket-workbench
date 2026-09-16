"""Build the predeclared stock-SST upwind replication from the accepted SA source."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
from pathlib import Path

from cfd_naca0012_stock_sst_restart import build as build_stock_sst
from cfd_naca0012_stock_sst_restart import sha256
from cfd_naca0012_stock_sst_upwind_restart import _replace_once


PLAN = (
    Path(__file__).resolve().parents[1]
    / "cfd"
    / "naca0012-stock-sst-upwind-from-sa-plan-v1.json"
)
METHOD = "direct-sa-to-stock-sst-upwind-replication"


def build(
    source: Path,
    source_audit: Path,
    grid_archive: Path,
    target: Path,
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    grid_archive = grid_archive.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)

    plan = json.loads(PLAN.read_text())
    audit = json.loads(source_audit.read_text())
    spec_path = source / "benchmark-spec.json"
    if sha256(spec_path) != plan["source"]["case_spec_sha256"]:
        raise ValueError("Source case specification does not match the plan")
    if sha256(source_audit) != plan["source"]["audit_sha256"]:
        raise ValueError("Source audit does not match the plan")
    if Path(audit.get("case", "")).resolve() != source:
        raise ValueError("Source audit refers to a different case")
    for name, expected in plan["source"]["required_gates"].items():
        if audit.get(name) != expected:
            raise ValueError(f"Source audit prerequisite {name} did not match the plan")

    target.parent.mkdir(parents=True, exist_ok=True)
    container = Path(tempfile.mkdtemp(prefix=f".{target.name}-", dir=target.parent))
    staging = container / "case"
    try:
        build_stock_sst(source, source_audit, grid_archive, staging, 5000)
        base_spec_path = staging / "benchmark-spec.json"
        spec = json.loads(base_spec_path.read_text())
        base_change_control = spec["change_control"]

        schemes_path = staging / "system" / "fvSchemes"
        source_schemes = schemes_path.read_text()
        schemes = _replace_once(
            source_schemes,
            "div(phi,k) bounded Gauss linearUpwind grad(k);",
            "div(phi,k) bounded Gauss upwind;",
        )
        schemes = _replace_once(
            schemes,
            "div(phi,omega) bounded Gauss linearUpwind grad(omega);",
            "div(phi,omega) bounded Gauss upwind;",
        )
        schemes_path.write_text(schemes)

        provenance = staging / "provenance"
        implementation_snapshot = provenance / Path(__file__).name
        plan_snapshot = provenance / PLAN.name
        shutil.copyfile(Path(__file__), implementation_snapshot)
        shutil.copyfile(PLAN, plan_snapshot)

        spec["scope"] = "Direct SA-to-stock-SST upwind replication downstream of failed Gate 1"
        spec["numerics"]["k_convection"] = "bounded Gauss upwind"
        spec["numerics"]["omega_convection"] = "bounded Gauss upwind"
        spec["initialization"]["method"] = METHOD
        spec["change_control"] = {
            "plan": str(PLAN),
            "plan_sha256": sha256(PLAN),
            "implementation": implementation_snapshot.name,
            "implementation_sha256": sha256(implementation_snapshot),
            "base_builder_plan": base_change_control["plan"],
            "base_builder_plan_sha256": base_change_control["plan_sha256"],
            "base_builder_implementation_snapshot": Path(
                base_change_control["implementation_snapshot"]
            ).name,
            "base_builder_implementation_sha256": base_change_control[
                "implementation_sha256"
            ],
            "copied_source_file_sha256": base_change_control[
                "copied_source_file_sha256"
            ],
            "source_generated_fvSchemes_sha256": hashlib.sha256(
                source_schemes.encode()
            ).hexdigest(),
            "target_fvSchemes_sha256": sha256(schemes_path),
            "declared_change": "stock-SST k and omega convection from bounded linearUpwind to bounded upwind only",
        }
        base_spec_path.write_text(json.dumps(spec, indent=2) + "\n")
        record = {
            "stage": METHOD,
            "stage_passed": True,
            "source_case": str(source),
            "source_audit": str(source_audit),
            "source_audit_sha256": sha256(source_audit),
            "plan_sha256": sha256(PLAN),
            "target_case_spec_sha256": sha256(base_spec_path),
        }
        (staging / "stock-sst-upwind-from-sa-execution.json").write_text(
            json.dumps(record, indent=2) + "\n"
        )
        os.replace(staging, target)
    except Exception:
        shutil.rmtree(container, ignore_errors=True)
        raise
    shutil.rmtree(container, ignore_errors=True)
    return json.loads((target / "benchmark-spec.json").read_text())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--grid-archive", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    args = parser.parse_args()
    result = build(args.source, args.source_audit, args.grid_archive, args.target)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
