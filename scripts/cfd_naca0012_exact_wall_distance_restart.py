"""Create the predeclared exact-wall-distance SSTm same-grid restart."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

from cfd_naca0012_sstm_limiter_restart import restart


METHOD = "same-grid exact-SSTm exact-wall-distance sensitivity restart"
IMAGE_ID = "sha256:ae3235d75b54311a6dbcdfc2b45f6c9be77a8ff0743c099cf5ca3f3e9db0d23f"
LIBS = (
    'libs ("libTmrSSTmCompressible.so" '
    '"libTmrSSTmKOnlyLimiterCompressible.so" '
    '"libTmrSSTmExactProductionCompressible.so" '
    '"libSutherlandPrTransport.so");'
)


def sha256(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


def construct(
    source: Path,
    source_audit: Path,
    target: Path,
    plan_path: Path,
) -> dict:
    plan_path = plan_path.resolve(strict=True)
    plan = json.loads(plan_path.read_text())
    if not plan.get("declared_before_candidate_execution"):
        raise ValueError("Wall-distance sensitivity was not predeclared")
    iterations = plan["candidate"]["iterations"]
    result = restart(
        source,
        source_audit,
        target,
        iterations,
        method=METHOD,
        image_id=IMAGE_ID,
        source_runtime_model="TmrSSTmExactProduction",
        source_runtime_library="libTmrSSTmExactProductionCompressible.so",
        source_libs=LIBS,
        target_runtime_model="TmrSSTmExactProduction",
        target_runtime_library="libTmrSSTmExactProductionCompressible.so",
        target_libs=LIBS,
        target_variant="tmr-sstm-exact-production-exact-wall-distance",
        record_name="exact-wall-distance-restart-execution.json",
        source_transport_model="exact-sutherland-pr072",
        source_end_time=1500,
    )
    target = target.resolve(strict=True)
    schemes_path = target / "system" / "fvSchemes"
    schemes = schemes_path.read_text()
    pattern = r"\bwallDist\s*\{\s*method\s+meshWave\s*;\s*\}"
    if len(re.findall(pattern, schemes)) != 1:
        raise ValueError("Expected exactly one meshWave wall-distance dictionary")
    schemes_path.write_text(
        re.sub(pattern, "wallDist { method exactDistance; }", schemes, count=1)
    )

    control_path = target / "system" / "controlDict"
    control = control_path.read_text()
    if control.count(LIBS) != 1:
        raise ValueError("Expected exact-production runtime library list once")
    exact_distance_libs = LIBS.replace(
        '"libSutherlandPrTransport.so"',
        '"libSutherlandPrTransport.so" "libscotchDecomp.so"',
    )
    control_path.write_text(control.replace(LIBS, exact_distance_libs, 1))

    snapshot = target / "provenance" / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    result["predeclared_plan"] = {
        "path": str(plan_path),
        "sha256": sha256(plan_path),
    }
    correction_path = plan_path.with_name(
        "naca0012-exact-wall-distance-runtime-name-correction.json"
    ).resolve(strict=True)
    correction = json.loads(correction_path.read_text())
    if not correction.get("declared_before_corrected_candidate_execution"):
        raise ValueError("Runtime-name correction was not predeclared")
    if correction["scientific_plan"]["sha256"] != sha256(plan_path):
        raise ValueError("Runtime-name correction does not match scientific plan")
    result["runtime_name_correction"] = {
        "path": str(correction_path),
        "sha256": sha256(correction_path),
    }
    parallel_correction_path = plan_path.with_name(
        "naca0012-exact-wall-distance-parallel-plugin-correction.json"
    ).resolve(strict=True)
    parallel_correction = json.loads(parallel_correction_path.read_text())
    if not parallel_correction.get("declared_before_corrected_candidate_execution"):
        raise ValueError("Parallel-plugin correction was not predeclared")
    if parallel_correction["scientific_plan"]["sha256"] != sha256(plan_path):
        raise ValueError("Parallel-plugin correction does not match scientific plan")
    result["parallel_plugin_correction"] = {
        "path": str(parallel_correction_path),
        "sha256": sha256(parallel_correction_path),
        "loaded_library": "libscotchDecomp.so",
        "controlDict_sha256": sha256(control_path),
    }
    redistribution_path = plan_path.with_name(
        "naca0012-exact-wall-distance-runtime-redistribution-correction.json"
    ).resolve(strict=True)
    redistribution = json.loads(redistribution_path.read_text())
    if not redistribution.get("declared_before_corrected_candidate_execution"):
        raise ValueError("Runtime-redistribution correction was not predeclared")
    if redistribution["scientific_plan"]["sha256"] != sha256(plan_path):
        raise ValueError("Runtime-redistribution correction does not match plan")
    result["runtime_redistribution_correction"] = {
        "path": str(redistribution_path),
        "sha256": sha256(redistribution_path),
        "volume_decomposition": "scotch",
        "exactDistance_surface_decomposition": "simple",
    }
    simple_coeffs_path = plan_path.with_name(
        "naca0012-exact-wall-distance-simple-coeffs-correction.json"
    ).resolve(strict=True)
    simple_coeffs = json.loads(simple_coeffs_path.read_text())
    if not simple_coeffs.get("declared_before_corrected_candidate_execution"):
        raise ValueError("Simple-coeffs correction was not predeclared")
    if simple_coeffs["scientific_plan"]["sha256"] != sha256(plan_path):
        raise ValueError("Simple-coeffs correction does not match plan")
    result["simple_coeffs_correction"] = {
        "path": str(simple_coeffs_path),
        "sha256": sha256(simple_coeffs_path),
        "n": [12, 1, 1],
        "delta": 0.001,
    }
    result["single_change"] = {
        "from": "meshWave",
        "to": "exactDistance",
        "fvSchemes_sha256": sha256(schemes_path),
    }
    result["wrapper_snapshot"] = str(snapshot)
    result["wrapper_sha256"] = sha256(snapshot)
    record_path = target / "exact-wall-distance-restart-execution.json"
    record_path.write_text(json.dumps(result, indent=2) + "\n")

    spec_path = target / "benchmark-spec.json"
    spec = json.loads(spec_path.read_text())
    spec["model_mapping"]["variant"] = (
        "tmr-sstm-exact-production-exact-wall-distance"
    )
    spec["wall_distance_sensitivity"] = {
        "method": "exactDistance",
        "predeclared_plan": result["predeclared_plan"],
        "runtime_name_correction": result["runtime_name_correction"],
        "parallel_plugin_correction": result["parallel_plugin_correction"],
        "runtime_redistribution_correction": result[
            "runtime_redistribution_correction"
        ],
        "simple_coeffs_correction": result["simple_coeffs_correction"],
        "restart_record": str(record_path),
        "restart_record_sha256": sha256(record_path),
    }
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    args = parser.parse_args()
    print(
        json.dumps(
            construct(args.source, args.source_audit, args.target, args.plan), indent=2
        )
    )


if __name__ == "__main__":
    main()
