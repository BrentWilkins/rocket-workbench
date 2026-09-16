"""Audit generated CFD surface geometry without running or modifying a case."""

import argparse
import hashlib
import json
import math
import struct
from collections import Counter
from pathlib import Path

import numpy as np


STL_DTYPE=np.dtype([('normal','<f4',3),('vertices','<f4',(3,3)),('attribute','<u2')])


def read_binary_stl(path: Path) -> tuple[np.ndarray,np.ndarray]:
    payload=path.read_bytes()
    if len(payload) < 84:
        raise ValueError('Binary STL is shorter than its 84-byte header')
    triangles=struct.unpack_from('<I',payload,80)[0]
    expected=84+triangles*STL_DTYPE.itemsize
    if len(payload) != expected:
        raise ValueError(f'Binary STL size mismatch: expected {expected}, got {len(payload)}')
    records=np.frombuffer(payload,dtype=STL_DTYPE,count=triangles,offset=84)
    return records['normal'].astype(float),records['vertices'].astype(float)


def nearest_distances(points: np.ndarray,transformed: np.ndarray,decimals: int=8) -> np.ndarray:
    buckets={}
    for point in points:
        buckets.setdefault(tuple(np.round(point,decimals)),[]).append(point)
    distances=[]
    for point in transformed:
        candidates=buckets.get(tuple(np.round(point,decimals)))
        if candidates:
            distances.append(min(float(np.linalg.norm(point-item)) for item in candidates))
        else:
            distances.append(float(np.linalg.norm(points-point,axis=1).min()))
    return np.asarray(distances)


def point_triangle_distances(point: np.ndarray, triangles: np.ndarray) -> np.ndarray:
    """Return exact distances from one point to each nondegenerate triangle."""
    a = triangles[:, 0]
    b = triangles[:, 1]
    c = triangles[:, 2]
    ab = b - a
    ac = c - a
    normal = np.cross(ab, ac)
    normal_squared = np.einsum("ij,ij->i", normal, normal)
    if np.any(normal_squared <= 1e-30):
        raise ValueError("Point-to-surface distance requires nondegenerate triangles")

    ap = point - a
    signed_numerator = np.einsum("ij,ij->i", ap, normal)
    projected = point - (signed_numerator / normal_squared)[:, None] * normal
    projected_ap = projected - a

    dot00 = np.einsum("ij,ij->i", ac, ac)
    dot01 = np.einsum("ij,ij->i", ac, ab)
    dot02 = np.einsum("ij,ij->i", ac, projected_ap)
    dot11 = np.einsum("ij,ij->i", ab, ab)
    dot12 = np.einsum("ij,ij->i", ab, projected_ap)
    denominator = dot00 * dot11 - dot01 * dot01
    u = (dot11 * dot02 - dot01 * dot12) / denominator
    v = (dot00 * dot12 - dot01 * dot02) / denominator
    inside = (u >= 0) & (v >= 0) & (u + v <= 1)
    plane_distance = np.abs(signed_numerator) / np.sqrt(normal_squared)

    def segment_distances(start, end):
        delta = end - start
        fraction = np.einsum("ij,ij->i", point - start, delta) / np.einsum(
            "ij,ij->i", delta, delta
        )
        fraction = np.clip(fraction, 0, 1)
        closest = start + fraction[:, None] * delta
        return np.linalg.norm(point - closest, axis=1)

    edge_distance = np.minimum.reduce(
        (
            segment_distances(a, b),
            segment_distances(b, c),
            segment_distances(c, a),
        )
    )
    return np.where(inside, plane_distance, edge_distance)


def transform_statistics(
    points: np.ndarray, triangles: np.ndarray, matrix: np.ndarray, tolerance_m: float
) -> dict:
    transformed = points @ matrix.T
    vertex_distances = nearest_distances(points, transformed)
    surface_distances = vertex_distances.copy()
    for index in np.flatnonzero(vertex_distances > tolerance_m):
        surface_distances[index] = float(point_triangle_distances(transformed[index], triangles).min())
    return {
        'max_nearest_vertex_error_m': float(vertex_distances.max(initial=0)),
        'p99_nearest_vertex_error_m': float(np.quantile(vertex_distances,.99)),
        'vertices_over_tolerance': int(np.count_nonzero(vertex_distances>tolerance_m)),
        'max_nearest_surface_error_m': float(surface_distances.max(initial=0)),
        'surface_points_over_tolerance': int(np.count_nonzero(surface_distances>tolerance_m)),
        'tolerance_m': tolerance_m,
        'screen_passed': bool(np.all(surface_distances<=tolerance_m)),
    }


