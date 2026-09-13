# Rocket Workbench report

Run: `conical-n70-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `4c1ab05eebfa3e797a5252a8d69edf129610351bd464dfd42b4f6b6e55a5ce7f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.05 |      6.58 |           2.43 | unavailable |       10.70 |    0.32 |            5.31 |             6.31 |              8.32 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.01 |      6.57 |           1.16 | unavailable |       10.02 |    0.30 |            5.31 |             6.31 |              8.29 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.73 |      8.29 |           2.36 |       15.85 |        5.35 |    0.16 |            7.13 |             8.13 |             16.99 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.91 |      8.28 |           1.30 |       20.22 |       17.97 |    9.70 |            7.12 |             8.12 |             16.75 |
| empty-C6-3-wind0  | completed / outside configured limits |    87.14 |      9.07 |           2.26 |        1.20 |        4.84 |    0.04 |            7.77 |             8.77 |             34.45 |
| empty-C6-3-wind2  | completed / outside configured limits |    83.10 |      9.06 |           1.62 |        6.28 |        4.84 |    5.24 |            7.76 |             8.76 |             34.29 |
| empty-C6-5-wind0  | completed / outside configured limits |    87.14 |      9.07 |           1.78 |       12.62 |        4.84 |    0.59 |            7.77 |             8.77 |             34.45 |
| empty-C6-5-wind2  | completed / outside configured limits |    83.10 |      9.06 |           1.62 |       19.19 |        4.84 |   13.98 |            7.76 |             8.76 |             34.29 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    70.88 |     13.16 |           2.15 |        4.82 |        4.85 |    0.00 |           11.74 |            12.74 |             26.46 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    69.11 |     13.15 |           1.67 |        5.95 |        4.85 |   10.59 |           11.73 |            12.73 |             26.30 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.18 |      5.66 |           2.92 | unavailable |        9.74 |    0.14 |            4.58 |             5.58 |              6.69 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.16 |      5.65 |           1.67 | unavailable |        9.22 |    0.28 |            4.58 |             5.58 |              6.67 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.71 |      7.33 |           2.82 | unavailable |       16.16 |    0.71 |            6.20 |             7.20 |             14.04 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.98 |      7.32 |           1.95 | unavailable |       18.01 |    8.02 |            6.20 |             7.20 |             13.79 |
| dummy-C6-3-wind0  | completed / outside configured limits |    69.45 |      8.13 |           2.69 |        2.46 |        5.16 |    0.03 |            6.79 |             7.79 |             29.20 |
| dummy-C6-3-wind2  | completed / outside configured limits |    65.01 |      8.13 |           2.08 |        7.91 |        5.16 |    6.42 |            6.78 |             7.78 |             29.09 |
| dummy-C6-5-wind0  | completed / outside configured limits |    69.45 |      8.13 |           2.69 |       17.43 |        5.16 |    1.19 |            6.79 |             7.79 |             29.20 |
| dummy-C6-5-wind2  | completed / outside configured limits |    65.01 |      8.13 |           2.08 |       22.79 |        5.16 |   29.37 |            6.78 |             7.78 |             29.09 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.70 |     12.41 |           2.59 |        8.34 |        5.16 |    0.15 |           10.32 |            11.32 |             21.95 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.70 |     12.41 |           2.29 |        9.70 |        5.16 |    0.22 |           10.31 |            11.31 |             21.80 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.18 |      5.66 |           2.92 | unavailable |        9.74 |    0.14 |            4.58 |             5.58 |              6.69 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.16 |      5.65 |           1.67 | unavailable |        9.22 |    0.28 |            4.58 |             5.58 |              6.67 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.71 |      7.33 |           2.82 | unavailable |       16.16 |    0.71 |            6.20 |             7.20 |             14.04 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.98 |      7.32 |           1.95 | unavailable |       18.01 |    8.02 |            6.20 |             7.20 |             13.79 |
| actual-C6-3-wind0 | completed / outside configured limits |    69.45 |      8.13 |           2.69 |        2.46 |        5.16 |    0.03 |            6.79 |             7.79 |             29.20 |
| actual-C6-3-wind2 | completed / outside configured limits |    65.01 |      8.13 |           2.08 |        7.91 |        5.16 |    6.42 |            6.78 |             7.78 |             29.09 |
| actual-C6-5-wind0 | completed / outside configured limits |    69.45 |      8.13 |           2.69 |       17.43 |        5.16 |    1.19 |            6.79 |             7.79 |             29.20 |
| actual-C6-5-wind2 | completed / outside configured limits |    65.01 |      8.13 |           2.08 |       22.79 |        5.16 |   29.37 |            6.78 |             7.78 |             29.09 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.70 |     12.41 |           2.59 |        8.34 |        5.16 |    0.15 |           10.32 |            11.32 |             21.95 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.70 |     12.41 |           2.29 |        9.70 |        5.16 |    0.22 |           10.31 |            11.31 |             21.80 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Recovery device deployment at high speed (20.2 m/s): "Nominal 457 mm parachute and lines"
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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.8 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (22.8 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=158.3757786261025 g (allowed None … 85.0); apogee_m=7.046318857558721 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.578886306191696 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.70317858504811 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=158.3757786261025 g (allowed None … 85.0); apogee_m=7.010990829589925 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.571702113520631 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.017350127751191 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=160.9257786261025 g (allowed None … 99.0); apogee_m=24.725137511615173 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.29254942068386 m/s (allowed 12.0 … None); deployment_speed_m_s=15.853601185618643 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=160.9257786261025 g (allowed None … 99.0); apogee_m=23.91030568519475 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.28482292061218 m/s (allowed 12.0 … None); deployment_speed_m_s=20.219840332622166 m/s
  (allowed None … 10.0); landing_descent_m_s=17.9659505853263 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=165.12577862610252 g (allowed None … 113.0); guide_departure_m_s=9.065203844099328 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=165.12577862610252 g (allowed None … 113.0); guide_departure_m_s=9.057813284771251 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=165.12577862610252 g (allowed None … 113.0); guide_departure_m_s=9.065203844099328 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.615490411691496 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=165.12577862610252 g (allowed None … 113.0); guide_departure_m_s=9.057813284771251 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.18865787965671 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=179.0257786261025 g (allowed None … 85.0); apogee_m=5.175318523196286 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.65545314329958 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.735276208111726 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=179.0257786261025 g (allowed None … 85.0); apogee_m=5.163756155609981 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.649594238377074 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.2213062310331 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=181.5757786261025 g (allowed None … 99.0); apogee_m=18.70767895467176 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.33139560835434 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.159957868360422 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=181.5757786261025 g (allowed None … 99.0); apogee_m=17.978851323992885 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.32472556344703 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=18.009962204395045 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.131735257885689 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.125236452946792 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.131735257885689 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.43174587099198 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.125236452946792 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.793301741210325 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=179.0257786261025 g (allowed None … 85.0); apogee_m=5.175318523196286 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.65545314329958 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.735276208111726 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=179.0257786261025 g (allowed None … 85.0); apogee_m=5.163756155609981 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.649594238377074 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.2213062310331 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=181.5757786261025 g (allowed None … 99.0); apogee_m=18.70767895467176 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.33139560835434 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.159957868360603 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=181.5757786261025 g (allowed None … 99.0); apogee_m=17.978851323992885 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.32472556344703 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.00996220439515 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.131735257885689 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.125236452946792 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.131735257885689 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.43174587099199 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=185.7757786261025 g (allowed None … 113.0); guide_departure_m_s=8.125236452946792 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.793301741210215 m/s (allowed None … 10.0)
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
