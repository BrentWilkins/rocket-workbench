"""Bounded deterministic search. Rejections and simulations retain full evidence."""
import csv
import hashlib
import itertools
import json
import traceback
from argparse import Namespace
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import yaml
from pydantic import Field, model_validator

from .config import Config, Model, load_config


class SweepSpec(Model):
    schema_version: int = Field(ge=1, le=1)
    axes: dict[str, list[float]]
    max_designs: int = Field(ge=1, le=100)
    source: str = Field(min_length=1)

    @model_validator(mode='after')
    def bounded(self):
        bounds = {'body_length': (240, 400), 'fin_span': (25, 60), 'chute_diameter': (250, 500),
                  'wall': (.8, 2), 'fin_thickness': (1.2, 2.4)}
        size = 1
        for key, values in self.axes.items():
            if key not in bounds or not values or len(values) != len(set(values)):
                raise ValueError('Unsupported sweep axis, empty axis, or duplicate values')
            if any(not bounds[key][0] <= v <= bounds[key][1] for v in values):
                raise ValueError(f'{key} outside supported bounds {bounds[key]}')
            size *= len(values)
        if not self.axes or size > self.max_designs:
            raise ValueError('Sweep exceeds explicit design budget or has no axes')
        return self


def variant(base: Config, values: dict, source: str) -> Config:
    data = base.model_dump()
    if base.printed_measurements:
        raise ValueError('Do not reuse measured printed masses across changed geometry; remove overrides for a design sweep')
    for key, value in values.items():
        data['geometry'][key].update(value=value, provenance='demonstration assumption', source=source)
    g = data['geometry']
    length, chute = g['body_length']['value'], g['chute_diameter']['value']
    n = g['nose_length']['value']
    area_ratio = (chute / base.geometry.chute_diameter.value)**2
    packed = base.geometry.chute_packed_length.value * area_ratio
    g['chute_packed_length'].update(value=packed, source='Area-scaled provisional packing estimate; physical pack test required')
    for item in data['purchased_masses']:
        role = item['role']
        if role == 'body':
            item['mass']['value'] *= length / base.geometry.body_length.value
            item['x']['value'] = n + length/2
        elif role == 'mount':
            item['x']['value'] = n + length-g['motor_overhang']['value']-g['motor_mount_length']['value']/2
        elif role == 'collar_adhesive':
            item['x']['value'] = n + length-g['collar_length']['value']/2
        elif role == 'lugs':
            item['x']['value'] = n+.475*length+.0125*1000
        elif role == 'chute':
            item['name'] = f'Nominal {chute:g} mm parachute and lines'
            item['mass']['value'] *= area_ratio
            item['x']['value'] = n+g['bay_length']['value']+10+packed/2
        elif role == 'wadding':
            item['x']['value'] = n+length-g['motor_overhang']['value']-g['motor_mount_length']['value']-20
        item['mass'].update(provenance='estimate', source='Baseline component estimate, tube length/chute area scaling applied where relevant')
        item['x'].update(provenance='demonstration assumption', source='Canonical nose-origin component placement for swept geometry')
    return Config.model_validate(data)


def run_sweep(config_path: Path, spec_path: Path, parent: Path):
    from .cli import workflow, save_json
    from .simulator import Engine
    base = load_config(config_path)
    if base.mode != 'baseline':
        raise ValueError('Geometry sweeps require baseline mode; reference remains unchanged')
    spec = SweepSpec.model_validate(yaml.safe_load(spec_path.read_text()))
    out = parent / ('sweep-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    out.mkdir(parents=True, exist_ok=False)
    save_json(out/'sweep-spec.json', spec.model_dump())
    save_json(out/'base-inputs.json', base.model_dump())
    records = []
    with Engine() as engine:
        for index, point in enumerate(itertools.product(*spec.axes.values())):
            values = dict(zip(spec.axes, point))
            folder = out/f'design-{index:03d}'
            folder.mkdir()
            record = dict(id=folder.name, parameters=values, eligible=False, rank=None)
            try:
                candidate = variant(base, values, spec.source)
            except ValueError as exc:
                record.update(status='rejected inputs', error=str(exc))
                save_json(folder/'rejection.json', record)
                records.append(record)
                continue
            resolved = candidate.model_dump()
            save_json(folder/'resolved-inputs.json', resolved)
            digest = hashlib.sha256(json.dumps(resolved, sort_keys=True).encode()).hexdigest()
            save_json(folder/'manifest.json', dict(schema_version=1, configuration_sha256=digest, parameters=values))
            try:
                exit_code = workflow(Namespace(command='simulate', strict=False), candidate, config_path.resolve(), folder, digest, engine)
                if exit_code != 0:
                    raise ValueError('One or more simulation cases failed; see retained results.json and report.md')
                cases = json.loads((folder/'results.json').read_text())['cases']
                passed = [c for c in cases if c['evaluation']['criteria_status'] == 'meets configured simulation criteria']
                # One motor/delay must pass every wind for a loading. Different
                # loadings may have different choices; do not pool isolated wins.
                supported = {}
                for loading in ['empty', 'dummy', 'actual']:
                    supported[loading] = []
                    for motor in candidate.motors:
                        group = [c for c in cases if c['loading'] == loading and c.get('motor', {}).get('designation') == motor.designation
                                 and c.get('motor', {}).get('delay_s') == motor.delay_s]
                        if len(group) == len(candidate.launch.wind_speeds) and all(c in passed for c in group):
                            supported[loading].append(f'{motor.designation}-{motor.delay_s:g}')
                record.update(status='evaluated', simulation_criteria_passes=len(passed), cases=len(cases),
                              loading_options=supported, all_loadings_nominally_supported=all(supported.values()),
                              dry_mass_g=json.loads((folder/'mass-ledger.json').read_text())['empty']['dry_mass_g'])
            except Exception as exc:
                record.update(status='execution failed', error=str(exc))
                (folder/'error.log').write_text(traceback.format_exc())
            records.append(record)
            save_json(out/'sweep-results.json', records)
            print(f"Design {index+1}: {record['status']}", flush=True)
    save_json(out/'sweep-results.json', records)
    lines = ['# Bounded design sweep', '', f'Search: {spec.source}', '',
             'No incomplete design is ranked as eligible for flight. Nominal simulation passes are identified separately.', '',
             '| Design | Parameters (mm) | Status | Passing cases | Empty/dummy/actual motor options |',
             '|---|---|---|---:|---|']
    for r in records:
        evidence = 'report.md' if r['status'] == 'evaluated' else ('rejection.json' if r['status'] == 'rejected inputs' else 'error.log')
        lines.append(f"| [{r['id']}]({r['id']}/{evidence}) | {r['parameters']} | {r['status']} | {r.get('simulation_criteria_passes', 0)} | {r.get('loading_options', r.get('error', ''))} |")
    supported = [r for r in records if r.get('all_loadings_nominally_supported')]
    lines += ['', f'{len(supported)} designs support all loadings under the nominal configured criteria.', '',
              'If zero: this bounded search found no qualifying design; it is not proof that no 18 mm design can work. See docs/REVIEW.md for tradeoff experiments.', '']
    (out/'report.md').write_text('\n'.join(lines))
    with (out/'sweep-results.csv').open('w', newline='') as f:
        fields = ['id', 'status', 'parameters', 'simulation_criteria_passes', 'dry_mass_g', 'all_loadings_nominally_supported']
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(records)
    print(f'Sweep report: {out.resolve()}/report.md')
    from .provenance import seal_run
    seal_run(out)
    return 1 if any(r['status'] == 'execution failed' for r in records) else 0
