"""Bundle matching D12 evidence and print files without rerunning or publishing."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

from check_bambu_project import inspect
from verify_study import verify
from package_bambu import PARTS

ROOT = Path(__file__).resolve().parents[1]
SCREEN = 'sourced24-insert-corrected-20260913'
DESIGN = 'apogee24-body500-heavy0-cd053-insert-trial'
STRESS = 'insert-recovery-wide-20260913'
SUMMARY = 'insert-wide-summary-20260913'
PRINT = 'd12-bt60-insert-review-20260913'
PROJECT = 'D12-BT60-insert-X1C-review.3mf'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_print_sources(print_source, cad_source, source_run):
    project_manifest = json.loads((print_source/'manifest.json').read_text())
    if project_manifest['source_run'] != source_run:
        raise ValueError('Print project points to a different simulation configuration')
    if set(project_manifest['parts']) != {name+'.stl' for name in PARTS}:
        raise ValueError('Print manifest must identify all six expected meshes')
    if digest(print_source/PROJECT) != project_manifest['project_sha256']:
        raise ValueError('Print project changed after export')
    for name, expected in project_manifest['parts'].items():
        if digest(cad_source/name) != expected:
            raise ValueError('Print mesh differs from simulated CAD export')
    return project_manifest


def package(out):
    out = out.resolve()
    if out.exists() or Path(str(out)+'.zip').exists():
        raise FileExistsError('Preserve previous packages; choose a fresh output path')
    studies = [SCREEN, STRESS, SUMMARY]
    checks = [verify(ROOT/'runs'/name) for name in studies]
    print_source = ROOT/'deliverables'/PRINT
    verify_print_sources(print_source, ROOT/'runs'/SCREEN/DESIGN/'cad', f'{SCREEN}/{DESIGN}')
    placement = inspect(print_source/PROJECT)
    out.mkdir(parents=True)
    for name in studies:
        shutil.copytree(ROOT/'runs'/name, out/'runs'/name)
    shutil.copytree(print_source, out/'print-review')
    # Include exact local implementation, but no dependency binaries or cached Python bytecode.
    for name in ['src', 'scripts', 'tests', 'examples']:
        shutil.copytree(ROOT/name, out/name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    for name in ['pyproject.toml', 'uv.lock', '.python-version']:
        shutil.copy2(ROOT/name, out/name)
    for name in studies:
        verify(out/'runs'/name)
    (out/'README.md').write_text(f'''# D12 / BT-60 insert-bay review

Review candidate, not flight clearance or a globally optimal design. Hardware inputs remain provisional.

- [Open the X1C / 0.4 mm / Textured PEI / PLA project](print-review/{PROJECT})
- [Full assembly STEP](runs/{SCREEN}/{DESIGN}/cad/assembly.step)
- [Installed avionics cutaway](print-review/render/installed-cutaway.png)
- [Loaded D12-5, zero-wind OpenRocket model](runs/{SCREEN}/{DESIGN}/actual-D12-5-wind0.ork)
- [Nominal configuration and mass ledger](runs/{SCREEN}/{DESIGN}/report.md)
- [288-flight uncertainty comparison](runs/{SUMMARY}/report.md)
- [All nominal/upper configurations and 36 flights](runs/{SCREEN}/report.md)

All 192 planned dummy/logger uncertainty cases meet the configured simulation criteria; 96 empty diagnostics are
retained separately. Scenario counts are not reliability probabilities. The literature-specimen 24-inch canopy mass,
packing, insert-joint allowance and electronics dimensions are not measurements of delivered hardware.

CAD includes separate printable STEP/STL files, detailed electronics approximations and conservative keepouts. Print
only the six parts in the Bambu project, not the paper tube, electronics, assembled rocket or keepout models. Toolpath
generation was checked separately; review supports, brim and settings in Bambu Studio before any print.

Physical fit, complete measured mass/CG, insert installation, recovery strength, separation and pressure response remain
unverified. No purchases or printer commands were issued. CFD coefficients are not used in these flight predictions.

Exact local Python sources and uv lock are included. Follow the repository setup instructions for the separately
installed OpenRocket dependency; no Java binary is redistributed. Rerun into fresh directories, for example:

```sh
uv run --extra cad python scripts/study_sourced_chute.py --insert-trial --output runs/new-insert-screen
uv run --extra cad python scripts/stress_fin_shapes.py --study runs/new-insert-screen \\
  --design {DESIGN} --uncertainty examples/uncertainty-recovery-wide.yaml \\
  --upper-chute-factor 1.2 --output runs/new-insert-stress
```

Build, sourcing and comparison guidance: https://brentwilkins.github.io/rocket-workbench/
The live site may precede this local bundle until the combined documentation publication.
`bundle-manifest.json` hashes all included files except itself; original study manifests remain unchanged.
''')
    files = {str(p.relative_to(out)): digest(p) for p in sorted(out.rglob('*')) if p.is_file()}
    (out/'bundle-manifest.json').write_text(json.dumps(dict(files_sha256=files,
        source_studies=studies, original_integrity_checks=checks, print_placement=placement,
        physical_validation=False, published=False), indent=2)+'\n')
    archive = shutil.make_archive(str(out), 'zip', root_dir=out.parent, base_dir=out.name)
    return dict(directory=str(out), archive=archive, archive_sha256=digest(Path(archive)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(package(args.output), indent=2))
