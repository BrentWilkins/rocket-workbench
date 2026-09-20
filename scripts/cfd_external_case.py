"""Prepare an exploratory flow case from an explicitly supplied sealed STEP exterior.

This adapter reuses the bounded pilot dictionaries, not its conical CAD surface.
It does not accept CFD coefficients for flight use or claim small-port resolution.
"""

import argparse
import hashlib
import json
import re
from pathlib import Path

import cadquery as cq

from cfd_case import generate, surface_mesh
from rocket_workbench.cli import save_json
from rocket_workbench.config import Config, load_config


def prepare(config, external_step, output, *, cell_mm=15, speed=40, alpha=5,
            iterations=1000, reference_x_mm=300):
    if not 15 <= cell_mm <= 50 or not 10 <= speed <= 70 or not 0 <= alpha <= 10:
        raise ValueError("Pilot mesh/flow bounds exceeded")
    if not 50 <= iterations <= 3000:
        raise ValueError("Pilot iteration bounds exceeded")
    exterior = cq.importers.importStep(str(external_step))
    solid = exterior.val()
    if not solid.isValid() or len(exterior.solids().vals()) != 1:
        raise ValueError("Supplied exterior must be one closed valid solid")
    box = solid.BoundingBox()
    length = config.geometry.mm("nose_length") + config.geometry.mm("body_length")
    if abs(box.zmin) > .05 or abs(box.zmax - length) > .05:
        raise ValueError("STEP must use millimetres, +Z from nose tip at zero to tail")
    # Only the template dictionaries survive; archive the actual source below.
    template = config.model_dump()
    template["nose_shape"] = "conical"
    generate(Config.model_validate(template), output, cell_mm, speed, alpha, iterations)
    # Withhold the runnable manifest while replacing geometry. A failed closure
    # check must not leave a runnable cone manifest beside a different STEP.
    template_spec = output / "template-case-spec.json"
    (output / "case-spec.json").rename(template_spec)
    (output / "external-mm.step").write_bytes(external_step.read_bytes())
    mesh = surface_mesh(solid.rotate((0, 0, 0), (0, 1, 0), 90).scale(.001),
                        output / "constant/triSurface/rocket.stl")
    save_json(output / "resolved-inputs.json", config.model_dump())
    spec = json.loads(template_spec.read_text())
    spec.pop("ring_tail", None)
    spec.update(
        design=config.name,
        geometry_variant="supplied-sealed-exterior",
        moment_origin_m=[reference_x_mm / 1000, 0, 0],
        moment_reference="Fixed geometric reference, not asserted assembled CG",
        source_step=str(external_step.resolve()),
        source_step_sha256=hashlib.sha256(external_step.read_bytes()).hexdigest(),
        external_adapter_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        mesh={**mesh, "surface_refinement_level": 4,
              "nominal_surface_cell_mm": cell_mm / 16},
        limitations=[
            "Exploratory steady incompressible fully turbulent SST visualization only",
            "External-body benchmark acceptance failed; not validated flight coefficients",
            "No inflation layers, mesh independence or near-wall adequacy established",
            "Sealed smooth exterior; camera aperture, pressure ports, guides, plume and roughness omitted",
            "No port/cavity pressure or drag-delta conclusion supported",
        ],
        accepted_for_design=False,
    )
    control = output / "system/controlDict"
    control.write_text(re.sub(r"CofR \([^)]*\)",
                              f"CofR ({reference_x_mm / 1000} 0 0)", control.read_text()))
    save_json(output / "case-spec.json", spec)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--external-step", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--cell-mm", type=float, default=15)
    parser.add_argument("--speed", type=float, default=40)
    parser.add_argument("--alpha", type=float, default=5)
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--reference-x-mm", type=float, default=300)
    args = parser.parse_args()
    prepare(load_config(args.config), args.external_step, args.output,
            cell_mm=args.cell_mm, speed=args.speed, alpha=args.alpha,
            iterations=args.iterations, reference_x_mm=args.reference_x_mm)


if __name__ == "__main__":
    main()
