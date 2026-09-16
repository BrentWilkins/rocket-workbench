import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_source_mapping_sensitivity import invariant_signature


def test_invariant_signature_excludes_only_model_mapping():
    spec = {
        "benchmark": "flat plate",
        "conditions": {"U": 1},
        "mesh": {"cells": 2},
        "domain": {"top": 1},
        "boundary_conditions": {"variant": "published"},
        "omega_wall_treatment": {"variant": "fixed"},
        "convection_scheme": "linearUpwind",
        "solver_controls": "tight",
        "source": {"coordinate_payload_sha256": "abc"},
        "model_mapping": {"variant": "ignored"},
    }
    signature = invariant_signature({"spec": spec})
    assert "model_mapping" not in signature
    assert signature["boundary_conditions"] == {"variant": "published"}
    assert signature["coordinate_payload_sha256"] == "abc"
