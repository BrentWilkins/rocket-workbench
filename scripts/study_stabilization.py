"""Compare aft-fin count, forward surfaces, camera-guard proxies and nose ballast.

Forward surfaces are native OpenRocket trapezoidal fins on the forward body.
They are study proxies, not production camera guards or active-control models.
"""

import argparse
import hashlib
import itertools
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path

from rocket_workbench.cli import save_json
from rocket_workbench.flight_model import component, element, generate
from rocket_workbench.simulator import Engine
from study_payload_grid import candidate, mass_records


BASES = ((500, 50, "conical"), (500, 40, "ogive"), (530, 40, "ogive"))
CURRENT_SPAN = 53.65384615384615


def surface_geometry(kind, span, density):
    if kind == "canard":
        count, root, tip, sweep, thickness, station, attachment = 3, 30, 10, 10, 1.2, 5, 1.0
    elif kind == "guard":
        count, root, tip, sweep, thickness, station, attachment = 1, 20, 10, 5, 1.2, 29, 0.5
    else:
        raise ValueError(kind)
    # Polygon centroid; x is axial distance from the fin root leading edge.
    points = ((0, 0), (root, 0), (sweep + tip, span), (sweep, span))
    cross = [a[0] * b[1] - b[0] * a[1]
             for a, b in zip(points, points[1:] + points[:1])]
    area = sum(cross) / 2
    centroid = sum((a[0] + b[0]) * c for a, b, c in
                   zip(points, points[1:] + points[:1], cross)) / (6 * area)
    fin_mass = count * area * thickness * density / 1000
    mass = fin_mass + attachment
    cg = (fin_mass * centroid + attachment * root / 2) / mass
    return dict(count=count, root_mm=root, tip_mm=tip, sweep_mm=sweep,
                span_mm=span, thickness_mm=thickness, body_station_mm=station,
                mass_g=mass, cg_from_root_mm=cg, attachment_allowance_g=attachment)


def augment_model(path, config, variant, value):
    tree = ET.parse(path)
    body = tree.getroot().find(".//stage/subcomponents/bodytube")
    if body is None:
        raise ValueError("No native main body tube")
    subs = body.find("subcomponents")
    if subs is None:
        subs = element(body, "subcomponents")
    if variant in ("baseline", "reference"):
        return dict(added_mass_g=0, added_mass_cg_mm=None)
    if variant == "ballast":
        node = component(subs, "masscomponent", f"Study nose ballast {value:g} g", value, 0,
                         packedlength=0.004, packedradius=0.004)
        element(node, "position", (20 - config.geometry.mm("nose_length")) / 1000, type="top")
        record = dict(added_mass_g=value, added_mass_cg_mm=20)
    else:
        kind = variant.removesuffix("-mass-only")
        surface = surface_geometry(kind, value, config.density.value)
        absolute_cg = config.geometry.mm("nose_length") + surface["body_station_mm"] + surface["cg_from_root_mm"]
        if variant.endswith("-mass-only"):
            node = component(subs, "masscomponent", f"{kind} mass control", surface["mass_g"], 0,
                             packedlength=0.004, packedradius=0.004)
            position = surface["body_station_mm"] + surface["cg_from_root_mm"]
        else:
            node = component(subs, "trapezoidfinset", f"Study {kind} proxy", surface["mass_g"],
                             surface["cg_from_root_mm"], fincount=surface["count"],
                             rootchord=surface["root_mm"] / 1000,
                             tipchord=surface["tip_mm"] / 1000,
                             sweeplength=surface["sweep_mm"] / 1000,
                             height=surface["span_mm"] / 1000,
                             thickness=surface["thickness_mm"] / 1000, crosssection="square")
            position = surface["body_station_mm"]
        element(node, "position", position / 1000, type="top")
        record = dict(added_mass_g=surface["mass_g"], added_mass_cg_mm=absolute_cg,
                      surface=surface, aerodynamic_surface=not variant.endswith("-mass-only"))
    ET.indent(tree)
    tree.write(path, encoding="utf-8", xml_declaration=True)
    return record


