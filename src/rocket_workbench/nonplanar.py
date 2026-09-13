"""Experimental passive geometry; not represented by native planar-fin aerodynamics."""


def ring_tail(config, collar, *, chord_mm=10., wall_mm=1.2):
    import cadquery as cq
    if config.fin_shape != 'clipped-delta':
        raise ValueError('Ring trial requires the clipped-delta tip attachment geometry')
    if not 5 <= chord_mm <= 12 or not 1.2 <= wall_mm <= 2.:
        raise ValueError('Ring trial exceeds bounded chord/wall range')
    g = config.geometry
    if g.mm('fin_root') != g.mm('collar_length'):
        raise ValueError('Ring trial requires coincident fin and collar aft ends')
    tip_radius = g.mm('body_od')/2 + g.mm('clearance') + g.mm('wall') + g.mm('fin_span')
    aft = g.mm('nose_length') + g.mm('body_length')
    # 0.3 mm radial overlap with all three fin tips. Real joint strength is unknown.
    inner = tip_radius - .3
    ring = cq.Workplane('XY', origin=(0,0,aft-chord_mm)).circle(inner+wall_mm).circle(inner).extrude(chord_mm)
    result = collar.union(ring)
    if not result.val().isValid() or len(result.solids().vals()) != 1:
        raise ValueError('Ring tail must be one valid connected solid')
    return result
