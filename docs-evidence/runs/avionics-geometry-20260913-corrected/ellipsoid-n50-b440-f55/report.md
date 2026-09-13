# Rocket Workbench report

Run: `ellipsoid-n50-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `da44b00906e0f646deafb32022bc7514c2891ddb0c59bff7723ad1ce1dd52f5c`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.73 |      6.43 |           2.45 | unavailable |       10.62 |    0.29 |            5.19 |             6.19 |              8.06 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.70 |      6.42 |           1.23 | unavailable |        9.91 |    0.28 |            5.19 |             6.19 |              8.03 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.80 |      8.13 |           2.18 |       16.97 |        9.30 |    0.54 |            6.97 |             7.97 |             16.53 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.99 |      8.12 |           1.38 | unavailable |       19.95 |    9.59 |            6.97 |             7.97 |             16.29 |
| empty-C6-3-wind0  | completed / outside configured limits |    85.46 |      8.91 |           2.34 |        1.03 |        4.89 |    0.04 |            7.61 |             8.61 |             33.80 |
| empty-C6-3-wind2  | completed / outside configured limits |    81.31 |      8.90 |           1.68 |        6.54 |        4.89 |    3.44 |            7.60 |             8.60 |             33.65 |
| empty-C6-5-wind0  | completed / outside configured limits |    85.46 |      8.91 |           2.08 |       13.31 |        4.89 |    0.38 |            7.61 |             8.61 |             33.80 |
| empty-C6-5-wind2  | completed / outside configured limits |    81.31 |      8.90 |           1.68 |       19.56 |        4.89 |   16.44 |            7.60 |             8.60 |             33.65 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    69.16 |     12.98 |           1.33 |        5.10 |        4.90 |    0.01 |           11.51 |            12.51 |             25.92 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    67.34 |     12.97 |           1.81 |        6.36 |        4.90 |    8.92 |           11.50 |            12.50 |             25.76 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.96 |      5.53 |           2.96 | unavailable |        9.61 |    0.13 |            4.49 |             5.48 |              6.48 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.95 |      5.54 |           1.74 | unavailable |        9.05 |    0.29 |            4.48 |             5.48 |              6.47 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.02 |      7.20 |           2.65 | unavailable |       15.73 |    0.69 |            6.08 |             7.08 |             13.67 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.32 |      7.19 |           2.03 | unavailable |       17.77 |    7.73 |            6.08 |             7.08 |             13.43 |
| dummy-C6-3-wind0  | completed / outside configured limits |    67.81 |      8.00 |           2.04 |        2.74 |        5.20 |    0.02 |            6.66 |             7.66 |             28.63 |
| dummy-C6-3-wind2  | completed / outside configured limits |    63.30 |      7.99 |           2.13 |        8.24 |        5.20 |    7.88 |            6.66 |             7.66 |             28.53 |
| dummy-C6-5-wind0  | completed / outside configured limits |    67.81 |      8.00 |           2.04 |       17.66 |        5.20 |    1.37 |            6.66 |             7.66 |             28.63 |
| dummy-C6-5-wind2  | completed / outside configured limits |    63.30 |      7.99 |           2.13 |       23.25 |        5.20 |   31.44 |            6.66 |             7.66 |             28.53 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.18 |     12.32 |           2.03 |        8.66 |        5.21 |    0.18 |           10.13 |            11.13 |             21.46 |
| dummy-C5-3-wind2  | completed / outside configured limits |    52.16 |     12.32 |           2.34 |       10.13 |        5.21 |    1.52 |           10.13 |            11.13 |             21.32 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.96 |      5.53 |           2.96 | unavailable |        9.61 |    0.13 |            4.49 |             5.48 |              6.48 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.95 |      5.54 |           1.74 | unavailable |        9.05 |    0.29 |            4.48 |             5.48 |              6.47 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.02 |      7.20 |           2.65 | unavailable |       15.73 |    0.69 |            6.08 |             7.08 |             13.67 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.32 |      7.19 |           2.03 | unavailable |       17.77 |    7.73 |            6.08 |             7.08 |             13.43 |
| actual-C6-3-wind0 | completed / outside configured limits |    67.81 |      8.00 |           2.04 |        2.74 |        5.20 |    0.02 |            6.66 |             7.66 |             28.63 |
| actual-C6-3-wind2 | completed / outside configured limits |    63.30 |      7.99 |           2.13 |        8.24 |        5.20 |    7.88 |            6.66 |             7.66 |             28.53 |
| actual-C6-5-wind0 | completed / outside configured limits |    67.81 |      8.00 |           2.04 |       17.66 |        5.20 |    1.37 |            6.66 |             7.66 |             28.63 |
| actual-C6-5-wind2 | completed / outside configured limits |    63.30 |      7.99 |           2.13 |       23.25 |        5.20 |   31.44 |            6.66 |             7.66 |             28.53 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.18 |     12.32 |           2.03 |        8.66 |        5.21 |    0.18 |           10.13 |            11.13 |             21.46 |
| actual-C5-3-wind2 | completed / outside configured limits |    52.16 |     12.32 |           2.34 |       10.13 |        5.21 |    1.52 |           10.13 |            11.13 |             21.32 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (17.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.3 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (17.4°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.3 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=161.45986920628965 g (allowed None … 85.0); apogee_m=6.72724868249953 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.430056590582161 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.622264415738657 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=161.45986920628965 g (allowed None … 85.0); apogee_m=6.6998686079002105 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.423618568313443 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.912462853034134 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=164.00986920628966 g (allowed None … 99.0); apogee_m=23.799974964491188 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.127591941206854 m/s (allowed 12.0 … None); deployment_speed_m_s=16.96524172466109
  m/s (allowed None … 10.0); landing_descent_m_s=9.301813727765596 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=164.00986920628966 g (allowed None … 99.0); apogee_m=22.990437802970956 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.120652023701888 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=19.954133235511623 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=168.20986920628965 g (allowed None … 113.0); guide_departure_m_s=8.90538519438196 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=168.20986920628965 g (allowed None … 113.0); guide_departure_m_s=8.898718256480503 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=168.20986920628965 g (allowed None … 113.0); guide_departure_m_s=8.90538519438196 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.310080477018065 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=168.20986920628965 g (allowed None … 113.0); guide_departure_m_s=8.898718256480503 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.560839032410843 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=182.10986920628966 g (allowed None … 85.0); apogee_m=4.955938193730969 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.530870152452707 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.610137276434708 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=182.10986920628966 g (allowed None … 85.0); apogee_m=4.947709542108577 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.535530047512076 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.04683645959264 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=184.65986920628967 g (allowed None … 99.0); apogee_m=18.022713766041914 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.195081634924784 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.732578748128205 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=184.65986920628967 g (allowed None … 99.0); apogee_m=17.31725227729099 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.189093559602447 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.77323435727132 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.998005426940762 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.992129994139023 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.998005426940762 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.66146955375693 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.992129994139023 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.251280467545236 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.128524289952885 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=182.10986920628966 g (allowed None … 85.0); apogee_m=4.955938193730969 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.530870152452707 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.610137276434708 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=182.10986920628966 g (allowed None … 85.0); apogee_m=4.947709542108577 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.535530047512076 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.04683645959264 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=184.65986920628967 g (allowed None … 99.0); apogee_m=18.022713766041914 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.195081634924784 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.732578748128207 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=184.65986920628967 g (allowed None … 99.0); apogee_m=17.31725227729099 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.189093559602447 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.773234357271207 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.998005426940762
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.992129994139023
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.998005426940762
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.661469553756927 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=188.85986920628966 g (allowed None … 113.0); guide_departure_m_s=7.992129994139023
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.251280467545225 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.128524289952876 m/s (allowed None … 10.0)

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
