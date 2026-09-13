"""Retained deterministic uncertainty comparison for passive fin finalists."""
import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path

from rocket_workbench.avionics import payload_budget
from rocket_workbench.cli import save_json
from rocket_workbench.config import Config, load_config
from rocket_workbench.progression import summarize_cases
from rocket_workbench.provenance import seal_run

DESIGNS = ['trapezoidal-a45-b430', 'elliptical-a55-b410', 'clipped-delta-a45-b410',
           'clipped-delta-a45-b430', 'swept-a45-b410']


def configuration(base, upper, mount_factor):
    data = base.model_dump()
    mass, cg = payload_budget(base.geometry.mm('nose_length'), upper)
    for key,value in [('mass',mass),('cg_x',cg)]:
        data['payload'][key].update(value=value,provenance='estimate',source='Component nominal/upper mass envelope')
    mount = next(i for i in data['purchased_masses'] if i['role']=='mount')
    mount['mass'].update(value=mount['mass']['value']*mount_factor,provenance='estimate',
                         source='Mount assembly mass sensitivity, unchanged axial CG')
    if upper and base.bay_retention == 'm2-insert-trial-v1':
        hardware = next(i for i in data['purchased_masses'] if i['role']=='bay_hardware')
        # Input is the nominal insert configuration; increase its 0.7 g allowance to 1.4 g.
        extra = .7
        mass = hardware['mass']['value']
        station = base.geometry.mm('nose_length') + base.geometry.mm('bay_length') - 5
        hardware['x'].update(value=(mass*hardware['x']['value']+extra*station)/(mass+extra),
                             provenance='estimate', source='Upper insert-joint allowance at aft bay')
        hardware['mass'].update(value=mass+extra, provenance='estimate',
                                source='Nominal insert configuration plus 0.7 g upper joint allowance; unmeasured')
    return Config.model_validate(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--design',action='append',help='Explicit design directory; may be repeated')
    parser.add_argument('--uncertainty', type=Path, default=Path('examples/uncertainty.yaml'))
    parser.add_argument('--upper-chute-factor', type=float, default=1.,
                        help='Additional chute mass factor paired with the upper avionics profile')
    args = parser.parse_args()
    if not 1 <= args.upper_chute_factor <= 1.5:
        parser.error('Upper chute mass factor must be within 1–1.5')
    args.output.mkdir(parents=True,exist_ok=False)
    designs=args.design or DESIGNS
    save_json(args.output/'search-spec.json',dict(designs=designs,flights=288*len(designs),
        upper_avionics=[False,True],mount_mass_factors=[1,1.5],
        inner_spec=str(args.uncertainty), upper_chute_factor=args.upper_chute_factor,
        insert_joint_upper_additional_g=.7,
        input_basis='Nominal mass configuration; insert trials already include nominal 0.7 g joint allowance',
        selection=('Explicit user/workflow-selected design directories' if args.design else
                   'Nominal feasible conventional reference; best feasible ellipse; small delta at both lengths; small swept. '
                   'Keep two delta lengths to compare recovery space and stability against performance.'),
        interpretation='Deterministic corners, not reliability probabilities or physical clearance'))
    rows=[]
    for design,upper,factor in itertools.product(designs,[False,True],[1.,1.5]):
        folder=args.output/f'{design}-upper{int(upper)}-mount{factor:g}'
        folder.mkdir()
        config=configuration(load_config(args.study/design/'config.yaml'),upper,factor)
        if upper and args.upper_chute_factor != 1:
            data = config.model_dump()
            chute = next(p for p in data['purchased_masses'] if p['role'] == 'chute')
            chute['mass'].update(value=chute['mass']['value']*args.upper_chute_factor,
                                 provenance='estimate', source='Upper chute mass allowance, not measured hardware')
            config = Config.model_validate(data)
        save_json(folder/'config.yaml',config.model_dump())
        with (folder/'execution.log').open('w') as log:
            result=subprocess.run([sys.executable,'-m','rocket_workbench.cli','stress',str(folder/'config.yaml'),
                str(args.uncertainty),'--output',str(folder)],stdout=log,stderr=subprocess.STDOUT)
        runs=list(folder.glob('stress-*/results.json'))
        if len(runs)!=1:
            raise RuntimeError(f'Missing or ambiguous stress results: {folder}; exit {result.returncode}')
        cases=json.loads(runs[0].read_text())['cases']
        loaded=[c for c in cases if c['loading']=='actual']
        row=dict(design=design,upper=upper,mount_factor=factor,returncode=result.returncode,
                 report=str(runs[0].parent.relative_to(args.output)/'report.md'),summary=summarize_cases(cases))
        for key in ['apogee_m','peak_powered_speed_m_s','minimum_ascent_stability_cal',
                    'guide_departure_m_s','deployment_speed_m_s','landing_descent_m_s']:
            values=[c.get('metrics',{}).get(key) for c in loaded]
            row[key]=[min(values),max(values)] if all(v is not None for v in values) else None
        rows.append(row)
        save_json(args.output/'comparison.json',rows)
        print('FIN STRESS',design,upper,factor,row['summary']['planned'],flush=True)
    lines=['# Fin finalist uncertainty comparison','','Deterministic corners, not reliability probabilities. '
           'Dummy/logger planned; empty diagnostic. No flight clearance.','',
           '| Design | Upper avionics | Mount factor | Planned pass / 48 | Failure counts |','| --- | --- | --- | --- | --- |']
    for r in rows:
        planned=r['summary']['planned']
        lines.append(f"| [{r['design']}]({r['report']}) | {r['upper']} | {r['mount_factor']} | "
                     f"{planned['passed']} | {planned['failures']} |")
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__=='__main__':
    main()
