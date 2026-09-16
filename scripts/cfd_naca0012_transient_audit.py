"""Audit a bounded transient NACA 0012 control against its steady parent."""

import argparse
import json
import re
from pathlib import Path

import numpy as np


IMAGE_ID = "sha256:143e0e81aa690349714910f096ef1a2dc5fbc723a27355f5078839503a9b7634"
COEFFICIENTS = ("Cd", "Cl", "CmPitch")


def coefficient_history(case: Path) -> tuple[list[str], np.ndarray]:
    files = sorted((case / "postProcessing" / "coefficients").glob("*/coefficient.dat"))
    if len(files) != 1:
        raise ValueError(f"Expected exactly one coefficient history, found {len(files)}")
    header = next(
        (line[1:].strip().split() for line in files[0].read_text().splitlines() if line.startswith("# Time ")),
        None,
    )
    if header is None:
        raise ValueError("Coefficient history has no # Time header")
    values = np.loadtxt(files[0], comments="#", ndmin=2)
    if values.shape[1] != len(header):
        raise ValueError("Coefficient header and data column counts differ")
    if len(values) < 2 or not np.all(np.diff(values[:, 0]) > 0):
        raise ValueError("Coefficient times must be strictly increasing")
    return header, values


def final_interval_statistics(
    header: list[str], values: np.ndarray, start_time: float
) -> tuple[int, dict[str, float], dict[str, float]]:
    tail = values[values[:, 0] >= start_time]
    if len(tail) < 100:
        raise ValueError(f"Need at least 100 samples in final flow-through interval, found {len(tail)}")
    indices = {name: header.index(name) for name in COEFFICIENTS}
    means = {name: float(np.mean(tail[:, indices[name]])) for name in COEFFICIENTS}
    half_ranges = {
        name: float(np.ptp(tail[:, indices[name]]) / 2) for name in COEFFICIENTS
    }
    return len(tail), means, half_ranges


def courant_history(log: str) -> list[tuple[float, float]]:
    matches = re.findall(
        r"Courant Number mean: \S+ max: (\S+)\s+"
        r"(?:deltaT = \S+\s+)?Time = (\S+)",
        log,
    )
    return [(float(time), float(maximum)) for maximum, time in matches]


def audit(case: Path, parent_audit: Path) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    execution = json.loads((case / "execution.json").read_text())
    image = json.loads((case / "image.json").read_text())
    parent = json.loads(parent_audit.read_text())
    controls = spec.get("time_integration", {})

    if spec.get("benchmark") != "TMR 2D NACA 0012":
        raise ValueError("Not a generated TMR NACA 0012 case")
    if controls.get("role") != "diagnostic_after_steady_solver_nonconvergence":
        raise ValueError("Not a bounded transient diagnostic")

    header, values = coefficient_history(case)
    end_time = float(controls["end_time_s"])
    convective_time = float(controls["convective_time_s"])
    samples, means, half_ranges = final_interval_statistics(
        header, values, end_time - convective_time
    )
    parent_means = parent["last_window_mean"]
    limits = parent["trend_absolute_limits_from_experimental_repeatability"]
    mean_differences = {
        name: abs(means[name] - float(parent_means[name])) for name in COEFFICIENTS
    }
    mean_gate = all(mean_differences[name] <= float(limits[name]) for name in COEFFICIENTS)
    range_gate = all(half_ranges[name] <= float(limits[name]) for name in COEFFICIENTS)

    log = (case / "2-mpirun.log").read_text()
    courant = courant_history(log)
    limiter = [int(value) for value in re.findall(r"LimitedCells=(\d+)", log)]
    runtime_gate = (
        image.get("Id") == IMAGE_ID
        and spec.get("model_mapping", {}).get("solver") == "rhoPimpleFoam"
        and spec.get("model_mapping", {}).get("runtime_library") == "libTmrSSTmCompressible.so"
        and all(stage.get("stage_passed") for stage in execution)
        and any("rhoPimpleFoam" in stage.get("stage", "") for stage in execution)
        and "Selecting RAS turbulence model TmrSSTm" in log
    )
    completion_gate = bool(values[-1, 0] >= end_time * (1 - 1e-6))
    final_courant = [maximum for time, maximum in courant if time >= end_time - convective_time]
    courant_gate = bool(final_courant) and max(final_courant) <= float(
        controls["maximum_courant_number"]
    ) + 1e-6
    limiter_gate = bool(limiter) and all(value == 0 for value in limiter)
    control_gate = all(
        (runtime_gate, completion_gate, courant_gate, limiter_gate, mean_gate, range_gate)
    )

    return {
        "case": str(case.resolve()),
        "parent_audit": str(parent_audit.resolve()),
        "final_flow_through_start_s": end_time - convective_time,
        "final_flow_through_samples": samples,
        "final_flow_through_mean": means,
        "final_flow_through_half_range": half_ranges,
        "steady_parent_mean": {name: float(parent_means[name]) for name in COEFFICIENTS},
        "absolute_mean_difference": mean_differences,
        "absolute_limits_from_experimental_repeatability": {
            name: float(limits[name]) for name in COEFFICIENTS
        },
        "maximum_observed_courant_number": max((value for _, value in courant), default=None),
        "maximum_final_flow_through_courant_number": max(final_courant) if final_courant else None,
        "runtime_and_execution_gate": runtime_gate,
        "completed_requested_duration_gate": completion_gate,
        "courant_gate": courant_gate,
        "temperature_limiter_inactive_gate": limiter_gate,
        "steady_mean_agreement_gate": mean_gate,
        "transient_half_range_gate": range_gate,
        "transient_control_passed": control_gate,
        "force_benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--parent-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.case, args.parent_audit)
    args.output.mkdir(parents=True, exist_ok=False)
    path = args.output / "naca0012-transient-control-audit.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
