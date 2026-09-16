"""Verify that a retained TMR flat-plate run used the declared SST mapping."""

import argparse
import hashlib
import json
import re
from pathlib import Path

from cfd_flat_plate_boundary_audit import audit as boundary_audit


EXPECTED_COEFFICIENTS = {
    "gamma1": 0.5531666666666668,
    "gamma2": 0.4403546666666667,
    "c1": 20.0,
    "alphaK1": 0.85,
    "alphaK2": 1.0,
    "alphaOmega1": 0.5,
    "alphaOmega2": 0.856,
    "beta1": 0.075,
    "beta2": 0.0828,
    "betaStar": 0.09,
    "a1": 0.31,
    "b1": 1.0,
}


def coefficient_block(log: str, block_name: str = "kOmegaSSTCoeffs") -> dict[str, float]:
    match = re.search(rf"{re.escape(block_name)}\s*\{{(?P<body>.*?)\}}", log, re.DOTALL)
    if not match:
        raise ValueError(f"Solver log has no printed {block_name} block")
    found = {}
    for name, value in re.findall(r"\b(\w+)\s+([-+0-9.eE]+)\s*;", match["body"]):
        found[name] = float(value)
    return found


def close_enough(actual: float, expected: float) -> bool:
    # OpenFOAM's coefficient report uses six significant decimal digits.
    return abs(actual - expected) <= max(5e-7, abs(expected) * 1e-6)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit(case: Path, provenance_path: Path | None = None) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    mapping = spec.get("model_mapping")
    if not isinstance(mapping, dict):
        raise ValueError("Case predates structured SST model mapping")
    supported_variants = {
        "tmr-sst-vm-flatplate-equivalent",  # retained legacy label; not accepted as equivalent
        "tmr-sstm-flatplate-partial-map",
        "tmr-sstm-v2512-source-map",
    }
    if mapping.get("variant") not in supported_variants:
        raise ValueError("Case is not a coefficient-mapped TMR SSTm flat-plate variant")
    wall = spec["omega_wall_treatment"]
    if wall["variant"] != "tmr-fixed-factor10":
        raise ValueError("Mapped case did not declare the TMR factor-10 omega wall value")

    execution = json.loads((case / "execution.json").read_text())
    solvers = [
        (index, record)
        for index, record in enumerate(execution)
        if "simpleFoam" in record["stage"]
    ]
    if len(solvers) != 1:
        raise ValueError(f"Expected one retained simpleFoam stage, found {len(solvers)}")
    solver_index, solver_record = solvers[0]
    if solver_record["returncode"] != 0 or not solver_record["stage_passed"]:
        raise ValueError("Retained simpleFoam stage did not pass")
    solver_name = solver_record["stage"].split()[0]
    log_path = case / f"{solver_index}-{solver_name}.log"
    exact_mapping = mapping["variant"] == "tmr-sstm-v2512-source-map"
    log_text = log_path.read_text()
    reported = coefficient_block(
        log_text,
        "TmrSSTmCoeffs" if exact_mapping else "kOmegaSSTCoeffs",
    )
    comparisons = {
        name: {
            "expected": expected,
            "reported": reported.get(name),
            "passed": name in reported and close_enough(reported[name], expected),
        }
        for name, expected in EXPECTED_COEFFICIENTS.items()
    }

    omega_text = (case / "0" / "omega").read_text()
    plate = re.search(r"plate\s*\{(?P<body>.*?)\}", omega_text, re.DOTALL)
    if not plate:
        raise ValueError("Initial omega field has no plate patch")
    wall_value_match = re.search(
        r"value\s+uniform\s+([-+0-9.eE]+)\s*;", plate["body"]
    )
    fixed_value = bool(re.search(r"type\s+fixedValue\s*;", plate["body"]))
    actual_wall_value = float(wall_value_match.group(1)) if wall_value_match else None
    expected_wall_value = float(wall["fixed_value_s-1"])
    wall_passed = bool(
        fixed_value
        and actual_wall_value is not None
        and close_enough(actual_wall_value, expected_wall_value)
    )
    passed = bool(all(item["passed"] for item in comparisons.values()) and wall_passed)

    provenance_result = None
    equation_mapping_complete = False
    known_unmapped = [
        "F1/F2 implementation details and cross-diffusion floor",
        "strain-rate rather than vorticity eddy-viscosity limiter invariant",
    ]
    scope_limit = (
        "Runtime coefficient and wall-value verification only; exact SSTm equation mapping "
        "remains incomplete. Legacy manifests that name SST-Vm are mislabeled evidence."
    )
    if exact_mapping:
        if provenance_path is None:
            provenance_path = Path(__file__).resolve().parents[1] / "cfd/sstm-image-provenance.json"
        provenance = json.loads(provenance_path.read_text())
        repo = Path(__file__).resolve().parents[1]
        source_checks = {
            name: {
                "expected": expected,
                "actual": sha256(repo / name),
                "passed": sha256(repo / name) == expected,
            }
            for name, expected in provenance["build_inputs_sha256"].items()
        }
        image = json.loads((case / "image.json").read_text())
        image_passed = image.get("Id") == provenance["sstm_image"]["id"]
        runtime_selected = bool(
            re.search(r"Selecting RAS turbulence model\s+TmrSSTm", log_text)
        )
        manifest_complete = mapping.get("equation_mapping_complete") is True
        boundary_mapping_passed = boundary_audit(case)["published_boundary_screen"]
        provenance_passed = bool(
            image_passed
            and runtime_selected
            and manifest_complete
            and boundary_mapping_passed
            and all(item["passed"] for item in source_checks.values())
        )
        provenance_result = {
            "provenance_file": str(provenance_path),
            "image_expected": provenance["sstm_image"]["id"],
            "image_actual": image.get("Id"),
            "image_passed": image_passed,
            "runtime_model_selected": runtime_selected,
            "manifest_mapping_complete": manifest_complete,
            "published_boundary_mapping_passed": boundary_mapping_passed,
            "build_inputs": source_checks,
            "passed": provenance_passed,
        }
        equation_mapping_complete = provenance_passed
        known_unmapped = (
            [] if provenance_passed
            else ["source/build/runtime/boundary mapping verification failed"]
        )
        scope_limit = (
            "Source-level SSTm mapping and runtime provenance screen only; independent "
            "numerical and benchmark gates remain required."
        )
    return {
        "variant": mapping["variant"],
        "solver_log": str(log_path),
        "reported_coefficients": comparisons,
        "omega_wall": {
            "type": "fixedValue" if fixed_value else "other",
            "expected_s-1": expected_wall_value,
            "actual_s-1": actual_wall_value,
            "passed": wall_passed,
        },
        "flat_plate_runtime_configuration_screen": passed,
        "source_mapping_provenance": provenance_result,
        "equation_mapping_complete": equation_mapping_complete,
        "known_unmapped_differences": known_unmapped,
        "scope_limit": scope_limit,
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--provenance", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = audit(args.case, args.provenance)
    (args.output / "flat-plate-model-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
