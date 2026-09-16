"""Create a fresh exact-SSTm target from a sealed reduced-domain mesh case."""

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

from cfd_naca0012_map_fields import FIELDS, NONUNIFORM, UNIFORM


IMAGE_ID = "sha256:ae3235d75b54311a6dbcdfc2b45f6c9be77a8ff0743c099cf5ca3f3e9db0d23f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def construct(
    template: Path,
    source: Path,
    target: Path,
    plan_path: Path | None = None,
) -> dict:
    template = template.resolve(strict=True)
    source = source.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)

    template_spec_path = template / "benchmark-spec.json"
    source_spec_path = source / "benchmark-spec.json"
    template_spec = json.loads(template_spec_path.read_text())
    source_spec = json.loads(source_spec_path.read_text())
    template_grid = template_spec.get("grid_dimensions")
    if (
        not isinstance(template_grid, list)
        or len(template_grid) != 2
        or template_grid[0] != 897
        or not 3 <= template_grid[1] < 257
    ):
        raise ValueError("Template is not a reduced retained-row 897-point domain")
    template_domain = template_spec.get("domain", {})
    if template_domain.get("retained_outer_row_index") != template_grid[1] - 1:
        raise ValueError("Template domain row metadata does not match its grid")
    control_text = (template / "system" / "controlDict").read_text()
    if not re.search(r"(?m)^\s*endTime\s+4000\s*;", control_text):
        raise ValueError("Template does not use the predeclared 4000 iterations")
    if template_spec.get("solver_controls", {}).get("relaxation_scale") != 0.5:
        raise ValueError("Template does not use the predeclared half relaxation")
    if source_spec.get("grid_dimensions") != [897, 257]:
        raise ValueError("Source is not the declared full domain")
    if source_spec.get("model_mapping", {}).get("variant") != "tmr-sstm-exact-production":
        raise ValueError("Source is not the corrected SSTm model")

    plan_record = None
    if plan_path is not None:
        plan_path = plan_path.resolve(strict=True)
        plan = json.loads(plan_path.read_text())
        if not plan.get("declared_before_new_solver_execution"):
            raise ValueError("Gate 3 remediation plan was not predeclared")
        domain_phase = next(
            entry for entry in plan["phase_order"] if entry["name"] == "domain_ladder"
        )
        candidates = domain_phase["candidates"]
        matching = [
            name
            for name, candidate in candidates.items()
            if candidate["grid_dimensions"] == template_grid
            and candidate["retained_outer_row_index_zero_based"]
            == template_domain["retained_outer_row_index"]
            and candidate["iterations"] == 4000
        ]
        if len(matching) != 1:
            raise ValueError("Template does not match one predeclared domain candidate")
        plan_record = {
            "path": str(plan_path),
            "sha256": sha256(plan_path),
            "candidate": matching[0],
        }

    target.mkdir(parents=True)
    shutil.copytree(template / "0", target / "0")
    shutil.copytree(template / "constant", target / "constant")
    shutil.copytree(template / "system", target / "system")
    shutil.copyfile(template / "tmr-naca0012-grid.npz", target / "tmr-naca0012-grid.npz")

    normalized_fields = {}
    for name in FIELDS:
        field_path = target / "0" / name
        text = field_path.read_text()
        matches = list(NONUNIFORM.finditer(text))
        if len(matches) == 1:
            kind = matches[0].group(1)
            placeholder = "0" if kind == "scalar" else "(0 0 0)"
            field_path.write_text(
                NONUNIFORM.sub(f"internalField uniform {placeholder};", text, count=1)
            )
            normalized_fields[name] = {
                "source_internal_field": "nonuniform",
                "target_internal_field": "uniform mapping placeholder",
                "kind": kind,
            }
        elif len(UNIFORM.findall(text)) == 1:
            normalized_fields[name] = {
                "source_internal_field": "uniform",
                "target_internal_field": "uniform mapping placeholder",
            }
        else:
            raise ValueError(f"Expected exactly one internalField payload in {name}")

    thermo_path = target / "constant" / "thermophysicalProperties"
    thermo = replace_once(
        thermo_path.read_text(), "transport sutherland;", "transport sutherlandPr;"
    )
    ts_pattern = r"(?m)^(\s*)Ts\s+110\.4;$"
    if len(re.findall(ts_pattern, thermo)) != 1:
        raise ValueError("Expected one Sutherland Ts 110.4 entry")
    thermo = re.sub(ts_pattern, r"\1Ts 110.4;\n\1Pr 0.72;", thermo)
    thermo_path.write_text(thermo)

    turbulence_path = target / "constant" / "turbulenceProperties"
    turbulence_path.write_text(
        replace_once(
            turbulence_path.read_text(),
            "RASModel TmrSSTm;",
            "RASModel TmrSSTmExactProduction;",
        )
    )

    control_path = target / "system" / "controlDict"
    control_path.write_text(
        replace_once(
            control_path.read_text(),
            'libs ("libTmrSSTmCompressible.so");',
            'libs ("libTmrSSTmCompressible.so" '
            '"libTmrSSTmKOnlyLimiterCompressible.so" '
            '"libTmrSSTmExactProductionCompressible.so" '
            '"libSutherlandPrTransport.so");',
        )
    )

    target_spec = dict(template_spec)
    target_spec["conditions"] = source_spec["conditions"]
    target_spec["model_mapping"] = source_spec["model_mapping"]
    target_spec["iterations"] = 4000
    target_spec["convection_scheme"] = "linear-upwind-velocity"
    target_spec["target_construction"] = {
        "method": "sealed reduced-domain mesh and dictionaries retargeted to exact SSTm",
        "template": str(template),
        "template_spec_sha256": sha256(template_spec_path),
        "source": str(source),
        "normalized_internal_fields": normalized_fields,
        "source_spec_sha256": sha256(source_spec_path),
        "image_id": IMAGE_ID,
        "predeclared_plan": plan_record,
    }
    (target / "benchmark-spec.json").write_text(json.dumps(target_spec, indent=2) + "\n")

    snapshot = target / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    record = {
        "stage": "exact-SSTm reduced-domain target construction",
        "stage_passed": True,
        "template": str(template),
        "template_grid_sha256": sha256(template / "tmr-naca0012-grid.npz"),
        "source": str(source),
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "target_spec_sha256": sha256(target / "benchmark-spec.json"),
    }
    (target / "exact-domain-target-construction.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--plan", type=Path)
    args = parser.parse_args()
    print(
        json.dumps(
            construct(args.template, args.source, args.target, args.plan), indent=2
        )
    )


if __name__ == "__main__":
    main()
