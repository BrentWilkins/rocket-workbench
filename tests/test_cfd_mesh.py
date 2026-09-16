import json
import sys
from pathlib import Path

import pytest

pytestmark=pytest.mark.integration
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))


def test_closed_cone_cfd_triangulation(tmp_path):
    import cadquery as cq
    from cfd_case import surface_mesh
    solid=cq.Solid.makeCone(0,.0208,.05)
    record=surface_mesh(solid,tmp_path/'cone.stl')
    assert record['triangles']>10
    assert (tmp_path/'cone.stl').stat().st_size==84+50*record['triangles']
    assert record['absolute_deflection_m']==1e-5
    assert not record['relative_deflection']


def test_delta_external_surface_is_closed(tmp_path):
    from cfd_case import generate
    from study_fin_shapes import variant
    generate(variant('clipped-delta',45,430),tmp_path/'case')
    record=json.loads((tmp_path/'case/case-spec.json').read_text())
    assert record['mesh']['triangles']>1000
    assert record['mesh']['absolute_deflection_m']==1e-5


def test_delta_cad_is_symmetric_even_when_surface_audit_fails_closed(tmp_path):
    from cfd_case import generate
    from cfd_geometry_audit import audit
    from study_fin_shapes import variant

    case=tmp_path/'case'
    generate(variant('clipped-delta',45,430),case)
    result=audit(case)
    assert result['cad_solid']['screen_passed']
    assert result['reference_checks']['screen_passed']
    assert not result['accepted_for_design']


def test_axisymmetric_control_excludes_fins_and_ring_tail(tmp_path):
    from cfd_case import generate
    from cfd_geometry_audit import audit
    from study_fin_shapes import variant

    case=tmp_path/'axisymmetric'
    generate(variant('clipped-delta',45,430),case,axisymmetric_control=True)
    record=json.loads((case/'case-spec.json').read_text())
    assert record['geometry_variant'] == 'axisymmetric-control'
    assert record['ring_tail']['chord_mm'] == 0
    assert record['mesh']['source'] == 'analytic-axisymmetric-control'
    assert record['mesh']['angular_segments'] == 192
    assert record['mesh']['maximum_radial_chord_error_m'] < 1e-5
    geometry=audit(case,rotational_order=12)
    assert geometry['geometry_screen_passed']
    assert geometry['symmetry']['screen_passed']
    with pytest.raises(ValueError,match='cannot include'):
        generate(variant('clipped-delta',45,430),tmp_path/'invalid',ring_chord_mm=5,
                 axisymmetric_control=True)
