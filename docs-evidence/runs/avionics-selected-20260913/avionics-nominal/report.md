# Rocket Workbench report

Run: `avionics-nominal`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `4b244671037619732abc10ea884e171fb651fbce6e7070a593d67873008f7375`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.69 |      6.84 |           1.76 | unavailable |       11.25 |    0.32 |            5.54 |             6.54 |              8.84 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.66 |      6.83 |           0.74 | unavailable |       10.63 |    0.58 |            5.54 |             6.54 |              8.81 |
| empty-B4-4-wind0  | completed / outside configured limits |    26.74 |      8.59 |           1.58 |       14.37 |        4.77 |    3.12 |            7.42 |             8.42 |             17.91 |
| empty-B4-4-wind2  | completed / outside configured limits |    25.99 |      8.58 |           0.77 |       14.82 |        4.76 |    5.34 |            7.41 |             8.41 |             17.68 |
| empty-C6-3-wind0  | completed / outside configured limits |    92.74 |      9.30 |           1.61 |        2.27 |        4.76 |    0.04 |            8.07 |             9.07 |             36.07 |
| empty-C6-3-wind2  | completed / outside configured limits |    89.21 |      9.30 |           1.07 |        5.85 |        4.76 |   10.93 |            8.07 |             9.07 |             35.90 |
| empty-C6-5-wind0  | completed / outside configured limits |    92.78 |      9.30 |           1.10 |       12.34 |        4.76 |    1.45 |            8.07 |             9.07 |             36.07 |
| empty-C6-5-wind2  | completed / outside configured limits |    89.24 |      9.30 |           1.07 |       17.88 |        4.76 |    6.24 |            8.07 |             9.07 |             35.90 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    75.77 |     13.29 |           1.51 |        3.75 |        4.76 |    0.02 |           12.19 |            13.19 |             27.86 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    74.10 |     13.28 |           1.03 |        4.91 |        4.76 |   14.36 |           12.18 |            13.18 |             27.68 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.61 |      5.89 |           2.24 | unavailable |       10.20 |    0.14 |            4.76 |             5.76 |              7.09 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.59 |      5.89 |           1.23 | unavailable |        9.52 |    0.35 |            4.76 |             5.76 |              7.07 |
| dummy-B4-4-wind0  | completed / outside configured limits |    20.14 |      7.56 |           2.13 | unavailable |       16.39 |    0.55 |            6.43 |             7.42 |             14.77 |
| dummy-B4-4-wind2  | completed / outside configured limits |    19.48 |      7.58 |           1.37 | unavailable |       18.55 |    7.58 |            6.42 |             7.42 |             14.54 |
| dummy-C6-3-wind0  | completed / outside configured limits |    73.97 |      8.37 |           1.77 |        1.44 |        5.08 |    0.03 |            7.03 |             8.03 |             30.54 |
| dummy-C6-3-wind2  | completed / outside configured limits |    69.96 |      8.37 |           1.52 |        6.95 |        5.08 |    1.85 |            7.02 |             8.02 |             30.40 |
| dummy-C6-5-wind0  | completed / outside configured limits |    73.97 |      8.37 |           1.77 |       16.11 |        5.08 |    0.64 |            7.03 |             8.03 |             30.54 |
| dummy-C6-5-wind2  | completed / outside configured limits |    69.96 |      8.37 |           1.52 |       21.67 |        5.08 |   23.12 |            7.02 |             8.02 |             30.40 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    59.50 |     12.52 |           1.97 |        7.43 |        5.08 |    0.06 |           10.67 |            11.67 |             23.10 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    57.62 |     12.51 |           1.68 |        8.62 |        5.08 |    2.93 |           10.66 |            11.66 |             22.95 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.61 |      5.89 |           2.24 | unavailable |       10.20 |    0.14 |            4.76 |             5.76 |              7.09 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.59 |      5.89 |           1.23 | unavailable |        9.52 |    0.35 |            4.76 |             5.76 |              7.07 |
| actual-B4-4-wind0 | completed / outside configured limits |    20.14 |      7.56 |           2.13 | unavailable |       16.39 |    0.55 |            6.43 |             7.42 |             14.77 |
| actual-B4-4-wind2 | completed / outside configured limits |    19.48 |      7.58 |           1.37 | unavailable |       18.55 |    7.58 |            6.42 |             7.42 |             14.54 |
| actual-C6-3-wind0 | completed / outside configured limits |    73.97 |      8.37 |           1.77 |        1.44 |        5.08 |    0.03 |            7.03 |             8.03 |             30.54 |
| actual-C6-3-wind2 | completed / outside configured limits |    69.96 |      8.37 |           1.52 |        6.95 |        5.08 |    1.85 |            7.02 |             8.02 |             30.40 |
| actual-C6-5-wind0 | completed / outside configured limits |    73.97 |      8.37 |           1.77 |       16.11 |        5.08 |    0.64 |            7.03 |             8.03 |             30.54 |
| actual-C6-5-wind2 | completed / outside configured limits |    69.96 |      8.37 |           1.52 |       21.67 |        5.08 |   23.12 |            7.02 |             8.02 |             30.40 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    59.50 |     12.52 |           1.97 |        7.43 |        5.08 |    0.06 |           10.67 |            11.67 |             23.10 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    57.62 |     12.51 |           1.68 |        8.62 |        5.08 |    2.93 |           10.66 |            11.66 |             22.95 |

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
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (21.7 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (21.7 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=152.8487754861409 g (allowed None … 85.0); apogee_m=7.688653494540828 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.84208495417975 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.247667727037735 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=152.8487754861409 g (allowed None … 85.0); apogee_m=7.6554417146883305 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.834724745970673 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7412528569920422 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.625846032963134 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=155.3987754861409 g (allowed None … 99.0); apogee_m=26.740331677734343 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.58962243258586 m/s (allowed 12.0 … None); deployment_speed_m_s=14.3724572149061 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=155.3987754861409 g (allowed None … 99.0); apogee_m=25.99349238126657 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.581700258062488 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7728057880822513 cal (allowed 1.0 … None); deployment_speed_m_s=14.822256069981943 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=159.5987754861409 g (allowed None … 113.0); guide_departure_m_s=9.303895175425858 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=159.5987754861409 g (allowed None … 113.0); guide_departure_m_s=9.296532525463194 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=159.5987754861409 g (allowed None … 113.0); guide_departure_m_s=9.303895175425858 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.340164751035099 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=159.5987754861409 g (allowed None … 113.0); guide_departure_m_s=9.296532525463194 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.88163504987274 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=173.4987754861409 g (allowed None … 85.0); apogee_m=5.6094073346244855 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.894251576289396 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.200409357614888 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=173.4987754861409 g (allowed None … 85.0); apogee_m=5.594999918386226 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.888116739879526 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.518975978094371 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=176.0487754861409 g (allowed None … 99.0); apogee_m=20.13918074521195 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.555758256372316 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.38587563467729 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=176.0487754861409 g (allowed None … 99.0); apogee_m=19.48257721209073 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.5758933103943225 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.550699962274816 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.374770226761727 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.368185653241117 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.374770226761727 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.11392728841308 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.368185653241117 m/s
  (allowed 12.0 … None); deployment_speed_m_s=21.66621124811662 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=173.4987754861409 g (allowed None … 85.0); apogee_m=5.6094073346244855 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.894251576289396 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.200409357614888 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=173.4987754861409 g (allowed None … 85.0); apogee_m=5.594999918386226 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.888116739879526 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.518975978094373 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=176.0487754861409 g (allowed None … 99.0); apogee_m=20.13918074521195 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.555758256372316 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.385875634677294 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=176.0487754861409 g (allowed None … 99.0); apogee_m=19.48257721209073 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.5758933103943225 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.550699962274802 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.374770226761727
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.368185653241117
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.374770226761727
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.113927288413077 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=180.24877548614091 g (allowed None … 113.0); guide_departure_m_s=8.368185653241117
  m/s (allowed 12.0 … None); deployment_speed_m_s=21.66621124811623 m/s (allowed None … 10.0)
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
