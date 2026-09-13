import sys
from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

from rocket_workbench.config import Config, MotorCase, load_config
from rocket_workbench.flight_model import generate

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from study_motor24 import configuration, PLATFORMS, PROFILES


def test_all_motor24_study_inputs_fit_and_keep_explicit_criteria():
    total = 0
    for platform in PLATFORMS:
        for profile in PROFILES:
            config = configuration(platform, profile)
            total += len(config.motors)*len(config.launch.wind_speeds)*3
            apogee = next(c for c in config.criteria if c.metric == 'apogee_m')
            assert apogee.maximum is None and apogee.minimum == 30
            g = config.geometry
            end = g.mm('nose_length')+g.mm('body_length')
            assert config.mass_item('wadding').x.value+5 <= end-g.mm('motor_mount_length')-g.mm('motor_overhang')
            assert g.mm('body_od') == 41.6
            if platform != '18-c5':
                assert g.mm('motor_mount_length') == 95
                assert g.mm('motor_mount_id') >= 24
    assert total == 405


def test_reject_24mm_motor_in_18mm_mount_and_long_motor_in_short_mount():
    data = configuration('18-c5', 'nominal').model_dump()
    data['motors'] = configuration('24-cd', 'nominal').model_dump()['motors']
    with pytest.raises(ValueError, match='motor does not fit'):
        Config.model_validate(data)
    data = configuration('24-e', 'nominal').model_dump()
    data['geometry']['motor_mount_length']['value'] = 70
    with pytest.raises(ValueError, match='motor does not fit'):
        Config.model_validate(data)


def test_short_motor_spacer_is_counted_in_mount_mass_and_cg():
    cd = configuration('24-cd', 'nominal').mass_item('mount')
    e = configuration('24-e', 'nominal').mass_item('mount')
    assert cd.mass.value == e.mass.value+1
    assert cd.x.value < e.x.value
    assert configuration('24-cd', 'heavy-build').mass_item('mount').mass.value == 19.5


@pytest.mark.parametrize('platform,diameter,length', [('18-c5', .018, .070), ('24-cd', .024, .070), ('24-e', .024, .095)])
def test_ork_declares_actual_motor_dimensions(tmp_path, platform, diameter, length):
    config = configuration(platform, 'nominal')
    parts = {name: dict(mass_g=1, cg_x_mm=150) for name in
             ['nose-bay', 'bay-bulkhead', 'payload-sled', 'fin-collar', 'lug-sleeve-1', 'lug-sleeve-2']}
    path = tmp_path/'model.ork'
    generate(config, parts, 'actual', path)
    motor = ET.parse(path).find('.//motormount/motor')
    assert float(motor.findtext('diameter')) == diameter
    assert float(motor.findtext('length')) == length
    assert motor.findtext('digest') == config.motors[0].digest


def test_historical_18mm_inputs_still_have_original_gate_and_no_new_fields():
    root = Path(__file__).resolve().parents[1]
    original = load_config(root/'examples/avionics-performance.yaml')
    assert original.criteria[0].maximum == 120
    assert set(original.motors[0].model_dump()) == {'designation', 'delay_s', 'digest', 'max_liftoff_mass'}
