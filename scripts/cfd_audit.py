"""Audit retained CFD coefficients without confusing solver completion with validation."""
import argparse
import json
from pathlib import Path

import numpy as np


def audit(case):
    spec=json.loads((case/'case-spec.json').read_text())
    stages=json.loads((case/'execution.json').read_text())
    coefficients=case/'postProcessing/forces/0/coefficient.dat'
    lines=coefficients.read_text().splitlines()
    columns=next(line.lstrip('#').split() for line in lines if line.startswith('# Time'))
    data=np.loadtxt(coefficients)
    if data.ndim!=2 or len(data)<100 or not np.isfinite(data).all():
        raise ValueError('Require at least 100 finite coefficient records')
    rows={name:data[:,i] for i,name in enumerate(columns)}
    tail={name:values[-100:] for name,values in rows.items() if name!='Time'}
    stats={name:dict(mean=float(values.mean()),peak_to_peak=float(np.ptp(values))) for name,values in tail.items()}
    completed=all(s.get('stage_passed') for s in stages) and any(s['stage']=='simpleFoam' for s in stages)
    iteration_complete=rows['Time'][-1]>=spec['iterations']
    settled=all(stats[name]['peak_to_peak']<=max(.001,.01*abs(stats[name]['mean']))
                for name in ['Cd','Cl','Cs','CmPitch','CmYaw','CmRoll'])
    symmetry=None
    if spec['alpha_deg']==0:
        symmetry=all(abs(stats[name]['mean'])<=.01 for name in ['Cl','Cs','CmPitch','CmYaw','CmRoll'])
    axes={line.split(':',1)[0].lstrip('#').strip():line.split(':',1)[1].strip()
          for line in lines if line.startswith('#') and ':' in line}
    return dict(design=spec['design'],solver_completed=completed,requested_iterations_completed=bool(iteration_complete),
        last_iteration=float(rows['Time'][-1]),tail_samples=100,coefficient_statistics=stats,
        tail_settled_screen=bool(settled),zero_angle_symmetry_screen=symmetry,reported_axes=axes,
        thresholds='Tail peak-to-peak <= max(0.001, 1% of mean); zero-angle lateral/moment magnitudes <=0.01. '
                   'Provisional diagnostic thresholds, not uncertainty bounds or certification.',
        accepted_for_design=False,
        remaining=['Grid convergence','Domain and wall-resolution sensitivity','Benchmark comparison',
                   'Resolve zero-angle asymmetry when flagged','Angle-of-attack/speed coverage',
                   'Physical validation remains separate'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    result=audit(args.case)
    result['source_case']=str(args.case)
    (args.output/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
    lines=['# CFD pilot audit','','Completed flow solution is not accepted design evidence.','',
           f"Solver completed: {result['solver_completed']}. Last iteration: {result['last_iteration']:.0f}.",
           f"Last-100-sample settling screen: {result['tail_settled_screen']}.",
           f"Zero-angle lateral/moment symmetry screen: {result['zero_angle_symmetry_screen']}.",'',
           '| Coefficient | Last-100 mean | Peak-to-peak |','| --- | --- | --- |']
    for name in ['Cd','Cl','Cs','CmPitch','CmRoll','CmYaw']:
        s=result['coefficient_statistics'][name]
        lines.append(f"| {name} | {s['mean']:.6f} | {s['peak_to_peak']:.6f} |")
    lines+=['','Axes are taken from the solver output, not assumed from input keywords. '
            'v2512 reports pitch about negative Z for this drag/lift basis. No coefficients have been transferred '
            'to flight models. Grid/wall/domain checks and benchmark comparison remain outstanding.']
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({key:result[key] for key in ['solver_completed','tail_settled_screen','zero_angle_symmetry_screen']}))


if __name__=='__main__':
    main()
