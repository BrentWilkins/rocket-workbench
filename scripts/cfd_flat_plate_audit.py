"""Post-process a retained TMR flat-plate preflight without accepting design CFD."""

import argparse
import json
import re
from pathlib import Path

import numpy as np


VECTOR=re.compile(r'\(([-+0-9.eE]+)\s+([-+0-9.eE]+)\s+([-+0-9.eE]+)\)')


def vector_list(text: str, marker: str) -> np.ndarray:
    start=text.index(marker)
    section=text[start:]
    count_match=re.search(r'nonuniform\s+List<vector>\s+(\d+)\s*\(',section)
    if not count_match:
        raise ValueError(f'No nonuniform vector list after {marker}')
    count=int(count_match.group(1))
    values=np.asarray([[float(item) for item in match]
                       for match in VECTOR.findall(section[count_match.end():])[:count]])
    if values.shape != (count,3):
        raise ValueError(f'Expected {count} vectors after {marker}, found {len(values)}')
    return values


def numeric_pairs(path: Path) -> np.ndarray:
    pairs=[]
    for line in path.read_text().splitlines():
        fields=line.split()
        if len(fields)>=2:
            try:
                pairs.append((float(fields[0]),float(fields[1])))
            except ValueError:
                pass
    if not pairs:
        raise ValueError(f'No numeric pairs in {path}')
    return np.asarray(pairs)


def final_time(case: Path) -> Path:
    times=[path for path in case.iterdir() if path.is_dir() and path.name.isdigit()]
    if not times:
        raise ValueError('No completed numeric solution time')
    return max(times,key=lambda path:int(path.name))


