# Current project status

Updated 2026-09-13. Start at [current designs](CURRENT_DESIGN.md), not an earlier study report.

- Current performance-led candidate: D12-5, BT-60, 430 mm body, small clipped-delta fins and a provisional 20-inch
  chute. Its 192 planned dummy/logger uncertainty cases meet the configured numeric gates; loaded apogee spans
  154.32–193.99 m. These cases are a bounded study, not a probability of success or physical validation.
- [24 mm motor comparison](MOTOR24.md): 405 completed flights.
- [Fin and recovery comparison](FIN_SHAPES.md): 144 nominal fin cases, 16 CAD print-orientation screens, 1,440 original
  uncertainty cases, 54 larger-chute screening cases and 864 larger-chute uncertainty cases. The original 18-inch
  recovery options did not clear the full planned uncertainty envelope. The 20-, 22- and 24-inch options each clear all
  192 planned cases in their respective revised configurations.
- CFD is in progress, not accepted for design selection. The first completed pilot fails the zero-angle symmetry check
  despite settled coefficients. A finer baseline is running; results will be posted after its audit.
- [Recovery attachment and cap hardware](RECOVERY_ANCHOR.md): specific insert and nut dimensions have been sourced.
  Neither is a drop-in fit to the existing bosses. Hardware selection, detailed fit, mass/CG updates and retention
  checks remain open.
- The existing six-part V5 X1C download is the older 18 mm review package, not the new D12 candidate. New final print
  packaging remains pending. No servo-equipped configuration or logger firmware is implemented.
- Physical fit, measured mass/CG, pressure response, recovery separation and flight validation remain pending.

## Ongoing work and publication

The active objective remains to compare designs and document their performance, including the outstanding CFD work. On
2026-09-13 the user authorized publishing all new findings to the repository's GitHub Pages documentation while work
continues. Publish completed evidence and clearly labeled interim results; do not describe unfinished studies as
validated. This authorization does not include purchases, printer operation or claims of physical validation.

Earlier 18 mm geometry/nose and avionics studies remain available from the explicitly labeled older review section of
[current designs](CURRENT_DESIGN.md). Their historical limits do not define the current performance target.

Old milestone tables, counts, generic-payload assumptions and prior shopping budgets are confined to the
[archive](ARCHIVE.md). The software/runtime integration method is documented in [modeling](MODELING.md).
