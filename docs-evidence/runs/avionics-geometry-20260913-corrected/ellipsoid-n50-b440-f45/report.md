# Rocket Workbench report

Run: `ellipsoid-n50-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `f5fac5874d91f158f3df1de626c2899b77989840d2ff6809cb05de4bfabb1546`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.03 |      6.56 |           2.14 | unavailable |       11.01 |    0.25 |            5.30 |             6.30 |              8.30 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.01 |      6.56 |           0.91 | unavailable |       10.17 |    0.57 |            5.30 |             6.30 |              8.28 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.84 |      8.27 |           2.06 |       12.89 |        4.87 |    2.39 |            7.11 |             8.11 |             17.00 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.17 |      8.27 |           0.98 |       18.84 |        8.87 |    9.14 |            7.11 |             8.11 |             16.78 |
| empty-C6-3-wind0  | completed / outside configured limits |    89.25 |      9.05 |           1.96 |        1.90 |        4.85 |    0.04 |            7.75 |             8.75 |             34.75 |
| empty-C6-3-wind2  | completed / outside configured limits |    85.70 |      9.04 |           1.29 |        6.04 |        4.85 |    8.21 |            7.75 |             8.75 |             34.60 |
| empty-C6-5-wind0  | completed / outside configured limits |    89.27 |      9.05 |           1.64 |       12.18 |        4.85 |    1.35 |            7.75 |             8.75 |             34.75 |
| empty-C6-5-wind2  | completed / outside configured limits |    85.71 |      9.04 |           1.29 |       18.44 |        4.85 |    9.74 |            7.75 |             8.75 |             34.60 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    72.22 |     13.13 |           1.85 |        4.33 |        4.86 |    0.02 |           11.73 |            12.72 |             26.76 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.52 |     13.12 |           1.25 |        5.46 |        4.86 |   11.54 |           11.72 |            12.72 |             26.59 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.16 |      5.65 |           2.58 | unavailable |        9.88 |    0.11 |            4.57 |             5.57 |              6.68 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.15 |      5.65 |           1.40 | unavailable |        9.22 |    0.42 |            4.57 |             5.57 |              6.66 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.74 |      7.32 |           2.57 | unavailable |       15.88 |    0.57 |            6.19 |             7.18 |             14.04 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.18 |      7.31 |           1.49 | unavailable |       17.88 |    6.71 |            6.18 |             7.18 |             13.84 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.59 |      8.12 |           2.14 |        2.02 |        5.16 |    0.03 |            6.78 |             7.77 |             29.38 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.61 |      8.11 |           1.74 |        7.35 |        5.16 |    3.99 |            6.77 |             7.77 |             29.26 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.59 |      8.12 |           2.14 |       16.46 |        5.16 |    0.90 |            6.78 |             7.77 |             29.38 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.61 |      8.11 |           1.74 |       22.42 |        5.16 |   26.01 |            6.77 |             7.77 |             29.26 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.38 |     12.39 |           2.25 |        8.11 |        5.17 |    0.09 |           10.30 |            11.30 |             22.12 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.49 |     12.38 |           1.90 |        9.29 |        5.17 |    0.61 |           10.30 |            11.29 |             21.98 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.16 |      5.65 |           2.58 | unavailable |        9.88 |    0.11 |            4.57 |             5.57 |              6.68 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.15 |      5.65 |           1.40 | unavailable |        9.22 |    0.42 |            4.57 |             5.57 |              6.66 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.74 |      7.32 |           2.57 | unavailable |       15.88 |    0.57 |            6.19 |             7.18 |             14.04 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.18 |      7.31 |           1.49 | unavailable |       17.88 |    6.71 |            6.18 |             7.18 |             13.84 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.59 |      8.12 |           2.14 |        2.02 |        5.16 |    0.03 |            6.78 |             7.77 |             29.38 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.61 |      8.11 |           1.74 |        7.35 |        5.16 |    3.99 |            6.77 |             7.77 |             29.26 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.59 |      8.12 |           2.14 |       16.46 |        5.16 |    0.90 |            6.78 |             7.77 |             29.38 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.61 |      8.11 |           1.74 |       22.42 |        5.16 |   26.01 |            6.77 |             7.77 |             29.26 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.38 |     12.39 |           2.25 |        8.11 |        5.17 |    0.09 |           10.30 |            11.30 |             22.12 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.49 |     12.38 |           1.90 |        9.29 |        5.17 |    0.61 |           10.30 |            11.29 |             21.98 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (20.6°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.4 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (20.6°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.4 m/s): "Nominal 457 mm parachute and lines"
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings

## Missing measurements / physical checks

- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: 18 mm motor mount tube, thrust ring, hook, two centering rings and adhesive
- Measured mass and balance: Nominal 457 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks
- V2 saddle bond strength and adhesive mass require physical checks; saddle-specific aerodynamic drag is unresolved
- Avionics board/antenna/battery masses, stack clearances, retention, wiring and power must be measured; vendor CAD is
  not physical validation
- Static-port drilling/alignment, bulkhead and screw seals, pressure lag and aerodynamic pressure bias require
  bench/flight validation

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=158.6922275169132 g (allowed None … 85.0); apogee_m=7.030369094130369 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.562565923358551 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.008712184446095 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=158.6922275169132 g (allowed None … 85.0); apogee_m=7.011309135404335 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.556431487827957 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9106589251007261 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.16923831998069 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=161.2422275169132 g (allowed None … 99.0); apogee_m=24.837320059867444 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.274737968756595 m/s (allowed 12.0 … None); deployment_speed_m_s=12.890601825242948 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=161.2422275169132 g (allowed None … 99.0); apogee_m=24.171064771372006 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.268143648622223 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9780819487786396 cal (allowed 1.0 … None); deployment_speed_m_s=18.842517929887688 m/s
  (allowed None … 10.0); landing_descent_m_s=8.865816849824839 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=165.4422275169132 g (allowed None … 113.0); guide_departure_m_s=9.04623140184501 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=165.4422275169132 g (allowed None … 113.0); guide_departure_m_s=9.039925224348027 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=165.4422275169132 g (allowed None … 113.0); guide_departure_m_s=9.04623140184501 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.184400346796867 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=165.4422275169132 g (allowed None … 113.0); guide_departure_m_s=9.039925224348027 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.44023288596148 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=179.3422275169132 g (allowed None … 85.0); apogee_m=5.160482177552065 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.652830100358566 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.87585696866554 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=179.3422275169132 g (allowed None … 85.0); apogee_m=5.152149301598506 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.647744084054922 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.217335754352725 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=181.8922275169132 g (allowed None … 99.0); apogee_m=18.739800317649877 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.316779608281286 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.875752462849464 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=181.8922275169132 g (allowed None … 99.0); apogee_m=18.176401916687873 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.31108087790995 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.882420875290716 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.116016167808455 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.110455972786667 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.116016167808455 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.460861970606683 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.110455972786667 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.415596055704647 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=179.3422275169132 g (allowed None … 85.0); apogee_m=5.160482177552065 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.652830100358566 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.87585696866554 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=179.3422275169132 g (allowed None … 85.0); apogee_m=5.152149301598506 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.647744084054922 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.217335754352725 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=181.8922275169132 g (allowed None … 99.0); apogee_m=18.739800317649877 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.316779608281286 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.875752462849471 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=181.8922275169132 g (allowed None … 99.0); apogee_m=18.176401916687873 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.31108087790995 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.88242087529073 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.116016167808455 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.110455972786667 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.116016167808455 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.460861970606686 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=186.0922275169132 g (allowed None … 113.0); guide_departure_m_s=8.110455972786667 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.41559605570503 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is
  scenario-dependent.
- Native OpenRocket aerodynamics; configured axisymmetric nose, cylindrical sections, three flat trapezoidal fins and
  tapered collar fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
- CAD volume × material density is a solid-mass estimate. Nose/bay/sled lumped mass and CG; fin mass included once in
  collar override.
- No external camera/antenna is modeled. Configuration rejects protrusions. An internal camera has no guaranteed useful
  view.
- Stability minimum is sampled from guide departure strictly before apogee or deployment, whichever comes first, using
  (CP−CG)/reference diameter. Low-speed samples remain included; time, speed and angle at the minimum are in JSON.
- Event metrics interpolate adjacent samples at the engine event time. Landing descent is vertical speed at ground
  event, not a structural impact assessment.
- Powered peaks use positive-thrust samples from liftoff strictly before first burnout, deployment, abort or ground
  contact. Missing events/data yield unavailable metrics; peak times and sample coverage are in JSON. These are sampled
  single-stage maxima, not continuous-time bounds.
- Powered acceleration is trajectory acceleration magnitude / 9.80665. Estimated load is hypot(lateral acceleration,
  vertical acceleration + local gravity) / 9.80665 at the center of mass. Coriolis correction, sensor-offset rotation,
  vibration and deployment/impact shock are excluded; this is not a per-axis IMU prediction or a hardware survival
  rating.
- Recovery is motor-ejection deployment with configured Cd; packing envelope, ejection seal, thermal protection and
  attachment loads require physical checks.
- Reference mode preserves upstream geometry and masses; demonstration CAD and baseline mass assumptions do not apply to
  that reference.

## Configured criteria

- apogee_m: 30.0 … 120.0 m; engineering assumption; Project engineering assumption for demonstration screening; not a
  launch clearance
- guide_departure_m_s: 12.0 … None m/s; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance
- minimum_ascent_stability_cal: 1.0 … None cal; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance
- deployment_speed_m_s: None … 10.0 m/s; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance
- landing_descent_m_s: None … 6.0 m/s; engineering assumption; Project engineering assumption for demonstration
  screening; not a launch clearance

## Reproducibility

```json
{
  "openrocket": "24.12",
  "java": "21.0.3+7-LTS-152",
  "python": "3.14.6",
  "bridge_revision": "fb132c49e661bb00c5586cce6a4ac0c655425197",
  "jar_sha256": "4959b72f52f5f607941e9722abbb7b7f0c4a38ebbbf84204a329db9f31c4f897",
  "packages": {
    "orhelper": "0.1.5",
    "jpype1": "1.7.1",
    "numpy": "2.5.3",
    "pydantic": "2.13.5",
    "cadquery": "2.8.0"
  },
  "repository_revision": "d2e7da5d4632c052bc516be47ba0e99b609fb176"
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
