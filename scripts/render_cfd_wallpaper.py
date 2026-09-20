"""Render a bright, rocket-led ultrawide view from retained OpenFOAM fields."""

import argparse
import math
from pathlib import Path

import vtk


def seed_rings(
    x: float,
    radii: tuple[float, ...],
    count: int,
) -> vtk.vtkPolyData:
    """Place a deterministic, surface-focused family of ring seeds."""
    points = vtk.vtkPoints()
    vertices = vtk.vtkCellArray()
    remaining = max(count, 4 * len(radii))
    for ring_index, radius in enumerate(radii):
        if ring_index == len(radii) - 1:
            ring_count = remaining
        else:
            ring_count = max(4, round(count / len(radii)))
            remaining -= ring_count
        offset = ring_index * math.pi / 17.0
        for index in range(ring_count):
            angle = 2.0 * math.pi * index / ring_count + offset
            point_id = points.InsertNextPoint(
                x,
                radius * math.cos(angle),
                radius * math.sin(angle),
            )
            vertices.InsertNextCell(1)
            vertices.InsertCellPoint(point_id)

    result = vtk.vtkPolyData()
    result.SetPoints(points)
    result.SetVerts(vertices)
    return result


def speed_lut() -> vtk.vtkColorTransferFunction:
    lut = vtk.vtkColorTransferFunction()
    lut.SetColorSpaceToRGB()
    lut.AddRGBPoint(0.0, 0.38, 0.02, 0.62)
    lut.AddRGBPoint(18.0, 0.18, 0.06, 0.82)
    lut.AddRGBPoint(32.0, 0.00, 0.30, 0.95)
    lut.AddRGBPoint(39.0, 0.00, 0.82, 1.00)
    lut.AddRGBPoint(42.0, 0.42, 0.98, 1.00)
    lut.AddRGBPoint(48.0, 1.00, 0.80, 0.18)
    lut.AddRGBPoint(55.0, 1.00, 0.98, 0.82)
    return lut


def pressure_lut() -> vtk.vtkColorTransferFunction:
    """Mostly white pressure tint: cool suction, warm stagnation."""
    lut = vtk.vtkColorTransferFunction()
    lut.SetColorSpaceToRGB()
    lut.AddRGBPoint(-1200.0, 0.46, 0.72, 0.96)
    lut.AddRGBPoint(-500.0, 0.77, 0.90, 1.00)
    lut.AddRGBPoint(-100.0, 0.94, 0.98, 1.00)
    lut.AddRGBPoint(100.0, 1.00, 1.00, 0.98)
    lut.AddRGBPoint(350.0, 1.00, 0.92, 0.69)
    lut.AddRGBPoint(550.0, 1.00, 0.76, 0.28)
    return lut


def traced_speed(
    volume,
    seeds: vtk.vtkPolyData,
    *,
    both_directions: bool = False,
) -> vtk.vtkArrayCalculator:
    stream = vtk.vtkStreamTracer()
    stream.SetInputData(volume)
    stream.SetSourceData(seeds)
    stream.SetInputArrayToProcess(
        0,
        0,
        0,
        vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS,
        "U",
    )
    if both_directions:
        stream.SetIntegrationDirectionToBoth()
    else:
        stream.SetIntegrationDirectionToForward()
    stream.SetIntegratorTypeToRungeKutta45()
    stream.SetInterpolatorTypeToCellLocator()
    stream.SetIntegrationStepUnit(vtk.vtkStreamTracer.LENGTH_UNIT)
    stream.SetMaximumPropagation(3.0)
    stream.SetInitialIntegrationStep(0.0012)
    stream.SetMinimumIntegrationStep(0.00008)
    stream.SetMaximumIntegrationStep(0.004)
    stream.SetMaximumNumberOfSteps(40000)
    stream.SetMaximumError(1e-7)
    stream.SetTerminalSpeed(0.02)
    stream.SetComputeVorticity(True)

    speed = vtk.vtkArrayCalculator()
    speed.SetInputConnection(stream.GetOutputPort())
    speed.SetAttributeTypeToPointData()
    speed.AddVectorArrayName("U")
    speed.SetFunction("mag(U)")
    speed.SetResultArrayName("speed")
    return speed


