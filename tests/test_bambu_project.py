import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_bambu_project import matrix


def test_3mf_row_vector_transform_order():
    component = matrix('0 1 0 -1 0 0 0 0 1 10 20 30')
    build = matrix('1 0 0 0 1 0 0 0 1 100 200 0')
    assert np.array([1,0,0,1]) @ component @ build == pytest.approx([110,221,30,1])


def test_nonfinite_transform_rejected():
    with pytest.raises(ValueError,match='Nonfinite'):
        matrix('1 0 0 0 1 0 0 0 1 nan 0 0')
