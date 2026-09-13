"""Keep execution, engineering criteria, and missing physical evidence separate."""
import csv
import json
from pathlib import Path

from .config import Config

REQUIRED_METRICS = {'apogee_m', 'guide_departure_m_s', 'minimum_ascent_stability_cal',
                    'deployment_speed_m_s', 'landing_descent_m_s'}


def evaluate(result: dict, config: Config):
    checks = []
    limit = result.get('motor', {}).get('max_liftoff_mass')
    launch_mass = result.get('mass', {}).get('launch_mass_g')
    if limit:
        checks.append(dict(metric='launch_mass_g', minimum=None, maximum=limit['value'], unit='g',
                           source=limit['source'], kind='manufacturer requirement', value=launch_mass,
                           passed=None if launch_mass is None else launch_mass <= limit['value']))
    for criterion in config.criteria:
        value = result.get('metrics', {}).get(criterion.metric)
        passed = None if value is None else (
            (criterion.minimum is None or value >= criterion.minimum) and
            (criterion.maximum is None or value <= criterion.maximum))
        checks.append(dict(**criterion.model_dump(), value=value, passed=passed))
    if result['execution'] != 'completed':
        criteria_status = 'simulation failed'
    elif any(c['passed'] is False for c in checks) or result.get('warnings') or result.get('load_warnings') or result.get('metrics', {}).get('deployment_before_ground') is False:
        criteria_status = 'outside configured limits'
    elif not limit or not REQUIRED_METRICS.issubset({c.metric for c in config.criteria}) or any(c['passed'] is None for c in checks):
        criteria_status = 'unevaluated'
    elif any(not c['passed'] for c in checks) or result.get('warnings'):
        criteria_status = 'outside configured limits'
    else:
        criteria_status = 'meets configured simulation criteria'
    return dict(criteria_status=criteria_status,
                status='incomplete inputs' if criteria_status == 'meets configured simulation criteria' and config.missing() else criteria_status,
                checks=checks, eligible=False, rank=None,
                ranking_note='No flight candidates ranked while physical inputs and validation remain incomplete')


def write_report(out: Path):
    data = json.loads((out / 'results.json').read_text())
    lines = ['# Rocket Workbench report', '', f"Run: `{out.name}`", '',
             'Provisional software demonstration. Physical assembly and flight validation are pending.', '',
             f"Configuration SHA256: `{data['configuration_sha256']}`", '',
             '## Cases', '',
             '| Case | Execution / evaluation | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |',
             '|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
    fields = ['apogee_m', 'guide_departure_m_s', 'minimum_ascent_stability_cal',
              'deployment_speed_m_s', 'landing_descent_m_s', 'landing_displacement_m',
              'peak_powered_acceleration_g', 'peak_powered_specific_force_estimate_g', 'peak_powered_speed_m_s']
    rows = []
    if not data['cases']:
        lines += ['', 'Build only: no flights were simulated in this run.', '']
    for case in data['cases']:
        metrics = case.get('metrics', {})
        values = ['unavailable' if metrics.get(k) is None else f'{metrics[k]:.2f}' for k in fields]
        status = case['evaluation']['status']
        lines.append(f"| {case['id']} | {case['execution']} / {status} | " + ' | '.join(values) + ' |')
        rows.append(dict(case=case['id'], execution=case['execution'], evaluation=status,
                         **{k: metrics.get(k) for k in fields}))
    lines += ['', 'No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.', '',
              '## Warnings and failures', '']
    for case in data['cases']:
        lines.append(f"- {case['id']}: " + '; '.join(filter(None, [case.get('error'), *case.get('warnings', []),
                                                                  *case.get('load_warnings', [])])) if case.get('error') or case.get('warnings') or case.get('load_warnings') else f"- {case['id']}: no engine warnings")
    lines += ['', '## Missing measurements / physical checks', ''] + [f'- {s}' for s in data['missing_inputs']]
    lines += ['', '## Per-case criterion failures', '']
    for case in data['cases']:
        failures = [f"{c['metric']}={c['value']} {c['unit']} (allowed {c['minimum']} … {c['maximum']})"
                    for c in case['evaluation']['checks'] if c['passed'] is not True]
        lines.append(f"- {case['id']}: " + ('; '.join(failures) if failures else 'no numeric criterion failures; consult warnings and missing inputs'))
    if (out/'stress-spec.json').exists():
        spec = json.loads((out/'stress-spec.json').read_text())
        lines += ['', '## Deterministic stress envelope', '',
                  'These are bounded scenario corners, not probabilities or reliability estimates.', '',
                  '```json', json.dumps(spec, indent=2), '```', '',
                  'Each case records its applied factors in results.json and has a resolved corner input file.']
    lines += ['', '## Assumptions and boundaries', '',
              '- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.',
              '- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is scenario-dependent.',
              '- Native OpenRocket aerodynamics; configured axisymmetric nose, cylindrical sections, three flat trapezoidal fins and tapered collar fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.',
              '- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in collar override.',
              '- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful view.',
              '- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.',
              '- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground event, not a structural impact assessment.',
              '- Powered peaks use positive-thrust samples from liftoff strictly before first burnout, deployment, abort or ground contact. Missing events/data yield unavailable metrics; peak times and sample coverage are in JSON. These are sampled single-stage maxima, not continuous-time bounds.',
              '- Powered acceleration is trajectory acceleration magnitude / 9.80665. Estimated load is hypot(lateral acceleration, vertical acceleration + local gravity) / 9.80665 at the center of mass. Coriolis correction, sensor-offset rotation, vibration and deployment/impact shock are excluded; this is not a per-axis IMU prediction or a hardware survival rating.',
              '- Recovery is motor-ejection deployment with configured Cd; packing envelope, ejection seal, thermal protection and attachment loads require physical checks.',
              '- Reference mode preserves upstream geometry and masses; demonstration CAD and baseline mass assumptions do not apply to that reference.',
              '', '## Configured criteria', '']
    for criterion in data['criteria']:
        lines.append(f"- {criterion['metric']}: {criterion['minimum']} … {criterion['maximum']} {criterion['unit']}; {criterion['kind']}; {criterion['source']}")
    lines += ['', '## Reproducibility', '', '```json', json.dumps(data['versions'], indent=2), '```', '',
              'Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the table.', '']
    (out / 'report.md').write_text('\n'.join(lines))
    with (out / 'results.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['case', 'execution', 'evaluation', *fields])
        writer.writeheader()
        writer.writerows(rows)
    return out / 'report.md'
