import json
import sys
from pathlib import Path

import numpy as np
import pytest

from rocket_workbench.robustness import profile, load_profile, samples, scenarios, flight_metrics, quantiles


def test_profile_coordinates_and_validation(tmp_path):
    p = profile([[1500, 1, 2], [2100, 3, 4]], altitude_reference="MSL", elevation_m=1500)
    assert p["levels"] == [[0, 1, 2], [600, 3, 4]]
    for levels in ([[0,0,0]], [[1,0,0],[600,0,0]], [[0,0,0],[0,1,1]], [[0,0,0],[500,float("nan"),0]]):
        with pytest.raises(ValueError):
            profile(levels)
    path = tmp_path/"wind.json"
    path.write_text(json.dumps(dict(source="test", timestamp="2026-09-19T00:00:00Z", latitude=40,
        longitude=-105, altitude_reference="MSL", units={"height":"m","velocity":"m/s"},
        levels=[[1500,1,2],[2500,3,4]])))
    assert load_profile(path,1500)["levels"][0][0] == 0


def test_samples_paired_prefix_and_variable_stability():
    short = samples(3,42,["body","payload"])
    assert short == samples(10,42,["payload","body"])[:3]
    added = samples(3,42,["body","payload","new"])
    assert [{k:v for k,v in s.items() if k != "mass:new"} for s in added] == short
    assert short != samples(3,43,["body","payload"])
    assert len(scenarios()) == 20


def test_phase_metrics_exclude_rod_and_recovery():
    a = dict(time_s=[0,1,2,3,4,5], thrust_n=[0,5,5,0,0,0],
             orientation_theta_rad=np.radians([90,90,80,75,50,0]).tolist(),
             angle_of_attack_rad=np.radians([90,8,2,4,40,90]).tolist(),
             cp_x_m=[.4]*6,cg_x_m=[.3]*6,reference_length_m=[.04]*6,
             pitch_rate_rad_s=[0,1,2,3,4,5],yaw_rate_rad_s=[0]*6,
             velocity_z_m_s=[0,10,20,10,0,-5],speed_m_s=[0,10,21,12,5,6])
    events=[dict(type=k,time_s=t) for k,t in [("LAUNCHROD",1),("BURNOUT",3),("APOGEE",4),("RECOVERY_DEVICE_DEPLOYMENT",4.5)]]
    m = flight_metrics(dict(timeseries=a,events=events))
    assert m["powered_max_aoa_deg"] == pytest.approx(8)
    assert m["powered_min_stability_cal"] == pytest.approx(2.5)
    assert m["burnout_tilt_deg"] == pytest.approx(15)
    assert m["powered_max_tilt_deg"] == pytest.approx(10)
    assert flight_metrics(dict(timeseries=a, events=[]))["powered_min_stability_cal"] is None
    a["angle_of_attack_rad"][2] = None
    assert flight_metrics(dict(timeseries=a, events=events))["powered_max_aoa_deg"] is None


def test_quantiles_keep_valid_count():
    assert quantiles([None,float("nan")])["valid"] == 0
    assert quantiles([1,2,3,None])["median"] == 2
