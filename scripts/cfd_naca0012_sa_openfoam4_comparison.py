"""Classify the predeclared OpenFOAM Foundation v4 SA lineage screen."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from cfd_naca0012_sa_freestream_restart import sha256
from cfd_naca0012_sa_nonorthogonal_comparison import classify


PLAN_SHA256 = "38d43843791eb822b613441392d79d9532a33d522eb5a8b72c30a23ca3c04c12"
SOURCE_AUDIT_SHA256 = "ff6fe49324c620978b6a1628d3a62eb56af8ac01a22aa7c6de4174dba9ca283f"


def compare(source_audit: Path, screen_audit: Path, plan: Path) -> dict:
    source_audit = source_audit.resolve(strict=True)
    screen_audit = screen_audit.resolve(strict=True)
    plan = plan.resolve(strict=True)
    if sha256(plan) != PLAN_SHA256:
        raise ValueError("OpenFOAM v4 lineage plan checksum mismatch")
    if sha256(source_audit) != SOURCE_AUDIT_SHA256:
        raise ValueError("Settled source audit checksum mismatch")
    source = json.loads(source_audit.read_text())
    screen = json.loads(screen_audit.read_text())
    if not all(
        screen.get(key) is True
        for key in (
            "provenance_gate",
            "restart_provenance_gate",
            "runtime_and_execution_gate",
            "model_configuration_gate",
            "settling_gate",
            "long_window_trend_gate",
        )
    ):
        raise ValueError("Screen did not pass execution and provenance prerequisites")

    source_cd = float(source["last_window_mean"]["Cd"])
    screen_cd = float(screen["last_window_mean"]["Cd"])
    delta_cd = screen_cd - source_cd
    improvement = -delta_cd
    classification = classify(delta_cd)
    gap_before = float(source["openfoam_minus_cfl3d"]["cd"])
    gap_after = float(screen["openfoam_minus_cfl3d"]["cd"])
    return {
        "scope": "Predeclared OpenFOAM Foundation v4 lineage screen",
        "plan": str(plan),
        "plan_sha256": sha256(plan),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "screen_audit": str(screen_audit),
        "screen_audit_sha256": sha256(screen_audit),
        "change": {
            "distribution_and_version": {
                "before": "OpenCFD v2512",
                "after": "OpenFOAM Foundation 4.1",
            }
        },
        "last_100_mean_cd": {"source": source_cd, "screen": screen_cd},
        "screen_minus_source_cd": delta_cd,
        "drag_improvement": improvement,
        "nasa_gap": {"before": gap_before, "after": gap_after},
        "fraction_of_original_nasa_gap_closed": improvement / gap_before,
        "classification": classification,
        "terminal_rule_applied": "Stop after the declared 1000 iterations; do not extend a null screen.",
        "conclusion": (
            "Foundation v4 lineage is ruled out as the missing cause of the "
            "official alpha-zero SA drag agreement under the documented setup."
            if classification == "null_effect"
            else "The historical lineage mechanism remains open under the declared rule."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--screen-audit", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = compare(args.source_audit, args.screen_audit, args.plan)
    args.output.mkdir(parents=True, exist_ok=False)
    artifact = args.output / "naca0012-sa-openfoam4-comparison.json"
    artifact.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
