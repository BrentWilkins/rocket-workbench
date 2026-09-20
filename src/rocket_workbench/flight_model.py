"""Write documented ORK XML, then validate/normalize with the pinned engine.

Exterior geometry uses native components. Each physical mass appears exactly
once: nose shell mass override, fins/collar own overrides, remaining mass items.
"""
import xml.etree.ElementTree as ET
from pathlib import Path

from .config import Config, mass_cg
from .interfaces import launch_guide

CONFIG_ID = '3eab299d-948a-4e87-92c4-c77466b59475'


def element(parent, tag, text=None, **attrs):
    node = ET.SubElement(parent, tag, attrs)
    if text is not None:
        node.text = str(text)
    return node


def component(parent, tag, name, mass=None, cg=None, **fields):
    node = element(parent, tag)
    element(node, 'name', name)
    if tag in {'nosecone', 'bodytube', 'transition', 'trapezoidfinset', 'freeformfinset', 'launchlug'}:
        element(node, 'finish', 'normal')
    if mass is not None:
        element(node, 'overridemass', mass/1000)
        element(node, 'overridesubcomponents', 'false')
    if cg is not None:
        element(node, 'overridecg', cg/1000)
    for key, value in fields.items():
        element(node, key, value)
    return node


def generate(config: Config, parts: dict, loading: str, out: Path):
    if loading not in ['empty', 'dummy', 'actual']:
        raise ValueError('Unsupported loading')
    g = config.geometry
    mm = g.mm
    n = mm('nose_length')
    root = ET.Element('openrocket', version='1.6', creator='Rocket Workbench 0.1')
    rocket = element(root, 'rocket')
    element(rocket, 'name', f'{config.name}-{loading}-PROVISIONAL')
    element(rocket, 'motorconfiguration', configid=CONFIG_ID, default='true')
    element(rocket, 'referencetype', 'custom')
    element(rocket, 'customreference', mm('body_od')/1000)
    stage = component(element(rocket, 'subcomponents'), 'stage', 'Sustainer')
    subs = element(stage, 'subcomponents')
    # Internal bay/cap/sled are accounted in one nose mass and CG override.
    front = [parts[k] for k in ['nose-bay', 'bay-bulkhead', 'payload-sled']]
    nose_mass, nose_cg = mass_cg([(p['mass_g'], p['cg_x_mm']) for p in front])
    component(subs, 'nosecone', 'Printed nose and bay assembly', nose_mass, nose_cg,
              shape=config.nose_shape, shapeparameter=1.0, length=n/1000, aftradius=mm('body_od')/2000,
              thickness=mm('wall')/1000, aftshoulderradius=(mm('body_id')/2-mm('clearance'))/1000,
              aftshoulderlength=mm('bay_length')/1000, aftshoulderthickness=mm('wall')/1000)
    # Tube ends at collar start in exterior model, but full purchased tube mass
    # lives here, with CG adjusted relative to this component's leading edge.
    tube_mass = config.mass_item('body')
    body = component(subs, 'bodytube', 'Purchased airframe', tube_mass.mass.value,
                     tube_mass.x.value-n, length=(mm('body_length')-mm('collar_length')-mm('fairing_length'))/1000,
                     radius=mm('body_od')/2000, thickness=(mm('body_od')-mm('body_id'))/2000)
    body_sub = element(body, 'subcomponents')
    collar_start = n+mm('body_length')-mm('collar_length')
    # Whole collar+fins mass assigned to collar; fin aero component overridden to
    # zero explicitly to prevent double-counting (known included mass, not unknown).
    collar_radius = mm('body_od')/2+mm('clearance')+mm('wall')
    component(subs, 'transition', 'Tapered collar fairing (mass included in collar)', 0,
              shape='conical', length=mm('fairing_length')/1000,
              foreradius=mm('body_od')/2000, aftradius=collar_radius/1000, thickness=mm('wall')/1000)
    collar = component(subs, 'bodytube', 'Printed collar including fin mass',
                       parts['fin-collar']['mass_g'], parts['fin-collar']['cg_x_mm']-collar_start,
                       length=mm('collar_length')/1000, radius=collar_radius/1000, thickness=mm('wall')/1000)
    collar_sub = element(collar, 'subcomponents')
    if config.fin_shape == 'trapezoidal':
        component(collar_sub, 'trapezoidfinset', f'{config.fin_count} fins (mass included in collar)', 0,
                  fincount=config.fin_count, rootchord=mm('fin_root')/1000, tipchord=mm('fin_tip')/1000,
                  height=mm('fin_span')/1000, sweeplength=mm('fin_sweep')/1000,
                  thickness=mm('fin_thickness')/1000, crosssection='square')
    else:
        from .fins import outline
        fins = component(collar_sub, 'freeformfinset', f'{config.fin_count} fins (mass included in collar)', 0,
                         fincount=config.fin_count, thickness=mm('fin_thickness')/1000, crosssection='square')
        points = element(fins, 'finpoints')
        for x, y in outline(config):
            element(points, 'point', x=str(x/1000), y=str(y/1000))
    # Native motor mount with explicitly accounted assembly mass in mass items.
    mount = component(body_sub, 'innertube', f"{config.motors[0].dimensions_mm[0]:g} mm motor mount", 0,
                      length=mm('motor_mount_length')/1000, outerradius=mm('motor_mount_od')/2000,
                      thickness=(mm('motor_mount_od')-mm('motor_mount_id'))/2000)
    element(mount, 'position', (mm('body_length')-mm('motor_mount_length')-mm('motor_overhang'))/1000, type='top')
    motor = element(mount, 'motormount')
    element(motor, 'ignitionevent', 'automatic')
    element(motor, 'overhang', mm('motor_overhang')/1000)
    m = element(motor, 'motor', configid=CONFIG_ID)
    first_motor = config.motors[0]
    for k, v in dict(type='single', manufacturer='Estes', designation=first_motor.designation,
                     digest=first_motor.digest, diameter=first_motor.dimensions_mm[0]/1000,
                     length=first_motor.dimensions_mm[1]/1000, delay=first_motor.delay_s).items():
        element(m, k, v)
    for item in config.purchased_masses:
        if item.role == 'body':
            continue
        if item.role == 'chute':
            chute = component(body_sub, 'parachute', item.name, item.mass.value, mm('chute_packed_length')/2,
                              diameter=mm('chute_diameter')/1000, cd=config.chute_cd.value,
                              deployevent='ejection', deploydelay=0,
                              packedlength=mm('chute_packed_length')/1000,
                              packedradius=mm('chute_packed_diameter')/2000,
                              linecount=6, linelength=.3)
            element(chute, 'position', (item.x.value-n-mm('chute_packed_length')/2)/1000, type='top')
        else:
            obj = component(body_sub, 'masscomponent', item.name, item.mass.value,
                            packedlength=.005, packedradius=.005)
            element(obj, 'position', (item.x.value-n)/1000, type='top')
            element(obj, 'overridecg', 0)
    # Native lug exterior represents sleeve + inserted paper lug. Internal glue
    # gap is irrelevant to exterior aero; printed sleeve AND saddle mass is counted here,
    # purchased paper/adhesive mass remains in the purchased ledger exactly once.
    # The saddle's noncylindrical aerodynamic contribution is NOT resolved by
    # this native lug surrogate. New runs must not imply drag validation.
    guide = launch_guide(config)
    for index, x in enumerate(guide['starts']):
        part = parts[f'lug-sleeve-{index+1}']
        lug = component(body_sub, 'launchlug', f'Launch lug and printed sleeve {index+1}',
                        part['mass_g'], part['cg_x_mm']-x,
                        length=guide['length']/1000, radius=guide['sleeve_outer_radius']/1000,
                        thickness=(guide['sleeve_outer_radius']-guide['lug_inner_radius'])/1000)
        element(lug, 'position', (x-n)/1000, type='top')
        element(lug, 'radialdirection', guide['angle_deg'])
    if loading != 'empty':
        payload = component(body_sub, 'masscomponent', f'{loading} payload', config.payload.mass.value,
                            packedlength=config.payload.length.value/1000,
                            packedradius=config.payload.width.value/2000)
        element(payload, 'position', (config.payload.cg_x.value-n)/1000, type='top')
        element(payload, 'overridecg', 0)
    ET.indent(root)
    out.write_bytes(ET.tostring(root, encoding='utf-8', xml_declaration=True))
    items = [(p['mass_g'], p['cg_x_mm']) for p in parts.values()]
    items += [(p.mass.value, p.x.value) for p in config.purchased_masses]
    if loading != 'empty':
        items.append((config.payload.mass.value, config.payload.cg_x.value))
    mass, cg = mass_cg(items)
    return dict(dry_mass_g=mass, dry_cg_x_mm=cg, loading=loading)
