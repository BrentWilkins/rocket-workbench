import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_numerical_study import compare_cf, interpolate_cf, invariant_signature


def test_compare_cf_uses_candidate_as_relative_denominator():
    result = compare_cf(
        np.asarray([0.98, 1.02, 1.0]),
        np.asarray([1.0, 1.0, 1.0]),
        0.02,
    )

    assert result["maximum_relative_change"] == pytest.approx(0.02)
    assert result["screen_passed"] is True


def test_compare_cf_fails_when_any_station_exceeds_limit():
    result = compare_cf(np.asarray([0.97, 1.0, 1.0]), np.ones(3), 0.02)

    assert result["screen_passed"] is False


def test_interpolate_cf_refuses_extrapolation():
    run = {
        "case": "retained-case",
        "x": np.asarray([1.0, 2.0]),
        "cf": np.asarray([0.1, 0.2]),
    }

    with pytest.raises(ValueError, match="exceed profile support"):
        interpolate_cf(run, np.asarray([0.5, 1.5]))


def test_grid_invariant_includes_boundary_and_solver_controls():
    spec = {
        "benchmark": "flat plate",
        "source": {"archive_sha256": "abc"},
        "conditions": {"U": 1},
        "model_mapping": {"variant": "sstm"},
        "omega_wall_treatment": {"variant": "fixed"},
        "boundary_conditions": {"variant": "published"},
        "solver_controls": "tight",
        "domain": {
            "requested_top_y_m": None,
            "selected_top_y_min_m": 1.0,
            "selected_top_y_mean_m": 1.0,
            "selected_top_y_max_m": 1.0,
        },
        "convection_scheme": "linearUpwind",
    }
    result = invariant_signature({"spec": spec}, include_scheme=True)
    assert result["boundary_conditions"] == {"variant": "published"}
    assert result["solver_controls"] == "tight"
    assert result["domain_extent"]["selected_top_y_mean_m"] == 1.0
