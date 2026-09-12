import numpy as np
import pytest
from rocket_workbench.simulator import summarize


def flight():
    return {key: np.array(value, dtype=float) for key, value in dict(
        time_s=[0, 1, 2, 2, 3, 4], altitude_m=[0, 10, 20, 20, 10, 0],
        speed_m_s=[0, 12, 8, 0, 5, 5], velocity_z_m_s=[0, 12, 8, 0, -5, -5],
        cp_x_m=[.3, .3, 0, 0, 0, 0], cg_x_m=[.2]*6, reference_length_m=[.05]*6,
        east_m=[0, 0, 1, 1, 2, 3], north_m=[0, 0, 1, 1, 2, 4]).items()}


def test_event_boundaries_and_stability():
    events = [dict(type=k, time_s=t) for k, t in [('LAUNCHROD',1), ('RECOVERY_DEVICE_DEPLOYMENT',2), ('APOGEE',2.1), ('GROUND_HIT',4)]]
    result = summarize(flight(), events)
    assert result['minimum_ascent_stability_cal'] == pytest.approx(2)
    assert result['deployment_speed_m_s'] == 8
    assert result['landing_displacement_m'] == 5
    assert result['landing_descent_m_s'] == 5


def test_deployment_after_ground_is_unavailable():
    result = summarize(flight(), [dict(type='GROUND_HIT',time_s=3), dict(type='RECOVERY_DEVICE_DEPLOYMENT',time_s=4)])
    assert result['deployment_speed_m_s'] is None
    assert result['deployment_altitude_m'] is None
    assert result['deployment_before_ground'] is False
    assert result['guide_departure_m_s'] is None
