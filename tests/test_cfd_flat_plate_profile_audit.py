import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_profile_audit import profile_errors


def test_profile_errors_interpolates_in_log_y_plus_space():
    reference_y = np.asarray([1.0, 10.0, 100.0])
    reference_u = np.asarray([1.0, 2.0, 3.0])
    y_plus = np.asarray([1.0, np.sqrt(10.0), 10.0, 100.0])
    u_plus = np.asarray([1.0, 1.5, 2.0, 3.0])

    result = profile_errors(y_plus, u_plus, reference_y, reference_u, 100.0)

    assert result["comparison_points"] == 4
    assert result["maximum_relative_error"] == pytest.approx(0.0)
    assert result["engineering_5_percent_screen"] is True


def test_profile_errors_enforces_declared_pointwise_screen():
    result = profile_errors(
        np.asarray([1.0, 10.0, 100.0]),
        np.asarray([1.0, 2.2, 3.0]),
        np.asarray([1.0, 10.0, 100.0]),
        np.asarray([1.0, 2.0, 3.0]),
        100.0,
    )

    assert result["maximum_relative_error"] == pytest.approx(0.1)
    assert result["engineering_5_percent_screen"] is False


def test_profile_errors_rejects_too_little_overlap():
    with pytest.raises(ValueError, match="Fewer than three"):
        profile_errors(
            np.asarray([0.1, 0.5, 1.0]),
            np.asarray([0.1, 0.5, 1.0]),
            np.asarray([1.0, 10.0]),
            np.asarray([1.0, 2.0]),
            10.0,
        )
