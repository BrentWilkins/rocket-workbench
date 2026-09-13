# Rocket Workbench report

Run: `ellipsoid-n70-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `a63f6b95e82e1e73fd9c1ad91c4191ab4262696d1690fc70a9a46f46bd45471c`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.47 |      6.32 |           2.57 | unavailable |       10.53 |    0.26 |            5.10 |             6.09 |              7.84 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.45 |      6.31 |           1.21 | unavailable |        9.76 |    0.36 |            5.09 |             6.09 |              7.82 |
| empty-B4-4-wind0  | completed / outside configured limits |    22.98 |      8.00 |           2.44 |       16.50 |       13.15 |    0.28 |            6.85 |             7.85 |             16.15 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.21 |      7.99 |           1.35 | unavailable |       19.64 |    9.21 |            6.85 |             7.85 |             15.91 |
| empty-C6-3-wind0  | completed / outside configured limits |    83.00 |      8.79 |           2.40 |        0.53 |        4.93 |    0.04 |            7.48 |             8.48 |             33.10 |
| empty-C6-3-wind2  | completed / outside configured limits |    78.92 |      8.78 |           1.68 |        6.51 |        4.93 |    2.46 |            7.48 |             8.47 |             32.95 |
| empty-C6-5-wind0  | completed / outside configured limits |    83.00 |      8.79 |           2.05 |       13.06 |        4.93 |    0.45 |            7.48 |             8.48 |             33.10 |
| empty-C6-5-wind2  | completed / outside configured limits |    78.92 |      8.78 |           1.68 |       19.95 |        4.93 |   17.62 |            7.48 |             8.47 |             32.95 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    67.07 |     12.90 |           1.22 |        5.58 |        4.94 |    0.02 |           11.33 |            12.32 |             25.32 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    65.24 |     12.90 |           1.82 |        6.76 |        4.94 |    7.68 |           11.32 |            12.32 |             25.15 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.78 |      5.43 |           3.04 | unavailable |        9.44 |    0.12 |            4.41 |             5.41 |              6.32 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.77 |      5.43 |           1.67 | unavailable |        8.93 |    0.34 |            4.41 |             5.41 |              6.30 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.44 |      7.09 |           2.68 | unavailable |       15.51 |    0.58 |            5.98 |             6.98 |             13.36 |
| dummy-B4-4-wind2  | completed / outside configured limits |    16.78 |      7.11 |           1.96 | unavailable |       17.47 |    7.26 |            5.98 |             6.98 |             13.13 |
| dummy-C6-3-wind0  | completed / outside configured limits |    65.87 |      7.90 |           2.47 |        3.20 |        5.24 |    0.02 |            6.56 |             7.56 |             28.05 |
| dummy-C6-3-wind2  | completed / outside configured limits |    61.45 |      7.89 |           2.11 |        8.42 |        5.24 |    8.53 |            6.56 |             7.56 |             27.96 |
| dummy-C6-5-wind0  | completed / outside configured limits |    65.87 |      7.90 |           2.47 |       17.97 |        5.24 |    1.22 |            6.56 |             7.56 |             28.05 |
| dummy-C6-5-wind2  | completed / outside configured limits |    61.45 |      7.89 |           2.11 |       23.61 |        5.24 |   32.22 |            6.56 |             7.56 |             27.96 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    52.57 |     12.13 |           2.65 |        9.05 |        5.25 |    0.22 |            9.99 |            10.98 |             20.96 |
| dummy-C5-3-wind2  | completed / outside configured limits |    50.56 |     12.13 |           2.33 |       10.52 |        5.25 |    2.45 |            9.98 |            10.98 |             20.83 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.78 |      5.43 |           3.04 | unavailable |        9.44 |    0.12 |            4.41 |             5.41 |              6.32 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.77 |      5.43 |           1.67 | unavailable |        8.93 |    0.34 |            4.41 |             5.41 |              6.30 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.44 |      7.09 |           2.68 | unavailable |       15.51 |    0.58 |            5.98 |             6.98 |             13.36 |
| actual-B4-4-wind2 | completed / outside configured limits |    16.78 |      7.11 |           1.96 | unavailable |       17.47 |    7.26 |            5.98 |             6.98 |             13.13 |
| actual-C6-3-wind0 | completed / outside configured limits |    65.87 |      7.90 |           2.47 |        3.20 |        5.24 |    0.02 |            6.56 |             7.56 |             28.05 |
| actual-C6-3-wind2 | completed / outside configured limits |    61.45 |      7.89 |           2.11 |        8.42 |        5.24 |    8.53 |            6.56 |             7.56 |             27.96 |
| actual-C6-5-wind0 | completed / outside configured limits |    65.87 |      7.90 |           2.47 |       17.97 |        5.24 |    1.22 |            6.56 |             7.56 |             28.05 |
| actual-C6-5-wind2 | completed / outside configured limits |    61.45 |      7.89 |           2.11 |       23.61 |        5.24 |   32.22 |            6.56 |             7.56 |             27.96 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    52.57 |     12.13 |           2.65 |        9.05 |        5.25 |    0.22 |            9.99 |            10.98 |             20.96 |
| actual-C5-3-wind2 | completed / outside configured limits |    50.56 |     12.13 |           2.33 |       10.52 |        5.25 |    2.45 |            9.98 |            10.98 |             20.83 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (18.8°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.6 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (18.8°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.6 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=163.97797314464864 g (allowed None … 85.0); apogee_m=6.4721738351561635 m (allowed
  30.0 … 120.0); guide_departure_m_s=6.319172655178326 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.528793618828953 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=163.97797314464864 g (allowed None … 85.0); apogee_m=6.450969571191337 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.312795506343787 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.759517746698243 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=166.52797314464866 g (allowed None … 99.0); apogee_m=22.977569074082503 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.001227809073946 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.503983985255545 m/s (allowed None … 10.0); landing_descent_m_s=13.154503204729865 m/s (allowed
  None … 6.0)
- empty-B4-4-wind2: launch_mass_g=166.52797314464866 g (allowed None … 99.0); apogee_m=22.20807187291926 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.99436894411062 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.640250947309355 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=170.72797314464867 g (allowed None … 113.0); guide_departure_m_s=8.78562171923424 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=170.72797314464867 g (allowed None … 113.0); guide_departure_m_s=8.779010206716643 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=170.72797314464867 g (allowed None … 113.0); guide_departure_m_s=8.78562171923424 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.062432121114583 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=170.72797314464867 g (allowed None … 113.0); guide_departure_m_s=8.779010206716643 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.95390590022507 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=184.62797314464865 g (allowed None … 85.0); apogee_m=4.781421877644231 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.433514344928091 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.444044632416407 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=184.62797314464865 g (allowed None … 85.0); apogee_m=4.774656526008466 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.428322256081411 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.934546873642931 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=187.17797314464866 g (allowed None … 99.0); apogee_m=17.436933734805255 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.089771803792153 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.514078459213977 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=187.17797314464866 g (allowed None … 99.0); apogee_m=16.78419840761582 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.107442505968096 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.47351518370984 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.897270224162233 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.8914493250339595
  m/s (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.897270224162233 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.968647907937278 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.8914493250339595
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.610601636338533 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.519177999940784 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=184.62797314464865 g (allowed None … 85.0); apogee_m=4.781421877644231 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.433514344928091 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.444044632416407 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=184.62797314464865 g (allowed None … 85.0); apogee_m=4.774656526008466 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.428322256081411 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.934546873642931 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=187.17797314464866 g (allowed None … 99.0); apogee_m=17.436933734805255 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.089771803792153 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.51407845921397 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=187.17797314464866 g (allowed None … 99.0); apogee_m=16.78419840761582 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.107442505968096 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.473515183709864 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.897270224162233
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.8914493250339595
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.897270224162233
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.968647907937285 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=191.37797314464865 g (allowed None … 113.0); guide_departure_m_s=7.8914493250339595
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.610601636338643 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.519177999940796 m/s (allowed None … 10.0)

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
