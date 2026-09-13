"""Bounded planar insertion-clearance screen for proposed M2 insert bosses.

No production CAD or flight mass is changed. This is not a retention-strength test.
"""
import argparse
import itertools
import json
import math
from pathlib import Path

from rocket_workbench.config import load_config


def circle_rectangle_clearance(x, y, radius, rectangle):
    xmin, xmax, ymin, ymax = rectangle
    dx = max(xmin - x, 0, x - xmax)
    dy = max(ymin - y, 0, y - ymax)
    return math.hypot(dx, dy) - radius


def screen(config):
    # Same conservative insertion projections used by avionics.fit_report.
    rectangles = [(-13, 13, -13, 13), (-14, 14, -12, -4)]
    boss_radius = 3.1  # Conservative 3.6 mm insert + 2 x 1.3 mm wall.
    sleeve_radius = config.geometry.mm('body_id') / 2 - config.geometry.mm('clearance')
    center_radius = sleeve_radius - boss_radius
    positions = []
    for angle in range(0, 360, 10):
        x, y = (center_radius * f(math.radians(angle)) for f in (math.cos, math.sin))
        clearance = min(circle_rectangle_clearance(x, y, boss_radius, r) for r in rectangles)
        positions.append(dict(angle_deg=angle, x_mm=x, y_mm=y, clearance_mm=clearance))
    feasible = []
    for group in itertools.combinations(positions, 3):
        angles = [p['angle_deg'] for p in group]
        gaps = [angles[1]-angles[0], angles[2]-angles[1], 360+angles[0]-angles[2]]
        # Center strictly inside support triangle, no near-coincident screw pair.
        if min(gaps) < 60 or max(gaps) >= 180:
            continue
        clearance = min(p['clearance_mm'] for p in group)
        if clearance < .2:
            continue
        feasible.append(dict(angles_deg=angles, minimum_insertion_clearance_mm=clearance,
                             largest_angular_gap_deg=max(gaps)))
    feasible.sort(key=lambda row: (-row['minimum_insertion_clearance_mm'], row['largest_angular_gap_deg']))
    return dict(design=config.name, boss_diameter_mm=2*boss_radius, center_radius_mm=center_radius,
                position_screen=positions, feasible_patterns=feasible, selected_for_production=False,
                limitations=['Conservative straight-insertion projections, not full CAD validation',
                             'No hardware mass, screw access, pull-out or cap bending qualification',
                             'New cap holes, seal interface and old boss removal require a CAD revision',
                             '0.2 mm clearance is a screening allowance, not a measured printer tolerance'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = screen(load_config(args.config))
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output/'comparison.json').write_text(json.dumps(result, indent=2)+'\n')
    lines = ['# Bay-cap insert-boss placement screen', '',
             'Proposed 6.2 mm bosses; production CAD and flight studies remain unchanged.', '',
             f"Feasible three-boss patterns in the 10-degree grid: {len(result['feasible_patterns'])}.", '',
             '| Angles deg | Minimum insertion clearance mm | Largest angular gap deg |',
             '| --- | --- | --- |']
    for row in result['feasible_patterns'][:10]:
        lines.append(f"| {row['angles_deg']} | {row['minimum_insertion_clearance_mm']:.3f} | "
                     f"{row['largest_angular_gap_deg']} |")
    lines += ['', 'Limitations:'] + ['- '+s for s in result['limitations']]
    (args.output/'report.md').write_text('\n'.join(lines)+'\n')
    print(lines[4])


if __name__ == '__main__':
    main()
