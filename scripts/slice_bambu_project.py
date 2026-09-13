"""Generate local toolpath evidence from an existing inspection project; never print."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from zipfile import ZipFile

from check_bambu_project import inspect


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source = args.project.resolve()
    placement = inspect(source)
    out = args.output.resolve()
    out.mkdir(parents=True,exist_ok=False)
    command = ['/Applications/BambuStudio.app/Contents/MacOS/BambuStudio', '--debug','2',
               '--slice','0','--outputdir',str(out),'--export-3mf','sliced-check.3mf',str(source)]
    result = subprocess.run(command,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (out/'slice.log').write_text(result.stdout)
    record = dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  command=command,returncode=result.returncode,placement=placement,
                  sent_to_printer=False,physical_validation=False)
    target = out/'sliced-check.3mf'
    if result.returncode == 0 and target.is_file():
        with ZipFile(target) as archive:
            record['archive_valid'] = archive.testzip() is None
            record['toolpath_entries'] = [name for name in archive.namelist() if name.endswith('.gcode')]
        record['output_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    record['slice_passed'] = bool(result.returncode == 0 and record.get('archive_valid')
                                and record.get('toolpath_entries'))
    (out/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
    if not record['slice_passed']:
        raise RuntimeError(f'Slice check failed; inspect retained log: {out}')
    print('Local slice passed:',target)


if __name__ == '__main__':
    main()
