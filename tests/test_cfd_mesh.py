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
    import json
    from cfd_case import generate
    from study_fin_shapes import variant
    generate(variant('clipped-delta',45,430),tmp_path/'case')
    record=json.loads((tmp_path/'case/case-spec.json').read_text())
    assert record['mesh']['triangles']>1000
    assert record['mesh']['absolute_deflection_m']==1e-5
