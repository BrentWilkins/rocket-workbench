from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from rocket_workbench.aero_export import export_aero_study


def _project(root: Path, designation: str, delay: int, thrust: float) -> Path:
    root.mkdir()
    measurements = {
        "body_od": 41.6,
        "body_length": 530.0,
        "nose_length": 40.0,
        "fin_root": 65.0,
        "fin_tip": 28.0,
        "fin_span": 53.65,
        "fin_sweep": 25.0,
        "fin_thickness": 1.6,
        "motor_overhang": 3.2,
    }
    config = {
        "name": "current-design",
        "geometry": {key: {"value": value} for key, value in measurements.items()},
        "nose_shape": "ogive",
        "fin_shape": "clipped-delta",
        "fin_count": 3,
    }
    motor = {
        "manufacturer": "Estes",
        "designation": designation,
        "delay_s": delay,
        "length_mm": 70 if designation == "D12" else 95,
        "loaded_mass_g": 42.6 if designation == "D12" else 59.2,
        "spent_mass_g": 21.5 if designation == "D12" else 24.0,
        "source": "test motor record",
        "time_s": [0.0, 0.1, 1.0],
        "thrust_n": [0.0, thrust, 0.0],
    }
    (root / "nominal.json").write_text(json.dumps(config))
    (root / "ledger.json").write_text(
        json.dumps({"dry_mass_g": 179.2, "dry_cg_x_mm": 268.7})
    )
    (root / "motor.json").write_text(json.dumps(motor))
    return root


def test_export_aero_study_preserves_vehicle_and_motor_set(tmp_path: Path) -> None:
    d12 = _project(tmp_path / "d12", "D12", 5, 24.0)
    e12 = _project(tmp_path / "e12", "E12", 6, 28.0)
    output = tmp_path / "bundle"

    manifest = export_aero_study(
        [d12, e12],
        output,
        payload_mass_kg=0.02065,
        payload_position_mm=92.95,
        launch_guide_m=1.374,
        min_guide_exit_m_s=12.0,
    )
    study = json.loads((output / "study.json").read_text())

    assert study["source_project"] == "rocket-workbench"
    assert study["body"]["radius_m"] == pytest.approx(0.0208)
    assert study["body"]["length_m"] == pytest.approx(0.570)
    assert study["baseline_fins"]["root_chord_m"] == pytest.approx(0.065)
    assert [case["name"] for case in study["mission"]["motor_cases"]] == [
        "Estes D12-5",
        "Estes E12-6",
    ]
    assert study["mission"]["payload_mass_bounds_kg"] == [0.02065, 0.02065]
    assert set(manifest["motor_curves"]) == {
        "estes-d12-5.eng",
        "estes-e12-6.eng",
    }
    assert manifest["study_sha256"] == hashlib.sha256(
        (output / "study.json").read_bytes()
    ).hexdigest()


def test_export_refuses_mixed_vehicle_geometry(tmp_path: Path) -> None:
    d12 = _project(tmp_path / "d12", "D12", 5, 24.0)
    e12 = _project(tmp_path / "e12", "E12", 6, 28.0)
    config_path = e12 / "nominal.json"
    config = json.loads(config_path.read_text())
    config["geometry"]["body_length"]["value"] = 500.0
    config_path.write_text(json.dumps(config))

    with pytest.raises(ValueError, match="same vehicle geometry"):
        export_aero_study(
            [d12, e12],
            tmp_path / "bundle",
            payload_mass_kg=0.02,
            payload_position_mm=90.0,
            launch_guide_m=1.0,
            min_guide_exit_m_s=12.0,
        )
