# Rocket Workbench report

Run: `ellipsoid-n70-b440-f50`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `2d0c1876d75ae4f560f395ab8b5e8819da883e0f15f04cf10a41962622478f8f`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.61 |      6.38 |           2.35 | unavailable |       10.70 |    0.24 |            5.15 |             6.15 |              7.96 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.60 |      6.38 |           1.05 | unavailable |        9.89 |    0.48 |            5.15 |             6.14 |              7.94 |
| empty-B4-4-wind0  | completed / outside configured limits |    23.46 |      8.09 |           2.31 |       12.31 |        5.97 |    1.06 |            6.92 |             7.92 |             16.37 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.76 |      8.08 |           1.16 | unavailable |       19.56 |    8.97 |            6.92 |             7.92 |             16.14 |
| empty-C6-3-wind0  | completed / outside configured limits |    84.79 |      8.83 |           2.22 |        0.95 |        4.91 |    0.04 |            7.55 |             8.55 |             33.56 |
| empty-C6-3-wind2  | completed / outside configured limits |    80.98 |      8.82 |           1.50 |        6.23 |        4.91 |    4.61 |            7.55 |             8.54 |             33.41 |
| empty-C6-5-wind0  | completed / outside configured limits |    84.80 |      8.83 |           2.01 |       12.18 |        4.91 |    1.10 |            7.55 |             8.55 |             33.56 |
| empty-C6-5-wind2  | completed / outside configured limits |    80.98 |      8.82 |           1.50 |       19.46 |        4.91 |   14.61 |            7.55 |             8.54 |             33.41 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    68.50 |     12.88 |           2.05 |        5.22 |        4.92 |    0.00 |           11.43 |            12.43 |             25.72 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    66.73 |     12.87 |           1.53 |        6.31 |        4.92 |    8.87 |           11.42 |            12.42 |             25.55 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.88 |      5.49 |           2.86 | unavailable |        9.57 |    0.11 |            4.45 |             5.45 |              6.41 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.87 |      5.48 |           1.51 | unavailable |        8.96 |    0.39 |            4.45 |             5.45 |              6.39 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.78 |      7.16 |           2.81 | unavailable |       15.56 |    0.54 |            6.03 |             7.03 |             13.54 |
| dummy-B4-4-wind2  | completed / outside configured limits |    17.18 |      7.16 |           1.69 | unavailable |       17.51 |    6.85 |            6.03 |             7.03 |             13.32 |
| dummy-C6-3-wind0  | completed / outside configured limits |    67.19 |      7.94 |           2.58 |        2.86 |        5.22 |    0.02 |            6.61 |             7.61 |             28.42 |
| dummy-C6-3-wind2  | completed / outside configured limits |    63.00 |      7.93 |           1.92 |        7.99 |        5.22 |    6.77 |            6.61 |             7.61 |             28.31 |
| dummy-C6-5-wind0  | completed / outside configured limits |    67.19 |      7.94 |           2.58 |       17.35 |        5.22 |    1.13 |            6.61 |             7.61 |             28.42 |
| dummy-C6-5-wind2  | completed / outside configured limits |    63.00 |      7.93 |           1.92 |       23.23 |        5.22 |   29.78 |            6.61 |             7.61 |             28.31 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    53.61 |     12.24 |           2.53 |        8.81 |        5.23 |    0.16 |           10.07 |            11.07 |             21.28 |
| dummy-C5-3-wind2  | completed / outside configured limits |    51.67 |     12.23 |           2.15 |       10.10 |        5.23 |    1.39 |           10.06 |            11.06 |             21.15 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.88 |      5.49 |           2.86 | unavailable |        9.57 |    0.11 |            4.45 |             5.45 |              6.41 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.87 |      5.48 |           1.51 | unavailable |        8.96 |    0.39 |            4.45 |             5.45 |              6.39 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.78 |      7.16 |           2.81 | unavailable |       15.56 |    0.54 |            6.03 |             7.03 |             13.54 |
| actual-B4-4-wind2 | completed / outside configured limits |    17.18 |      7.16 |           1.69 | unavailable |       17.51 |    6.85 |            6.03 |             7.03 |             13.32 |
| actual-C6-3-wind0 | completed / outside configured limits |    67.19 |      7.94 |           2.58 |        2.86 |        5.22 |    0.02 |            6.61 |             7.61 |             28.42 |
| actual-C6-3-wind2 | completed / outside configured limits |    63.00 |      7.93 |           1.92 |        7.99 |        5.22 |    6.77 |            6.61 |             7.61 |             28.31 |
| actual-C6-5-wind0 | completed / outside configured limits |    67.19 |      7.94 |           2.58 |       17.35 |        5.22 |    1.13 |            6.61 |             7.61 |             28.42 |
| actual-C6-5-wind2 | completed / outside configured limits |    63.00 |      7.93 |           1.92 |       23.23 |        5.22 |   29.78 |            6.61 |             7.61 |             28.31 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    53.61 |     12.24 |           2.53 |        8.81 |        5.23 |    0.16 |           10.07 |            11.07 |             21.28 |
| actual-C5-3-wind2 | completed / outside configured limits |    51.67 |     12.23 |           2.15 |       10.10 |        5.23 |    1.39 |           10.06 |            11.06 |             21.15 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (21°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: Recovery device deployment at high speed (23.2 m/s): "Nominal 457 mm parachute and lines"
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (21°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- actual-B4-4-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: Recovery device deployment at high speed (23.2 m/s): "Nominal 457 mm parachute and lines"
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

- empty-A8-3-wind0: launch_mass_g=162.5941503958539 g (allowed None … 85.0); apogee_m=6.614125602074796 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.381947661452192 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.703875350339612 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=162.5941503958539 g (allowed None … 85.0); apogee_m=6.595935887995505 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.37572595853985 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.891989644135295 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=165.1441503958539 g (allowed None … 99.0); apogee_m=23.464229898355878 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.087724559751177 m/s (allowed 12.0 … None); deployment_speed_m_s=12.307955142567872 m/s
  (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=165.1441503958539 g (allowed None … 99.0); apogee_m=22.760606143785786 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.08101669052356 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.56019750313608 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=169.34415039585392 g (allowed None … 113.0); guide_departure_m_s=8.830282780653603 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=169.34415039585392 g (allowed None … 113.0); guide_departure_m_s=8.823917113859375 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=169.34415039585392 g (allowed None … 113.0); guide_departure_m_s=8.830282780653603 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.177702650013236 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=169.34415039585392 g (allowed None … 113.0); guide_departure_m_s=8.823917113859375 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.45824212917279 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=183.2441503958539 g (allowed None … 85.0); apogee_m=4.87788116992606 m (allowed 30.0 …
  120.0); guide_departure_m_s=5.4881954945900455 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.572293480056738 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=183.2441503958539 g (allowed None … 85.0); apogee_m=4.870837768486037 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.483118640372465 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.963644935570834 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=185.7941503958539 g (allowed None … 99.0); apogee_m=17.77573149597517 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.161069778877138 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.556674227753891 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=185.7941503958539 g (allowed None … 99.0); apogee_m=17.18429218341389 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.155246013850682 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.510534566856858 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.9356597651575695 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.930045174724491 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.9356597651575695 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.348783708136096 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.930045174724491 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.234295021243742 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.10300138641193 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=183.2441503958539 g (allowed None … 85.0); apogee_m=4.87788116992606 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.4881954945900455 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.572293480056738 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=183.2441503958539 g (allowed None … 85.0); apogee_m=4.870837768486037 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.483118640372465 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.963644935570834 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=185.7941503958539 g (allowed None … 99.0); apogee_m=17.77573149597517 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.161069778877138 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=15.55667422775389 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=185.7941503958539 g (allowed None … 99.0); apogee_m=17.18429218341389 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.155246013850682 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.51053456685684 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.9356597651575695
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.930045174724491 m/s
  (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.9356597651575695
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.348783708136118 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=189.9941503958539 g (allowed None … 113.0); guide_departure_m_s=7.930045174724491 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.23429502124386 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.10300138641193 m/s (allowed None … 10.0)

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
