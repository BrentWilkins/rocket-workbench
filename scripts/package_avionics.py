"""Package current avionics CAD/fit proof without repeating unchanged physics."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

from rocket_workbench.cad import build
from rocket_workbench.config import load_config
from rocket_workbench.provenance import seal_run

ROOT = Path(__file__).resolve().parents[1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--run', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    source, out = ROOT/args.run, ROOT/args.output
    out.mkdir(parents=True, exist_ok=False)
    config = load_config(source/'config.yaml')
    if not config.avionics_profile:
        raise ValueError('An avionics-profile run is required')
    current = build(config, out/'cad')
    original = json.loads((source/'cad/mass-properties.json').read_text())
    for name, part in current.items():
        for key in ['volume_mm3','mass_g','cg_x_mm']:
            if abs(part[key]-original[name][key]) > 1e-7:
                raise ValueError('CAD physics changed: rerun simulations before packaging')
    for name in ['config.yaml', 'results.json', 'results.csv', 'report.md', 'mass-ledger.json']:
        shutil.copy2(source/name, out/name)
    manifest = dict(simulation_source=str(source.relative_to(ROOT)),
                    simulation_manifest_sha256=hashlib.sha256((source/'manifest.json').read_bytes()).hexdigest(),
                    geometry_matches_simulated_mass_properties=True)
    (out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    (out/'README.md').write_text('''# Avionics bay review package

Provisional engineering model, not physical flight or crash validation.

- [Labeled two-view layout](cad/avionics-layout.svg)
- [Installed detailed approximation](cad/avionics-installed.step)
- [Electronics detailed approximation](cad/avionics-detailed.step)
- [Conservative component keepouts](cad/avionics-keepouts.step)
- [Full rocket assembly](cad/assembly.step)
- [Numeric installed/insertion clearance proof](cad/avionics-fit.json)
- [Component masses, uncertainty and static-port specification](cad/avionics.json)
- [Nominal flight report](report.md)
- [Mass ledger](mass-ledger.json)

Printed parts are separate named STL files in cad/. Do not print the electronics
or vendor model. This package's regenerated CAD mass properties were checked
against the retained simulation run before packaging; no new physics was inferred.

See docs/AVIONICS_DESIGN.md in the repository for the wiring/power specification,
upper-mass flight failures, sources and final hardware-check list.
''')
    seal_run(out)
    print(out)


if __name__ == '__main__':
    main()
