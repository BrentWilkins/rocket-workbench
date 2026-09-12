"""CadQuery boundary. All CAD dimensions in mm, rocket axis +Z nose to tail."""
from __future__ import annotations

import json
import math
from pathlib import Path

from .config import Config
from .interfaces import launch_guide


def shapes(config: Config):
    import cadquery as cq

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
    for deg in [30, 150, 270]:
        a = math.radians(deg)
        x, y = (ri - 2.2) * math.cos(a), (ri - 2.2) * math.sin(a)
        boss_points.append((x, y))
        boss = cq.Workplane('XY', origin=(x, y, n + b - 11)).circle(2.8).extrude(8)
        pilot = cq.Workplane('XY', origin=(x, y, n + b - 11)).circle(0.8).extrude(8)
        nose = nose.union(boss).cut(pilot)
    cap = cq.Workplane('XY', origin=(0, 0, n + b - 3)).circle(ri).extrude(3)
    for x, y in boss_points + [(0, 0), (-10, -8), (10, -8)]:
        radius = 1.6 if (x, y) == (0, 0) else 1.1
        cap = cap.cut(cq.Workplane('XY', origin=(x, y, n+b-3)).circle(radius).extrude(3))
    width = config.payload.width.value + 4
    sled = cq.Workplane('XY', origin=(0, -11, n+5)).rect(width, 2).extrude(b-8)
    foot = cq.Workplane('XY', origin=(0, -8, n+b-7)).rect(width, 8).extrude(4)
    sled = sled.union(foot)
    for x in [-10, 10]:
        sled = sled.cut(cq.Workplane('XY', origin=(x, -8, n+b-7)).circle(0.8).extrude(4))
    for z in [n+12, n+b-17]:
        for x in [-width/2+3, width/2-3]:
            sled = sled.cut(cq.Workplane('XY', origin=(x, -11, z)).box(3, 4, 3))
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
    fin = (cq.Workplane('XZ').polyline([
        (collar_outer-0.3, collar_start),
        (collar_outer+g.mm('fin_span'), collar_start+g.mm('fin_sweep')),
        (collar_outer+g.mm('fin_span'), collar_start+g.mm('fin_sweep')+g.mm('fin_tip')),
        (collar_outer-0.3, collar_start+g.mm('fin_root')),
    ]).close().extrude(g.mm('fin_thickness')/2, both=True))
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
    (out / 'interfaces.json').write_text(json.dumps({'launch_guide': guide}, indent=2)+'\n')
    (out / 'mass-properties.json').write_text(json.dumps(records, indent=2)+'\n')
    preview(config, out / 'assembly.svg')
    return records


def preview(config: Config, path: Path):
    from .nose import radius_at
    g = config.geometry
    n, length, r = g.mm('nose_length'), g.mm('body_length'), g.mm('body_od')/2
    end = n+length
    start = end-g.mm('collar_length')
    span = g.mm('fin_span')
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
<path d="M{start} {-r} L{start+g.mm('fin_sweep')} {-r-span} L{start+g.mm('fin_sweep')+g.mm('fin_tip')} {-r-span} L{end} {-r} Z" fill="#ce6258" stroke="#333"/>
<text x="0" y="-78">PROVISIONAL — axial dimensions in mm; not a fabrication approval</text>
<text x="5" y="48">Printed nose</text><text x="{n}" y="65">Sealed removable bay / sled</text>
<text x="{n+80}" y="48">Chute + harness</text><text x="{start-10}" y="-68">Printed fin collar</text>
<text x="{end-90}" y="65">Purchased motor mount</text>
<text x="0" y="105">Nose tip x=0 → aft x={end:g}; body OD {2*r:g}; length {length:g}</text></svg>''')
