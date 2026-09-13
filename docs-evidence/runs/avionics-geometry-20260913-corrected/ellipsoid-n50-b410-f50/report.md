# Rocket Workbench report

Run: `ellipsoid-n50-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `f0550c7f1c838f5a1e62bedd2dc47d64be3e028010e8084d10340557fe2896b8`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.04 |      6.57 |           2.05 | unavailable |       10.86 |    0.29 |            5.31 |             6.30 |              8.31 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.01 |      6.56 |           0.93 | unavailable |       10.13 |    0.39 |            5.30 |             6.30 |              8.29 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.85 |      8.28 |           1.98 |       12.62 |        4.87 |    1.59 |            7.12 |             8.12 |             17.01 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.07 |      8.28 |           1.02 |       19.94 |       14.74 |    9.72 |            7.12 |             8.11 |             16.78 |
| empty-C6-3-wind0  | completed / outside configured limits |    89.06 |      9.05 |           1.89 |        1.83 |        4.85 |    0.04 |            7.76 |             8.76 |             34.74 |
| empty-C6-3-wind2  | completed / outside configured limits |    85.12 |      9.05 |           1.31 |        6.40 |        4.85 |    6.27 |            7.75 |             8.75 |             34.58 |
| empty-C6-5-wind0  | completed / outside configured limits |    89.08 |      9.05 |           1.72 |       12.09 |        4.85 |    1.05 |            7.76 |             8.76 |             34.74 |
| empty-C6-5-wind2  | completed / outside configured limits |    85.13 |      9.05 |           1.31 |       18.78 |        4.85 |   12.65 |            7.75 |             8.75 |             34.58 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    72.12 |     13.14 |           1.63 |        4.37 |        4.85 |    0.01 |           11.73 |            12.73 |             26.74 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    70.34 |     13.14 |           1.39 |        5.72 |        4.85 |   10.87 |           11.73 |            12.72 |             26.57 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.17 |      5.66 |           2.48 | unavailable |        9.80 |    0.13 |            4.57 |             5.57 |              6.68 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.16 |      5.65 |           1.39 | unavailable |        9.26 |    0.31 |            4.57 |             5.57 |              6.67 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.75 |      7.32 |           2.45 | unavailable |       16.03 |    0.58 |            6.19 |             7.19 |             14.05 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.08 |      7.32 |           1.62 | unavailable |       18.10 |    7.67 |            6.19 |             7.19 |             13.82 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.51 |      8.12 |           1.55 |        2.06 |        5.16 |    0.03 |            6.78 |             7.78 |             29.38 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.17 |      8.12 |           1.73 |        7.76 |        5.16 |    5.74 |            6.78 |             7.78 |             29.27 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.51 |      8.12 |           1.55 |       16.88 |        5.16 |    1.11 |            6.78 |             7.78 |             29.38 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.17 |      8.12 |           1.73 |       22.63 |        5.16 |   28.58 |            6.78 |             7.78 |             29.27 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.35 |     12.40 |           2.04 |        8.11 |        5.17 |    0.11 |           10.31 |            11.31 |             22.11 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.37 |     12.39 |           1.91 |        9.51 |        5.17 |    0.00 |           10.30 |            11.30 |             21.98 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.17 |      5.66 |           2.48 | unavailable |        9.80 |    0.13 |            4.57 |             5.57 |              6.68 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.16 |      5.65 |           1.39 | unavailable |        9.26 |    0.31 |            4.57 |             5.57 |              6.67 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.75 |      7.32 |           2.45 | unavailable |       16.03 |    0.58 |            6.19 |             7.19 |             14.05 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.08 |      7.32 |           1.62 | unavailable |       18.10 |    7.67 |            6.19 |             7.19 |             13.82 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.51 |      8.12 |           1.55 |        2.06 |        5.16 |    0.03 |            6.78 |             7.78 |             29.38 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.17 |      8.12 |           1.73 |        7.76 |        5.16 |    5.74 |            6.78 |             7.78 |             29.27 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.51 |      8.12 |           1.55 |       16.88 |        5.16 |    1.11 |            6.78 |             7.78 |             29.38 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.17 |      8.12 |           1.73 |       22.63 |        5.16 |   28.58 |            6.78 |             7.78 |             29.27 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.35 |     12.40 |           2.04 |        8.11 |        5.17 |    0.11 |           10.31 |            11.31 |             22.11 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.37 |     12.39 |           1.91 |        9.51 |        5.17 |    0.00 |           10.30 |            11.30 |             21.98 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (16.7°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.6 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (16.7°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.6 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=158.57604645749495 g (allowed None … 85.0); apogee_m=7.0408797670376995 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.5691341165209725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=10.85556875001329 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=158.57604645749495 g (allowed None … 85.0); apogee_m=7.014809067768132 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.5628653218969335 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9296215968094794 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.126048522045073 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=161.12604645749497 g (allowed None … 99.0); apogee_m=24.85043981287873 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.281973473764573 m/s (allowed 12.0 … None); deployment_speed_m_s=12.619644011117813 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=161.12604645749497 g (allowed None … 99.0); apogee_m=24.071797752874282 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.275235447099238 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.939749625706167 m/s (allowed None … 10.0); landing_descent_m_s=14.743075275478244 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=165.32604645749495 g (allowed None … 113.0); guide_departure_m_s=9.053904763567703 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=165.32604645749495 g (allowed None … 113.0); guide_departure_m_s=9.047461333629565 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=165.32604645749495 g (allowed None … 113.0); guide_departure_m_s=9.053904763567703 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.091189914476203 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=165.32604645749495 g (allowed None … 113.0); guide_departure_m_s=9.047461333629565 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.779935643232793 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=179.22604645749496 g (allowed None … 85.0); apogee_m=5.168088325886742 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.658219401648833 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.796828861135728 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=179.22604645749496 g (allowed None … 85.0); apogee_m=5.159210579776767 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.653023471314419 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.26247254290279 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=181.77604645749494 g (allowed None … 99.0); apogee_m=18.7549604138536 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.32270242480156 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.028457354097945 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=181.77604645749494 g (allowed None … 99.0); apogee_m=18.077865829632515 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.316880729605326 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.097984427196756 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.122366181719118 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.11668736575772 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.122366181719118 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.88043431359313 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.11668736575772 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.63475646801794 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=179.22604645749496 g (allowed None … 85.0); apogee_m=5.168088325886742 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.658219401648833 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.796828861135728 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=179.22604645749496 g (allowed None … 85.0); apogee_m=5.159210579776767 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.653023471314419 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.26247254290279 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=181.77604645749494 g (allowed None … 99.0); apogee_m=18.7549604138536 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.32270242480156 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=16.02845735409795 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=181.77604645749494 g (allowed None … 99.0); apogee_m=18.077865829632525 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.316880729605326 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=18.097984427196767 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.122366181719118
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.11668736575772 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.122366181719118
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.880434313593142 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=185.97604645749496 g (allowed None … 113.0); guide_departure_m_s=8.11668736575772 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.634756468017958 m/s (allowed None … 10.0)
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
