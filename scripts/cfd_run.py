"""Run one explicit generated case; retain stage logs and exit codes."""
import argparse
import json
import subprocess
import re
from pathlib import Path


def stage_passes(stage, returncode, log):
    if returncode != 0 or 'FOAM FATAL' in log:
        return False
    if stage=='checkMesh':
        return 'Mesh OK.' in log and not re.search(r'Failed\s+\d+\s+mesh checks',log)
    if stage.startswith('surfaceCheck'):
        return 'Surface is closed' in log
    return bool(re.search(r'^End\s*$',log,re.MULTILINE))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',required=True,type=Path)
    parser.add_argument('--mesh-only',action='store_true')
    parser.add_argument('--image',default='rocket-workbench-cfd:2512-arm64')
    args=parser.parse_args()
    folder=args.case.resolve(strict=True)
    if not (folder/'case-spec.json').is_file() or (folder/'execution.json').exists():
        raise ValueError('Require generated, not previously executed case')
    image=args.image
    identity=json.loads(subprocess.check_output(['docker','image','inspect',image],text=True))[0]
    (folder/'image.json').write_text(json.dumps(identity,indent=2)+'\n')
    stages=['surfaceCheck constant/triSurface/rocket.stl','blockMesh','snappyHexMesh -overwrite','checkMesh']
    if not args.mesh_only:
        stages.append('simpleFoam')
    results=[]
    for index,stage in enumerate(stages):
        shell_stage=stage
        if image=='rocket-workbench-cfd:2512-arm64':
            shell_stage='source /usr/lib/openfoam/openfoam2512/etc/bashrc && '+stage
        command=['docker','run','--rm','--network=none','--cpus=2','--memory=4g',
                 '--mount',f'type=bind,src={folder},dst=/case',identity['Id'],shell_stage]
        with (folder/f'{index}-{stage.split()[0]}.log').open('w') as log:
            result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT)
        log_text=(folder/f'{index}-{stage.split()[0]}.log').read_text()
        passed=stage_passes(stage,result.returncode,log_text)
        results.append(dict(stage=stage,returncode=result.returncode,stage_passed=passed))
        (folder/'execution.json').write_text(json.dumps(results,indent=2)+'\n')
        print(stage,result.returncode,flush=True)
        if not passed:
            raise SystemExit(result.returncode or 2)


if __name__=='__main__':
    main()
