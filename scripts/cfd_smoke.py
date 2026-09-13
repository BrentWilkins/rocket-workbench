"""Run an isolated upstream cavity installation check, not a rocket validation."""
import argparse
import json
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    image = 'rocket-workbench-cfd:1912-arm64'
    identity = subprocess.check_output(['docker','image','inspect',image],text=True)
    (args.output/'image.json').write_text(identity)
    command = ['docker','run','--rm','--network=none','--cpus=2','--memory=2g',image,
        'dpkg-query -W; '
        'cp -r /usr/share/doc/openfoam-examples/examples/incompressible/icoFoam/cavity/cavity /tmp/cavity && '
        'cd /tmp/cavity && blockMesh && checkMesh && icoFoam']
    with (args.output/'execution.log').open('w') as log:
        result = subprocess.run(command,stdout=log,stderr=subprocess.STDOUT)
    (args.output/'result.json').write_text(json.dumps(dict(command=command,returncode=result.returncode,
        purpose='Upstream cavity installation smoke test only; not rocket validation',
        rocket_cfd_validated=False),indent=2)+'\n')
    print('CFD installation smoke-test exit:', result.returncode)
    raise SystemExit(result.returncode)


if __name__=='__main__':
    main()
