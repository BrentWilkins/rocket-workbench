from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import subprocess
import sys
import traceback
from contextlib import nullcontext
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from .config import load_config
from .report import evaluate, write_report


def save_json(path, data):
    path.write_text(json.dumps(data, indent=2, allow_nan=False)+'\n')


def execute(args):
    if args.command == 'report':
        print(write_report(Path(args.path)))
        from .provenance import seal_run
        seal_run(Path(args.path), record_sources=False)
        return 0
    if args.command == 'motors':
        from .config import MOTOR_DIMENSIONS_MM
        from .simulator import Engine
        if args.designation not in MOTOR_DIMENSIONS_MM:
            raise ValueError(f'Unsupported family; choose from {list(MOTOR_DIMENSIONS_MM)}')
        diameter, length = MOTOR_DIMENSIONS_MM[args.designation]
        with Engine() as engine:
            matches = engine.core.startup.Application.getMotorSetDatabase().findMotors(
                None, engine.core.motor.Motor.Type.SINGLE, 'Estes', args.designation, diameter/1000, length/1000)
            print(json.dumps([engine.motor_record(m, None) for m in matches], indent=2))
        return 0
    if args.command == 'sweep':
        from .sweep import run_sweep
        return run_sweep(Path(args.path), Path(args.spec), Path(args.output))
    if args.command == 'stress':
        from .uncertainty import run_stress
        return run_stress(Path(args.path), Path(args.spec), Path(args.output))
    if args.command == 'doctor':
        from .simulator import Engine, runtime
        jar, jvm = runtime()
        print(f'JAR checksum verified: {jar}\nJVM: {jvm}')
        with Engine() as engine:
            print(json.dumps(engine.versions(), indent=2))
        try:
            print('CadQuery:', importlib.metadata.version('cadquery'))
        except importlib.metadata.PackageNotFoundError:
            print('CadQuery absent: install with uv sync --extra cad for baseline CAD')
        print('Startup verified. Use integration-proof to verify real simulation and persistence.')
        return 0
    if args.command == 'integration-proof':
        from .proof import run_proof
        return run_proof(Path(args.output))
    path = Path(args.path).resolve()
    config = load_config(path)
    if args.command == 'validate':
        print('Configuration valid for demonstration. Final fit/flight inputs incomplete:')
        print('\n'.join(f'- {m}' for m in config.missing()))
        return 2 if args.strict else 0
    out = Path(args.output) / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+config.name+'-'+uuid4().hex[:8])
    out.mkdir(parents=True, exist_ok=False)
    resolved = config.model_dump()
    digest = hashlib.sha256(json.dumps(resolved, sort_keys=True).encode()).hexdigest()
    save_json(out / 'resolved-inputs.json', resolved)
    save_json(out / 'manifest.json', dict(schema_version=1, configuration_sha256=digest,
                                        source=str(path), command=args.command))
    print(f'Run directory: {out.resolve()}', flush=True)
    try:
        return workflow(args, config, path, out, digest)
    except Exception:
        (out / 'error.log').write_text(traceback.format_exc())
        raise


def workflow(args, config, source, out, digest, supplied_engine=None):
    from .simulator import Engine
    from .flight_model import generate
    expected = {}
    if config.mode == 'baseline':
        from .cad import build
        parts = build(config, out / 'cad')
        for loading in ['empty', 'dummy', 'actual']:
            expected[loading] = generate(config, parts, loading, out / f'{loading}-input.ork')
        save_json(out / 'mass-ledger.json', expected)
    cases = []
    with (Engine() if supplied_engine is None else nullcontext(supplied_engine)) as engine:
        versions = engine.versions()
        if config.mode == 'baseline':
            versions['packages']['cadquery'] = importlib.metadata.version('cadquery')
        loadings = ['reference'] if config.mode == 'reference' else ['empty', 'dummy', 'actual']
        for loading in loadings:
            model_path = source.parent / config.reference_file if loading == 'reference' else out / f'{loading}-input.ork'
            doc, load_warnings = engine.load(model_path)
            if load_warnings:
                raise ValueError(f'Model import warnings must be resolved: {load_warnings}')
            sim = doc.getSimulation(0) if loading == 'reference' else engine.new_simulation(doc)
            actual_mass = engine.mass(sim)
            if loading != 'reference':
                for key in ['dry_mass_g', 'dry_cg_x_mm']:
                    if abs(actual_mass[key]-expected[loading][key]) > 0.05:
                        raise ValueError(f'Mass/CG mismatch for {loading}: {key} expected {expected[loading][key]}, engine {actual_mass[key]}')
            engine.save(doc, out / f'{loading}.ork')
            if args.command == 'build':
                continue
            for motor in config.motors:
                for wind in config.launch.wind_speeds:
                    case_id = f'{loading}-{motor.designation}-{motor.delay_s:g}-wind{wind.value:g}'
                    try:
                        # Reload a fresh document for every case; no changing a
                        # previously simulated vehicle or sharing motor state.
                        doc, warnings = engine.load(out / f'{loading}.ork')
                        sim = doc.getSimulation(0)
                        motor_record = engine.motor(sim, motor, config)
                        engine.configure(sim, config, wind.value)
                        sim.setName(case_id)
                        result = engine.run(sim)
                        result.update(motor=motor_record, mass=engine.mass(sim), load_warnings=warnings)
                        result['motor']['max_liftoff_mass'] = motor.max_liftoff_mass.model_dump()
                        engine.save(doc, out / f'{case_id}.ork')
                    except Exception as exc:
                        result = dict(execution='simulation failed', error=str(exc), warnings=[], metrics={},
                                      requested_motor=motor.model_dump())
                    result.update(id=case_id, loading=loading, wind_m_s=wind.value)
                    result['evaluation'] = evaluate(result, config)
                    cases.append(result)
                    print(f"{case_id}: {result['execution']}; {result['evaluation']['status']}", flush=True)
    revision = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    versions['repository_revision'] = revision.stdout.strip() if revision.returncode == 0 else None
    save_json(out / 'results.json', dict(schema_version=1, configuration_sha256=digest,
              versions=versions, missing_inputs=config.missing(), criteria=[c.model_dump() for c in config.criteria], cases=cases))
    (out / 'run.log').write_text('\n'.join(f"{c['id']}: {c['execution']}; {c.get('error')}" for c in cases)+'\n')
    print(write_report(out))
    from .provenance import seal_run
    seal_run(out)
    if any(c['execution'] != 'completed' for c in cases):
        return 1
    return 2 if args.strict and (config.missing() or any(not c['evaluation']['eligible'] for c in cases)) else 0


def main():
    parser = argparse.ArgumentParser(description='Printable model rocket design workbench')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('doctor')
    sub.add_parser('motors').add_argument('designation')
    sweep = sub.add_parser('sweep')
    sweep.add_argument('path')
    sweep.add_argument('spec')
    sweep.add_argument('--output', default='runs')
    stress = sub.add_parser('stress')
    stress.add_argument('path')
    stress.add_argument('spec')
    stress.add_argument('--output', default='runs')
    proof = sub.add_parser('integration-proof')
    proof.add_argument('--output', default='runs')
    for name in ['validate', 'build', 'simulate']:
        command = sub.add_parser(name)
        command.add_argument('path')
        command.add_argument('--output', default='runs')
        command.add_argument('--strict', action='store_true')
    sub.add_parser('report').add_argument('path')
    args = parser.parse_args()
    try:
        code = execute(args)
    except (ValueError, OSError, ImportError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        code = 1
    sys.exit(code)


if __name__ == '__main__':
    main()
