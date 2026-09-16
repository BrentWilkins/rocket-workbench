"""Run wall-shear post-processing on a temporary copy of a sealed NACA case."""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from cfd_naca0012_yplus_run import latest_time


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(case: Path, output: Path, image: str, cpus: float, memory: str) -> dict:
    case = case.resolve(strict=True)
    execution_path = case / "execution.json"
    execution = json.loads(execution_path.read_text())
    if not execution or not all(stage.get("stage_passed") for stage in execution):
        raise ValueError("Source case execution did not pass")
    spec_path = case / "benchmark-spec.json"
    if not spec_path.is_file():
        raise ValueError("Source case has no benchmark specification")
    spec = json.loads(spec_path.read_text())
    solver = spec.get("solver") or spec.get("model_mapping", {}).get("solver")
    if solver not in {"simpleFoam", "rhoSimpleFoam"}:
        raise ValueError(f"Unsupported source solver for wall shear: {solver!r}")
    time = latest_time(case)
    output.mkdir(parents=True, exist_ok=False)
    identity = json.loads(
        subprocess.check_output(["docker", "image", "inspect", image], text=True)
    )[0]
    shell_stage = (
        "source /usr/lib/openfoam/openfoam2512/etc/bashrc && "
        f"{solver} -postProcess -func wallShearStress -latestTime; "
        f"status=$?; chown -R {os.getuid()}:{os.getgid()} /case; exit $status"
    )
    with tempfile.TemporaryDirectory(prefix="naca0012-shear-", dir="/tmp") as temporary:
        temporary_case = Path(temporary) / "case"
        temporary_case.mkdir()
        for name in ("0", "constant", "system"):
            shutil.copytree(case / name, temporary_case / name, symlinks=True)
        if time.name != "0":
            shutil.copytree(time, temporary_case / time.name, symlinks=True)
        command = [
            "docker",
            "run",
            "--rm",
            "--network=none",
            "--cpus",
            str(cpus),
            "--memory",
            memory,
            "--mount",
            f"type=bind,src={temporary_case},dst=/case",
            identity["Id"],
            shell_stage,
        ]
        result = subprocess.run(command, text=True, capture_output=True)
        log_path = output / f"{solver}-wallShearStress.log"
        log_path.write_text(result.stdout + result.stderr)
        generated = temporary_case / time.name / "wallShearStress"
        passed = (
            result.returncode == 0
            and "FOAM FATAL" not in log_path.read_text()
            and generated.is_file()
        )
        if passed:
            shutil.copyfile(generated, output / "wallShearStress")
    record = {
        "case": str(case),
        "case_spec_sha256": sha256(spec_path),
        "case_execution_sha256": sha256(execution_path),
        "source_time": float(time.name),
        "command": command,
        "image_id": identity["Id"],
        "resource_limits": {"cpus": cpus, "memory": memory},
        "network_disabled": True,
        "returncode": result.returncode,
        "log_sha256": sha256(log_path),
        "field_sha256": sha256(output / "wallShearStress") if passed else None,
        "stage_passed": passed,
    }
    (output / "execution.json").write_text(json.dumps(record, indent=2) + "\n")
    if not passed:
        raise SystemExit(1)
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--image", default="rocket-workbench-cfd:2512-sstm-compressible")
    parser.add_argument("--cpus", type=float, default=2)
    parser.add_argument("--memory", default="8g")
    args = parser.parse_args()
    print(json.dumps(run(args.case, args.output, args.image, args.cpus, args.memory)))


if __name__ == "__main__":
    main()
