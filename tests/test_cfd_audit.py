import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from cfd_audit import audit


def fixture_case(tmp_path, lateral):
    (tmp_path/'case-spec.json').write_text(json.dumps(dict(design='test',alpha_deg=0,iterations=100)))
    (tmp_path/'execution.json').write_text(json.dumps([dict(stage='simpleFoam',stage_passed=True)]))
    coefficients=tmp_path/'postProcessing/forces/0/coefficient.dat'
    coefficients.parent.mkdir(parents=True)
    coefficients.write_text('# pitchAxis : (0 0 -1)\n# Time Cd Cl Cs CmPitch CmYaw CmRoll\n'+
        '\n'.join(f'{i} .6 {lateral} 0 0 0 0' for i in range(1,101)))
    return tmp_path


def test_settled_asymmetric_solution_is_not_accepted(tmp_path):
    result=audit(fixture_case(tmp_path,.15))
    assert result['tail_settled_screen']
    assert not result['zero_angle_symmetry_screen']
    assert not result['accepted_for_design']
    assert result['reported_axes']['pitchAxis']=='(0 0 -1)'


def test_symmetric_settling_still_needs_grid_and_benchmark(tmp_path):
    result=audit(fixture_case(tmp_path,0))
    assert result['zero_angle_symmetry_screen']
    assert not result['accepted_for_design']
    assert 'Grid convergence' in result['remaining']
