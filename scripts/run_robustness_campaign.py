"""Run disjoint model shards in isolated JVMs, preserving prefix checkpoints and logs."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--workers",type=int,default=6)
    args=p.parse_args()
    if not 1<=args.workers<=6:p.error("workers must be1..6")
    study=json.loads((args.output/"study.json").read_text())
    logs=args.output/"logs";logs.mkdir(exist_ok=True)
    def worker(tag):
        env=os.environ.copy()
        env.update(PYTHONPATH="src:scripts",MPLCONFIGDIR="/tmp/rocket-mpl",
            JAVA_TOOL_OPTIONS=f"-XX:ActiveProcessorCount=1 -Xmx512m -Djava.util.prefs.userRoot=/tmp/rocket-robustness-{tag}")
        base=[sys.executable,"scripts/study_robustness.py","--output",str(args.output),"--model",tag]
        commands=[("deterministic",base+["--phase","deterministic"])]
        for seed in study["seeds"]:
            for count in (100,500,1000):
                commands.append((f"s{seed}-n{count}",base+["--phase","ensemble","--seed",str(seed),"--count",str(count)]))
        for label,cmd in commands:
            with (logs/f"{tag}-{label}.log").open("a") as f:
                proc=subprocess.run(cmd,env=env,stdout=f,stderr=subprocess.STDOUT)
            if proc.returncode:raise RuntimeError(f"{tag} {label} exited{proc.returncode}; see log")
            print(tag,label,"complete",flush=True)
        return tag
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for future in as_completed([pool.submit(worker,tag) for tag in study["models"]]):
            print("finished",future.result(),flush=True)


if __name__=="__main__":main()
