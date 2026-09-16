import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_near_wall_audit import scalar_list


def test_scalar_list_is_counted_and_patch_scoped():
    text = "internalField uniform 9; plate { value nonuniform List<scalar> 3 (1 .2 3e-2); }"

    assert np.array_equal(scalar_list(text, "plate"), np.asarray([1.0, 0.2, 0.03]))


def test_scalar_list_rejects_truncation():
    with pytest.raises(ValueError, match="Expected 3"):
        scalar_list("plate { value nonuniform List<scalar> 3 (1 2); }", "plate")
