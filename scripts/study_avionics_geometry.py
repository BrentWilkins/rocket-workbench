"""Bounded current-avionics geometry search; retain failures and Pareto tradeoffs."""
import argparse
import hashlib
import itertools
import json
from argparse import Namespace
from pathlib import Path

from rocket_workbench.avionics import payload_budget
from rocket_workbench.cli import save_json, workflow
from rocket_workbench.config import Config
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine
from study_avionics import avionics_config, place_wadding
from study_noses import candidate


def variant(shape, nose, body, span):
    base = candidate(avionics_config(), shape, nose)
    data = base.model_dump()
    data['name'] = f'{shape}-n{nose}-b{body}-f{span}'
    delta = body - base.geometry.mm('body_length')
    for key, value in [('body_length', body), ('fin_span', span)]:
        data['geometry'][key].update(value=value, provenance='estimate',
                                    source='Bounded current-avionics geometry study')
    for item in data['purchased_masses']:
        if item['role'] == 'body':
            item['mass']['value'] *= body / base.geometry.mm('body_length')
            item['x']['value'] += delta / 2
        elif item['role'] in ['mount', 'collar_adhesive']:
            item['x']['value'] += delta
        elif item['role'] == 'lugs':
            item['x']['value'] += .475 * delta
    # Recovery and electronics stay fixed relative to the nose shoulder.
    place_wadding(data)
    return Config.model_validate(data)


def summarize(folder):
    cases = json.loads((folder/'results.json').read_text())['cases']
    groups = {}
    for case in cases:
        key = case['id'].split('-', 1)[1].rsplit('-wind', 1)[0]
        groups.setdefault(key, []).append(case)
    rows = []
    for motor, group in groups.items():
        feasible = len(group) == 6 and all(c['execution'] == 'completed' and
            c['evaluation']['criteria_status'] == 'meets configured simulation criteria' for c in group)
        loaded = [c for c in group if c['loading'] == 'actual']
        def worst(metric):
            values = [c.get('metrics', {}).get(metric) for c in loaded]
            return min(values) if values and all(v is not None for v in values) else None
        rows.append(dict(design=folder.name, motor=motor, nominal_feasible=feasible,
                         apogee_m=worst('apogee_m'), speed_m_s=worst('peak_powered_speed_m_s'),
                         stability_cal=worst('minimum_ascent_stability_cal'),
                         completed=sum(c['execution']=='completed' for c in group), cases=len(group)))
    return rows


def pareto(rows):
    feasible = [r for r in rows if r['nominal_feasible']]
    keys = ['apogee_m', 'speed_m_s']
    return [r for r in feasible if not any(
        all(s[k] >= r[k] for k in keys) and any(s[k] > r[k] for k in keys)
        for s in feasible)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    out = args.output
    out.mkdir(parents=True, exist_ok=False)
    specification = dict(nose_shapes=['conical', 'ogive', 'ellipsoid'], nose_lengths_mm=[50,70,90],
                         body_lengths_mm=[410,440], fin_spans_mm=[45,50,55], maximum_designs=54,
                         payload_budget_g=payload_budget(50)[0], bay_length_mm=145,
                         objectives=['maximize worst-wind loaded apogee', 'maximize worst-wind loaded powered speed'],
                         constraints='All six nominal load/wind cases for a motor must meet existing gates; no physical eligibility',
                         limitations='Fixed tube, wall, fin chord/thickness, chute and sealed avionics layout; not global optimization. Ogive drag has an unresolved upstream modeling caveat.')
    save_json(out/'search-spec.json', specification)
    rows = []
    with Engine() as engine:
        for shape, nose, body, span in itertools.product(specification['nose_shapes'],
                specification['nose_lengths_mm'], specification['body_lengths_mm'], specification['fin_spans_mm']):
            config = variant(shape, nose, body, span)
            folder = out/config.name
            folder.mkdir()
            path = folder/'config.yaml'
            save_json(path, config.model_dump())
            save_json(folder/'resolved-inputs.json', config.model_dump())
            digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
            save_json(folder/'manifest.json', dict(configuration_sha256=digest, command='avionics-geometry'))
            workflow(Namespace(command='simulate', strict=False), config, path, folder, digest, engine)
            fit = json.loads((folder/'cad/avionics-fit.json').read_text())
            current = summarize(folder)
            for row in current:
                row['packaging_fit'] = fit['passed']
                row['nominal_feasible'] &= fit['passed']
            rows.extend(current)
            save_json(out/'comparison.json', rows)
            print(f'GEOMETRY COMPLETE {config.name}', flush=True)
    front = pareto(rows)
    save_json(out/'pareto.json', front)
    # Up to three distinct feasible designs: altitude, speed and stability leaders.
    finalists = []
    feasible = [r for r in rows if r['nominal_feasible']]
    for key in ['apogee_m', 'speed_m_s', 'stability_cal']:
        if feasible:
            best = max(feasible, key=lambda r:r[key])
            if best not in finalists:
                finalists.append(best)
    save_json(out/'finalists.json', finalists)
    lines = ['# Current-avionics bounded geometry comparison', '',
             '54 geometries, five motor/delay cases, three loadings, winds 0/2 m/s. Nominal component mass 20.65 g.',
             'Not a global optimum or flight clearance. Upper-mass and broader stress checks are separate.', '',
             '| Design | Motor | Nominal feasible | Worst loaded apogee m | Worst loaded powered speed m/s |',
             '| --- | --- | --- | --- | --- |']
    for r in rows:
        lines.append(f"| [{r['design']}]({r['design']}/report.md) | {r['motor']} | {r['nominal_feasible']} | {r['apogee_m']} | {r['speed_m_s']} |")
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(out)
    print('STUDY COMPLETE', out, flush=True)


if __name__ == '__main__':
    main()
