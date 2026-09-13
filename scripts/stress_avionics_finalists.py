"""Run nominal/upper avionics budgets through the full deterministic stress grid."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from rocket_workbench.avionics import payload_budget
from rocket_workbench.cli import save_json
from rocket_workbench.config import Config, load_config
from rocket_workbench.provenance import seal_run


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--design', help='Explicit completed nominal-feasible baseline instead of automatic finalists')
    args = parser.parse_args()
    if args.design:
        finalists = [r for r in json.loads((args.study/'comparison.json').read_text())
                     if r['design']==args.design and r['nominal_feasible']]
    else:
        finalists = json.loads((args.study/'finalists.json').read_text())
    if not finalists:
        raise ValueError('No nominal feasible finalist; evaluate design changes before stress selection')
    args.output.mkdir(parents=True, exist_ok=False)
    results = []
    for row in finalists:
        base = load_config(args.study/row['design']/'config.yaml')
        for upper in [False, True]:
            name = row['design'] + ('-upper' if upper else '-nominal')
            folder = args.output/name
            folder.mkdir()
            data = base.model_dump()
            mass, cg = payload_budget(base.geometry.mm('nose_length'), upper)
            data['payload']['mass']['value'] = mass
            data['payload']['cg_x']['value'] = cg
            data['motors'] = [m for m in data['motors'] if f"{m['designation']}-{m['delay_s']:g}" == row['motor']]
            if len(data['motors']) != 1:
                raise ValueError('Finalist motor not resolved uniquely')
            config = Config.model_validate(data)
            save_json(folder/'config.yaml', config.model_dump())
            with (folder/'execution.log').open('w') as log:
                subprocess.run([sys.executable, '-m', 'rocket_workbench.cli', 'stress',
                    str(folder/'config.yaml'), 'examples/uncertainty.yaml', '--output', str(folder)],
                    stdout=log, stderr=subprocess.STDOUT, check=True)
            runs = list(folder.glob('stress-*'))
            if len(runs) != 1:
                raise ValueError('Stress output not unique')
            run = runs[0]
            cases = json.loads((run/'results.json').read_text())['cases']
            loaded = [c for c in cases if c['loading']=='actual']
            metrics = {k:dict(min=min(c['metrics'][k] for c in loaded), max=max(c['metrics'][k] for c in loaded))
                       for k in ['apogee_m','peak_powered_speed_m_s','guide_departure_m_s',
                                 'minimum_ascent_stability_cal','deployment_speed_m_s','landing_descent_m_s']}
            results.append(dict(design=row['design'], motor=row['motor'], payload_g=mass,
                upper=upper, run=str(run), cases=len(cases),
                passed=sum(c['evaluation']['criteria_status']=='meets configured simulation criteria' for c in cases),
                loaded_metrics=metrics))
            save_json(args.output/'comparison.json', results)
            print(f"STRESS COMPLETE {name}: {results[-1]['passed']}/{len(cases)}", flush=True)
    lines = ['# Current-avionics finalist uncertainty comparison', '',
             'Each row: print mass 1.0/1.2, payload CG -5/+5 mm, chute Cd 0.6/0.9, winds 0/2/4 m/s, three loadings.',
             'Nominal and upper avionics budgets are separate. Corner counts are not reliability probabilities.', '',
             '| Design | Avionics g | Cases meeting gates | Loaded apogee range m | Loaded speed range m/s |',
             '| --- | --- | --- | --- | --- |']
    for r in results:
        rel = Path(r['run']).relative_to(args.output)
        m = r['loaded_metrics']
        lines.append(f"| [{r['design']}]({rel}/report.md) | {r['payload_g']} | {r['passed']}/{r['cases']} | {m['apogee_m']['min']:.2f}–{m['apogee_m']['max']:.2f} | {m['peak_powered_speed_m_s']['min']:.2f}–{m['peak_powered_speed_m_s']['max']:.2f} |")
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__ == '__main__':
    main()
