import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from study_cap_bosses import circle_rectangle_clearance


def test_circle_rectangle_clearance():
    rectangle = (-13, 13, -13, 13)
    assert circle_rectangle_clearance(17, 0, 3.1, rectangle) == pytest.approx(.9)
    assert circle_rectangle_clearance(0, 0, 3.1, rectangle) < 0
    assert circle_rectangle_clearance(16, 17, 3.1, rectangle) == pytest.approx(1.9)
