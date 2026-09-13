"""Component-level provisional XIAO flight logger and static-port interface.

All dimensions are mm. Components are packaging keepouts, never printable parts.
Published PCB dimensions do not imply measured complete assemblies or masses.
"""
import math
from html import escape

XIAO = 'https://wiki.seeedstudio.com/XIAO_BLE/'
GPS = 'https://wiki.seeedstudio.com/get_start_l76k_gnss/'
BARO = 'https://github.com/adafruit/Adafruit-BMP5xx-Temperature-and-Pressure-Sensor-PCB'
BATTERY = 'https://www.adafruit.com/product/1317'


def components(config=None):
    # dims = transverse X, stack Y, rocket-axis Z; z offsets from nose shoulder.
    rows = [
        ('xiao-sense', 'Seeed XIAO nRF52840 Sense (not Plus)', [18, 5, 24.5], [0, -5, 38.25], 2.5, 3.2, XIAO,
         'Keepout includes USB overhang; board datum at shoulder+39 mm aligns GNSS header rows; mass estimated'),
        ('l76k', 'Seeed L76K XIAO GNSS SKU 109100021', [18, 5, 21], [0, 3, 39], 3.0, 4.0, GPS,
         'Published PCB 18 x 21; 5 mm height and mass estimated; soldered interboard spacing must be measured'),
        ('antenna', 'Included L76K active antenna, exact delivered variant unverified', [26, 26, 8], [0, 0, 12], 5.0, 8.0, GPS,
         'Conservative supported antenna envelope, not a vendor dimension; 100 mm supplied coax routed separately; measure delivered antenna'),
        ('battery', 'Adafruit 1317 protected 150 mAh 1S LiPo', [20.75, 5.8, 28.02], [0, -5, 73], 4.65, 5.5, BATTERY,
         'Published 19.75 x 26.02 x 3.8 mm, 4.65 g; keepout adds packaging clearance, not certified swelling allowance'),
        ('barometer', 'Adafruit BMP581 breakout 6407 rev B', [17.78, 5, 25.4], [0, 3, 73], 1.5, 2.0, BARO,
         'PCB outline from official Eagle board: 25.4 x 17.78; populated height and mass estimated'),
        ('battery-connector', 'Mated JST-PH 2-pin battery connector, provisional envelope', [8, 6, 10], [0, 0, 99], .7, 1.0, BATTERY,
         'Explicit disconnect/service envelope; verify chosen receptacle and latch access'),
        ('harness', 'Soldered headers, short signal wires and antenna coax routing', [4, 10, 90], [15, 0, 65], 1.8, 3.0, 'Engineering allowance',
         'Routing reserve includes battery lead/service loop; connector mass accounted separately'),
        ('retention', 'Insulating pads, ties, strain relief and sealing consumables', [4, 10, 60], [-15, 0, 52], 1.5, 2.5, 'Engineering allowance',
         'Allowance; printed sled accounted separately; no potting over pressure sensor'),
    ]
    result = [dict(id=i, identity=name, dimensions_mm=d, center_mm=c, mass_g=m,
                   upper_mass_g=upper, source=source, provenance=note)
              for i, name, d, c, m, upper, source, note in rows]
    if config is not None and config.bay_retention == 'm2-insert-trial-v1':
        for part in result:
            if part['id'] in ('harness', 'retention'):
                part['dimensions_mm'] = [10, 4, part['dimensions_mm'][2]]
                part['center_mm'] = [6 if part['id']=='harness' else -6, 10, part['center_mm'][2]]
                part['provenance'] += '; equal-volume routing trial for insert bosses; verify bends and service access'
    return result


def payload_budget(nose_length, upper=False):
    parts = components()
    key = 'upper_mass_g' if upper else 'mass_g'
    mass = sum(p[key] for p in parts)
    return mass, nose_length + sum(p[key]*p['center_mm'][2] for p in parts)/mass


def vent_interface(config):
    g = config.geometry
    return dict(count=3, diameter_mm=1.0, angles_deg=[0, 120, 240],
                shoulder_offset_mm=125.0, station_mm=g.mm('nose_length')+125,
                shoulder_distance_cal=125/g.mm('body_od'),
                seal_stations_mm=[g.mm('nose_length')+6, g.mm('nose_length')+132],
                seal_groove_depth_mm=.5, seal_groove_width_mm=1.3,
                source='Provisional three-port straight-body layout; bench lag/leak and aerodynamic bias tests required',
                sealing='Align paper and sleeve holes. Two circumferential seals close the sleeve-to-paper annulus; also seal bulkhead perimeter and fasteners. Seal sizing/friction must be measured.')


def cut_ports(part, config):
    import cadquery as cq
    v = vent_interface(config)
    for angle in v['angles_deg']:
        a = math.radians(angle)
        direction = cq.Vector(math.cos(a), math.sin(a), 0)
        cutter = cq.Solid.makeCylinder(v['diameter_mm']/2, config.geometry.mm('body_od'),
                                      cq.Vector(0, 0, v['station_mm']), direction)
        part = part.cut(cutter)
    return part


