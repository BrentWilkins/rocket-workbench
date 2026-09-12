# Bounded design sweep

Search: Initial bounded engineering exploration; paper tube length, fin span, commercial nominal chute sizes in mm

No incomplete design is ranked as eligible for flight. Nominal simulation passes are identified separately.

| Design | Parameters (mm) | Status | Passing cases | Empty/dummy/actual motor options |
|---|---|---|---:|---|
| [design-000](design-000/rejection.json) | {'body_length': 260.0, 'fin_span': 35.0, 'chute_diameter': 305.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-001](design-001/rejection.json) | {'body_length': 260.0, 'fin_span': 35.0, 'chute_diameter': 381.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-002](design-002/rejection.json) | {'body_length': 260.0, 'fin_span': 35.0, 'chute_diameter': 457.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-003](design-003/rejection.json) | {'body_length': 260.0, 'fin_span': 45.0, 'chute_diameter': 305.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-004](design-004/rejection.json) | {'body_length': 260.0, 'fin_span': 45.0, 'chute_diameter': 381.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-005](design-005/rejection.json) | {'body_length': 260.0, 'fin_span': 45.0, 'chute_diameter': 457.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-006](design-006/rejection.json) | {'body_length': 260.0, 'fin_span': 55.0, 'chute_diameter': 305.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-007](design-007/rejection.json) | {'body_length': 260.0, 'fin_span': 55.0, 'chute_diameter': 381.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-008](design-008/rejection.json) | {'body_length': 260.0, 'fin_span': 55.0, 'chute_diameter': 457.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Aft launch-lug sleeve overlaps collar fairing; increase body length [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-009](design-009/report.md) | {'body_length': 300.0, 'fin_span': 35.0, 'chute_diameter': 305.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-010](design-010/report.md) | {'body_length': 300.0, 'fin_span': 35.0, 'chute_diameter': 381.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-011](design-011/rejection.json) | {'body_length': 300.0, 'fin_span': 35.0, 'chute_diameter': 457.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Recovery packing envelope and routing clearance do not fit [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-012](design-012/report.md) | {'body_length': 300.0, 'fin_span': 45.0, 'chute_diameter': 305.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-013](design-013/report.md) | {'body_length': 300.0, 'fin_span': 45.0, 'chute_diameter': 381.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-014](design-014/rejection.json) | {'body_length': 300.0, 'fin_span': 45.0, 'chute_diameter': 457.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Recovery packing envelope and routing clearance do not fit [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-015](design-015/report.md) | {'body_length': 300.0, 'fin_span': 55.0, 'chute_diameter': 305.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-016](design-016/report.md) | {'body_length': 300.0, 'fin_span': 55.0, 'chute_diameter': 381.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-017](design-017/rejection.json) | {'body_length': 300.0, 'fin_span': 55.0, 'chute_diameter': 457.0} | rejected inputs | 0 | 1 validation error for Config
  Value error, Recovery packing envelope and routing clearance do not fit [type=value_error, input_value={'schema_version': 1, 'na...inted_measurements': {}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error |
| [design-018](design-018/report.md) | {'body_length': 340.0, 'fin_span': 35.0, 'chute_diameter': 305.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-019](design-019/report.md) | {'body_length': 340.0, 'fin_span': 35.0, 'chute_diameter': 381.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-020](design-020/report.md) | {'body_length': 340.0, 'fin_span': 35.0, 'chute_diameter': 457.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-021](design-021/report.md) | {'body_length': 340.0, 'fin_span': 45.0, 'chute_diameter': 305.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-022](design-022/report.md) | {'body_length': 340.0, 'fin_span': 45.0, 'chute_diameter': 381.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-023](design-023/report.md) | {'body_length': 340.0, 'fin_span': 45.0, 'chute_diameter': 457.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-024](design-024/report.md) | {'body_length': 340.0, 'fin_span': 55.0, 'chute_diameter': 305.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-025](design-025/report.md) | {'body_length': 340.0, 'fin_span': 55.0, 'chute_diameter': 381.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |
| [design-026](design-026/report.md) | {'body_length': 340.0, 'fin_span': 55.0, 'chute_diameter': 457.0} | evaluated | 0 | {'empty': [], 'dummy': [], 'actual': []} |

0 designs support all loadings under the nominal configured criteria.

If zero: this bounded search found no qualifying design; it is not proof that no 18 mm design can work. See docs/REVIEW.md for tradeoff experiments.
