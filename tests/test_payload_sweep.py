import json

import pytest

from scripts.plot_payload_sweep import (
    BODIES, MOTORS, NOSES, SHAPES, SPANS, c11_mass_screen, load_grid,
    short_listed,
)


def _rows():
    return [
        dict(body_mm=body, nose_mm=nose, span_mm=span, nose_shape=shape,
             motor=motor, wind_m_s=4.0, status="completed", dry_mass_g=173.0,
             launch_mass_g=215.0 if motor == "D12-5" else 231.0)
        for body in BODIES for nose in NOSES for span in SPANS
        for shape in SHAPES for motor in MOTORS
    ]


def test_grid_rejects_missing_and_duplicate_points(tmp_path):
    path = tmp_path / "comparison.json"
    rows = _rows()
    path.write_text(json.dumps(rows))
    assert len(load_grid([path])) == 360
    path.write_text(json.dumps(rows[:-1]))
    with pytest.raises(ValueError, match="Incomplete nominal grid"):
        load_grid([path])
    path.write_text(json.dumps(rows + rows[:1]))
    with pytest.raises(ValueError, match="Duplicate grid point"):
        load_grid([path])


def test_c11_mass_transfer_requires_same_dry_design(tmp_path):
    rows = _rows()
    anchor_path = tmp_path / "c11.json"
    output = tmp_path / "c11.csv"
    anchor = dict(body_mm=500.0, nose_mm=40.0, span_mm=45.0,
                  nose_shape="conical", dry_mass_g=173.0, launch_mass_g=207.7,
                  motor_liftoff_limit_g=170, status="excluded: manufacturer liftoff-mass limit")
    anchor_path.write_text(json.dumps([anchor]))
    assert c11_mass_screen(rows, anchor_path, output) == pytest.approx(207.7)
    assert len(output.read_text().splitlines()) == 181
    anchor["dry_mass_g"] = 174.0
    anchor_path.write_text(json.dumps([anchor]))
    with pytest.raises(ValueError, match="dry masses differ"):
        c11_mass_screen(rows, anchor_path, output)


def test_shortlist_is_comparison_target_not_only_stability():
    row = dict(stability_cal=1.51, guide_m_s=12.1,
               deployment_m_s=9.9, descent_m_s=5.9)
    assert short_listed(row)
    for name, failing_value in (("stability_cal", 1.49), ("guide_m_s", 11.9),
                                ("deployment_m_s", 10.1), ("descent_m_s", 6.1)):
        assert not short_listed(dict(row, **{name: failing_value}))
