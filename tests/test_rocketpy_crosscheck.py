"""Adapter physics regressions with synthetic inputs: no Java or retained runs needed."""
import sys
from pathlib import Path

import numpy as np
import pytest

pytest.importorskip('rocketpy')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

from crosscheck_rocketpy import build, crosscheck
from study_payload_grid import candidate


@pytest.fixture(scope='module')
def inputs():
    config = candidate(500, 40, 53.65384615384615, 'ogive', 'D12')
    # Independent parallel-axis arithmetic, not values copied from RocketPy.
    structure, structure_cg, motor_cg = .18, .26, .50
    loaded, spent, radius, length = .042, .022, .012, .070
    total = structure + loaded
    cg = (structure * structure_cg + loaded * motor_cg) / total
    pitch = .005 + structure * (structure_cg - cg)**2
    pitch += loaded * ((3 * radius**2 + length**2) / 12 + (motor_cg - cg)**2)
    mass = dict(dry_mass_g=structure * 1000, dry_cg_x_mm=structure_cg * 1000,
                dry_pitch_inertia_kg_m2=.005, dry_roll_inertia_kg_m2=5e-5,
                launch_mass_g=total * 1000, launch_cg_x_mm=cg * 1000,
                launch_pitch_inertia_kg_m2=pitch,
                launch_roll_inertia_kg_m2=5e-5 + loaded * radius**2 / 2)
    elevation = config.launch.elevation.value
    native = dict(mass_audit=mass, design='synthetic-adapter-test', scenario='calm',
                  effective_guide_m=.8,
                  atmosphere=dict(levels=[[elevation, 84000, 285, 9.8],
                                           [elevation + 1000, 74000, 278, 9.8]]),
                  inputs=dict(tilt_deg=0, tilt_heading_deg=0,
                              wind=dict(levels=[[0, 0, 0], [1000, 0, 0]])))
    motor = dict(length_mm=70, diameter_mm=24, spent_mass_g=22, loaded_mass_g=42,
                 time_s=[0, .1, .5, 1.], thrust_n=[0, 20, 12, 0],
                 cg_from_front_mm=[35] * 4, mass_g=[42, 40, 30, 22], delay_s=2.)
    anchor = dict(timeseries=dict(time_s=[0, .2, .5, 1., 1.2, 2., 3.],
                                 speed_m_s=[0, 5, 12, 20, 18, 10, 0],
                                 mach=[0, .015, .035, .06, .055, .03, 0],
                                 drag_coefficient=[.6] * 7),
                  metrics=dict(burnout_time_s=1.), events=[dict(type='APOGEE', time_s=3.)])
    return config, native, motor, anchor


def test_mass_cg_and_inertia_match_through_burn(inputs):
    rocket, _, audit = build(*inputs)
    motor = inputs[2]
    for t in [0, .05, .1, .3, .5, .75, 1., 1.2]:
        mm = np.interp(t, motor['time_s'], motor['mass_g']) / 1000
        total = .18 + mm
        cg = (.18 * .26 + mm * .50) / total
        expected_pitch = .005 + .18 * (.26 - cg)**2
        expected_pitch += mm * ((3 * .012**2 + .070**2) / 12 + (.50 - cg)**2)
        actual_pitch = rocket.I_11(t) - total * (cg - rocket.center_of_dry_mass_position)**2
        assert rocket.total_mass(t) == pytest.approx(total, abs=1e-12)
        assert rocket.center_of_mass(t) == pytest.approx(cg, abs=1e-12)
        assert actual_pitch == pytest.approx(expected_pitch, rel=1e-9)
        assert rocket.I_33(t) == pytest.approx(5e-5 + mm * .012**2 / 2, rel=1e-9)
    assert audit['launch_pitch_inertia_kg_m2_relative_delta'] == pytest.approx(0, abs=1e-12)


def test_mass_flow_supports_complex_step_and_matches_mass_slope(inputs):
    rocket, _, _ = build(*inputs)
    for t in [.05, .3, .75, 1.2]:
        delta = 1e-5
        slope = (rocket.total_mass(t + delta) - rocket.total_mass(t - delta)) / (2 * delta)
        assert rocket.total_mass_flow_rate(t) == pytest.approx(slope, abs=1e-10)
        assert rocket.total_mass_flow_rate(t + 1e-20j) == pytest.approx(slope, abs=1e-10)
        assert rocket.total_mass_flow_rate.differentiate_complex_step(t) == pytest.approx(0)


def test_ejection_timer_audit_is_burnout_plus_delay(inputs):
    rocket, _, audit = build(*inputs)
    expected = inputs[2]['time_s'][-1] + inputs[2]['delay_s'] + .001
    assert audit['deployment_requested_s'] == pytest.approx(expected)
    assert rocket.parachutes[0].lag == pytest.approx(expected)


def test_ascent_stops_at_apogee_without_inventing_landing(inputs):
    result = crosscheck(*inputs, max_step=.04)
    assert result['execution'] == 'completed'
    assert result['scope'] == 'ascent_only'
    assert result['metrics']['deployment_time_s'] is None
    assert result['metrics']['landing_displacement_m'] is None
    assert result['metrics']['landing_descent_m_s'] is None
    events = {e['type']: e['time_s'] for e in result['events']}
    assert 'GROUND_HIT' not in events
    assert 'RECOVERY_DEVICE_DEPLOYMENT' not in events
    assert result['metrics']['rod_exit_time_s'] < result['metrics']['burnout_time_s'] < events['APOGEE']
    trace = result['timeseries']
    assert trace['time_s'][-1] == pytest.approx(events['APOGEE'], abs=1e-6)
    assert trace['altitude_m'][-1] > 0
    rod_altitude = np.interp(result['metrics']['rod_exit_time_s'], trace['time_s'], trace['altitude_m'])
    assert rod_altitude == pytest.approx(inputs[1]['effective_guide_m'], abs=1e-4)
