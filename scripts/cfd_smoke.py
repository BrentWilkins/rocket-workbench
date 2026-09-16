"""Run an isolated upstream cavity installation check, not rocket validation."""

import argparse
import json
import shlex
import subprocess
from pathlib import Path


def smoke_command(openfoam_bashrc: str) -> str:
    setup = f"source {shlex.quote(openfoam_bashrc)} && " if openfoam_bashrc else ""
    return (
        setup
        + 'cp -r "$FOAM_TUTORIALS/incompressible/icoFoam/cavity/cavity" '
        "/evidence/cavity && "
        "cd /evidence/cavity && blockMesh && checkMesh && icoFoam"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--image", default="rocket-workbench-cfd:2512-arm64")
    parser.add_argument(
        "--openfoam-bashrc",
        default="/usr/lib/openfoam/openfoam2512/etc/bashrc",
        help="OpenFOAM environment inside image; empty for a preconfigured image",
    )
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    output = args.output.resolve()
    identity = json.loads(
        subprocess.check_output(["docker", "image", "inspect", args.image], text=True)
    )[0]
    (output / "image.json").write_text(json.dumps(identity, indent=2) + "\n")
    command = [
        "docker",
        "run",
        "--rm",
        "--network=none",
        "--cpus=2",
        "--memory=2g",
        "--mount",
        f"type=bind,src={output},dst=/evidence",
        identity["Id"],
        smoke_command(args.openfoam_bashrc),
    ]
    with (output / "execution.log").open("w") as log:
        result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT)
    (output / "result.json").write_text(
        json.dumps(
            dict(
                command=command,
                returncode=result.returncode,
                openfoam_bashrc=args.openfoam_bashrc,
                resource_limits=dict(cpus=2, memory="2g"),
                network_disabled=True,
                purpose="Upstream cavity smoke only; not rocket validation",
                rocket_cfd_validated=False,
            ),
            indent=2,
        )
        + "\n"
    )
    print("CFD installation smoke-test exit:", result.returncode)
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
