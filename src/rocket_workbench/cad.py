"""CadQuery boundary. All CAD dimensions in mm, rocket axis +Z nose to tail."""
from __future__ import annotations

import json
import math
from pathlib import Path

from .config import Config
from .interfaces import launch_guide


def shapes(config: Config, *, cap_insert_angles=None):
    """Build production geometry, or an explicitly requested experimental insert layout.

    The optional layout is used only by the cap fit study. Normal exports and flight
    mass accounting retain the existing printed pilots until a revision is selected.
    """
    import cadquery as cq

    if cap_insert_angles is None and config.bay_retention == 'm2-insert-trial-v1':
        cap_insert_angles = [10, 170, 270]
    if cap_insert_angles is not None:
        if (not config.avionics_profile or len(cap_insert_angles) != 3
                or len(set(cap_insert_angles)) != 3
                or any(not math.isfinite(a) or not 0 <= a < 360 for a in cap_insert_angles)):
            raise ValueError('Experimental insert layout requires an avionics profile and three distinct angles')

    g = config.geometry
    n, b, w = g.mm('nose_length'), g.mm('bay_length'), g.mm('wall')
    r, ri = g.mm('body_od') / 2, g.mm('body_id') / 2 - g.mm('clearance')
    if config.nose_shape == 'conical':
        nose = cq.Workplane(obj=cq.Solid.makeCone(0.01, r, n))
        inner = cq.Solid.makeCone(0.01, r - w, n - 2 * w, cq.Vector(0, 0, 2 * w))
    else:
        from .nose import solid
        nose = solid(config.nose_shape, n, r)
        inner = solid(config.nose_shape, n-2*w, r-w).translate((0, 0, 2*w))
    nose = nose.cut(inner)
    sleeve = cq.Workplane('XY', origin=(0, 0, n)).circle(ri).circle(ri - w).extrude(b - 3)
    nose = nose.union(sleeve)
    boss_points = []
    for deg in ([30, 150, 270] if cap_insert_angles is None else cap_insert_angles):
        a = math.radians(deg)
        boss_offset = (1.7 if config.avionics_profile else 2.2) if cap_insert_angles is None else 3.1
        x, y = (ri - boss_offset) * math.cos(a), (ri - boss_offset) * math.sin(a)
        boss_points.append((x, y))
        boss_radius = (2.2 if config.avionics_profile else 2.8) if cap_insert_angles is None else 3.1
        boss = cq.Workplane('XY', origin=(x, y, n + b - 11)).circle(boss_radius).extrude(8)
        if config.avionics_profile:
            boss = boss.intersect(cq.Workplane('XY', origin=(0,0,n+b-11)).circle(ri).extrude(8))
        pilot_radius = .8 if cap_insert_angles is None else 1.1
        pilot = cq.Workplane('XY', origin=(x, y, n + b - 11)).circle(pilot_radius).extrude(8)
        if cap_insert_angles is not None:
            # TC-M2x3.0: 3.2 mm receiving hole, 3 mm insert plus 1 mm depth allowance.
            pilot = pilot.union(cq.Workplane('XY', origin=(x, y, n+b-7)).circle(1.6).extrude(4))
        nose = nose.union(boss).cut(pilot)
    cap = cq.Workplane('XY', origin=(0, 0, n + b - 3)).circle(ri).extrude(3)
    for x, y in boss_points + [(0, 0), (-10, -8), (10, -8)]:
        radius = 1.6 if (x, y) == (0, 0) else 1.1
        cap = cap.cut(cq.Workplane('XY', origin=(x, y, n+b-3)).circle(radius).extrude(3))
    width = 28 if config.avionics_profile else config.payload.width.value + 4
    sled = cq.Workplane('XY', origin=(0, -11, n+5)).rect(width, 2).extrude(b-8)
    foot = cq.Workplane('XY', origin=(0, -8, n+b-7)).rect(width, 8).extrude(4)
    sled = sled.union(foot)
    for x in [-10, 10]:
        sled = sled.cut(cq.Workplane('XY', origin=(x, -8, n+b-7)).circle(0.8).extrude(4))
    for z in [n+12, n+b-17]:
        for x in [-width/2+3, width/2-3]:
            sled = sled.cut(cq.Workplane('XY', origin=(x, -11, z)).box(3, 4, 3))
    if config.avionics_profile:
        from .avionics import cut_ports, vent_interface
        nose = cut_ports(nose, config)
        for station in vent_interface(config)['seal_stations_mm']:
            groove = cq.Workplane('XY', origin=(0, 0, station-.65)).circle(ri+.1).circle(ri-.5).extrude(1.3)
            nose = nose.cut(groove)
        # Lift the sled's forward end clear of the antenna. The transverse shelf
        # supports a separately tied patch antenna, not its fragile coax connector.
        sled = sled.cut(cq.Workplane('XY', origin=(0, 0, n)).box(60, 60, 34))
        shelf = cq.Workplane('XY', origin=(0, 0, n+18)).box(26, 26, 2)
        sled = sled.union(shelf)
        # Padded, separately strapped pockets. Rails carry side loads instead of
        # relying on soldered pins, the battery lead or antenna coax as restraints.
        for x in [-10.5, 10.5]:
            sled = sled.union(cq.Workplane('XY', origin=(x,-2.1,n+39)).box(1.6,16.2,26))
        for x in [-11.8, 11.8]:
            sled = sled.union(cq.Workplane('XY', origin=(x,-6.1,n+73)).box(2,8.2,32))
        for z in [n+56.5, n+89.5]:
            sled = sled.union(cq.Workplane('XY', origin=(0,-6.1,z)).box(25.6,8.2,1.6))
        for x in [-11, 11]:
            for z in [n+31, n+47, n+63, n+83]:
                sled = sled.cut(cq.Workplane('XY', origin=(x, -11, z)).box(3, 4, 3))
        for x in [-9, 9]:
            shelf_slot = cq.Workplane('XY', origin=(x, 0, n+18)).box(2, 6, 4)
            sled = sled.cut(shelf_slot)
        # Close aft ends of the two sled screw holes. Remaining cap/eye-bolt
        # penetrations need the specified sealing washers and perimeter seal.
        for x in [-10, 10]:
            cap = cap.union(cq.Workplane('XY', origin=(x, -8, n+b-1.2)).circle(1.1).extrude(1.2))
    collar_start = n + g.mm('body_length') - g.mm('collar_length')
    collar_inner = r + g.mm('clearance')
    collar_outer = collar_inner + w
    collar = cq.Workplane('XY', origin=(0, 0, collar_start)).circle(collar_outer).circle(collar_inner).extrude(g.mm('collar_length'))
    fairing_length = g.mm('fairing_length')
    fairing = cq.Workplane(obj=cq.Solid.makeCone(r, collar_outer, fairing_length,
                                               cq.Vector(0, 0, collar_start-fairing_length)))
    fairing = fairing.cut(cq.Workplane('XY', origin=(0, 0, collar_start-fairing_length)).circle(collar_inner).extrude(fairing_length))
    collar = collar.union(fairing)
    # XZ polygon, extruded symmetrically in Y. Roots overlap the collar wall.
    from .fins import outline
    points = outline(config)
    # Add hidden root overlap without changing the exposed aerodynamic outline.
    polygon = [(collar_outer-.3, collar_start)]
    polygon += [(collar_outer+y, collar_start+x) for x, y in points]
    polygon += [(collar_outer-.3, collar_start+g.mm('fin_root'))]
    if config.fin_shape == 'trapezoidal':
        # Preserve the historical trapezoid root-union construction and mass.
        polygon = [(collar_outer+y-(.3 if y == 0 else 0), collar_start+x) for x,y in points]
    fin = cq.Workplane('XZ').polyline(polygon).close().extrude(g.mm('fin_thickness')/2, both=True)
    if config.fin_profile == 'organic-v2':
        # Round the exposed leading and tip edges without softening the hidden
        # root. The aft edge is tapered separately instead of made half-round.
        exposed_edges = [
            edge for edge in fin.val().Edges()
            if edge.BoundingBox().ylen < 1e-6
            and edge.Center().x > collar_outer + .5
            and edge.Center().z < collar_start + g.mm('fin_root') - .5
        ]
        fin = fin.newObject(exposed_edges).fillet(g.mm('fin_thickness') / 2 - .1)

        # Taper the final 7 mm of chord to a printable 0.7 mm trailing edge.
        # These cuts are made before union with the collar, so its wall remains
        # intact behind the hidden fin root.
        trailing_z = collar_start + g.mm('fin_root')
        taper_length = 7.0
        edge_half = .35
        full_half = g.mm('fin_thickness') / 2
        radial_start = collar_outer - 1
        radial_length = g.mm('fin_span') + 3
        for side in (-1, 1):
            cut = (cq.Workplane('YZ', origin=(radial_start, 0, 0))
                   .moveTo(side * edge_half, trailing_z)
                   .lineTo(side * full_half, trailing_z - taper_length)
                   .lineTo(side * (full_half + 1), trailing_z - taper_length)
                   .lineTo(side * (full_half + 1), trailing_z)
                   .close().extrude(radial_length))
            fin = fin.cut(cut)

        # A variable-radius cove grows through the load-bearing middle of the
        # root and relaxes near both ends. It leaves the selected planform,
        # span, and sweep unchanged.
        def root_cove(side):
            wires = []
            stations = ((0, .8), (.12, 2.4), (.38, 3.0),
                        (.68, 3.0), (.88, 2.4), (1, .8))
            y0 = side * g.mm('fin_thickness') / 2
            for fraction, radius in stations:
                z = collar_start + fraction * g.mm('fin_root')
                # Solve the fillet circle tangent to both the cylindrical
                # collar and the planar fin side. The earlier tangent-plane
                # approximation touched the collar only at one line and left
                # a visible trough alongside the cove.
                y_center = y0 + side * radius
                x_center = math.sqrt((collar_outer + radius) ** 2 - y_center ** 2)
                tangent_angle = math.atan2(y_center, x_center)
                body_tangent = (
                    collar_outer * math.cos(tangent_angle),
                    collar_outer * math.sin(tangent_angle),
                )
                fillet_start_angle = tangent_angle + math.pi
                fin_tangent_angle = 3 * math.pi / 2 if side > 0 else math.pi / 2
                fillet_mid_angle = (fillet_start_angle + fin_tangent_angle) / 2
                fillet_mid = (
                    x_center + radius * math.cos(fillet_mid_angle),
                    y_center + radius * math.sin(fillet_mid_angle),
                )
                fin_tangent = (x_center, y0)
                # Extend the hidden side of the cove 0.2 mm into both solids.
                # The visible arc remains exactly tangent to the collar, while
                # the overlap prevents coincident-face seams in STL slicers.
                overlap_radius = collar_outer - .2
                root_inner_x = math.sqrt(overlap_radius ** 2 - y0 ** 2)
                body_inner = (
                    overlap_radius * math.cos(tangent_angle),
                    overlap_radius * math.sin(tangent_angle),
                )
                root_inner_angle = math.atan2(y0, root_inner_x)
                inner_mid_angle = (root_inner_angle + tangent_angle) / 2
                body_inner_mid = (
                    overlap_radius * math.cos(inner_mid_angle),
                    overlap_radius * math.sin(inner_mid_angle),
                )
                section = (cq.Workplane('XY', origin=(0, 0, z))
                           .moveTo(root_inner_x, y0)
                           .lineTo(*fin_tangent)
                           .threePointArc(fillet_mid, body_tangent)
                           .lineTo(*body_inner)
                           .threePointArc(body_inner_mid, (root_inner_x, y0))
                           .close())
                wires.append(section.wire().val())
            return cq.Workplane(obj=cq.Solid.makeLoft(wires, False))

        fin = fin.union(root_cove(-1)).union(root_cove(1))
    for angle in [0, 120, 240]:
        collar = collar.union(fin.rotate((0, 0, 0), (0, 0, 1), angle))
    parts = {'nose-bay': nose, 'bay-bulkhead': cap, 'payload-sled': sled, 'fin-collar': collar}
    guide = launch_guide(config)
    angle = math.radians(guide['angle_deg'])
    for index, z in enumerate(guide['starts']):
        # Build along +X, then rotate the complete mount. A concave pad replaces
        # the old tangential cylinder-to-paper joint without changing the rod axis.
        center = (guide['center_radius'], 0, z)
        sleeve = (cq.Workplane('XY', origin=center)
            .circle(guide['sleeve_outer_radius']).circle(guide['sleeve_inner_radius']).extrude(guide['length']))
        inner = guide['saddle_inner_radius']
        outer = inner + guide['saddle_thickness']
        pad = (cq.Workplane('XY', origin=(0, 0, z)).circle(outer).circle(inner).extrude(guide['length'])
               .intersect(cq.Workplane('XY', origin=(outer/2, 0, z+guide['length']/2))
                          .box(outer, guide['saddle_width'], guide['length'])))
        # Clear the bore again after union; changes to dimensions must not seal it.
        mount = sleeve.union(pad).cut(cq.Workplane('XY', origin=center)
                                      .circle(guide['sleeve_inner_radius']).extrude(guide['length']))
        # Trim every solid at the saddle radius, including the sleeve's former
        # tangent tip, for a continuous glue gap and no point contact with paper.
        mount = mount.cut(cq.Workplane('XY', origin=(0, 0, z)).circle(inner).extrude(guide['length']))
        parts[f'lug-sleeve-{index+1}'] = mount.rotate((0, 0, 0), (0, 0, 1), guide['angle_deg'])
    return parts