def surface_statistics(normals: np.ndarray,vertices: np.ndarray,tolerance_m: float,
                       rotational_order: int) -> dict:
    if not len(vertices):
        raise ValueError('Surface contains no triangles')
    flat=vertices.reshape(-1,3)
    points,inverse=np.unique(flat,axis=0,return_inverse=True)
    triangle_indices=inverse.reshape(-1,3)
    edge_counts=Counter()
    for triangle in triangle_indices:
        for start,end in ((0,1),(1,2),(2,0)):
            edge_counts[tuple(sorted((int(triangle[start]),int(triangle[end]))))]+=1
    bad_edges=Counter(count for count in edge_counts.values() if count != 2)
    cross=np.cross(vertices[:,1]-vertices[:,0],vertices[:,2]-vertices[:,0])
    double_area=np.linalg.norm(cross,axis=1)
    nondegenerate=double_area>1e-18
    alignment=np.full(len(vertices),np.nan)
    alignment[nondegenerate]=np.einsum('ij,ij->i',normals[nondegenerate],cross[nondegenerate])/double_area[nondegenerate]
    tetra_volume=np.einsum('ij,ij->i',vertices[:,0],np.cross(vertices[:,1],vertices[:,2]))/6
    signed_volume=float(tetra_volume.sum())
    if abs(signed_volume) <= 1e-18:
        volume_centroid=[math.nan,math.nan,math.nan]
    else:
        tetra_centroid=vertices.sum(axis=1)/4
        volume_centroid=(tetra_volume[:,None]*tetra_centroid).sum(axis=0)/signed_volume
        volume_centroid=volume_centroid.tolist()
    rotations=[]
    for step in range(1,rotational_order):
        angle=2*math.pi*step/rotational_order
        matrix=np.array([[1,0,0],[0,math.cos(angle),-math.sin(angle)],
                         [0,math.sin(angle),math.cos(angle)]])
        rotations.append(dict(angle_deg=360*step/rotational_order,
                              **transform_statistics(points,vertices,matrix,tolerance_m)))
    mirror_y=np.diag([1,-1,1])
    integrity={
        'closed_two_manifold': not bad_edges,
        'bad_edge_incidence_counts': {str(key):value for key,value in sorted(bad_edges.items())},
        'degenerate_triangles': int(np.count_nonzero(~nondegenerate)),
        'stored_normals_match_winding': bool(np.all(alignment[nondegenerate]>.999)),
        'minimum_normal_winding_dot': float(np.nanmin(alignment)),
        'positive_signed_volume': signed_volume>0,
    }
    symmetry={
        'rotational_order_about_x': rotational_order,
        'rotations': rotations,
        'mirror_y': transform_statistics(points,vertices,mirror_y,tolerance_m),
        'lateral_volume_centroid_within_tolerance': bool(
            np.isfinite(volume_centroid[1:]).all()
            and max(abs(value) for value in volume_centroid[1:])<=tolerance_m
        ),
    }
    symmetry['screen_passed']=bool(
        all(item['screen_passed'] for item in rotations)
        and symmetry['mirror_y']['screen_passed']
        and symmetry['lateral_volume_centroid_within_tolerance']
    )
    return {
        'triangles': len(vertices),
        'unique_vertices': len(points),
        'bbox_min_m': flat.min(axis=0).tolist(),
        'bbox_max_m': flat.max(axis=0).tolist(),
        'signed_volume_m3': signed_volume,
        'volume_centroid_m': volume_centroid,
        'integrity': integrity,
        'symmetry': symmetry,
    }


def millimetres_to_metres(record: dict) -> float:
    if record.get('unit') != 'mm':
        raise ValueError(f"Expected millimetres, got {record.get('unit')!r}")
    return float(record['value'])*.001


