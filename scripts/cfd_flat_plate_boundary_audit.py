"""Verify a retained flat-plate case matches the published TMR/OpenFOAM BC table."""

import argparse
import json
import re
from pathlib import Path


EXPECTED = {
    "U": {
        "inlet": "fixedValue", "outlet": "zeroGradient", "top": "zeroGradient",
        "symmetry": "symmetryPlane", "plate": "noSlip", "frontAndBack": "empty",
    },
    "p": {
        "inlet": "zeroGradient", "outlet": "fixedValue", "top": "zeroGradient",
        "symmetry": "symmetryPlane", "plate": "zeroGradient", "frontAndBack": "empty",
    },
    "k": {
        "inlet": "fixedValue", "outlet": "zeroGradient", "top": "zeroGradient",
        "symmetry": "symmetryPlane", "plate": "fixedValue", "frontAndBack": "empty",
    },
    "omega": {
        "inlet": "fixedValue", "outlet": "zeroGradient", "top": "zeroGradient",
        "symmetry": "symmetryPlane", "plate": "fixedValue", "frontAndBack": "empty",
    },
    "nut": {
        "inlet": "fixedValue", "outlet": "zeroGradient", "top": "zeroGradient",
        "symmetry": "symmetryPlane", "plate": "fixedValue", "frontAndBack": "empty",
    },
}


def patch_body(text: str, patch: str) -> str:
    match = re.search(rf"\b{re.escape(patch)}\s*\{{(?P<body>.*?)\}}", text, re.DOTALL)
    if not match:
        raise ValueError(f"Missing patch {patch}")
    return match["body"]


def patch_type(text: str, patch: str) -> str:
    type_match = re.search(r"\btype\s+(\w+)\s*;", patch_body(text, patch))
    if not type_match:
        raise ValueError(f"Patch {patch} has no type")
    return type_match.group(1)


def patch_uniform_scalar(text: str, patch: str) -> float:
    match = re.search(
        r"\bvalue\s+uniform\s+([-+0-9.eE]+)\s*;",
        patch_body(text, patch),
    )
    if not match:
        raise ValueError(f"Patch {patch} has no uniform scalar value")
    return float(match.group(1))


def audit(case: Path) -> dict:
    spec = json.loads((case / "benchmark-spec.json").read_text())
    checks = {}
    for field, expected_patches in EXPECTED.items():
        text = (case / "0" / field).read_text()
        checks[field] = {}
        for patch, expected in expected_patches.items():
            actual = patch_type(text, patch)
            checks[field][patch] = {
                "expected": expected,
                "actual": actual,
                "passed": actual == expected,
            }

    conditions = spec["conditions"]
    omega_wall = spec["omega_wall_treatment"]["fixed_value_s-1"]
    expected_values = {
        ("p", "outlet"): 0.0,
        ("k", "inlet"): float(conditions["k_m2_s2"]),
        ("k", "plate"): 0.0,
        ("omega", "inlet"): float(conditions["omega_s-1"]),
        ("omega", "plate"): float(omega_wall),
        ("nut", "inlet"): float(
            conditions.get(
                "freestream_nut_m2_s",
                conditions["freestream_nut_over_nu"]*conditions["nu_m2_s"],
            )
        ),
        ("nut", "plate"): 0.0,
    }
    value_checks = {}
    for (field, patch), expected in expected_values.items():
        actual = patch_uniform_scalar((case / "0" / field).read_text(), patch)
        tolerance = max(1e-14, abs(expected)*1e-9)
        value_checks[f"{field}:{patch}"] = {
            "expected": expected,
            "actual": actual,
            "passed": abs(actual - expected) <= tolerance,
        }

    manifest_variant = spec.get("boundary_conditions", {}).get("variant")
    manifest_passed = manifest_variant == "tmr-standard-sstm-flat-plate-table"
    fields_passed = all(
        item["passed"]
        for field in checks.values()
        for item in field.values()
    )
    values_passed = all(item["passed"] for item in value_checks.values())
    return {
        "published_source": (
            "https://tmbwg.github.io/turbmodels/Papers/ChangesToOpenFOAM.pdf"
        ),
        "manifest_variant": manifest_variant,
        "manifest_passed": manifest_passed,
        "checks": checks,
        "value_checks": value_checks,
        "published_boundary_screen": bool(
            manifest_passed and fields_passed and values_passed
        ),
        "accepted_for_rocket": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = audit(args.case)
    (args.output / "flat-plate-boundary-audit.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