def streamline_actor(source, radius: float) -> vtk.vtkActor:
    tube = vtk.vtkTubeFilter()
    tube.SetInputConnection(source.GetOutputPort())
    tube.SetRadius(radius)
    tube.SetNumberOfSides(10)
    tube.CappingOff()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(tube.GetOutputPort())
    mapper.SetScalarModeToUsePointFieldData()
    mapper.SelectColorArray("speed")
    mapper.SetLookupTable(speed_lut())
    mapper.SetScalarRange(0.0, 55.0)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetOpacity(1.0)
    actor.GetProperty().SetAmbient(1.0)
    actor.GetProperty().SetDiffuse(0.0)
    actor.GetProperty().SetSpecular(0.0)
    return actor


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--foam", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--width", type=int, default=2560)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--seeds", type=int, default=220)
    parser.add_argument("--time", type=float, default=600.0)
    parser.add_argument("--length", type=float, help="Actual nose-to-tail length in metres for matched framing")
    parser.add_argument("--multisamples", type=int, default=0,
                        help="MSAA samples; zero avoids black frames on headless EGL")
    parser.add_argument("--caption", help="Optional provenance/caveat text burned into the image")
    parser.add_argument("--no-lic", action="store_true", help="Use pressure surface without optional wall-shear texture")
    parser.add_argument("--stream-radius-scale", type=float, default=1., help="Visualization-only streamline tube thickness")
    args = parser.parse_args()

    reader = vtk.vtkOpenFOAMReader()
    reader.SetFileName(str(args.foam))
    reader.UpdateInformation()
    times = reader.GetTimeValues()
    if times is None or not any(abs(times.GetValue(i) - args.time) < 1e-9 for i in range(times.GetNumberOfValues())):
        raise ValueError(f'Requested solved field time {args.time:g} is not available; refusing nearest-time substitution')
    reader.SetPatchArrayStatus("patch/rocket", 1)
    reader.SetTimeValue(args.time)
    reader.EnableAllCellArrays()
    reader.Update()

    output = reader.GetOutput()
    volume = output.GetBlock(0)
    rocket = output.GetBlock(1).GetBlock(0)
    # Linear tetrahedral interpolation avoids spurious velocity overshoots in
    # VTK's native polyhedral stream-tracing weights near the fin wake.
    triangles = vtk.vtkDataSetTriangleFilter()
    triangles.SetInputData(volume)
    triangles.TetrahedraOnlyOn()
    triangles.Update()
    volume = triangles.GetOutput()

    nose_speed = traced_speed(
        volume,
        seed_rings(
            -0.30,
            (0.025, 0.031, 0.039, 0.049, 0.061, 0.075),
            max(24, args.seeds // 4),
        ),
    )
    wake_speed = traced_speed(
        volume,
        seed_rings(
            args.length + 0.04 if args.length else 0.49,
            (0.006, 0.012, 0.020, 0.030, 0.045, 0.065, 0.085) if args.length else
            (0.024, 0.030, 0.037, 0.045, 0.054, 0.064, 0.075, 0.088),
            args.seeds,
        ),
        both_directions=True,
    )
    source_max = volume.GetPointData().GetArray('U').GetRange(-1)[1]
    for traces in (nose_speed, wake_speed):
        traces.Update()
        speed_array = traces.GetOutput().GetPointData().GetArray('speed')
        if speed_array is None or speed_array.GetRange()[1] > source_max * 1.00001:
            raise ValueError('Trace velocity exceeds source point-field bound; refusing misleading render')

    renderer = vtk.vtkRenderer()
    renderer.GradientBackgroundOn()
    renderer.SetBackground(0.0, 0.0, 0.0)
    renderer.SetBackground2(0.003, 0.006, 0.016)
    renderer.SetUseDepthPeeling(False)
    renderer.SetUseFXAA(True)

    camera = renderer.GetActiveCamera()
    camera.SetPosition(0.02, 1.08, 0.50)
    camera.SetFocalPoint(0.31, 0.0, -0.002)
    camera.SetViewUp(0.0, 0.0, 1.0)
    camera.ParallelProjectionOn()
    camera.SetParallelScale(0.090)
    camera.Roll(10.0)
    if args.length:
        camera.SetFocalPoint(args.length / 2 + .05, 0.0, 0.0)
        camera.SetParallelScale(max(.12, args.length / (args.width / args.height) * .76))

    rocket_mapper = vtk.vtkSurfaceLICMapper()
    rocket_mapper.SetInputData(rocket)
    rocket_mapper.SetScalarModeToUsePointFieldData()
    rocket_mapper.SelectColorArray("p")
    rocket_mapper.SetLookupTable(pressure_lut())
    rocket_mapper.SetScalarRange(-1200.0, 550.0)
    rocket_mapper.SetInputArrayToProcess(
        0,
        0,
        0,
        vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS,
        "wallShearStress",
    )

    lic = rocket_mapper.GetLICInterface()
    if args.no_lic:
        lic.EnableOff()
    else:
        if rocket.GetPointData().GetArray('wallShearStress') is None:
            raise ValueError('wallShearStress is absent; use --no-lic for an honest pressure/velocity view')
        lic.EnableOn()
    lic.SetNormalizeVectors(True)
    lic.SetNumberOfSteps(42)
    lic.SetStepSize(0.38)
    lic.SetLICIntensity(0.34)
    lic.SetNoiseGeneratorSeed(9)
    lic.SetNoiseTextureSize(min(4096, max(512, args.width // 2)))
    lic.SetNoiseGrainSize(2)
    lic.SetEnhanceContrast(lic.ENHANCE_CONTRAST_LIC)
    lic.SetColorMode(lic.COLOR_MODE_BLEND)

    rocket_actor = vtk.vtkActor()
    rocket_actor.SetMapper(rocket_mapper)
    rocket_property = rocket_actor.GetProperty()
    rocket_property.SetColor(1.0, 1.0, 1.0)
    rocket_property.SetInterpolationToPhong()
    rocket_property.SetAmbient(0.38)
    rocket_property.SetDiffuse(0.36)
    rocket_property.SetSpecular(0.55)
    rocket_property.SetSpecularPower(80)
    renderer.AddActor(rocket_actor)

    silhouette = vtk.vtkPolyDataSilhouette()
    silhouette.SetInputData(rocket)
    silhouette.SetCamera(camera)
    silhouette.SetEnableFeatureAngle(0)
    silhouette_mapper = vtk.vtkPolyDataMapper()
    silhouette_mapper.SetInputConnection(silhouette.GetOutputPort())
    silhouette_actor = vtk.vtkActor()
    silhouette_actor.SetMapper(silhouette_mapper)
    silhouette_actor.GetProperty().SetColor(0.65, 0.92, 1.0)
    silhouette_actor.GetProperty().SetOpacity(0.58)
    silhouette_actor.GetProperty().SetLineWidth(max(1.2, args.width / 3200.0))
    renderer.AddActor(silhouette_actor)

    renderer.AddActor(streamline_actor(nose_speed, 0.000085 * args.stream_radius_scale))
    renderer.AddActor(streamline_actor(wake_speed, 0.00015 * args.stream_radius_scale))

    key = vtk.vtkLight()
    key.SetPosition(-0.10, 0.55, 0.48)
    key.SetFocalPoint(0.25, 0.0, 0.0)
    key.SetColor(0.82, 0.95, 1.0)
    key.SetIntensity(1.55)
    renderer.AddLight(key)

    rim = vtk.vtkLight()
    rim.SetPosition(0.52, -0.38, 0.22)
    rim.SetFocalPoint(0.30, 0.0, 0.0)
    rim.SetColor(0.15, 0.55, 1.0)
    rim.SetIntensity(0.85)
    renderer.AddLight(rim)
    if args.caption:
        title = vtk.vtkTextActor()
        title.SetInput(args.caption)
        title.SetPosition(30, 25)
        title.GetTextProperty().SetFontSize(max(18, args.width // 125))
        title.GetTextProperty().SetColor(.75, .84, .93)
        title.GetTextProperty().SetBackgroundColor(0., 0., 0.)
        title.GetTextProperty().SetBackgroundOpacity(.8)
        renderer.AddViewProp(title)
        legend = vtk.vtkScalarBarActor()
        legend.SetLookupTable(speed_lut())
        legend.SetTitle('Streamline speed (m/s)')
        legend.SetOrientationToHorizontal()
        legend.SetPosition(.73, .86)
        legend.SetWidth(.23)
        legend.SetHeight(.10)
        legend.SetNumberOfLabels(4)
        legend.SetLabelFormat('%.0f')
        legend.GetTitleTextProperty().SetColor(.82, .9, 1.)
        legend.GetLabelTextProperty().SetColor(.82, .9, 1.)
        legend.GetTitleTextProperty().SetFontFamilyToArial()
        legend.GetLabelTextProperty().SetFontFamilyToArial()
        legend.GetTitleTextProperty().ItalicOff()
        legend.GetLabelTextProperty().ItalicOff()
        legend.DrawBackgroundOn()
        legend.GetBackgroundProperty().SetColor(.005, .01, .02)
        legend.GetBackgroundProperty().SetOpacity(.9)
        renderer.AddViewProp(legend)

    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(1)
    window.SetAlphaBitPlanes(1)
    window.SetMultiSamples(args.multisamples)
    window.SetSize(args.width, args.height)
    window.AddRenderer(renderer)
    window.Render()

    capture = vtk.vtkWindowToImageFilter()
    capture.SetInput(window)
    capture.SetInputBufferTypeToRGB()
    capture.ReadFrontBufferOff()
    capture.Update()
    if max(capture.GetOutput().GetPointData().GetScalars().GetRange(i)[1] for i in range(3)) < 2:
        raise RuntimeError("Renderer produced a black frame; check EGL and --multisamples 0")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(args.output))
    writer.SetInputConnection(capture.GetOutputPort())
    writer.Write()

    nose_speed.Update()
    wake_speed.Update()
    print(
        "nose_streamlines",
        nose_speed.GetOutput().GetNumberOfCells(),
        "wake_streamlines",
        wake_speed.GetOutput().GetNumberOfCells(),
        "wake_speed_range",
        wake_speed.GetOutput().GetPointData().GetArray("speed").GetRange(),
    )
    print(args.output)


if __name__ == "__main__":
    main()
