import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from study_d12_nose_lengths import (
    NOSE_LENGTHS_MM,
    STOCK_PORTA_PAD_GUIDE_LENGTH_M,
    variant,
)


def test_nose_screen_includes_sub_50_lengths():
    assert NOSE_LENGTHS_MM == (30, 35, 40, 45, 50)


def test_shorter_nose_preserves_shoulder_relative_stations():
    baseline = variant(50)
    shortened = variant(30)

    assert shortened.geometry.mm("nose_length") == 30
    assert shortened.payload.cg_x.value - baseline.payload.cg_x.value == pytest.approx(-20)
    for role in ("body", "mount", "chute", "harness", "lugs", "bay_hardware"):
        assert shortened.mass_item(role).x.value - baseline.mass_item(role).x.value == pytest.approx(-20)


@pytest.mark.parametrize("nose_length_mm", NOSE_LENGTHS_MM)
def test_nose_variants_retain_current_d12_configuration(nose_length_mm):
    config = variant(nose_length_mm)

    assert config.nose_shape == "conical"
    assert config.geometry.mm("body_length") == 500
    assert config.bay_retention == "m2-insert-trial-v1"
    assert [(motor.designation, motor.delay_s) for motor in config.motors] == [("D12", 5)]
    assert [wind.value for wind in config.launch.wind_speeds] == [0, 2, 4]
    assert config.launch.guide_length.value == pytest.approx(
        STOCK_PORTA_PAD_GUIDE_LENGTH_M
    )
