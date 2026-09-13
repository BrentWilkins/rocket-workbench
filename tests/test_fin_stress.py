import sys
from pathlib import Path

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from study_fin_shapes import variant
from stress_fin_shapes import configuration


def test_upper_insert_joint_mass_and_moment():
    from study_sourced_chute import configuration as sourced
    base = sourced(False, .53, True)
    upper = configuration(base, True, 1)
    before, after = base.mass_item('bay_hardware'), upper.mass_item('bay_hardware')
    assert after.mass.value == pytest.approx(before.mass.value + .7)
    assert after.mass.value * after.x.value == pytest.approx(
        before.mass.value * before.x.value + .7 * 190)
    assert configuration(base, False, 1).mass_item('bay_hardware') == before


@pytest.mark.parametrize('upper,mount',[(False,1),(False,1.5),(True,1),(True,1.5)])
def test_stress_mass_accounting_keeps_geometry_and_motor(upper,mount):
    base=variant('clipped-delta',45,430)
    config=configuration(base,upper,mount)
    assert config.geometry==base.geometry
    assert config.motors==base.motors
    assert config.mass_item('mount').mass.value==pytest.approx(13*mount)
    assert config.payload.mass.value==pytest.approx(29.2 if upper else 20.65)
    assert config.criteria==base.criteria


@pytest.mark.parametrize('inches,body',[(20,430),(22,460),(24,500)])
def test_larger_recovery_accounts_for_mass_and_space(inches,body):
    from study_fin_recovery import configuration as recovery
    base=variant('clipped-delta',45,body)
    config=recovery(inches,body,True)
    g=config.geometry
    assert g.mm('chute_diameter')==pytest.approx(inches*25.4)
    assert g.mm('chute_packed_diameter')==32
    assert config.mass_item('chute').mass.value>base.mass_item('chute').mass.value
    chute_end=config.mass_item('chute').x.value+g.mm('chute_packed_length')/2
    mount_start=g.mm('nose_length')+g.mm('body_length')-g.mm('motor_mount_length')-g.mm('motor_overhang')
    assert mount_start-chute_end>=10
    assert config.chute_cd.value==.6
