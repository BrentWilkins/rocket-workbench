# MVP design review — 2026-09-12

**Follow-up studies:** [nose comparison](NOSE_STUDY.md) identifies a lighter 50 mm cone for fit checking;
[print-orientation analysis](PRINT_ORIENTATION.md) corrects the earlier fin collar and sled layouts.

**Mount revision:** the original narrow-contact lug sleeves below have been superseded for printing by
[V2 curved saddles](LUG_SADDLES.md), with new CAD and mass/CG rechecks. The table below retains the historical shortlist
results; do not mistake those historical CAD files for the revised mounts.

Three provisional designs meet the nominal simulation criteria on the specific Estes C5-3 curve. The larger-recovery
candidate is the most useful starting point for **review**, because its 18-inch chute also meets the tested descent
stress cases. It is not cleared for fabrication with arbitrary electronics or for flight. The user explicitly chose a
generic bay and has not selected a battery.

## Shortlist and tradeoffs

All use 41.6 mm OD paper BT-60, a 70 mm printed conical nose, 65 mm internal bay, three 55 mm-span fins, 1.2 mm shell,
1.6 mm fins, two printed lug sleeves, and a commercial 18 mm mount. Provisional payload is 18 g including battery/wires/
sensors, at nose-origin CG 103 mm. Empty retains the bay/sled/hardware.

The ranges below span empty and loaded cases, winds 0 and 2 m/s, C5-3 only. Dummy and `actual` are equivalent mass/CG
cases, not two measured assemblies.

| Candidate       | Body / chute mm | Dry empty / loaded g | Apogee m     | Guide m/s   | Lowest ascent stability cal | Vertical descent m/s | Max displacement m |
| --------------- | --------------- | -------------------- | ------------ | ----------- | --------------------------- | -------------------- | ------------------ |
| Compact         | 340 / 381       | 108.70 / 126.70      | 83.83–105.25 | 13.66–14.37 | 1.06                        | 5.15–5.52            | 25.29              |
| Longer          | 380 / 381       | 110.70 / 128.70      | 81.52–102.36 | 13.45–14.12 | 1.19                        | 5.20–5.56            | 23.86              |
| Larger recovery | 380 / 457       | 114.80 / 132.80      | 77.59–97.72  | 13.53–13.92 | 1.15                        | 4.40–4.70            | 28.69              |

Compact saves 40 mm length and 2 g versus longer, but empty-wind stability is only about 0.06 cal above the assumed
minimum. Longer offers more packing room and a better nominal empty-wind margin. Larger recovery adds about 4.1 g versus
longer and increases modeled bundle length from about 101 to 146 mm; it slows descent at the expense of drift. These are
transparent tradeoffs, not a ranked flight-eligible list. All cases retain `eligible: false`, `rank: null`.

Each candidate compares 5 motor/delay cases × 3 loadings × 2 winds = 30 flights. Six C5-3 cases meet nominal numerical
criteria. The other 24 A8-3, B4-4, C6-3 and C6-5 cases fail one or more gates. In particular, A8 includes deployment
after impact, and the A/B/C6 choices exceed their manufacturer liftoff-mass limits and/or miss guide/deployment targets.
A C6 is not interchangeable with the selected C5 despite sharing the same letter and diameter.

Full evidence:

- [Compact report](../runs/20260912T202256Z-candidate-compact-c137e6e1/report.md)
- [Longer report](../runs/20260912T202254Z-candidate-stable-f4dd410f/report.md)
- [Larger-recovery report](../runs/20260912T192553Z-candidate-recovery-7f53a228/report.md)
- [Larger-recovery assembly preview](../runs/20260912T192553Z-candidate-recovery-7f53a228/cad/assembly.svg)
- [Larger-recovery STEP assembly](../runs/20260912T192553Z-candidate-recovery-7f53a228/cad/assembly.step)
- [Provisional loaded C5-3 flight model, wind 2 m/s](../runs/20260912T192553Z-candidate-recovery-7f53a228/actual-C5-3-wind2.ork)

## Search history and reasonable design changes

The corrected [original bounded grid](../runs/sweep-20260912T192627Z-f956bc56/report.md) contains 27 geometry
combinations: body 260/300/340 mm, fin span 35/45/55 mm, chute 305/381/457 mm. Twelve are rejected for guide/fairing or
packing fit; 15 designs produce 360 retained A8/B4/C6 simulations. None meets the full nominal criteria. This is
evidence about this bounded family, not proof that no small commercial-motor rocket can work.

