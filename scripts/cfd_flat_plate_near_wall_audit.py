"""Audit wall-resolved y+ over the declared TMR flat-plate comparison region."""

import argparse
import json
import re
from pathlib import Path

import numpy as np

from cfd_flat_plate_audit import final_time, numeric_pairs


SCALAR = re.compile(r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?")


def scalar_list(text: str, marker: str) -> np.ndarray:
    start = text.index(marker)
    section = text[start:]
    count_match = re.search(r"nonuniform\s+List<scalar>\s+(\d+)\s*\(", section)
    if not count_match:
        raise ValueError(f"No nonuniform scalar list after {marker}")
    count = int(count_match.group(1))
    values = [
        float(value)
        for value in SCALAR.findall(section[count_match.end() :])[:count]
    ]
    if len(values) != count:
        raise ValueError(f"Expected {count} scalars after {marker}, found {len(values)}")
    return np.asarray(values)


def audit(case: Path, data: Path, plan: Path) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    plan_data = json.loads(plan.read_text())
    benchmark = next(
        item for item in plan_data["benchmarks"] if item["id"] == "tmr-2dzp-flat-plate"
    )
    declared = benchmark["predeclared_numerical_screen"]["near_wall"]
    lower, upper = declared["evaluation_region_reynolds_theta"]
    maximum = float(declared["maximum_y_plus"])

    grid = np.load(case / "tmr-grid.npz")
    x = grid["x"]
    ni = x.shape[1]
    leading = int(spec["mesh"]["plate_leading_edge_i"])
    plate_x = (x[0, leading:-1] + x[0, leading + 1 :]) / 2
    time = final_time(case)
    y_plus = scalar_list((time / "yPlus").read_text(), "plate")
    if len(y_plus) != len(plate_x):
        raise ValueError(
            f"Expected {len(plate_x)} plate y+ values for {ni} x-points, found {len(y_plus)}"
        )
    typical = numeric_pairs(data / "retheta_variation_typical.dat")
    mapped_retheta = np.interp(plate_x, typical[:, 0], typical[:, 1])
    selected = (mapped_retheta >= lower) & (mapped_retheta <= upper)
    if not selected.any():
        raise ValueError("No wall faces lie in the declared Re_theta interval")
    values = y_plus[selected]
    return {
        "solution_time": time.name,
        "comparison_faces": int(selected.sum()),
        "declared_retheta_interval": [float(lower), float(upper)],
        "declared_maximum_y_plus": maximum,
        "minimum_y_plus": float(values.min()),
        "median_y_plus": float(np.median(values)),
        "mean_y_plus": float(values.mean()),
        "percentile_95_y_plus": float(np.percentile(values, 95)),
        "maximum_y_plus": float(values.max()),
        "wall_resolved_y_plus_screen": bool(np.all(values <= maximum)),
        "all_plate_maximum_y_plus": float(y_plus.max()),
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = audit(args.case, args.benchmark_data, args.plan)
    (args.output / "flat-plate-near-wall-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
