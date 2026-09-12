# Print-orientation analysis

The workbench now compares six fixed orientations for each of the six printed parts. This screen exposed two incorrect
export orientations: the fin collar rested on its tapered forward edge, and the sled rested on its small foot. Current
exports turn the collar aft-down and place the sled's broad back against the plate.

## What is measured

- **First-layer average material area:** exact CAD volume inside a 0.2 mm slab divided by 0.2 mm. This is not a measured
  adhesive contact area; it excludes brim and supports and averages over the first-layer thickness.
- **Downward-facing surface area:** tessellated surfaces above the first layer whose normals indicate overhangs beyond
  45 degrees from vertical. This does not resolve bridging, support access, or required support volume.
- Build height and XY envelope, with a conservative 236 mm-square footprint screen for the 256 mm X1C bed.
- Geometric Pareto membership: more initial contact, less height, and less downward area. No arbitrary weighted score or
  automatic strength ranking. Final plate placement/exclusions remain the slicer's responsibility.

[All 36 geometric comparisons](../runs/orientation-20260912T230119Z/report.md)

| Part / orientation              | First-layer area mm² | Downward area mm² | Height mm |
| ------------------------------- | -------------------: | ----------------: | --------: |
| Fin collar: old forward-down    |                 2.31 |            289.75 |     71.86 |
| Fin collar: corrected aft-down  |               163.88 |            270.17 |     71.86 |
| Sled: old foot-down             |               116.00 |           1510.89 |      8.00 |
| Sled: corrected broad-back-down |              1617.00 |              9.89 |      8.00 |

Fin initial material contact increases about 71-fold. The fins remain integral with the collar and cannot all lie flat;
the change improves the geometric print setup but does not establish layer-bond or fin-root strength.

## Native Bambu Studio checks

Local slice comparisons use Bambu Studio 02.08.02.61, X1C/0.4 mm, Generic PLA, Textured PEI, 0.20 mm layers, three
walls, 100% rectilinear fill in modeled solids, automatic build-plate-only supports, and a 5 mm outer brim. The geometry
is identical within each old/new pair; only orientation changes. These are slicer estimates, not print observations.

| Part       | Old total filament g | Corrected total filament g | Old predicted time | Corrected predicted time |
| ---------- | -------------------: | -------------------------: | -----------------: | -----------------------: |
| Fin collar |                34.05 |                      30.34 |           71.4 min |                 65.6 min |
| Sled       |                 7.95 |                       5.29 |           23.3 min |                 19.3 min |

Totals include slicer-generated consumables such as supports/brims; they are not the finished flight-part mass.
[Native slicer summary and source hashes](../docs-evidence/orientation-slices.json) retain the numeric comparison. Both
fin orientations still generate support. The corrected sled has no support extrusion in the filament usage metadata. The
raw `support_used` flag is true even there, so it is not used alone to infer actual support material. Raw
`first_layer_time` values include nonsensical numbers and are not reported as valid measurements. CLI logs include
missing expanded-system-preset warnings; the projects embed the resolved installed profiles. The per-plate warning
message is empty for these checks, but that is not a physical printability guarantee.

Local projects, G-code, logs, settings, and result JSON are preserved under `deliverables/orientation-fin-forward/`,
`orientation-fin-aft/`, `orientation-sled-old/`, and `orientation-sled-flat/`. No G-code was sent to a printer.

## Use the revised project

[Download the unsliced V3 Bambu Studio project](../docs-evidence/prints/rocket-fit-check-v3.3mf).

`deliverables/x1c-pla-orientation-v3/rocket-fit-check-v3.3mf` combines the 50 mm cone, curved lug saddles, aft-down fin
collar, and broad-back-down sled. Open the unsliced project, choose/calibrate the actual filament, and inspect its
sliced layers before printing. Do not reuse the earlier fin/sled layouts.

Supports must be removable without damaging the thin fins, nose interior, screw bosses, or fitting surfaces. Initial
adhesion, paper/PLA bonds, printed mass, and load-path strength still require physical checks. Separately printing flat
fins with keyed joints is a possible future geometry revision, not implemented here.

## Reproduce

```sh
uv run --extra cad python scripts/analyze_orientation.py path/to/config.yaml
```

Each output retains all oriented STLs and JSON metrics.
`scripts/package_bambu.py --run <orientation-run>/<orientation> --parts fin-collar --output <new-output-directory> --slice-check`
creates native projects and local slicing evidence. The generator refuses to overwrite an existing project. The
six-orientation search is bounded, not exhaustive.
