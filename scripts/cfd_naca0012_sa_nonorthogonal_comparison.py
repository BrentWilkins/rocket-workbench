"""Classify the predeclared NACA 0012 non-orthogonal-corrector screen."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


PLAN_SHA256 = "a4ca0b1382e35c5356680e96135c23876a8f2fe5242032f51a739814b12b8354"
SOURCE_AUDIT_SHA256 = "ff6fe49324c620978b6a1628d3a62eb56af8ac01a22aa7c6de4174dba9ca283f"
MATERIAL_THRESHOLD = 0.00005
NULL_THRESHOLD = 0.00002


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def classify(delta_cd: float) -> str:
    improvement = -delta_cd
    if abs(delta_cd) <= NULL_THRESHOLD:
        return "null_effect"
    if improvement >= MATERIAL_THRESHOLD:
        return "material_toward_official_plot"
    return "ambiguous_effect"


def compare(source_audit: Path, screen_audit: Path, plan: Path) -> dict:
    source_audit = source_audit.resolve(strict=True)
    screen_audit = screen_audit.resolve(strict=True)
    plan = plan.resolve(strict=True)
    if sha256(plan) != PLAN_SHA256:
        raise ValueError("Non-orthogonal-corrector screen plan checksum mismatch")
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

    nasa_gap_before = float(source["openfoam_minus_cfl3d"]["cd"])
    nasa_gap_after = float(screen["openfoam_minus_cfl3d"]["cd"])
    return {
        "scope": "Predeclared SIMPLE non-orthogonal-corrector screen",
        "plan": str(plan),
        "plan_sha256": sha256(plan),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "screen_audit": str(screen_audit),
        "screen_audit_sha256": sha256(screen_audit),
        "change": {"nNonOrthogonalCorrectors": {"before": 0, "after": 4}},
        "last_100_mean_cd": {"source": source_cd, "screen": screen_cd},
        "screen_minus_source_cd": delta_cd,
        "drag_improvement": improvement,
        "nasa_gap": {"before": nasa_gap_before, "after": nasa_gap_after},
        "fraction_of_original_nasa_gap_closed": improvement / nasa_gap_before,
        "thresholds": {
            "material_toward_official_plot": MATERIAL_THRESHOLD,
            "null_effect_absolute": NULL_THRESHOLD,
        },
        "classification": classification,
        "terminal_rule_applied": "Stop after the declared 1000 iterations; do not extend a null screen.",
        "conclusion": (
            "Four non-orthogonal correctors are ruled out as the missing cause of "
            "the documented SA drag agreement."
            if classification == "null_effect"
            else "The mechanism remains open under the predeclared decision rule."
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
    artifact = args.output / "naca0012-sa-nonorthogonal-comparison.json"
    artifact.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
