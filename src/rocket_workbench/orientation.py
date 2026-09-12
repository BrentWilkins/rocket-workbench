"""Geometric print-orientation screening, not adhesion or strength certification."""
import math

import numpy as np

ORIENTATIONS = {
    'forward-down': ((1, 0, 0), 0),
    'aft-down': ((1, 0, 0), 180),
    'side-x-plus': ((0, 1, 0), 90),
    'side-x-minus': ((0, 1, 0), -90),
    'side-y-plus': ((1, 0, 0), 90),
    'side-y-minus': ((1, 0, 0), -90),
}


def place(part, orientation):
    axis, angle = ORIENTATIONS[orientation]
    rotated = part.rotate((0, 0, 0), axis, angle)
    bb = rotated.val().BoundingBox()
    return rotated.translate((-(bb.xmin+bb.xmax)/2, -(bb.ymin+bb.ymax)/2, -bb.zmin))


def measure(part, layer=0.2, threshold=45):
    """Average material cross-section in first layer; downward mesh surface above it.

    Downward area does not account for bridging or supports growing from other
    surfaces. It is a screening proxy, never a support-volume prediction.
    """
    import cadquery as cq
    if layer <= 0 or not 0 < threshold < 90:
        raise ValueError('Invalid layer height or overhang angle')
    bb = part.val().BoundingBox()
    if abs(bb.zmin) > .001:
        raise ValueError('Part must be placed on Z=0 first')
    slab = cq.Workplane('XY', origin=(0, 0, layer/2)).box(bb.xlen+2, bb.ylen+2, layer)
    contact = part.intersect(slab).val().Volume()/layer
    verts, triangles = part.val().tessellate(.05, .1)
    vertices = np.array([v.toTuple() for v in verts])
    downward = 0.0
    for indices in triangles:
        tri = vertices[list(indices)]
        normal = np.cross(tri[1]-tri[0], tri[2]-tri[0])
        twice_area = np.linalg.norm(normal)
        if twice_area and normal[2]/twice_area < -math.cos(math.radians(threshold)) and tri[:, 2].mean() > layer+.001:
            downward += twice_area/2
    return dict(first_layer_average_area_mm2=contact, downward_area_above_first_layer_mm2=downward,
                height_mm=bb.zlen, width_mm=bb.xlen, depth_mm=bb.ylen,
                fits_usable_236mm_square=bb.xlen<=236 and bb.ylen<=236 and bb.zlen<=256,
                layer_mm=layer, overhang_threshold_deg=threshold)


def nondominated(rows):
    """Pareto screen: more initial contact, less height and downward area."""
    def costs(row):
        return (-row['first_layer_average_area_mm2'], row['height_mm'], row['downward_area_above_first_layer_mm2'])
    return [r for r in rows if not any(all(a<=b+1e-6 for a,b in zip(costs(o),costs(r)))
            and any(a<b-1e-6 for a,b in zip(costs(o),costs(r))) for o in rows)]
