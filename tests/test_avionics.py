import math
import pytest

from rocket_workbench.avionics import components, payload_budget, pressure_screen, keepouts, vent_interface, detail_models, fit_report


def test_component_budget():
    parts = components()
    mass, cg = payload_budget(50)
    assert mass == pytest.approx(sum(p['mass_g'] for p in parts))
    assert cg == pytest.approx(50+sum(p['mass_g']*p['center_mm'][2] for p in parts)/mass)
    assert payload_budget(50, True)[0] > mass > 18
    assert all(p['source'] and p['provenance'] for p in parts)


@pytest.mark.integration
def test_avionics_fit_and_ports():
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
    from study_avionics import avionics_config
    from rocket_workbench.cad import shapes
    import cadquery as cq
    config = avionics_config()
    printed = shapes(config)
    proof = fit_report(config, printed)
    assert proof['passed']
    assert proof['sled_insertion_intersection_mm3'] < 1e-5
    assert proof['sled_outside_sweep_mm3'] < 1e-5
    assert proof['sleeve_tube_intersection_mm3'] < 1e-5
    assert proof['minimum_component_radial_clearance_mm'] == pytest.approx(.46522368915)
    hardware = keepouts(config)
    for name, detail in detail_models(config).items():
        a, b = detail.toCompound().BoundingBox(), hardware[name].val().BoundingBox()
        for axis in 'xyz':
            assert getattr(a, axis+'min') >= getattr(b, axis+'min')-1e-6, name
            assert getattr(a, axis+'max') <= getattr(b, axis+'max')+1e-6, name
    for part in printed.values():
        assert part.val().isValid() and len(part.solids().vals()) == 1
    radius = config.geometry.mm('body_id')/2-config.geometry.mm('clearance')-config.geometry.mm('wall')
    for name, part in hardware.items():
        b = part.val().BoundingBox()
        assert max(math.hypot(x,y) for x in [b.xmin,b.xmax] for y in [b.ymin,b.ymax]) < radius
        for solid in printed.values():
            assert part.intersect(solid).val().Volume() < 1e-5, name
    names = list(hardware)
    for i, name in enumerate(names):
        for other in names[i+1:]:
            assert hardware[name].intersect(hardware[other]).val().Volume() < 1e-5
    # Conservative straight axial insertion sweeps: each complete keepout must
    # pass the boss throat, not merely fit once installed.
    for name, part in hardware.items():
        b = part.val().BoundingBox()
        sweep = cq.Workplane('XY', origin=((b.xmin+b.xmax)/2,(b.ymin+b.ymax)/2,b.zmin)).rect(
            b.xlen,b.ylen).extrude(250)
        assert sweep.intersect(printed['nose-bay']).val().Volume() < 1e-5, name
    v = vent_interface(config)
    assert v['shoulder_distance_cal'] >= 3
    assert pressure_screen(config)['altitude_lag_screen_m'] < .1
    g = config.geometry
    chute = config.mass_item('chute').x.value
    assert chute-g.mm('chute_packed_length')/2 > g.mm('nose_length')+g.mm('bay_length')
    assert chute+g.mm('chute_packed_length')/2 < g.mm('nose_length')+g.mm('body_length')-g.mm('motor_mount_length')-g.mm('motor_overhang')
    for angle in v['angles_deg']:
        a = math.radians(angle)
        probe = cq.Workplane(obj=cq.Solid.makeCylinder(.45, 30,
            cq.Vector(0,0,v['station_mm']), cq.Vector(math.cos(a),math.sin(a),0)))
        assert probe.intersect(printed['nose-bay']).val().Volume() < 1e-5
    # Sled fasteners have blind aft ends, unlike the old through holes.
    for x in [-10, 10]:
        probe = cq.Workplane('XY', origin=(x, -8, g.mm('nose_length')+g.mm('bay_length')-.6)).box(.5,.5,.5)
        assert probe.intersect(printed['bay-bulkhead']).val().Volume() == pytest.approx(.125)
    # Both seal grooves remove the outer skin but retain a continuous inner wall.
    sleeve_radius = g.mm('body_id')/2-g.mm('clearance')
    for z in v['seal_stations_mm']:
        outer = cq.Workplane('XY', origin=(sleeve_radius-.2, 0, z)).box(.1,.1,.1)
        inner = cq.Workplane('XY', origin=(sleeve_radius-.8, 0, z)).box(.1,.1,.1)
        assert outer.intersect(printed['nose-bay']).val().Volume() < 1e-5
        assert inner.intersect(printed['nose-bay']).val().Volume() == pytest.approx(.001)
