"""Bounded D12-5/E12-6 geometry screen on the sourced 24-inch recovery design.

The fin collar is parametric and stands in for the hand-finished integrated collar.
Body-joint and mount masses are explicit estimates until hardware is weighed.
"""

import argparse
import hashlib
import itertools
import json
from argparse import Namespace
from pathlib import Path

from rocket_workbench.cli import save_json, workflow
from rocket_workbench.config import Config, mass_cg
from rocket_workbench.provenance import seal_run
from rocket_workbench.simulator import Engine

from study_avionics import place_wadding
from study_motor24 import DIGESTS, LIMITS
from study_sourced_chute import configuration as sourced_configuration


def quantity(value, unit, source, provenance="estimate"):
    return dict(value=value, unit=unit, provenance=provenance, source=source)


def configuration(body_mm, nose_mm, span_mm, motor_name, *, upper=False, chute_cd=0.53,
                  integrated_collar=False, fin_collar_mass_g=None, finish_allowance_g=0.0,
                  collar_calibration_g=None):
    base = sourced_configuration(upper, chute_cd, insert_trial=True)
    data = base.model_dump()
    source = "Bounded D12/E12 geometry screen; nominal dimensions and masses require measurement"
    span_tag = f"{span_mm:.4f}".rstrip("0").rstrip(".").replace(".", "p")
    data["name"] = f"de-b{body_mm:g}-n{nose_mm:g}-s{span_tag}-{motor_name.lower()}-{'upper' if upper else 'nominal'}-cd{round(chute_cd*100):03d}"
    data["avionics_profile"] = "xiao-sensor-logger-v2"
    if integrated_collar:
        if abs(span_mm - 53.65384615384615) > 1e-3:
            raise ValueError("Integrated collar mass override requires its original 53.65 mm fin span")
        data["name"] += "-integrated"
        if fin_collar_mass_g is None:
            collar_mass = 23.760391 * base.density.value
            collar_source = "integrated-collar STEP volume times assumed PLA density; printed mass unmeasured"
            collar_provenance = "estimate"
        else:
            collar_mass = fin_collar_mass_g + finish_allowance_g
            collar_source = (f"User-weighed raw integrated collar {fin_collar_mass_g:g} g including tiny removable brim; "
                             f"{finish_allowance_g:g} g provisional finish allowance")
            collar_provenance = "measured" if finish_allowance_g == 0 else "estimate"
            data["name"] += "-weighed"
        data["printed_measurements"]["fin-collar"] = (
            quantity(collar_mass, "g", collar_source, collar_provenance),
            quantity(522.285 + body_mm - 500 + nose_mm - 50, "mm",
                     "integrated-collar STEP center of volume translated to aft body end; printed CG unmeasured"),
        )
    geometry = data["geometry"]
    old_body = base.geometry.mm("body_length")
    old_nose = base.geometry.mm("nose_length")
    body_delta = body_mm - old_body
    nose_delta = nose_mm - old_nose
    for key, value in (("body_length", body_mm), ("nose_length", nose_mm), ("fin_span", span_mm)):
        geometry[key].update(value=value, provenance="estimate", source=source)

    # All installed stations follow the nose shoulder. Only the tube, aft
    # hardware, and launch lugs additionally move when body length changes.
    for item in data["purchased_masses"]:
        role = item["role"]
        item["x"]["value"] += nose_delta
        if role == "body":
            item["mass"]["value"] *= body_mm / old_body
            item["x"]["value"] += body_delta / 2
        elif role in ("mount", "collar_adhesive"):
            item["x"]["value"] += body_delta
        elif role == "lugs":
            item["x"]["value"] += body_delta / 2
    data["payload"]["cg_x"]["value"] += nose_delta

    # The chosen two-tube build introduces a coupler and bond that were absent
    # from the earlier unjointed airframe ledger. It remains a sensitivity
    # allowance, not an asserted mass of the delivered part.
    data["purchased_masses"].append(dict(
        role="airframe_joint", name="BT-60 coupler plus bond allowance",
        mass=quantity(6.0 if upper else 3.0, "g", "Unmeasured two-tube coupler/bond allowance; replace with measured mass"),
        x=quantity(nose_mm + body_mm / 2, "mm", "Provisional central splice station; verify clearance from packed recovery"),
    ))

    # Both motors use the same 95 mm tube. The D12 needs a short-motor spacer;
    # the E12 uses the long mount without it.
    mount = next(item for item in data["purchased_masses"] if item["role"] == "mount")
    if motor_name == "E12":
        mount_start = nose_mm + body_mm - geometry["motor_mount_length"]["value"] - geometry["motor_overhang"]["value"]
        mount["mass"].update(value=12.0, provenance="estimate", source="Provisional 24 mm mount without D12 spacer")
        mount["x"].update(value=mount_start + 47.5, provenance="estimate", source="Provisional 95 mm mount midpoint")
        delay = 6
    else:
        mount_start = nose_mm + body_mm - geometry["motor_mount_length"]["value"] - geometry["motor_overhang"]["value"]
        spacer_end = nose_mm + body_mm - 70
        mount_mass, mount_cg = mass_cg([(12.0, mount_start + 47.5), (1.0, spacer_end - 12.5)])
        mount["mass"].update(value=mount_mass, provenance="estimate", source="Provisional 24 mm mount and removable D12 spacer")
        mount["x"].update(value=mount_cg, provenance="estimate", source="Mount and spacer mass balance")
        delay = 5
    data["motors"] = [dict(
        designation=motor_name, delay_s=delay, digest=DIGESTS[motor_name],
        max_liftoff_mass=quantity(
            LIMITS[motor_name][delay], "g", "Manufacturer maximum liftoff mass; verified in prior motor study"
        ),
    )]
    data["launch"]["wind_speeds"] = [quantity(v, "m/s", "Bounded constant-wind geometry screen") for v in (0, 2, 4)]
    place_wadding(data)
    if collar_calibration_g is not None:
        if upper or integrated_collar:
            raise ValueError("Parametric collar calibration is for nominal, non-current geometries")
        from rocket_workbench.cad import shapes

        preliminary = Config.model_validate(data)
        parametric = shapes(preliminary)["fin-collar"].val()
        reference_parametric_g = 26.268925743573625  # 53.6538 mm span, 1.24 g/cm3 baseline
        reference_cg_offset_mm = 522.285 - 521.385752917282
        calibrated_mass = parametric.Volume() / 1000 * preliminary.density.value
        calibrated_mass *= collar_calibration_g / reference_parametric_g
        data["printed_measurements"]["fin-collar"] = (
            quantity(calibrated_mass, "g",
                     f"Estimated by scaling parametric CAD volume to {collar_calibration_g:g} g current collar print"),
            quantity(parametric.Center().z + reference_cg_offset_mm, "mm",
                     "Parametric CAD CG plus current collar STEP-to-parametric CG offset; hypothetical variant"),
        )
        data["name"] += "-calibrated"
    return Config.model_validate(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--body", type=float, nargs="+", default=[500, 530, 560])
    parser.add_argument("--nose", type=float, nargs="+", default=[40, 50])
    parser.add_argument("--span", type=float, nargs="+", default=[50, 55, 65])
    parser.add_argument("--candidate", type=float, nargs=3, action="append", metavar=("BODY", "NOSE", "SPAN"),
                        help="Screen only this body/nose/span tuple; may be repeated")
    parser.add_argument("--upper", action="store_true")
    parser.add_argument("--chute-cd", type=float, default=0.53)
    parser.add_argument("--measured-fin-collar-g", type=float,
                        help="Raw integrated collar print mass before cleanup or finishing; requires --integrated-collar")
    parser.add_argument("--collar-calibration-g", type=float,
                        help="Scale nominal parametric collar volumes to this raw current-collar mass at 53.65 mm span")
    parser.add_argument("--finish-allowance-g", type=float, default=0.0,
                        help="Additional provisional primer/paint mass on a measured collar")
    parser.add_argument("--integrated-collar", action="store_true",
                        help="Use the existing Integrated collar STEP mass and CG at its original station")
    args = parser.parse_args()
    if args.measured_fin_collar_g is not None and not args.integrated_collar:
        parser.error("--measured-fin-collar-g requires --integrated-collar")
    if args.finish_allowance_g < 0 or (args.finish_allowance_g and args.measured_fin_collar_g is None):
        parser.error("--finish-allowance-g requires a measured collar mass and a nonnegative allowance")
    if args.collar_calibration_g is not None and (args.collar_calibration_g <= 0 or args.upper or args.integrated_collar):
        parser.error("--collar-calibration-g requires positive mass, nominal case, and no --integrated-collar")
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    geometry_cases = args.candidate or list(itertools.product(args.body, args.nose, args.span))
    designs = [(body, nose, span, motor) for body, nose, span in geometry_cases for motor in ("D12", "E12")]
    save_json(out / "search-spec.json", dict(
        bodies_mm=args.body, noses_mm=args.nose, fin_spans_mm=args.span,
        selected_geometry_cases=geometry_cases,
        motors=["D12-5", "E12-6"], winds_m_s=[0, 2, 4],
        upper_mass=args.upper, chute_cd=args.chute_cd,
        integrated_collar_mass_override=args.integrated_collar,
        measured_fin_collar_g=args.measured_fin_collar_g,
        collar_calibration_g=args.collar_calibration_g,
        finish_allowance_g=args.finish_allowance_g,
        airframe_joint_allowance_g=6.0 if args.upper else 3.0,
        expected_configurations=len(designs), expected_flights=len(designs) * 9,
        limitations="Parametric collar and unmeasured splice/mount/recovery estimates; no flight clearance",
    ))
    rows = []
    with Engine() as engine:
        for body, nose, span, motor in designs:
            config = configuration(body, nose, span, motor, upper=args.upper, chute_cd=args.chute_cd,
                                   integrated_collar=args.integrated_collar,
                                   fin_collar_mass_g=args.measured_fin_collar_g,
                                   finish_allowance_g=args.finish_allowance_g,
                                   collar_calibration_g=args.collar_calibration_g)
            folder = out / config.name
            folder.mkdir()
            path = folder / "config.yaml"
            save_json(path, config.model_dump())
            digest = hashlib.sha256(json.dumps(config.model_dump(), sort_keys=True).encode()).hexdigest()
            save_json(folder / "manifest.json", dict(configuration_sha256=digest, command="study-de-geometry"))
            workflow(Namespace(command="simulate", strict=False), config, path, folder, digest, engine)
            for case in json.loads((folder / "results.json").read_text())["cases"]:
                if case["loading"] != "actual":
                    continue
                metrics = case.get("metrics", {})
                rows.append(dict(
                    design=config.name, body_mm=body, nose_mm=nose, span_mm=span,
                    motor=f"{motor}-{config.motors[0].delay_s:g}", wind_m_s=case["wind_m_s"],
                    evaluation=case["evaluation"]["criteria_status"],
                    launch_mass_g=case.get("mass", {}).get("launch_mass_g"),
                    apogee_m=metrics.get("apogee_m"),
                    guide_m_s=metrics.get("guide_departure_m_s"),
                    stability_cal=metrics.get("minimum_ascent_stability_cal"),
                    deployment_m_s=metrics.get("deployment_speed_m_s"),
                    descent_m_s=metrics.get("landing_descent_m_s"),
                    drift_m=metrics.get("landing_displacement_m"),
                ))
            save_json(out / "comparison.json", rows)
            print("DESIGN COMPLETE", config.name, flush=True)
    seal_run(out)
    print("D/E GEOMETRY SCREEN COMPLETE", out, flush=True)


if __name__ == "__main__":
    main()
