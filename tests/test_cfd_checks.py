import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from cfd_run import stage_passes


def test_checkmesh_zero_exit_does_not_hide_quality_failure():
    assert not stage_passes('checkMesh',0,'Failed 1 mesh checks.\nEnd\n')
    assert stage_passes('checkMesh',0,'Mesh OK.\nEnd\n')
    assert not stage_passes('checkMesh',0,'End\n')


def test_solver_and_surface_checks_fail_closed():
    assert not stage_passes('simpleFoam',0,'FOAM FATAL IO ERROR\nEnd\n')
    assert not stage_passes('simpleFoam',1,'End\n')
    assert not stage_passes('simpleFoam',0,'Time = 10\n')
    assert stage_passes('simpleFoam',0,'Time = 600\nEnd\n')
    assert not stage_passes('surfaceCheck constant/triSurface/rocket.stl',0,'Surface is not closed')
    assert stage_passes('surfaceCheck constant/triSurface/rocket.stl',0,'Surface is closed')
