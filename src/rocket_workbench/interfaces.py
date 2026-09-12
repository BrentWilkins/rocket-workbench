"""Named v1 interfaces shared by CAD and flight geometry (millimetres).

These are provisional design dimensions, not measurements of purchased parts.
"""
from .config import Config


def launch_guide(config: Config) -> dict:
    g = config.geometry
    # Printed sleeves raise ordinary paper lugs clear of the widest collar.
    # 0.1 mm radial glue clearance around an assumed 4.6 mm OD paper lug.
    radius = max(4.0, g.mm('clearance') + g.mm('wall') + 1.5875 + .75)
    return dict(unit='mm', provenance='demonstration assumption',
                source='V1 sleeve interface; measure actual lugs/rod and test sliding clearance',
                sleeve_outer_radius=radius, sleeve_inner_radius=2.4,
                lug_inner_radius=1.8, lug_outer_radius=2.3, rod_radius=1.5875,
                length=25.0, angle_deg=60.0,
                center_radius=g.mm('body_od')/2 + radius,
                starts=[g.mm('nose_length') + f*g.mm('body_length') for f in [.3, .65]],
                collar_rod_gap=radius-1.5875-g.mm('clearance')-g.mm('wall'))
