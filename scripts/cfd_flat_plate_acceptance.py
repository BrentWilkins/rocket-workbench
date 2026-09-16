"""Combine all flat-plate evidence into one fail-closed subsystem decision."""

import argparse
import hashlib
import json
from pathlib import Path


FILES = {
    "benchmark": "flat-plate-audit.json",
    "profile": "flat-plate-profile-audit.json",
    "outer": "flat-plate-outer-flow-audit.json",
    "near_wall": "flat-plate-near-wall-audit.json",
    "boundary": "flat-plate-boundary-audit.json",
    "model": "flat-plate-model-audit.json",
    "numerical": "flat-plate-numerical-study.json",
    "domain": "flat-plate-domain-study.json",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate(evidence: dict[str, dict]) -> dict:
    benchmark = evidence["benchmark"]
    model = evidence["model"]
    gates = {
        "iterative_residuals": benchmark["iterative_1e-7_screen"],
        "skin_friction_correlation": benchmark[
            "cf_vs_karman_schoenherr_using_tmr_x_to_retheta"
        ]["engineering_5_percent_screen"],
        "momentum_thickness_extraction": benchmark[
            "edge_truncated_momentum_thickness_gate"
        ],
        "law_of_wall_profile": evidence["profile"]["profile_gate"],
        "outer_flow_quality": evidence["outer"]["outer_flow_quality_screen"],
        "wall_resolution": evidence["near_wall"]["wall_resolved_y_plus_screen"],
        "published_boundary_conditions": evidence["boundary"][
            "published_boundary_screen"
        ],
        "runtime_model_configuration": model[
            "flat_plate_runtime_configuration_screen"
        ],
        "sstm_equation_and_image_mapping": model["equation_mapping_complete"],
        "mesh_refinement": evidence["numerical"]["mesh_screen_passed"],
        "scheme_sensitivity": evidence["numerical"]["scheme_screen_passed"],
        "domain_sensitivity": evidence["domain"]["domain_screen_passed"],
    }
    return {
        "gates": gates,
        "flat_plate_subsystem_accepted": bool(all(gates.values())),
        "validated_scope": "attached_wall_and_sstm_turbulence_subsystem_only",
        "excluded_scope": [
            "external_body_pressure_force_and_moment",
            "separation_and_angle_of_attack",
            "rocket_geometry_and_fins",
            "flight_prediction",
        ],
        "accepted_for_rocket": False,
    }


def combine(paths: dict[str, Path]) -> dict:
    evidence = {name: json.loads(path.read_text()) for name, path in paths.items()}
    result = evaluate(evidence)
    result["evidence"] = {
        name: {"path": str(path), "sha256": sha256(path)}
        for name, path in paths.items()
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    for name in FILES:
        parser.add_argument(f"--{name.replace('_', '-')}", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    paths = {name: getattr(args, name) for name in FILES}
    args.output.mkdir(parents=True, exist_ok=False)
    result = combine(paths)
    (args.output / "flat-plate-acceptance.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
