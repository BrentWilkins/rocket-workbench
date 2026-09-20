"""Reproducible paired flight experiments. Run prepare, deterministic, then ensemble."""
import argparse
import copy
import hashlib
import json
import math
import os
import shutil
from uuid import uuid4
from pathlib import Path

import numpy as np

from rocket_workbench.cli import save_json
from rocket_workbench.config import Config
from rocket_workbench.flight_model import generate
from rocket_workbench.robustness import BASES, SPAN_MM, SEEDS, scenarios, samples, configure_wind, flight_metrics, load_profile
from rocket_workbench.simulator import Engine
from study_payload_grid import candidate, mass_records


def prepare(out, count):
    out.mkdir(parents=True, exist_ok=False)
    models = []
    for body, nose, shape in BASES:
        for motor in ("D12", "E12"):
            tag = f"b{body}-n{nose}-{shape}-{motor}"
            folder = out / tag
            folder.mkdir()
            nominal = candidate(body, nose, SPAN_MM, shape, motor)
            upper = candidate(body, nose, SPAN_MM, shape, motor, upper=True, finish_allowance_g=0)
            parts = mass_records(nominal)
            save_json(folder / "nominal.json", nominal.model_dump())
            save_json(folder / "upper.json", upper.model_dump())
            save_json(folder / "parts.json", parts)
            expected = generate(nominal, parts, "actual", folder / "input.ork")
            save_json(folder / "ledger.json", expected)
            models.append(tag)
            print(f"prepared {tag}", flush=True)
    roles = [p.role for p in nominal.purchased_masses] + ["payload"]
    manifest = [s for seed in SEEDS for s in samples(count, seed, roles)]
    save_json(out / "samples.json", manifest)
    sources = [Path(__file__), Path("src/rocket_workbench/robustness.py"),Path("src/rocket_workbench/simulator.py"),
               Path("src/rocket_workbench/flight_model.py"),Path("scripts/study_payload_grid.py"),Path("scripts/study_de_geometry.py"),Path("uv.lock")]
    snapshot=out/"source";snapshot.mkdir()
    for path in sources:
        shutil.copyfile(path,snapshot/path.name)
    save_json(out / "study.json", dict(schema_version=4, models=models, seeds=SEEDS, samples_per_seed=count,
        turbulence_seed_policy="Each native altitude-level PinkNoiseWindModel receives a deterministic sample/level seed; simulation seed alone is insufficient in OR24.12",
        source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        samples_sha256=hashlib.sha256((out/"samples.json").read_bytes()).hexdigest(),
        guide_policy="Physical rod minus native lug offset supplied explicitly to OR event threshold; 24.12 ignores its calculated effective length",
        scope="conditional engineering robustness, not measured failure probability",
        mass_bounds="existing nominal to upper purchased/payload records, joint mass/station interpolation",
        finish_g=[0,5], launcher_tilt_deg=[0,2], wind_speed_m_s=[0,6], shear_m_s=[-2,2],
        veer_deg=[-30,30], turbulence_std_m_s=[0,.5],
        distributions="independent uniform exploratory bounds; component mass and station are coupled",
        fixed_uncertainties=["motor curve/delay (no lot evidence)", "chute Cd .53 (plastic hardware uncharacterized)",
            "independent placement tolerance (no evidence)", "aerodynamic model error", "fin misalignment"],
        caveats=["chute mass/Cd inherited nylon proxy, not validated for selected Estes plastic chute",
                 "inertias are native OR component approximations, not measured or resolved electronics",
                 "current modeled lugs are 1/8-inch; rod length study does not validate 3/16-inch guide fit"],
        files_sha256={str(p.relative_to(out)):hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in out.glob("*/*") if p.is_file()}))


def sampled_config(nominal, upper, parts, sample):
    data = nominal.model_dump()
    high = {p.role:p for p in upper.purchased_masses}
    for p in data["purchased_masses"]:
        f = sample.get(f"mass:{p['role']}", 0)
        u = high[p["role"]]
        for key, target in (("mass",u.mass.value), ("x",u.x.value)):
            p[key]["value"] += f*(target-p[key]["value"])
    f = sample.get("mass:payload", 0)
    for key in ("mass", "cg_x"):
        data["payload"][key]["value"] += f*(getattr(upper.payload,key).value-data["payload"][key]["value"])
    printed = copy.deepcopy(parts)
    printed["fin-collar"]["mass_g"] += sample.get("finish_g", 0)
    return Config.model_validate(data), printed