def build(config: Config, out: Path) -> dict:
    import cadquery as cq

    out.mkdir(parents=True, exist_ok=True)
    parts = shapes(config)
    records = {}
    assembly = cq.Assembly(name=config.name)
    colors = ['orange', 'gray', 'blue', 'red', 'gray', 'gray']
    for (name, part), color in zip(parts.items(), colors):
        shape = part.val()
        if not shape.isValid() or len(part.solids().vals()) != 1 or shape.Volume() <= 0:
            raise ValueError(f'Invalid or disconnected CAD solid: {name}')
        bb = shape.BoundingBox()
        center = shape.Center()
        records[name] = dict(volume_mm3=shape.Volume(), mass_g=shape.Volume()/1000*config.density.value,
                             cg_x_mm=center.z, bbox_mm=[bb.xlen, bb.ylen, bb.zlen],
                             provenance='estimate', source='CAD solid volume × configured density; verify print mass')
        if name in config.printed_measurements:
            mass, cg = config.printed_measurements[name]
            records[name].update(mass_g=mass.value, cg_x_mm=cg.value,
                                 provenance=mass.provenance, source=mass.source)
        cq.exporters.export(part, str(out / f'{name}.step'))
        # STLs laid on their minimum Z; assembly coordinates retained in STEP.
        printable = part
        if name in {'nose-bay', 'fin-collar'}:
            printable = part.rotate((0, 0, 0), (1, 0, 0), 180)
        elif name == 'payload-sled':
            printable = part.rotate((0, 0, 0), (1, 0, 0), 90)
        pbb = printable.val().BoundingBox()
        cq.exporters.export(printable.translate((0, 0, -pbb.zmin)), str(out / f'{name}.stl'), tolerance=0.05, angularTolerance=0.1)
        assembly.add(part, name=name, color=cq.Color(color))
    g = config.geometry
    tube = cq.Workplane('XY', origin=(0, 0, g.mm('nose_length'))).circle(g.mm('body_od')/2).circle(g.mm('body_id')/2).extrude(g.mm('body_length'))
    if config.avionics_profile:
        from .avionics import cut_ports, keepouts, components, vent_interface, pressure_screen
        tube = cut_ports(tube, config)
        hardware = cq.Assembly(name='avionics-keepouts-not-for-printing')
        for name, envelope in keepouts(config).items():
            hardware.add(envelope, name=name, color=cq.Color(0.2, 0.65, 0.6, 0.5))
        hardware.export(str(out/'avionics-keepouts.step'))
        assembly.add(hardware, name='avionics-not-for-printing')
        from .avionics import detail_models, stack_pins, fit_report, layout_svg
        detailed = cq.Assembly(name='engineering-avionics-approximation')
        for name, model in detail_models(config).items():
            detailed.add(model, name=name)
        detailed.add(stack_pins(config), name='stack-pins')
        detailed.export(str(out/'avionics-detailed.step'))
        installed = cq.Assembly(name='avionics-installed-section')
        installed.add(detailed, name='electronics-approximations')
        for name in ['nose-bay','payload-sled','bay-bulkhead']:
            installed.add(parts[name], name=name, color=cq.Color(.65,.7,.75,.25))
        installed.export(str(out/'avionics-installed.step'))
        checked_fit = fit_report(config, parts)
        if not checked_fit['passed']:
            raise ValueError(f'Avionics installed/insertion fit failed: {checked_fit}')
        (out/'avionics-fit.json').write_text(json.dumps(checked_fit, indent=2)+'\n')
        layout_svg(config, out/'avionics-layout.svg')
        for index, station in enumerate(vent_interface(config)['seal_stations_mm']):
            # Compressed rectangular seal envelope, not an elastomer manufacturing model.
            seal = cq.Workplane('XY', origin=(0, 0, station-.65)).circle(g.mm('body_id')/2).circle(
                g.mm('body_id')/2-g.mm('clearance')-.5).extrude(1.3)
            assembly.add(seal, name=f'purchased-seal-envelope-{index}', color=cq.Color('black'))
        (out/'avionics.json').write_text(json.dumps(dict(components=components(config),
            static_ports=vent_interface(config), pressure_screen=pressure_screen(config)), indent=2)+'\n')
    assembly.add(tube, name='purchased-BT60', color=cq.Color(0.65, 0.55, 0.35, 0.3))
    end = g.mm('nose_length')+g.mm('body_length')
    mount_start = end-g.mm('motor_mount_length')-g.mm('motor_overhang')
    mount = cq.Workplane('XY', origin=(0,0,mount_start)).circle(g.mm('motor_mount_od')/2).circle(g.mm('motor_mount_id')/2).extrude(g.mm('motor_mount_length'))
    assembly.add(mount, name='purchased-mount-envelope', color=cq.Color('gray'))
    for index, z in enumerate([mount_start+7, end-g.mm('motor_overhang')-5]):
        ring = cq.Workplane('XY', origin=(0,0,z)).circle(g.mm('body_id')/2).circle(g.mm('motor_mount_od')/2).extrude(2)
        assembly.add(ring,name=f'purchased-centering-ring-envelope-{index}',color=cq.Color('brown'))
    chute_start = config.mass_item('chute').x.value-g.mm('chute_packed_length')/2
    chute = cq.Workplane('XY', origin=(0,0,chute_start)).circle(g.mm('chute_packed_diameter')/2).extrude(g.mm('chute_packed_length'))
    assembly.add(chute,name='packing-envelope-not-a-print',color=cq.Color(0.2,0.8,0.3,0.4))
    guide = launch_guide(config)
    for index, z in enumerate(guide['starts']):
        angle = math.radians(guide['angle_deg'])
        center = (guide['center_radius']*math.cos(angle), guide['center_radius']*math.sin(angle), z)
        lug = (cq.Workplane('XY', origin=center).circle(guide['lug_outer_radius'])
               .circle(guide['lug_inner_radius']).extrude(guide['length']))
        assembly.add(lug, name=f'purchased-paper-lug-{index+1}', color=cq.Color('brown'))
    assembly.export(str(out / 'assembly.step'))
    interfaces = {'launch_guide': guide}
    if config.avionics_profile:
        from .avionics import vent_interface
        interfaces['static_ports'] = vent_interface(config)
    (out / 'interfaces.json').write_text(json.dumps(interfaces, indent=2)+'\n')
    (out / 'mass-properties.json').write_text(json.dumps(records, indent=2)+'\n')
    preview(config, out / 'assembly.svg')
    return records


