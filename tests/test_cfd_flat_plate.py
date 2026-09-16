import json
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))

from cfd_flat_plate_case import archive_grid, generate, mesh_lists, parse_plot3d, write_mesh


def test_plot3d_parser_preserves_fortran_i_fastest_order():
    payload=b'1 3 2  -1 0 1 -1 0 1  0 0 0 1 1 1'
    x,y=parse_plot3d(payload)
    assert x.tolist() == [[-1,0,1],[-1,0,1]]
    assert y.tolist() == [[0,0,0],[1,1,1]]


def test_structured_mesh_splits_upstream_symmetry_from_plate(tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    points,internal,patches,leading=mesh_lists(x,y)
    assert leading == 1
    assert len(points) == 12
    assert len(internal) == 1
    assert len(patches['symmetry']) == 1
    assert len(patches['plate']) == 1
    record=write_mesh(tmp_path,x,y)
    assert record['cells'] == 2
    assert 'type wall;' in (tmp_path/'constant/polyMesh/boundary').read_text()
    assert 'type empty;' in (tmp_path/'constant/polyMesh/boundary').read_text()


def test_grid_archive_checksum_fails_closed(tmp_path):
    archive=tmp_path/'changed.zip'
    archive.write_bytes(b'not the official archive')
    with pytest.raises(ValueError,match='checksum mismatch'):
        archive_grid(archive,69)


def test_generated_velocity_uses_no_slip_plate(monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10)
    assert 'plate { type noSlip; }' in (case/'0/U').read_text()
    spec=json.loads((case/'benchmark-spec.json').read_text())
    assert spec['conditions']['Re_per_unit_length'] == 5_000_000
    assert spec['conditions']['Re_plate_length'] == 10_000_000


def test_tmr_fixed_omega_wall_records_prescribed_factor(monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10,
             omega_wall='tmr-fixed-factor10')
    spec=json.loads((case/'benchmark-spec.json').read_text())
    assert spec['omega_wall_treatment']['variant'] == 'tmr-fixed-factor10'
    assert 'type fixedValue;' in (case/'0/omega').read_text()


def test_tmr_sst_mapping_writes_original_coefficients_and_requires_wall_value(
        monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    with pytest.raises(ValueError,match='factor-10'):
        generate(tmp_path/'ignored.zip',tmp_path/'rejected',ni=69,iterations=10,
                 sst_variant='tmr-sstm-flatplate-partial-map')
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10,
             omega_wall='tmr-fixed-factor10',
             sst_variant='tmr-sstm-flatplate-partial-map')
    properties=(case/'constant/turbulenceProperties').read_text()
    assert 'gamma1 0.5531666666666668' in properties
    assert 'gamma2 0.4403546666666667' in properties
    assert 'c1 20' in properties
    spec=json.loads((case/'benchmark-spec.json').read_text())
    assert spec['model_mapping']['variant'] == 'tmr-sstm-flatplate-partial-map'
    assert spec['model_mapping']['equation_mapping_complete'] is False


def test_reduced_domain_preserves_inner_rows_and_records_selected_top(monkeypatch,tmp_path):
    x=np.tile(np.asarray([-1.,0.,1.]),(4,1))
    y=np.tile(np.asarray([0.,.4,.55,1.])[:,None],(1,3))
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10,domain_top_y_m=.5)
    retained=np.load(case/'tmr-grid.npz')
    assert retained['y'].shape == (3,3)
    assert np.array_equal(retained['y'],y[:3])
    spec=json.loads((case/'benchmark-spec.json').read_text())
    assert spec['domain']['selected_top_y_mean_m'] == pytest.approx(.55)
    assert spec['domain']['original_rows'] == 4
    assert spec['domain']['retained_rows'] == 3


def test_tmr_solver_controls_disable_relative_linear_tolerance(monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10,
             solver_controls='tmr-2014')
    solution=(case/'system/fvSolution').read_text()
    assert 'tolerance 1e-20' in solution
    assert 'relTol 0' in solution
    assert 'p 0.3' in solution
    assert 'U 0.7' in solution
    spec=json.loads((case/'benchmark-spec.json').read_text())
    assert spec['solver_controls'] == 'tmr-2014'


def test_bounded_linear_upwind_is_explicit_for_each_transport(monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10,
             convection='bounded-linear-upwind')
    schemes=(case/'system/fvSchemes').read_text()
    assert 'div(phi,U) bounded Gauss linearUpwind grad(U);' in schemes
    assert 'div(phi,k) bounded Gauss linearUpwind grad(k);' in schemes
    assert 'div(phi,omega) bounded Gauss linearUpwind grad(omega);' in schemes


def test_mixed_scheme_keeps_turbulence_transport_positive(monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10,
             convection='linear-upwind-velocity')
    schemes=(case/'system/fvSchemes').read_text()
    assert 'div(phi,U) bounded Gauss linearUpwind grad(U);' in schemes
    assert 'div(phi,k) bounded Gauss upwind;' in schemes
    assert 'div(phi,omega) bounded Gauss upwind;' in schemes


def test_generated_boundaries_match_published_tmr_flat_plate_table(
        monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(tmp_path/'ignored.zip',case,ni=69,iterations=10)

    velocity=(case/'0/U').read_text()
    pressure=(case/'0/p').read_text()
    turbulence=(case/'0/k').read_text()
    assert 'top { type zeroGradient; }' in velocity
    assert 'top { type zeroGradient; }' in turbulence
    assert 'inlet { type zeroGradient; }' in pressure
    assert 'outlet { type fixedValue; value uniform 0; }' in pressure
    assert 'top { type zeroGradient; }' in pressure

    spec=json.loads((case/'benchmark-spec.json').read_text())
    assert spec['boundary_conditions']['variant']=='tmr-standard-sstm-flat-plate-table'
    assert spec['boundary_conditions']['pressure']['outlet']=='fixedValue'
    assert spec['boundary_conditions']['wall_turbulence']['k']=='fixedValue zero'


def test_source_mapped_sstm_loads_runtime_library_and_records_complete_mapping(
        monkeypatch,tmp_path):
    x=np.asarray([[-1.,0.,1.],[-1.,0.,1.]])
    y=np.asarray([[0.,0.,0.],[1.,1.,1.]])
    monkeypatch.setattr('cfd_flat_plate_case.archive_grid',lambda archive,ni:(x,y,{
        'archive_sha256':'test','archive_member':'test','member_crc32':'0',
        'coordinate_payload_sha256':'test'}))
    case=tmp_path/'case'
    generate(
        tmp_path/'ignored.zip',case,ni=69,iterations=10,
        omega_wall='tmr-fixed-factor10',
        sst_variant='tmr-sstm-v2512-source-map',
    )

    properties=(case/'constant/turbulenceProperties').read_text()
    control=(case/'system/controlDict').read_text()
    assert 'RASModel TmrSSTm;' in properties
    assert 'TmrSSTmCoeffs' in properties
    assert 'libs ("libTmrSSTm.so");' in control

    spec=json.loads((case/'benchmark-spec.json').read_text())
    assert spec['model_mapping']['equation_mapping_complete'] is True
    assert spec['model_mapping']['known_unmapped_differences']==[]
