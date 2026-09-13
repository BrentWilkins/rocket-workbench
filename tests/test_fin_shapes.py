import math
import sys
from pathlib import Path

import pytest

from rocket_workbench.fins import outline, area_mm2

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from study_fin_shapes import variant, SHAPES


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
