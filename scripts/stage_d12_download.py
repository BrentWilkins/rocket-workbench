"""Stage a compact, verified public review download; never upload or print."""
import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from package_d12_review import ROOT, SCREEN, DESIGN, PRINT, PROJECT, digest, verify_print_sources
from verify_study import verify
from check_bambu_project import inspect


def stage(output):
    source = ROOT/'runs'/SCREEN/DESIGN
    print_source = ROOT/'deliverables'/PRINT
    verify(source)
    verify_print_sources(print_source, source/'cad', f'{SCREEN}/{DESIGN}')
    inspect(print_source/PROJECT)
    if output.exists():
        raise FileExistsError('Do not overwrite a published review download')
    output.parent.mkdir(parents=True, exist_ok=True)
    files = {f'candidate/{p.relative_to(source)}':p for p in source.rglob('*') if p.is_file()}
    files['print/'+PROJECT] = print_source/PROJECT
    for name in ['installed-cutaway.png', 'exploded.png']:
        files['render/'+name] = print_source/'render'/name
    manifest = dict(source_run=f'{SCREEN}/{DESIGN}',
                    files_sha256={name:digest(path) for name,path in files.items()},
                    physical_validation=False)
    with ZipFile(output, 'x', ZIP_DEFLATED) as archive:
        for name, path in sorted(files.items()):
            archive.write(path, name)
        archive.writestr('download-manifest.json', json.dumps(manifest, indent=2)+'\n')
        archive.writestr('README.md', f'''# D12 / BT-60 insert-bay review files

Provisional hardware, not physical validation or flight clearance.

- Open print/{PROJECT} as a project in Bambu Studio: X1C, 0.4 mm, Textured PEI, PLA.
- candidate/cad/ contains the six printable STEP/STL parts and complete assembly/electronics approximations.
  Do not print the assembly, paper tube or electronics keepouts.
- candidate/ contains configuration, mass ledger, nominal flight reports, results and OpenRocket models.
- render/ contains actual CAD cutaway and exploded views; electronics details are approximations.

This is the nominal integrated insert candidate. The broader 288-case uncertainty study, comparisons, build guide,
sourcing and remaining physical checks are documented at https://brentwilkins.github.io/rocket-workbench/ .
All 192 planned dummy/logger uncertainty cases pass configured numeric gates, not a reliability probability.
No active control, physical retention qualification or printer operation is included.

Do not mix this configuration with the older V5/18 mm package. Inspect toolpaths and fit before any printing;
measure complete mass/CG and verify recovery before flight consideration.
''')
    with ZipFile(output) as archive:
        if archive.testzip():
            raise ValueError('Download archive integrity failure')
    return dict(path=str(output), bytes=output.stat().st_size, sha256=digest(output))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(stage(args.output), indent=2))
