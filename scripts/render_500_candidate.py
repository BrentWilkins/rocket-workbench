"""Render the 500 mm / 40 mm ogive candidate from real CAD, not an illustration."""

import argparse
import hashlib
import json
import math
from pathlib import Path

import cadquery as cq
import vtk

from render_avionics import actor
from study_payload_grid import candidate
from rocket_workbench.cad import shapes


def studio_environment():
    """Procedural HDR softboxes, used only for lighting actual CAD surfaces."""
    data = vtk.vtkImageData()
    data.SetDimensions(512, 256, 1)
    data.AllocateScalars(vtk.VTK_FLOAT, 3)
    for y in range(256):
        latitude = math.pi * (y / 255 - .5)
        for x in range(512):
            longitude = 2 * math.pi * x / 511
            brightness = .17 + .11 * max(0., math.sin(latitude))
            for lon, lat, width, height, strength in [(.8, .65, .24, .7, 4.),
                                                       (3.7, .25, .18, .9, 2.6),
                                                       (5.4, -.2, .38, .35, 1.6)]:
                delta = (longitude - lon + math.pi) % (2 * math.pi) - math.pi
                brightness += strength * math.exp(-((delta / width)**4 + ((latitude - lat) / height)**4))
            for channel in range(3):
                data.SetScalarComponentFromFloat(x, y, 0, channel, brightness)
    texture = vtk.vtkTexture()
    texture.SetInputData(data)
    texture.InterpolateOn()
    texture.MipmapOn()
    return texture


