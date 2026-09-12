"""Create a documented follow-up experiment, not a silent motor-size upgrade."""
import json
from pathlib import Path
from rocket_workbench.config import load_config
from rocket_workbench.sweep import variant

root = Path(__file__).resolve().parents[1]
base = load_config(root/'examples/baseline.yaml')
candidate = variant(base, {'wall': .8, 'fin_thickness': 1.2},
                    'Light-wall comparison only; print strength remains unverified')
data = candidate.model_dump()
data['name'] = 'c5-light-study'
data['motors'] = [dict(designation='C5', delay_s=3,
    digest='73a9ed8bd883e2de7c1684f76fb54ab3',
    max_liftoff_mass=dict(value=226, unit='g', provenance='manufacturer specification',
                        source='https://estesrockets.com/products/c5-3-engines ; Technical Specifications, checked 2026-09-12'))]
(root/'examples/c5-study.yaml').write_text(json.dumps(data, indent=2)+'\n')
standard = base.model_dump()
standard['name'] = 'c5-standard-study'
standard['motors'] = data['motors']
(root/'examples/c5-standard.yaml').write_text(json.dumps(standard, indent=2)+'\n')
