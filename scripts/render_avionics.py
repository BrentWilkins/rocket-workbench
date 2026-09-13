"""Render actual nominal CAD, with visual-only cutaway/explosion transforms."""
import argparse
from pathlib import Path

import cadquery as cq
import vtk

from rocket_workbench.avionics import detail_models, stack_pins
from rocket_workbench.cad import preview, shapes
from rocket_workbench.config import load_config


def actor(shape, color, offset=(0, 0, 0)):
    if isinstance(shape, cq.Workplane):
        shape = shape.val()
    vertices, triangles = shape.tessellate(.08, .15)
    points = vtk.vtkPoints()
    for v in vertices:
        points.InsertNextPoint(v.x, v.y, v.z)
    cells = vtk.vtkCellArray()
    for triangle in triangles:
        cells.InsertNextCell(3)
        for i in triangle:
            cells.InsertCellPoint(i)
    data = vtk.vtkPolyData()
    data.SetPoints(points)
    data.SetPolys(cells)
    normals = vtk.vtkPolyDataNormals()
    normals.SetInputData(data)
    normals.SetFeatureAngle(35)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(normals.GetOutputPort())
    result = vtk.vtkActor()
    result.SetMapper(mapper)
    result.SetPosition(*offset)
    result.GetProperty().SetColor(*color[:3])
    result.GetProperty().SetSpecular(.22)
    result.GetProperty().SetSpecularPower(35)
    return result


def label(renderer, text, x, y, size=24):
    a = vtk.vtkTextActor()
    a.SetInput(text)
    a.SetPosition(x, y)
    p = a.GetTextProperty()
    p.SetFontSize(size)
    p.SetColor(.10, .16, .23)
    renderer.AddViewProp(a)


def render(config, destination, exploded=False):
    parts = shapes(config)
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(.95, .96, .98)
    shell = parts['nose-bay']
    # Remove the camera-facing half for visibility only; exported CAD is intact.
    cutter = cq.Workplane('XY').box(150, 100, 500).translate((0, 50, 150))
    shell = shell.cut(cutter)
    renderer.AddActor(actor(shell, (.68, .76, .83), (-48, 0, 0) if exploded else (0, 0, 0)))
    renderer.AddActor(actor(parts['payload-sled'], (.90, .48, .12)))
    renderer.AddActor(actor(parts['bay-bulkhead'], (.68, .76, .83), (0, 0, 25) if exploded else (0, 0, 0)))
    offsets = {'xiao-sense': (0, 25, 0), 'l76k': (0, 48, 0),
               'barometer': (0, 48, 0), 'battery': (0, 25, 0),
               'antenna': (0, 25, -10), 'battery-connector': (0, 25, 0)}
    groups = detail_models(config)
    groups['headers'] = stack_pins(config)
    for name, assembly in groups.items():
        for shape, _, location, color in assembly:
            renderer.AddActor(actor(shape.moved(location), color.toTuple(),
                                    offsets.get(name, (0, 0, 0)) if exploded else (0, 0, 0)))
    camera = renderer.GetActiveCamera()
    camera.SetPosition(220, 400, -30)
    camera.SetFocalPoint(0, 0, 105)
    camera.SetViewUp(0, 0, -1)
    camera.ParallelProjectionOn()
    renderer.ResetCamera()
    camera.SetParallelScale(160 if exploded else 145)
    label(renderer, 'AVIONICS / ' + ('EXPLODED REVIEW' if exploded else 'INSTALLED CUTAWAY'), 45, 1120, 32)
    label(renderer, 'Actual CAD geometry | nose tip above, aft bulkhead below', 45, 1080, 21)
    label(renderer, 'Gray: cutaway shell + cap     Orange: printed sled', 45, 110, 22)
    label(renderer, 'Green: XIAO / GNSS / antenna PCB     Blue: pressure board', 45, 78, 22)
    label(renderer, 'Silver: battery / shields     Ivory: antenna patch', 45, 46, 22)
    label(renderer, 'PROVISIONAL: electronics detail approximated; wiring and straps omitted. Not physical validation.', 45, 15, 18)
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(1)
    window.SetSize(1500, 1200)
    window.SetMultiSamples(8)
    window.AddRenderer(renderer)
    window.Render()
    capture = vtk.vtkWindowToImageFilter()
    capture.SetInput(window)
    capture.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(destination))
    writer.SetInputConnection(capture.GetOutputPort())
    writer.Write()
    window.Finalize()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    config = load_config(args.config)
    render(config, args.output / 'installed-cutaway.png')
    render(config, args.output / 'exploded.png', exploded=True)
    preview(config, args.output / 'assembly.svg')
    print(args.output)
