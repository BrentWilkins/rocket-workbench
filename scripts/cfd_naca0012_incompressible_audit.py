"""Audit the diagnostic same-grid incompressible NACA solver-path control."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import numpy as np

from cfd_naca0012_force_audit import (
    coefficient_history,
    cfl3d_reference,
    long_window_trend,
)
from cfd_naca0012_incompressible_restart import FIELDS, IMAGE_ID, METHOD
from cfd_naca0012_transport_sensitivity import drag_decomposition, solver_log


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def residual_gate(log: str, window: int = 100) -> tuple[dict, dict, bool]:
    patterns = {
        name: re.compile(
            rf"Solving for {name}, Initial residual = ([0-9.eE+-]+)"
        )
        for name in ("p", "Ux", "Uy", "omega", "k")
    }
    histories = {
        name: [float(value) for value in pattern.findall(log)]
        for name, pattern in patterns.items()
    }
    missing = [name for name, values in histories.items() if len(values) < window]
    if missing:
        raise ValueError(f"Need at least {window} residual samples for {missing}")
    final = {name: values[-1] for name, values in histories.items()}
    recent_max = {name: max(values[-window:]) for name, values in histories.items()}
    gate = all(value <= 1e-5 for value in final.values()) and all(
        value <= 1e-4 for value in recent_max.values()
    )
    return final, recent_max, gate


def audit(case: Path, benchmark_data: Path, window: int = 100) -> dict:
    case = case.resolve(strict=True)
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    execution = json.loads((case / "execution.json").read_text())
    image = json.loads((case / "image.json").read_text())
    initialization = spec.get("initialization", {})
    record = json.loads((case / "incompressible-restart-execution.json").read_text())
    snapshot = Path(initialization["implementation_snapshot"])
    source_audit = Path(initialization["source_audit"])
    provenance_gate = (
        initialization.get("method") == METHOD
        and record.get("stage_passed") is True
        and sha256(snapshot) == initialization.get("implementation_sha256")
        and sha256(source_audit) == initialization.get("source_audit_sha256")
        and all(
            sha256(case / "0" / name) == metadata["restart_sha256"]
            for name, metadata in initialization["fields"].items()
        )
    )
    runtime_gate = (
        spec["model_mapping"].get("solver") == "simpleFoam"
        and spec["model_mapping"].get("runtime_library") == "libTmrSSTm.so"
        and spec["model_mapping"].get("image_id") == IMAGE_ID
        and image.get("Id") == IMAGE_ID
        and all(stage.get("stage_passed") for stage in execution)
        and any("simpleFoam" in stage.get("stage", "") for stage in execution)
    )
    log_path = solver_log(case)
    log = log_path.read_text()
    model_gate = all(
        re.search(pattern, log)
        for pattern in (
            r"Selecting incompressible transport model Newtonian",
            r"Selecting RAS turbulence model TmrSSTm",
            r"gamma1\s+0\.553166",
            r"gamma2\s+0\.44035",
            r"c1\s+20;",
        )
    )

    columns, values = coefficient_history(case)
    indices = {name: columns.index(name) for name in ("Time", "Cd", "Cl", "CmPitch")}
    if len(values) < max(window, 500):
        raise ValueError("Need at least 500 coefficient samples")
    tail = values[-window:]
    means = {
        name: float(tail[:, indices[name]].mean())
        for name in ("Cd", "Cl", "CmPitch")
    }
    peak_to_peak = {
        name: float(np.ptp(tail[:, indices[name]]))
        for name in ("Cd", "Cl", "CmPitch")
    }
    projected, limits, trend_gate = long_window_trend(values, indices, 0.0, 500)
    final_residuals, recent_max_residuals, equations_gate = residual_gate(log, window)
    symmetry_gate = abs(means["Cl"]) <= 0.01 and abs(means["CmPitch"]) <= 0.01
    settling_gate = all(value <= 0.01 for value in peak_to_peak.values())
    preflight = all(
        (
            provenance_gate,
            runtime_gate,
            model_gate,
            trend_gate,
            equations_gate,
            symmetry_gate,
            settling_gate,
        )
    )
    cfl3d = cfl3d_reference(
        benchmark_data.resolve(strict=True) / "n0012clcd_cfl3d_sst.dat", 0.0
    )
    cfl3d["control_minus_cfl3d_cd"] = means["Cd"] - cfl3d["cd"]

    return {
        "scope": "diagnostic incompressible solver-path control only",
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "runtime_and_execution_gate": runtime_gate,
        "restart_provenance_gate": provenance_gate,
        "model_configuration_gate": bool(model_gate),
        "last_window_mean": means,
        "last_window_peak_to_peak": peak_to_peak,
        "settling_gate": settling_gate,
        "projected_change_over_500_iterations": projected,
        "trend_absolute_limits": limits,
        "long_window_trend_gate": trend_gate,
        "solver_initial_residuals_final": final_residuals,
        "solver_initial_residuals_last_100_max": recent_max_residuals,
        "solver_residual_gate": equations_gate,
        "zero_angle_symmetry_gate": symmetry_gate,
        "drag_decomposition": drag_decomposition(log_path),
        "tmr_cfl3d_sst_reference": cfl3d,
        "control_preflight_passed": preflight,
        "production_compressible_workflow_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.case, args.benchmark_data)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-incompressible-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
