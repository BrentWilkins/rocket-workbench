"""Publish the expanded recovery comparison, including drift from retained flight cases."""
import argparse
import json
from pathlib import Path

from rocket_workbench.cli import save_json
from rocket_workbench.provenance import seal_run
from summarize_recovery_stress import summarize


def drift_bounds(row):
    values = []
    for profile in row['profiles']:
        root = Path(profile['source_study']).resolve()
        result = (root / profile['report']).with_name('results.json').resolve()
        if not result.is_relative_to(root):
            raise ValueError('Flight evidence escapes study directory')
        cases = json.loads(result.read_text())['cases']
        loaded = [case for case in cases if case['loading'] == 'actual']
        if len(loaded) != 24:
            raise ValueError('Expected 24 logger cases per mass profile')
        for case in loaded:
            value = case.get('metrics', {}).get('landing_displacement_m')
            if value is None:
                raise ValueError('Missing logger drift metric; do not publish partial bounds')
            values.append(value)
    return [min(values), max(values)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads((args.study/'search-spec.json').read_text())
    rows = summarize([args.study], expected_designs=spec['designs'])
    for row in rows:
        if row['planned']['completed'] != 192 or row['diagnostic_empty']['completed'] != 96:
            raise ValueError('All flight cases must finish before publishing complete comparison')
        row['landing_displacement_m'] = drift_bounds(row)
    args.output.mkdir(parents=True, exist_ok=False)
    save_json(args.output/'comparison.json', rows)
    lines = ['# Expanded recovery uncertainty comparison', '',
             f'{288*len(rows)} deterministic flights; 192 planned dummy/logger and 96 empty diagnostics per design. '
             'Scenario counts are not reliability probabilities.', '',
             'Bounds: print mass ×1/1.2, payload CG ±5 mm, wind 0/2/4 m/s, chute Cd 0.53/1.04, '
             'mount mass ×1/1.5. Upper avionics and +20% chute mass are paired, not independently varied. '
             'Generic packing remains provisional; sourced chute mass is a literature specimen, not our hardware.', '',
             '| Design | Planned passes / 192 | Altitude m | Speed m/s | Descent m/s | Drift m |',
             '| --- | --- | --- | --- | --- | --- |']
    for row in rows:
        cells = []
        for metric in ('apogee_m', 'peak_powered_speed_m_s', 'landing_descent_m_s', 'landing_displacement_m'):
            bounds = row[metric]
            cells.append('unavailable' if bounds is None else f'{bounds[0]:.2f}–{bounds[1]:.2f}')
        lines.append(f"| {row['design']} | {row['planned']['passed']} | "+' | '.join(cells)+' |')
    lines += ['', 'Drift is horizontal landing displacement from the pad under the modeled uniform winds. '
              'It is not a landing-zone guarantee. CFD, final retention hardware and physical validation remain separate.']
    if any('insert-trial' in row['design'] for row in rows):
        lines += ['', f"Insert-trial upper profiles add {spec['insert_joint_upper_additional_g']:g} g "
                  'to the nominal joint allowance, paired with upper avionics/chute mass. '
                  'These are unmeasured engineering allowances, not tested joint strength.']
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__ == '__main__':
    main()
