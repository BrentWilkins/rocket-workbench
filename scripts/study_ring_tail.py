"""Bounded ring-tail mass and print-geometry comparison; aerodynamic ranking unsupported."""
import argparse
from pathlib import Path

import cadquery as cq
from rocket_workbench.cad import shapes
from rocket_workbench.cli import save_json
from rocket_workbench.config import load_config
from rocket_workbench.nonplanar import ring_tail
from rocket_workbench.orientation import place, measure
from rocket_workbench.provenance import seal_run


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    config = load_config(args.config)
    baseline = shapes(config)['fin-collar']
    args.output.mkdir(parents=True, exist_ok=False)
    save_json(args.output/'resolved-inputs.json', config.model_dump())
    rows = []
    for chord in (0, 5, 10):
        part = baseline if chord == 0 else ring_tail(config, baseline, chord_mm=chord)
        label = 'planar-baseline' if chord == 0 else f'ring-tail-{chord}mm'
        folder = args.output/label
        folder.mkdir()
        cq.exporters.export(part, str(folder/'fin-collar.step'))
        # Analyze the exported STEP, matching the existing planar orientation study.
        part = cq.importers.importStep(str(folder/'fin-collar.step'))
        printable = place(part, 'aft-down')
        orientation = measure(printable)
        cq.exporters.export(printable, str(folder/'fin-collar.stl'), tolerance=.05, angularTolerance=.1)
        row = dict(design=label, chord_mm=chord, wall_mm=1.2 if chord else None,
                   mass_g=part.val().Volume()*config.density.value/1000,
                   added_mass_g=(part.val().Volume()-baseline.val().Volume())*config.density.value/1000,
                   cg_x_mm=part.val().Center().z, orientation=orientation,
                   aerodynamic_model_supported=chord == 0, production_selected=False)
        rows.append(row)
        print(label, round(row['added_mass_g'],3), flush=True)
    save_json(args.output/'comparison.json', rows)
    lines = ['# Ring-tail geometry comparison', '',
             'Experimental 1.2 mm wall rings joining three clipped-delta tips. No flight-performance ranking, '
             'structural qualification or print release. Native planar OpenRocket models do not represent the ring.', '',
             '| Candidate | Added mass g | First-layer area mm² | Fits 236 mm square |', '| --- | --- | --- | --- |']
    for row in rows:
        orientation = row['orientation']
        lines.append(f"| {row['design']} | {row['added_mass_g']:.3f} | "
                     f"{orientation['first_layer_average_area_mm2']:.1f} | {orientation['fits_usable_236mm_square']} |")
    lines += ['', 'Mass is a CAD-density estimate. Ring area increases bed contact, but does not establish adhesion, '
              'impact tolerance or aerodynamic benefit. External CFD and force/moment validation remain required.']
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__ == '__main__':
    main()
