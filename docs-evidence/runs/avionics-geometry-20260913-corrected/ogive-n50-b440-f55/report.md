# Rocket Workbench report

Run: `ogive-n50-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `08a8a51ea75fce6495acec0d83b333e44039af20720af9b8466fb9ee7ba9244a`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.87 |      6.49 |           2.46 | unavailable |       10.64 |    0.30 |            5.24 |             6.24 |              8.17 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.84 |      6.49 |           1.22 | unavailable |        9.99 |    0.26 |            5.24 |             6.24 |              8.15 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.26 |      8.21 |           2.11 |       16.78 |        7.14 |    0.54 |            7.04 |             8.04 |             16.75 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.44 |      8.21 |           1.37 | unavailable |       20.19 |    9.67 |            7.04 |             8.04 |             16.51 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.76 |      8.95 |           2.30 |        1.28 |        4.87 |    0.04 |            7.68 |             8.68 |             34.18 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.60 |      8.94 |           1.66 |        6.53 |        4.87 |    4.11 |            7.67 |             8.67 |             34.03 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.77 |      8.95 |           1.67 |       13.08 |        4.87 |    0.42 |            7.68 |             8.68 |             34.18 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.60 |      8.94 |           1.66 |       19.33 |        4.87 |   15.60 |            7.67 |             8.67 |             34.03 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    70.29 |     13.00 |           2.10 |        4.84 |        4.88 |    0.00 |           11.61 |            12.61 |             26.25 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.48 |     12.99 |           1.78 |        6.12 |        4.88 |    9.67 |           11.61 |            12.61 |             26.08 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.05 |      5.60 |           2.91 | unavailable |        9.68 |    0.14 |            4.53 |             5.53 |              6.58 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.04 |      5.59 |           1.72 | unavailable |        9.12 |    0.28 |            4.53 |             5.52 |              6.56 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.35 |      7.27 |           2.92 | unavailable |       15.94 |    0.74 |            6.13 |             7.13 |             13.84 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.63 |      7.26 |           2.03 | unavailable |       17.93 |    7.91 |            6.13 |             7.13 |             13.60 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.85 |      8.04 |           2.58 |        2.50 |        5.18 |    0.03 |            6.72 |             7.72 |             28.94 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.32 |      8.03 |           2.12 |        8.13 |        5.18 |    7.43 |            6.71 |             7.71 |             28.84 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.85 |      8.04 |           2.58 |       17.50 |        5.18 |    1.35 |            6.72 |             7.72 |             28.94 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.32 |      8.03 |           2.12 |       23.04 |        5.18 |   30.86 |            6.71 |             7.71 |             28.84 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.05 |     12.28 |           2.56 |        8.45 |        5.19 |    0.16 |           10.22 |            11.21 |             21.73 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.03 |     12.27 |           2.32 |        9.90 |        5.19 |    1.01 |           10.21 |            11.21 |             21.59 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.05 |      5.60 |           2.91 | unavailable |        9.68 |    0.14 |            4.53 |             5.53 |              6.58 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.04 |      5.59 |           1.72 | unavailable |        9.12 |    0.28 |            4.53 |             5.52 |              6.56 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.35 |      7.27 |           2.92 | unavailable |       15.94 |    0.74 |            6.13 |             7.13 |             13.84 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.63 |      7.26 |           2.03 | unavailable |       17.93 |    7.91 |            6.13 |             7.13 |             13.60 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.85 |      8.04 |           2.58 |        2.50 |        5.18 |    0.03 |            6.72 |             7.72 |             28.94 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.32 |      8.03 |           2.12 |        8.13 |        5.18 |    7.43 |            6.71 |             7.71 |             28.84 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.85 |      8.04 |           2.58 |       17.50 |        5.18 |    1.35 |            6.72 |             7.72 |             28.94 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.32 |      8.03 |           2.12 |       23.04 |        5.18 |   30.86 |            6.71 |             7.71 |             28.84 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.05 |     12.28 |           2.56 |        8.45 |        5.19 |    0.16 |           10.22 |            11.21 |             21.73 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.03 |     12.27 |           2.32 |        9.90 |        5.19 |    1.01 |           10.21 |            11.21 |             21.59 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
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
- dummy-C6-5-wind2: Recovery device deployment at high speed (23 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (23 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=160.09238712641988 g (allowed None … 85.0); apogee_m=6.870469280677541 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.492287604470219 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.643468557523528 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=160.09238712641988 g (allowed None … 85.0); apogee_m=6.83993494797417 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.4858380440524535 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.987297105748269 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=162.64238712641986 g (allowed None … 99.0); apogee_m=24.255551782288663 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.214800229215447 m/s (allowed 12.0 … None); deployment_speed_m_s=16.77564649308948
  m/s (allowed None … 10.0); landing_descent_m_s=7.141458687580952 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=162.64238712641986 g (allowed None … 99.0); apogee_m=23.438644395652123 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.207704489048892 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=20.185510902945616 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=166.84238712641988 g (allowed None … 113.0); guide_departure_m_s=8.949135524015558 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=166.84238712641988 g (allowed None … 113.0); guide_departure_m_s=8.942475772670905 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=166.84238712641988 g (allowed None … 113.0); guide_departure_m_s=8.949135524015558 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.08400803225285 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=166.84238712641988 g (allowed None … 113.0); guide_departure_m_s=8.942475772670905 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.329841777799544 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=180.74238712641989 g (allowed None … 85.0); apogee_m=5.053740367758429 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.595426513278441 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.682188222971364 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=180.74238712641989 g (allowed None … 85.0); apogee_m=5.044638078398039 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.590019379603169 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.121923538581408 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=183.29238712641987 g (allowed None … 99.0); apogee_m=18.347744553358208 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.266552414294283 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.937770213252838 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=183.29238712641987 g (allowed None … 99.0); apogee_m=17.626818239482123 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.260431320731699 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.9277279198681 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.035681457664445 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.029806638110138 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.035681457664445 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.49834601858816 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.029806638110138 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.042157249355977 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=180.74238712641989 g (allowed None … 85.0); apogee_m=5.053740367758429 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.595426513278441 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.682188222971364 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=180.74238712641989 g (allowed None … 85.0); apogee_m=5.044638078398039 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.590019379603169 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.121923538581408 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=183.29238712641987 g (allowed None … 99.0); apogee_m=18.347744553358208 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.266552414294283 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.937770213252838 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=183.29238712641987 g (allowed None … 99.0); apogee_m=17.626818239482123 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.260431320731699 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.92772791986806 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.035681457664445
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.029806638110138
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.035681457664445
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.498346018588148 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=187.49238712641989 g (allowed None … 113.0); guide_departure_m_s=8.029806638110138
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.04215724935596 m/s (allowed None … 10.0)
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
