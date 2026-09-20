"""Bounded all-upper-mass 60-inch-guide corner; not a worst-CG proof."""

import argparse
import hashlib
import json
from pathlib import Path

from rocket_workbench.cli import save_json
from rocket_workbench.config import Config
from rocket_workbench.robustness import scenarios
from rocket_workbench.simulator import Engine
from study_robustness import run_one, sampled_config


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, required=True)
    args = parser.parse_args()
    root = args.study
    study = json.loads((root / "study.json").read_text())
    for path, digest in study["source_sha256"].items():
        if hashlib.sha256(Path(path).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Study source changed: {path}")
    for path, digest in study["files_sha256"].items():
        if hashlib.sha256((root / path).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Prepared input changed: {path}")
    output = root / "long-guide-upper"
    output.mkdir(exist_ok=False)
    scenario = next(s for s in scenarios() if s["id"] == "rod1.524-wind6-heading0")
    records = []
    with Engine() as engine:
        for tag in study["models"]:
            folder = root / tag
            nominal = Config.model_validate_json((folder / "nominal.json").read_text())
            upper = Config.model_validate_json((folder / "upper.json").read_text())
            parts = json.loads((folder / "parts.json").read_text())
            sample = {f"mass:{item.role}": 1. for item in nominal.purchased_masses}
            sample.update({"mass:payload": 1., "finish_g": 5.})
            case = {**scenario, **sample, "id": "all-upper-finish5-rod1.524-wind6-heading0"}
            cfg, printed = sampled_config(nominal, upper, parts, case)
            result, motor = run_one(engine, folder, cfg, printed, case, keep_trace=True)
            result["corner_scope"] = "All upper mass/station interpolation plus 5 g fin finish; not worst CG"
            result["motor"] = motor
            save_json(output / f"{tag}.json", result)
            record = {"design": tag, "execution": result["execution"],
                      "mass_audit": result["mass_audit"], "metrics": result["metrics"],
                      "effective_guide_m": result["effective_guide_m"],
                      "warnings": result["warnings"]}
            records.append(record)
            print(json.dumps(record), flush=True)
        versions = engine.versions()
    save_json(output / "comparison.json", records)
    save_json(output / "provenance.json", {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "study_sha256": hashlib.sha256((root / "study.json").read_bytes()).hexdigest(),
        "versions": versions, "scope": "Six all-upper mass corners, not a stochastic or worst-CG claim",
        "nominal_rod_m": 1.524, "wind_m_s": 6, "wind_toward_heading_deg": 0,
        "tilt_deg": 0, "turbulence_m_s": 0, "finish_g": 5,
    })


if __name__ == "__main__":
    main()
