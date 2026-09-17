"""Screen sub-50 mm conical noses on the current D12 insert-bay design."""

import argparse
import hashlib
import json
from argparse import Namespace
from pathlib import Path

from rocket_workbench.cli import save_json, workflow
from rocket_workbench.config import Config
from rocket_workbench.progression import summarize_cases
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine
from study_avionics import place_wadding
from study_sourced_chute import configuration as sourced_chute_configuration


NOSE_LENGTHS_MM = (30, 35, 40, 45, 50)
STOCK_PORTA_PAD_GUIDE_LENGTH_M = 0.762


def variant(nose_length_mm: int) -> Config:
    """Shorten only the nose and preserve shoulder-relative component stations."""
    base = sourced_chute_configuration(False, 0.53, insert_trial=True)
    data = base.model_dump()
    old_length = base.geometry.mm("nose_length")
    delta = nose_length_mm - old_length
    source = "Bounded current-D12 sub-50 mm conical nose-length screen"

    data["name"] = f"d12-conical-n{nose_length_mm}-b500-insert"
    data["geometry"]["nose_length"].update(
        value=nose_length_mm,
        provenance="estimate",
        source=source,
    )
    data["launch"]["guide_length"].update(
        value=STOCK_PORTA_PAD_GUIDE_LENGTH_M,
        provenance="manufacturer specification",
        source="Estes Porta-Pad II stock two-piece 1/8-inch rod is 30 inches; usable travel must still be measured on assembled pad",
    )

    # Purchased components and avionics remain fixed relative to the shoulder.
    for item in data["purchased_masses"]:
        item["x"]["value"] += delta
    data["payload"]["cg_x"]["value"] += delta

    # Recompute the recovery-wadding station from the changed airframe bounds.
    place_wadding(data)
    return Config.model_validate(data)


def metric_range(cases: list[dict], key: str) -> list[float] | None:
    loaded = [case for case in cases if case["loading"] == "actual"]
    values = [case.get("metrics", {}).get(key) for case in loaded]
    if not values or any(value is None for value in values):
        return None
    return [min(values), max(values)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)

    save_json(
        args.output / "search-spec.json",
        {
            "nose_shape": "conical",
            "nose_lengths_mm": list(NOSE_LENGTHS_MM),
            "body_length_mm": 500,
            "motor": "D12-5",
            "winds_m_s": [0, 2, 4],
            "launch_guide": "Estes Porta-Pad II stock 30-inch (0.762 m), 1/8-inch rod; usable travel and rod stiffness require physical checks",
            "chute": "Apogee 29093 24-inch nominal-mass lower-Cd bound",
            "bay_retention": "m2-insert-trial-v1",
            "designs": len(NOSE_LENGTHS_MM),
            "flights": len(NOSE_LENGTHS_MM) * 9,
            "objective": "Identify whether a conical nose shorter than 50 mm preserves all configured gates while reducing printed mass",
            "limitations": "Bounded simulation screen, not aerodynamic optimization or flight clearance; modeled 0.762 m guide may exceed usable rod travel above the standoff, and rod flex is not modeled; hardware mass, packing, surface finish, and OpenRocket drag uncertainty remain unresolved.",
        },
    )

    rows = []
    with Engine() as engine:
        for nose_length_mm in NOSE_LENGTHS_MM:
            config = variant(nose_length_mm)
            folder = args.output / config.name
            folder.mkdir()
            path = folder / "config.yaml"
            save_json(path, config.model_dump())
            save_json(folder / "resolved-inputs.json", config.model_dump())
            digest = hashlib.sha256(
                json.dumps(config.model_dump(), sort_keys=True).encode()
            ).hexdigest()
            save_json(
                folder / "manifest.json",
                {"configuration_sha256": digest, "command": "d12-nose-length-screen"},
            )
            workflow(
                Namespace(command="simulate", strict=False),
                config,
                path,
                folder,
                digest,
                engine,
            )

            cases = json.loads((folder / "results.json").read_text())["cases"]
            mass_properties = json.loads(
                (folder / "cad" / "mass-properties.json").read_text()
            )
            actual_cases = [case for case in cases if case["loading"] == "actual"]
            dry_masses = [case["mass"]["dry_mass_g"] for case in actual_cases]
            nose_mass = mass_properties["nose-bay"]["mass_g"]
            row = {
                "design": config.name,
                "nose_length_mm": nose_length_mm,
                "nose_fineness_ratio": nose_length_mm / config.geometry.mm("body_od"),
                "nose_bay_mass_g": nose_mass,
                "loaded_dry_mass_g": [min(dry_masses), max(dry_masses)],
                "summary": summarize_cases(cases),
            }
            for metric in (
                "apogee_m",
                "peak_powered_speed_m_s",
                "minimum_ascent_stability_cal",
                "guide_departure_m_s",
                "deployment_speed_m_s",
                "landing_descent_m_s",
            ):
                row[metric] = metric_range(cases, metric)
            rows.append(row)
            seal_run(folder)
            print(
                "NOSE COMPLETE",
                config.name,
                row["summary"]["planned"],
                flush=True,
            )

    save_json(args.output / "comparison.json", rows)
    lines = [
        "# Current D12 conical nose-length screen",
        "",
        "Nominal-mass, lower-Cd 24-inch chute configuration. This is a bounded simulation screen, not flight clearance or a validated aerodynamic optimum.",
        "The launch model uses the stock Porta-Pad II 30-inch rod rather than the earlier provisional 36-inch assumption. Usable travel and 1/8-inch rod flex still require physical checks.",
        "",
        "| Nose mm | L/D | Nose/bay mass g | Planned passes / 6 | Loaded stability cal | Loaded apogee m | Guide departure m/s |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| {row['nose_length_mm']} | {row['nose_fineness_ratio']:.3f} | "
            f"{row['nose_bay_mass_g']:.2f} | {row['summary']['planned']['passed']} | "
            f"{row['minimum_ascent_stability_cal']} | {row['apogee_m']} | "
            f"{row['guide_departure_m_s']} |"
        )
    lines += [
        "",
        "All purchased components and avionics retain their stations relative to the nose shoulder. CAD mass and CG are regenerated for every nose length.",
    ]
    (args.output / "report.md").write_text("\n".join(lines) + "\n")
    seal_run(args.output)
    print("D12 NOSE SCREEN COMPLETE", args.output, flush=True)


if __name__ == "__main__":
    main()
