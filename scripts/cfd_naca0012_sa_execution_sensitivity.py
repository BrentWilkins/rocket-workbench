"""Compare serial and 12-rank documented-SA execution results."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PLAN_SHA256 = "cb009af63a54c9b18602e8c5efce8a354055cc44a6361f25349cacd7e01b78b1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare(source_audit: Path, serial_audit: Path, plan: Path) -> dict:
    source_audit = source_audit.resolve(strict=True)
    serial_audit = serial_audit.resolve(strict=True)
    plan = plan.resolve(strict=True)
    if sha256(plan) != PLAN_SHA256:
        raise ValueError("SA serial plan checksum mismatch")

    source = json.loads(source_audit.read_text())
    serial = json.loads(serial_audit.read_text())
    serial_case = Path(serial["case"])
    serial_spec = json.loads((serial_case / "benchmark-spec.json").read_text())
    initialization = serial_spec["initialization"]
    mechanism = serial_spec["mechanism_test"]

    provenance_gate = (
        Path(initialization["source_case"]).resolve() == Path(source["case"]).resolve()
        and initialization["source_audit_sha256"] == sha256(source_audit)
        and mechanism["plan_sha256"] == PLAN_SHA256
        and mechanism["only_execution_decomposition_changed"] is True
        and mechanism["before"] == {"mpi_ranks": 12, "decomposition": "Scotch"}
        and mechanism["after"] == {"mpi_ranks": 1, "decomposition": "none"}
        and serial.get("restart_provenance_gate") is True
        and serial.get("runtime_and_execution_gate") is True
    )

    names = ("Cd", "Cl", "CmPitch")
    differences = {
        name: serial["last_window_mean"][name] - source["last_window_mean"][name]
        for name in names
    }
    limits = {"Cd": 0.0002, "Cl": 0.004, "CmPitch": 0.0002}
    coefficient_equivalence = {
        name: abs(differences[name]) <= limits[name] for name in names
    }
    source_uy = source["solver_initial_residuals_final"]["Uy"]
    serial_uy = serial["solver_initial_residuals_final"]["Uy"]
    residual_ratio = serial_uy / source_uy
    residual_gate_changed = (
        serial["solver_residual_gate"] != source["solver_residual_gate"]
    )
    dominant = residual_gate_changed or not all(coefficient_equivalence.values())

    return {
        "scope": (
            "Serial versus 12-rank Scotch execution sensitivity on identical "
            "documented-SA state"
        ),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "serial_audit": str(serial_audit),
        "serial_audit_sha256": sha256(serial_audit),
        "plan": str(plan),
        "plan_sha256": PLAN_SHA256,
        "provenance_gate": provenance_gate,
        "last_window_mean_difference_serial_minus_parallel": differences,
        "equivalence_limits": limits,
        "coefficient_equivalence": coefficient_equivalence,
        "source_final_uy_initial_residual": source_uy,
        "serial_final_uy_initial_residual": serial_uy,
        "serial_to_parallel_uy_residual_ratio": residual_ratio,
        "residual_gate_changed": residual_gate_changed,
        "decomposition_is_dominant_mechanism": dominant,
        "conclusion": (
            "Serial execution did not materially change the coefficients or clear "
            "the residual gate; 12-rank Scotch decomposition is not the dominant "
            "cause of the documented-SA discrepancy."
            if not dominant
            else "Execution decomposition changed the result materially."
        ),
        "gate": provenance_gate and not dominant,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--serial-audit", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = compare(args.source_audit, args.serial_audit, args.plan)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-sa-execution-sensitivity.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
