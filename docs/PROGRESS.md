# Current project status

Updated 2026-09-13. Start at [current designs](CURRENT_DESIGN.md), not an earlier study report.

- Current shortlist: D12-5 / BT-60 / clipped-delta, with 22-inch recovery and a 460 mm body, or a sourced 24-inch canopy
  and a 500 mm body. Both pass 192/192 planned expanded uncertainty cases. Loaded altitudes span approximately 145–188
  m; see the comparison for speed, descent and drift. These are bounded results, not physical validation.
- [24 mm motor comparison](MOTOR24.md): 405 completed flights.
- [Fin and recovery comparison](FIN_SHAPES.md): 144 nominal fin cases, 16 CAD print-orientation screens, 1,440 original
  uncertainty cases, 54 larger-chute screening cases and 864 larger-chute uncertainty cases. The original 18-inch
  recovery options did not clear the full planned uncertainty envelope. The subsequent 36-case sourced-chute screen and
  864-case expanded recovery comparison are also complete. In the expanded bounds, the prior 20-inch option passes only
  156/192 planned cases, with 36 descent failures; the 22-inch and sourced 24-inch options each pass 192/192.
- CFD diagnostics are complete for this review, but not accepted for design selection. Three baseline grids settle but
  fail zero-angle symmetry; drag changes by −2.46% then −7.51% with refinement. The corrected-surface baseline also
  completes and fails symmetry. Ring-tail CAD trials add 3.55/7.10 g; their aerodynamic ranking is deferred until a
  baseline passes validation. No aerodynamic benefit or disadvantage is established.
- [Recovery attachment and cap hardware](RECOVERY_ANCHOR.md): specific insert and nut dimensions have been sourced.
  Neither is a drop-in fit to the existing bosses. Two insert CAD trials clear the full modeled insertion path only
  after rerouting equal-volume wiring allowances. A separate configured insert integration now passes all 24 planned
  cases in a 36-flight screen and all 192 planned cases in the completed 288-flight uncertainty rerun, including
  provisional joint mass. Measured hardware mass and physical retention remain open.
- A separate integrated D12 review bundle now includes matching CAD, flight models, X1C project, renders and retained
  simulation evidence. Local slicing and placement checks pass. The V5 download remains the archived 18 mm package;
  physical print/flight qualification is not implied. No servo-equipped configuration or logger firmware is implemented.
- Physical fit, measured mass/CG, pressure response, recovery separation and flight validation remain pending.

## Ongoing work and publication

The active objective remains to compare designs and document their performance, including the outstanding CFD work. On
2026-09-13 the user authorized publishing all new findings to the repository's GitHub Pages documentation while work
continues, then requested that subsequent findings be bundled for publication when ready. Publish completed evidence and
clearly labeled interim results; do not describe unfinished studies as validated. This authorization does not include
purchases, printer operation or claims of physical validation.

Earlier 18 mm geometry/nose and avionics studies remain available from the explicitly labeled older review section of
[current designs](CURRENT_DESIGN.md). Their historical limits do not define the current performance target.

Old milestone tables, counts, generic-payload assumptions and prior shopping budgets are confined to the
[archive](ARCHIVE.md). The software/runtime integration method is documented in [modeling](MODELING.md).