def render(parts, output, *, detail=False):
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(.07, .085, .11)
    renderer.SetBackground2(.24, .27, .31)
    renderer.GradientBackgroundOn()
    renderer.SetUseFXAA(True)
    renderer.UseImageBasedLightingOn()
    renderer.SetEnvironmentTexture(studio_environment())
    for name, shape in parts.items():
        color = (.66, .025, .016) if not name.startswith('mount-') else (.24, .17, .09)
        if name == 'mount-tube-envelope':
            color = (.04, .025, .012)
        model = actor(shape, color)
        prop = model.GetProperty()
        prop.SetInterpolationToPBR()
        prop.SetMetallic(0.)
        prop.SetRoughness(.3 if not name.startswith('mount-') else .85)
        prop.SetCoatStrength(.3 if not name.startswith('mount-') else 0.)
        prop.SetCoatRoughness(.22)
        renderer.AddActor(model)
    renderer.AutomaticLightCreationOff()
    for position, intensity, color in [((300, 420, 100), 1.3, (1., .98, .95)),
                                        ((-250, -150, 240), .7, (.82, .9, 1.)),
                                        ((100, -450, 620), 1.1, (1., .98, .95))]:
        light = vtk.vtkLight()
        light.SetLightTypeToSceneLight()
        light.SetPosition(*position)
        light.SetFocalPoint(0, 0, 270)
        light.SetColor(*color)
        light.SetIntensity(intensity)
        renderer.AddLight(light)
    camera = renderer.GetActiveCamera()
    center = 481 if detail else 270
    camera.SetFocalPoint(0, 0, center)
    camera.SetPosition(430, 600, center + 350)
    camera.SetViewUp(0, 0, -1)
    camera.ParallelProjectionOn()
    camera.Roll(72 if not detail else 22)
    camera.SetParallelScale(146 if not detail else 93)
    renderer.ResetCameraClippingRange()
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(1)
    window.SetSize(3200, 1400 if not detail else 2400)
    window.SetMultiSamples(0)
    window.AddRenderer(renderer)
    window.Render()
    capture = vtk.vtkWindowToImageFilter()
    capture.SetInput(window)
    capture.ReadFrontBufferOff()
    capture.Update()
    if max(capture.GetOutput().GetPointData().GetScalars().GetRange(i)[1] for i in range(3)) < 2:
        raise RuntimeError('Headless renderer produced a black frame; check EGL and multisampling')
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(output))
    writer.SetInputConnection(capture.GetOutputPort())
    writer.Write()
    window.Finalize()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Choose a new output directory to retain earlier evidence')
    args.output.mkdir(parents=True)
    config = candidate(500, 40, 53.65384615384615, 'ogive', 'D12')
    generated = shapes(config)
    source = Path('docs/assets/integrated-fin-collar-v1/collar-fins.step')
    # Authoritative printed collar was authored at a 550 mm total airframe length.
    collar = cq.Workplane(obj=cq.importers.importStep(str(source)).solids().val()).translate((0, 0, -10))
    g = config.geometry
    tube = (cq.Workplane('XY', origin=(0, 0, 40))
            .circle(g.mm('body_od') / 2).circle(g.mm('body_id') / 2).extrude(500))
    parts = {'nose': generated['nose-bay'], 'tube': tube, 'printed-collar': collar}
    parts.update({name: part for name, part in generated.items() if name.startswith('lug-sleeve-')})
    mount_start = 540 - g.mm('motor_mount_length') - g.mm('motor_overhang')
    parts['mount-tube-envelope'] = (cq.Workplane('XY', origin=(0, 0, mount_start))
        .circle(g.mm('motor_mount_od') / 2).circle(g.mm('motor_mount_id') / 2)
        .extrude(g.mm('motor_mount_length')))
    for index, z in enumerate([mount_start + 7, 540 - g.mm('motor_overhang') - 5]):
        parts[f'mount-centering-ring-envelope-{index}'] = (cq.Workplane('XY', origin=(0, 0, z))
            .circle(g.mm('body_id') / 2).circle(g.mm('motor_mount_od') / 2).extrude(2))
    from rocket_workbench.nose import solid as nose_solid
    exterior = (nose_solid('ogive', 40, g.mm('body_od') / 2)
                .union(cq.Workplane('XY', origin=(0, 0, 40)).circle(g.mm('body_od') / 2).extrude(500))
                .union(cq.Workplane('XY', origin=(0, 0, 469)).circle(21.05).extrude(71))
                .union(collar))
    if not exterior.val().isValid() or len(exterior.solids().vals()) != 1:
        raise ValueError('Filled exterior must be one valid solid')
    cq.exporters.export(exterior, str(args.output / 'external-no-guides-mm.step'))
    records = {}
    for name, part in parts.items():
        solid = part.val()
        if not solid.isValid():
            raise ValueError(f'Invalid geometry: {name}')
        bounds = solid.BoundingBox()
        records[name] = dict(volume_mm3=solid.Volume(),
                             bounds_mm=[bounds.xmin, bounds.xmax, bounds.ymin, bounds.ymax,
                                        bounds.zmin, bounds.zmax])
        cq.exporters.export(part, str(args.output / f'{name}.stl'), tolerance=.02, angularTolerance=.08)
    render(parts, args.output / '500-ogive-hero.png')
    render(parts, args.output / '500-ogive-fin-detail.png', detail=True)
    (args.output / 'config.json').write_text(config.model_dump_json(indent=2) + '\n')
    manifest = dict(description='Geometry-faithful render of 500 mm body / 40 mm ogive candidate',
                    collar_source=str(source), collar_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                    collar_translation_mm=[0, 0, -10], parts=records,
                    cfd_exterior_note='Separate sealed external-no-guides STEP uses a 21.05 mm radius internal fill at Z469..540 mm to close the under-collar clearance; guides, apertures and motor cavity omitted.',
                    limitations=['Red finish is a visualization, not measured surface roughness.',
                                 'Guide sleeves retain existing old guide geometry, not the proposed 3/16 inch revision.',
                                 'No camera aperture has been added: camera pose, recess, and field of view remain unresolved.',
                                 'No inferred external pressure ports are drilled through the purchased tube.',
                                 'Exterior review only; visible aft mount tube/rings are purchased-part envelopes; motor, retainer and wiring are not rendered or fit-validated.',
                                 'This is the 40 mm ogive study candidate, not the 50 mm conical baseline.'])
    (args.output / 'render-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(args.output)


if __name__ == '__main__':
    main()
