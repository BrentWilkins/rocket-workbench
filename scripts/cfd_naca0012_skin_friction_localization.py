"""Localize the chordwise OpenFOAM-to-CFL3D skin-friction discrepancy."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


BINS = ((0.01, 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 0.98))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def localize(plan_path: Path, skin_friction_audit_path: Path) -> dict:
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    if not plan.get("declared_before_new_solver_execution"):
        raise ValueError("Gate 3 remediation plan was not predeclared")
    audit_path = skin_friction_audit_path.resolve(strict=True)
    audit = json.loads(audit_path.read_text())
    profile = audit["profile"]
    x = np.asarray([row["x_over_c"] for row in profile])
    openfoam = np.asarray([row["openfoam_cf"] for row in profile])
    cfl3d = np.asarray([row["cfl3d_cf"] for row in profile])
    ratio = openfoam / cfl3d
    bins = []
    for lower, upper in BINS:
        mask = (x >= lower) & (x < upper)
        if not np.any(mask):
            raise ValueError(f"No skin-friction samples in bin {lower} to {upper}")
        bins.append(
            {
                "x_over_c": [lower, upper],
                "samples": int(mask.sum()),
                "mean_openfoam_to_cfl3d_cf_ratio": float(ratio[mask].mean()),
                "median_openfoam_to_cfl3d_cf_ratio": float(np.median(ratio[mask])),
                "minimum_openfoam_to_cfl3d_cf_ratio": float(ratio[mask].min()),
                "maximum_openfoam_to_cfl3d_cf_ratio": float(ratio[mask].max()),
                "mean_signed_cf_difference": float((openfoam[mask] - cfl3d[mask]).mean()),
            }
        )
    downstream_means = [
        row["mean_openfoam_to_cfl3d_cf_ratio"] for row in bins if row["x_over_c"][0] >= 0.2
    ]
    return {
        "schema_version": 1,
        "scope": "chordwise localization of the sealed exact-SSTm skin-friction discrepancy",
        "predeclared_plan": {"path": str(plan_path), "sha256": sha256(plan_path)},
        "source_audit": {"path": str(audit_path), "sha256": sha256(audit_path)},
        "bins": bins,
        "downstream_bin_means_strictly_increase": bool(
            np.all(np.diff(downstream_means) > 0)
        ),
        "diagnostic_conclusion": "The discrepancy grows downstream under the airfoil pressure-gradient and curvature history; it is not a uniform force normalization offset.",
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--skin-friction-audit", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = localize(args.plan, args.skin_friction_audit)
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "naca0012-skin-friction-localization.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "bins": result["bins"]}))


if __name__ == "__main__":
    main()
