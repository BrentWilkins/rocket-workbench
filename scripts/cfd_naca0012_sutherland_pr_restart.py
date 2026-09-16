"""Create a same-grid NACA restart with exact Sutherland viscosity and Pr=0.72."""

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from cfd_naca0012_map_fields import FIELDS, latest_time


METHOD = "same-grid exact-Sutherland constant-Prandtl sensitivity restart"
MOLECULAR_PRANDTL = 0.72
IMAGE_ID = "sha256:2870176815d77d1b6e252003db8f7598f2bb25e891c7ea97ec459e469b54d020"


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
) -> dict:
    source = source.resolve(strict=True)
    source_audit = source_audit.resolve(strict=True)
    target = target.resolve()
    if target.exists():
        raise FileExistsError(target)
    if iterations < 500:
        raise ValueError("At least 500 iterations are required for the trend gate")

    source_spec_path = source / "benchmark-spec.json"
    source_spec = json.loads(source_spec_path.read_text())
    audit = json.loads(source_audit.read_text())
    execution = json.loads((source / "execution.json").read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source execution did not pass")
    if (
        Path(audit.get("case", "")).resolve() != source
        or not audit.get("coarse_preflight_passed")
        or not audit.get("solver_residual_gate")
        or not audit.get("long_window_trend_gate")
    ):
        raise ValueError("Source force audit did not pass")
    conditions = source_spec.get("conditions", {})
    if conditions.get("transport_model") != "sutherland":
        raise ValueError("Source must use built-in Sutherland transport")

    target.mkdir(parents=True)
    shutil.copytree(source / "constant", target / "constant")
    shutil.copytree(source / "system", target / "system")
    shutil.copyfile(source / "tmr-naca0012-grid.npz", target / "tmr-naca0012-grid.npz")

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

    thermo_path = target / "constant" / "thermophysicalProperties"
    thermo = thermo_path.read_text()
    thermo = replace_once(thermo, "transport sutherland;", "transport sutherlandPr;")
    thermo = replace_once(thermo, " Ts 110.4;", " Ts 110.4;\n Pr 0.72;")
    thermo_path.write_text(thermo)

    control_path = target / "system" / "controlDict"
    control = control_path.read_text()
    control = replace_once(
        control,
        'libs ("libTmrSSTmCompressible.so");',
        'libs ("libTmrSSTmCompressible.so" "libSutherlandPrTransport.so");',
    )
    control = replace_once(control, "endTime 6000;", f"endTime {iterations};")
    control_path.write_text(control)

    provenance = target / "provenance"
    provenance.mkdir()
    implementation_snapshot = provenance / Path(__file__).name
    shutil.copyfile(Path(__file__), implementation_snapshot)
    implementation_sha256 = sha256(implementation_snapshot)
    initialization = {
        "method": METHOD,
        "stage_passed": True,
        "source_case": str(source),
        "source_time": float(source_time.name),
        "source_audit": str(source_audit),
        "source_audit_sha256": sha256(source_audit),
        "implementation_snapshot": str(implementation_snapshot),
        "implementation_sha256": implementation_sha256,
        "fields": fields,
    }

    spec = dict(source_spec)
    spec["iterations"] = iterations
    spec["model_mapping"] = dict(source_spec["model_mapping"])
    spec["model_mapping"]["image_id"] = IMAGE_ID
    spec["conditions"] = dict(conditions)
    spec["conditions"].update(
        {
            "transport_model": "exact-sutherland-pr072",
            "openfoam_transport_model": "sutherlandPr",
            "molecular_prandtl": MOLECULAR_PRANDTL,
        }
    )
    spec["transport_mapping"] = {
        "method": METHOD,
        "viscosity": "exact OpenFOAM v2512 Sutherland formula and source As/Ts",
        "thermal_conductivity_relation": "kappa(T) = Cp * mu(T) / Pr",
        "molecular_prandtl": MOLECULAR_PRANDTL,
        "unchanged_thermo_combination": (
            "hePsiThermo pureMixture hConst perfectGas sensibleInternalEnergy"
        ),
        "runtime_library": "libSutherlandPrTransport.so",
        "image_id": IMAGE_ID,
    }
    spec["initialization"] = initialization
    spec_path = target / "benchmark-spec.json"
    spec_path.write_text(json.dumps(spec, indent=2) + "\n")

    record = {
        "stage": METHOD,
        **initialization,
        "target_case": str(target),
        "target_case_spec_sha256": sha256(spec_path),
        "target_thermophysical_properties_sha256": sha256(thermo_path),
    }
    (target / "sutherland-pr-restart-execution.json").write_text(
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
