"""Passive dummy-to-logger progression; never infer physical flight clearance."""
import math
from collections import Counter

from .avionics import components, payload_budget

PLANNED_LOADINGS = ('dummy', 'actual')


def dummy_targets(nose_length, sled, config=None):
    rows = components(config)
    payload_mass, payload_cg = payload_budget(nose_length)
    total = payload_mass + sled['mass_g']
    cg = (payload_mass*payload_cg + sled['mass_g']*sled['cg_x_mm'])/total
    return dict(
        basis='complete_sled_assembly',
        axial_datum='Assembled nose tip; positive aft, not STL print coordinates',
        provenance='Provisional component estimates and CAD mass; not measured hardware',
        payload_excluding_sled_g=payload_mass, payload_cg_x_mm=payload_cg,
        shared_sled_mass_g=sled['mass_g'], shared_sled_cg_x_mm=sled['cg_x_mm'],
        complete_sled_mass_g=total, complete_sled_cg_x_mm=cg,
        components=[dict(id=p['id'], target_mass_g=p['mass_g'],
                         center_mm=[p['center_mm'][0], p['center_mm'][1], nose_length+p['center_mm'][2]],
                         keepout_mm=p['dimensions_mm']) for p in rows],
        provisional_matching_tolerances=dict(mass_g=.5, axial_cg_mm=2.0),
        limits='Include all dummy holders, padding and retention in its measured assembly mass. '
               'Match measured logger assembly when available. Matching mass/CG does not establish inertia, '
               'strength, retention, separation, pressure response or flight clearance.',
        flight_cleared=False,
    )


def compare_assemblies(dummy, logger):
    """Compare measured complete removable sleds, using explicit common datum/basis."""
    for record in [dummy, logger]:
        if record.get('basis') != 'complete_sled_assembly':
            raise ValueError('Use complete_sled_assembly including sled, contents, holders and retention')
        if record.get('provenance') != 'measured' or not str(record.get('source', '')).strip():
            raise ValueError('Measured provenance and measurement source are required')
        if record.get('datum') != 'assembled_nose_tip_positive_aft':
            raise ValueError('Both axial CGs must use assembled_nose_tip_positive_aft')
        if record.get('includes_retention') is not True:
            raise ValueError('Include retention in both assembly measurements')
        for key in ['mass_g', 'cg_x_mm']:
            value = record.get(key)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
                raise ValueError(f'Missing or invalid measured {key}')
    mass_error = dummy['mass_g']-logger['mass_g']
    cg_error = dummy['cg_x_mm']-logger['cg_x_mm']
    return dict(mass_difference_g=mass_error, axial_cg_difference_mm=cg_error,
                matches_provisional_bench_tolerances=abs(mass_error) <= .5 and abs(cg_error) <= 2,
                tolerances=dict(mass_g=.5, axial_cg_mm=2), flight_cleared=False,
                next_gate='Check full-rocket measured mass/CG and physical retention/recovery; rerun actual configuration')


def summarize_cases(cases):
    """Keep diagnostic empty failures visible without calling them planned flights."""
    def summary(group):
        return dict(cases=len(group), completed=sum(c['execution']=='completed' for c in group),
                    passed=sum(c['execution']=='completed' and c['evaluation']['criteria_status'] ==
                               'meets configured simulation criteria' for c in group),
                    failures=dict(Counter(check['metric'] for c in group for check in c['evaluation']['checks']
                                          if check['passed'] is not True)),
                    warning_cases=sum(bool(c.get('warnings') or c.get('load_warnings')) for c in group))
    return dict(planned_loadings=list(PLANNED_LOADINGS),
        planned=summary([c for c in cases if c['loading'] in PLANNED_LOADINGS]),
        diagnostic_empty=summary([c for c in cases if c['loading']=='empty']), flight_cleared=False)