def preview(config: Config, path: Path):
    from .nose import radius_at
    g = config.geometry
    n, length, r = g.mm('nose_length'), g.mm('body_length'), g.mm('body_od')/2
    end = n+length
    start = end-g.mm('collar_length')
    from .fins import outline as fin_outline
    fin_radius = r+g.mm('clearance')+g.mm('wall')
    fin_path = 'M'+' L'.join(f'{start+x:g} {-fin_radius-y:g}' for x,y in fin_outline(config))+' Z'
    top = [(n*i/100, -radius_at(config.nose_shape, n*i/100, n, r)) for i in range(101)]
    outline = top + [(x, -y) for x, y in reversed(top)]
    nose_outline = 'M' + ' L'.join(f'{x:g} {y:g}' for x, y in outline) + ' Z'
    path.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-30 -100 {end+90} 240">
<style>text{{font:9px sans-serif}} .label{{fill:#152238}}</style>
<rect x="-30" y="-100" width="{end+90}" height="240" fill="#f5f7fa"/>
<path d="{nose_outline}" fill="#ed9b40" stroke="#333"/>
<rect x="{n}" y="{-r}" width="{length}" height="{2*r}" fill="#d4bd95" fill-opacity="0.35" stroke="#333"/>
<rect x="{n}" y="{-r+2}" width="{g.mm('bay_length')}" height="{2*r-4}" fill="#4c9ad455" stroke="#4c9ad4"/>
<rect x="{n+g.mm('bay_length')+10}" y="-15" width="{g.mm('chute_packed_length')}" height="30" fill="#83b86c"/>
<rect x="{end-g.mm('motor_mount_length')-g.mm('motor_overhang')}" y="{-g.mm('motor_mount_od')/2}" width="{g.mm('motor_mount_length')}" height="{g.mm('motor_mount_od')}" fill="#888"/>
<path d="{fin_path}" fill="#ce6258" stroke="#333"/>
<text x="0" y="-78">PROVISIONAL — axial dimensions in mm; not a fabrication approval</text>
<text x="5" y="48">Printed nose</text><text x="{n}" y="65">Sealed removable bay / sled</text>
<text x="{n+80}" y="48">Chute + harness</text>
<path d="M{start-12} -53 H{start-28} V{-r-8} H{start+8}" fill="none" stroke="#526070" stroke-width="0.7"/>
<text x="{start-32}" y="-50" text-anchor="end">Printed fin collar</text>
<text x="{end-90}" y="65">Purchased motor mount</text>
<text x="0" y="105">Nose tip x=0 → aft x={end:g}; body OD {2*r:g}; length {length:g}</text></svg>''')
