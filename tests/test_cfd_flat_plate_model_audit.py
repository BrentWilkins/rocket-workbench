import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_model_audit import close_enough, coefficient_block


def test_coefficient_block_is_scoped_to_printed_sst_dictionary():
    log = """
unrelated gamma1 99;
kOmegaSSTCoeffs
{
    gamma1 0.553167;
    gamma2 0.440355;
    c1 20;
}
"""
    assert coefficient_block(log) == {
        "gamma1": pytest.approx(0.553167),
        "gamma2": pytest.approx(0.440355),
        "c1": pytest.approx(20.0),
    }


def test_coefficient_block_supports_source_mapped_model_name():
    log = "TmrSSTmCoeffs { gamma1 0.553167; c1 20; }"
    assert coefficient_block(log, "TmrSSTmCoeffs") == {
        "gamma1": pytest.approx(0.553167),
        "c1": pytest.approx(20.0),
    }


def test_runtime_report_precision_is_allowed_but_material_change_is_not():
    assert close_enough(0.553167, 0.5531666666666668)
    assert not close_enough(0.55, 0.5531666666666668)
