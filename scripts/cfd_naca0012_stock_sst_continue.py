"""Create the predeclared unchanged stock-SST convergence continuation."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
from pathlib import Path

from cfd_naca0012_map_fields import latest_time
from cfd_naca0012_stock_sst_restart import reset_field_location, sha256


PLAN = Path(__file__).resolve().parents[1] / "cfd" / "naca0012-stock-sst-continuation-plan.json"
METHOD = "direct-stock-sst-unchanged-convergence-continuation"
FIELDS = ("U", "p", "k", "omega", "nut")


def build(
    source: Path,
    source_audit: Path,
    target: Path,
    plan_path: Path = PLAN,
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    plan_path = plan_path.resolve(strict=True)
    if target.exists():
        raise FileExistsError(target)

    plan = json.loads(plan_path.read_text())
    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    if sha256(source_spec_path) != plan["source"]["case_spec_sha256"]:
        raise ValueError("Stock-SST source case does not match the continuation plan")
    expected_audit_sha256 = plan["source"].get("audit_sha256")
    if expected_audit_sha256 and sha256(source_audit) != expected_audit_sha256:
        raise ValueError("Stock-SST source audit does not match the continuation plan")
    if Path(audit.get("case", "")).resolve() != source:
        raise ValueError("Stock-SST audit refers to a different case")
    if audit.get("case_spec_sha256") != sha256(source_spec_path):
        raise ValueError("Stock-SST audit does not cover the current source specification")
    for gate in plan["trigger"]["required_true"]:
        if audit.get(gate) is not True:
            raise ValueError(f"Continuation prerequisite {gate} did not pass")
    convergence_gates = (
        "settling_gate",
        "long_window_trend_gate",
        "solver_residual_gate",
        "zero_angle_symmetry_gate",
    )
    if all(audit.get(gate) is True for gate in convergence_gates):
        raise ValueError("Stock-SST source already passes numerical convergence gates")
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Stock-SST source execution did not complete cleanly")
    if source_spec.get("model_mapping", {}).get("ras_model") != "kOmegaSST":
        raise ValueError("Continuation source is not stock kOmegaSST")
    if source_spec.get("model_mapping", {}).get("image_id") != plan["execution"]["image_id"]:
        raise ValueError("Continuation source image differs from the plan")

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-", dir=target.parent))
    try:
        (staging / "constant").mkdir()
        (staging / "system").mkdir()
        shutil.copytree(source / "constant" / "polyMesh", staging / "constant" / "polyMesh")
        copied_hashes = {}
        for relative in (
            "constant/transportProperties",
            "constant/turbulenceProperties",
            "system/controlDict",
            "system/decomposeParDict",
            "system/fvSchemes",
            "system/fvSolution",
        ):
            source_file = source / relative
            shutil.copyfile(source_file, staging / relative)
            copied_hashes[relative] = sha256(source_file)
        for name in ("boundary", "faces", "neighbour", "owner", "points"):
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

        provenance = staging / "provenance"
        provenance.mkdir()
        implementation_snapshot = provenance / Path(__file__).name
        plan_snapshot = provenance / plan_path.name
        shutil.copyfile(Path(__file__), implementation_snapshot)
        shutil.copyfile(plan_path, plan_snapshot)

        target_spec = json.loads(json.dumps(source_spec))
        source_change_control = target_spec.pop("change_control")
        target_spec["scope"] = "Unchanged stock-SST convergence continuation downstream of failed Gate 1"
        target_spec["initialization"] = {
            "method": METHOD,
            "source_case": str(source),
            "source_time": float(source_time.name),
            "source_audit": str(source_audit),
            "source_audit_sha256": sha256(source_audit),
            "copied_solution_fields": field_records,
            "physics_or_numerics_changed": False,
        }
        target_spec["continuation"] = {
            "additional_iterations": plan["execution"]["additional_iterations"],
            "cumulative_iterations": plan["execution"]["cumulative_iterations"],
        }
        target_spec["change_control"] = {
            "plan": str(plan_path),
            "plan_sha256": sha256(plan_path),
            "implementation_snapshot": str(target / "provenance" / implementation_snapshot.name),
            "implementation_sha256": sha256(implementation_snapshot),
            "copied_source_file_sha256": copied_hashes,
            "upstream_direct_sa_to_sst_change_control": source_change_control,
            "declared_change": "none; unchanged convergence continuation",
        }
        target_spec["accepted_for_rocket"] = False
        (staging / "benchmark-spec.json").write_text(json.dumps(target_spec, indent=2) + "\n")
        (staging / "stock-sst-continuation-execution.json").write_text(
            json.dumps(
                {
                    "stage": METHOD,
                    "stage_passed": True,
                    "source_case": str(source),
                    "source_time": float(source_time.name),
                    "source_audit": str(source_audit),
                    "source_audit_sha256": sha256(source_audit),
                    "plan_sha256": sha256(plan_path),
                    "target_case_spec_sha256": sha256(staging / "benchmark-spec.json"),
                },
                indent=2,
            )
            + "\n"
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
    parser.add_argument("--plan", type=Path, default=PLAN)
    args = parser.parse_args()
    print(
        json.dumps(
            build(args.source, args.source_audit, args.target, args.plan), indent=2
        )
    )


if __name__ == "__main__":
    main()
