"""Nine bounded nose candidates; preserve each CAD, flight model, and case result."""
import hashlib
import itertools
import json
from argparse import Namespace
from datetime import datetime, timezone
from pathlib import Path

from rocket_workbench.cli import workflow, save_json
from rocket_workbench.config import Config, load_config
from rocket_workbench.simulator import Engine

ROOT = Path(__file__).resolve().parents[1]


def candidate(base, shape, length):
    if base.printed_measurements:
        raise ValueError('Measured print overrides cannot be reused for new nose geometry')
    data = base.model_dump()
    delta = length-base.geometry.nose_length.value
    data['name'] = f'nose-{shape}-{length}'
    data['nose_shape'] = shape
    data['geometry']['nose_length'].update(value=length, provenance='demonstration assumption',
                                         source='Bounded nose study: 50/70/90 mm; no measured fit')
    # Keep every item fixed relative to the tube/bay, not the changing tip origin.
    for item in data['purchased_masses']:
        item['x']['value'] += delta
    data['payload']['cg_x']['value'] += delta
    return Config.model_validate(data)


def main():
    base = load_config(ROOT/'examples/candidate-recovery-stress.yaml')
    out = ROOT/'runs'/('nose-study-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    out.mkdir(exist_ok=False)
    records = []
    with Engine() as engine:
        for shape, length in itertools.product(['conical', 'ogive', 'ellipsoid'], [50, 70, 90]):
            config = candidate(base, shape, length)
            folder = out/config.name
            folder.mkdir()
            config_path = folder/'config.yaml'
            config_path.write_text(json.dumps(config.model_dump(), indent=2)+'\n')
            digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
            save_json(folder/'resolved-inputs.json', config.model_dump())
            save_json(folder/'manifest.json', dict(configuration_sha256=digest, command='nose-study'))
            result = workflow(Namespace(command='simulate', strict=False), config, config_path, folder, digest, engine)
            if result:
                raise RuntimeError(f'Failed candidate: {folder}')
            cases = json.loads((folder/'results.json').read_text())['cases']
            part = json.loads((folder/'cad/mass-properties.json').read_text())['nose-bay']
            ledger = json.loads((folder/'mass-ledger.json').read_text())
            row = dict(name=config.name, shape=shape, length_mm=length, nose_bay_mass_g=part['mass_g'],
                       dry_empty_mass_g=ledger['empty']['dry_mass_g'], cases=len(cases),
                       passed=sum(c['evaluation']['criteria_status']=='meets configured simulation criteria' for c in cases),
                       eligible=False, ogive_drag_caveat=shape=='ogive')
            for metric in ['apogee_m','guide_departure_m_s','minimum_ascent_stability_cal','deployment_speed_m_s','landing_descent_m_s','landing_displacement_m']:
                values = [c['metrics'][metric] for c in cases]
                row[metric] = dict(min=min(values), max=max(values))
            records.append(row)
            save_json(out/'comparison.json', records)
            print(f"{row['name']}: {row['passed']}/{len(cases)} gates; nose/bay {part['mass_g']:.3f} g", flush=True)
    lines = ['# Bounded nose study', '', 'C5-3 only; three loadings and winds 0/2 m/s. Not flight approval.', '',
             'OpenRocket 24.12 is current stable. Tangent-ogive pressure drag has an upstream development fix (#2999); do not treat small differences as definitive.', '',
             '| Candidate | Nose/bay g | Dry empty g | Passes | Lowest stability cal | Peak deployment m/s |',
             '|---|---:|---:|---:|---:|---:|']
    for r in records:
        lines.append(f"| [{r['name']}]({r['name']}/report.md) | {r['nose_bay_mass_g']:.2f} | {r['dry_empty_mass_g']:.2f} | {r['passed']}/{r['cases']} | {r['minimum_ascent_stability_cal']['min']:.3f} | {r['deployment_speed_m_s']['max']:.3f} |")
    (out/'report.md').write_text('\n'.join(lines)+'\n')
    print(out, flush=True)


if __name__ == '__main__':
    main()
