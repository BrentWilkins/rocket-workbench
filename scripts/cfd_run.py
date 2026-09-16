"""Run one explicit generated case; retain stage logs and exit codes."""
import argparse
import json
import subprocess
import re
import shlex
from pathlib import Path


def shell_command(stage, bashrc):
    return 'source '+shlex.quote(bashrc)+' && '+stage if bashrc else stage


def stage_passes(stage, returncode, log):
    if returncode != 0 or 'FOAM FATAL' in log:
        return False
    if stage.startswith('checkMesh'):
        return 'Mesh OK.' in log and not re.search(r'Failed\s+\d+\s+mesh checks',log)
    if stage.startswith('surfaceCheck'):
        return 'Surface is closed' in log
    if stage.startswith('foamDictionary'):
        return True
    return bool(re.search(r'^End\s*$',log,re.MULTILINE))


def tmr_flat_plate_mesh_passes(log: str, spec: dict) -> bool:
    """Accept only the two documented stretching diagnostics in the pinned TMR grid."""
    if (spec.get('benchmark') != 'TMR 2DZP flat plate' or
            spec.get('source',{}).get('archive_sha256') !=
            '4b0a64c2c1648f696f92bf9a91e64e972e6c32e76e8daa70ffa65ed8dd641412'):
        return False
    required=('Boundary definition OK.','Cell to face addressing OK.','Face vertices OK.',
              'Number of regions: 1 (OK).','Cell volumes OK.','Non-orthogonality check OK.',
              'Face pyramids OK.','Max skewness =','Failed 2 mesh checks.','End')
    diagnostics=re.findall(r'^\s*\*\*\*(.+)$',log,re.MULTILINE)
    expected=('High aspect ratio cells found,','Cells with small determinant (< 0.001) found,')
    return all(item in log for item in required) and len(diagnostics)==2 and all(
        diagnostic.startswith(prefix) for diagnostic,prefix in zip(diagnostics,expected)
    )


def tmr_naca0012_mesh_passes(log: str, spec: dict) -> bool:
    """Accept only the documented quality diagnostics in a pinned TMR C-grid."""
    if (
        spec.get("benchmark") != "TMR 2D NACA 0012"
        or spec.get("source", {}).get("archive_sha256")
        != "b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4"
    ):
        return False
    dimensions = spec.get("grid_dimensions", [])
    mesh = spec.get("mesh", {})
    if (
        len(dimensions) != 2
        or dimensions[0] not in {113, 225, 449, 897, 1793}
        or mesh.get("airfoil_faces") != 4 * (dimensions[0] - 1) // 7
    ):
        return False
    required = (
        "Boundary definition OK.",
        "Cell to face addressing OK.",
        "Face vertices OK.",
        "Number of regions: 1 (OK).",
        "Cell volumes OK.",
        "Non-orthogonality check OK.",
        "Face pyramids OK.",
        "Max skewness =",
        "Failed 4 mesh checks.",
        "End",
    )
    diagnostics = re.findall(r"^\s*\*\*\*(.+)$", log, re.MULTILINE)
    expected = (
        "High aspect ratio cells found,",
        "Error in face tets:",
        "Cells with small determinant (< 0.001) found,",
        "Concave cells (using face planes) found,",
    )
    return (
        all(item in log for item in required)
        and len(diagnostics) == len(expected)
        and all(
            diagnostic.startswith(prefix)
            for diagnostic, prefix in zip(diagnostics, expected, strict=True)
        )
    )


def solver_stages(
    *,
    mesh_only: bool,
    mpi_ranks: int,
    prebuilt_mesh: bool = False,
    solver: str = 'simpleFoam',
    runtime_decomposition_method: str | None = None,
) -> list[str]:
    if solver not in {'simpleFoam', 'rhoSimpleFoam', 'rhoPimpleFoam'}:
        raise ValueError(f'Unsupported solver {solver!r}')
    stages=(['checkMesh -allTopology -allGeometry'] if prebuilt_mesh else [
        'surfaceCheck constant/triSurface/rocket.stl',
        'blockMesh',
        'snappyHexMesh -overwrite',
        'checkMesh',
    ])
    if mesh_only:
        return stages
    if runtime_decomposition_method not in {None, 'simple'}:
        raise ValueError(
            f'Unsupported runtime decomposition method {runtime_decomposition_method!r}'
        )
    if mpi_ranks == 1:
        if runtime_decomposition_method is not None:
            raise ValueError('Runtime decomposition method requires a parallel solver')
        return stages + [solver]
    parallel_stages = ['decomposePar -force']
    if runtime_decomposition_method is not None:
        parallel_stages.append(
            'foamDictionary system/decomposeParDict -entry method '
            f'-set {runtime_decomposition_method}'
        )
    parallel_stages.append(
        f'mpirun --allow-run-as-root -np {mpi_ranks} {solver} -parallel'
    )
    if runtime_decomposition_method is not None:
        parallel_stages.append(
            'foamDictionary system/decomposeParDict -entry method -set scotch'
        )
    parallel_stages.append('reconstructPar -latestTime')
    return stages + parallel_stages


def validate_resources(*, cpus: float, memory: str, mpi_ranks: int, mesh_only: bool):
    if cpus <= 0:
        raise ValueError('CPU limit must be positive')
    if not re.fullmatch(r'[1-9][0-9]*(?:\.[0-9]+)?[bkmgBKMG]', memory):
        raise ValueError('Memory limit must be a positive Docker size such as 4g or 24576m')
    if mpi_ranks < 1:
        raise ValueError('MPI ranks must be positive')
    if mpi_ranks > cpus:
        raise ValueError('MPI ranks cannot exceed the Docker CPU limit')
    if mesh_only and mpi_ranks != 1:
        raise ValueError('MPI ranks apply to a solver run, not --mesh-only')


