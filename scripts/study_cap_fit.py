"""Check full CAD fit of bounded insert layouts without revising production exports."""
import argparse
import json
from pathlib import Path

import cadquery as cq
from rocket_workbench.avionics import fit_report, keepouts
from rocket_workbench.cad import shapes
from rocket_workbench.config import load_config


def trial_hardware(config, reroute=False):
    hardware = keepouts(config)
    if reroute:
        n = config.geometry.mm('nose_length')
        # Rotate 4 x 10 transverse allowances to 10 x 4, preserving volume and axial placement.
        hardware['harness'] = cq.Workplane('XY').box(10, 4, 90).translate((6, 10, n+65))
        hardware['retention'] = cq.Workplane('XY').box(10, 4, 60).translate((-6, 10, n+52))
    return hardware


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--reroute', action='store_true', help='Trial equal-volume harness/retention routing above boards')
    args = parser.parse_args()
    config = load_config(args.config)
    args.output.mkdir(parents=True, exist_ok=False)
    baseline = shapes(config)
    base_volume = sum(part.val().Volume() for part in baseline.values())
    rows = []
    hardware = trial_hardware(config, args.reroute)
    for angles in ([30, 150, 270], [0, 100, 260], [10, 170, 270]):
        parts = shapes(config, cap_insert_angles=angles)
        label = '-'.join(map(str, angles))
        folder = args.output / label
        folder.mkdir()
        fit = fit_report(config, parts, hardware=hardware)
        solids = {name: dict(valid=part.val().isValid(), count=len(part.solids().vals()))
                  for name, part in parts.items()}
        for name in ('nose-bay', 'bay-bulkhead'):
            cq.exporters.export(parts[name], str(folder / f'{name}.step'))
        change = (sum(part.val().Volume() for part in parts.values())-base_volume)*config.density.value/1000
        row = dict(angles_deg=angles, fit=fit, solids=solids, printed_mass_change_g=change,
                   rerouted_equal_volume_allowances=args.reroute,
                   added_hardware_mass_g=None, production_selected=False)
        (folder / 'fit.json').write_text(json.dumps(row, indent=2)+'\n')
        rows.append(row)
        print(label, 'fit', fit['passed'], 'printed mass delta', round(change, 3), flush=True)
    (args.output / 'comparison.json').write_text(json.dumps(rows, indent=2)+'\n')
    lines = ['# Experimental bay-cap insert CAD fit', '',
             'TC-M2x3.0 receiving holes; no production geometry or flight mass ledger changed.', '',
             '| Boss angles deg | CAD insertion/installed fit | Printed mass change g |',
             '| --- | --- | --- |']
    for row in rows:
        lines.append(f"| {row['angles_deg']} | {row['fit']['passed']} | {row['printed_mass_change_g']:.3f} |")
    lines += ['', 'Insert/screw/washer mass, tool access, seal effectiveness, pull-out, cap bending and physical '
              'retention are not established by this geometric check. STEP files are trial parts, not print releases.']
    if args.reroute:
        lines += ['', 'Routing trial: harness and retention keepouts are rotated in cross-section from 4 × 10 to '
                  '10 × 4 mm and moved to (6, 10) and (-6, 10) mm. Their axial positions, volumes and mass budgets '
                  'are unchanged. Bend radius, tie access and actual cable routing still need verification.']
    (args.output / 'report.md').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    main()
