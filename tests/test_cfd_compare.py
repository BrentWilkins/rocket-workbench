import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import cfd_compare


def cases(tmp_path, monkeypatch):
    monkeypatch.setattr(cfd_compare, 'audit', lambda _: dict(
        solver_completed=True, requested_iterations_completed=True, reported_axes={'pitchAxis': '(0 0 -1)'},
        coefficient_statistics={'Cd': {'mean': .6}}, tail_settled_screen=True,
        zero_angle_symmetry_screen=False))
    paths = []
    for spacing in (30, 20):
        path = tmp_path / str(spacing)
        path.mkdir()
        spec = dict(design='test', speed_m_s=40, alpha_deg=0, reference_area_m2=.001,
                    reference_length_m=.04, moment_origin_m=[.25, 0, 0], cell_mm=spacing)
        (path / 'case-spec.json').write_text(json.dumps(spec))
        (path / 'image.json').write_text(json.dumps({'Id': 'same-image'}))
        for relative in ('constant/triSurface/rocket.stl', 'constant/transportProperties',
                         'constant/turbulenceProperties', 'system/snappyHexMeshDict',
                         'system/fvSchemes', 'system/fvSolution', 'system/controlDict',
                         '0/U', '0/p', '0/k', '0/omega', '0/nut'):
            target = path / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('identical input')
        paths.append(path)
    return paths


def test_equal_drag_does_not_imply_acceptance(tmp_path, monkeypatch):
    result = cfd_compare.compare(cases(tmp_path, monkeypatch))
    assert not result['accepted_for_design']
    assert result['cases'][1]['cd_change_from_coarser_percent'] == 0
    assert not result['cases'][1]['zero_angle_symmetry_screen']


def test_changed_surface_is_not_grid_study(tmp_path, monkeypatch):
    paths = cases(tmp_path, monkeypatch)
    (paths[1] / 'constant/triSurface/rocket.stl').write_text('different geometry')
    with pytest.raises(ValueError, match='not an isolated grid comparison'):
        cfd_compare.compare(paths)


def test_live_solver_is_not_completed_evidence(tmp_path, monkeypatch):
    paths = cases(tmp_path, monkeypatch)
    monkeypatch.setattr(cfd_compare, 'audit', lambda _: dict(solver_completed=False))
    with pytest.raises(ValueError, match='not complete'):
        cfd_compare.compare(paths)
