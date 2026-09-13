"""Compare bounded commercial 24 mm cases in the current BT-60 passive logger."""
import argparse
import csv
import hashlib
import json
from argparse import Namespace
from collections import Counter
from pathlib import Path

from rocket_workbench.avionics import payload_budget
from rocket_workbench.cli import save_json, workflow
from rocket_workbench.config import Config, load_config, mass_cg
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine
from study_avionics import place_wadding

ROOT = Path(__file__).resolve().parents[1]
DIGESTS = {
    'C11': '4f0059c416964ba2528c83551e6a6839',
    'D12': 'ec683e131a2b32950561abfe011b0afc',
    'E12': '27575268e95ac6983801956efb389764',
}
# Exact delay-specific manufacturer limits, checked 2026-09-13.
LIMITS = {
    'C11': {3: 170, 5: 142},
    'D12': {3: 396, 5: 283, 7: 226},
    'E12': {4: 482, 6: 397, 8: 340},
}
PROFILES = {
    'nominal': dict(upper=False, printed_factor=1.0, mount_factor=1.0, extra_g=0),
    'upper-avionics': dict(upper=True, printed_factor=1.0, mount_factor=1.0, extra_g=0),
    'heavy-build': dict(upper=True, printed_factor=1.2, mount_factor=1.5, extra_g=0),
    'inert-plus20': dict(upper=False, printed_factor=1.0, mount_factor=1.0, extra_g=20),
    'inert-plus40': dict(upper=False, printed_factor=1.0, mount_factor=1.0, extra_g=40),
}
PLATFORMS = ('18-c5', '24-cd', '24-e')


def configuration(platform, profile):
    data = load_config(ROOT / 'examples/avionics-performance.yaml').model_dump()
    p = PROFILES[profile]
    data['name'] = f'bt60-{platform}-{profile}'
    source = '24 mm BT-60 comparison: provisional estimate, not measured commercial assembly'
    def setq(q, value, why=source):
        q.update(value=value, provenance='estimate', source=why)
    g = data['geometry']
    if platform != '18-c5':
        # Common long mount permits an E-length motor; CD version includes a removable spacer allowance.
        # Actual kit cut length, hook/block/ring positions and packing must be measured.
        for key, value in [('motor_mount_id', 24.1), ('motor_mount_od', 24.8), ('motor_mount_length', 95.0)]:
            setq(g[key], value)
        start = g['nose_length']['value'] + g['body_length']['value'] - 95 - g['motor_overhang']['value']
        assembly = [(12.0, start + 95/2)]
        if platform == '24-cd':
            # Motor aft face is at the airframe aft end. Short motor front is end-70.
            spacer_end = g['nose_length']['value'] + g['body_length']['value'] - 70
            assembly.append((1.0, spacer_end-25/2))
        mount_mass, mount_cg = mass_cg(assembly)
        mount = next(i for i in data['purchased_masses'] if i['role'] == 'mount')
        mount['name'] = 'Provisional commercial 24 mm mount assembly' + (' plus CD spacer' if platform == '24-cd' else '')
        setq(mount['mass'], mount_mass)
        setq(mount['x'], mount_cg)
        families = ['C11', 'D12'] if platform == '24-cd' else ['E12']
        data['motors'] = [
            dict(designation=family, delay_s=delay, digest=DIGESTS[family],
                 max_liftoff_mass=dict(value=limit, unit='g', provenance='manufacturer specification',
                     source=f'https://estesrockets.com/products/{family.lower()}-{delay}-engines ; checked 2026-09-13'))
            for family in families for delay, limit in LIMITS[family].items()
        ]
    else:
        data['motors'] = [m for m in data['motors'] if m['designation'] == 'C5']
    mount = next(i for i in data['purchased_masses'] if i['role'] == 'mount')
    if p['mount_factor'] != 1:
        setq(mount['mass'], mount['mass']['value'] * p['mount_factor'], 'Sensitivity: mount assembly mass +50%, same CG')
    if p['printed_factor'] != 1:
        setq(data['density'], data['density']['value'] * p['printed_factor'],
             'Mass-only sensitivity: modeled printed mass +20%; not a claim about PLA physical density')
    mass, cg = payload_budget(g['nose_length']['value'], p['upper'])
    setq(data['payload']['mass'], mass + p['extra_g'])
    setq(data['payload']['cg_x'], cg)
    if p['extra_g']:
        data['payload']['identity'] += f"; hypothetical {p['extra_g']} g inert payload at existing payload CG; packaging NOT modeled"
    for criterion in data['criteria']:
        if criterion['metric'] == 'apogee_m':
            criterion['maximum'] = None
            criterion['source'] = ('New motor comparison: report altitude without inherited 120 m ceiling; '
                                   'retain 30 m minimum. Site altitude clearance is unassessed.')
    data['launch']['wind_speeds'] = [dict(value=v, unit='m/s', provenance='estimate',
        source='Bounded constant-wind comparison; not a forecast') for v in [0, 2, 4]]
    place_wadding(data)
    return Config.model_validate(data)


