"""Build component-level avionics variant and retain nominal/upper-mass flights."""
import hashlib
import argparse
import json
from argparse import Namespace
from datetime import datetime, timezone
from pathlib import Path

from rocket_workbench.avionics import payload_budget, components, pressure_screen
from rocket_workbench.cli import workflow, save_json
from rocket_workbench.config import Config, load_config
from rocket_workbench.simulator import Engine
from study_noses import candidate

ROOT = Path(__file__).resolve().parents[1]


def place_wadding(data):
    """Place the provisional 10 mm axial wadding allowance between chute and mount."""
    g = data['geometry']
    mass = {p['role']: p for p in data['purchased_masses']}
    chute_end = mass['chute']['x']['value'] + g['chute_packed_length']['value']/2
    mount_start = (g['nose_length']['value']+g['body_length']['value']
                   -g['motor_mount_length']['value']-g['motor_overhang']['value'])
    if mount_start-chute_end < 10:
        raise ValueError('Recovery wadding allowance does not fit between packed chute and mount')
    mass['wadding']['x'].update(value=(chute_end+mount_start)/2, provenance='estimate',
        source='Provisional 10 mm axial wadding allowance between recovery pack and motor mount; verify physical packing')


def avionics_config(upper=False):
    base = candidate(load_config(ROOT/'examples/candidate-recovery.yaml'), 'conical', 50)
    data = base.model_dump()
    data['name'] = 'avionics-upper-mass' if upper else 'avionics-nominal'
    data['avionics_profile'] = 'xiao-gnss-baro-v1'
    source = 'Provisional avionics packaging/pressure-port variant; verify physical fit and pressure response'
    def setq(q, value):
        q.update(value=value, provenance='estimate', source=source)
    setq(data['geometry']['bay_length'], 145)
    setq(data['geometry']['body_length'], 410)
    mass, cg = payload_budget(50, upper)
    p = data['payload']
    p.update(identity='XIAO nRF52840 Sense + L76K + BMP581; provisional component budget',
             battery_identity='Adafruit 1317 150 mAh 1S LiPo; not yet purchased or measured')
    for key, value in dict(length=110, width=34, height=26, mass=mass, cg_x=cg).items():
        setq(p[key], value)
    # Move recovery pack aft of the extended bay; motor stays at the aft end.
    # Body mass scales with length. Other purchased masses remain explicit estimates.
    for item in data['purchased_masses']:
        role = item['role']
        if role == 'body':
            setq(item['mass'], item['mass']['value']*410/380)
            setq(item['x'], 50+410/2)
        elif role == 'mount':
            setq(item['x'], item['x']['value']+30)
        elif role in ['chute', 'harness']:
            setq(item['x'], item['x']['value']+80)
        elif role in ['bay_hardware', 'thermal']:
            setq(item['x'], item['x']['value']+80)
        elif role == 'collar_adhesive':
            setq(item['x'], item['x']['value']+30)
        elif role == 'lugs':
            setq(item['x'], item['x']['value']+.475*30)
    place_wadding(data)
    return Config.model_validate(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-config', type=Path, help='Use a selected geometry instead of the original avionics baseline')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    out = args.output or ROOT/'runs'/('avionics-study-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    out.mkdir()
    summary = []
    with Engine() as engine:
        for upper in [False, True]:
            config = avionics_config(upper)
            if args.base_config:
                data = load_config(args.base_config).model_dump()
                data['name'] = config.name
                mass, cg = payload_budget(data['geometry']['nose_length']['value'], upper)
                data['payload']['mass']['value'] = mass
                data['payload']['cg_x']['value'] = cg
                config = Config.model_validate(data)
            folder = out/config.name
            folder.mkdir()
            path = folder/'config.yaml'
            save_json(path, config.model_dump())
            save_json(folder/'resolved-inputs.json', config.model_dump())
            digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
            save_json(folder/'manifest.json', dict(configuration_sha256=digest, command='avionics-study'))
            workflow(Namespace(command='simulate', strict=False), config, path, folder, digest, engine)
            data = json.loads((folder/'results.json').read_text())
            for c in data['cases']:
                summary.append(dict(variant=config.name, case=c['id'], execution=c['execution'],
                    evaluation=c['evaluation'], metrics=c.get('metrics', {})))
    save_json(out/'comparison.json', summary)
    save_json(out/'components.json', dict(components=components(),
        nominal_payload_g=payload_budget(50)[0], upper_payload_g=payload_budget(50, True)[0],
        pressure_screen=pressure_screen(avionics_config())))
    lines = ['# Component-level avionics comparison', '',
        'Provisional parts/masses, no hardware validation. All failed cases retained.', '',
        '[Nominal report](avionics-nominal/report.md) | [Upper-mass report](avionics-upper-mass/report.md)', '',
        '| Variant / C5 case | Apogee m | Guide m/s | Estimated load g | Criteria |',
        '|---|---:|---:|---:|---|']
    for row in summary:
        if 'C5' not in row['case']:
            continue
        m = row['metrics']
        lines.append(f"| {row['variant']} / {row['case']} | {m['apogee_m']:.2f} | {m['guide_departure_m_s']:.2f} | {m['peak_powered_specific_force_estimate_g']:.2f} | {row['evaluation']['criteria_status']} |")
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    from rocket_workbench.provenance import seal_run
    seal_run(out)
    print(out, flush=True)


if __name__ == '__main__':
    main()