def audit(case: Path,data: Path) -> dict:
    spec=json.loads((case/'benchmark-spec.json').read_text())
    with np.load(case/'tmr-grid.npz') as grid:
        x,y=grid['x'],grid['y']
    time=final_time(case)
    velocity=vector_list((time/'U').read_text(),'internalField')[:,0]
    nj,ni=x.shape
    velocity=velocity.reshape(nj-1,ni-1)
    wall_shear=vector_list((time/'wallShearStress').read_text(),'plate')[:,0]
    leading=spec['mesh']['plate_leading_edge_i']
    if len(wall_shear) != ni-1-leading:
        raise ValueError('Wall-shear patch size does not match retained grid')
    nu=spec['conditions']['nu_m2_s']; speed=spec['conditions']['U_m_s']
    rows=[]
    cutoffs=(0.99,0.995,0.999)
    cutoff_retheta={cutoff:[] for cutoff in cutoffs}
    for offset,i in enumerate(range(leading,ni-1)):
        y_faces=(y[:,i]+y[:,i+1])/2
        dy=np.diff(y_faces)
        # Preserve overshoot/undershoot evidence. Clipping made alternating outer-flow
        # errors contribute only positive momentum thickness and biased Re_theta high.
        ratio=velocity[:,i]/speed
        theta=float(np.sum(ratio*(1-ratio)*dy))
        for cutoff in cutoffs:
            indices=np.flatnonzero(ratio>=cutoff)
            edge=int(indices[0]) if len(indices) else len(ratio)-1
            cutoff_theta=float(np.sum(ratio[:edge+1]*(1-ratio[:edge+1])*dy[:edge+1]))
            cutoff_retheta[cutoff].append(speed*cutoff_theta/nu)
        rows.append((float((x[0,i]+x[0,i+1])/2),speed*theta/nu,
                     float(-2*wall_shear[offset]/speed**2)))
    values=np.asarray(rows)
    reference=numeric_pairs(data/'cf_K-S.dat')
    official_sst=numeric_pairs(data/'sst-cf_cfl3d.dat')
    typical_retheta=numeric_pairs(data/'retheta_variation_typical.dat')
    mapped_retheta=np.interp(values[:,0],typical_retheta[:,0],typical_retheta[:,1])
    selected=(mapped_retheta>=4000)&(mapped_retheta<=13000)
    reference_cf=np.interp(mapped_retheta[selected],reference[:,0],reference[:,1])
    relative=np.abs(values[selected,2]-reference_cf)/reference_cf
    official_sst_cf=np.interp(mapped_retheta[selected],official_sst[:,1],official_sst[:,0])
    sst_relative=np.abs(values[selected,2]-official_sst_cf)/official_sst_cf
    retheta_relative=np.abs(values[selected,1]-mapped_retheta[selected])/mapped_retheta[selected]
    cutoff_sensitivity={}
    for cutoff,retheta_values in cutoff_retheta.items():
        retheta_values=np.asarray(retheta_values)
        cutoff_selected=(retheta_values>=4000)&(retheta_values<=13000)
        cutoff_reference=np.interp(retheta_values[cutoff_selected],reference[:,0],reference[:,1])
        cutoff_error=np.abs(values[cutoff_selected,2]-cutoff_reference)/cutoff_reference
        cutoff_retheta_error=(
            np.abs(retheta_values[selected]-mapped_retheta[selected])/mapped_retheta[selected]
        )
        cutoff_sensitivity[f'{cutoff:.3f}']={
            'comparison_points':int(cutoff_selected.sum()),
            'maximum_cf_relative_error':float(cutoff_error.max()) if len(cutoff_error) else None,
            'mean_cf_relative_error':float(cutoff_error.mean()) if len(cutoff_error) else None,
            'engineering_5_percent_screen':bool(len(cutoff_error) and np.all(cutoff_error<=0.05)),
            'minimum_retheta':float(retheta_values.min()),
            'maximum_retheta':float(retheta_values.max()),
            'maximum_retheta_relative_error_vs_tmr_typical':(
                float(cutoff_retheta_error.max()) if len(cutoff_retheta_error) else None),
            'mean_retheta_relative_error_vs_tmr_typical':(
                float(cutoff_retheta_error.mean()) if len(cutoff_retheta_error) else None),
            'retheta_5_percent_screen':bool(
                len(cutoff_retheta_error) and np.all(cutoff_retheta_error<=0.05)),
        }
    edge_momentum_gate=bool(
        cutoff_sensitivity
        and all(item['retheta_5_percent_screen'] for item in cutoff_sensitivity.values())
    )
    execution=json.loads((case/'execution.json').read_text())
    solver_indices=[index for index,record in enumerate(execution) if 'simpleFoam' in record['stage']]
    if len(solver_indices)!=1:
        raise ValueError(f'Expected one simpleFoam execution stage, found {len(solver_indices)}')
    solver_index=solver_indices[0]
    solver_name=execution[solver_index]['stage'].split()[0]
    solver_log=(case/f'{solver_index}-{solver_name}.log').read_text()
    residuals={name:[float(value) for value in re.findall(
        rf'Solving (?:for )?{name}, Initial residual = ([-+0-9.eE]+)',solver_log)]
        for name in ('Ux','Uy','p','omega','k')}
    final_initial={name:(series[-1] if series else None) for name,series in residuals.items()}
    iterative_screen=bool(residuals and all(value is not None and value<=1e-7
                                             for value in final_initial.values()))
    return {
        'benchmark':spec['benchmark'],'solution_time':time.name,
        'comparison_points':int(selected.sum()),
        'cf_vs_karman_schoenherr_using_tmr_x_to_retheta':{
            'maximum_relative_error':float(relative.max()) if len(relative) else None,
            'mean_relative_error':float(relative.mean()) if len(relative) else None,
            'engineering_5_percent_screen':bool(len(relative) and np.all(relative<=0.05)),
        },
        'integrated_retheta_vs_tmr_typical':{
            'maximum_relative_error':float(retheta_relative.max()) if len(retheta_relative) else None,
            'mean_relative_error':float(retheta_relative.mean()) if len(retheta_relative) else None,
            'screen_passed':bool(len(retheta_relative) and np.all(retheta_relative<=0.05)),
            'governing':False,
            'diagnostic_note':(
                'Full finite-domain integration is tail-biased when outer velocity differs '
                'slightly from U-infinity; preserve as a diagnostic, not an acceptance metric.'),
        },
        'edge_velocity_cutoff_sensitivity':cutoff_sensitivity,
        'edge_truncated_momentum_thickness_gate':edge_momentum_gate,
        'cf_vs_official_cfl3d_sstm_using_tmr_x_to_retheta':{
            'maximum_relative_error':float(sst_relative.max()) if len(sst_relative) else None,
            'mean_relative_error':float(sst_relative.mean()) if len(sst_relative) else None,
            'diagnostic_only':True,
        },
        'final_initial_residuals':final_initial,'iterative_1e-7_screen':iterative_screen,
        'numerical_phase':spec['numerical_phase'],
        'limitations':['Cell-centred midpoint integration of momentum thickness is an extraction approximation.',
                       'Velocity is not clipped; outer-flow oscillations require the separate fail-closed quality audit.',
                       'Edge-cutoff sensitivity uses first crossing of 99, 99.5, and 99.9 percent U-infinity; no single cutoff can establish acceptance.',
                       'First-order preflight is not the final benchmark discretization.',
                       'Karman-Schoenherr is a correlation with unclear experimental uncertainty, not exact truth.'],
        'accepted_for_design':False,
        'benchmark_gate_passed':False,
        'profiles':[{'x_m':float(row[0]),'Re_theta':float(row[1]),'Cf':float(row[2])}
                    for row in values],
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',required=True,type=Path)
    parser.add_argument('--benchmark-data',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    result=audit(args.case,args.benchmark_data)
    (args.output/'flat-plate-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in (
        'comparison_points','cf_vs_karman_schoenherr_using_tmr_x_to_retheta',
        'cf_vs_official_cfl3d_sstm_using_tmr_x_to_retheta',
        'integrated_retheta_vs_tmr_typical','edge_velocity_cutoff_sensitivity',
        'iterative_1e-7_screen',
        'benchmark_gate_passed')}))


if __name__=='__main__':
    main()
