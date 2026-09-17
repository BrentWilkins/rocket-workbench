import math
import sys
from pathlib import Path

import pytest

from rocket_workbench.fins import outline, area_mm2

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from study_fin_shapes import variant, SHAPES


def test_organic_profile_is_limited_to_clipped_delta():
    config = variant('elliptical', 45, 430)
    data = config.model_dump()
    data['fin_profile'] = 'organic-v2'
    with pytest.raises(ValueError, match='Organic fin profile'):
        type(config).model_validate(data)


def test_organic_fin_collar_is_single_valid_solid():
    import cadquery as cq

    from rocket_workbench.cad import shapes

    config = variant('clipped-delta', 45, 430)
    data = config.model_dump()
    data['fin_profile'] = 'organic-v2'
    data['geometry']['fin_thickness']['value'] = 2.0
    organic = type(config).model_validate(data)
    part = shapes(organic)['fin-collar']
    assert part.val().isValid()
    assert len(part.solids().vals()) == 1

    g = organic.geometry
    collar_outer = g.mm('body_od') / 2 + g.mm('clearance') + g.mm('wall')
    collar_start = g.mm('nose_length') + g.mm('body_length') - g.mm('collar_length')
    root_mid = collar_start + g.mm('fin_root') / 2
    # Material immediately outside the cylindrical collar must connect into
    # the cove. This point was empty in the rejected tangent-plane geometry.
    y = 3.0
    radius = collar_outer + .01
    x = math.sqrt(radius ** 2 - y ** 2)
    assert part.val().isInside(cq.Vector(x, y, root_mid), 1e-6)


@pytest.mark.parametrize('shape', SHAPES)
@pytest.mark.parametrize('span', [45,55])
def test_equal_area_and_finite_outline(shape, span):
    config = variant(shape, span, 430)
    points = outline(config)
    assert points[0] == (0,0)
    assert points[-1] == (config.geometry.mm('fin_root'),0)
    assert all(math.isfinite(v) for p in points for v in p)
    assert area_mm2(points) == pytest.approx(area_mm2(outline(variant('trapezoidal', span, 430))))
    assert len(config.motors)==1 and config.motors[0].designation=='D12'
    assert config.motors[0].delay_s==5
