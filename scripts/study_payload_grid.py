"""Fast, reproducible actual-logger screen across the passive BT-60 design grid.

This is a coarse screen, not the nine-case validation workflow. It excludes a
motor before flight simulation when its manufacturer liftoff-mass limit is
exceeded. Full empty/dummy/logger and uncertainty runs belong on finalists.
"""

import argparse
import itertools
import tempfile
from pathlib import Path

from rocket_workbench.cad import shapes
from rocket_workbench.cli import save_json
from rocket_workbench.config import Config
from rocket_workbench.flight_model import generate
from rocket_workbench.simulator import Engine
from study_de_geometry import configuration


def mass_records(config: Config) -> dict:
    """Calculate flight-model part masses without exporting review CAD."""
    records = {}
    for name, part in shapes(config).items():
        shape = part.val()
        if not shape.isValid() or len(part.solids().vals()) != 1 or shape.Volume() <= 0:
            raise ValueError(f"Invalid or disconnected CAD solid: {name}")
        record = dict(mass_g=shape.Volume() / 1000 * config.density.value,
                      cg_x_mm=shape.Center().z)
        if name in config.printed_measurements:
            mass, cg = config.printed_measurements[name]
            record.update(mass_g=mass.value, cg_x_mm=cg.value)
        records[name] = record
    return records


def candidate(body: float, nose: float, span: float, shape: str, motor: str,
              fin_root: float = 65,
              *, upper: bool = False, finish_allowance_g: float = 3,
              fin_count: int = 3) -> Config:
    if upper:
        if abs(span - 53.65384615384615) > 1e-3:
            raise ValueError("Upper weighed-collar screen requires the printed collar's original span")
        if fin_root != 65:
            raise ValueError("Upper weighed-collar screen requires the printed collar's original root chord")
        config = configuration(body, nose, span, motor, upper=True, integrated_collar=True,
                               fin_collar_mass_g=27, finish_allowance_g=finish_allowance_g,
                               fin_count=fin_count)
    else:
        config = configuration(body, nose, span, motor, collar_calibration_g=27,
                               fin_root_mm=fin_root if fin_root != 65 else None,
                               fin_count=fin_count)
    data = config.model_dump()
    data["nose_shape"] = shape
    if shape != "conical":
        data["geometry"]["nose_tip_radius"] = None
    data["name"] += f"-{shape}"
    if fin_count != 3:
        data["name"] += f"-{fin_count}fins"
    return Config.model_validate(data)


def screen(config: Config, engine: Engine, winds: list[float], temporary: Path) -> list[dict]:
    model = temporary / f"{config.name}.ork"
    expected = generate(config, mass_records(config), "actual", model)
    rows = []
    for wind in winds:
        doc, warnings = engine.load(model)
        if warnings:
            raise ValueError(f"OpenRocket model warnings: {warnings}")
        sim = engine.new_simulation(doc)
        motor = config.motors[0]
        engine.motor(sim, motor, config)
        engine.configure(sim, config, wind)
        mass = engine.mass(sim)
        row = dict(design=config.name, body_mm=config.geometry.mm("body_length"),
                   nose_mm=config.geometry.mm("nose_length"), nose_shape=config.nose_shape,
                   span_mm=config.geometry.mm("fin_span"), motor=f"{motor.designation}-{motor.delay_s:g}",
                   fin_root_mm=config.geometry.mm("fin_root"),
                   effective_tip_chord_mm=0.2 * config.geometry.mm("fin_root"),
                   wind_m_s=wind, launch_mass_g=mass["launch_mass_g"],
                   dry_mass_g=expected["dry_mass_g"], loaded_cg_mm=mass["launch_cg_x_mm"],
                   motor_liftoff_limit_g=motor.max_liftoff_mass.value)
        if mass["launch_mass_g"] > motor.max_liftoff_mass.value:
            row.update(status="excluded: manufacturer liftoff-mass limit")
            rows.append(row)
            continue
        result = engine.run(sim)
        metrics = result.get("metrics", {})
        row.update(status=result.get("execution", "unknown"),
                   apogee_m=metrics.get("apogee_m"),
                   guide_m_s=metrics.get("guide_departure_m_s"),
                   stability_cal=metrics.get("minimum_ascent_stability_cal"),
                   deployment_m_s=metrics.get("deployment_speed_m_s"),
                   descent_m_s=metrics.get("landing_descent_m_s"),
                   drift_m=metrics.get("landing_displacement_m"),
                   warnings=result.get("warnings", []))
        rows.append(row)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--body", type=float, nargs="+", default=[500, 530, 560])
    parser.add_argument("--nose", type=float, nargs="+", default=[40, 50, 60, 70])
    parser.add_argument("--span", type=float, nargs="+", default=[45, 50, 53.65384615384615, 55, 65])
    parser.add_argument("--fin-root", type=float, nargs="+", default=[65])
    parser.add_argument("--nose-shape", nargs="+", choices=("conical", "ogive", "ellipsoid"),
                        default=["conical", "ogive", "ellipsoid"])
    parser.add_argument("--motor", nargs="+", choices=("C11", "D12", "E12"),
                        default=["C11", "D12", "E12"])
    parser.add_argument("--wind", type=float, nargs="+", default=[0, 4])
    parser.add_argument("--upper", action="store_true", help="Upper other masses with weighed current collar")
    parser.add_argument("--finish-allowance-g", type=float, default=3,
                        help="Provisional collar finish mass for --upper (default 3 g)")
    args = parser.parse_args()
    if args.upper and any(abs(span - 53.65384615384615) > 1e-3 for span in args.span):
        parser.error("--upper only supports the printed collar's 53.65 mm span")
    if args.upper and args.fin_root != [65]:
        parser.error("--upper only supports the printed collar's original 65 mm root chord")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    axes = list(itertools.product(args.body, args.nose, args.span, args.nose_shape,
                                  args.fin_root, args.motor))
    save_json(output / "search-spec.json", dict(body_mm=args.body, nose_mm=args.nose,
              span_mm=args.span, nose_shapes=args.nose_shape, fin_roots_mm=args.fin_root,
              clipped_delta_tip_chord="20% of root; generic fin_tip field is inactive",
              motor_families=args.motor,
              primary_delays=dict(C11=3, D12=5, E12=6), winds_m_s=args.wind,
              configurations=len(axes), loading="actual only", collar_calibration_raw_g=27,
              upper_other_masses=args.upper, finish_allowance_g=args.finish_allowance_g if args.upper else 0,
              active_control="not modeled: hardware mass and location unknown",
              limits="Coarse nominal screen; full wind/loading/upper-mass validation required"))
    rows = []
    with tempfile.TemporaryDirectory(prefix="rocket-payload-grid-") as temp, Engine() as engine:
        temporary = Path(temp)
        for index, (body, nose, span, shape, fin_root, motor) in enumerate(axes, 1):
            try:
                config = candidate(body, nose, span, shape, motor, fin_root, upper=args.upper,
                                   finish_allowance_g=args.finish_allowance_g)
                rows.extend(screen(config, engine, args.wind, temporary))
            except (ValueError, RuntimeError) as exc:
                rows.append(dict(body_mm=body, nose_mm=nose, span_mm=span, nose_shape=shape,
                                 fin_root_mm=fin_root,
                                 motor=motor, status="excluded: invalid configuration",
                                 reason=str(exc)))
            if index % 10 == 0 or index == len(axes):
                save_json(output / "comparison.json", rows)
                print(f"screened {index}/{len(axes)} configurations", flush=True)
    save_json(output / "comparison.json", rows)


if __name__ == "__main__":
    main()
