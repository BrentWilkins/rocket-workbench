from pathlib import Path
import copy
import pytest
from rocket_workbench.config import Config, load_config, mass_cg
from rocket_workbench.sweep import SweepSpec, variant
from rocket_workbench.report import evaluate

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def base():
    return load_config(ROOT/'examples/baseline.yaml')


def test_mass_balance():
    assert mass_cg([(10, 20), (30, 100)]) == (40, 80)
    for values in [[], [(0, 1)], [(float('nan'), 1)], [(1, float('inf'))]]:
        with pytest.raises(ValueError):
            mass_cg(values)


@pytest.mark.parametrize('field,value', [('body_id', 50), ('motor_mount_id', 17), ('fin_root', 10),
    ('chute_packed_length', 500), ('wall', 10), ('clearance', 2)])
def test_bad_fit(base, field, value):
    data = base.model_dump()
    data['geometry'][field]['value'] = value
    with pytest.raises(ValueError):
        Config.model_validate(data)


def test_missing_mass_and_units(base):
    data = base.model_dump()
    data['purchased_masses'][0]['mass']['value'] = None
    with pytest.raises(ValueError, match='Missing'):
        Config.model_validate(data)
    data = base.model_dump()
    data['geometry']['body_length']['unit'] = 'm'
    with pytest.raises(ValueError, match='Expected mm'):
        Config.model_validate(data)


def test_unsupported_geometry_and_ledger(base):
    for change in ['external', 'missing_role', 'unknown_part']:
        data = base.model_dump()
        if change == 'external':
            data['payload']['external_protrusions'] = True
        elif change == 'missing_role':
            data['purchased_masses'].pop()
        else:
            data['printed_measurements'] = {'unknown': [data['payload']['mass'], data['payload']['cg_x']]}
        with pytest.raises(ValueError):
            Config.model_validate(data)


def test_sweep_updates_masses_and_positions(base):
    candidate = variant(base, {'body_length': 340, 'chute_diameter': 381}, 'test')
    assert candidate.mass_item('body').mass.value == pytest.approx(17)
    assert candidate.mass_item('body').x.value == 240
    assert candidate.mass_item('mount').x.value == pytest.approx(372.5-3.2)
    assert candidate.mass_item('chute').mass.value == pytest.approx(6*(381/305)**2)
    assert base.mass_item('body').mass.value == 15
    with pytest.raises(ValueError):
        SweepSpec(schema_version=1, axes={'body_length':[260, 300, 340]}, max_designs=2, source='test')
    with pytest.raises(ValueError):
        SweepSpec(schema_version=1, axes={'unknown':[1]}, max_designs=2, source='test')


def test_evaluation_never_ranks_incomplete_or_failed(base):
    result = dict(execution='completed', warnings=[], metrics={
        'apogee_m':60, 'guide_departure_m_s':15, 'minimum_ascent_stability_cal':1.5,
        'deployment_speed_m_s':5, 'landing_descent_m_s':4, 'deployment_before_ground':True},
        motor={'max_liftoff_mass':base.motors[-1].max_liftoff_mass.model_dump()}, mass={'launch_mass_g':90})
    evaluation = evaluate(result, base)
    assert evaluation['criteria_status'] == 'meets configured simulation criteria'
    assert evaluation['status'] == 'incomplete inputs'
    assert not evaluation['eligible'] and evaluation['rank'] is None
    for change in ['failure', 'warning', 'overmass', 'missing']:
        case = copy.deepcopy(result)
        if change == 'failure': case['execution'] = 'simulation failed'
        if change == 'warning': case['warnings'] = ['recovery failure']
        if change == 'overmass': case['mass']['launch_mass_g'] = 200
        if change == 'missing': case['metrics']['deployment_speed_m_s'] = None
        assert evaluate(case, base)['criteria_status'] != 'meets configured simulation criteria'
