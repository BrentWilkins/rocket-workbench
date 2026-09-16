"""Detect non-uniform or oscillatory outer flow in retained TMR flat-plate cases."""

import argparse
import json
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import final_time, numeric_pairs, vector_list


def outer_metrics(
    velocity_ratio: np.ndarray,
    outer_mask: np.ndarray,
    deviation_limit: float,
    jump_limit: float,
) -> dict:
    values = velocity_ratio[outer_mask]
    if values.size == 0:
        raise ValueError("Outer-flow selection is empty")
    pair_mask = outer_mask[:-1] & outer_mask[1:]
    jumps = np.abs(np.diff(velocity_ratio, axis=0))[pair_mask]
    if jumps.size == 0:
        raise ValueError("Outer-flow selection has no adjacent wall-normal pairs")
    deviation = np.abs(values - 1)
    return {
        "samples": int(values.size),
        "minimum_u_over_uinf": float(values.min()),
        "maximum_u_over_uinf": float(values.max()),
        "maximum_absolute_deviation": float(deviation.max()),
        "maximum_adjacent_wall_normal_jump": float(jumps.max()),
        "deviation_limit": deviation_limit,
        "adjacent_jump_limit": jump_limit,
        "deviation_screen_passed": bool(np.all(deviation <= deviation_limit)),
        "adjacent_jump_screen_passed": bool(np.all(jumps <= jump_limit)),
        "outer_flow_quality_screen": bool(
            np.all(deviation <= deviation_limit) and np.all(jumps <= jump_limit)
        ),
    }


def audit(case: Path, data: Path, plan: Path) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    plan_data = json.loads(plan.read_text())
    benchmark = next(
        item for item in plan_data["benchmarks"] if item["id"] == "tmr-2dzp-flat-plate"
    )
    declared = benchmark["predeclared_numerical_screen"]["outer_flow_quality"]
    grid = np.load(case / "tmr-grid.npz")
    x, y = grid["x"], grid["y"]
    time = final_time(case)
    velocity = vector_list((time / "U").read_text(), "internalField")[:, 0]
    velocity = velocity.reshape(y.shape[0] - 1, x.shape[1] - 1)
    x_centres = (x[:-1, :-1] + x[1:, :-1] + x[:-1, 1:] + x[1:, 1:]) / 4
    y_centres = (y[:-1, :-1] + y[1:, :-1] + y[:-1, 1:] + y[1:, 1:]) / 4
    typical = numeric_pairs(data / "retheta_variation_typical.dat")
    mapped_retheta = np.interp(x_centres, typical[:, 0], typical[:, 1])
    lower, upper = benchmark["conditions"]["comparison_reynolds_theta_range"]
    outer_mask = (
        (mapped_retheta >= lower)
        & (mapped_retheta <= upper)
        & (y_centres >= float(declared["evaluation_minimum_y_m"]))
    )
    speed = float(spec["conditions"]["U_m_s"])
    result = outer_metrics(
        velocity / speed,
        outer_mask,
        float(declared["maximum_absolute_u_over_uinf_minus_one"]),
        float(declared["maximum_adjacent_wall_normal_u_over_uinf_jump"]),
    )
    result.update(
        {
            "solution_time": time.name,
            "evaluation_minimum_y_m": float(declared["evaluation_minimum_y_m"]),
            "evaluation_retheta_interval": [float(lower), float(upper)],
            "velocity_clipped_for_audit": False,
            "accepted_for_rocket": False,
        }
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = audit(args.case, args.benchmark_data, args.plan)
    (args.output / "flat-plate-outer-flow-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
