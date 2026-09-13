"""Render retained STEP candidates at a shared scale; not an aerodynamic visualization."""
import argparse
from pathlib import Path

import cadquery as cq
import vtk
from render_avionics import actor, label


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Choose a new output; retain previous review renders')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(1)
    window.SetSize(1500, 650)
    candidates = [('planar-baseline', 'Planar baseline', '+0 g'),
                  ('ring-tail-5mm', '5 mm ring', '+3.55 g'),
                  ('ring-tail-10mm', '10 mm ring', '+7.10 g')]
    for index, (name, title, mass) in enumerate(candidates):
        part = cq.importers.importStep(str(args.study/name/'fin-collar.step'))
        bb = part.val().BoundingBox()
        part = part.translate((0,0,-(bb.zmin+bb.zmax)/2))
        renderer = vtk.vtkRenderer()
        renderer.SetViewport(index/3, 0, (index+1)/3, 1)
        renderer.SetBackground(.95, .96, .98)
        renderer.AddActor(actor(part, (.0, .447, .698)))
        camera = renderer.GetActiveCamera()
        camera.SetPosition(230,-330,240)
        camera.SetFocalPoint(0,0,0)
        camera.SetViewUp(0,0,1)
        camera.ParallelProjectionOn()
        camera.SetParallelScale(110)
        renderer.ResetCameraClippingRange()
        label(renderer, title, 25, 590, 27)
        label(renderer, mass+' CAD estimate', 25, 550, 22)
        label(renderer, 'Experimental geometry', 25, 40, 18)
        label(renderer, 'No aerodynamic benefit established', 25, 15, 16)
        window.AddRenderer(renderer)
    window.Render()
    capture = vtk.vtkWindowToImageFilter()
    capture.SetInput(window)
    capture.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(args.output))
    writer.SetInputConnection(capture.GetOutputPort())
    writer.Write()
    window.Finalize()


if __name__ == '__main__':
    main()
