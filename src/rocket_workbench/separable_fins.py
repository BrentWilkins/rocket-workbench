"""Plain collar and one detachable fin for manual assembly and root fillets."""

from __future__ import annotations

import cadquery as cq

from .config import Config


def parts(config: Config) -> tuple[cq.Workplane, cq.Workplane]:
    g = config.geometry
    body_radius = g.mm('body_od') / 2
    inner_radius = body_radius + g.mm('clearance')
    outer_radius = inner_radius + g.mm('wall')
    collar_start = g.mm('nose_length') + g.mm('body_length') - g.mm('collar_length')
    collar_length = g.mm('collar_length')
    fairing_length = g.mm('fairing_length')

    collar = (cq.Workplane('XY', origin=(0, 0, collar_start))
              .circle(outer_radius).circle(inner_radius).extrude(collar_length))
    fairing = cq.Workplane(obj=cq.Solid.makeCone(
        body_radius, outer_radius, fairing_length,
        cq.Vector(0, 0, collar_start - fairing_length)))
    fairing = fairing.cut(cq.Workplane(
        'XY', origin=(0, 0, collar_start - fairing_length))
        .circle(inner_radius).extrude(fairing_length))
    collar = collar.union(fairing)

    # One plain, full-thickness fin. Its flat root is tangent to the round
    # collar; the maximum geometric edge gap over the 2 mm thickness is tiny
    # and can be filled by the user's manual adhesive fillet.
    span = g.mm('fin_span')
    root = g.mm('fin_root')
    front = collar_start + 2.0
    aft = collar_start + root
    leading_tip = collar_start + .8 * root
    outline = [(outer_radius, front), (outer_radius + span, leading_tip),
               (outer_radius + span, aft), (outer_radius, aft)]
    fin = cq.Workplane('XZ').polyline(outline).close().extrude(
        g.mm('fin_thickness') / 2, both=True)
    return collar, fin


def printable_parts(config: Config) -> tuple[cq.Workplane, cq.Workplane]:
    collar, fin = parts(config)
    collar = collar.rotate((0, 0, 0), (1, 0, 0), 180)
    fin = fin.rotate((0, 0, 0), (1, 0, 0), 90)
    collar = collar.translate((0, 0, -collar.val().BoundingBox().zmin))
    fin = fin.translate((0, 0, -fin.val().BoundingBox().zmin))
    return collar, fin