def write_decompose_par_dict(folder: Path, mpi_ranks: int):
    (folder/'system'/'decomposeParDict').write_text(
        'FoamFile {version 2.0; format ascii; class dictionary; '
        'object decomposeParDict;}\n'
        f'numberOfSubdomains {mpi_ranks};\n'
        'method scotch;\n'
        f'simpleCoeffs {{ n ({mpi_ranks} 1 1); delta 0.001; }}\n'
    )


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',required=True,type=Path)
    parser.add_argument('--mesh-only',action='store_true')
    parser.add_argument('--prebuilt-mesh',action='store_true',
                        help='Use an existing constant/polyMesh, such as a pinned benchmark grid')
    parser.add_argument('--image',default='rocket-workbench-cfd:2512-arm64')
    parser.add_argument('--openfoam-bashrc', default='/usr/lib/openfoam/openfoam2512/etc/bashrc',
                        help='OpenFOAM environment inside the image; empty for an already configured image')
    parser.add_argument('--container-entrypoint')
    parser.add_argument('--container-workdir')
    parser.add_argument('--container-user')
    parser.add_argument('--cpus',type=float,default=2)
    parser.add_argument('--memory',default='4g')
    parser.add_argument('--mpi-ranks',type=int,default=1)
    parser.add_argument(
        '--runtime-decomposition-method',
        choices=['simple'],
        help=(
            'After decomposing the volume with scotch, temporarily select this '
            'point-capable method for solver-internal parallel redistribution.'
        ),
    )
    args=parser.parse_args()
    try:
        validate_resources(cpus=args.cpus,memory=args.memory,mpi_ranks=args.mpi_ranks,
                           mesh_only=args.mesh_only)
    except ValueError as error:
        parser.error(str(error))
    folder=args.case.resolve(strict=True)
    if not ((folder/'case-spec.json').is_file() or (folder/'benchmark-spec.json').is_file()) or (folder/'execution.json').exists():
        raise ValueError('Require generated, not previously executed case')
    image=args.image
    identity=json.loads(subprocess.check_output(['docker','image','inspect',image],text=True))[0]
    (folder/'image.json').write_text(json.dumps(identity,indent=2)+'\n')
    if args.mpi_ranks > 1:
        write_decompose_par_dict(folder,args.mpi_ranks)
    benchmark_spec=(json.loads((folder/'benchmark-spec.json').read_text())
                    if (folder/'benchmark-spec.json').is_file() else {})
    solver=benchmark_spec.get('model_mapping',{}).get('solver','simpleFoam')
    stages=solver_stages(
        mesh_only=args.mesh_only,
        mpi_ranks=args.mpi_ranks,
        prebuilt_mesh=args.prebuilt_mesh,
        solver=solver,
        runtime_decomposition_method=args.runtime_decomposition_method,
    )
    results=[]
    for index,stage in enumerate(stages):
        shell_stage=shell_command(stage, args.openfoam_bashrc)
        command=['docker','run','--rm','--network=none','--cpus',str(args.cpus),'--memory',args.memory,
                 '--mount',f'type=bind,src={folder},dst=/case']
        if args.container_workdir:
            command.extend(['--workdir', args.container_workdir])
        if args.container_user:
            command.extend(['--user', args.container_user])
        if args.container_entrypoint:
            command.extend(['--entrypoint', args.container_entrypoint])
        command.append(identity['Id'])
        if args.container_entrypoint:
            command.append('-lc')
        command.append(shell_stage)
        log_path=folder/f'{index}-{stage.split()[0]}.log'
        try:
            with log_path.open('w') as log:
                result=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT)
        except KeyboardInterrupt:
            results.append(dict(stage=stage,returncode=130,stage_passed=False,
                                interrupted=True,command=command,
                                openfoam_bashrc=args.openfoam_bashrc,
                                resource_limits=dict(cpus=args.cpus,memory=args.memory),
                                mpi_ranks=args.mpi_ranks,network_disabled=True,
                                image_id=identity['Id']))
            (folder/'execution.json').write_text(json.dumps(results,indent=2)+'\n')
            raise SystemExit(130)
        log_text=log_path.read_text()
        passed=stage_passes(stage,result.returncode,log_text)
        benchmark_mesh_exception=(
            args.prebuilt_mesh
            and stage.startswith('checkMesh')
            and (
                tmr_flat_plate_mesh_passes(log_text,benchmark_spec)
                or tmr_naca0012_mesh_passes(log_text,benchmark_spec)
            )
        )
        passed=passed or benchmark_mesh_exception
        results.append(dict(stage=stage,returncode=result.returncode,stage_passed=passed,
                            benchmark_mesh_exception=benchmark_mesh_exception,
                            command=command,openfoam_bashrc=args.openfoam_bashrc,
                            resource_limits=dict(cpus=args.cpus,memory=args.memory),
                mpi_ranks=args.mpi_ranks,network_disabled=True,
                container_entrypoint=args.container_entrypoint,
                container_workdir=args.container_workdir,
                container_user=args.container_user,
                image_id=identity['Id']))
        (folder/'execution.json').write_text(json.dumps(results,indent=2)+'\n')
        print(stage,result.returncode,flush=True)
        if not passed:
            raise SystemExit(result.returncode or 2)


if __name__=='__main__':
    main()
