# Rocket Workbench report

Run: `ellipsoid-n70-b410-f45`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `ef394c374b4ecabd18cb49609bd9cfa69841d9e11dcbf6e65304b6320d1a1061`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.92 |      6.52 |           1.89 | unavailable |       11.01 |    0.25 |            5.26 |             6.26 |              8.21 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.90 |      6.51 |           0.72 | unavailable |       10.27 |    0.65 |            5.26 |             6.26 |              8.19 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.50 |      8.21 |           1.73 |       15.36 |        5.47 |    3.61 |            7.06 |             8.06 |             16.84 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.86 |      8.20 |           0.79 |       15.46 |        5.30 |    6.31 |            7.06 |             8.06 |             16.63 |
| empty-C6-3-wind0  | completed / outside configured limits |    88.39 |      8.98 |           1.73 |        1.76 |        4.86 |    0.04 |            7.70 |             8.70 |             34.49 |
| empty-C6-3-wind2  | completed / outside configured limits |    84.89 |      8.97 |           1.10 |        5.98 |        4.86 |    7.97 |            7.69 |             8.69 |             34.33 |
| empty-C6-5-wind0  | completed / outside configured limits |    88.41 |      8.98 |           0.77 |       12.66 |        4.86 |    1.73 |            7.70 |             8.70 |             34.49 |
| empty-C6-5-wind2  | completed / outside configured limits |    84.90 |      8.97 |           1.10 |       18.55 |        4.86 |    9.98 |            7.69 |             8.69 |             34.33 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    71.44 |     13.04 |           1.27 |        4.49 |        4.87 |    0.01 |           11.65 |            12.65 |             26.53 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    69.75 |     13.03 |           1.04 |        5.57 |        4.87 |   11.10 |           11.64 |            12.64 |             26.37 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.09 |      5.60 |           2.33 | unavailable |        9.77 |    0.10 |            4.54 |             5.54 |              6.61 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.08 |      5.60 |           1.16 | unavailable |        9.16 |    0.43 |            4.54 |             5.54 |              6.59 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.50 |      7.29 |           2.25 | unavailable |       15.28 |    0.53 |            6.15 |             7.14 |             13.91 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.95 |      7.28 |           1.23 | unavailable |       17.65 |    6.61 |            6.14 |             7.14 |             13.71 |
| dummy-C6-3-wind0  | completed / outside configured limits |    69.87 |      8.06 |           2.06 |        2.18 |        5.18 |    0.03 |            6.73 |             7.73 |             29.16 |
| dummy-C6-3-wind2  | completed / outside configured limits |    65.92 |      8.05 |           1.50 |        7.40 |        5.18 |    4.25 |            6.73 |             7.73 |             29.04 |
| dummy-C6-5-wind0  | completed / outside configured limits |    69.87 |      8.06 |           2.06 |       16.21 |        5.18 |    0.35 |            6.73 |             7.73 |             29.16 |
| dummy-C6-5-wind2  | completed / outside configured limits |    65.92 |      8.05 |           1.50 |       22.55 |        5.18 |   26.35 |            6.73 |             7.73 |             29.04 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    55.76 |     12.31 |           2.10 |        8.26 |        5.18 |    0.10 |           10.24 |            11.24 |             21.93 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    53.86 |     12.30 |           1.64 |        9.44 |        5.18 |    0.19 |           10.23 |            11.23 |             21.79 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.09 |      5.60 |           2.33 | unavailable |        9.77 |    0.10 |            4.54 |             5.54 |              6.61 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.08 |      5.60 |           1.16 | unavailable |        9.16 |    0.43 |            4.54 |             5.54 |              6.59 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.50 |      7.29 |           2.25 | unavailable |       15.28 |    0.53 |            6.15 |             7.14 |             13.91 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.95 |      7.28 |           1.23 | unavailable |       17.65 |    6.61 |            6.14 |             7.14 |             13.71 |
| actual-C6-3-wind0 | completed / outside configured limits |    69.87 |      8.06 |           2.06 |        2.18 |        5.18 |    0.03 |            6.73 |             7.73 |             29.16 |
| actual-C6-3-wind2 | completed / outside configured limits |    65.92 |      8.05 |           1.50 |        7.40 |        5.18 |    4.25 |            6.73 |             7.73 |             29.04 |
| actual-C6-5-wind0 | completed / outside configured limits |    69.87 |      8.06 |           2.06 |       16.21 |        5.18 |    0.35 |            6.73 |             7.73 |             29.16 |
| actual-C6-5-wind2 | completed / outside configured limits |    65.92 |      8.05 |           1.50 |       22.55 |        5.18 |   26.35 |            6.73 |             7.73 |             29.04 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    55.76 |     12.31 |           2.10 |        8.26 |        5.18 |    0.10 |           10.24 |            11.24 |             21.93 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    53.86 |     12.30 |           1.64 |        9.44 |        5.18 |    0.19 |           10.23 |            11.23 |             21.79 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (22.4°); Flight Event occurred after landing: Ejection charge;
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
- actual-A8-3-wind2: Large angle of attack encountered (22.4°); Flight Event occurred after landing: Ejection charge;
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

