"""Shared exposed fin outline: axial-aft x, radial-out y, in millimetres.

Curves are explicitly polygonal in both CAD and the native freeform flight model.
No airfoil, fillet, or nonplanar aerodynamic equivalence is implied.
"""
import math


def outline(config):
    g = config.geometry
    root, span = g.mm('fin_root'), g.mm('fin_span')
    if config.fin_shape == 'elliptical':
        return [(root*(1-math.cos(math.pi*i/64))/2,
                 span*math.sin(math.pi*i/64) if i not in (0, 64) else 0.0)
                for i in range(65)]
    if config.fin_shape == 'clipped-delta':
        return [(0., 0.), (.8*root, span), (root, span), (root, 0.)]
    if config.fin_shape == 'swept':
        return [(0., 0.), (.65*root, span), (.95*root, span), (root, 0.)]
    return [(0., 0.), (g.mm('fin_sweep'), span),
            (g.mm('fin_sweep')+g.mm('fin_tip'), span), (root, 0.)]


def area_mm2(points):
    return abs(sum(x*v-u*y for (x,y),(u,v) in zip(points, points[1:]+points[:1])))/2
