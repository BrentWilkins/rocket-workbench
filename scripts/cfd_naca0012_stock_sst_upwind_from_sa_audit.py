"""Audit the predeclared stock-SST upwind replication from the accepted SA source."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from cfd_naca0012_stock_sst_audit import audit as base_stock_audit
from cfd_naca0012_stock_sst_audit import sha256
from cfd_naca0012_stock_sst_restart import reset_field_location
from cfd_naca0012_stock_sst_upwind_from_sa import METHOD, PLAN
from cfd_naca0012_stock_sst_upwind_restart import _replace_once


def audit(case: Path, benchmark_data: Path, window: int = 100) -> dict:
    case = case.resolve(strict=True)
    benchmark_data = benchmark_data.resolve(strict=True)
    plan = json.loads(PLAN.read_text())
    spec_path = case / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    record = json.loads((case / "stock-sst-upwind-from-sa-execution.json").read_text())
    base_record = json.loads((case / "stock-sst-restart-execution.json").read_text())
    source = Path(spec["initialization"]["source_case"]).resolve(strict=True)
    source_audit_path = Path(spec["initialization"]["source_audit"]).resolve(strict=True)
    source_audit = json.loads(source_audit_path.read_text())

    required_source_gate = all(
        source_audit.get(name) == expected
        for name, expected in plan["source"]["required_gates"].items()
    )
    source_gate = (
        sha256(source / "benchmark-spec.json") == plan["source"]["case_spec_sha256"]
        and sha256(source_audit_path) == plan["source"]["audit_sha256"]
        and Path(source_audit.get("case", "")).resolve() == source
        and required_source_gate
    )

    initialization = spec["initialization"]
    copied_fields_gate = (
        initialization.get("method") == METHOD
        and set(initialization.get("copied_solution_fields", {})) == {"U", "p"}
        and set(initialization.get("new_turbulence_fields", [])) == {"k", "omega", "nut"}
        and all(
            Path(entry["source"]).is_file()
            and sha256(Path(entry["source"])) == entry["source_sha256"]
            and sha256(case / "0" / name) == entry["target_sha256"]
            and (case / "0" / name).read_text()
            == reset_field_location(Path(entry["source"]).read_text())
            for name, entry in initialization["copied_solution_fields"].items()
        )
    )

    change = spec["change_control"]
    target_schemes_path = case / "system" / "fvSchemes"
    target_schemes = target_schemes_path.read_text()
    generated_schemes = _replace_once(
        target_schemes,
        "div(phi,k) bounded Gauss upwind;",
        "div(phi,k) bounded Gauss linearUpwind grad(k);",
    )
    generated_schemes = _replace_once(
        generated_schemes,
        "div(phi,omega) bounded Gauss upwind;",
        "div(phi,omega) bounded Gauss linearUpwind grad(omega);",
    )
    generated_hash = hashlib.sha256(generated_schemes.encode()).hexdigest()
    scheme_change_gate = (
        generated_hash == change.get("source_generated_fvSchemes_sha256")
        and sha256(target_schemes_path) == change.get("target_fvSchemes_sha256")
        and spec["numerics"].get("velocity_convection")
        == "bounded Gauss linearUpwind grad(U)"
        and spec["numerics"].get("k_convection") == "bounded Gauss upwind"
        and spec["numerics"].get("omega_convection") == "bounded Gauss upwind"
        and change.get("declared_change")
        == "stock-SST k and omega convection from bounded linearUpwind to bounded upwind only"
    )

    copied = change["copied_source_file_sha256"]
    direct_copy_names = {
        "constant/transportProperties",
        "system/controlDict",
        "system/decomposeParDict",
        "constant/polyMesh/boundary",
        "constant/polyMesh/faces",
        "constant/polyMesh/neighbour",
        "constant/polyMesh/owner",
        "constant/polyMesh/points",
    }
    copied_invariants_gate = all(
        relative in copied
        and sha256(source / relative) == copied[relative]
        and sha256(case / relative) == copied[relative]
        for relative in direct_copy_names
    )

    wrapper_snapshot = case / "provenance" / change["implementation"]
    wrapper_plan_snapshot = case / "provenance" / PLAN.name
    base_snapshot = case / "provenance" / change["base_builder_implementation_snapshot"]
    base_plan_path = Path(change["base_builder_plan"])
    base_plan_snapshot = case / "provenance" / base_plan_path.name
    construction_gate = (
        record.get("stage") == METHOD
        and record.get("stage_passed") is True
        and record.get("source_audit_sha256") == sha256(source_audit_path)
        and record.get("plan_sha256") == sha256(PLAN)
        and record.get("target_case_spec_sha256") == sha256(spec_path)
        and wrapper_snapshot.is_file()
        and sha256(wrapper_snapshot) == change.get("implementation_sha256")
        and wrapper_plan_snapshot.is_file()
        and sha256(wrapper_plan_snapshot) == sha256(PLAN)
        and base_snapshot.is_file()
        and sha256(base_snapshot) == change.get("base_builder_implementation_sha256")
        and base_plan_path.is_file()
        and sha256(base_plan_path) == change.get("base_builder_plan_sha256")
        and base_plan_snapshot.is_file()
        and sha256(base_plan_snapshot) == change.get("base_builder_plan_sha256")
        and base_record.get("stage_passed") is True
        # The base builder predates the source-audit digest field.  Its immutable
        # source paths and plan digest are still recorded; the wrapper record
        # above supplies and verifies the missing audit digest.
        and Path(base_record.get("source_case", "")).resolve() == source
        and Path(base_record.get("source_audit", "")).resolve()
        == source_audit_path
        and base_record.get("plan_sha256") == change.get("base_builder_plan_sha256")
    )
    provenance_gate = all(
        (
            source_gate,
            copied_fields_gate,
            scheme_change_gate,
            copied_invariants_gate,
            construction_gate,
        )
    )

    base = base_stock_audit(case, benchmark_data, window)
    base_provenance_gate = base["provenance_gate"]
    diagnostic_numerics_passed = all(
        base[name]
        for name in (
            "runtime_and_execution_gate",
            "model_configuration_gate",
            "finite_force_history_gate",
            "iteration_horizon_gate",
            "settling_gate",
            "long_window_trend_gate",
            "solver_residual_gate",
            "zero_angle_symmetry_gate",
        )
    ) and provenance_gate
    base.update(
        {
            "schema_version": 1,
            "scope": "Direct SA-to-stock-SST upwind replication downstream of failed Gate 1",
            "plan": str(PLAN),
            "plan_sha256": sha256(PLAN),
            "source_required_state_gate": required_source_gate,
            "source_provenance_gate": source_gate,
            "copied_solution_fields_gate": copied_fields_gate,
            "copied_invariants_gate": copied_invariants_gate,
            "scheme_change_only_gate": scheme_change_gate,
            "construction_provenance_gate": construction_gate,
            "base_linearupwind_audit_provenance_gate_expected_false": base_provenance_gate,
            "provenance_gate": provenance_gate,
            "diagnostic_numerics_passed": diagnostic_numerics_passed,
            "replication_passed": diagnostic_numerics_passed,
            "strict_gate_2_passed": False,
            "strict_gate_2_status": "blocked_by_failed_gate_1",
            "accepted_for_rocket": False,
        }
    )
    return base


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--benchmark-data", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--window", type=int, default=100)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    result = audit(args.case, args.benchmark_data, args.window)
    args.output.mkdir(parents=True)
    output = args.output / "naca0012-stock-sst-upwind-from-sa-audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