def keepouts(config):
    import cadquery as cq
    return {p['id']: cq.Workplane('XY').box(*p['dimensions_mm']).translate(
        (p['center_mm'][0], p['center_mm'][1], config.geometry.mm('nose_length')+p['center_mm'][2]))
            for p in components(config)}


def detail_models(config):
    """Original engineering approximations with identifiable PCB/component features.

    Each assembly stays inside its tested keepout. Component internals are visual
    approximations, not vendor manufacturing CAD or a source of mass estimates.
    """
    import cadquery as cq
    n = config.geometry.mm('nose_length')
    def box(d, c):
        return cq.Workplane('XY').box(*d).translate((c[0], c[1], n+c[2]))
    groups = {}
    def group(name, items):
        a = cq.Assembly(name=name)
        for index, (shape, color) in enumerate(items):
            a.add(shape, name=f'{name}-{index}', color=cq.Color({'silver':'#b8bcc2', 'ivory':'#fff1cb'}.get(color,color)))
        groups[name] = a
    group('xiao-sense', [
        (box([17.78,1.25,20.955], [0,-6.625,39]), 'green'),
        (box([12.6,2.7,10.6], [0,-4.4,40]), 'silver'),
        (box([8.94,3.8,7.3], [0,-4.7,30.9]), 'silver'),
    ])
    group('l76k', [
        (box([18,.8,21], [0,.9,39]), 'green'),
        (box([9.7,2.4,10.1], [0,2.5,39]), 'silver'),
        (box([3,2.5,3], [5.5,2.55,47]), 'gold'),
        (box([5,2,5], [-5,2.3,32]), 'gray'),
    ])
    group('barometer', [
        (box([17.78,1.6,25.4], [0,1.3,73]), 'blue'),
        (box([3.2,1.1,3.2], [0,2.65,73]), 'silver'),
        (box([.7,.1,.7], [0,3.25,73]), 'black'),
        (box([5,2.9,4], [0,3.5,63]), 'white'),
        (box([5,2.9,4], [0,3.5,83]), 'white'),
    ])
    group('antenna', [
        (box([25,25,1], [0,0,15.5]), 'green'),
        (box([20,20,5], [0,0,11.5]), 'ivory'),
    ])
    group('battery', [(box([19.75,3.8,26.02], [0,-5,73]), 'silver')])
    group('battery-connector', [(box([7,5,9], [0,0,99]), 'white')])
    return groups


def stack_pins(config):
    """Fourteen 2.54 mm-pitch soldered pins; PCB center datum, not bbox datum."""
    import cadquery as cq
    pins = cq.Assembly(name='soldered-interboard-pins')
    for side in [-1, 1]:
        for i in range(7):
            pin = cq.Workplane('XY').box(.64, 9, .64).translate(
                (side*7.62, -2.9, config.geometry.mm('nose_length')+39+(i-3)*2.54))
            pins.add(pin, name=f'pin-{side}-{i}', color=cq.Color('gold'))
            if i in [0,6]:
                # Insulating sleeve on four corner pins: support between PCB
                # surfaces, not against the GPS shield or the XIAO RF can.
                sleeve = cq.Workplane('XZ', origin=(side*7.62,.5,
                    config.geometry.mm('nose_length')+39+(i-3)*2.54)).circle(.95).circle(.45).extrude(6.5)
                pins.add(sleeve, name=f'spacer-{side}-{i}', color=cq.Color('white'))
    return pins


def fit_report(config, printed, *, hardware=None):
    """Check installed solids and the conservative straight insertion path."""
    import cadquery as cq
    hardware = keepouts(config) if hardware is None else hardware
    g = config.geometry
    radius = g.mm('body_id')/2-g.mm('clearance')-g.mm('wall')
    rows = []
    for name, part in hardware.items():
        b = part.val().BoundingBox()
        radial = radius-max(math.hypot(x,y) for x in [b.xmin,b.xmax] for y in [b.ymin,b.ymax])
        collision = sum(part.intersect(s).val().Volume() for s in printed.values())
        sweep = cq.Workplane('XY', origin=((b.xmin+b.xmax)/2,(b.ymin+b.ymax)/2,b.zmin)).rect(b.xlen,b.ylen).extrude(250)
        insertion_collision = sweep.intersect(printed['nose-bay']).val().Volume()
        rows.append(dict(component=name, radial_clearance_mm=radial,
                         installed_intersection_mm3=collision, insertion_intersection_mm3=insertion_collision))
    # Printed sleeve/bosses must also clear the purchased paper tube.
    tube = cq.Workplane('XY', origin=(0,0,g.mm('nose_length'))).circle(g.mm('body_od')/2).circle(g.mm('body_id')/2).extrude(g.mm('body_length'))
    tube_collision = printed['nose-bay'].intersect(tube).val().Volume()
    # Shelf encompasses the new rails in projection; the backplate/foot are
    # wider only on the negative-Y side. This is a conservative swept prism.
    z = printed['payload-sled'].val().BoundingBox().zmin
    sled_sweep = cq.Workplane('XY', origin=(0,0,z)).rect(26,26).extrude(250).union(
        cq.Workplane('XY', origin=(0,-8,z)).rect(28,8).extrude(250))
    omitted_sled = printed['payload-sled'].cut(sled_sweep).val().Volume()
    sled_collision = sled_sweep.intersect(printed['nose-bay']).val().Volume()
    passed = tube_collision < 1e-5 and sled_collision < 1e-5 and omitted_sled < 1e-5 and all(r['radial_clearance_mm'] > 0 and
        r['installed_intersection_mm3'] < 1e-5 and r['insertion_intersection_mm3'] < 1e-5 for r in rows)
    return dict(passed=passed, components=rows, sleeve_tube_intersection_mm3=tube_collision,
                sled_insertion_intersection_mm3=sled_collision, sled_outside_sweep_mm3=omitted_sled,
                minimum_component_radial_clearance_mm=min(r['radial_clearance_mm'] for r in rows),
                assumptions='Nominal solid geometry; compressed seals and flexible ties excluded from insertion sweep. Verify real friction and clearances.')


