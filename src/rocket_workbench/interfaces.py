"""Named v1 interfaces shared by CAD and flight geometry (millimetres).

These are provisional design dimensions, not measurements of purchased parts.
"""
import math

from .config import Config


def launch_guide(config: Config) -> dict:
    g = config.geometry
    # Printed sleeves raise ordinary paper lugs clear of the widest collar.
    # 0.1 mm radial glue clearance around an assumed 4.6 mm OD paper lug.
    radius = max(4.0, g.mm('clearance') + g.mm('wall') + 1.5875 + .75)
    return dict(unit='mm', provenance='demonstration assumption',
                source='V2 curved saddle interface; measure tube/lugs/rod and test bonds and sliding clearance',
                sleeve_outer_radius=radius, sleeve_inner_radius=2.4,
                lug_inner_radius=1.8, lug_outer_radius=2.3, rod_radius=1.5875,
                length=25.0, angle_deg=60.0,
                center_radius=g.mm('body_od')/2 + radius,
                saddle_inner_radius=g.mm('body_od')/2 + .15,
                saddle_thickness=1.2, saddle_width=12.0, saddle_glue_gap=.15,
                saddle_bond_area_mm2=2*(g.mm('body_od')/2+.15)*math.asin(6/(g.mm('body_od')/2+.15))*25,
                aero_note='Native launchlug models cylindrical sleeve only; saddle mass included, saddle drag unresolved',
                starts=[g.mm('nose_length') + f*g.mm('body_length') for f in [.3, .65]],
                collar_rod_gap=radius-1.5875-g.mm('clearance')-g.mm('wall'))
