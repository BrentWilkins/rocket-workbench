"""Compare one-cell and two-layer airfoil wall-velocity gradients."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from cfd_naca0012_farfield_audit import latest_time, sha256
from cfd_naca0012_surface_force_audit import internal_vector, patch_owners


BINS = ((0.01, 0.05), (0.05, 0.1), (0.1, 0.2), (0.2, 0.4), (0.4, 0.6),
        (0.6, 0.8), (0.8, 0.98))


def evidence(path: Path) -> dict:
    return {"path": str(path), "sha256": sha256(path)}


def audit(plan_path: Path, case: Path, shear_output: Path) -> dict:
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    if not plan.get("declared_before_new_solver_execution"):
        raise ValueError("Gate 3 remediation plan was not predeclared")
    case = case.resolve(strict=True)
    time = latest_time(case)
    velocity_path = time / "U"
    velocity = internal_vector(velocity_path)
    owners = patch_owners(case, "airfoil")
    with np.load(case / "tmr-naca0012-grid.npz") as grid:
        x = grid["x"]
        y = grid["y"]
    ni = x.shape[1]
    cell_i = owners % (ni - 1)
    cell_j = owners // (ni - 1)
    if np.any(cell_j != 0):
        raise ValueError("Airfoil owner cells are not in the first structured layer")
    second = owners + (ni - 1)

    wall_a = np.column_stack((x[0, cell_i], y[0, cell_i]))
    wall_b = np.column_stack((x[0, cell_i + 1], y[0, cell_i + 1]))
    tangent = wall_b - wall_a
    tangent /= np.linalg.norm(tangent, axis=1)[:, None]
    centers0 = np.column_stack(
        (
            (x[0, cell_i] + x[0, cell_i + 1] + x[1, cell_i + 1] + x[1, cell_i]) / 4,
            (y[0, cell_i] + y[0, cell_i + 1] + y[1, cell_i + 1] + y[1, cell_i]) / 4,
        )
    )
    centers1 = np.column_stack(
        (
            (x[1, cell_i] + x[1, cell_i + 1] + x[2, cell_i + 1] + x[2, cell_i]) / 4,
            (y[1, cell_i] + y[1, cell_i + 1] + y[2, cell_i + 1] + y[2, cell_i]) / 4,
        )
    )
    normal = np.column_stack((-tangent[:, 1], tangent[:, 0]))
    wall_center = 0.5 * (wall_a + wall_b)
    d0 = np.abs(np.sum((centers0 - wall_center) * normal, axis=1))
    d1 = np.abs(np.sum((centers1 - wall_center) * normal, axis=1))
    u0 = np.sum(velocity[owners, :2] * tangent, axis=1)
    u1 = np.sum(velocity[second, :2] * tangent, axis=1)
    first = u0 / d0
    quadratic = (u0 * d1**2 - u1 * d0**2) / (d0 * d1 * (d1 - d0))
    ratio = quadratic / first
    x_over_c = wall_center[:, 0]
    retained = (
        (x_over_c >= 0.01)
        & (x_over_c <= 0.98)
        & np.isfinite(ratio)
        & (np.abs(first) > 0)
        & (d1 > d0)
    )
    if retained.sum() < 100:
        raise ValueError(
            "Too few retained wall-gradient samples: "
            f"x-range={int(((x_over_c >= 0.01) & (x_over_c <= 0.98)).sum())}, "
            f"finite={int(np.isfinite(ratio).sum())}, "
            f"d1>d0={int((d1 > d0).sum())}, total={len(owners)}"
        )

    bins = []
    for lower, upper in BINS:
        selected = retained & (x_over_c >= lower) & (x_over_c < upper)
        values = ratio[selected]
        bins.append(
            {
                "x_over_c": [lower, upper],
                "samples": int(selected.sum()),
                "quadratic_to_one_cell_gradient_mean": float(values.mean()),
                "quadratic_to_one_cell_gradient_median": float(np.median(values)),
                "quadratic_to_one_cell_gradient_rms_from_one": float(
                    np.sqrt(np.mean((values - 1) ** 2))
                ),
            }
        )
    values = ratio[retained]
    shear_execution = (shear_output.resolve(strict=True) / "execution.json")
    return {
        "schema_version": 1,
        "scope": "fixed-solution two-layer wall-gradient discretization diagnostic",
        "predeclared_plan": evidence(plan_path),
        "case": str(case),
        "solution_time": float(time.name),
        "source_hashes": {
            "case_spec": sha256(case / "benchmark-spec.json"),
            "velocity_field": sha256(velocity_path),
            "structured_grid": sha256(case / "tmr-naca0012-grid.npz"),
            "wall_shear_execution": sha256(shear_execution),
        },
        "method": (
            "Project first- and second-layer cell-centre velocity onto each wall-face "
            "tangent; compare U_t1/d1 with the wall derivative of the quadratic "
            "through no-slip wall, layer one, and layer two. This is a fixed-solution "
            "diagnostic and does not replace a solver sensitivity."
        ),
        "retained_x_over_c": [0.01, 0.98],
        "retained_samples": int(retained.sum()),
        "quadratic_to_one_cell_gradient": {
            "mean": float(values.mean()),
            "median": float(np.median(values)),
            "minimum": float(values.min()),
            "maximum": float(values.max()),
            "rms_from_one": float(np.sqrt(np.mean((values - 1) ** 2))),
        },
        "bins": bins,
        "interpretation_limit": (
            "Second-layer centres are projected onto the local face tangent and normal "
            "without streamwise interpolation; material results require a predeclared "
            "solver-level wall-gradient sensitivity."
        ),
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--wall-shear-output", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = audit(args.plan, args.case, args.wall_shear_output)
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "naca0012-wall-gradient-order-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "summary": result["quadratic_to_one_cell_gradient"], "bins": result["bins"]}))


if __name__ == "__main__":
    main()