def cad_statistics(path: Path,tolerance_m: float,rotational_order: int) -> dict:
    import cadquery as cq

    solid=cq.importers.importStep(str(path)).val()
    center=solid.Center()
    comparisons=[]
    for step in range(1,rotational_order):
        angle=360*step/rotational_order
        transformed=solid.rotate((0,0,0),(0,0,1),angle)
        difference=solid.cut(transformed).Volume()+transformed.cut(solid).Volume()
        comparisons.append({'angle_deg':angle,'symmetric_difference_mm3':difference})
    mirrored=solid.mirror('XZ')
    mirror_difference=solid.cut(mirrored).Volume()+mirrored.cut(solid).Volume()
    volume_tolerance_mm3=(tolerance_m*1000)**3
    lateral_tolerance_mm=tolerance_m*1000
    return {
        'valid': solid.isValid(),
        'solids': len(solid.Solids()),
        'faces': len(solid.Faces()),
        'edges': len(solid.Edges()),
        'volume_mm3': solid.Volume(),
        'volume_centroid_mm': list(center.toTuple()),
        'rotation_comparisons': comparisons,
        'mirror_y_symmetric_difference_mm3': mirror_difference,
        'symmetric_difference_tolerance_mm3': volume_tolerance_mm3,
        'screen_passed': bool(
            solid.isValid()
            and len(solid.Solids()) == 1
            and all(item['symmetric_difference_mm3']<=volume_tolerance_mm3
                    for item in comparisons)
            and mirror_difference<=volume_tolerance_mm3
            and abs(center.x)<=lateral_tolerance_mm
            and abs(center.y)<=lateral_tolerance_mm
        ),
    }


def audit(case: Path,rotational_order: int=3) -> dict:
    if rotational_order < 1:
        raise ValueError('Rotational order must be positive')
    case=case.resolve(strict=True)
    surface=case/'constant'/'triSurface'/'rocket.stl'
    spec=json.loads((case/'case-spec.json').read_text())
    inputs=json.loads((case/'resolved-inputs.json').read_text())
    tolerance=float(spec['mesh']['absolute_deflection_m'])
    normals,vertices=read_binary_stl(surface)
    result=surface_statistics(normals,vertices,tolerance,rotational_order)
    cad=cad_statistics(case/'external-mm.step',tolerance,rotational_order)
    geometry=inputs['geometry']
    expected_length=(millimetres_to_metres(geometry['nose_length'])
                     + millimetres_to_metres(geometry['body_length']))
    expected_diameter=millimetres_to_metres(geometry['body_od'])
    expected_area=math.pi*(expected_diameter/2)**2
    actual_length=result['bbox_max_m'][0]-result['bbox_min_m'][0]
    references={
        'expected_axial_length_m': expected_length,
        'surface_axial_length_m': actual_length,
        'axial_length_error_m': actual_length-expected_length,
        'expected_reference_length_m': expected_diameter,
        'case_reference_length_m': spec['reference_length_m'],
        'expected_reference_area_m2': expected_area,
        'case_reference_area_m2': spec['reference_area_m2'],
    }
    references['screen_passed']=bool(
        abs(references['axial_length_error_m'])<=tolerance
        and math.isclose(spec['reference_length_m'],expected_diameter,rel_tol=0,abs_tol=1e-12)
        and math.isclose(spec['reference_area_m2'],expected_area,rel_tol=0,abs_tol=1e-12)
    )
    result.update({
        'source_case': str(case),
        'surface_sha256': hashlib.sha256(surface.read_bytes()).hexdigest(),
        'tessellation_tolerance_m': tolerance,
        'cad_solid': cad,
        'stl_minus_cad_volume_mm3': result['signed_volume_m3']*1e9-cad['volume_mm3'],
        'reference_checks': references,
        'geometry_screen_passed': bool(
            all(result['integrity'][key] for key in (
                'closed_two_manifold','stored_normals_match_winding','positive_signed_volume'))
            and result['integrity']['degenerate_triangles'] == 0
            and result['symmetry']['screen_passed']
            and cad['screen_passed']
            and references['screen_passed']
        ),
        'accepted_for_design': False,
    })
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--rotational-order',type=int,default=3)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    result=audit(args.case,args.rotational_order)
    (args.output/'geometry-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({
        'geometry_screen_passed': result['geometry_screen_passed'],
        'integrity': result['integrity'],
        'cad_screen_passed': result['cad_solid']['screen_passed'],
        'symmetry_screen_passed': result['symmetry']['screen_passed'],
        'reference_screen_passed': result['reference_checks']['screen_passed'],
    }))


if __name__ == '__main__':
    main()
