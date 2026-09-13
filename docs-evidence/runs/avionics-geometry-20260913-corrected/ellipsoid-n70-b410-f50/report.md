# Rocket Workbench report

Run: `ellipsoid-n70-b410-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `39216b4d6f218eb716851180ae5a488d97fe4e5049eea72827bcc2fb4a61b565`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.77 |      6.45 |           2.09 | unavailable |       10.76 |    0.26 |            5.21 |             6.20 |              8.09 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.75 |      6.45 |           0.90 | unavailable |       10.01 |    0.47 |            5.20 |             6.20 |              8.07 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.98 |      8.15 |           1.61 |       13.73 |        5.49 |    2.57 |            6.99 |             7.99 |             16.61 |
| empty-B4-4-wind2  | completed / outside configured limits |    23.25 |      8.14 |           0.98 | unavailable |       19.62 |    9.47 |            6.99 |             7.99 |             16.38 |
| empty-C6-3-wind0  | completed / outside configured limits |    86.48 |      8.93 |           1.94 |        1.31 |        4.89 |    0.04 |            7.63 |             8.63 |             34.01 |
| empty-C6-3-wind2  | completed / outside configured limits |    82.63 |      8.92 |           1.30 |        6.28 |        4.89 |    5.30 |            7.62 |             8.62 |             33.86 |
| empty-C6-5-wind0  | completed / outside configured limits |    86.48 |      8.93 |           1.61 |       12.12 |        4.89 |    1.36 |            7.63 |             8.63 |             34.01 |
| empty-C6-5-wind2  | completed / outside configured limits |    82.63 |      8.92 |           1.30 |       19.18 |        4.89 |   13.78 |            7.62 |             8.62 |             33.86 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    69.90 |     13.01 |           1.47 |        4.88 |        4.89 |    0.00 |           11.54 |            12.54 |             26.11 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    68.13 |     13.01 |           1.36 |        6.08 |        4.89 |    9.62 |           11.53 |            12.53 |             25.95 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.98 |      5.55 |           2.53 | unavailable |        9.64 |    0.11 |            4.50 |             5.50 |              6.51 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.98 |      5.54 |           1.34 | unavailable |        9.10 |    0.37 |            4.50 |             5.49 |              6.50 |
| dummy-B4-4-wind0  | completed / outside configured limits |    18.14 |      7.21 |           2.48 | unavailable |       15.72 |    0.48 |            6.09 |             7.09 |             13.73 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.51 |      7.21 |           1.53 | unavailable |       17.69 |    7.21 |            6.09 |             7.09 |             13.51 |
| dummy-C6-3-wind0  | completed / outside configured limits |    68.47 |      8.02 |           1.76 |        2.54 |        5.20 |    0.03 |            6.68 |             7.68 |             28.78 |
| dummy-C6-3-wind2  | completed / outside configured limits |    64.23 |      8.01 |           1.70 |        7.90 |        5.20 |    6.37 |            6.67 |             7.67 |             28.68 |
| dummy-C6-5-wind0  | completed / outside configured limits |    68.47 |      8.02 |           1.76 |       17.06 |        5.20 |    0.91 |            6.68 |             7.68 |             28.78 |
| dummy-C6-5-wind2  | completed / outside configured limits |    64.23 |      8.01 |           1.70 |       23.01 |        5.20 |   29.34 |            6.67 |             7.67 |             28.68 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    54.65 |     12.20 |           2.23 |        8.54 |        5.20 |    0.14 |           10.16 |            11.16 |             21.60 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    52.69 |     12.20 |           1.90 |        9.90 |        5.20 |    0.94 |           10.15 |            11.15 |             21.47 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.98 |      5.55 |           2.53 | unavailable |        9.64 |    0.11 |            4.50 |             5.50 |              6.51 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.98 |      5.54 |           1.34 | unavailable |        9.10 |    0.37 |            4.50 |             5.49 |              6.50 |
| actual-B4-4-wind0 | completed / outside configured limits |    18.14 |      7.21 |           2.48 | unavailable |       15.72 |    0.48 |            6.09 |             7.09 |             13.73 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.51 |      7.21 |           1.53 | unavailable |       17.69 |    7.21 |            6.09 |             7.09 |             13.51 |
| actual-C6-3-wind0 | completed / outside configured limits |    68.47 |      8.02 |           1.76 |        2.54 |        5.20 |    0.03 |            6.68 |             7.68 |             28.78 |
| actual-C6-3-wind2 | completed / outside configured limits |    64.23 |      8.01 |           1.70 |        7.90 |        5.20 |    6.37 |            6.67 |             7.67 |             28.68 |
| actual-C6-5-wind0 | completed / outside configured limits |    68.47 |      8.02 |           1.76 |       17.06 |        5.20 |    0.91 |            6.68 |             7.68 |             28.78 |
| actual-C6-5-wind2 | completed / outside configured limits |    64.23 |      8.01 |           1.70 |       23.01 |        5.20 |   29.34 |            6.67 |             7.67 |             28.68 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    54.65 |     12.20 |           2.23 |        8.54 |        5.20 |    0.14 |           10.16 |            11.16 |             21.60 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    52.69 |     12.20 |           1.90 |        9.90 |        5.20 |    0.94 |           10.15 |            11.15 |             21.47 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (19.7°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (19.7°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=161.09415039585392 g (allowed None … 85.0); apogee_m=6.7703095788638725 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.4516969916196025 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=10.76461381266177 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=161.09415039585392 g (allowed None … 85.0); apogee_m=6.750003028067027 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.445506339106883 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9025062594187652 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.013765224416796 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=163.64415039585393 g (allowed None … 99.0); apogee_m=23.980064873950955 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.151604706844793 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.734041034620855 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=163.64415039585393 g (allowed None … 99.0); apogee_m=23.2479813447722 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.144942473328918 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9805806308143921 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.61737199590982 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=167.84415039585394 g (allowed None … 113.0); guide_departure_m_s=8.930825232588983 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=167.84415039585394 g (allowed None … 113.0); guide_departure_m_s=8.924428348830883 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=167.84415039585394 g (allowed None … 113.0); guide_departure_m_s=8.930825232588983 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.124029253443931 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=167.84415039585394 g (allowed None … 113.0); guide_departure_m_s=8.924428348830883 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.18024671513518 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=181.74415039585392 g (allowed None … 85.0); apogee_m=4.984206476411265 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.548587193553476 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.635065487424285 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=181.74415039585392 g (allowed None … 85.0); apogee_m=4.976734096660071 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.543531163947287 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.100319342093682 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=184.29415039585393 g (allowed None … 99.0); apogee_m=18.138684212148647 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.214761479409559 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.722712344647439 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=184.29415039585393 g (allowed None … 99.0); apogee_m=17.51383069543786 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.2090137521710504 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.694923067931988 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.019092411526955 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.013455439543746 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.019092411526955 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.057504304345542 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.013455439543746 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.006779191123577 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=181.74415039585392 g (allowed None … 85.0); apogee_m=4.984206476411265 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.548587193553476 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.635065487424285 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=181.74415039585392 g (allowed None … 85.0); apogee_m=4.976734096660071 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.543531163947287 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.100319342093682 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=184.29415039585393 g (allowed None … 99.0); apogee_m=18.138684212148647 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.214761479409559 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.72271234464744 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=184.29415039585393 g (allowed None … 99.0); apogee_m=17.513830695437857 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.2090137521710504 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s
  (allowed None … 10.0); landing_descent_m_s=17.694923067932006 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.019092411526955
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.013455439543746
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.019092411526955
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.05750430434553 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=188.49415039585392 g (allowed None … 113.0); guide_departure_m_s=8.013455439543746
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.006779191123673 m/s (allowed None … 10.0)
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
