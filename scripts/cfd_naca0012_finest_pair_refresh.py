"""Audit the predeclared corrected-SSTm NACA finest nested-grid pair."""

import argparse
import hashlib
import json
import math
from pathlib import Path


COEFFICIENTS = ("Cd", "Cl", "CmPitch")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(case: Path, audit_path: Path) -> tuple[dict, dict]:
    case = case.resolve(strict=True)
    audit_path = audit_path.resolve(strict=True)
    spec = json.loads((case / "benchmark-spec.json").read_text())
    audit = json.loads(audit_path.read_text())
    if Path(audit.get("case", "")).resolve() != case:
        raise ValueError(f"Audit does not match case: {case}")
    if not audit.get("coarse_preflight_passed"):
        raise ValueError(f"Case diagnostic gates did not pass: {case}")
    return spec, audit


def evaluate(
    medium_case: Path,
    medium_audit_path: Path,
    fine_case: Path,
    fine_audit_path: Path,
) -> dict:
    medium_spec, medium_audit = load(medium_case, medium_audit_path)
    fine_spec, fine_audit = load(fine_case, fine_audit_path)

    if medium_spec.get("grid_dimensions") != [449, 129]:
        raise ValueError("Medium case is not the declared 449x129 grid")
    if fine_spec.get("grid_dimensions") != [897, 257]:
        raise ValueError("Fine case is not the declared 897x257 grid")
    if medium_spec["mesh"]["cells"] * 4 != fine_spec["mesh"]["cells"]:
        raise ValueError("Finest pair does not have the expected 4x cell refinement")

    for label, spec in (("medium", medium_spec), ("fine", fine_spec)):
        model = spec.get("model_mapping", {})
        conditions = spec.get("conditions", {})
        if spec.get("benchmark") != "TMR 2D NACA 0012":
            raise ValueError(f"{label} benchmark mismatch")
        if spec.get("convection_scheme") != "linear-upwind-velocity":
            raise ValueError(f"{label} scheme mismatch")
        if model.get("variant") != "tmr-sstm-exact-production":
            raise ValueError(f"{label} model mismatch")
        if model.get("runtime_library") != "libTmrSSTmExactProductionCompressible.so":
            raise ValueError(f"{label} runtime library mismatch")
        if conditions.get("transport_model") != "exact-sutherland-pr072":
            raise ValueError(f"{label} transport mismatch")
        if conditions.get("molecular_prandtl") != 0.72:
            raise ValueError(f"{label} molecular Prandtl mismatch")

    invariant_condition_keys = (
        "mach",
        "reynolds_number_chord",
        "angle_of_attack_deg",
        "chord_m",
        "temperature_k",
        "pressure_pa",
        "speed_m_s",
        "density_kg_m3",
        "dynamic_viscosity_pa_s",
        "turbulent_prandtl",
        "freestream_k_over_acoustic_speed_squared",
        "freestream_omega_mu_over_rho_acoustic_speed_squared",
    )
    for key in invariant_condition_keys:
        if medium_spec["conditions"].get(key) != fine_spec["conditions"].get(key):
            raise ValueError(f"Condition differs across finest pair: {key}")

    angle = math.radians(float(fine_spec["conditions"]["angle_of_attack_deg"]))
    limits = {
        "Cd": 0.0002,
        "Cl": 0.004 * abs(math.cos(angle)) + 0.0002 * abs(math.sin(angle)),
        "CmPitch": 0.0002,
    }
    changes = {
        name: {
            "signed_change": (
                fine_audit["last_window_mean"][name]
                - medium_audit["last_window_mean"][name]
            ),
            "absolute_change": abs(
                fine_audit["last_window_mean"][name]
                - medium_audit["last_window_mean"][name]
            ),
        }
        for name in COEFFICIENTS
    }
    passed = all(changes[name]["absolute_change"] <= limits[name] for name in COEFFICIENTS)

    return {
        "scope": "corrected NASA TMR SSTm finest-pair numerical refresh",
        "method": "direct nested-grid differences; no GCI or asymptotic claim",
        "medium": {
            "case": str(medium_case),
            "audit": str(medium_audit_path),
            "audit_sha256": sha256(medium_audit_path),
            "grid_dimensions": [449, 129],
            "cells": medium_spec["mesh"]["cells"],
            "mean": medium_audit["last_window_mean"],
        },
        "fine": {
            "case": str(fine_case),
            "audit": str(fine_audit_path),
            "audit_sha256": sha256(fine_audit_path),
            "grid_dimensions": [897, 257],
            "cells": fine_spec["mesh"]["cells"],
            "mean": fine_audit["last_window_mean"],
        },
        "coefficient_change": changes,
        "absolute_limits_from_experimental_repeatability": limits,
        "finest_pair_grid_independence_gate": passed,
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--medium-case", required=True, type=Path)
    parser.add_argument("--medium-audit", required=True, type=Path)
    parser.add_argument("--fine-case", required=True, type=Path)
    parser.add_argument("--fine-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    result = evaluate(
        args.medium_case,
        args.medium_audit,
        args.fine_case,
        args.fine_audit,
    )
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "naca0012-finest-pair-refresh.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
