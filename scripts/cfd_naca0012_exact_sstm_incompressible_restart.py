"""Create the gated stock-SST-to-exact-SSTm incompressible diagnostic case."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import tempfile
from pathlib import Path

from cfd_flat_plate_case import foam_header
from cfd_naca0012_map_fields import latest_time
from cfd_naca0012_stock_sst_restart import reset_field_location, sha256


PLAN = (
    Path(__file__).resolve().parents[1]
    / "cfd"
    / "naca0012-exact-sstm-incompressible-relative-plan.json"
)
IMAGE_PROVENANCE = (
    Path(__file__).resolve().parents[1]
    / "cfd"
    / "sstm-exact-production-dual-image-provenance.json"
)
METHOD = "stock-sst-to-exact-nasa-sstm-incompressible-relative-diagnostic"
FIELDS = ("U", "p", "k", "omega", "nut")
RUNTIME_LIBRARIES = (
    'libs ("libTmrSSTm.so" "libTmrSSTmKOnlyLimiter.so" '
    '"libTmrSSTmExactProduction.so");'
)


def add_runtime_libraries(control: str) -> str:
    """Add the exact-model libraries without touching nested function libs."""
    if control.count("libs ();") == 1:
        return control.replace("libs ();", RUNTIME_LIBRARIES)
    if control.count("libs ();") > 1 or re.search(r"(?m)^libs\s*\(", control):
        raise ValueError("Expected no top-level runtime libraries or one empty list")
    marker = "functions\n{"
    if control.count(marker) != 1:
        raise ValueError("Expected exactly one top-level functions dictionary")
    return control.replace(marker, f"{RUNTIME_LIBRARIES}\n\n{marker}")


def build(
    source: Path,
    source_audit: Path,
    target: Path,
    iterations: int = 5000,
    plan_path: Path = PLAN,
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    plan_path = plan_path.resolve(strict=True)
    if target.exists():
        raise FileExistsError(target)
    if iterations != 5000:
        raise ValueError("This predeclared diagnostic requires exactly 5000 iterations")

    plan = json.loads(plan_path.read_text())
    image_provenance = json.loads(IMAGE_PROVENANCE.read_text())
    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    if sha256(source_spec_path) != plan["source"]["case_spec_sha256"]:
        raise ValueError("Stock-SST source case does not match the predeclared plan")
    expected_audit_sha256 = plan["source"].get("audit_sha256")
    if expected_audit_sha256:
        if source_audit != Path(plan["source"]["required_audit"]).resolve():
            raise ValueError("Stock-SST source audit path does not match the predeclared plan")
        if sha256(source_audit) != expected_audit_sha256:
            raise ValueError("Stock-SST source audit does not match the predeclared plan")
    if Path(audit.get("case", "")).resolve() != source:
        raise ValueError("Stock-SST audit refers to a different case")
    if audit.get("case_spec_sha256") != sha256(source_spec_path):
        raise ValueError("Stock-SST audit does not cover the current case specification")
    if audit.get("diagnostic_numerics_passed") is not True:
        raise ValueError("Stock-SST diagnostic numerical entry gate did not pass")
    if audit.get("strict_gate_2_passed") is not False:
        raise ValueError("Strict Gate 2 must remain fail-closed downstream of failed Gate 1")
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Stock-SST source execution did not complete cleanly")
    expected_source_model = {
        "solver": "simpleFoam",
        "ras_model": "kOmegaSST",
        "variant": "openfoam-v2512-kOmegaSST-default-coefficients",
        "runtime_library": None,
        "image_id": plan["declared_changes"]["runtime_image"]["from_id"],
    }
    if source_spec.get("model_mapping") != expected_source_model:
        raise ValueError("Source does not use the declared packaged stock SST model")
    if sha256(IMAGE_PROVENANCE) != plan["declared_changes"]["runtime_image"]["provenance_sha256"]:
        raise ValueError("Exact-SSTm image provenance changed after the plan was declared")
    if image_provenance.get("image_id") != plan["execution"]["image_id"]:
        raise ValueError("Exact-SSTm image ID differs from the plan")

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-", dir=target.parent))
    try:
        (staging / "constant").mkdir()
        (staging / "system").mkdir()
        shutil.copytree(source / "constant" / "polyMesh", staging / "constant" / "polyMesh")
        copied_hashes = {}
        for relative in (
            "constant/transportProperties",
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

        coefficients = plan["declared_changes"]["required_coefficients"]
        turbulence = (
            foam_header("dictionary", "constant", "turbulenceProperties")
            + "simulationType RAS;\n"
            + "RAS\n{\n"
            + " RASModel TmrSSTmExactProduction;\n"
            + " turbulence on;\n"
            + " printCoeffs on;\n"
            + f" gamma1 {coefficients['gamma1']};\n"
            + f" gamma2 {coefficients['gamma2']};\n"
            + f" c1 {coefficients['c1']};\n"
            + "}\n"
        )
        (staging / "constant" / "turbulenceProperties").write_text(turbulence)

        control_path = staging / "system" / "controlDict"
        control = control_path.read_text()
        control = add_runtime_libraries(control)
        control_path.write_text(control)

        provenance = staging / "provenance"
        provenance.mkdir()
        implementation_snapshot = provenance / Path(__file__).name
        plan_snapshot = provenance / plan_path.name
        image_snapshot = provenance / IMAGE_PROVENANCE.name
        shutil.copyfile(Path(__file__), implementation_snapshot)
        shutil.copyfile(plan_path, plan_snapshot)
        shutil.copyfile(IMAGE_PROVENANCE, image_snapshot)

        target_spec = json.loads(json.dumps(source_spec))
        target_spec["scope"] = "Exact NASA SSTm incompressible relative diagnostic downstream of failed Gate 1"
        target_spec["model_mapping"] = {
            "solver": "simpleFoam",
            "ras_model": "TmrSSTmExactProduction",
            "variant": "tmr-sstm-exact-production-v2512-source-audited",
            "runtime_library": "libTmrSSTmExactProduction.so",
            "image_id": plan["execution"]["image_id"],
        }
        target_spec["initialization"] = {
            "method": METHOD,
            "source_case": str(source),
            "source_time": float(source_time.name),
            "source_audit": str(source_audit),
            "source_audit_sha256": sha256(source_audit),
            "copied_solution_fields": field_records,
            "fields_reinitialized": False,
        }
        target_spec["change_control"] = {
            "plan": str(plan_path),
            "plan_sha256": sha256(plan_path),
            "image_provenance": str(IMAGE_PROVENANCE),
            "image_provenance_sha256": sha256(IMAGE_PROVENANCE),
            "implementation_snapshot": str(target / "provenance" / implementation_snapshot.name),
            "implementation_sha256": sha256(implementation_snapshot),
            "copied_source_file_sha256": copied_hashes,
            "declared_change": "stock kOmegaSST to source-audited TmrSSTmExactProduction only",
        }
        target_spec["strict_gate_3_status"] = "blocked_by_failed_gate_1"
        target_spec.pop("strict_gate_2_status", None)
        target_spec["accepted_for_rocket"] = False
        (staging / "benchmark-spec.json").write_text(json.dumps(target_spec, indent=2) + "\n")
        (staging / "exact-sstm-restart-execution.json").write_text(
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
    parser.add_argument("--iterations", type=int, default=5000)
    parser.add_argument("--plan", type=Path, default=PLAN)
    args = parser.parse_args()
    result = build(args.source, args.source_audit, args.target, args.iterations, args.plan)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
