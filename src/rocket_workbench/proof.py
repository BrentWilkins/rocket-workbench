"""Real bridge acceptance, plus an independent Java execution path."""
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from .config import load_config
from .simulator import Engine, ROOT, runtime


def run_proof(parent: Path) -> int:
    out = parent / ('proof-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid4().hex[:8])
    out.mkdir(parents=True, exist_ok=False)
    config = load_config(ROOT / 'examples/reference.yaml')
    evidence = dict(schema_version=1, gui_comparison='pending', tolerance={'apogee_m': 1e-6, 'time_series_absolute': 1e-9})
    with Engine() as engine:
        import orhelper
        evidence['versions'] = engine.versions()
        doc, warnings = engine.load(ROOT / 'examples/upstream-simple.ork')
        assert not warnings, warnings
        sim = doc.getSimulation(0)
        engine.configure(sim, config, 0)
        evidence['reference'] = engine.run(sim)
        assert evidence['reference']['execution'] == 'completed'
        mounts = list(sim.getActiveConfiguration().getActiveMotors())
        evidence['motor'] = engine.motor_record(mounts[0].getMotor(), mounts[0].getEjectionDelay())
        # Pin the actual conditions in an engine-saved fixture for Java/GUI use.
        engine.save(doc, out / 'reference.ork')
        # Upstream helper path, listener callbacks, and observed seed mutation.
        class Counter(orhelper.AbstractSimulationListener):
            def __init__(self):
                self.steps = [0]  # Shared across the engine's shallow listener clones.
            def postStep(self, status):
                self.steps[0] += 1
        listener = Counter()
        sim.getOptions().setRandomSeed(42)
        engine.helper.run_simulation(sim, [listener])
        evidence['upstream_helper'] = dict(listener_steps=listener.steps[0],
            seed_after=sim.getOptions().getRandomSeed(), apogee_m=sim.getSimulatedData().getMaxAltitude())
        assert listener.steps[0] > 0
        body = engine.helper.get_component_named(doc.getRocket(), 'Body tube')
        original = float(body.getLength())
        body.setLength(original + .01)
        engine.save(doc, out / 'modified.ork')
        reloaded, warnings = engine.load(out / 'modified.ork')
        new_length = float(engine.helper.get_component_named(reloaded.getRocket(), 'Body tube').getLength())
        assert abs(new_length - original - .01) < 1e-12
        evidence['modify_save_reload'] = dict(original_length_m=original, reloaded_length_m=new_length, warnings=warnings)
        # A-B-A, fresh documents but one JVM, detects leaked model/options state.
        repeats = []
        for wind in [0, 2, 0]:
            fresh, _ = engine.load(out / 'reference.ork')
            s = fresh.getSimulation(0)
            engine.configure(s, config, wind)
            repeats.append(engine.run(s))
        assert repeats[0]['timeseries'] == repeats[2]['timeseries']
        evidence['isolation'] = dict(wind_m_s=[0, 2, 0], apogee_m=[r['metrics']['apogee_m'] for r in repeats],
                                     identical_A_timeseries=True)
        evidence['reference'] = repeats[0]
    # This is a comparison executable only, not a replacement simulator adapter.
    jar, jvm = runtime()
    java = Path(os.environ.get('ROCKET_JAVA', jvm.parents[2] / 'bin/java'))
    if not java.is_file():
        java = Path(os.environ.get('ROCKET_JAVA', '/Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home/bin/java'))
    command = [str(java), '-Djava.awt.headless=true', '-cp', str(jar), str(ROOT / 'scripts/ReferenceCheck.java'),
               str((out / 'reference.ork').resolve())]
    run = subprocess.run(command, text=True, capture_output=True, timeout=90)
    (out / 'java-reference.log').write_text(run.stdout+'\n'+run.stderr)
    records = [line.removeprefix('REFERENCE_JSON=') for line in run.stdout.splitlines() if line.startswith('REFERENCE_JSON=')]
    if run.returncode != 0 or not records:
        evidence['independent_java'] = dict(status='failed', returncode=run.returncode)
    else:
        import numpy as np
        independent = json.loads(records[-1])
        delta = abs(independent['apogee_m']-evidence['reference']['metrics']['apogee_m'])
        differences = {key: float(np.max(np.abs(np.array(independent[key])-evidence['reference']['timeseries'][key])))
                       for key in ['time_s', 'altitude_m']}
        summary_differences = {key: abs(independent[key]-evidence['reference']['metrics'][key])
                              for key in ['guide_departure_m_s', 'deployment_speed_m_s', 'landing_total_speed_m_s']}
        passed = delta <= 1e-6 and max(differences.values()) <= 1e-9 and max(summary_differences.values()) <= 1e-6
        evidence['independent_java'] = dict(status='passed' if passed else 'failed',
            result=independent, apogee_difference_m=delta, timeseries_max_difference=differences,
            summary_differences=summary_differences)
    (out / 'evidence.json').write_text(json.dumps(evidence, indent=2, allow_nan=False)+'\n')
    print(out.resolve())
    print('Independent Java comparison:', evidence['independent_java']['status'])
    print('GUI comparison: pending (no GUI run performed)')
    from .provenance import seal_run
    seal_run(out)
    return 0 if evidence['independent_java']['status'] == 'passed' else 1
