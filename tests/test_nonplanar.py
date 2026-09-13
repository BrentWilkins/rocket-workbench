import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from study_fin_shapes import variant
from rocket_workbench.cad import shapes
from rocket_workbench.nonplanar import ring_tail

pytestmark = pytest.mark.integration


def test_ring_is_connected_and_adds_material():
    config = variant('clipped-delta',45,430)
    baseline = shapes(config)['fin-collar']
    ring = ring_tail(config, baseline)
    assert ring.val().isValid() and len(ring.solids().vals()) == 1
    assert ring.val().Volume() > baseline.val().Volume()
    assert ring.val().BoundingBox().zmax == pytest.approx(baseline.val().BoundingBox().zmax)
    with pytest.raises(ValueError, match='bounded'):
        ring_tail(config, baseline, wall_mm=.4)
    with pytest.raises(ValueError, match='clipped-delta'):
        ring_tail(variant('trapezoidal',45,430), baseline)
