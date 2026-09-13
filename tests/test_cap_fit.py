import itertools
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from study_cap_fit import trial_hardware
from study_fin_recovery import configuration
from rocket_workbench.avionics import fit_report
from rocket_workbench.cad import shapes

pytestmark = pytest.mark.integration


def test_insert_layout_requires_routing_revision():
    config = configuration(20, 430)
    parts = shapes(config, cap_insert_angles=[10, 170, 270])
    original = trial_hardware(config)
    revised = trial_hardware(config, True)
    assert not fit_report(config, parts, hardware=original)['passed']
    assert fit_report(config, parts, hardware=revised)['passed']
    for name in original:
        assert revised[name].val().Volume() == pytest.approx(original[name].val().Volume())
        assert revised[name].val().Center().z == pytest.approx(original[name].val().Center().z)
    for first, second in itertools.combinations(revised.values(), 2):
        assert first.intersect(second).val().Volume() < 1e-5
    assert all(part.val().isValid() and len(part.solids().vals()) == 1 for part in parts.values())


def test_default_geometry_retains_pilot_mass():
    config = configuration(20, 430)
    default = shapes(config)
    explicit = shapes(config, cap_insert_angles=None)
    assert {key: p.val().Volume() for key,p in default.items()} == pytest.approx(
        {key: p.val().Volume() for key,p in explicit.items()})
