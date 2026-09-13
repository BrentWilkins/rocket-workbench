import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from study_avionics_geometry import pareto, variant
from rocket_workbench.avionics import payload_budget


def test_geometry_changes_preserve_component_datums():
    baseline = variant('conical', 50, 410, 55)
    changed = variant('ellipsoid', 90, 440, 45)
    assert changed.payload.mass.value == payload_budget(90)[0]
    assert changed.payload.cg_x.value == pytest.approx(payload_budget(90)[1])
    assert changed.mass_item('mount').x.value - baseline.mass_item('mount').x.value == 70
    assert changed.mass_item('chute').x.value - baseline.mass_item('chute').x.value == 40
    assert changed.mass_item('body').mass.value / baseline.mass_item('body').mass.value == pytest.approx(440/410)
    assert changed.mass_item('body').x.value == 90+440/2
    assert changed.geometry.mm('bay_length') == 145
    assert changed.geometry.mm('fin_span') == 45
    for config in [baseline, changed]:
        g = config.geometry
        assert config.mass_item('wadding').x.value-5 >= config.mass_item('chute').x.value+g.mm('chute_packed_length')/2
        assert config.mass_item('wadding').x.value+5 <= g.mm('nose_length')+g.mm('body_length')-g.mm('motor_mount_length')-g.mm('motor_overhang')


def test_wadding_inside_motor_is_rejected():
    from rocket_workbench.config import Config
    data = variant('conical', 50, 410, 55).model_dump()
    next(p for p in data['purchased_masses'] if p['role']=='wadding')['x']['value'] = 411.8
    with pytest.raises(ValueError, match='wadding'):
        Config.model_validate(data)


def test_pareto_filters_constraints_before_performance():
    rows = [dict(design=name, nominal_feasible=feasible, apogee_m=alt, speed_m_s=speed)
            for name, feasible, alt, speed in [('high', True, 60, 25), ('fast', True, 55, 30),
                ('dominated', True, 50, 24), ('unsafe', False, 100, 40)]]
    assert {r['design'] for r in pareto(rows)} == {'high', 'fast'}