def summarize(folder, platform, profile):
    data = json.loads((folder / 'results.json').read_text())
    groups = {}
    for case in data['cases']:
        motor = case['id'].split('-', 1)[1].rsplit('-wind', 1)[0]
        groups.setdefault(motor, []).append(case)
    rows = []
    for motor, cases in groups.items():
        loaded = [c for c in cases if c['loading'] == 'actual' and c['wind_m_s'] <= 2]
        def bounds(metric):
            values = [c.get('metrics', {}).get(metric) for c in loaded]
            return [min(values), max(values)] if len(values) == 2 and all(v is not None for v in values) else [None, None]
        failures = Counter(check['metric'] for c in cases for check in c['evaluation']['checks'] if check['passed'] is not True)
        passed = lambda c: c['execution'] == 'completed' and c['evaluation']['criteria_status'] == 'meets configured simulation criteria'
        row = dict(platform=platform, profile=profile, motor=motor, report=f'{folder.name}/report.md',
                   completed=sum(c['execution'] == 'completed' for c in cases), cases=len(cases),
                   pass_0_2=sum(passed(c) for c in cases if c['wind_m_s'] <= 2),
                   pass_0_2_4=sum(passed(c) for c in cases), failures=dict(failures),
                   loaded_dry_mass_g=loaded[0].get('mass', {}).get('dry_mass_g'),
                   loaded_launch_mass_g=loaded[0].get('mass', {}).get('launch_mass_g'))
        for metric in ['apogee_m', 'peak_powered_speed_m_s', 'guide_departure_m_s',
                       'minimum_ascent_stability_cal', 'deployment_speed_m_s', 'landing_descent_m_s',
                       'landing_displacement_m', 'peak_powered_specific_force_estimate_g']:
            row[metric] = bounds(metric)
        rows.append(row)
    return rows


