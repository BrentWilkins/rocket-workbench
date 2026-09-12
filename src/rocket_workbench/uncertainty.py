"""Deterministic stress envelope; do not interpret corner counts as probabilities."""
import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import yaml
from pydantic import Field, model_validator

from .config import Config, Model, load_config


class StressSpec(Model):
    schema_version: int = Field(ge=1, le=1)
    print_mass_factors: list[float]
    payload_cg_offsets_mm: list[float]
    chute_cd: list[float]
    wind_m_s: list[float]
    max_cases: int = Field(ge=1, le=1000)
    source: str = Field(min_length=1)

    @model_validator(mode='after')
    def bounds(self):
        for values, low, high in [(self.print_mass_factors,.5,1.5), (self.payload_cg_offsets_mm,-10,10),
                                   (self.chute_cd,.3,1.5), (self.wind_m_s,0,8)]:
            if not values or any(not low <= v <= high for v in values):
                raise ValueError('Stress parameters empty or outside supported bounds')
        return self


def run_stress(path: Path, spec_path: Path, parent: Path):
    from .cad import build
    from .cli import save_json
    from .flight_model import generate
    from .report import evaluate, write_report
    from .simulator import Engine
    config = load_config(path)
    if config.mode != 'baseline':
        raise ValueError('Stress study requires a generated baseline')
    spec = StressSpec.model_validate(yaml.safe_load(spec_path.read_text()))
    total = len(spec.print_mass_factors)*len(spec.payload_cg_offsets_mm)*len(spec.chute_cd)*len(spec.wind_m_s)*3*len(config.motors)
    if total > spec.max_cases:
        raise ValueError(f'{total} cases exceed explicit budget {spec.max_cases}; use a configuration with selected motors')
    out = parent/('stress-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    out.mkdir(parents=True, exist_ok=False)
    save_json(out/'resolved-inputs.json', config.model_dump())
    save_json(out/'stress-spec.json', spec.model_dump())
    digest = hashlib.sha256(json.dumps(dict(config=config.model_dump(), stress=spec.model_dump()), sort_keys=True).encode()).hexdigest()
    parts = build(config, out/'cad')
    results = []
    with Engine() as engine:
        versions = engine.versions()
        for index, (factor, offset, cd) in enumerate(itertools.product(spec.print_mass_factors, spec.payload_cg_offsets_mm, spec.chute_cd)):
            data = config.model_dump()
            data['payload']['cg_x']['value'] += offset
            data['chute_cd']['value'] = cd
            changed = Config.model_validate(data)
            scaled = {name: dict(p, mass_g=p['mass_g']*factor, source=spec.source) for name,p in parts.items()}
            save_json(out/f'stress-{index}-inputs.json', dict(config=changed.model_dump(), print_mass_factor=factor, source=spec.source))
            for loading in ['empty','dummy','actual']:
                model_path = out/f'stress-{index}-{loading}.ork'
                ledger = generate(changed, scaled, loading, model_path)
                for motor in changed.motors:
                    for wind in spec.wind_m_s:
                        case_id = f'{index}-{loading}-{motor.designation}-{motor.delay_s:g}-wind{wind:g}'
                        try:
                            doc, warnings = engine.load(model_path)
                            sim = engine.new_simulation(doc)
                            record = engine.motor(sim,motor,changed)
                            record['max_liftoff_mass'] = motor.max_liftoff_mass.model_dump()
                            engine.configure(sim, changed, wind)
                            sim.setName(case_id)
                            result = engine.run(sim)
                            result.update(motor=record, mass=engine.mass(sim), load_warnings=warnings)
                            for key in ['dry_mass_g', 'dry_cg_x_mm']:
                                if abs(result['mass'][key]-ledger[key]) > .05:
                                    raise ValueError('Stress model mass/CG mismatch')
                            engine.save(doc,out/f'{case_id}.ork')
                        except Exception as exc:
                            result = dict(execution='simulation failed', error=str(exc), metrics={}, warnings=[])
                        result.update(id=case_id, loading=loading, wind_m_s=wind,
                                      stress=dict(print_mass_factor=factor,payload_cg_offset_mm=offset,chute_cd=cd))
                        result['evaluation'] = evaluate(result,changed)
                        results.append(result)
            print(f'Stress corner {index+1}: {len(results)}/{total} cases', flush=True)
    save_json(out/'results.json',dict(schema_version=1, configuration_sha256=digest, versions=versions,
        missing_inputs=config.missing(), criteria=[c.model_dump() for c in config.criteria], cases=results))
    write_report(out)
    (out/'run.log').write_text(spec.source+'\nThis is a deterministic envelope, not a probability estimate.\n')
    from .provenance import seal_run
    save_json(out/'manifest.json', dict(schema_version=1, configuration_sha256=digest, command='stress'))
    seal_run(out)
    print(out.resolve())
    return 1 if any(c['execution'] != 'completed' for c in results) else 0
