"""Evaluate larger passive recovery within BT-60, retaining provisional packing/mass estimates."""
import argparse
import hashlib
import json
from argparse import Namespace
from pathlib import Path

from rocket_workbench.cli import save_json, workflow
from rocket_workbench.config import Config
from rocket_workbench.progression import summarize_cases
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine
from study_avionics import place_wadding
from study_fin_shapes import variant
from stress_fin_shapes import configuration as mass_case

OPTIONS=[(20,430),(22,460),(24,500)]


def configuration(inches,body,heavy=False):
    base=mass_case(variant('clipped-delta',45,body),heavy,1.5 if heavy else 1.)
    data=base.model_dump()
    data['name']=f'delta-chute{inches}-body{body}-'+('heavy' if heavy else 'nominal')
    g=data['geometry']
    ratio=(inches*25.4/g['chute_diameter']['value'])**2
    # Preserve estimated packed volume per canopy area. Do not silently squeeze
    # a larger canopy into the old envelope or omit its added mass.
    packed=g['chute_packed_length']['value']*ratio*(g['chute_packed_diameter']['value']/32.)**2
    source='Provisional area-scaled recovery study; physical mass/packing/deployment tests required'
    for key,value in [('chute_diameter',inches*25.4),('chute_packed_length',packed),('chute_packed_diameter',32.)]:
        g[key].update(value=value,provenance='estimate',source=source)
    chute=next(i for i in data['purchased_masses'] if i['role']=='chute')
    chute['name']=f'Provisional {inches} inch parachute and lines'
    chute['mass'].update(value=chute['mass']['value']*ratio,provenance='estimate',source=source)
    chute['x'].update(value=g['nose_length']['value']+g['bay_length']['value']+10+packed/2,
                       provenance='estimate',source=source)
    if heavy:
        data['density'].update(value=data['density']['value']*1.2,provenance='estimate',
                               source='Printed mass +20% sensitivity, not measured material density')
        data['chute_cd'].update(value=.6,provenance='estimate',source='Low-drag recovery sensitivity')
        data['payload']['cg_x']['value']+=5
    place_wadding(data)
    return Config.model_validate(data)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    save_json(args.output/'search-spec.json',dict(options=OPTIONS,flights=54,
        profiles=['nominal','upper avionics, mount +50%, print +20%, payload CG +5mm, chute Cd .6'],
        limitations='Two profiles are a recovery-change screen, not replacement for full uncertainty grid. '
                   'Chute mass and packed volume scale with canopy area; 32mm pack diameter provisional.'))
    rows=[]
    with Engine() as engine:
        for inches,body in OPTIONS:
            for heavy in [False,True]:
                config=configuration(inches,body,heavy)
                folder=args.output/config.name
                folder.mkdir()
                path=folder/'config.yaml'
                save_json(path,config.model_dump())
                save_json(folder/'resolved-inputs.json',config.model_dump())
                digest=hashlib.sha256(json.dumps(config.model_dump(),sort_keys=True).encode()).hexdigest()
                save_json(folder/'manifest.json',dict(configuration_sha256=digest,command='recovery-screen'))
                workflow(Namespace(command='simulate',strict=False),config,path,folder,digest,engine)
                cases=json.loads((folder/'results.json').read_text())['cases']
                row=dict(design=config.name,summary=summarize_cases(cases))
                loaded=[c for c in cases if c['loading']=='actual']
                for key in ['apogee_m','peak_powered_speed_m_s','landing_descent_m_s','landing_displacement_m',
                            'minimum_ascent_stability_cal','guide_departure_m_s','deployment_speed_m_s']:
                    values=[c.get('metrics',{}).get(key) for c in loaded]
                    row[key]=[min(values),max(values)] if all(v is not None for v in values) else None
                rows.append(row)
                save_json(args.output/'comparison.json',rows)
                print('RECOVERY',config.name,row['summary']['planned'],flush=True)
    lines=['# Larger passive recovery screen','','Provisional canopy mass and packing estimates. '
           'Not full uncertainty coverage or physical clearance.','',
           '| Design | Planned passes / 6 | Loaded descent m/s | Loaded altitude m |','| --- | --- | --- | --- |']
    for r in rows:
        lines.append(f"| [{r['design']}]({r['design']}/report.md) | {r['summary']['planned']['passed']} | "
                     f"{r['landing_descent_m_s']} | {r['apogee_m']} |")
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__=='__main__':
    main()
