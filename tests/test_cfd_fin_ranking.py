import json
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_fin_ranking_audit import clear_drag_order, closed_interval, evaluate, interval_relation
from cfd_fin_ranking_prepare import case_matrix, design_matrix
from cfd_fin_ring_remediation_prepare import remediation_matrix


def test_predeclared_matrix_has_six_designs_and_twenty_four_cases():
    designs = design_matrix()
    cases = case_matrix()
    assert len(designs) == 6
    assert len(cases) == 24
    assert {item["shape"] for item in designs} == {
        "trapezoidal",
        "elliptical",
        "clipped-delta",
        "swept",
    }
    assert {item["ring_chord_mm"] for item in designs} == {0, 5, 10}
    assert {(item["alpha_deg"], item["cell_mm"]) for item in cases} == {
        (0, 20),
        (0, 15),
        (5, 20),
        (5, 15),
    }


def test_ring_remediation_matrix_has_matched_control_and_two_rings():
    assert remediation_matrix() == [
        {"id": "clipped-delta", "ring_chord_mm": 0},
        {"id": "clipped-delta-ring-5mm", "ring_chord_mm": 5},
        {"id": "clipped-delta-ring-10mm", "ring_chord_mm": 10},
    ]


def test_ranking_audit_records_missing_solver_output_as_unrankable(tmp_path):
    manifest = {
        "cases": [
            {
                "id": "ring",
                "case_id": "ring-a0-cell20",
                "path": "ring-a0-cell20",
                "alpha_deg": 0,
                "cell_mm": 20,
            }
        ],
        "claim_boundary": {"validated_rocket_aerodynamics": False},
    }
    (tmp_path / "ranking-manifest.json").write_text(json.dumps(manifest))
    case = tmp_path / "ring-a0-cell20"
    case.mkdir()
    (case / "execution.json").write_text(
        json.dumps([{"stage": "checkMesh", "returncode": 0}])
    )

    result = evaluate(tmp_path)

    assert result["status"] == "complete_with_unrankable_cases"
    assert result["unavailable_cases"] == ["ring-a0-cell20"]
    assert result["rows"][0]["completed_stages"] == ["checkMesh"]
    assert result["zero_angle_drag_ranking"] is None


def test_closed_grid_intervals_are_order_independent():
    assert closed_interval(0.6, 0.5) == [0.5, 0.6]
    assert interval_relation([0.4, 0.5], [0.6, 0.7]) == "lower"
    assert interval_relation([0.6, 0.7], [0.4, 0.5]) == "higher"
    assert interval_relation([0.4, 0.6], [0.6, 0.7]) == "overlap"


def test_clear_drag_order_requires_nonoverlapping_grid_intervals():
    result = clear_drag_order(
        {
            "winner": [0.40, 0.42],
            "middle": [0.45, 0.50],
            "overlap-middle": [0.49, 0.53],
            "loser": [0.60, 0.70],
        }
    )
    assert result["clear_winners"] == ["winner"]
    assert result["clear_losers"] == ["loser"]
    overlap = next(
        row
        for row in result["pairwise"]
        if {row["left"], row["right"]} == {"middle", "overlap-middle"}
    )
    assert overlap["relation"] == "overlap"
    assert overlap["winner"] is None
