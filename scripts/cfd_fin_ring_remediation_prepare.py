"""Prepare the predeclared matched level-5 ring-tail mesh-remediation cases."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

from cfd_case import generate
from rocket_workbench.cli import save_json

sys.path.insert(0, str(Path(__file__).resolve().parent))
from study_fin_shapes import variant  # noqa: E402


PLAN = Path(__file__).resolve().parents[1] / "cfd" / "fin-ranking-ring-mesh-remediation-v1.json"


def remediation_matrix():
    return [
        {"id": "clipped-delta", "ring_chord_mm": 0},
        {"id": "clipped-delta-ring-5mm", "ring_chord_mm": 5},
        {"id": "clipped-delta-ring-10mm", "ring_chord_mm": 10},
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output directory must not already exist")

    declared = json.loads(PLAN.read_text())
    args.output.mkdir(parents=True)
    config = variant("clipped-delta", 45, 430)
    save_json(args.output / "config-clipped-delta.json", config.model_dump())
    cases = []
    for item in remediation_matrix():
        case_id = f"{item['id']}-a0-cell20-level5"
        case = args.output / case_id
        generate(
            config,
            case,
            cell_mm=20,
            speed=40,
            alpha=0,
            iterations=600,
            ring_chord_mm=item["ring_chord_mm"],
            surface_refinement_level=5,
        )
        cases.append(
            {
                **item,
                "case_id": case_id,
                "path": case_id,
                "surface_sha256": hashlib.sha256(
                    (case / "constant" / "triSurface" / "rocket.stl").read_bytes()
                ).hexdigest(),
            }
        )

    save_json(
        args.output / "remediation-manifest.json",
        {
            "schema_version": 1,
            "plan": str(PLAN.relative_to(PLAN.parents[1])),
            "plan_sha256": hashlib.sha256(PLAN.read_bytes()).hexdigest(),
            "conditions": declared["conditions"],
            "cases": cases,
        },
    )
    print(json.dumps({"output": str(args.output), "case_count": len(cases)}, indent=2))


if __name__ == "__main__":
    main()
