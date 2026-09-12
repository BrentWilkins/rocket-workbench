"""Deterministic candidate shortlist based on the documented completed sweeps."""
import json
from pathlib import Path
from rocket_workbench.config import load_config
from rocket_workbench.sweep import variant

root = Path(__file__).resolve().parents[1]
base = load_config(root/'examples/c5-standard.yaml')
original = load_config(root/'examples/baseline.yaml')
for name, length, span, chute in [('candidate-compact',340,55,381), ('candidate-stable',380,55,381), ('candidate-small-fins',380,45,381), ('candidate-recovery',380,55,457)]:
    candidate = variant(base, dict(body_length=length, fin_span=span, chute_diameter=chute),
                        'Review shortlist selected from bounded C5 comparison; no physical validation')
    data = candidate.model_dump()
    for key, value in dict(motor_mount_id=18.0, motor_mount_od=18.7, motor_mount_length=69.85).items():
        data['geometry'][key].update(value=value, source='Estes BT-20 / #3158 nominal interface; 2.75 inch mount length from product listing, ID/OD estimate pending caliper check')
    for item in data['purchased_masses']:
        if item['role'] == 'mount':
            item['x']['value'] = data['geometry']['nose_length']['value']+length-3.2-69.85/2
    data['name'] = name
    data['motors'] = [m.model_dump() for m in original.motors] + data['motors']
    (root/f'examples/{name}.yaml').write_text(json.dumps(data, indent=2)+'\n')
    if name == 'candidate-stable':
        data['motors'] = base.model_dump()['motors']
        (root/'examples/candidate-stress.yaml').write_text(json.dumps(data, indent=2)+'\n')
    if name == 'candidate-recovery':
        data['motors'] = base.model_dump()['motors']
        (root/'examples/candidate-recovery-stress.yaml').write_text(json.dumps(data, indent=2)+'\n')