- empty-A8-3-wind0: launch_mass_g=159.71033145527215 g (allowed None … 85.0); apogee_m=6.921111813951336 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.515804997833072 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.014873870394329 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=159.71033145527215 g (allowed None … 85.0); apogee_m=6.9041576711594 m (allowed 30.0 …
  120.0); guide_departure_m_s=6.509785552213209 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7180238610726043 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.271151041714186 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=162.26033145527217 g (allowed None … 99.0); apogee_m=24.497513690442478 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.209014589716965 m/s (allowed 12.0 … None); deployment_speed_m_s=15.36327927677906
  m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=162.26033145527217 g (allowed None … 99.0); apogee_m=23.860858583835586 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.202594149696953 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7925531916084669 cal (allowed 1.0 … None); deployment_speed_m_s=15.463667988866236 m/s
  (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=166.46033145527218 g (allowed None … 113.0); guide_departure_m_s=8.976618996867987 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=166.46033145527218 g (allowed None … 113.0); guide_departure_m_s=8.97047286965133 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=166.46033145527218 g (allowed None … 113.0); guide_departure_m_s=8.976618996867987 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.7661956987552604 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.659667877058608 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=166.46033145527218 g (allowed None … 113.0); guide_departure_m_s=8.97047286965133 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.545786657928495 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=180.36033145527216 g (allowed None … 85.0); apogee_m=5.085944781220878 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.604183071591719 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.7680145303918 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=180.36033145527216 g (allowed None … 85.0); apogee_m=5.078127736628248 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.599252787290451 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.162723009468117 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=182.91033145527217 g (allowed None … 99.0); apogee_m=18.49612408014643 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.287939268773912 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.281372119102501 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=182.91033145527217 g (allowed None … 99.0); apogee_m=17.9546988308214 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.282286470535454 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.647789215518188 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.058424269895648 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.053002259059976 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.058424269895648 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.209958718131773 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.053002259059976 m/s
  (allowed 12.0 … None); deployment_speed_m_s=22.554761788705868 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=180.36033145527216 g (allowed None … 85.0); apogee_m=5.085944781220878 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.604183071591719 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.7680145303918 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=180.36033145527216 g (allowed None … 85.0); apogee_m=5.078127736628248 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.599252787290451 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.162723009468117 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=182.91033145527217 g (allowed None … 99.0); apogee_m=18.49612408014643 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.287939268773912 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.2813721191025 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=182.91033145527217 g (allowed None … 99.0); apogee_m=17.9546988308214 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.282286470535454 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.647789215518188 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.058424269895648
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.053002259059976
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.058424269895648
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.209958718131777 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=187.11033145527216 g (allowed None … 113.0); guide_departure_m_s=8.053002259059976
  m/s (allowed 12.0 … None); deployment_speed_m_s=22.554761788705857 m/s (allowed None … 10.0)
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
