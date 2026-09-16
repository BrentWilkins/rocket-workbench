import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import pytest

from cfd_run import (
    solver_stages,
    stage_passes,
    tmr_flat_plate_mesh_passes,
    tmr_naca0012_mesh_passes,
    shell_command,
    validate_resources,
    write_decompose_par_dict,
)


def test_environment_setup_does_not_depend_on_image_tag():
    assert shell_command('simpleFoam', '/opt/foam/etc/bashrc') == 'source /opt/foam/etc/bashrc && simpleFoam'
    assert shell_command('simpleFoam', '') == 'simpleFoam'
    assert shell_command('simpleFoam', '/opt/foam with spaces/bashrc') == (
        "source '/opt/foam with spaces/bashrc' && simpleFoam")


def test_checkmesh_zero_exit_does_not_hide_quality_failure():
    assert not stage_passes('checkMesh',0,'Failed 1 mesh checks.\nEnd\n')
    assert not stage_passes('checkMesh -allTopology -allGeometry',0,
                            'Failed 2 mesh checks.\nEnd\n')
    assert stage_passes('checkMesh',0,'Mesh OK.\nEnd\n')
    assert not stage_passes('checkMesh',0,'End\n')


def test_solver_and_surface_checks_fail_closed():
    assert not stage_passes('simpleFoam',0,'FOAM FATAL IO ERROR\nEnd\n')
    assert not stage_passes('simpleFoam',1,'End\n')
    assert not stage_passes('simpleFoam',0,'Time = 10\n')
    assert stage_passes('simpleFoam',0,'Time = 600\nEnd\n')
    assert not stage_passes('surfaceCheck constant/triSurface/rocket.stl',0,'Surface is not closed')
    assert stage_passes('surfaceCheck constant/triSurface/rocket.stl',0,'Surface is closed')
    assert stage_passes(
        'foamDictionary system/decomposeParDict -entry method -set simple', 0, ''
    )
    assert not stage_passes(
        'foamDictionary system/decomposeParDict -entry method -set simple',
        1,
        '',
    )


def test_parallel_solver_uses_decompose_mpi_and_reconstruction():
    stages=solver_stages(mesh_only=False,mpi_ranks=8)
    assert stages[-3:] == [
        'decomposePar -force',
        'mpirun --allow-run-as-root -np 8 simpleFoam -parallel',
        'reconstructPar -latestTime',
    ]
    assert solver_stages(mesh_only=False,mpi_ranks=1)[-1] == 'simpleFoam'


def test_compressible_solver_is_explicitly_allowlisted():
    stages = solver_stages(
        mesh_only=False, mpi_ranks=2, prebuilt_mesh=True, solver='rhoSimpleFoam'
    )
    assert stages[-2] == (
        'mpirun --allow-run-as-root -np 2 rhoSimpleFoam -parallel'
    )
    with pytest.raises(ValueError, match='Unsupported solver'):
        solver_stages(mesh_only=False, mpi_ranks=1, solver='arbitraryCommand')


def test_transient_compressible_solver_is_explicitly_allowlisted():
    stages = solver_stages(
        mesh_only=False, mpi_ranks=2, prebuilt_mesh=True, solver='rhoPimpleFoam'
    )
    assert stages[-2] == (
        'mpirun --allow-run-as-root -np 2 rhoPimpleFoam -parallel'
    )


def test_prebuilt_benchmark_mesh_skips_surface_and_meshing_stages():
    assert solver_stages(mesh_only=False,mpi_ranks=1,prebuilt_mesh=True) == [
        'checkMesh -allTopology -allGeometry','simpleFoam'
    ]


def test_parallel_solver_can_switch_only_runtime_surface_decomposition():
    stages = solver_stages(
        mesh_only=False,
        mpi_ranks=12,
        prebuilt_mesh=True,
        solver='rhoSimpleFoam',
        runtime_decomposition_method='simple',
    )
    assert stages[-5:] == [
        'decomposePar -force',
        'foamDictionary system/decomposeParDict -entry method -set simple',
        'mpirun --allow-run-as-root -np 12 rhoSimpleFoam -parallel',
        'foamDictionary system/decomposeParDict -entry method -set scotch',
        'reconstructPar -latestTime',
    ]


def test_runtime_surface_decomposition_requires_parallel_solver():
    with pytest.raises(ValueError, match='requires a parallel solver'):
        solver_stages(
            mesh_only=False,
            mpi_ranks=1,
            runtime_decomposition_method='simple',
        )


def test_tmr_mesh_exception_is_exact_and_source_pinned():
    spec={'benchmark':'TMR 2DZP flat plate','source':{'archive_sha256':
        '4b0a64c2c1648f696f92bf9a91e64e972e6c32e76e8daa70ffa65ed8dd641412'}}
    log='''Boundary definition OK.\nCell to face addressing OK.\nFace vertices OK.\nNumber of regions: 1 (OK).\nCell volumes OK.\nNon-orthogonality check OK.\nFace pyramids OK.\nMax skewness = 0 OK.\n***High aspect ratio cells found, Max aspect ratio: 20000\n***Cells with small determinant (< 0.001) found, number of cells: 2\nFailed 2 mesh checks.\nEnd\n'''
    assert tmr_flat_plate_mesh_passes(log,spec)
    assert not tmr_flat_plate_mesh_passes(log+'***Wrong extra warning\n',spec)
    spec['source']['archive_sha256']='changed'
    assert not tmr_flat_plate_mesh_passes(log,spec)


def test_tmr_naca_mesh_exception_is_exact_source_and_topology_pinned():
    spec = {
        'benchmark': 'TMR 2D NACA 0012',
        'source': {
            'archive_sha256':
                'b4418dd04ab6aee04dc700f9f7769b6eca1af0dd31ccefb958b7d89da53ff1c4'
        },
        'grid_dimensions': [113, 33],
        'mesh': {'airfoil_faces': 64},
    }
    log = '\n'.join((
        'Boundary definition OK.',
        'Cell to face addressing OK.',
        'Face vertices OK.',
        'Number of regions: 1 (OK).',
        'Cell volumes OK.',
        'Non-orthogonality check OK.',
        'Face pyramids OK.',
        'Max skewness = 0.5 OK.',
        ' ***High aspect ratio cells found, details',
        ' ***Error in face tets: details',
        ' ***Cells with small determinant (< 0.001) found, details',
        ' ***Concave cells (using face planes) found, details',
        'Failed 4 mesh checks.',
        'End',
    ))
    assert tmr_naca0012_mesh_passes(log, spec)
    assert not tmr_naca0012_mesh_passes(log.replace('Failed 4', 'Failed 5'), spec)
    assert not tmr_naca0012_mesh_passes(
        log, {**spec, 'mesh': {'airfoil_faces': 55}}
    )


def test_parallel_resources_must_not_oversubscribe_container():
    validate_resources(cpus=8,memory='24g',mpi_ranks=8,mesh_only=False)
    with pytest.raises(ValueError,match='cannot exceed'):
        validate_resources(cpus=2,memory='4g',mpi_ranks=8,mesh_only=False)
    with pytest.raises(ValueError,match='mesh-only'):
        validate_resources(cpus=8,memory='24g',mpi_ranks=8,mesh_only=True)


def test_decomposition_dictionary_records_rank_count(tmp_path):
    system=tmp_path/'system'
    system.mkdir()
    write_decompose_par_dict(tmp_path,8)
    text=(system/'decomposeParDict').read_text()
    assert 'numberOfSubdomains 8;' in text
    assert 'method scotch;' in text
    assert 'simpleCoeffs { n (8 1 1); delta 0.001; }' in text
