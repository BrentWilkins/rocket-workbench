# Progress

Implementation started 2026-09-12 from ROCKET_PROJECT_BRIEF.md.

## Current avionics milestone

See [current designs](CURRENT_DESIGN.md) for the corrected 54-geometry search (1,620 flights), three-option uncertainty
comparison (432 flights), and full nominal/upper performance-option comparison (60 flights). The recovery-wadding CG
error is corrected and guarded by validation. Component-level mass, detailed/keepout CAD, renders, fresh
print-orientation analysis and the native six-part V5 project are supplied. No candidate clears the complete stress
envelope.

## Historical MVP evidence

This table records the first MVP milestone, not the current avionics configuration or current test count. See the
[component-level hardware work](AVIONICS_DESIGN.md) for the later mass, CAD and simulation revisions.

| Requirement                                               | Status / evidence                                                                                                                                                                                            |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Python 3.14 + uv-managed dependencies                     | Python 3.14.6, uv.lock; offline locked sync succeeds; README setup commands                                                                                                                                  |
| Maintained bridge and current stable engine investigation | Pinned OpenRocket 24.12 / exact OpenRocket-owned orhelper archive; runtime verifies identities; MODELING.md decision record                                                                                  |
| Real integration and independent comparison               | `runs/proof-20260912T202227Z-35a8f881/evidence.json`; real simulation, listener, modification/reload, A–B–A and independent Java path pass                                                                   |
| GUI comparison                                            | Pending, explicitly not claimed; same-engine independent path supplied                                                                                                                                       |
| Canonical CAD/flight model                                | Typed inputs, six printable parts, purchased assembly envelopes, normalized ORK, independent dry mass/CG checks, STEP/STL/rod-clearance tests                                                                |
| Metric corrections                                        | Vertical versus total landing speed, event timing/after-impact deployment, complete ascent interval, missing abort channels, collar transition, lug clearance and mount overhang addressed; regression tests |
| Bounded geometry studies                                  | Corrected 27-design grid: 12 fit rejections + 360 flights, no nominal passes; six-design C5 follow-up: 36 flights and two all-loading combinations                                                           |
| Shortlist                                                 | Three complete candidates, 30 motor/loading/wind cases each; six nominal C5-3 passes per candidate, other cases retained; REVIEW.md links                                                                    |
| Uncertainty / design changes                              | 15-inch chute: 42/72 stress passes; 18-inch: 72/72 within tested bounds; no probability or reliability claim                                                                                                 |
| Reports and reproducibility                               | Resolved inputs, curves/time series/events, CSV/Markdown/logs, unique run paths and new content-hash manifests; source available without publishing                                                          |
| Tests                                                     | 20 checks passed in a freshly recreated Python 3.14 environment using offline uv; package_review.py reruns them and preserves logs/JUnit in each bundle                                                      |
| Build and first-outing shopping guide                     | BUILD.md, SHOPPING.md, MEASUREMENTS.md; sourced commercial components, quantities, allowances, load paths and physical gates                                                                                 |
| Generic avionics scope                                    | User explicitly requested generic bay, no battery selected; AVIONICS.md records this decision and future sensor options; no final fitted-electronics claim                                                   |
| Advanced scope                                            | Separate adapters and documented future log/CFD/sampling boundaries; no active guidance, firmware or motor/ignition work                                                                                     |

See REVIEW.md for authoritative reviewed run paths. Earlier development runs remain intact but may predate corrected
metrics/interfaces. New generation never overwrites them. The packaging script copies selected evidence into a unique
local directory, verifies available run hashes and writes a bundle manifest.

Physical hardware identification, measurements, fabrication, assembly, ejection checks, and flight validation have not
occurred. Demonstration assumptions must not be interpreted as measured hardware or an approved flight design.
