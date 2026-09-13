"""Compare completed mesh diagnostics; never infer validation from similar drag."""
import argparse
import hashlib
import json
from pathlib import Path

from cfd_audit import audit


def compare(cases):
    if len(cases) < 2 or len(set(map(Path.resolve, cases))) != len(cases):
        raise ValueError('Require at least two distinct completed cases')
    rows = []
    signatures = []
    for case in cases:
        spec = json.loads((case / 'case-spec.json').read_text())
        result = audit(case)
        if not result['solver_completed'] or not result['requested_iterations_completed']:
            raise ValueError(f'Case is not complete: {case}')
        signature = {key: spec[key] for key in ('design', 'speed_m_s', 'alpha_deg',
                     'reference_area_m2', 'reference_length_m', 'moment_origin_m')}
        signature['image'] = json.loads((case / 'image.json').read_text())['Id']
        signature['axes'] = result['reported_axes']
        # Only blockMeshDict may differ in this background-grid diagnostic.
        for relative in ('constant/triSurface/rocket.stl', 'constant/transportProperties',
                         'constant/turbulenceProperties', 'system/snappyHexMeshDict',
                         'system/fvSchemes', 'system/fvSolution', 'system/controlDict',
                         '0/U', '0/p', '0/k', '0/omega', '0/nut'):
            signature[relative] = hashlib.sha256((case / relative).read_bytes()).hexdigest()
        signatures.append(signature)
        rows.append(dict(case=str(case), cell_mm=spec['cell_mm'], **result))
    if any(signature != signatures[0] for signature in signatures[1:]):
        raise ValueError('Geometry, physics, solver, axes or reference inputs differ; not an isolated grid comparison')
    rows.sort(key=lambda row: row['cell_mm'], reverse=True)
    if len({row['cell_mm'] for row in rows}) != len(rows):
        raise ValueError('Grid spacings must be distinct')
    for previous, current in zip(rows, rows[1:]):
        cd0 = previous['coefficient_statistics']['Cd']['mean']
        cd1 = current['coefficient_statistics']['Cd']['mean']
        current['cd_change_from_coarser_percent'] = 100 * (cd1 - cd0) / abs(cd0) if cd0 else None
    return dict(cases=rows, common_inputs=signatures[0], accepted_for_design=False,
                interpretation='Diagnostic only: spacing is the background grid, not a measured effective mesh size. '
                'No Richardson extrapolation or grid-convergence index is claimed. '
                'Check symmetry, iterative convergence, wall resolution, domain sensitivity and benchmarks separately.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', type=Path, action='append', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = compare(args.case)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / 'comparison.json').write_text(json.dumps(result, indent=2) + '\n')
    lines = ['# CFD background-grid diagnostics', '', result['interpretation'], '',
             '| Background spacing mm | Cd | Change from coarser % | Settled | Zero-angle symmetry |',
             '| --- | --- | --- | --- | --- |']
    for row in result['cases']:
        change = row.get('cd_change_from_coarser_percent')
        delta = '—' if change is None else f'{change:.3f}'
        lines.append(f"| {row['cell_mm']:g} | {row['coefficient_statistics']['Cd']['mean']:.6f} | "
                     f"{delta} | {row['tail_settled_screen']} | {row['zero_angle_symmetry_screen']} |")
    lines += ['', 'Source cases:'] + [f"- `{row['case']}`" for row in result['cases']]
    (args.output / 'report.md').write_text('\n'.join(lines) + '\n')


if __name__ == '__main__':
    main()
