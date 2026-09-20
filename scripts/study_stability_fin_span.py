"""Screen larger fin spans for the primary C11/D12/E12 motor envelope."""

import argparse
import hashlib
import json
from argparse import Namespace
from pathlib import Path

from rocket_workbench.cli import save_json, workflow
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine

from study_motor24 import configuration


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--span", type=float, nargs="+", default=[45, 55, 65])
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    summary = []

    with Engine() as engine:
        for span in args.span:
            for platform in ("24-cd", "24-e"):
                for profile in ("nominal", "upper-avionics"):
                    config = configuration(platform, profile)
                    data = config.model_dump()
                    data["name"] = f"bt60-{platform}-span{span:g}-{profile}"
                    data["geometry"]["fin_span"]["value"] = span
                    data["geometry"]["fin_span"]["provenance"] = "estimate"
                    data["geometry"]["fin_span"]["source"] = "Stability fin-span screening"
                    # Compare only the intended C11/D12 or E12 motor families,
                    # retaining all certified delays for recovery screening.
                    from rocket_workbench.config import Config
                    config = Config.model_validate(data)
                    folder = out / config.name
                    folder.mkdir()
                    path = folder / "config.yaml"
                    save_json(path, config.model_dump())
                    digest = hashlib.sha256(
                        json.dumps(config.model_dump(), sort_keys=True).encode()
                    ).hexdigest()
                    save_json(folder / "manifest.json", {
                        "configuration_sha256": digest,
                        "command": "study-stability-fin-span",
                    })
                    workflow(Namespace(command="simulate", strict=False), config, path, folder, digest, engine)
                    results = json.loads((folder / "results.json").read_text())
                    for case in results["cases"]:
                        if case["loading"] == "actual":
                            metrics = case.get("metrics", {})
                            summary.append({
                                "configuration": config.name,
                                "span_mm": span,
                                "platform": platform,
                                "profile": profile,
                                "case": case["id"],
                                "evaluation": case["evaluation"],
                                "apogee_m": metrics.get("apogee_m"),
                                "minimum_stability_cal": metrics.get("minimum_ascent_stability_cal"),
                                "deployment_speed_m_s": metrics.get("deployment_speed_m_s"),
                            })
    save_json(out / "comparison.json", summary)
    seal_run(out)
    print(f"FIN SPAN STABILITY SCREEN COMPLETE {out}", flush=True)


if __name__ == "__main__":
    main()
