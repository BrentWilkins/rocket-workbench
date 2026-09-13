# Rocket Workbench report

Run: `conical-n90-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `658e1ad2a5d784c422ed6049bf1d6f63afa7c5ad85bfc9a605b4c4387a45060b`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.08 |      6.59 |           2.04 | unavailable |       10.74 |    0.33 |            5.32 |             6.32 |              8.35 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.04 |      6.59 |           0.97 | unavailable |       10.03 |    0.34 |            5.32 |             6.32 |              8.32 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.88 |      8.31 |           2.06 |       12.35 |        4.49 |    1.42 |            7.14 |             8.14 |             17.04 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.07 |      8.30 |           1.11 |       20.10 |       15.00 |    9.95 |            7.14 |             8.14 |             16.81 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.10 |      9.03 |           1.99 |        1.47 |        4.84 |    0.04 |            7.78 |             8.78 |             34.64 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.04 |      9.03 |           1.40 |        6.39 |        4.84 |    5.41 |            7.78 |             8.78 |             34.48 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.11 |      9.03 |           1.29 |       11.97 |        4.84 |    1.03 |            7.78 |             8.78 |             34.64 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.04 |      9.03 |           1.40 |       19.02 |        4.84 |   13.85 |            7.78 |             8.78 |             34.48 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.57 |     13.18 |           1.25 |        4.60 |        4.85 |    0.00 |           11.76 |            12.76 |             26.63 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    69.80 |     13.17 |           1.46 |        5.80 |        4.85 |   10.85 |           11.76 |            12.75 |             26.47 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.20 |      5.67 |           2.62 | unavailable |        9.79 |    0.15 |            4.59 |             5.59 |              6.71 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.19 |      5.66 |           1.45 | unavailable |        9.20 |    0.27 |            4.59 |             5.59 |              6.69 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.80 |      7.34 |           2.57 | unavailable |       16.16 |    0.57 |            6.21 |             7.21 |             14.08 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.07 |      7.34 |           1.70 | unavailable |       18.09 |    8.20 |            6.21 |             7.21 |             13.84 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.06 |      8.15 |           2.39 |        2.27 |        5.15 |    0.03 |            6.80 |             7.80 |             29.34 |
| dummy-C6-3-wind2  | completed / outside configured limits |    65.59 |      8.14 |           1.83 |        7.90 |        5.15 |    6.41 |            6.80 |             7.79 |             29.23 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.06 |      8.15 |           2.39 |       17.25 |        5.15 |    0.94 |            6.80 |             7.80 |             29.34 |
| dummy-C6-5-wind2  | completed / outside configured limits |    65.59 |      8.14 |           1.83 |       22.72 |        5.15 |   29.45 |            6.80 |             7.79 |             29.23 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.13 |     12.43 |           1.78 |        8.20 |        5.16 |    0.14 |           10.33 |            11.33 |             22.07 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.13 |     12.43 |           2.02 |        9.59 |        5.16 |    0.13 |           10.33 |            11.33 |             21.92 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.20 |      5.67 |           2.62 | unavailable |        9.79 |    0.15 |            4.59 |             5.59 |              6.71 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.19 |      5.66 |           1.45 | unavailable |        9.20 |    0.27 |            4.59 |             5.59 |              6.69 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.80 |      7.34 |           2.57 | unavailable |       16.16 |    0.57 |            6.21 |             7.21 |             14.08 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.07 |      7.34 |           1.70 | unavailable |       18.09 |    8.20 |            6.21 |             7.21 |             13.84 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.06 |      8.15 |           2.39 |        2.27 |        5.15 |    0.03 |            6.80 |             7.80 |             29.34 |
| actual-C6-3-wind2 | completed / outside configured limits |    65.59 |      8.14 |           1.83 |        7.90 |        5.15 |    6.41 |            6.80 |             7.79 |             29.23 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.06 |      8.15 |           2.39 |       17.25 |        5.15 |    0.94 |            6.80 |             7.80 |             29.34 |
| actual-C6-5-wind2 | completed / outside configured limits |    65.59 |      8.14 |           1.83 |       22.72 |        5.15 |   29.45 |            6.80 |             7.79 |             29.23 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.13 |     12.43 |           1.78 |        8.20 |        5.16 |    0.14 |           10.33 |            11.33 |             22.07 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.13 |     12.43 |           2.02 |        9.59 |        5.16 |    0.13 |           10.33 |            11.33 |             21.92 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: Recovery device deployment at high speed (20.1 m/s): "Nominal 457 mm parachute and lines"
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
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.7 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=158.13514007668752 g (allowed None … 85.0); apogee_m=7.0787815599120165 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.593874155162081 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.738946061266963 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=158.13514007668752 g (allowed None … 85.0); apogee_m=7.044393028043249 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.586978319503889 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9703174652205208 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.02572587049057 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=160.68514007668753 g (allowed None … 99.0); apogee_m=24.8770222021896 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.309209507908093 m/s (allowed 12.0 … None); deployment_speed_m_s=12.346193912123555 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=160.68514007668753 g (allowed None … 99.0); apogee_m=24.06855242417297 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.301803229290288 m/s (allowed 12.0 … None); deployment_speed_m_s=20.098807783688734 m/s
  (allowed None … 10.0); landing_descent_m_s=14.998825973325726 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=164.88514007668752 g (allowed None … 113.0); guide_departure_m_s=9.032874950644722 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=164.88514007668752 g (allowed None … 113.0); guide_departure_m_s=9.025960710272477 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=164.88514007668752 g (allowed None … 113.0); guide_departure_m_s=9.032874950644722 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.97259944777454 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=164.88514007668752 g (allowed None … 113.0); guide_departure_m_s=9.025960710272477 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.024821020151304 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=178.78514007668753 g (allowed None … 85.0); apogee_m=5.196061013460806 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.667651801986318 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.786147893033823 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=178.78514007668753 g (allowed None … 85.0); apogee_m=5.185103561195007 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.662027946832035 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.197489077676922 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=181.33514007668754 g (allowed None … 99.0); apogee_m=18.801481664953858 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.344990732564891 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.160435606219725 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=181.33514007668754 g (allowed None … 99.0); apogee_m=18.067400599085698 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.338596366235426 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.09445774721327 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.146110682556689 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.14004079269623 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.146110682556689 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.247360190525477 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.14004079269623 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.72078690152877 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=178.78514007668753 g (allowed None … 85.0); apogee_m=5.196061013460806 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.667651801986318 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.786147893033823 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=178.78514007668753 g (allowed None … 85.0); apogee_m=5.185103561195007 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.662027946832035 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.197489077676922 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=181.33514007668754 g (allowed None … 99.0); apogee_m=18.801481664953858 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.344990732564891 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=16.16043560621972 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=181.33514007668754 g (allowed None … 99.0); apogee_m=18.067400599085698 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.338596366235426 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.09445774721327 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.146110682556689
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.14004079269623 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.146110682556689
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.247360190525463 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=185.53514007668753 g (allowed None … 113.0); guide_departure_m_s=8.14004079269623 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.720786901528825 m/s (allowed None … 10.0)
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
