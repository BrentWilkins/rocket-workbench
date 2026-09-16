"""Consolidate Gate 3 remediation evidence and enforce the downstream block."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> tuple[Path, dict]:
    resolved = path.resolve(strict=True)
    return resolved, json.loads(resolved.read_text())


def evidence(path: Path) -> dict:
    return {"path": str(path), "sha256": sha256(path)}


def decide(paths: dict[str, Path]) -> dict:
    loaded = {name: load(path) for name, path in paths.items()}
    plan_path, plan = loaded["plan"]
    if not plan.get("declared_before_new_solver_execution"):
        raise ValueError("Gate 3 remediation plan was not predeclared")
    data = {name: item[1] for name, item in loaded.items()}

    if data["wall_distance"]["exact_wall_distance_mechanism_supported"]:
        raise ValueError("A correction survived and requires Gate 3 revalidation")
    if data["domain"]["numerical_independence_passed"]:
        raise ValueError("Reduced-domain ladder unexpectedly passed")
    if data["solver_path"][
        "compressibility_or_thermophysical_coupling_is_dominant_explanation"
    ]:
        raise ValueError("Solver-path mechanism unexpectedly supported")
    if data["transport"]["transport_mismatch_is_dominant_explanation"]:
        raise ValueError("Transport mechanism unexpectedly supported")

    surface_fraction = data["surface_force"][
        "maximum_difference_as_fraction_of_benchmark_gap"
    ]
    gradient_ratio = data["gradient"]["comparison"][
        "airfoil_owner_cells_x_over_c_0p01_to_0p98"
    ]["sum_nut_S2_limited_over_unlimited"]
    wall_gradient = data["wall_gradient"]["quadratic_to_one_cell_gradient"]
    downstream_cf = data["localization"]["bins"][-1][
        "mean_openfoam_to_cfl3d_cf_ratio"
    ]
    if surface_fraction >= 1e-4:
        raise ValueError("Force reconstruction difference is not negligible")
    if abs(gradient_ratio - 1) >= 1e-3:
        raise ValueError("Gradient limiter remains a material candidate")
    if wall_gradient["rms_from_one"] >= 1e-3:
        raise ValueError("Wall-gradient order remains a material candidate")

    return {
        "schema_version": 1,
        "scope": "NACA 0012 exact-SSTm Gate 3 remediation decision",
        "predeclared_plan": evidence(plan_path),
        "evidence": {
            name: evidence(path)
            for name, (path, _) in loaded.items()
            if name != "plan"
        },
        "baseline_discrepancy": {
            "openfoam_mean_cd": data["wall_distance"]["drag"][
                "baseline_mean_cd"
            ],
            "cfl3d_cd": data["wall_distance"]["drag"]["baseline_mean_cd"]
            - data["wall_distance"]["drag"][
                "baseline_openfoam_minus_cfl3d_cd"
            ],
            "openfoam_minus_cfl3d_cd": data["wall_distance"]["drag"][
                "baseline_openfoam_minus_cfl3d_cd"
            ],
            "mean_openfoam_to_cfl3d_cf_ratio": data["wall_distance"][
                "skin_friction"
            ]["baseline_mean_openfoam_to_cfl3d_ratio"],
            "downstream_x_over_c_0p8_to_0p98_cf_ratio": downstream_cf,
        },
        "mechanism_findings": {
            "farfield_flux_and_boundary": (
                "Mass and total-enthalpy closure are small; boundary contraction "
                "increases disturbance monotonically but the inadmissible raw drag "
                "movement is only 9.85 percent of the baseline gap."
            ),
            "pressure_energy_solver_path": (
                "The incompressible control changes less than five percent of the "
                "gap and leaves viscous drag essentially unchanged."
            ),
            "surface_force_evaluation": {
                "maximum_component_difference_as_fraction_of_gap": surface_fraction,
                "dominant": False,
            },
            "velocity_gradient_limiter": {
                "limited_over_unlimited_sum_nut_S2": gradient_ratio,
                "dominant": False,
            },
            "wall_distance": {
                "fraction_of_materiality_threshold": data["wall_distance"]["drag"][
                    "fraction_of_materiality_threshold"
                ],
                "fraction_of_baseline_gap_removed": data["wall_distance"]["drag"][
                    "fraction_of_baseline_gap_removed"
                ],
                "dominant": False,
            },
            "wall_gradient_order": {
                "quadratic_to_one_cell_mean": wall_gradient["mean"],
                "quadratic_to_one_cell_downstream_mean": data["wall_gradient"][
                    "bins"
                ][-1]["quadratic_to_one_cell_gradient_mean"],
                "dominant": False,
            },
            "molecular_prandtl_and_sutherland": (
                "Exact Sutherland and Pr=0.72 remove less than one percent of the "
                "then-baseline gap."
            ),
            "sstm_equation_corrections": (
                "Correct limiter placement and exact S-squared production are "
                "required fidelity corrections but leave the accepted baseline "
                "discrepancy unresolved."
            ),
        },
        "supported_correction_found": False,
        "phase_5_gate3_revalidation_entered": False,
        "reason_phase_5_not_entered": (
            "The remediation plan requires a correction to survive its predeclared "
            "mechanism test. None did; rerunning or retuning the full Gate 3 suite "
            "would be post-hoc expenditure without a supported correction."
        ),
        "remaining_localization": (
            "The discrepancy is a solved-field boundary-layer history difference: "
            "OpenFOAM-to-CFL3D Cf is near unity over the forward chord and grows "
            "downstream, while force evaluation, molecular wall stress, wall distance, "
            "and the near-wall derivative stencil reproduce their declared operators."
        ),
        "next_scope_requires_decision": (
            "Further progress requires a separately predeclared cross-solver or "
            "higher-order discretization study, not another parameter change inside "
            "the pinned v2512 workflow."
        ),
        "validation_status": "rejected_not_validated",
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
        "downstream_10deg_rocket_openrocket_blocked": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in (
        "plan",
        "domain",
        "farfield",
        "surface_force",
        "gradient",
        "wall_distance",
        "wall_gradient",
        "solver_path",
        "transport",
        "production",
        "localization",
    ):
        parser.add_argument(f"--{name.replace('_', '-')}", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = decide(
        {
            name: getattr(args, name)
            for name in (
                "plan",
                "domain",
                "farfield",
                "surface_force",
                "gradient",
                "wall_distance",
                "wall_gradient",
                "solver_path",
                "transport",
                "production",
                "localization",
            )
        }
    )
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "naca0012-gate3-remediation-decision.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "status": result["validation_status"], "supported_correction_found": result["supported_correction_found"]}))


if __name__ == "__main__":
    main()
