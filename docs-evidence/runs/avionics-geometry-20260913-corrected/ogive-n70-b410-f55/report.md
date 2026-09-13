# Rocket Workbench report

Run: `ogive-n70-b410-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `c828f071d7f276a5624bf07eb7251473bae59dbf311e31d2cbb4b234d181171a`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.83 |      6.47 |           2.21 | unavailable |       10.62 |    0.30 |            5.23 |             6.23 |              8.14 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.80 |      6.46 |           1.04 | unavailable |        9.95 |    0.30 |            5.23 |             6.22 |              8.11 |
| empty-B4-4-wind0  | completed / outside configured limits |    24.13 |      8.19 |           2.11 |       13.72 |        5.36 |    0.15 |            7.02 |             8.02 |             16.68 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.32 |      8.18 |           1.17 | unavailable |       20.11 |    9.79 |            7.02 |             8.02 |             16.45 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.53 |      8.92 |           2.05 |        1.26 |        4.88 |    0.04 |            7.66 |             8.65 |             34.09 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.37 |      8.91 |           1.45 |        6.56 |        4.88 |    3.93 |            7.65 |             8.65 |             33.94 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.54 |      8.92 |           1.95 |       12.34 |        4.88 |    0.73 |            7.66 |             8.65 |             34.09 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.37 |      8.91 |           1.45 |       19.37 |        4.88 |   15.85 |            7.65 |             8.65 |             33.94 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    70.05 |     12.96 |           1.54 |        4.88 |        4.88 |    0.00 |           11.58 |            12.58 |             26.17 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.24 |     12.96 |           1.56 |        6.17 |        4.88 |    9.46 |           11.57 |            12.57 |             26.01 |
| dummy-A8-3-wind0  | completed / outside configured limits |     5.02 |      5.58 |           2.67 | unavailable |        9.62 |    0.13 |            4.51 |             5.51 |              6.55 |
| dummy-A8-3-wind2  | completed / outside configured limits |     5.01 |      5.57 |           1.50 | unavailable |        9.13 |    0.28 |            4.51 |             5.51 |              6.53 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.25 |      7.24 |           2.51 | unavailable |       15.94 |    0.60 |            6.11 |             7.11 |             13.79 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.53 |      7.24 |           1.77 | unavailable |       17.86 |    7.95 |            6.11 |             7.11 |             13.55 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.63 |      8.01 |           1.90 |        2.54 |        5.19 |    0.03 |            6.70 |             7.70 |             28.86 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.10 |      8.04 |           1.87 |        8.17 |        5.19 |    7.57 |            6.70 |             7.70 |             28.77 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.63 |      8.01 |           1.90 |       17.57 |        5.19 |    1.11 |            6.70 |             7.70 |             28.86 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.10 |      8.04 |           1.87 |       23.10 |        5.19 |   31.07 |            6.70 |             7.70 |             28.77 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.84 |     12.25 |           2.46 |        8.49 |        5.20 |    0.16 |           10.19 |            11.19 |             21.66 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    52.81 |     12.24 |           2.06 |        9.97 |        5.20 |    1.23 |           10.18 |            11.18 |             21.52 |
| actual-A8-3-wind0 | completed / outside configured limits |     5.02 |      5.58 |           2.67 | unavailable |        9.62 |    0.13 |            4.51 |             5.51 |              6.55 |
| actual-A8-3-wind2 | completed / outside configured limits |     5.01 |      5.57 |           1.50 | unavailable |        9.13 |    0.28 |            4.51 |             5.51 |              6.53 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.25 |      7.24 |           2.51 | unavailable |       15.94 |    0.60 |            6.11 |             7.11 |             13.79 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.53 |      7.24 |           1.77 | unavailable |       17.86 |    7.95 |            6.11 |             7.11 |             13.55 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.63 |      8.01 |           1.90 |        2.54 |        5.19 |    0.03 |            6.70 |             7.70 |             28.86 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.10 |      8.04 |           1.87 |        8.17 |        5.19 |    7.57 |            6.70 |             7.70 |             28.77 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.63 |      8.01 |           1.90 |       17.57 |        5.19 |    1.11 |            6.70 |             7.70 |             28.86 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.10 |      8.04 |           1.87 |       23.10 |        5.19 |   31.07 |            6.70 |             7.70 |             28.77 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.84 |     12.25 |           2.46 |        8.49 |        5.20 |    0.16 |           10.19 |            11.19 |             21.66 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    52.81 |     12.24 |           2.06 |        9.97 |        5.20 |    1.23 |           10.18 |            11.18 |             21.52 |

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
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.1 m/s): "Nominal 457 mm parachute and lines"
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
- actual-C6-5-wind2: Recovery device deployment at high speed (23.1 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=160.5227676975382 g (allowed None … 85.0); apogee_m=6.826614432624145 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.467670623554907 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.621673533217809 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=160.5227676975382 g (allowed None … 85.0); apogee_m=6.7974501943989445 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.461306545556051 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.945598988062306 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=163.0727676975382 g (allowed None … 99.0); apogee_m=24.127270927691928 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.18744089839541 m/s (allowed 12.0 … None); deployment_speed_m_s=13.717361646721796 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=163.0727676975382 g (allowed None … 99.0); apogee_m=23.317509904548785 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.180485834264429 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=20.112829827903383 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=167.2727676975382 g (allowed None … 113.0); guide_departure_m_s=8.920275258227438 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=167.2727676975382 g (allowed None … 113.0); guide_departure_m_s=8.913745043517697 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=167.2727676975382 g (allowed None … 113.0); guide_departure_m_s=8.920275258227438 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.336042664393686 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=167.2727676975382 g (allowed None … 113.0); guide_departure_m_s=8.913745043517697 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.367843901819448 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=181.1727676975382 g (allowed None … 85.0); apogee_m=5.023448135638368 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.5751641443182205 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.621874975206394 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=181.1727676975382 g (allowed None … 85.0); apogee_m=5.014733726540982 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.569883574841005 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.133143025308186 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=183.72276769753822 g (allowed None … 99.0); apogee_m=18.252898614065924 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2441437073917685 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.940802378139178 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=183.72276769753822 g (allowed None … 99.0); apogee_m=17.533093199321318 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.23814425179991 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.859882718796356 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.01176789098867 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.044744292002857 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.01176789098867 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.56545210479323 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.044744292002857 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.097492343661653 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=181.1727676975382 g (allowed None … 85.0); apogee_m=5.023448135638368 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.5751641443182205 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.621874975206394 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=181.1727676975382 g (allowed None … 85.0); apogee_m=5.014733726540982 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.569883574841005 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.133143025308186 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=183.72276769753822 g (allowed None … 99.0); apogee_m=18.252898614065924 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2441437073917685 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=15.940802378139182 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=183.72276769753822 g (allowed None … 99.0); apogee_m=17.533093199321318 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.23814425179991 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.859882718796836 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.01176789098867 m/s
  (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.044744292002857 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.01176789098867 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.565452104793216 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=187.9227676975382 g (allowed None … 113.0); guide_departure_m_s=8.044744292002857 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.097492343661596 m/s (allowed None … 10.0)
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