def run_case(engine, output, body, nose, shape, motor, count, span, variant="baseline", value=0):
    config = candidate(body, nose, span, shape, motor, fin_count=count)
    tag = f"b{body}-n{nose}-{shape}-{motor}-{count}f-s{span:.4f}-{variant}-{value:g}".replace(".", "p")
    folder = output / tag
    folder.mkdir()
    save_json(folder / "config.json", config.model_dump())
    parts = mass_records(config)
    expected = generate(config, parts, "actual", folder / "input.ork")
    extra = augment_model(folder / "input.ork", config, variant, value)
    save_json(folder / "modification.json", extra)
    rows = []
    conditions = [(0, 0), (2, 0), (4, 0)] if variant == "baseline" else [(0, 0), (4, 0), (4, 90)]
    for wind, heading in conditions:
        doc, load_warnings = engine.load(folder / "input.ork")
        if load_warnings:
            raise ValueError(f"Model load warnings: {load_warnings}")
        sim = engine.new_simulation(doc)
        motor_record = engine.motor(sim, config.motors[0], config)
        engine.configure(sim, config, wind)
        sim.getOptions().getAverageWindModel().setDirection(math.radians(heading))
        mass = engine.mass(sim)
        expected_dry = expected["dry_mass_g"] + extra["added_mass_g"]
        expected_cg = (expected["dry_mass_g"] * expected["dry_cg_x_mm"]
                       + extra["added_mass_g"] * (extra["added_mass_cg_mm"] or 0)) / expected_dry
        if (abs(mass["dry_mass_g"] - expected_dry) > 1e-5
                or abs(mass["dry_cg_x_mm"] - expected_cg) > 1e-4
                or abs(mass["launch_mass_g"] - expected_dry - motor_record["loaded_mass_g"]) > 1e-5):
            raise ValueError(f"Native OpenRocket mass/CG does not match study ledger: {tag}")
        result = engine.run(sim)
        save_json(folder / f"wind{wind}-heading{heading}.json", result)
        m = result["metrics"]
        rows.append(dict(design=tag, body_mm=body, nose_mm=nose, nose_shape=shape,
                         motor=f"{motor}-{config.motors[0].delay_s:g}", fin_count=count,
                         span_mm=span, variant=variant, variant_size=value,
                         wind_m_s=wind, wind_heading_deg=heading,
                         launch_mass_g=mass["launch_mass_g"], loaded_cg_mm=mass["launch_cg_x_mm"],
                         added_mass_g=extra["added_mass_g"],
                         collar_mass_g=parts["fin-collar"]["mass_g"],
                         status=result["execution"], warnings=result["warnings"],
                         apogee_m=m.get("apogee_m"), guide_m_s=m.get("guide_departure_m_s"),
                         stability_cal=m.get("minimum_ascent_stability_cal"),
                         deployment_m_s=m.get("deployment_speed_m_s"),
                         descent_m_s=m.get("landing_descent_m_s"), drift_m=m.get("landing_displacement_m")))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mode", choices=("fins", "forward", "small-guard", "references", "smoke"), required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    if args.mode == "fins":
        cases = [(body, nose, shape, motor, count, span, "baseline", 0)
                 for (body, nose, shape), motor, count, span in itertools.product(
                     BASES, ("D12", "E12"), (3, 4), (45, 50, CURRENT_SPAN, 55))]
    else:
        variants = [("ballast", mass) for mass in (2, 5, 10)]
        variants += [(kind, span) for kind in ("canard", "canard-mass-only") for span in (10, 20)]
        variants += [(kind, span) for kind in ("guard", "guard-mass-only") for span in (5, 10)]
        if args.mode == "references":
            variants = [("reference", 0)]
        if args.mode == "small-guard":
            variants = [(kind, span) for kind in ("guard", "guard-mass-only") for span in (1, 2)]
        if args.mode == "smoke":
            variants = [("guard", 5), ("canard", 10)]
            bases, motors = BASES[:1], ("E12",)
        else:
            bases, motors = BASES, ("D12", "E12")
        cases = [(body, nose, shape, motor, 3, CURRENT_SPAN, kind, size)
                 for (body, nose, shape), motor, (kind, size) in itertools.product(bases, motors, variants)]
    save_json(args.output / "search-spec.json", dict(mode=args.mode, configurations=len(cases),
              cases=cases, active_control="Not modeled; fixed zero-cant surfaces only",
              guard="Single-fin aerodynamic proxy at forward-body station 29 mm; lens pose/FOV unverified",
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
    rows = []
    with Engine() as engine:
        save_json(args.output / "engine.json", engine.versions())
        for index, case in enumerate(cases, 1):
            rows.extend(run_case(engine, args.output, *case))
            save_json(args.output / "comparison.json", rows)
            print(f"completed {index}/{len(cases)} configurations", flush=True)


if __name__ == "__main__":
    main()
