"""Create a local, unsliced X1C fit-check project using installed Bambu Studio presets."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
APP = Path('/Applications/BambuStudio.app/Contents')
RUN = '20260912T224649Z-candidate-recovery-b6aebae0'
PARTS = ('nose-bay', 'bay-bulkhead', 'payload-sled', 'fin-collar', 'lug-sleeve-1', 'lug-sleeve-2')


def resolve_profile(directory, name, active=()):
    if name in active:
        raise ValueError(f'Profile inheritance cycle: {name}')
    path = directory / f'{name}.json'
    data = json.loads(path.read_text())
    result = {}
    if data.get('inherits'):
        result.update(resolve_profile(directory, data['inherits'], (*active, name)))
    for include in data.get('include', []):
        result.update(resolve_profile(directory, include, (*active, name)))
    result.update(data)
    result.pop('inherits', None)
    result.pop('include', None)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'deliverables/bambu-x1c-pla-saddles-v2')
    parser.add_argument('--run', default=RUN, help='Source run directory name under runs/')
    parser.add_argument('--parts', nargs='+', choices=PARTS, default=list(PARTS))
    parser.add_argument('--project-name', default='larger-recovery-X1C-PLA-fit-check.3mf')
    parser.add_argument('--slice-check', action='store_true', help='Generate local toolpath evidence; never send to printer')
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    if Path(args.project_name).name != args.project_name or not args.project_name.endswith('.3mf'):
        raise ValueError('Project name must be a .3mf filename without directories')
    target = out / args.project_name
    if target.exists():
        raise FileExistsError(f'Preserving existing project: {target}; select another --output')
    profiles = APP / 'Resources/profiles/BBL'
    machine = resolve_profile(profiles / 'machine', 'Bambu Lab X1 Carbon 0.4 nozzle')
    process = resolve_profile(profiles / 'process', '0.20mm Standard @BBL X1C')
    filament = resolve_profile(profiles / 'filament', 'Generic PLA')
    process.update(curr_bed_type='Textured PEI Plate', sparse_infill_density='100%', sparse_infill_pattern='zig-zag',
                   wall_loops='3', enable_support='1', support_type='normal(auto)',
                   support_on_build_plate_only='1', brim_type='outer_only', brim_width='5')
    settings = []
    for name, data in [('machine', machine), ('process', process), ('filament', filament)]:
        path = out / f'{name}.json'
        path.write_text(json.dumps(data, indent=2) + '\n')
        settings.append(path)
    meshes = [ROOT / 'runs' / args.run / 'cad' / f'{name}.stl' for name in args.parts]
    for mesh in meshes:
        if not mesh.is_file():
            raise FileNotFoundError(mesh)
    command = [str(APP / 'MacOS/BambuStudio'), '--debug', '2',
               '--load-settings', f'{settings[0]};{settings[1]}', '--load-filaments', str(settings[2]),
               '--arrange', '1', '--orient', '0', '--ensure-on-bed',
               '--outputdir', str(out), '--export-3mf', target.name, *map(str, meshes)]
    result = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (out / 'export.log').write_text(result.stdout)
    if result.returncode:
        raise RuntimeError(f'Bambu Studio exited {result.returncode}; see {out / "export.log"}')
    with ZipFile(target) as archive:
        if archive.testzip():
            raise ValueError('Corrupt 3MF archive')
        names = archive.namelist()
        if 'Metadata/project_settings.config' not in names:
            raise ValueError('Missing native Bambu project settings')
        embedded = json.loads(archive.read('Metadata/project_settings.config'))
        assert embedded['curr_bed_type'] == 'Textured PEI Plate'
        assert embedded['printer_model'] == 'Bambu Lab X1 Carbon'
        assert embedded['nozzle_diameter'] == ['0.4']
        assert embedded['filament_type'] == ['PLA']
    manifest = dict(source_run=args.run, purpose='Unsliced fit-check project; not flight-qualified',
                    parts={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in meshes},
                    project_sha256=hashlib.sha256(target.read_bytes()).hexdigest())
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if args.slice_check:
        check = subprocess.run([str(APP/'MacOS/BambuStudio'), '--debug', '2', '--slice', '0',
                                '--outputdir', str(out), '--export-3mf', 'sliced-check.3mf', str(target)],
                               text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (out/'slice-check.log').write_text(check.stdout)
        if check.returncode:
            raise RuntimeError(f'Slice check failed ({check.returncode}); see {out / "slice-check.log"}')
    print(target)


if __name__ == '__main__':
    main()
