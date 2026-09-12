# V2 launch-lug saddles

The original printed cylinders had only narrow tangential contact with the paper tube. New CAD replaces that interface
with a concave pad joined to each sleeve. Historical runs and print projects are preserved, not retroactively fixed.

## Geometry

- 25 mm axial length, 12 mm saddle width, 1.2 mm radial pad thickness.
- Saddle inner radius is half the configured body OD plus a provisional 0.15 mm adhesive gap.
- Approximately 304 mm² of curved mating area on a nominal 41.6 mm OD tube, per mount.
- The original sleeve's tangent tip is trimmed at the saddle radius, preventing concentrated contact with the paper.
- Original 4.8 mm sleeve bore accepts the assumed 4.6 mm OD paper lug. Measure those purchased lugs.
- Rod center, axial locations, and 60-degree placement between fins are unchanged.
- No holes or screws penetrate the thin paper tube. These are rod-lug mounts, not rail buttons.

This is our own mounting-pad geometry, not a copy of an Estes molded part or a claim of superior tested strength.
[Estes instructions](https://estesrockets.com/cdn/shop/files/007301-Green-Eggs-Instructions.pdf) provide a reference for
aligned lug attachment and adhesive fillets. Plastic-to-paper bonding needs its own compatible adhesive and physical
tests; ordinary paper/balsa glue guidance does not establish a reliable PLA bond.

## Verification boundaries

CAD tests check single connected solids, concave mating area, tube clearance, open bores, and unobstructed rod travel.
STEP/STL checks and the mass ledger include the saddle material. Additional adhesive mass is still provisional. The
native OpenRocket launch-lug component still approximates the cylindrical sleeve: it does not explicitly resolve the
saddle's noncylindrical drag. Updated simulations are mass/CG rechecks under that aerodynamic approximation, not
aerodynamic or mechanical validation of the new mount.

Print fit samples first. Verify seating without rocking, paper integrity, fillet quality, and free sliding of both lugs
on the actual rod. Check representative bonded coupons before accepting the assembly for further flight review. Larger
mating area reduces the geometric contact limitation; it does not prove sufficient peel or shear strength.

## Revised evidence

Each PLA mount is estimated at 1.287 g, versus 0.997 g for the old cylinder: approximately 0.58 g added for the pair.
The updated [30-case motor comparison](../runs/20260912T224649Z-candidate-recovery-b6aebae0/report.md) retains six C5-3
cases meeting numerical gates. The other motor/delay cases still fail one or more gates. The
[72-case sensitivity recheck](../runs/stress-20260912T224737Z-ab489bc8/report.md) meets the numerical gates in all 72
cases under the cylindrical-lug aerodynamic approximation. This is not a reliability probability or flight approval.

- [Revised STEP mount](../runs/20260912T224649Z-candidate-recovery-b6aebae0/cad/lug-sleeve-1.step)
- [Revised STL mount](../runs/20260912T224649Z-candidate-recovery-b6aebae0/cad/lug-sleeve-1.stl)
- [Complete revised assembly](../runs/20260912T224649Z-candidate-recovery-b6aebae0/cad/assembly.step)

The local Bambu project is in `deliverables/bambu-x1c-pla-saddles-v2/`; use that instead of the original fit-check
project. All 23 tests pass, including real CAD/Java integration. No physical bond or print test has been performed.
