"""Component-level XIAO camera flight logger and static-port interface.

All dimensions are mm. Components are packaging keepouts, never printable parts.
Published PCB dimensions do not imply measured complete assemblies or masses.
"""
import math
from html import escape

XIAO = 'https://wiki.seeedstudio.com/xiao_esp32s3_sense/'
ACCEL = 'https://www.adafruit.com/product/4626'
BARO = 'https://www.adafruit.com/product/6067'
BATTERY = 'https://www.adafruit.com/product/3898'
CABLE = 'https://www.adafruit.com/product/261'
LEGACY_XIAO = 'https://wiki.seeedstudio.com/XIAO_BLE/'
LEGACY_GPS = 'https://wiki.seeedstudio.com/get_start_l76k_gnss/'
LEGACY_BARO = 'https://github.com/adafruit/Adafruit-BMP5xx-Temperature-and-Pressure-Sensor-PCB'
LEGACY_BATTERY = 'https://www.adafruit.com/product/1317'


def components(config=None):
    # dims = transverse X, stack Y, rocket-axis Z; z offsets from nose shoulder.
    rows = [
        ('xiao-sense', 'Seeed XIAO ESP32-S3 Sense camera + microSD recorder', [18, 7, 21], [0, -5, 39], 6.0, 6.5, XIAO,
         'User-weighed raw XIAO Sense with camera and WiFi antenna: 6 g; verify lens clearance and attachment mass'),
        ('lis331', 'Adafruit LIS331HH ±24 g accelerometer breakout', [25.6, 5, 22.7], [0, -5, 0], 2.0, 3.0, ACCEL,
         'STEMMA QT board envelope and populated height are provisional; use ±24 g range for powered flight'),
        ('barometer', 'Adafruit LPS28 breakout 6067', [17.8, 4.8, 25.4], [0, 3, 85], 1.8, 2.3, BARO,
         'Published 25.4 x 17.8 x 4.8 mm, 1.8 g; port and populated height still need fit measurement'),
        ('battery', 'Adafruit protected 3.7 V 400 mAh LiPo #3898', [17.5, 8.2, 37], [0, 5, 40], 8.2, 10.5, BATTERY,
         'Published battery choice is approximately 37 x 17.5 x 8.2 mm; opposite XIAO face, provisional clearance and retention'),
        ('battery-connector', 'JST-PH 2-pin mating pigtail, Adafruit #261', [8, 6, 10], [0, 5, 66], .5, .8, CABLE,
         'Solder the pigtail to XIAO BAT+/BAT− pads; verify mating gender and polarity before connection'),
        ('harness', 'Short sensor wires, camera/SD service loop and strain relief', [4, 10, 90], [15, 0, 65], 1.5, 2.5, 'Engineering allowance',
         'No GNSS coax in baseline; retain routing reserve for optional GPS'),
        ('retention', 'Insulating pads, ties, strain relief and sealing consumables', [4, 10, 60], [-15, 0, 52], 1.5, 2.5, 'Engineering allowance',
         'Allowance; printed sled accounted separately; no potting over pressure sensor'),
    ]
    if config is not None and config.avionics_profile == 'xiao-gnss-baro-v1':
        rows = [
            ('xiao-sense', 'Seeed XIAO nRF52840 Sense (not Plus)', [18, 5, 24.5], [0, -5, 38.25], 2.5, 3.2, LEGACY_XIAO,
             'Keepout includes USB overhang; board datum shoulder+39 mm aligns GNSS header rows; mass estimated'),
            ('l76k', 'Seeed L76K XIAO GNSS SKU 109100021', [18, 5, 21], [0, 3, 39], 3.0, 4.0, LEGACY_GPS,
             'Published PCB 18 x 21; 5 mm height and mass estimated; soldered interboard spacing must be measured'),
            ('antenna', 'Included L76K active antenna, exact delivered variant unverified', [26, 26, 8], [0, 0, 12], 5.0, 8.0, LEGACY_GPS,
             'Conservative supported antenna envelope, not vendor dimension; supplied coax routed separately'),
            ('battery', 'Adafruit 1317 protected 150 mAh 1S LiPo', [20.75, 5.8, 28.02], [0, -5, 73], 4.65, 5.5, LEGACY_BATTERY,
             'Published 19.75 x 26.02 x 3.8 mm, 4.65 g; keepout adds packaging clearance, not certified swelling allowance'),
            ('barometer', 'Adafruit BMP581 breakout 6407 rev B', [17.78, 5, 25.4], [0, 3, 73], 1.5, 2.0, LEGACY_BARO,
             'PCB outline official Eagle board: 25.4 x 17.78; populated height and mass estimated'),
            ('battery-connector', 'Mated JST-PH 2-pin battery connector, provisional envelope', [8, 6, 10], [0, 0, 99], .7, 1.0, LEGACY_BATTERY,
             'Explicit disconnect/service envelope; verify chosen receptacle latch access'),
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
                if config.avionics_profile == 'xiao-gnss-baro-v1':
                    part['dimensions_mm'] = [10, 4, part['dimensions_mm'][2]]
                    part['center_mm'] = [6 if part['id']=='harness' else -6, 10, part['center_mm'][2]]
                    part['provenance'] += '; equal-volume routing trial for insert bosses; verify bends and service access'
                else:
                    part['dimensions_mm'] = [4, 4, part['dimensions_mm'][2]]
                    part['center_mm'] = [12 if part['id']=='harness' else -12, 8, part['center_mm'][2]]
                    part['provenance'] += '; narrow side-channel routing trial for insert bosses; verify bends and service access'
    return result


def payload_budget(nose_length, upper=False, config=None):
    parts = components(config)
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
    if config.avionics_profile == 'xiao-gnss-baro-v1':
        # The retired GNSS profile has no maintained detailed PCB art. Keep its
        # CAD assembly truthful to that profile using labeled envelope solids.
        for part in components(config):
            if part['id'] in {'xiao-sense', 'l76k', 'antenna', 'battery', 'barometer', 'battery-connector'}:
                group(part['id'], [(box(part['dimensions_mm'], part['center_mm']), 'silver')])
        return groups
    group('xiao-sense', [
        (box([17.8,1.8,20.5], [0,-6.1,39]), 'green'),
        (box([12.6,3.0,10.6], [0,-4.5,40]), 'silver'),
        (box([8.9,4.0,7.3], [0,-4.4,32.2]), 'silver'),
    ])
    group('lis331', [
        (box([25.6,1.6,22.7], [0,-5.3,0]), 'blue'),
        (box([4.0,1.1,4.0], [0,-3.95,0]), 'silver'),
        (box([2.0,.2,2.0], [0,-3.3,0]), 'black'),
    ])
    group('barometer', [
        (box([17.8,1.6,25.4], [0,1.4,85]), 'blue'),
        (box([3.2,1.1,3.2], [0,2.65,85]), 'silver'),
        (box([.7,.1,.7], [0,3.25,85]), 'black'),
        (box([5,2.9,4], [0,3.5,75]), 'white'),
        (box([5,2.9,4], [0,3.5,95]), 'white'),
    ])
    group('battery', [(box([17.5,8.2,37], [0,5,40]), 'silver')])
    group('battery-connector', [(box([7,5,9], [0,5,66]), 'white')])
    return groups


def stack_pins(config):
    """Return a wiring placeholder; the camera board is not a stacked PCB."""
    import cadquery as cq
    return cq.Assembly(name='camera-sensor-wiring-placeholder')


def fit_report(config, printed, *, hardware=None):
    """Check installed solids and the conservative straight insertion path."""
    import cadquery as cq
    hardware = keepouts(config) if hardware is None else hardware
    component_intersections = []
    names = list(hardware)
    for index, name in enumerate(names):
        for other in names[index+1:]:
            volume = hardware[name].intersect(hardware[other]).val().Volume()
            if volume > 1e-5:
                component_intersections.append(dict(first=name, second=other, volume_mm3=volume))
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
    passed = not component_intersections and tube_collision < 1e-5 and sled_collision < 1e-5 and omitted_sled < 1e-5 and all(r['radial_clearance_mm'] > 0 and
        r['installed_intersection_mm3'] < 1e-5 and r['insertion_intersection_mm3'] < 1e-5 for r in rows)
    return dict(passed=passed, components=rows, component_intersections=component_intersections,
                sleeve_tube_intersection_mm3=tube_collision,
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
