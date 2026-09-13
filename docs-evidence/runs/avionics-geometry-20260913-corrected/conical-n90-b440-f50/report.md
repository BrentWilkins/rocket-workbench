# Rocket Workbench report

Run: `conical-n90-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `3d8fe9065e660ba1d5987e17dd6ccdf505d048375d8611d8e07664fc01c16e2f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     7.07 |      6.59 |           2.29 | unavailable |       10.89 |    0.29 |            5.32 |             6.32 |              8.34 |
| empty-A8-3-wind2  | completed / outside configured limits |     7.04 |      6.58 |           0.98 | unavailable |       10.10 |    0.51 |            5.31 |             6.31 |              8.31 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.86 |      8.30 |           2.19 |       12.56 |        4.86 |    2.17 |            7.13 |             8.13 |             17.03 |
| empty-B4-4-wind2  | completed / outside configured limits |    24.13 |      8.29 |           1.04 |       19.32 |       10.72 |    9.55 |            7.13 |             8.13 |             16.81 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.28 |      9.03 |           2.12 |        1.54 |        4.84 |    0.04 |            7.78 |             8.77 |             34.65 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.54 |      9.07 |           1.43 |        6.08 |        4.84 |    7.04 |            7.77 |             8.77 |             34.49 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.29 |      9.03 |           1.94 |       11.99 |        4.84 |    1.33 |            7.78 |             8.77 |             34.65 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.55 |      9.07 |           1.43 |       18.76 |        4.84 |   11.39 |            7.77 |             8.77 |             34.49 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.67 |     13.17 |           1.83 |        4.56 |        4.85 |    0.01 |           11.76 |            12.76 |             26.65 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    69.94 |     13.16 |           1.42 |        5.65 |        4.85 |   11.22 |           11.75 |            12.75 |             26.48 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.19 |      5.66 |           2.79 | unavailable |        9.80 |    0.13 |            4.58 |             5.58 |              6.70 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.18 |      5.66 |           1.48 | unavailable |        9.20 |    0.38 |            4.58 |             5.58 |              6.69 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.79 |      7.34 |           2.74 | unavailable |       15.90 |    0.56 |            6.20 |             7.20 |             14.07 |
| dummy-B4-4-wind2  | completed / outside configured limits |    18.15 |      7.33 |           1.68 | unavailable |       18.00 |    7.42 |            6.20 |             7.20 |             13.85 |
| dummy-C6-3-wind0  | completed / outside configured limits |    70.14 |      8.14 |           2.19 |        2.23 |        5.16 |    0.03 |            6.79 |             7.79 |             29.34 |
| dummy-C6-3-wind2  | completed / outside configured limits |    66.00 |      8.13 |           1.88 |        7.54 |        5.16 |    4.82 |            6.79 |             7.79 |             29.23 |
| dummy-C6-5-wind0  | completed / outside configured limits |    70.14 |      8.14 |           2.19 |       16.72 |        5.16 |    0.89 |            6.79 |             7.79 |             29.34 |
| dummy-C6-5-wind2  | completed / outside configured limits |    66.00 |      8.13 |           1.88 |       22.53 |        5.16 |   27.14 |            6.79 |             7.79 |             29.23 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    56.16 |     12.42 |           2.21 |        8.20 |        5.16 |    0.12 |           10.33 |            11.33 |             22.07 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    54.25 |     12.42 |           2.10 |        9.43 |        5.16 |    0.46 |           10.32 |            11.32 |             21.93 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.19 |      5.66 |           2.79 | unavailable |        9.80 |    0.13 |            4.58 |             5.58 |              6.70 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.18 |      5.66 |           1.48 | unavailable |        9.20 |    0.38 |            4.58 |             5.58 |              6.69 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.79 |      7.34 |           2.74 | unavailable |       15.90 |    0.56 |            6.20 |             7.20 |             14.07 |
| actual-B4-4-wind2 | completed / outside configured limits |    18.15 |      7.33 |           1.68 | unavailable |       18.00 |    7.42 |            6.20 |             7.20 |             13.85 |
| actual-C6-3-wind0 | completed / outside configured limits |    70.14 |      8.14 |           2.19 |        2.23 |        5.16 |    0.03 |            6.79 |             7.79 |             29.34 |
| actual-C6-3-wind2 | completed / outside configured limits |    66.00 |      8.13 |           1.88 |        7.54 |        5.16 |    4.82 |            6.79 |             7.79 |             29.23 |
| actual-C6-5-wind0 | completed / outside configured limits |    70.14 |      8.14 |           2.19 |       16.72 |        5.16 |    0.89 |            6.79 |             7.79 |             29.34 |
| actual-C6-5-wind2 | completed / outside configured limits |    66.00 |      8.13 |           1.88 |       22.53 |        5.16 |   27.14 |            6.79 |             7.79 |             29.23 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    56.16 |     12.42 |           2.21 |        8.20 |        5.16 |    0.12 |           10.33 |            11.33 |             22.07 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    54.25 |     12.42 |           2.10 |        9.43 |        5.16 |    0.46 |           10.32 |            11.32 |             21.93 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (18°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (22.5 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (18°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (22.5 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=158.25131732789296 g (allowed None … 85.0); apogee_m=7.068201344004508 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.587266733891551 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.890119091035745 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=158.25131732789296 g (allowed None … 85.0); apogee_m=7.043033803088997 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.580504409809387 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9832344376611513 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.095811509203049 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=160.80131732789297 g (allowed None … 99.0); apogee_m=24.863577035742612 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.301930938767612 m/s (allowed 12.0 … None);
  deployment_speed_m_s=12.555472162805208 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=160.80131732789297 g (allowed None … 99.0); apogee_m=24.128417136169542 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.29466696840111 m/s (allowed 12.0 … None); deployment_speed_m_s=19.318372399921184
  m/s (allowed None … 10.0); landing_descent_m_s=10.717997214419034 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=165.00131732789296 g (allowed None … 113.0); guide_departure_m_s=9.02520509225089 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=165.00131732789296 g (allowed None … 113.0); guide_departure_m_s=9.06813987708695 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=165.00131732789296 g (allowed None … 113.0); guide_departure_m_s=9.02520509225089 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.993630364618301 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=165.00131732789296 g (allowed None … 113.0); guide_departure_m_s=9.06813987708695 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.75823513325232 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=178.90131732789297 g (allowed None … 85.0); apogee_m=5.188374766305241 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.662249803651835 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.795957012678752 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=178.90131732789297 g (allowed None … 85.0); apogee_m=5.178798789558844 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.656733403941229 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.202809748373577 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=181.45131732789295 g (allowed None … 99.0); apogee_m=18.786118269467792 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.339035875057661 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.896551638484818 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=181.45131732789295 g (allowed None … 99.0); apogee_m=18.15309923002129 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.332763230242038 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.995320120429533 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.139821472040909 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.133774591441838 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.139821472040909 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.718418403672725 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.133774591441838 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.526649390008952 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=178.90131732789297 g (allowed None … 85.0); apogee_m=5.188374766305241 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.662249803651835 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.795957012678752 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=178.90131732789297 g (allowed None … 85.0); apogee_m=5.178798789558844 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.656733403941229 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.202809748373577 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=181.45131732789295 g (allowed None … 99.0); apogee_m=18.786118269467792 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.339035875057661 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.896551638484816 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=181.45131732789295 g (allowed None … 99.0); apogee_m=18.15309923002129 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.332763230242038 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.995320120429614 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.139821472040909
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.133774591441838
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.139821472040909
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.71841840367273 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=185.65131732789297 g (allowed None … 113.0); guide_departure_m_s=8.133774591441838
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.52664939000905 m/s (allowed None … 10.0)
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
