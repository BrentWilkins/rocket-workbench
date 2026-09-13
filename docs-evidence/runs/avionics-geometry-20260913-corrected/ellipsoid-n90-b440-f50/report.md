# Rocket Workbench report

Run: `ellipsoid-n90-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `c8de789ea77c5fefe6f2bd4465747bdcc889b4ec0cb9aa79fcbb6cbb51a988a2`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.36 |      6.26 |           2.33 | unavailable |       10.63 |    0.22 |            5.05 |             6.05 |              7.75 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.35 |      6.25 |           1.01 | unavailable |        9.79 |    0.56 |            5.05 |             6.05 |              7.73 |
| empty-B4-4-wind0  | completed / outside configured limits |    22.65 |      7.96 |           2.07 |       12.86 |        8.38 |    2.06 |            6.80 |             7.80 |             15.99 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.00 |      7.96 |           1.13 | unavailable |       19.08 |    8.57 |            6.80 |             7.80 |             15.77 |
| empty-C6-3-wind0  | completed / outside configured limits |    82.33 |      8.71 |           2.28 |        0.44 |        4.95 |    0.04 |            7.42 |             8.42 |             32.86 |
| empty-C6-3-wind2  | completed / outside configured limits |    78.60 |      8.71 |           1.49 |        6.18 |        4.95 |    3.69 |            7.42 |             8.42 |             32.71 |
| empty-C6-5-wind0  | completed / outside configured limits |    82.33 |      8.71 |           1.95 |       12.10 |        4.95 |    1.42 |            7.42 |             8.42 |             32.86 |
| empty-C6-5-wind2  | completed / outside configured limits |    78.60 |      8.71 |           1.49 |       19.85 |        4.95 |   15.67 |            7.42 |             8.42 |             32.71 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    66.41 |     12.81 |           2.05 |        5.71 |        4.96 |    0.01 |           11.24 |            12.24 |             25.12 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    64.65 |     12.80 |           1.50 |        6.67 |        4.96 |    7.73 |           11.24 |            12.24 |             24.96 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.71 |      5.39 |           2.91 | unavailable |        9.47 |    0.10 |            4.38 |             5.38 |              6.24 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.70 |      5.39 |           1.46 | unavailable |        8.89 |    0.44 |            4.38 |             5.37 |              6.23 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.20 |      7.06 |           2.85 | unavailable |       15.10 |    0.55 |            5.94 |             6.94 |             13.24 |
| dummy-B4-4-wind2  | completed / outside configured limits |    16.65 |      7.05 |           1.56 | unavailable |       17.08 |    6.42 |            5.94 |             6.94 |             13.03 |
| dummy-C6-3-wind0  | completed / outside configured limits |    65.25 |      7.84 |           1.93 |        3.32 |        5.26 |    0.02 |            6.51 |             7.51 |             27.84 |
| dummy-C6-3-wind2  | completed / outside configured limits |    61.16 |      7.83 |           1.89 |        8.16 |        5.26 |    7.38 |            6.51 |             7.51 |             27.74 |
| dummy-C6-5-wind0  | completed / outside configured limits |    65.25 |      7.84 |           1.93 |       17.47 |        5.26 |    0.96 |            6.51 |             7.51 |             27.84 |
| dummy-C6-5-wind2  | completed / outside configured limits |    61.16 |      7.83 |           1.89 |       23.59 |        5.26 |   30.49 |            6.51 |             7.51 |             27.74 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    52.01 |     12.05 |           2.03 |        9.21 |        5.26 |    0.20 |            9.92 |            10.92 |             20.78 |
| dummy-C5-3-wind2  | completed / outside configured limits |    50.07 |     12.04 |           2.13 |       10.48 |        5.26 |    2.34 |            9.91 |            10.91 |             20.66 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.71 |      5.39 |           2.91 | unavailable |        9.47 |    0.10 |            4.38 |             5.38 |              6.24 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.70 |      5.39 |           1.46 | unavailable |        8.89 |    0.44 |            4.38 |             5.37 |              6.23 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.20 |      7.06 |           2.85 | unavailable |       15.10 |    0.55 |            5.94 |             6.94 |             13.24 |
| actual-B4-4-wind2 | completed / outside configured limits |    16.65 |      7.05 |           1.56 | unavailable |       17.08 |    6.42 |            5.94 |             6.94 |             13.03 |
| actual-C6-3-wind0 | completed / outside configured limits |    65.25 |      7.84 |           1.93 |        3.32 |        5.26 |    0.02 |            6.51 |             7.51 |             27.84 |
| actual-C6-3-wind2 | completed / outside configured limits |    61.16 |      7.83 |           1.89 |        8.16 |        5.26 |    7.38 |            6.51 |             7.51 |             27.74 |
| actual-C6-5-wind0 | completed / outside configured limits |    65.25 |      7.84 |           1.93 |       17.47 |        5.26 |    0.96 |            6.51 |             7.51 |             27.84 |
| actual-C6-5-wind2 | completed / outside configured limits |    61.16 |      7.83 |           1.89 |       23.59 |        5.26 |   30.49 |            6.51 |             7.51 |             27.74 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    52.01 |     12.05 |           2.03 |        9.21 |        5.26 |    0.20 |            9.92 |            10.92 |             20.78 |
| actual-C5-3-wind2 | completed / outside configured limits |    50.07 |     12.04 |           2.13 |       10.48 |        5.26 |    2.34 |            9.91 |            10.91 |             20.66 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (24°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.6 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (24°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.6 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=165.11213543272981 g (allowed None … 85.0); apogee_m=6.364245461805702 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.256719722382817 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.628024378713576 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=165.11213543272981 g (allowed None … 85.0); apogee_m=6.3494671196610195 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.250653997654913 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.786310135238118 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=167.66213543272983 g (allowed None … 99.0); apogee_m=22.654252838700977 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.962319999037028 m/s (allowed 12.0 … None); deployment_speed_m_s=12.85920004984111
  m/s (allowed None … 10.0); landing_descent_m_s=8.376025647256592 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=167.66213543272983 g (allowed None … 99.0); apogee_m=22.001284470812774 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.955636070496991 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=19.08478784961912 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=171.86213543272981 g (allowed None … 113.0); guide_departure_m_s=8.712309907054632 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=171.86213543272981 g (allowed None … 113.0); guide_departure_m_s=8.705986026196356 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=171.86213543272981 g (allowed None … 113.0); guide_departure_m_s=8.712309907054632 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.102349687220189 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=171.86213543272981 g (allowed None … 113.0); guide_departure_m_s=8.705986026196356 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.846187693146288 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=185.7621354327298 g (allowed None … 85.0); apogee_m=4.706895144995074 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.39127903498384 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.473809456055898 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=185.7621354327298 g (allowed None … 85.0); apogee_m=4.700559029172334 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.386267062158608 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.891931071295247 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=188.31213543272978 g (allowed None … 99.0); apogee_m=17.19897728069794 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.056401047682367 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.098389036132406 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=188.31213543272978 g (allowed None … 99.0); apogee_m=16.653042145063708 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.050659031918562 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.08399416657932 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.836301156739108 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.830729420698766 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.836301156739108 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.4658571213985 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.830729420698766 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.589171274683913 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.482461228060462 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=185.7621354327298 g (allowed None … 85.0); apogee_m=4.706895144995074 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.39127903498384 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.473809456055898 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=185.7621354327298 g (allowed None … 85.0); apogee_m=4.700559029172334 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.386267062158608 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.891931071295245 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=188.31213543272978 g (allowed None … 99.0); apogee_m=17.19897728069794 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.056401047682367 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.098389036132403 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=188.31213543272978 g (allowed None … 99.0); apogee_m=16.653042145063708 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.050659031918562 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.083994166579338 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.836301156739108 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.830729420698766 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.836301156739108 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.465857121398482 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=192.5121354327298 g (allowed None … 113.0); guide_departure_m_s=7.830729420698766 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.58917127468393 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.482461228060501 m/s (allowed None … 10.0)

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
