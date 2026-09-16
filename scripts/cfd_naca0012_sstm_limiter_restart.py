"""Create the predeclared same-grid SSTm k-only limiter sensitivity restart."""

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

from cfd_naca0012_map_fields import FIELDS, latest_time


METHOD = "same-grid SSTm k-only production-limiter sensitivity restart"
IMAGE_ID = "sha256:777e5ff0348eab1026f69bfe7fd2a01685d250a6a186a674a9bdc0e83ff7ef8b"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one occurrence of {old!r}")
    return text.replace(old, new)


def restart(
    source: Path,
    source_audit: Path,
    target: Path,
    iterations: int,
    *,
    method: str = METHOD,
    image_id: str = IMAGE_ID,
    source_runtime_model: str = "TmrSSTm",
    source_runtime_library: str = "libTmrSSTmCompressible.so",
    source_libs: str = (
        'libs ("libTmrSSTmCompressible.so" "libSutherlandPrTransport.so");'
    ),
    target_runtime_model: str = "TmrSSTmKOnlyLimiter",
    target_runtime_library: str = "libTmrSSTmKOnlyLimiterCompressible.so",
    target_libs: str = (
        'libs ("libTmrSSTmCompressible.so" '
        '"libTmrSSTmKOnlyLimiterCompressible.so" '
        '"libSutherlandPrTransport.so");'
    ),
    target_variant: str = "tmr-sstm-k-only-production-limiter",
    record_name: str = "sstm-limiter-restart-execution.json",
    allow_source_residual_only_failure: bool = False,
    source_transport_model: str = "exact-sutherland-pr072",
    convert_to_exact_sutherland_pr072: bool = False,
    source_end_time: int = 1500,
    target_convection_scheme: str | None = None,
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)
    if iterations < 500:
        raise ValueError("At least 500 iterations are required for the trend gate")

    source_spec = json.loads((source / "benchmark-spec.json").read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not pass")
    if Path(audit.get("case", "")).resolve() != source:
        raise ValueError("Source force audit does not match source case")
    source_passed = bool(audit.get("coarse_preflight_passed"))
    if not source_passed and allow_source_residual_only_failure:
        residuals = audit.get("solver_initial_residuals_last_100_max", {})
        source_passed = bool(
            audit.get("settling_gate")
            and audit.get("temperature_limiter_inactive_over_window")
            and audit.get("zero_angle_symmetry_gate")
            and residuals
            and max(float(value) for value in residuals.values()) <= 2e-5
        )
    if not source_passed:
        raise ValueError("Source force audit did not pass continuation eligibility")

    conditions = source_spec.get("conditions", {})
    model = source_spec.get("model_mapping", {})
    if conditions.get("transport_model") != source_transport_model:
        raise ValueError("Source transport does not match the declared restart")
    if model.get("runtime_library") != source_runtime_library:
        raise ValueError("Source runtime library does not match the declared restart")

    target.mkdir(parents=True)
    shutil.copytree(source / "constant", target / "constant")
    shutil.copytree(source / "system", target / "system")
    shutil.copyfile(source / "tmr-naca0012-grid.npz", target / "tmr-naca0012-grid.npz")

    if target_convection_scheme is not None:
        if target_convection_scheme != "lust-blended":
            raise ValueError("Only the predeclared LUST transform is supported")
        schemes_path = target / "system" / "fvSchemes"
        schemes = schemes_path.read_text()
        schemes = replace_once(
            schemes,
            "div(phi,U) bounded Gauss linearUpwind grad(U);",
            "div(phi,U) bounded Gauss LUST grad(U);",
        )
        schemes = replace_once(
            schemes,
            "energy bounded Gauss linearUpwind default;",
            "energy bounded Gauss LUST default;",
        )
        schemes_path.write_text(schemes)

        solution_path = target / "system" / "fvSolution"
        solution = solution_path.read_text()
        relaxation_replacements = {
            "p 0.2;": "p 0.1;",
            "rho 0.01;": "rho 0.005;",
            "U 0.1;": "U 0.05;",
            "e 0.1;": "e 0.05;",
            '"(k|omega)" 0.3;': '"(k|omega)" 0.15;',
        }
        for old, new in relaxation_replacements.items():
            solution = replace_once(solution, old, new)
        solution_path.write_text(solution)

    if convert_to_exact_sutherland_pr072:
        thermo_path = target / "constant" / "thermophysicalProperties"
        thermo = thermo_path.read_text()
        thermo = replace_once(thermo, "transport sutherland;", "transport sutherlandPr;")
        ts_pattern = r"(?m)^(\s*)Ts\s+110\.4;$"
        if len(re.findall(ts_pattern, thermo)) != 1:
            raise ValueError("Expected one Sutherland Ts 110.4 entry")
        thermo = re.sub(ts_pattern, r"\1Ts 110.4;\n\1Pr 0.72;", thermo)
        thermo_path.write_text(thermo)

    source_time = latest_time(source)
    initial = target / "0"
    initial.mkdir()
    fields = {}
    for name in FIELDS:
        source_field = source_time / name
        target_field = initial / name
        shutil.copyfile(source_field, target_field)
        fields[name] = {
            "source_sha256": sha256(source_field),
            "restart_sha256": sha256(target_field),
        }

    control_path = target / "system" / "controlDict"
    control = control_path.read_text()
    control = replace_once(
        control,
        source_libs,
        target_libs,
    )
    end_time_pattern = rf"endTime\s+{source_end_time};"
    if len(re.findall(end_time_pattern, control)) != 1:
        raise ValueError(f"Expected one source endTime {source_end_time}")
    control = re.sub(end_time_pattern, f"endTime {iterations};", control)
    control_path.write_text(control)

    turbulence_path = target / "constant" / "turbulenceProperties"
    turbulence = turbulence_path.read_text()
    turbulence = replace_once(
        turbulence,
        f"RASModel {source_runtime_model};",
        f"RASModel {target_runtime_model};",
    )
    turbulence_path.write_text(turbulence)

    provenance = target / "provenance"
    provenance.mkdir()
    snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), snapshot)
    record = {
        "method": method,
        "stage": method,
        "stage_passed": True,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(snapshot),
        "implementation_sha256": sha256(snapshot),
        "image_id": image_id,
        "fields": fields,
    }
    if target_convection_scheme is not None:
        record["source_convection_scheme"] = source_spec["convection_scheme"]
        record["target_convection_scheme"] = target_convection_scheme
        record["relaxation_scale_from_source"] = 0.5

    spec = dict(source_spec)
    spec["iterations"] = iterations
    if target_convection_scheme is not None:
        spec["convection_scheme"] = target_convection_scheme
    spec["conditions"] = dict(conditions)
    if convert_to_exact_sutherland_pr072:
        spec["conditions"].update(
            {
                "transport_model": "exact-sutherland-pr072",
                "openfoam_transport_model": "sutherlandPr",
                "molecular_prandtl": 0.72,
            }
        )
        spec["transport_mapping"] = {
            "method": method,
            "viscosity": "exact OpenFOAM v2512 Sutherland formula source As/Ts",
            "thermal_conductivity_relation": "kappa(T) = Cp * mu(T) / Pr",
            "molecular_prandtl": 0.72,
            "runtime_library": "libSutherlandPrTransport.so",
            "image_id": image_id,
        }
    spec["model_mapping"] = dict(model)
    spec["model_mapping"].update(
        {
            "variant": target_variant,
            "runtime_model": target_runtime_model,
            "runtime_library": target_runtime_library,
            "base_runtime_library": source_runtime_library,
            "image_id": image_id,
            "omega_production": "unlimited G/nut",
            "k_production": "min(G, 20 betaStar omega k)",
        }
    )
    spec["initialization"] = record
    (target / "benchmark-spec.json").write_text(json.dumps(spec, indent=2) + "\n")
    (target / record_name).write_text(
        json.dumps(record, indent=2) + "\n"
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--source-audit", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--iterations", type=int, default=1500)
    args = parser.parse_args()
    print(json.dumps(restart(args.source, args.source_audit, args.target, args.iterations)))


if __name__ == "__main__":
    main()
