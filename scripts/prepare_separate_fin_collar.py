"""Export a round collar and one flat-print fin for manual assembly."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import cadquery as cq

from rocket_workbench.separable_fins import parts, printable_parts
from scripts.prepare_tip_refinement import refined_config


def build(output: Path) -> None:
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f'Use an empty output directory: {output}')
    output.mkdir(parents=True, exist_ok=True)
    config = refined_config()
    collar, fin = parts(config)
    printable_collar, printable_fin = printable_parts(config)
    solids = {'round-collar': collar, 'single-fin': fin}
    for name, solid in solids.items():
        if not solid.val().isValid() or len(solid.val().Solids()) != 1:
            raise ValueError(f'{name} is not one valid solid')
        cq.exporters.export(solid, str(output / f'{name}.step'))
    for name, solid in [('round-collar', printable_collar),
                        ('single-fin', printable_fin)]:
        cq.exporters.export(solid, str(output / f'{name}.stl'),
                            tolerance=.05, angularTolerance=.1)

    assembly = cq.Assembly(name='separate-fin-collar-fit-reference')
    assembly.add(collar, name='round-collar', color=cq.Color('gray'))
    for angle in (0, 120, 240):
        assembly.add(fin.rotate((0, 0, 0), (0, 0, 1), angle),
                     name=f'fin-{angle}', color=cq.Color('green'))
    assembly.export(str(output / 'assembled-fit-reference.step'))

    g = config.geometry
    summary = {
        'status': 'separate print and manual assembly review; no flight qualification',
        'print_quantities': {'round-collar.stl': 1, 'single-fin.stl': 3},
        'print_orientation': {'round-collar': 'aft end down', 'single-fin': 'flat on broad side'},
        'manual_root_fillets': True,
        'modeled_root_fillets': False,
        'geometry_mm': {
            'collar_outer_diameter': g.mm('body_od') + 2 * (g.mm('clearance') + g.mm('wall')),
            'collar_inner_diameter': g.mm('body_od') + 2 * g.mm('clearance'),
            'collar_length': g.mm('collar_length'),
            'fin_thickness': g.mm('fin_thickness'),
            'fin_span': g.mm('fin_span'),
            'fin_root_length': g.mm('fin_root') - 2,
        },
        'cad_volume_mm3': {name: round(solid.val().Volume(), 3)
                           for name, solid in solids.items()},
    }
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    (output / 'config.json').write_text(config.model_dump_json(indent=2) + '\n')
    manifest = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(output.iterdir()) if path.is_file()
                and path.name != 'manifest.json'}
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    build(args.output)
