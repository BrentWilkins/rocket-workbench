import math
from pathlib import Path

import pytest

from rocket_workbench.config import Config, load_config
from rocket_workbench.nose import radius_at, solid

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize('shape', ['conical', 'ogive', 'ellipsoid'])
def test_profile_endpoints_and_monotonicity(shape):
    values = [radius_at(shape, x, 70, 20.8) for x in range(71)]
    assert values[0] == pytest.approx(0)
    assert values[-1] == pytest.approx(20.8)
    assert all(a <= b for a, b in zip(values, values[1:]))


@pytest.mark.integration
@pytest.mark.parametrize('shape', ['ogive', 'ellipsoid'])
def test_curved_nose_solid_and_volume(shape):
    from rocket_workbench.cad import shapes
    for length in [50, 70, 90]:
        outer = solid(shape, length, 20.8)
        assert outer.val().isValid()
        assert len(outer.solids().vals()) == 1
        # Independent numeric integration of analytic cross-sections.
        count = 10000
        expected = sum(math.pi*radius_at(shape, (i+.5)*length/count, length, 20.8)**2
                       * length/count for i in range(count))
        assert outer.val().Volume() == pytest.approx(expected, rel=1e-4)
        data = load_config(ROOT/'examples/candidate-recovery.yaml').model_dump()
        data['nose_shape'] = shape
        data['geometry']['nose_length']['value'] = length
        nose = shapes(Config.model_validate(data))['nose-bay']
        assert nose.val().isValid()
        assert len(nose.solids().vals()) == 1
