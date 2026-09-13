"""Compare actual exported fin-collar STEP geometry on the intended aft-down bed."""
import argparse
import json
from pathlib import Path

import cadquery as cq
from rocket_workbench.cli import save_json
from rocket_workbench.orientation import place, measure
from rocket_workbench.provenance import seal_run


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    rows=[]
    for design in json.loads((args.study/'comparison.json').read_text()):
        source=args.study/design['design']/'cad/fin-collar.step'
        part=cq.importers.importStep(str(source))
        if not part.val().isValid() or len(part.solids().vals())!=1:
            raise ValueError(f'Invalid or disconnected collar: {source}')
        row=dict(design=design['design'],source=str(source),orientation='aft-down',
                 **measure(place(part,'aft-down')))
        rows.append(row)
        save_json(args.output/'comparison.json',rows)
        print('ORIENTATION',row['design'],row['first_layer_average_area_mm2'],flush=True)
    lines=['# Fin-shape print orientation comparison','','Aft-down, 0.2 mm first-layer slab. '
           'Geometric screening only: not adhesion, support-volume or strength certification.','',
           '| Design | First-layer average area mm² | Downward area above bed mm² | Fits 236 mm square |',
           '| --- | --- | --- | --- |']
    for r in rows:
        lines.append(f"| {r['design']} | {r['first_layer_average_area_mm2']:.1f} | "
                     f"{r['downward_area_above_first_layer_mm2']:.1f} | {r['fits_usable_236mm_square']} |")
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    seal_run(args.output)


if __name__=='__main__':
    main()
