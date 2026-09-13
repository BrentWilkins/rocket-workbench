# Rocket Workbench report

Run: `ogive-n90-b440-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `dc95505c4706b1aadaf998c5762f6936dc4afa66af39bca03d4ff2d2c8e82ac0`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.76 |      6.44 |           2.16 | unavailable |       10.96 |    0.23 |            5.20 |             6.20 |              8.08 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.74 |      6.44 |           0.81 | unavailable |       10.15 |    0.69 |            5.20 |             6.20 |              8.06 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.96 |      8.14 |           1.45 |       14.55 |        6.00 |    3.45 |            6.99 |             7.98 |             16.60 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.37 |      8.14 |           0.89 |       12.78 |        5.02 |    7.43 |            6.98 |             7.98 |             16.39 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.60 |      8.92 |           2.00 |        1.37 |        4.89 |    0.04 |            7.62 |             8.62 |             34.02 |
| empty-C6-3-wind2  | completed / outside configured limits |    83.19 |      8.92 |           1.25 |        5.84 |        4.89 |    7.48 |            7.62 |             8.62 |             33.86 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.61 |      8.92 |           0.96 |       12.49 |        4.89 |    1.81 |            7.62 |             8.62 |             34.02 |
| empty-C6-5-wind2  | completed / outside configured limits |    83.19 |      8.92 |           1.25 |       18.77 |        4.89 |   10.47 |            7.62 |             8.62 |             33.86 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    69.96 |     13.00 |           1.71 |        4.85 |        4.90 |    0.01 |           11.53 |            12.53 |             26.12 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.30 |     13.00 |           1.18 |        5.77 |        4.90 |   10.44 |           11.52 |            12.52 |             25.96 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.98 |      5.54 |           2.63 | unavailable |        9.70 |    0.10 |            4.49 |             5.49 |              6.50 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.97 |      5.54 |           1.29 | unavailable |        9.11 |    0.48 |            4.49 |             5.49 |              6.49 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.12 |      7.21 |           2.56 | unavailable |       14.91 |    0.64 |            6.09 |             7.09 |             13.72 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.62 |      7.20 |           1.32 | unavailable |       17.39 |    6.33 |            6.09 |             7.09 |             13.53 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.51 |      8.01 |           2.09 |        2.51 |        5.20 |    0.03 |            6.67 |             7.67 |             28.78 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.68 |      8.01 |           1.67 |        7.42 |        5.20 |    4.36 |            6.67 |             7.67 |             28.66 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.51 |      8.01 |           2.09 |       16.33 |        5.20 |    0.50 |            6.67 |             7.67 |             28.78 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.68 |      8.01 |           1.67 |       22.74 |        5.20 |   26.36 |            6.67 |             7.67 |             28.66 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.66 |     12.19 |           2.33 |        8.55 |        5.21 |    0.12 |           10.15 |            11.15 |             21.60 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    52.79 |     12.19 |           1.81 |        9.66 |        5.21 |    0.33 |           10.14 |            11.14 |             21.46 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.98 |      5.54 |           2.63 | unavailable |        9.70 |    0.10 |            4.49 |             5.49 |              6.50 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.97 |      5.54 |           1.29 | unavailable |        9.11 |    0.48 |            4.49 |             5.49 |              6.49 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.12 |      7.21 |           2.56 | unavailable |       14.91 |    0.64 |            6.09 |             7.09 |             13.72 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.62 |      7.20 |           1.32 | unavailable |       17.39 |    6.33 |            6.09 |             7.09 |             13.53 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.51 |      8.01 |           2.09 |        2.51 |        5.20 |    0.03 |            6.67 |             7.67 |             28.78 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.68 |      8.01 |           1.67 |        7.42 |        5.20 |    4.36 |            6.67 |             7.67 |             28.66 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.51 |      8.01 |           2.09 |       16.33 |        5.20 |    0.50 |            6.67 |             7.67 |             28.78 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.68 |      8.01 |           1.67 |       22.74 |        5.20 |   26.36 |            6.67 |             7.67 |             28.66 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.66 |     12.19 |           2.33 |        8.55 |        5.21 |    0.12 |           10.15 |            11.15 |             21.60 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    52.79 |     12.19 |           1.81 |        9.66 |        5.21 |    0.33 |           10.14 |            11.14 |             21.46 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (24.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.7 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (24.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.7 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=161.2151753916149 g (allowed None … 85.0); apogee_m=6.75942072176416 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.444987624946647 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=10.955505489450529 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=161.2151753916149 g (allowed None … 85.0); apogee_m=6.743958753486438 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.438913257687065 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8147960311405705 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.14616488564595 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=163.7651753916149 g (allowed None … 99.0); apogee_m=23.96093539765869 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.144204680316363 m/s (allowed 12.0 … None); deployment_speed_m_s=14.547782251224197 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=163.7651753916149 g (allowed None … 99.0); apogee_m=23.365758205628868 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.137666905966375 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.887572654399763 cal (allowed 1.0 … None); deployment_speed_m_s=12.783959253423067 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=167.9651753916149 g (allowed None … 113.0); guide_departure_m_s=8.922964666936283 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=167.9651753916149 g (allowed None … 113.0); guide_departure_m_s=8.916686482658541 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=167.9651753916149 g (allowed None … 113.0); guide_departure_m_s=8.922964666936283 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.9596698039783859 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.48685057648628 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=167.9651753916149 g (allowed None … 113.0); guide_departure_m_s=8.916686482658541 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.77476461914488 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=181.86517539161488 g (allowed None … 85.0); apogee_m=4.9764429019328205 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.543078552773852 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.703285621955594 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=181.86517539161488 g (allowed None … 85.0); apogee_m=4.968814868844067 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.538115299776047 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.109202807831881 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=184.4151753916149 g (allowed None … 99.0); apogee_m=18.120673118473917 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.208686846088555 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=14.910265870937806 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=184.4151753916149 g (allowed None … 99.0); apogee_m=17.616312220384607 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.203045072240377 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.38970820043814 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.01256935603823 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.00703611489636 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.01256935603823 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.329917881154408 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.00703611489636 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.7350820845931 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=181.86517539161488 g (allowed None … 85.0); apogee_m=4.9764429019328205 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.543078552773852 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.703285621955594 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=181.86517539161488 g (allowed None … 85.0); apogee_m=4.968814868844067 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.538115299776047 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.109202807831881 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=184.4151753916149 g (allowed None … 99.0); apogee_m=18.120673118473917 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.208686846088555 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=14.910265870937817 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=184.4151753916149 g (allowed None … 99.0); apogee_m=17.616312220384607 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.203045072240377 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.38970820043814 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.01256935603823 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.00703611489636 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.01256935603823 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.329917881154408 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=188.6151753916149 g (allowed None … 113.0); guide_departure_m_s=8.00703611489636 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.735082084593017 m/s (allowed None … 10.0)
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