def layout_svg(config, path):
    """Dimensioned two-view packaging diagram, generated from the tested keepouts."""
    colors = ['#0072b2','#e69f00','#009e73','#cc79a7','#56b4e9','#d55e00','#666666','#333333']
    rows = components(config)
    items = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1050 430">',
             '<rect width="1050" height="430" fill="#ffffff"/>',
             '<style>text{font:14px sans-serif;fill:#152238} .small{font-size:12px}</style>',
             '<text x="20" y="25">AVIONICS PACKAGING — nominal dimensions, not measured hardware</text>']
    for axis, cy, title in [(0,115,'X–Z: transverse width / axial position'), (1,280,'Y–Z: stack thickness / axial position')]:
        items.append(f'<text x="30" y="{cy-68}">{title}</text>')
        items.append(f'<rect x="35" y="{cy-60.75}" width="435" height="121.5" fill="none" stroke="#555"/>')
        for index, (p,color) in enumerate(zip(rows, colors),1):
            d,c = p['dimensions_mm'],p['center_mm']
            x, y = 35+3*(c[2]-d[2]/2), cy-3*(c[axis]+d[axis]/2)
            items.append(f'<rect x="{x}" y="{y}" width="{3*d[2]}" height="{3*d[axis]}" fill="{color}" fill-opacity=".35" stroke="{color}"/>')
            items.append(f'<text class="small" x="{35+3*c[2]}" y="{cy-3*c[axis]+4}" text-anchor="middle">{index}</text>')
        items.append(f'<path d="M410 {cy-63}v126" stroke="#b00020" stroke-dasharray="5 3"/>')
        items.append(f'<text class="small" x="35" y="{cy+80}">Shoulder 0 mm → aft bulkhead 145 mm; dashed line: ports at 125 mm</text>')
    for index,(p,color) in enumerate(zip(rows,colors),1):
        items.append(f'<text x="510" y="{65+index*30}">{index}. {escape(p["id"])} — {p["mass_g"]:.2f} g</text>')
    items += ['<text x="510" y="345">Colors show component keepouts, not physical filled blocks.</text>',
              '<text x="510" y="370">3D detail and insertion checks are separate CAD artifacts.</text>',
              '<text x="30" y="415">Cable bends, restraint compression, seal friction and delivered antenna size need physical checks.</text>', '</svg>']
    path.write_text('\n'.join(items)+'\n')


def pressure_screen(config, speed_m_s=50):
    """Conservative empty-chamber volume, isothermal low-pressure-drop sizing screen.

    Sum Poiseuille passage loss and incompressible orifice loss. This is not CFD,
    an aerodynamic port-pressure model or validated transient response.
    """
    g = config.geometry
    radius = g.mm('body_id')/2-g.mm('clearance')-g.mm('wall')
    volume = (math.pi*radius**2*g.mm('bay_length') +
              math.pi*(g.mm('body_od')/2-g.mm('wall'))**2*(g.mm('nose_length')-2*g.mm('wall'))/3)*1e-9
    v = vent_interface(config)
    diameter, count = v['diameter_mm']*.001, v['count']
    length = (g.mm('wall')+(g.mm('body_od')-g.mm('body_id'))/2)*.001
    density, viscosity, temperature, cd = 1.225, 1.81e-5, 288.15, .6
    flow = volume*9.80665*speed_m_s/(287.05*temperature)
    area = count*math.pi*diameter**2/4
    viscous = 128*viscosity*length*flow/(count*math.pi*diameter**4)
    inertial = density/2*(flow/(cd*area))**2
    return dict(empty_volume_cm3=volume*1e6, speed_m_s=speed_m_s, port_area_mm2=area*1e6,
                pressure_lag_screen_pa=viscous+inertial,
                altitude_lag_screen_m=(viscous+inertial)/(density*9.80665),
                assumptions='Sea-level ISA, isothermal, Cd=0.6, smooth unobstructed ports; leakage and aerodynamic bias excluded')
