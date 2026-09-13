"""Combine completed, nonoverlapping recovery batches after an interrupted orchestrator."""
import argparse
import json
from pathlib import Path

from rocket_workbench.cli import save_json
from rocket_workbench.provenance import seal_run


def summarize(studies, expected_designs=None):
    profiles={}
    for study in studies:
        for row in json.loads((study/'comparison.json').read_text()):
            key=(row['design'],row['upper'],row['mount_factor'])
            if key in profiles:
                raise ValueError('Overlapping uncertainty batches; do not double-count')
            profiles[key]=dict(row,source_study=str(study))
    designs=sorted({key[0] for key in profiles})
    if expected_designs is not None and set(designs) != set(expected_designs):
        raise ValueError('Designs do not match the declared study inventory')
    if expected_designs is None and len(designs)!=3:
        raise ValueError('Expected three recovery designs')
    rows=[]
    for design in designs:
        group=[row for key,row in profiles.items() if key[0]==design]
        if {(r['upper'],r['mount_factor']) for r in group}!={(u,m) for u in [False,True] for m in [1.,1.5]}:
            raise ValueError(f'Incomplete uncertainty profiles for {design}')
        planned={key:sum(r['summary']['planned'][key] for r in group) for key in ['cases','completed','passed']}
        diagnostic={key:sum(r['summary']['diagnostic_empty'][key] for r in group) for key in ['cases','completed','passed']}
        if planned['cases']!=192 or diagnostic['cases']!=96:
            raise ValueError('Incomplete corner count')
        row=dict(design=design,planned=planned,diagnostic_empty=diagnostic,
                 all_planned_numeric_gates_pass=planned['passed']==planned['completed']==192,
                 physical_clearance=False,profiles=group)
        for key in ['apogee_m','peak_powered_speed_m_s','minimum_ascent_stability_cal',
                    'guide_departure_m_s','deployment_speed_m_s','landing_descent_m_s']:
            bounds=[r[key] for r in group]
            row[key]=[min(v[0] for v in bounds),max(v[1] for v in bounds)] if all(v is not None for v in bounds) else None
        rows.append(row)
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study',action='append',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    rows=summarize(args.study)
    args.output.mkdir(parents=True,exist_ok=False)
    save_json(args.output/'comparison.json',rows)
    lines=['# Full recovery uncertainty comparison','','Three designs × 288 deterministic cases = 864 flights. '
           '192 planned dummy/logger and 96 diagnostic-empty cases per design. These are not reliability probabilities.',
           'No CFD acceptance or physical launch clearance is implied.','',
           '| Design | Planned passes / 192 | Loaded altitude m | Loaded speed m/s | Loaded descent m/s |',
           '| --- | --- | --- | --- | --- |']
    for r in rows:
        def bounds(key):
            v=r[key]
            return 'unavailable' if v is None else f'{v[0]:.2f}–{v[1]:.2f}'
        lines.append(f"| {r['design']} | {r['planned']['passed']} | {bounds('apogee_m')} | "
                     f"{bounds('peak_powered_speed_m_s')} | {bounds('landing_descent_m_s')} |")
    lines+=['','Inputs: nominal/upper avionics, mount mass ×1/1.5, printed mass ×1/1.2, '
            'payload CG ±5 mm, chute Cd 0.6/0.9, winds 0/2/4 m/s. '
            'Canopy mass and packed volume are provisional area-scaled estimates.']
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__=='__main__':
    main()
