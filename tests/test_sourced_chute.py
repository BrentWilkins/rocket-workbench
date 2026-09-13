import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from study_sourced_chute import configuration
from study_fin_recovery import configuration as generic


def test_wider_drag_grid_keeps_bounded_case_count():
    import yaml
    from rocket_workbench.uncertainty import StressSpec
    root = Path(__file__).resolve().parents[1]
    spec = StressSpec.model_validate(yaml.safe_load((root/'examples/uncertainty-recovery-wide.yaml').read_text()))
    assert spec.chute_cd == [.53, 1.04]
    count = (len(spec.print_mass_factors)*len(spec.payload_cg_offsets_mm)*len(spec.chute_cd)
             *len(spec.wind_m_s)*3)
    assert count == spec.max_cases == 72


@pytest.mark.parametrize('heavy,mass', [(False, 16.9), (True, 20.28)])
def test_sourced_mass_does_not_silently_reduce_packing(heavy, mass):
    config = configuration(heavy, .53)
    base = generic(24, 500, heavy)
    chute = next(p for p in config.purchased_masses if p.role == 'chute')
    assert chute.mass.value == pytest.approx(mass)
    assert config.chute_cd.value == .53
    for key in ('chute_packed_length', 'chute_packed_diameter', 'body_length'):
        assert config.geometry.mm(key) == base.geometry.mm(key)
