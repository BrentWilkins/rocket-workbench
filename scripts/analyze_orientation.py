"""Compare six fixed orientations per part and retain oriented meshes for slicing."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import cadquery as cq

from rocket_workbench.cad import shapes
from rocket_workbench.config import load_config
from rocket_workbench.orientation import ORIENTATIONS, measure, nondominated, place


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config', type=Path)
    parser.add_argument('--output', type=Path, default=Path('runs')/('orientation-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')))
    args = parser.parse_args()
    config = load_config(args.config)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output/'config.json').write_text(json.dumps(config.model_dump(), indent=2)+'\n')
    records = []
    lines = ['# Print-orientation screen', '',
             '0.2 mm first-layer slab, 45° overhang proxy. Contact excludes brim/supports. No adhesion or strength qualification.', '',
             '| Part | Orientation | First layer mm² | Downward area mm² | Height mm | Geometric Pareto |',
             '|---|---|---:|---:|---:|---|']
    for name, part in shapes(config).items():
        rows = []
        for orientation in ORIENTATIONS:
            placed = place(part, orientation)
            row = dict(part=name, orientation=orientation, **measure(placed))
            folder = args.output/orientation/'cad'
            folder.mkdir(parents=True, exist_ok=True)
            cq.exporters.export(placed, str(folder/f'{name}.stl'), tolerance=.05, angularTolerance=.1)
            rows.append(row)
        frontier = nondominated(rows)
        for r in rows:
            r['geometric_pareto'] = r in frontier
            lines.append(f"| {name} | {r['orientation']} | {r['first_layer_average_area_mm2']:.2f} | {r['downward_area_above_first_layer_mm2']:.2f} | {r['height_mm']:.2f} | {r['geometric_pareto']} |")
        records.extend(rows)
        print(f'{name}: six orientations evaluated', flush=True)
    (args.output/'analysis.json').write_text(json.dumps(records, indent=2)+'\n')
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    print(args.output.resolve())


if __name__ == '__main__':
    main()
