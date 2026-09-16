"""Audit completed matched fin cases and make conservative exploratory rankings."""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cfd_audit import audit  # noqa: E402


def closed_interval(first, second):
    return [min(first, second), max(first, second)]


def interval_relation(left, right):
    """Return lower/higher/overlap for two closed numerical intervals."""
    if left[1] < right[0]:
        return "lower"
    if left[0] > right[1]:
        return "higher"
    return "overlap"


def clear_drag_order(intervals):
    pairwise = []
    wins = {name: 0 for name in intervals}
    losses = {name: 0 for name in intervals}
    names = sorted(intervals)
    for index, left_name in enumerate(names):
        for right_name in names[index + 1 :]:
            relation = interval_relation(intervals[left_name], intervals[right_name])
            winner = loser = None
            if relation == "lower":
                winner, loser = left_name, right_name
            elif relation == "higher":
                winner, loser = right_name, left_name
            if winner:
                wins[winner] += 1
                losses[loser] += 1
            pairwise.append(
                {
                    "left": left_name,
                    "right": right_name,
                    "relation": relation,
                    "winner": winner,
                    "loser": loser,
                }
            )
    count = len(names) - 1
    return {
        "pairwise": pairwise,
        "clear_winners": sorted(name for name, value in wins.items() if value == count),
        "clear_losers": sorted(name for name, value in losses.items() if value == count),
        "wins": wins,
        "losses": losses,
    }


def evaluate(root):
    manifest = json.loads((root / "ranking-manifest.json").read_text())
    rows = []
    invariant_image = None
    invariant_axes = None
    for item in manifest["cases"]:
        case = root / item["path"]
        coefficients = case / "postProcessing" / "forces" / "0" / "coefficient.dat"
        if not coefficients.is_file():
            execution_path = case / "execution.json"
            execution = json.loads(execution_path.read_text()) if execution_path.is_file() else []
            rows.append(
                {
                    **item,
                    "usable_for_ranking": False,
                    "same_environment": None,
                    "audit": None,
                    "unavailable_reason": "solver_output_missing",
                    "completed_stages": [stage["stage"] for stage in execution],
                }
            )
            continue
        result = audit(case)
        image_path = case / "image.json"
        image = json.loads(image_path.read_text())["Id"] if image_path.is_file() else None
        if invariant_image is None:
            invariant_image = image
            invariant_axes = result["reported_axes"]
        same_environment = (
            image is not None
            and image == invariant_image
            and result["reported_axes"] == invariant_axes
        )
        usable = (
            result["solver_completed"]
            and result["requested_iterations_completed"]
            and result["tail_settled_screen"]
            and same_environment
            and (item["alpha_deg"] != 0 or result["zero_angle_symmetry_screen"] is True)
        )
        rows.append(
            {
                **item,
                "usable_for_ranking": usable,
                "same_environment": same_environment,
                "audit": result,
            }
        )

    grouped = {}
    for row in rows:
        grouped.setdefault((row["id"], row["alpha_deg"]), {})[row["cell_mm"]] = row

    metrics = {}
    provisional_metrics = {}
    for (design, alpha), by_grid in grouped.items():
        has_two_solver_results = (
            set(by_grid) == {15, 20}
            and all(row["audit"] is not None for row in by_grid.values())
        )
        if has_two_solver_results:
            provisional_stats = {}
            for coefficient in ("Cd", "Cl", "CmPitch"):
                coarse = by_grid[20]["audit"]["coefficient_statistics"][coefficient]["mean"]
                fine = by_grid[15]["audit"]["coefficient_statistics"][coefficient]["mean"]
                provisional_stats[coefficient] = {
                    "cell20": coarse,
                    "cell15": fine,
                    "grid_interval": closed_interval(coarse, fine),
                    "absolute_grid_shift": abs(fine - coarse),
                }
            provisional_metrics[f"{design}:a{alpha}"] = {
                "status": "provisional_quality_gate_failed"
                if not all(row["usable_for_ranking"] for row in by_grid.values())
                else "quality_gates_passed",
                "metrics": provisional_stats,
            }
        if not has_two_solver_results or not all(
            row["usable_for_ranking"] for row in by_grid.values()
        ):
            metrics[f"{design}:a{alpha}"] = {"status": "not_rankable"}
            continue
        stats = {}
        for coefficient in ("Cd", "Cl", "CmPitch"):
            coarse = by_grid[20]["audit"]["coefficient_statistics"][coefficient]["mean"]
            fine = by_grid[15]["audit"]["coefficient_statistics"][coefficient]["mean"]
            stats[coefficient] = {
                "cell20": coarse,
                "cell15": fine,
                "grid_interval": closed_interval(coarse, fine),
                "absolute_grid_shift": abs(fine - coarse),
            }
        metrics[f"{design}:a{alpha}"] = {"status": "rankable", "metrics": stats}

    drag_intervals = {
        design: value["metrics"]["Cd"]["grid_interval"]
        for key, value in metrics.items()
        if key.endswith(":a0") and value["status"] == "rankable"
        for design in [key.removesuffix(":a0")]
    }
    expected = len({item["id"] for item in manifest["cases"]})
    ranking = clear_drag_order(drag_intervals) if len(drag_intervals) == expected else None
    unavailable = [row["case_id"] for row in rows if row["audit"] is None]
    rejected = [row["case_id"] for row in rows if row["audit"] is not None and not row["usable_for_ranking"]]
    return {
        "schema_version": 1,
        "status": "complete" if not unavailable and not rejected else "complete_with_unrankable_cases",
        "case_count": len(rows),
        "rankable_zero_angle_designs": len(drag_intervals),
        "unavailable_cases": unavailable,
        "quality_gate_rejected_cases": rejected,
        "rows": rows,
        "grid_metrics": metrics,
        "provisional_grid_metrics": provisional_metrics,
        "zero_angle_drag_ranking": ranking,
        "claim_boundary": manifest["claim_boundary"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("Output must not already exist")
    result = evaluate(args.study)
    args.output.mkdir(parents=True)
    (args.output / "ranking.json").write_text(json.dumps(result, indent=2) + "\n")
    summary = {
        "status": result["status"],
        "rankable_zero_angle_designs": result["rankable_zero_angle_designs"],
        "zero_angle_drag_ranking": result["zero_angle_drag_ranking"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
