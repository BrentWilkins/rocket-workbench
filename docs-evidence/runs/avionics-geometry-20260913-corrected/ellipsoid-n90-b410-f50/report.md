# Rocket Workbench report

Run: `ellipsoid-n90-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `81d0314c39a578c9b5a31bca1ead49ce012ff7b34173129fa98c6bc9d3fd84ad`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.51 |      6.32 |           2.12 | unavailable |       10.65 |    0.23 |            5.11 |             6.11 |              7.87 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.50 |      6.32 |           0.86 | unavailable |        9.90 |    0.53 |            5.11 |             6.11 |              7.86 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.15 |      8.02 |           1.97 |       14.64 |        8.15 |    3.02 |            6.87 |             7.87 |             16.22 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.47 |      8.02 |           0.96 | unavailable |       19.08 |    9.15 |            6.87 |             7.87 |             15.99 |
| empty-C6-3-wind0  | completed / outside configured limits |    83.96 |      8.81 |           1.98 |        0.80 |        4.93 |    0.04 |            7.50 |             8.50 |             33.30 |
| empty-C6-3-wind2  | completed / outside configured limits |    80.20 |      8.80 |           1.30 |        6.19 |        4.92 |    4.41 |            7.49 |             8.49 |             33.15 |
| empty-C6-5-wind0  | completed / outside configured limits |    83.96 |      8.81 |           1.37 |       12.35 |        4.93 |    1.74 |            7.50 |             8.50 |             33.30 |
| empty-C6-5-wind2  | completed / outside configured limits |    80.20 |      8.80 |           1.30 |       19.58 |        4.92 |   14.83 |            7.49 |             8.49 |             33.15 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    67.76 |     12.94 |           1.24 |        5.38 |        4.93 |    0.01 |           11.35 |            12.35 |             25.50 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    65.99 |     12.93 |           1.31 |        6.42 |        4.93 |    8.45 |           11.35 |            12.34 |             25.34 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.81 |      5.45 |           2.57 | unavailable |        9.54 |    0.11 |            4.42 |             5.42 |              6.34 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.80 |      5.45 |           1.27 | unavailable |        8.96 |    0.41 |            4.42 |             5.42 |              6.33 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.55 |      7.11 |           2.51 | unavailable |       15.11 |    0.49 |            6.00 |             6.99 |             13.42 |
| dummy-B4-4-wind2  | completed / outside configured limits |    16.97 |      7.10 |           1.42 | unavailable |       17.35 |    6.78 |            5.99 |             6.99 |             13.21 |
| dummy-C6-3-wind0  | completed / outside configured limits |    66.49 |      7.92 |           1.97 |        3.01 |        5.23 |    0.02 |            6.57 |             7.57 |             28.20 |
| dummy-C6-3-wind2  | completed / outside configured limits |    62.35 |      7.91 |           1.67 |        8.05 |        5.23 |    6.96 |            6.57 |             7.57 |             28.10 |
| dummy-C6-5-wind0  | completed / outside configured limits |    66.49 |      7.92 |           1.97 |       17.05 |        5.23 |    0.66 |            6.57 |             7.57 |             28.20 |
| dummy-C6-5-wind2  | completed / outside configured limits |    62.35 |      7.91 |           1.67 |       23.37 |        5.23 |   30.02 |            6.57 |             7.57 |             28.10 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    53.02 |     12.16 |           1.65 |        8.95 |        5.24 |    0.17 |           10.01 |            11.01 |             21.09 |
| dummy-C5-3-wind2  | completed / outside configured limits |    51.07 |     12.16 |           1.89 |       10.25 |        5.24 |    1.80 |           10.00 |            11.00 |             20.97 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.81 |      5.45 |           2.57 | unavailable |        9.54 |    0.11 |            4.42 |             5.42 |              6.34 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.80 |      5.45 |           1.27 | unavailable |        8.96 |    0.41 |            4.42 |             5.42 |              6.33 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.55 |      7.11 |           2.51 | unavailable |       15.11 |    0.49 |            6.00 |             6.99 |             13.42 |
| actual-B4-4-wind2 | completed / outside configured limits |    16.97 |      7.10 |           1.42 | unavailable |       17.35 |    6.78 |            5.99 |             6.99 |             13.21 |
| actual-C6-3-wind0 | completed / outside configured limits |    66.49 |      7.92 |           1.97 |        3.01 |        5.23 |    0.02 |            6.57 |             7.57 |             28.20 |
| actual-C6-3-wind2 | completed / outside configured limits |    62.35 |      7.91 |           1.67 |        8.05 |        5.23 |    6.96 |            6.57 |             7.57 |             28.10 |
| actual-C6-5-wind0 | completed / outside configured limits |    66.49 |      7.92 |           1.97 |       17.05 |        5.23 |    0.66 |            6.57 |             7.57 |             28.20 |
| actual-C6-5-wind2 | completed / outside configured limits |    62.35 |      7.91 |           1.67 |       23.37 |        5.23 |   30.02 |            6.57 |             7.57 |             28.10 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    53.02 |     12.16 |           1.65 |        8.95 |        5.24 |    0.17 |           10.01 |            11.01 |             21.09 |
| actual-C5-3-wind2 | completed / outside configured limits |    51.07 |     12.16 |           1.89 |       10.25 |        5.24 |    1.80 |           10.00 |            11.00 |             20.97 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (21.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.4 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (21.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.4 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=163.61213543272976 g (allowed None … 85.0); apogee_m=6.512798851863312 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.324796203731917 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.647889200750765 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=163.61213543272976 g (allowed None … 85.0); apogee_m=6.4966356206432 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.3188347075743 m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.8566979360539511
  cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None … 10.0); landing_descent_m_s=9.895301781597386
  m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=166.16213543272977 g (allowed None … 99.0); apogee_m=23.147033245149974 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.024599562917592 m/s (allowed 12.0 … None);
  deployment_speed_m_s=14.644922560549599 m/s (allowed None … 10.0); landing_descent_m_s=8.151385465539455 m/s (allowed
  None … 6.0)
- empty-B4-4-wind2: launch_mass_g=166.16213543272977 g (allowed None … 99.0); apogee_m=22.46740121073963 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.01801157122287 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9626068636291388 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.07770344597171 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=170.36213543272976 g (allowed None … 113.0); guide_departure_m_s=8.810449315347013 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=170.36213543272976 g (allowed None … 113.0); guide_departure_m_s=8.804112510727093 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=170.36213543272976 g (allowed None … 113.0); guide_departure_m_s=8.810449315347013 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.350166868677254 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=170.36213543272976 g (allowed None … 113.0); guide_departure_m_s=8.804112510727093 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.575783726558157 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=184.26213543272976 g (allowed None … 85.0); apogee_m=4.80853101077131 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.450847338004991 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.542800199695833 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=184.26213543272976 g (allowed None … 85.0); apogee_m=4.801943864208694 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.445849188746297 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.959745028966436 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=186.81213543272975 g (allowed None … 99.0); apogee_m=17.547102259238702 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.1090770532733245 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.112185474344681 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=186.81213543272975 g (allowed None … 99.0); apogee_m=16.972239376913212 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.103405962492314 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.353763289211017 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.917799967633403 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.912302645650806 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.917799967633403 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.05137909241616 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.912302645650806 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.368401065639485 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.253427874440742 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=184.26213543272976 g (allowed None … 85.0); apogee_m=4.80853101077131 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.450847338004991 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.542800199695833 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=184.26213543272976 g (allowed None … 85.0); apogee_m=4.801943864208694 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.445849188746297 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.959745028966436 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=186.81213543272975 g (allowed None … 99.0); apogee_m=17.547102259238702 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.1090770532733245 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.112185474344681 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=186.81213543272975 g (allowed None … 99.0); apogee_m=16.972239376913407 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.103405962492314 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.35376328921023 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.917799967633403
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.912302645650806
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.917799967633403
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.05137909241618 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=191.01213543272976 g (allowed None … 113.0); guide_departure_m_s=7.912302645650806
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.368401065638917 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.253427874440803 m/s (allowed None … 10.0)

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
