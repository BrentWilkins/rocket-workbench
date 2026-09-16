import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))

from cfd_flat_plate_audit import numeric_pairs, vector_list


def test_vector_list_is_counted_and_scoped():
    text='internalField nonuniform List<vector> 2 ((1 2 3) (4e-2 -5 6)); other (9 9 9)'
    assert np.allclose(vector_list(text,'internalField'),[[1,2,3],[.04,-5,6]])


def test_vector_list_fails_on_truncation():
    with pytest.raises(ValueError,match='Expected 2'):
        vector_list('plate nonuniform List<vector> 2 ((1 2 3));','plate')


def test_numeric_pairs_ignore_tecplot_headers(tmp_path):
    path=tmp_path/'data.dat'
    path.write_text('# source\nvariables="x","y"\n1 2\n3.0 4.0 extra\n')
    assert numeric_pairs(path).tolist() == [[1,2],[3,4]]
