"""Generate the selected D12 organic fin-collar CAD and review render."""

import argparse
import json
import sys
from pathlib import Path

import vtk

from rocket_workbench.cad import build, shapes
from rocket_workbench.cli import save_json
from rocket_workbench.config import Config

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_avionics import actor, label  # noqa: E402
from study_sourced_chute import configuration  # noqa: E402


def organic_config() -> Config:
    data = configuration(False, 0.53, insert_trial=True).model_dump()
    data["name"] = "d12-conical-n50-b500-organic-fin-v2"
    data["fin_profile"] = "organic-v2"
    data["geometry"]["fin_thickness"].update(
        value=2.0,
        provenance="estimate",
        source=(
            "Organic fin release v2: five nominal 0.4 mm extrusion widths; "
            "verify sliced walls and physical strength"
        ),
    )
    return Config.model_validate(data)


def render(config: Config, destination: Path) -> None:
    part = shapes(config)["fin-collar"]
    center = part.val().Center()
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(1)
    window.SetSize(1800, 1200)
    window.SetMultiSamples(8)

    views = (
        ((0.0, 0.0, 0.68, 1.0), (175, -225, 625), 92, f"FIN COLLAR {config.fin_profile.upper()}"),
        ((0.68, 0.0, 1.0, 1.0), (115, -85, 530), 37, "ROOT BLEND"),
    )
    for viewport, camera_position, scale, title in views:
        renderer = vtk.vtkRenderer()
        renderer.SetViewport(*viewport)
        renderer.SetBackground(0.965, 0.972, 0.982)
        renderer.SetBackground2(0.80, 0.85, 0.91)
        renderer.GradientBackgroundOn()
        renderer.AddActor(actor(part, (0.08, 0.43, 0.72)))
        camera = renderer.GetActiveCamera()
        camera.SetPosition(*camera_position)
        camera.SetFocalPoint(center.x, center.y, center.z)
        camera.SetViewUp(0, 0, 1)
        camera.ParallelProjectionOn()
        camera.SetParallelScale(scale)
        renderer.ResetCameraClippingRange()
        label(renderer, title, 34, 1138, 27 if viewport[0] == 0 else 22)
        window.AddRenderer(renderer)

    first = window.GetRenderers().GetFirstRenderer()
    root_label = ("uniform 1.7 mm root cove" if config.fin_profile == 'organic-v5'
                  else "flowing 1-3-1 mm root cove")
    label(first, f"2.0 mm clipped-delta fins / {root_label}", 34, 52, 22)
    if config.fin_profile == 'organic-v5':
        detail = "4 mm outer leading bevel / uniform 1.7 mm root cove / 2 mm trailing edge"
    elif config.fin_profile == 'organic-v4':
        detail = "4 mm leading bevel / 8 mm radial taper / 0.7 mm trailing edge"
    elif config.fin_profile == 'organic-v3':
        detail = "8 mm radial tip taper / 0.8 mm land / 0.7 mm trailing edge"
    else:
        detail = "rounded leading + tip edges / 0.7 mm tapered trailing edge"
    label(first, detail, 34, 22, 19)
    label(first, "CAD REVIEW - NOT PHYSICAL STRENGTH VALIDATION", 1185, 22, 17)
    window.Render()
    capture = vtk.vtkWindowToImageFilter()
    capture.SetInput(window)
    capture.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(destination))
    writer.SetInputConnection(capture.GetOutputPort())
    writer.Write()
    window.Finalize()

    if not destination.is_file() or destination.stat().st_size == 0:
        raise RuntimeError(f"Render was not written: {destination}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)

    config = organic_config()
    save_json(args.output / "config.json", config.model_dump())
    cad = args.output / "cad"
    records = build(config, cad)
    render(config, args.output / "fin-collar-review.png")
    save_json(
        args.output / "design-summary.json",
        {
            "part": "fin-collar",
            "profile": config.fin_profile,
            "fin_thickness_mm": config.geometry.mm("fin_thickness"),
            "root_cove_radius_mm": {"ends": 0.8, "maximum": 3.0},
            "root_cove_hidden_overlap_mm": 0.2,
            "trailing_edge_mm": 0.7,
            "mass_g_solid_density_estimate": records["fin-collar"]["mass_g"],
            "limitations": [
                "No mechanical coupon or destructive test completed",
                "Slicer and measured print mass remain required",
                "Root-fairing aerodynamics are not validated CFD evidence",
            ],
        },
    )
    print(json.dumps({"output": str(args.output), "fin_collar": records["fin-collar"]}, indent=2))


if __name__ == "__main__":
    main()
