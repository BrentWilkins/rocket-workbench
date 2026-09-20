import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from rocket_workbench.flight_model import generate
from study_payload_grid import candidate, mass_records
from study_stabilization import augment_model, surface_geometry


def test_four_fin_cad_and_native_model_agree(tmp_path):
    three = candidate(500, 50, 53.65384615384615, "conical", "D12")
    four = candidate(500, 50, 53.65384615384615, "conical", "D12", fin_count=4)
    assert three.fin_count == 3
    assert four.fin_count == 4
    assert four.printed_measurements["fin-collar"][0].value > three.printed_measurements["fin-collar"][0].value
    parts = mass_records(four)
    path = tmp_path / "four.ork"
    generate(four, parts, "actual", path)
    assert ET.parse(path).findtext(".//freeformfinset/fincount") == "4"
    assert parts["fin-collar"]["mass_g"] == four.printed_measurements["fin-collar"][0].value
    with pytest.raises(ValueError, match="three fins"):
        candidate(500, 50, 53.65384615384615, "conical", "D12", fin_count=4, upper=True)


def test_surface_and_mass_control_have_identical_mass_and_cg(tmp_path):
    config = candidate(500, 50, 53.65384615384615, "conical", "E12")
    parts = mass_records(config)
    surface_path, control_path = tmp_path / "surface.ork", tmp_path / "control.ork"
    for path in (surface_path, control_path):
        generate(config, parts, "actual", path)
    surface = augment_model(surface_path, config, "guard", 5)
    control = augment_model(control_path, config, "guard-mass-only", 5)
    assert surface["added_mass_g"] == control["added_mass_g"]
    assert surface["added_mass_cg_mm"] == control["added_mass_cg_mm"]
    assert ET.parse(surface_path).findtext(".//trapezoidfinset/fincount") == "1"
    assert ET.parse(control_path).find(".//trapezoidfinset") is None
    geometry = surface_geometry("guard", 5, 1.24)
    assert geometry["mass_g"] == pytest.approx(0.6116)
    assert geometry["cg_from_root_mm"] == pytest.approx(10)
