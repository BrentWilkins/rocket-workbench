import struct
import sys
from pathlib import Path

import numpy as np
import pytest


sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))

from cfd_geometry_audit import read_binary_stl, surface_statistics


def tetrahedron():
    points=np.array([[0.,0.,0.],[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
    faces=np.array([[0,2,1],[0,1,3],[0,3,2],[1,2,3]])
    vertices=points[faces]
    cross=np.cross(vertices[:,1]-vertices[:,0],vertices[:,2]-vertices[:,0])
    normals=cross/np.linalg.norm(cross,axis=1)[:,None]
    return normals,vertices


def test_surface_integrity_detects_closed_outward_tetrahedron():
    normals,vertices=tetrahedron()
    result=surface_statistics(normals,vertices,1e-8,rotational_order=1)
    assert result['integrity']['closed_two_manifold']
    assert result['integrity']['stored_normals_match_winding']
    assert result['integrity']['positive_signed_volume']
    assert result['integrity']['degenerate_triangles'] == 0


def test_binary_stl_reader_fails_closed_on_size_mismatch(tmp_path):
    path=tmp_path/'bad.stl'
    path.write_bytes(bytes(80)+struct.pack('<I',1))
    with pytest.raises(ValueError,match='size mismatch'):
        read_binary_stl(path)


def test_symmetry_screen_retains_vertex_mismatch():
    normals,vertices=tetrahedron()
    result=surface_statistics(normals,vertices,1e-8,rotational_order=2)
    assert not result['symmetry']['screen_passed']
    assert result['symmetry']['rotations'][0]['vertices_over_tolerance'] > 0
