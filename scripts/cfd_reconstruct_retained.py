"""Reconstruct retained parallel fields in a NEW copy after interrupted logging.

Never upgrades the original solver execution status; records reconstruction only.
"""

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--time", type=int, required=True)
    parser.add_argument("--ranks", type=int, required=True)
    args = parser.parse_args()
    source = args.case.resolve(strict=True)
    if args.time <= 0 or args.ranks < 1:
        raise ValueError("Require positive recorded time and rank count")
    for rank in range(args.ranks):
        for field in ("U", "p", "k", "omega", "nut"):
            if not (source / f"processor{rank}" / str(args.time) / field).is_file():
                raise ValueError(f"Missing retained rank {rank} field {field}")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    for name in ("0", "constant", "system", "postProcessing"):
        shutil.copytree(source / name, output / name)
    for path in source.iterdir():
        if path.is_file():
            shutil.copy2(path, output / path.name)
    for rank in range(args.ranks):
        for name in ("constant", str(args.time)):
            shutil.copytree(source / f"processor{rank}" / name,
                            output / f"processor{rank}" / name)
    image_id = json.loads((source / "image.json").read_text())["Id"]
    command = ["docker", "run", "--rm", "--network=none", "--cpus", "4", "--memory", "16g",
               "--mount", f"type=bind,src={output},dst=/case", image_id,
               "source /usr/lib/openfoam/openfoam2512/etc/bashrc && "
               f"reconstructPar -time {args.time}"]
    result = subprocess.run(command, capture_output=True, text=True)
    log = result.stdout + result.stderr
    (output / "reconstruction.log").write_text(log)
    passed = (result.returncode == 0 and "FOAM FATAL" not in log and "End" in log.splitlines()
              and (output / str(args.time) / "U").is_file()
              and (output / str(args.time) / "p").is_file())
    record = {"source_case": str(source), "time": args.time, "ranks": args.ranks,
              "command": command, "returncode": result.returncode,
              "reconstruction_passed": passed,
              "source_execution_status_unchanged": True,
              "limitation": "Original solver completion was not fully logged; retained fields only"}
    (output / "reconstruction.json").write_text(json.dumps(record, indent=2) + "\n")
    (output / "case.foam").touch()
    print(json.dumps(record))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
