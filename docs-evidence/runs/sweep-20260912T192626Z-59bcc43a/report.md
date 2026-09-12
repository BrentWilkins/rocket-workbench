# Bounded design sweep

Search: Follow-up: commercial 18 mm C5-3 with original 1.2 mm shell / 1.6 mm fins; keep stronger-print candidate
dimensions while assessing low-altitude and payload tradeoffs. Strength remains unverified.

No incomplete design is ranked as eligible for flight. Nominal simulation passes are identified separately.

| Design                             | Parameters (mm)                                                   | Status    | Passing cases | Empty/dummy/actual motor options                           |
| ---------------------------------- | ----------------------------------------------------------------- | --------- | ------------: | ---------------------------------------------------------- |
| [design-000](design-000/report.md) | {'body_length': 300.0, 'fin_span': 45.0, 'chute_diameter': 381.0} | evaluated |             2 | {'empty': [], 'dummy': [], 'actual': []}                   |
| [design-001](design-001/report.md) | {'body_length': 300.0, 'fin_span': 55.0, 'chute_diameter': 381.0} | evaluated |             5 | {'empty': [], 'dummy': ['C5-3'], 'actual': ['C5-3']}       |
| [design-002](design-002/report.md) | {'body_length': 340.0, 'fin_span': 45.0, 'chute_diameter': 381.0} | evaluated |             5 | {'empty': [], 'dummy': ['C5-3'], 'actual': ['C5-3']}       |
| [design-003](design-003/report.md) | {'body_length': 340.0, 'fin_span': 55.0, 'chute_diameter': 381.0} | evaluated |             6 | {'empty': ['C5-3'], 'dummy': ['C5-3'], 'actual': ['C5-3']} |
| [design-004](design-004/report.md) | {'body_length': 380.0, 'fin_span': 45.0, 'chute_diameter': 381.0} | evaluated |             5 | {'empty': [], 'dummy': ['C5-3'], 'actual': ['C5-3']}       |
| [design-005](design-005/report.md) | {'body_length': 380.0, 'fin_span': 55.0, 'chute_diameter': 381.0} | evaluated |             6 | {'empty': ['C5-3'], 'dummy': ['C5-3'], 'actual': ['C5-3']} |

2 designs support all loadings under the nominal configured criteria.

If zero: this bounded search found no qualifying design; it is not proof that no 18 mm design can work. See
docs/REVIEW.md for tradeoff experiments.
