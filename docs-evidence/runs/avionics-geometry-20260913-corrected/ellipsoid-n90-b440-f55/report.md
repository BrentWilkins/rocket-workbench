# Rocket Workbench report

Run: `ellipsoid-n90-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `fed26b1de7ac6e9d16097fec24eee50b9603f4bf361f3cdd787cdabed8ce870f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.23 |      6.20 |           2.63 | unavailable |       10.41 |    0.23 |            5.00 |             6.00 |              7.63 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.21 |      6.19 |           1.18 | unavailable |        9.66 |    0.42 |            5.00 |             6.00 |              7.62 |
| empty-B4-4-wind0  | completed / outside configured limits |    22.19 |      7.88 |           2.56 | unavailable |       15.32 |    0.20 |            6.73 |             7.73 |             15.77 |
| empty-B4-4-wind2  | completed / outside configured limits |    21.46 |      7.87 |           1.33 | unavailable |       19.22 |    8.86 |            6.73 |             7.73 |             15.54 |
| empty-C6-3-wind0  | completed / outside configured limits |    80.61 |      8.67 |           1.90 |        0.04 |        4.97 |    0.04 |            7.36 |             8.35 |             32.42 |
| empty-C6-3-wind2  | completed / outside configured limits |    76.61 |      8.66 |           1.69 |        6.51 |        4.97 |    1.54 |            7.35 |             8.35 |             32.27 |
| empty-C6-5-wind0  | completed / outside configured limits |    80.61 |      8.67 |           2.02 |       12.78 |        4.97 |    0.64 |            7.36 |             8.35 |             32.42 |
| empty-C6-5-wind2  | completed / outside configured limits |    76.61 |      8.66 |           1.69 |       20.34 |        4.97 |   18.72 |            7.35 |             8.35 |             32.27 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    65.03 |     12.88 |           1.27 |        6.06 |        4.98 |    0.03 |           11.14 |            12.14 |             24.73 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    63.22 |     12.87 |           1.79 |        7.14 |        4.98 |    6.53 |           11.14 |            12.14 |             24.57 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.61 |      5.34 |           3.08 | unavailable |        9.35 |    0.11 |            4.34 |             5.34 |              6.15 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.61 |      5.33 |           1.63 | unavailable |        8.77 |    0.39 |            4.34 |             5.33 |              6.14 |
| dummy-B4-4-wind0  | completed / outside configured limits |    16.87 |      7.01 |           2.81 | unavailable |       15.23 |    0.52 |            5.89 |             6.89 |             13.06 |
| dummy-B4-4-wind2  | completed / outside configured limits |    16.27 |      7.00 |           1.85 | unavailable |       17.11 |    6.85 |            5.89 |             6.89 |             12.84 |
| dummy-C6-3-wind0  | completed / outside configured limits |    63.99 |      7.80 |           2.70 |        3.66 |        5.28 |    0.01 |            6.46 |             7.46 |             27.49 |
| dummy-C6-3-wind2  | completed / outside configured limits |    59.66 |      7.79 |           2.09 |        8.61 |        5.28 |    9.14 |            6.46 |             7.46 |             27.40 |
| dummy-C6-5-wind0  | completed / outside configured limits |    63.99 |      7.80 |           2.70 |       18.21 |        5.28 |    1.08 |            6.46 |             7.46 |             27.49 |
| dummy-C6-5-wind2  | completed / outside configured limits |    59.66 |      7.79 |           2.09 |       23.96 |        5.28 |   32.95 |            6.46 |             7.46 |             27.40 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    51.01 |     12.08 |           2.10 |        9.43 |        5.28 |    0.26 |            9.84 |            10.84 |             20.47 |
| dummy-C5-3-wind2  | completed / outside configured limits |    49.02 |     12.08 |           2.33 |       10.88 |        5.28 |    3.28 |            9.83 |            10.83 |             20.35 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.61 |      5.34 |           3.08 | unavailable |        9.35 |    0.11 |            4.34 |             5.34 |              6.15 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.61 |      5.33 |           1.63 | unavailable |        8.77 |    0.39 |            4.34 |             5.33 |              6.14 |
| actual-B4-4-wind0 | completed / outside configured limits |    16.87 |      7.01 |           2.81 | unavailable |       15.23 |    0.52 |            5.89 |             6.89 |             13.06 |
| actual-B4-4-wind2 | completed / outside configured limits |    16.27 |      7.00 |           1.85 | unavailable |       17.11 |    6.85 |            5.89 |             6.89 |             12.84 |
| actual-C6-3-wind0 | completed / outside configured limits |    63.99 |      7.80 |           2.70 |        3.66 |        5.28 |    0.01 |            6.46 |             7.46 |             27.49 |
| actual-C6-3-wind2 | completed / outside configured limits |    59.66 |      7.79 |           2.09 |        8.61 |        5.28 |    9.14 |            6.46 |             7.46 |             27.40 |
| actual-C6-5-wind0 | completed / outside configured limits |    63.99 |      7.80 |           2.70 |       18.21 |        5.28 |    1.08 |            6.46 |             7.46 |             27.49 |
| actual-C6-5-wind2 | completed / outside configured limits |    59.66 |      7.79 |           2.09 |       23.96 |        5.28 |   32.95 |            6.46 |             7.46 |             27.40 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    51.01 |     12.08 |           2.10 |        9.43 |        5.28 |    0.26 |            9.84 |            10.84 |             20.47 |
| actual-C5-3-wind2 | completed / outside configured limits |    49.02 |     12.08 |           2.33 |       10.88 |        5.28 |    3.28 |            9.83 |            10.83 |             20.35 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: Recovery device deployment at high speed (20.3 m/s): "Nominal 457 mm parachute and lines"
- empty-C5-3-wind0: no engine warnings
- empty-C5-3-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (21.7°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (24 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (21.7°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (24 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=166.49595818152446 g (allowed None … 85.0); apogee_m=6.229134164869361 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.195374385746017 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.407934986892826 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=166.49595818152446 g (allowed None … 85.0); apogee_m=6.212308999974176 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.189162160933162 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.66138986424616 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=169.04595818152447 g (allowed None … 99.0); apogee_m=22.18981424521481 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.877943793146676 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.324800098183738 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=169.04595818152447 g (allowed None … 99.0); apogee_m=21.464687910161032 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.871165140813047 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=19.222941462139772 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=173.24595818152446 g (allowed None … 113.0); guide_departure_m_s=8.668511433030343 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=173.24595818152446 g (allowed None … 113.0); guide_departure_m_s=8.66194883056899 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=173.24595818152446 g (allowed None … 113.0); guide_departure_m_s=8.668511433030343 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.778160451956907 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=173.24595818152446 g (allowed None … 113.0); guide_departure_m_s=8.66194883056899 m/s
  (allowed 12.0 … None); deployment_speed_m_s=20.342787777440424 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=187.14595818152443 g (allowed None … 85.0); apogee_m=4.614675668096961 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.337231168529474 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.346840229222169 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=187.14595818152443 g (allowed None … 85.0); apogee_m=4.608873603392656 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.332102914226725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.770652674101546 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=189.69595818152445 g (allowed None … 99.0); apogee_m=16.87458563453657 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.009671525388379 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.23147035322453 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=189.69595818152445 g (allowed None … 99.0); apogee_m=16.268361889030807 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.003735433340835 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.10807237487136 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.798637631563097 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.792862221327654 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.798637631563097 m/s
  (allowed 12.0 … None); deployment_speed_m_s=18.20511694249617 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.792862221327654 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.964631842575464 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.879231321918853 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=187.14595818152443 g (allowed None … 85.0); apogee_m=4.614675668096961 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.337231168529474 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.34684022922217 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=187.14595818152443 g (allowed None … 85.0); apogee_m=4.608873603392656 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.332102914226725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.770652674101546 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=189.69595818152445 g (allowed None … 99.0); apogee_m=16.87458563453657 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.009671525388379 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.23147035322453 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=189.69595818152445 g (allowed None … 99.0); apogee_m=16.268361889030807 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.003735433340835 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.10807237487135 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.798637631563097
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.792862221327654
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.798637631563097
  m/s (allowed 12.0 … None); deployment_speed_m_s=18.205116942496165 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=193.89595818152443 g (allowed None … 113.0); guide_departure_m_s=7.792862221327654
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.964631842575507 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.87923132191889 m/s (allowed None … 10.0)

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