def report(out, rows):
    def span(v):
        return 'unavailable' if None in v else f'{v[0]:.2f}–{v[1]:.2f}'
    lines = ['# Commercial 24 mm / BT-60 motor comparison', '',
        'Current 50 mm cone, 410 mm BT-60 body, 45 mm fins, 145 mm bay and 18-inch chute; passive logger only.',
        '405 flights: nine motor/delay cases × five mass scenarios × three loadings × three winds.',
        'Nominal/upper/heavy-build scenarios and hypothetical +20/+40 g payload sensitivity are distinct.',
        'Extra payload is mass-only at the existing payload CG: no additional hardware packaging or active-control claim.',
        'All numeric passes remain provisional. No site clearance, physical validation, motor purchase or new print-project approval.', '',
        '## Changed criterion and mount assumptions', '',
        'This NEW study removes only the inherited 120 m apogee maximum. The 30 m minimum and all guide, stability,',
        'deployment, descent and manufacturer mass limits remain. Historical study results are untouched.',
        'There is no assessed site altitude ceiling or drift boundary; numeric passes do not establish field suitability.',
        'The common long 24 mm mount is estimated at 12 g (18 g heavy-build), with an additional 1 g CD spacer',
        '(1.5 g heavy-build), at explicit axial CGs. Mount ID/OD/length are 24.1/24.8/95 mm, not measured kit dimensions.',
        'Heavy-build combines upper avionics, +20% print mass and +50% mount mass. It is not a full uncertainty sweep.',
        'Chute Cd, payload CG, guide and motor curves are otherwise fixed. The short-motor spacer is lumped in the mount',
        'mass/CG, not a separately modeled printable part. The long mount leaves a tight recovery-wadding gap.',
        'CAD fit checks cover existing avionics only, not the hypothetical extra payload.', '',
        '## Sources and motor identity', '',
        '[Commercial mount kit](https://estesrockets.com/products/d-and-e-engine-mount-kit).',
        'Curve digests, thrust/mass histories and engine versions are retained in each results.json.',
        'The bundled C11/D12/E12 curves derive from older NAR data, not measurements of current inventory;',
        'manufacturer advertised impulse/mass may differ. Do not substitute marketing impulse for the simulated curve.',
        '**E12 purchasing hold:** [manufacturer affected-lot bulletin](https://estesrockets.com/pages/e12-service-bulletin),',
        'lots 2K1 25336 00 and 2I3 25303 00; E12 is compared computationally, not recommended for purchase here.', '']
    for family, limits in LIMITS.items():
        for delay in limits:
            lines.append(f'- [{family}-{delay} manufacturer limit](https://estesrockets.com/products/{family.lower()}-{delay}-engines): {limits[delay]} g; checked 2026-09-13.')
    lines += ['', '## Loaded performance at winds 0/2 m/s', '',
        'Pass counts include empty/dummy/actual: six cases at winds 0/2, nine at winds 0/2/4. They are not probabilities.',
        'Dummy and actual use identical mass/CG. The mass-only growth allowance is absent from empty cases.', '',
        '| Mass scenario | Motor | Apogee m | Powered speed m/s | Guide m/s | Min stability cal | Deployment m/s | Descent m/s | Pass /6 | Pass /9 |',
        '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for r in rows:
        lines.append(f"| [{r['profile']}]({r['report']}) | {r['motor']} | " +
            ' | '.join(span(r[k]) for k in ['apogee_m', 'peak_powered_speed_m_s', 'guide_departure_m_s',
                'minimum_ascent_stability_cal', 'deployment_speed_m_s', 'landing_descent_m_s']) +
            f" | {r['pass_0_2']}/6 | {r['pass_0_2_4']}/9 |")
    lines += ['', '## Failure counts by metric', '']
    for r in rows:
        lines.append(f"- {r['profile']} / {r['motor']}: {r['failures'] or 'no numeric failures; inspect warnings and physical gates'}")
    lines += ['', '## Downloads', '', '[Machine-readable comparison](comparison.json) | [Flat comparison CSV](comparison.csv)',
              '', 'Each linked case report has corresponding config.yaml, results.json, results.csv, mass-ledger.json,',
              'cad/assembly.step and individual motor/load/wind ORK files in the same directory.', '']
    (out / 'report.md').write_text('\n'.join(lines))
    flat = [{k: (json.dumps(v) if isinstance(v, (dict, list)) else v) for k, v in r.items()} for r in rows]
    with (out / 'comparison.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(flat[0]))
        writer.writeheader()
        writer.writerows(flat)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    out = args.output
    out.mkdir(parents=True, exist_ok=False)
    save_json(out / 'search-spec.json', dict(platforms=PLATFORMS, mass_scenarios=PROFILES,
        manufacturer_limits_g=LIMITS, curve_digests=DIGESTS, winds_m_s=[0, 2, 4],
        expected_flights=405, inherited_apogee_maximum_removed=True,
        scope='Passive commercial single-stage comparison; no control hardware or physical validation'))
    rows = []
    with Engine() as engine:
        for profile in PROFILES:
            for platform in PLATFORMS:
                config = configuration(platform, profile)
                folder = out / config.name
                folder.mkdir()
                path = folder / 'config.yaml'
                save_json(path, config.model_dump())
                save_json(folder / 'resolved-inputs.json', config.model_dump())
                digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
                save_json(folder / 'manifest.json', dict(configuration_sha256=digest, command='motor24-study'))
                workflow(Namespace(command='simulate', strict=False), config, path, folder, digest, engine)
                rows.extend(summarize(folder, platform, profile))
                save_json(out / 'comparison.json', rows)
                print('PLATFORM COMPLETE', config.name, flush=True)
    report(out, rows)
    seal_run(out)
    print('STUDY COMPLETE', out, flush=True)


if __name__ == '__main__':
    main()
