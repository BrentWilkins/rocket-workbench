import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from cfd_smoke import smoke_command


def test_smoke_command_uses_configured_environment_and_packaged_tutorial():
    command = smoke_command("/opt/OpenFOAM path/etc/bashrc")

    assert command.startswith("source '/opt/OpenFOAM path/etc/bashrc' && ")
    assert "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" in command
    assert "cd /evidence/cavity && blockMesh && checkMesh && icoFoam" in command


def test_smoke_command_supports_preconfigured_image():
    assert not smoke_command("").startswith("source ")
