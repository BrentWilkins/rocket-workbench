"""Re-run the current 50 mm cone with all five motor/delay cases at two time steps."""
import hashlib
import json
from argparse import Namespace
from datetime import datetime, timezone
from pathlib import Path

from rocket_workbench.cli import workflow, save_json
from rocket_workbench.config import load_config, Config
from rocket_workbench.simulator import Engine
from study_noses import candidate

ROOT = Path(__file__).resolve().parents[1]


def main():
    base = candidate(load_config(ROOT/'examples/candidate-recovery.yaml'), 'conical', 50)
    out = ROOT/'runs'/('powered-study-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
    out.mkdir()
    runs = []
    with Engine() as engine:
        for label, factor in [('nominal', 1), ('half-step', .5)]:
            data = base.model_dump()
            data['launch']['time_step']['value'] *= factor
            config = Config.model_validate(data)
            folder = out/label
            folder.mkdir()
            config_path = folder/'config.yaml'
            save_json(config_path, config.model_dump())
            digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
            save_json(folder/'resolved-inputs.json', config.model_dump())
            save_json(folder/'manifest.json', dict(configuration_sha256=digest, command='powered-flight-study'))
            workflow(Namespace(command='simulate', strict=False), config, config_path, folder, digest, engine)
            runs.append(json.loads((folder/'results.json').read_text()))
    metrics = ['peak_powered_acceleration_g', 'peak_powered_specific_force_estimate_g', 'peak_powered_speed_m_s']
    comparison = []
    finer = {c['id']: c for c in runs[1]['cases']}
    for case in runs[0]['cases']:
        fine = finer[case['id']]
        row = dict(case=case['id'], execution=case['execution'],
                   evaluation=case['evaluation']['criteria_status'])
        for metric in metrics:
            a, b = case['metrics'].get(metric), fine['metrics'].get(metric)
            row[metric] = dict(nominal=a, half_step=b,
                               absolute_change=None if a is None or b is None else abs(b-a))
        comparison.append(row)
    save_json(out/'comparison.json', comparison)
    lines = ['# Powered-flight acceleration study', '',
             '50 mm conical nose, revised lug saddles, provisional 18 g loaded payload; no physical validation.', '',
             '[Nominal-step full report](nominal/report.md) | [Half-step full report](half-step/report.md)', '',
             'All 30 motor/loading/wind cases remain visible, including failed criteria. Half-step differences',
             'check numerical sensitivity, not uncertainty in the hardware or thrust curve.', '',
             '| Case | Peak trajectory g | Estimated load g | Peak powered m/s | Load change on halving step g |',
             '|---|---:|---:|---:|---:|']
    def fmt(value):
        return 'unavailable' if value is None else f'{value:.3f}'
    for row in comparison:
        vals = [row[m]['nominal'] for m in metrics] + [row[metrics[1]]['absolute_change']]
        lines.append('| '+row['case']+' | '+' | '.join(map(fmt, vals))+' |')
    lines += ['', 'Estimated load restores local gravity to trajectory acceleration; neglects Coriolis and sensor-offset',
              'rotation. Not a per-axis IMU prediction, shock rating, or certification. See full reports for definitions.', '']
    (out/'report.md').write_text('\n'.join(lines))
    from rocket_workbench.provenance import seal_run
    seal_run(out)
    print(out, flush=True)


if __name__ == '__main__':
    main()
