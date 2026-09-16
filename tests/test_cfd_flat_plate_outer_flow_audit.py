import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_flat_plate_outer_flow_audit import outer_metrics


def test_outer_metrics_rejects_alternating_velocity():
    velocity=np.asarray([[1.,1.],[1.01,.99],[.99,1.01]])
    result=outer_metrics(velocity,np.ones_like(velocity,dtype=bool),.005,.005)
    assert result['deviation_screen_passed'] is False
    assert result['adjacent_jump_screen_passed'] is False
    assert result['outer_flow_quality_screen'] is False


def test_outer_metrics_accepts_small_smooth_departure():
    velocity=np.asarray([[1.,1.],[1.001,1.001],[1.002,1.002]])
    result=outer_metrics(velocity,np.ones_like(velocity,dtype=bool),.005,.005)
    assert result['outer_flow_quality_screen'] is True
