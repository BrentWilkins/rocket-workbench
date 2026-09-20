"""Event/guide, baseline regression, reproducibility and timestep checks on retained models."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from rocket_workbench.cli import save_json
from rocket_workbench.config import Config
from rocket_workbench.robustness import scenarios
from rocket_workbench.simulator import Engine
from study_robustness import run_one, sampled_config


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args(); out=args.output; audit=out/"verification";audit.mkdir(exist_ok=True)
    study=json.loads((out/"study.json").read_text())
    models=study["models"]
    for relative,digest in study["files_sha256"].items():
        if hashlib.sha256((out/relative).read_bytes()).hexdigest()!=digest:
            raise ValueError(f"Prepared input changed: {relative}")
    for path,digest in study["source_sha256"].items():
        if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=digest:
            raise ValueError(f"Study source changed: {path}")
    if hashlib.sha256((out/"samples.json").read_bytes()).hexdigest()!=study["samples_sha256"]:
        raise ValueError("Sample manifest changed")
    rows=[]
    with Engine() as engine:
        for tag in models:
            folder=out/tag;c=Config.model_validate_json((folder/"nominal.json").read_text())
            upper=Config.model_validate_json((folder/"upper.json").read_text())
            parts=json.loads((folder/"parts.json").read_text())
            selected=[(s,c,parts) for s in scenarios() if s["id"] in ("rod0.9144-wind0-heading0","rod0.9144-wind6-heading0")]
            samples=[]
            for f in out.glob(f"ensemble-*/{tag}.jsonl"):
                samples.extend(json.loads(l) for l in f.read_text().splitlines())
            samples=[r for r in samples if r["metrics"].get("powered_min_stability_cal") is not None]
            if samples:
                worst=min(samples,key=lambda r:r["metrics"]["powered_min_stability_cal"])
                cfg,printed=sampled_config(c,upper,parts,worst["inputs"])
                selected.append((worst["inputs"],cfg,printed))
            for scenario,cfg,printed in selected:
                for dt in (.01,.005,.0025):
                    path=audit/f"{tag}-{scenario['id']}-dt{dt:g}.json"
                    if path.exists():r=json.loads(path.read_text())
                    else:
                        r,_=run_one(engine,folder,cfg,printed,scenario,keep_trace=True,timestep=dt)
                        save_json(path,r)
                    event=r["metrics"]["rod_exit_time_s"]; a=r["timeseries"]
                    travel=float(np.interp(event,a["time_s"],a["altitude_m"]))/np.cos(np.radians(scenario["tilt_deg"]))
                    overshoot=travel-r["effective_guide_m"]
                    # OR checks threshold after a rod-constrained step (dt/5).
                    bound=r["metrics"]["guide_departure_m_s"]*dt/5*1.1+.002
                    if overshoot<-.002 or overshoot>bound:
                        raise ValueError(f"Guide event inconsistent {tag}: {overshoot}, bound {bound}")
                    rows.append(dict(design=tag,scenario=scenario["id"],dt=dt,execution=r["execution"],
                        guide_overshoot_m=overshoot,metrics=r["metrics"],warnings=r["warnings"]))
            # A fixed turbulent case repeated under the same seed must match.
            scenario=scenarios()[-1]
            a,_=run_one(engine,folder,c,parts,scenario,keep_trace=False)
            b,_=run_one(engine,folder,c,parts,scenario,keep_trace=False)
            keys=a["metrics"].keys() | b["metrics"].keys()
            same = all(a["metrics"].get(k)==b["metrics"].get(k) or
                (isinstance(a["metrics"].get(k),(float,int)) and isinstance(b["metrics"].get(k),(float,int)) and
                 np.isclose(a["metrics"][k],b["metrics"][k],rtol=1e-10,atol=1e-8)) for k in keys)
            if not same:
                raise ValueError("Same-seed turbulent runs are not repeatable")
            save_json(audit/f"{tag}-repeatability.json",dict(equal_within_tolerance=True,rtol=1e-10,atol=1e-8,
                seed=scenario["seed"],metrics=a["metrics"],repeated_metrics=b["metrics"]))
            print("verified",tag,flush=True)
    save_json(audit/"comparison.json",rows)
    save_json(audit/"provenance.json",dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        study_sha256=hashlib.sha256((out/"study.json").read_bytes()).hexdigest(),
        scope="nominal calm/6m/s plus currently lowest sampled stability; time-step convergence must be interpreted, not assumed"))


if __name__=="__main__":main()
