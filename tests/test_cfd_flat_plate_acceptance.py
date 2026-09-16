import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_acceptance import evaluate


def passing_evidence():
    return {
        "benchmark": {
            "iterative_1e-7_screen": True,
            "cf_vs_karman_schoenherr_using_tmr_x_to_retheta": {
                "engineering_5_percent_screen": True,
            },
            "edge_truncated_momentum_thickness_gate": True,
        },
        "profile": {"profile_gate": True},
        "outer": {"outer_flow_quality_screen": True},
        "near_wall": {"wall_resolved_y_plus_screen": True},
        "boundary": {"published_boundary_screen": True},
        "model": {
            "flat_plate_runtime_configuration_screen": True,
            "equation_mapping_complete": True,
        },
        "numerical": {"mesh_screen_passed": True, "scheme_screen_passed": True},
        "domain": {"domain_screen_passed": True},
    }


def test_all_gates_accept_only_flat_plate_subsystem():
    result = evaluate(passing_evidence())
    assert result["flat_plate_subsystem_accepted"] is True
    assert result["accepted_for_rocket"] is False


def test_any_failed_gate_rejects_subsystem():
    evidence = copy.deepcopy(passing_evidence())
    evidence["outer"]["outer_flow_quality_screen"] = False
    result = evaluate(evidence)
    assert result["flat_plate_subsystem_accepted"] is False
    assert result["gates"]["outer_flow_quality"] is False
