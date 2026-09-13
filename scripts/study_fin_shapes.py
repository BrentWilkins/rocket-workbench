"""Bounded equal-area passive D12-5 fin-planform screen, with every case retained."""
import argparse
import hashlib
import itertools
import json
from argparse import Namespace
from pathlib import Path

from rocket_workbench.cli import save_json, workflow
from rocket_workbench.config import Config
from rocket_workbench.fins import outline, area_mm2
from rocket_workbench.progression import summarize_cases, dummy_targets
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine
from study_motor24 import configuration
from study_avionics import place_wadding

SHAPES = ['trapezoidal', 'elliptical', 'clipped-delta', 'swept']


def variant(shape, area_span, body):
    base = configuration('24-cd', 'nominal')
    data = base.model_dump()
    data['name'] = f'{shape}-a{area_span}-b{body}'
    data['motors'] = [m for m in data['motors'] if m['designation']=='D12' and m['delay_s']==5]
    data['geometry']['fin_span']['value'] = area_span
    reference = Config.model_validate(data)
    target_area = area_mm2(outline(reference))
    data['fin_shape'] = shape
    provisional = Config.model_validate(data)
    data['geometry']['fin_span']['value'] *= target_area/area_mm2(outline(provisional))
    delta = body-base.geometry.mm('body_length')
    data['geometry']['body_length']['value'] = body
    for key in ['fin_span', 'body_length']:
        data['geometry'][key].update(provenance='estimate', source='Bounded equal-area fin-shape study')
    for item in data['purchased_masses']:
        if item['role']=='body':
            item['mass']['value'] *= body/base.geometry.mm('body_length')
            item['x']['value'] += delta/2
        elif item['role'] in ['mount', 'collar_adhesive']:
            item['x']['value'] += delta
        elif item['role']=='lugs':
            item['x']['value'] += .475*delta
    place_wadding(data)
    return Config.model_validate(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    out = args.output
    out.mkdir(parents=True, exist_ok=False)
    save_json(out/'search-spec.json', dict(shapes=SHAPES, area_reference_spans_mm=[45,55],
        body_lengths_mm=[410,430], designs=16, flights=144, motor='D12-5', winds_m_s=[0,2,4],
        planned=['dummy','actual'], diagnostic=['empty'],
        limits='Nominal mass screen only; not global optimization, CFD, strength validation or flight clearance. '
               'Curved outline is a shared 64-segment CAD/flight polygon. Flat square-section fins, no fillets.'))
    rows = []
    with Engine() as engine:
        for shape, area, body in itertools.product(SHAPES, [45,55], [410,430]):
            config = variant(shape, area, body)
            folder = out/config.name
            folder.mkdir()
            path = folder/'config.yaml'
            save_json(path, config.model_dump())
            save_json(folder/'resolved-inputs.json', config.model_dump())
            digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
            save_json(folder/'manifest.json', dict(configuration_sha256=digest, command='fin-shape-screen'))
            workflow(Namespace(command='simulate', strict=False), config, path, folder, digest, engine)
            cases = json.loads((folder/'results.json').read_text())['cases']
            parts = json.loads((folder/'cad/mass-properties.json').read_text())
            save_json(folder/'dummy-targets.json', dummy_targets(config.geometry.mm('nose_length'), parts['payload-sled'], config))
            row = dict(design=config.name, shape=shape, area_mm2=area_mm2(outline(config)),
                       span_mm=config.geometry.mm('fin_span'), summary=summarize_cases(cases))
            loaded = [c for c in cases if c['loading']=='actual']
            for metric in ['apogee_m','peak_powered_speed_m_s','minimum_ascent_stability_cal',
                           'guide_departure_m_s','deployment_speed_m_s','landing_descent_m_s']:
                values = [c.get('metrics',{}).get(metric) for c in loaded]
                row[metric] = [min(values),max(values)] if all(v is not None for v in values) else None
            rows.append(row)
            save_json(out/'comparison.json', rows)
            seal_run(folder)
            print('FIN COMPLETE', config.name, row['summary']['planned'], flush=True)
    lines = ['# Equal-area D12-5 fin-shape screen', '',
             'Nominal estimates only; no physical clearance. Dummy/logger are planned; empty is diagnostic.', '',
             '| Design | Area mm² | Span mm | Planned passes / 6 | Loaded apogee range m |',
             '| --- | --- | --- | --- | --- |']
    for r in rows:
        lines.append(f"| [{r['design']}]({r['design']}/report.md) | {r['area_mm2']:.1f} | {r['span_mm']:.1f} | "
                     f"{r['summary']['planned']['passed']} | {r['apogee_m']} |")
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(out)
    print('FIN SCREEN COMPLETE', out, flush=True)


if __name__ == '__main__':
    main()
