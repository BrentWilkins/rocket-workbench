"""Screen a literature-characterized chute; hardware and packing remain unverified."""
import argparse
import hashlib
import json
from argparse import Namespace
from pathlib import Path

from rocket_workbench.cli import save_json, workflow
from rocket_workbench.config import Config
from rocket_workbench.progression import summarize_cases
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine
from study_fin_recovery import configuration as recovery_configuration

SOURCE = 'https://www.apogeerockets.com/Peak-of-Flight/Newsletter662'


def configuration(heavy, cd, insert_trial=False):
    data = recovery_configuration(24, 500, heavy).model_dump()
    data['name'] = f'apogee24-body500-heavy{int(heavy)}-cd{round(cd*100):03d}'
    chute = next(p for p in data['purchased_masses'] if p['role'] == 'chute')
    chute['name'] = 'Apogee 29093 24-inch nylon chute; literature specimen, not weighed hardware'
    chute['mass'].update(value=16.9 * (1.2 if heavy else 1), provenance='estimate',
                         source=SOURCE+'; 16.9 g reported specimen; upper +20% engineering allowance')
    data['chute_cd'].update(value=cd, provenance='estimate',
                            source=SOURCE+'; empirical .53–1.04 using circular area at flat-to-flat diameter')
    if insert_trial:
        data['name'] += '-insert-trial'
        data['bay_retention'] = 'm2-insert-trial-v1'
        hardware = next(p for p in data['purchased_masses'] if p['role']=='bay_hardware')
        # Additional allowance, not a claim of measured insert/screw mass. Preserve existing eye/seal budget.
        extra = 1.4 if heavy else .7
        mass = hardware['mass']['value']
        station = data['geometry']['nose_length']['value']+data['geometry']['bay_length']['value']-5
        hardware['x'].update(value=(mass*hardware['x']['value']+extra*station)/(mass+extra),
                             provenance='estimate',source='Existing hardware plus insert-joint allowance at aft bay')
        hardware['mass'].update(value=mass+extra,provenance='estimate',
                                source='Additional 0.7/1.4 g insert-joint allowance; weigh complete joint before flight')
    # Retain conservative generic 24-inch packing envelope and body. Lower mass does not prove tighter packing.
    return Config.model_validate(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--insert-trial', action='store_true')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    save_json(args.output/'search-spec.json', dict(source=SOURCE, flights=36, mass_g=[16.9,20.28],
        chute_cd=[.53,1.04], body_mm=500, packing='Unchanged generic 24-inch envelope; not measured',
        insert_trial=args.insert_trial,
        scope='Two mass profiles and two chute drag bounds, not a replacement for full uncertainty coverage'))
    rows = []
    with Engine() as engine:
        for heavy in (False, True):
            for cd in (.53, 1.04):
                config = configuration(heavy, cd, args.insert_trial)
                folder = args.output/config.name
                folder.mkdir()
                path = folder/'config.yaml'
                save_json(path, config.model_dump())
                save_json(folder/'resolved-inputs.json', config.model_dump())
                digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
                save_json(folder/'manifest.json', dict(configuration_sha256=digest, command='sourced-chute-screen'))
                workflow(Namespace(command='simulate', strict=False), config, path, folder, digest, engine)
                cases = json.loads((folder/'results.json').read_text())['cases']
                row = dict(design=config.name, summary=summarize_cases(cases))
                for metric in ('apogee_m', 'peak_powered_speed_m_s', 'landing_descent_m_s', 'landing_displacement_m'):
                    values = [c.get('metrics', {}).get(metric) for c in cases if c['loading']=='actual']
                    row[metric] = [min(values), max(values)] if all(v is not None for v in values) else None
                rows.append(row)
                save_json(args.output/'comparison.json', rows)
                print(config.name, row['summary']['planned'], flush=True)
    lines = ['# Literature-characterized 24-inch recovery screen', '',
             'Reported specimen mass and drag range are not measurements of our eventual hardware. '
             'Packing remains provisional. No production selection or physical validation.', '',
             '| Case | Planned passes / 6 | Loaded apogee m | Loaded descent m/s |', '| --- | --- | --- | --- |']
    for row in rows:
        lines.append(f"| [{row['design']}]({row['design']}/report.md) | {row['summary']['planned']['passed']} | "
                     f"{row['apogee_m']} | {row['landing_descent_m_s']} |")
    lines += ['', f'[Primary flight-test report]({SOURCE})']
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__ == '__main__':
    main()
