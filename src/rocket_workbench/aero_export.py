"""Portable Rocket Workbench to Rocket Aero Design Lab project adapter."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ADAPTER_VERSION = "rocket-workbench-aero-study-v1"
GEOMETRY_KEYS = (
    "body_od",
    "body_length",
    "nose_length",
    "fin_root",
    "fin_tip",
    "fin_span",
    "fin_sweep",
    "fin_thickness",
)


def _read(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _measurement(config: dict[str, Any], name: str) -> float:
    value = config["geometry"][name]
    return float(value["value"] if isinstance(value, dict) else value)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _content_hash(value: Any) -> str:
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _load_project(directory: Path) -> dict[str, Any]:
    directory = directory.resolve()
    paths = {
        "config": directory / "nominal.json",
        "ledger": directory / "ledger.json",
        "motor": directory / "motor.json",
    }
    for path in paths.values():
        if not path.is_file():
            raise ValueError(f"Rocket Workbench project is incomplete: {path}")
    return {
        "directory": directory,
        "paths": paths,
        **{name: _read(path) for name, path in paths.items()},
    }


def export_aero_study(
    project_dirs: list[Path],
    output_dir: Path,
    *,
    payload_mass_kg: float,
    payload_position_mm: float,
    launch_guide_m: float,
    min_guide_exit_m_s: float,
) -> dict[str, Any]:
    """Export one vehicle and one or more real motor cases as a portable study."""
    if not project_dirs:
        raise ValueError("at least one Rocket Workbench project directory is required")
    if payload_mass_kg < 0 or payload_position_mm <= 0:
        raise ValueError("payload mass and position must be physical values")
    if output_dir.exists():
        raise ValueError(f"output directory already exists: {output_dir}")
    records = [_load_project(path) for path in project_dirs]
    reference = records[0]["config"]
    geometry = {key: _measurement(reference, key) for key in GEOMETRY_KEYS}
    shape = (
        reference.get("nose_shape"),
        reference.get("fin_shape"),
        reference.get("fin_count", 3),
    )
    for record in records[1:]:
        other = {key: _measurement(record["config"], key) for key in GEOMETRY_KEYS}
        other_shape = (
            record["config"].get("nose_shape"),
            record["config"].get("fin_shape"),
            record["config"].get("fin_count", 3),
        )
        if other != geometry or other_shape != shape:
            raise ValueError("all motor projects must describe the same vehicle geometry")

    output_dir.mkdir(parents=True)
    motor_dir = output_dir / "motors"
    motor_dir.mkdir()
    radius_m = geometry["body_od"] / 2000
    cylinder_m = geometry["body_length"] / 1000
    nose_m = geometry["nose_length"] / 1000
    overall_m = cylinder_m + nose_m
    baseline = min(records, key=lambda item: item["ledger"]["dry_mass_g"])
    dry_mass_kg = float(baseline["ledger"]["dry_mass_g"]) / 1000
    dry_cg_m = float(baseline["ledger"]["dry_cg_x_mm"]) / 1000
    pitch_inertia = dry_mass_kg * (3 * radius_m**2 + overall_m**2) / 12
    roll_inertia = dry_mass_kg * radius_m**2 / 2

    motor_cases: list[dict[str, Any]] = []
    source_paths: list[Path] = []
    for record in records:
        motor = record["motor"]
        designation = str(motor["designation"])
        delay = float(motor["delay_s"])
        label = f"{motor.get('manufacturer', '').strip()} {designation}-{delay:g}".strip()
        curve_path = motor_dir / f"{_slug(label)}.eng"
        times, thrust = motor["time_s"], motor["thrust_n"]
        if len(times) != len(thrust) or len(times) < 2:
            raise ValueError(f"invalid motor curve in {record['paths']['motor']}")
        curve_path.write_text(
            "\n".join(
                f"{float(time):.12g} {float(force):.12g}"
                for time, force in zip(times, thrust)
            )
            + "\n"
        )
        dry_delta = (
            float(record["ledger"]["dry_mass_g"])
            - float(baseline["ledger"]["dry_mass_g"])
        ) / 1000
        motor_length_m = float(motor["length_mm"]) / 1000
        overhang_m = _measurement(record["config"], "motor_overhang") / 1000
        motor_cases.append(
            {
                "schema_version": "1.0",
                "name": label,
                "motor_file": f"motors/{curve_path.name}",
                "motor_wet_mass_kg": float(motor["loaded_mass_g"]) / 1000
                + dry_delta,
                "motor_dry_mass_kg": float(motor["spent_mass_g"]) / 1000
                + dry_delta,
                "motor_cg_m": overall_m + overhang_m - motor_length_m / 2,
                "source": str(motor["source"]),
            }
        )
        source_paths.extend(record["paths"].values())

    nose_shape = str(reference.get("nose_shape", "ogive"))
    supported_noses = {"conical", "ogive", "tangent-ogive", "elliptical"}
    if nose_shape not in supported_noses:
        raise ValueError(f"unsupported Aero Lab nose mapping: {nose_shape}")
    fin_count = int(reference.get("fin_count", 3))
    root_m = geometry["fin_root"] / 1000
    span_m = geometry["fin_span"] / 1000
    study = {
        "schema_version": "1.0",
        "name": f"{reference.get('name', 'Rocket Workbench vehicle')} motor-set study",
        "mode": "mission",
        "source_project": "rocket-workbench",
        "source_label": f"Imported by {ADAPTER_VERSION}",
        "source_notes": [
            "Geometry, nominal dry mass and CG are copied from Rocket Workbench evidence.",
            "Inertia uses an explicit uniform-cylinder approximation; measure before flight.",
            "Motor-specific spacer mass differences are folded into each motor case.",
        ],
        "planned_motor_names": [case["name"] for case in motor_cases],
        "target_payload_mass_kg": payload_mass_kg,
        "body": {
            "schema_version": "1.0",
            "radius_m": radius_m,
            "length_m": overall_m,
            "dry_mass_kg": dry_mass_kg,
            "cg_m": dry_cg_m,
            "inertia_kg_m2": [pitch_inertia, pitch_inertia, roll_inertia],
        },
        "baseline_nose": {
            "schema_version": "1.0",
            "family": nose_shape,
            "length_m": nose_m,
            "base_radius_m": radius_m,
            "bluffness": 0.0,
            "power_exponent": None,
        },
        "baseline_fins": {
            "schema_version": "1.0",
            "family": "trapezoidal",
            "count": fin_count,
            "root_chord_m": root_m,
            "tip_chord_m": geometry["fin_tip"] / 1000,
            "span_m": span_m,
            "sweep_m": geometry["fin_sweep"] / 1000,
            "thickness_m": geometry["fin_thickness"] / 1000,
            "axial_position_m": overall_m - root_m,
            "cant_rad": 0.0,
            "boundary": None,
            "experimental_notch": False,
        },
        "baseline_tail": None,
        "nose_families": [nose_shape],
        "fin_families": ["trapezoidal"],
        "fin_presets": ["custom", "clipped-delta", "swept"],
        "fin_counts": sorted({3, 4, fin_count}),
        "nose_length_bounds_m": [nose_m, nose_m],
        "fin_span_bounds_m": [span_m * 0.85, span_m * 1.15],
        "tail_length_bounds_m": [0.0, 0.0],
        "motor_file": None,
        "mission": {
            "schema_version": "1.0",
            "motor_wet_mass_kg": None,
            "motor_dry_mass_kg": None,
            "motor_cg_m": None,
            "motor_cases": motor_cases,
            "payload_mass_bounds_kg": [payload_mass_kg, payload_mass_kg],
            "payload_position_m": payload_position_mm / 1000,
            "launch_guide_length_m": launch_guide_m,
            "min_guide_exit_speed_m_s": min_guide_exit_m_s,
            "min_apogee_m": 0.0,
            "integration_step_s": 0.01,
            "max_time_s": 180.0,
        },
    }
    study_path = output_dir / "study.json"
    study_path.write_text(json.dumps(study, indent=2, allow_nan=False) + "\n")
    manifest = {
        "schema_version": "1.0",
        "kind": "rocket-workbench-aero-study",
        "adapter_version": ADAPTER_VERSION,
        "study": study_path.name,
        "study_sha256": _sha256(study_path),
        "study_content_hash": _content_hash(study),
        "motor_curves": {
            path.name: _sha256(path) for path in sorted(motor_dir.iterdir())
        },
        "source_files": {str(path): _sha256(path) for path in source_paths},
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, allow_nan=False) + "\n"
    )
    return manifest