def run_one(engine, folder, config, parts, scenario, keep_trace=True, timestep=None):
    # Each worker uses a separate model folder; original input.ork is never overwritten.
    # Separate tool sandboxes may reuse the same PID while sharing this filesystem.
    path = folder / f"work-{uuid4().hex}.ork"
    expected = generate(config, parts, "actual", path)
    try:
        doc, warnings = engine.load(path)
    finally:
        path.unlink()
    if warnings:
        raise ValueError(f"Model load warnings: {warnings}")
    sim = engine.new_simulation(doc)
    motor = engine.motor(sim, config.motors[0], config)
    engine.configure(sim, config, 0)
    configure_wind(engine, sim, scenario)
    if timestep:
        sim.getOptions().setTimeStep(timestep)
    mass = engine.mass(sim)
    for field in ("dry_mass_g", "dry_cg_x_mm"):
        if abs(expected[field]-mass[field]) > 1e-5:
            raise ValueError(f"Ledger mismatch {field}")
    if abs(mass["launch_mass_g"]-mass["dry_mass_g"]-motor["loaded_mass_g"]) > 1e-5:
        raise ValueError("Motor mass counted incorrectly")
    conditions = sim.getOptions().toSimulationConditions()
    status = engine.core.simulation.SimulationStatus(sim.getActiveConfiguration(), conditions)
    effective = float(status.getEffectiveLaunchRodLength())
    if effective<=0:
        raise ValueError("No usable launch-guide travel")
    # 24.12 BasicEventSimulationEngine checks conditions.getLaunchRodLength(),
    # not status.getEffectiveLaunchRodLength(). Supply physical usable travel.
    sim.getOptions().setLaunchRodLength(effective)
    # Ground-level vector convention audit (zero-turbulence clone).
    wind = sim.getOptions().getMultiLevelWindModel().clone()
    for level in wind.getLevels():
        level.setStandardDeviation(0.)
    v = wind.getWindVelocity(0., config.launch.elevation.value, 0.)
    a = np.asarray(scenario["wind"]["levels"])
    intended = [np.interp(0,a[:,0],a[:,k]) for k in (1,2)]
    if not np.allclose([v.x,v.y], -np.asarray(intended), atol=1e-8):
        raise ValueError(f"Wind coordinate mismatch: native {v.x,v.y}, intended {intended}")
    result = engine.run(sim)
    result.update(design=folder.name, scenario=scenario["id"], engine="OpenRocket",
                  inputs=scenario, mass_audit=mass, effective_guide_m=effective,
                  nominal_guide_m=scenario["guide_m"], timestep_s=sim.getOptions().getTimeStep())
    if result["timeseries"]:
        result["metrics"].update(flight_metrics(result))
    if keep_trace:
        atmosphere = conditions.getAtmosphericModel()
        gravity = conditions.getGravityModel()
        table = []
        for h in range(0,1001,25):
            z = config.launch.elevation.value+h
            air = atmosphere.getConditions(z)
            location = engine.core.util.WorldCoordinate(config.launch.latitude.value, config.launch.longitude.value, z)
            table.append([z, float(air.getPressure()), float(air.getTemperature()), float(gravity.getGravity(location))])
        result["atmosphere"] = dict(columns=["height_msl_m", "pressure_pa", "temperature_k", "gravity_m_s2"], levels=table)
    if not keep_trace:
        result.pop("timeseries", None)
    return result, motor


def run(out, phase, seed, limit, wind_paths, models=None):
    study = json.loads((out/"study.json").read_text())
    if study.get("schema_version") != 4:
        raise ValueError("Prepare a fresh schema4 study; earlier runs lack seeded altitude-level turbulence")
    for path,digest in study["source_sha256"].items():
        if hashlib.sha256(Path(path).read_bytes()).hexdigest()!=digest:
            raise ValueError(f"Study source changed: {path}; prepare a new version, do not mix runs")
    if hashlib.sha256((out/"samples.json").read_bytes()).hexdigest()!=study["samples_sha256"]:
        raise ValueError("Sample manifest changed")
    manifest = json.loads((out/"samples.json").read_text())
    dest = out / ("deterministic" if phase == "deterministic" else f"ensemble-{seed}")
    dest.mkdir(exist_ok=True)
    with Engine() as engine:
        selected=study["models"] if not models else models
        if any(tag not in study["models"] for tag in selected):
            raise ValueError("Unknown model selection")
        save_json(dest/("runtime-"+"_".join(selected)+".json"), engine.versions())
        for tag in selected:
            folder = out/tag
            nominal = Config.model_validate_json((folder/"nominal.json").read_text())
            upper = Config.model_validate_json((folder/"upper.json").read_text())
            parts = json.loads((folder/"parts.json").read_text())
            cases = scenarios() if phase == "deterministic" else [s for s in manifest if s["master_seed"] == seed and s["index"] < limit]
            for path in wind_paths:
                if phase == "deterministic":
                    p = load_profile(path, nominal.launch.elevation.value)
                    cases.append(dict(id=f"imported-{p['sha256'][:12]}", wind=p, guide_m=.9144,
                                      tilt_deg=0, tilt_heading_deg=0, turbulence_m_s=0, seed=SEEDS[0]))
            result_file = dest/f"{tag}.jsonl"
            done = set()
            if result_file.exists():
                done = {json.loads(l)["scenario"] for l in result_file.read_text().splitlines()}
            for i, s in enumerate(cases):
                if s["id"] in done:
                    continue
                cfg, printed = sampled_config(nominal, upper, parts, s)
                try:
                    result, motor = run_one(engine, folder, cfg, printed, s,
                                           keep_trace=phase == "deterministic" or i < 5)
                    if phase == "deterministic":
                        save_json(folder/"motor.json", motor)
                except Exception as exc:
                    result = dict(design=tag, scenario=s["id"], inputs=s, engine="OpenRocket",
                                  execution="simulation failed", error=f"{type(exc).__name__}: {exc}",
                                  warnings=[], metrics={})
                with result_file.open("a") as f:
                    f.write(json.dumps(result, allow_nan=False)+"\n")
                if (i+1) % 50 == 0 or i == len(cases)-1 or result["execution"] != "completed":
                    print(tag, phase, i+1, "/", len(cases), result["execution"], result.get("error"), flush=True)
    print(f"saved {dest}", flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--phase", choices=("prepare","deterministic","ensemble"), required=True)
    p.add_argument("--count", type=int, default=1000)
    p.add_argument("--seed", type=int, choices=SEEDS, default=SEEDS[0])
    p.add_argument("--wind-profile", type=Path, action="append", default=[])
    p.add_argument("--model", nargs="+", help="Disjoint model shards for separate JVM workers")
    args = p.parse_args()
    if args.count < 1 or args.count > 10000:
        p.error("count must be 1..10000")
    if args.phase == "prepare":
        prepare(args.output, args.count)
    else:
        run(args.output, args.phase, args.seed, args.count, args.wind_profile,args.model)


if __name__ == "__main__":
    main()