An early thin-wall experiment reduced mass but did not support all loadings under the chosen altitude/stability
criteria. The corrected [six-design C5 grid](../runs/sweep-20260912T192626Z-59bcc43a/report.md) retains the original
1.2/1.6 mm shell/fin assumptions and examines body 300/340/380 mm and span 45/55 mm with a 381 mm chute. It produces 36
flights and identifies the 340/55 and 380/55 combinations as supporting all three loadings nominally. Shortlist configs
then use the purchasable mount's nominal dimensions. The 18-inch chute variant is an explicit follow-up to the
sensitivity failure, not an unreported enlargement or move outside 18 mm commercial A/B/C scope.

## Uncertainty result

Two studies each run 72 cases: printed mass multipliers 1.0/1.2, payload CG offsets −5/+5 mm, chute Cd 0.6/0.9, wind
0/2/4 m/s, and all three loadings. Purchased mass estimates are **not** varied; nor are motor tolerances, turbulence,
deformation, packing/ejection reliability or the full range of possible payloads.

- [15-inch study](../runs/stress-20260912T192230Z-f253babf/report.md): 42/72 meet the numerical criteria. The other 30
  exceed 6 m/s vertical descent at Cd 0.6.
- [18-inch study](../runs/stress-20260912T192555Z-b85b3edb/report.md): 72/72 meet the numerical criteria. Apogee
  62.64–97.72 m, guide speed 12.93–13.92 m/s, vertical descent 4.02–5.46 m/s, minimum stability 1.055 cal, maximum
  deployment speed 9.883 m/s, maximum displacement 64.98 m.

The last two margins are narrow. Do not extend these findings to stronger winds or heavier payloads. No probability
distributions were assigned; 72/72 is not a reliability percentage. Greater chute area does not guarantee recovery
within a particular field. Physical protection/attachment/packing performance remains unknown regardless of the
simulation pass count.

## Screening criteria and assumptions

| Gate                     | Configured threshold                | Rationale / provenance                                                             |
| ------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------- |
| Apogee                   | 30–120 m                            | Engineering demonstration target for a modest visible flight; not a site approval  |
| Guide departure          | ≥12 m/s                             | Engineering screening assumption; measured usable guide and weather still required |
| Minimum ascent stability | ≥1 caliber                          | Engineering screening assumption; retain low-speed samples and inspect their AOA   |
| Deployment speed         | ≤10 m/s                             | Engineering screening assumption; no validated attachment-load limit               |
| Vertical descent         | ≤6 m/s                              | Engineering landing-speed target; not a structural impact qualification            |
| Liftoff mass             | Motor-specific manufacturer maximum | Sourced in each motor input; C5-3 226 g, A8-3 85 g, B4-4 99 g, C6-3/-5 113 g       |

Atmosphere: ISA at assumed elevation 1600 m, latitude 40°, longitude −105°; vertical 0.9144 m guide, constant wind, zero
turbulence, seed 42. These are not an identified field or forecast. Chute Cd 0.75 is nominal, not manufacturer data.
Launch mass for the larger-recovery C5 case is about 138.60 g empty / 156.60 g loaded. See each report for exact
criteria, curves, warnings and missing inputs.

## Validation and remaining physical gates

The [independent engine proof](../runs/proof-20260912T202227Z-35a8f881/evidence.json) passes altitude/time-series and
event-summary comparison to the separate Java path through OpenRocket 24.12. The earlier proof had zero differences and
the current proof records its own exact differences. A–B–A repeatability and modify/save/reload are exercised. This is
software integration evidence only. An interactive GUI comparison remains pending as permitted by the brief.

Tests cover unit/fit rejection, mass/CG arithmetic and double counting, native geometry propagation, real simulation
failures, missing event outputs, stable reloads, valid STEP solids, watertight STL meshes and rod clearance. See the
packaged test log for the final run; do not infer hardware strength from tests.

Before physical use: follow [BUILD](BUILD.md), [MEASUREMENTS](MEASUREMENTS.md), [SHOPPING](SHOPPING.md) and
[AVIONICS](AVIONICS.md). No purchase, physical validation or launch authorization has occurred. Software completion is
an intermediate review milestone, not a successful first flight.
