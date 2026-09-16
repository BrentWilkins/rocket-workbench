"""Prepare the predeclared matched fin-ranking CFD matrix without running it."""

import argparse
import hashlib
import json
import sys
from pathlib import Path

from cfd_case import generate
from rocket_workbench.cli import save_json

sys.path.insert(0, str(Path(__file__).resolve().parent))
from study_fin_shapes import variant  # noqa: E402


PLAN = Path(__file__).resolve().parents[1] / "cfd" / "fin-ranking-plan-v1.json"


def design_matrix():
    return [
        {"id": "trapezoidal", "shape": "trapezoidal", "ring_chord_mm": 0},
        {"id": "elliptical", "shape": "elliptical", "ring_chord_mm": 0},
        {"id": "clipped-delta", "shape": "clipped-delta", "ring_chord_mm": 0},
        {"id": "swept", "shape": "swept", "ring_chord_mm": 0},
        {"id": "clipped-delta-ring-5mm", "shape": "clipped-delta", "ring_chord_mm": 5},
        {"id": "clipped-delta-ring-10mm", "shape": "clipped-delta", "ring_chord_mm": 10},
    ]


def case_matrix(cell_sizes=(20, 15), angles=(0, 5)):
    return [
        {
            **design,
            "cell_mm": cell_mm,
            "alpha_deg": alpha_deg,
            "case_id": f"{design['id']}-a{alpha_deg}-cell{cell_mm}",
        }
        for design in design_matrix()
        for alpha_deg in angles
        for cell_mm in cell_sizes
    ]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--iterations", type=int, default=600)
    parser.add_argument("--speed", type=float, default=40)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output must not already exist")
    if args.iterations < 100:
        parser.error("At least 100 iterations are required by the coefficient audit")

    declared = json.loads(PLAN.read_text())
    args.output.mkdir(parents=True)
    cases = []
    configs = {}
    for item in case_matrix():
        design_id = item["id"]
        if design_id not in configs:
            config = variant(item["shape"], 45, 430)
            configs[design_id] = config
            save_json(args.output / f"config-{design_id}.json", config.model_dump())
        config = configs[design_id]
        case = args.output / item["case_id"]
        generate(
            config,
            case,
            cell_mm=item["cell_mm"],
            speed=args.speed,
            alpha=item["alpha_deg"],
            iterations=args.iterations,
            ring_chord_mm=item["ring_chord_mm"],
        )
        spec = json.loads((case / "case-spec.json").read_text())
        surface_hash = hashlib.sha256(
            (case / "constant" / "triSurface" / "rocket.stl").read_bytes()
        ).hexdigest()
        cases.append(
            {
                **item,
                "path": item["case_id"],
                "surface_sha256": surface_hash,
                "reference_area_m2": spec["reference_area_m2"],
                "reference_length_m": spec["reference_length_m"],
                "moment_origin_m": spec["moment_origin_m"],
            }
        )

    manifest = {
        "schema_version": 1,
        "plan": str(PLAN.relative_to(PLAN.parents[1])),
        "plan_sha256": hashlib.sha256(PLAN.read_bytes()).hexdigest(),
        "speed_m_s": args.speed,
        "iterations": args.iterations,
        "case_count": len(cases),
        "cases": cases,
        "claim_boundary": declared["claim_boundary"],
        "ranking_rule": declared["ranking_rule"],
    }
    save_json(args.output / "ranking-manifest.json", manifest)
    print(json.dumps({"output": str(args.output), "case_count": len(cases)}, indent=2))


if __name__ == "__main__":
    main()
