# 500 mm ogive candidate renders

Real CAD geometry: 500 mm BT-60 body, 40 mm ogive, and the authoritative integrated collar STEP translated 10 mm toward the nose from its original 550 mm datum. The red finish is an appearance choice, not a roughness model. The fin-detail image deliberately crops the forward body.

The current guide sleeves are shown, **not the proposed 3/16-inch revision**. The visible aft mount tube and centering rings are the existing CAD purchased-part envelopes; no motor or retainer is depicted. No camera aperture or pressure holes have been invented in the exterior tube. This is an exterior review of the ogive study candidate, not an updated manufacturing release of the conical baseline. See `render-manifest.json` for geometry bounds and source hash.

Studio views use procedural neutral softbox lighting and a cosmetic red clearcoat material. These highlights describe the CAD curvature, not measured paint gloss or print texture.

Reproduce from the repository root, choosing a new output directory:

```sh
VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow LIBGL_ALWAYS_SOFTWARE=1 PYTHONPATH=src:scripts .venv/bin/python scripts/render_500_candidate.py --output runs/render-500-ogive-new
```

The script also exports a separate **sealed, no-guide CFD exterior**. That geometry fills the under-collar clearance, omits apertures and the motor cavity, and is not the literal assembly shown in the beauty renders. Streamline images must use fields solved on their stated CFD geometry; they are not evidence of camera- or pressure-port performance.

## Exploratory flow view

A separate [5120 × 1440 wallpaper](500-ogive-streamlines-5120x1440.png) is rendered from the same fields and settings, using `--width 5120 --height 1440`. The original 3200 × 1100 image is preserved.

`500-ogive-streamlines.png` uses the recovered iteration-1000 velocity field at 40 m/s and 5° angle of attack. Colors on streamlines represent speed; the rocket surface has a qualitative pressure tint, not a wall-shear texture. See `cfd-audit.json` for solver limitations and `streamline-manifest.json` for field hashes, interpolation, and velocity bounds. This is not a validated aerodynamic result or a port comparison.

```sh
VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow LIBGL_ALWAYS_SOFTWARE=1 .venv/bin/python scripts/render_cfd_wallpaper.py --foam runs/cfd-500-ogive-a5-20260919-reconstructed-v1/case.foam --output runs/500-ogive-streamlines-new.png --width 3200 --height 1100 --seeds 60 --time 1000 --length .54 --multisamples 0 --no-lic --stream-radius-scale 2 --caption '500 mm / 40 mm ogive | 40 m/s, 5 deg | Exploratory field: guides and ports omitted; not validated'
```
