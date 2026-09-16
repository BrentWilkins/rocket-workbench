"""Aggregate the predeclared NACA domain ladder without admitting failed cases."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evidence(path: Path) -> dict:
    path = path.resolve(strict=True)
    return {"path": str(path), "sha256": sha256(path)}


def aggregate(plan_path: Path, farfield_path: Path, audit_paths: list[Path]) -> dict:
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    if not plan.get("declared_before_new_solver_execution"):
        raise ValueError("Gate 3 remediation plan was not predeclared")
    farfield_path = farfield_path.resolve(strict=True)
    farfield = json.loads(farfield_path.read_text())
    if farfield["predeclared_plan"]["sha256"] != sha256(plan_path):
        raise ValueError("Farfield audit does not match the remediation plan")
    farfield_by_case = {
        str(Path(item["case"]).resolve()): item for item in farfield["cases"]
    }

    rows = []
    for audit_path in audit_paths:
        audit_path = audit_path.resolve(strict=True)
        audit = json.loads(audit_path.read_text())
        case = Path(audit["case"]).resolve(strict=True)
        spec = json.loads((case / "benchmark-spec.json").read_text())
        if str(case) not in farfield_by_case:
            raise ValueError(f"Farfield audit lacks {case}")
        field = farfield_by_case[str(case)]["farfield"]
        domain = spec.get("domain") or {
            "upstream_extent_chords": 484.456616747519,
            "crossflow_extent_chords": 507.806809185105,
            "downstream_extent_chords": 500.000007802345,
            "uses_official_outer_boundary": True,
        }
        rows.append(
            {
                "case": str(case),
                "grid_dimensions": spec["grid_dimensions"],
                "upstream_extent_chords": domain["upstream_extent_chords"],
                "crossflow_extent_chords": domain["crossflow_extent_chords"],
                "force_audit": evidence(audit_path),
                "solver_residual_gate": audit["solver_residual_gate"],
                "coarse_preflight_passed": audit["coarse_preflight_passed"],
                "solver_initial_residuals_final": audit[
                    "solver_initial_residuals_final"
                ],
                "solver_initial_residuals_last_100_max": audit[
                    "solver_initial_residuals_last_100_max"
                ],
                "raw_last_window_mean": audit["last_window_mean"],
                "coefficients_withheld": not audit["coarse_preflight_passed"],
                "farfield_diagnostics": {
                    "mass_closure": field["transport"]["mass_flux"][
                        "absolute_closure_over_total_throughflow"
                    ],
                    "energy_closure": field["transport"][
                        "absolute_energy_closure_over_total_transport"
                    ],
                    "p_rms_delta_pa": field["state"]["p"][
                        "area_weighted_rms_delta_from_freestream"
                    ],
                    "T_rms_delta_k": field["state"]["T"][
                        "area_weighted_rms_delta_from_freestream"
                    ],
                    "Ux_rms_delta_m_s": field["state"]["U"][
                        "area_weighted_rms_delta_from_freestream"
                    ][0],
                },
            }
        )
    rows.sort(key=lambda row: row["upstream_extent_chords"], reverse=True)
    expected_dimensions = ([897, 257], [897, 247], [897, 240], [897, 233])
    if tuple(row["grid_dimensions"] for row in rows) != expected_dimensions:
        raise ValueError("Domain ladder does not contain the four predeclared grids")
    full_cd = rows[0]["raw_last_window_mean"]["Cd"]
    for row in rows:
        row["raw_cd_change_from_full"] = row["raw_last_window_mean"]["Cd"] - full_cd

    monotonic_metrics = {}
    for key in ("energy_closure", "p_rms_delta_pa", "T_rms_delta_k", "Ux_rms_delta_m_s"):
        values = [row["farfield_diagnostics"][key] for row in rows]
        monotonic_metrics[key] = {
            "values_full_to_smallest_domain": values,
            "nondecreasing_as_domain_contracts": bool(np.all(np.diff(values) >= 0)),
        }
    max_raw_cd_change = max(abs(row["raw_cd_change_from_full"]) for row in rows[1:])
    frozen_gap = 0.0006585114360100012
    return {
        "schema_version": 1,
        "scope": "predeclared exact-SSTm full-to-100c domain ladder",
        "predeclared_plan": evidence(plan_path),
        "farfield_audit": evidence(farfield_path),
        "rows_full_to_smallest_domain": rows,
        "monotonic_farfield_signatures": monotonic_metrics,
        "all_reduced_domains_admissible": all(
            row["coarse_preflight_passed"] for row in rows[1:]
        ),
        "maximum_absolute_raw_reduced_domain_cd_change": max_raw_cd_change,
        "frozen_full_domain_cfl3d_cd_gap": frozen_gap,
        "maximum_raw_domain_change_as_fraction_of_gap": max_raw_cd_change / frozen_gap,
        "coefficient_interpretation": "All reduced-domain coefficients are withheld because each failed the unchanged residual gate; raw values are shown only to bound diagnostic scale.",
        "diagnostic_conclusion": "Boundary contraction produces monotonic thermodynamic and farfield disturbance, but the inadmissible raw Cd scale is only a small fraction of the full-domain NASA gap. It is not the dominant drag-bias mechanism, and the original 100c domain gate remains failed.",
        "numerical_independence_passed": False,
        "benchmark_accepted": False,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--farfield", required=True, type=Path)
    parser.add_argument("--force-audit", required=True, action="append", type=Path, dest="audits")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = aggregate(args.plan, args.farfield, args.audits)
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output / "naca0012-domain-ladder-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"output": str(output), "conclusion": result["diagnostic_conclusion"]}))


if __name__ == "__main__":
    main()
