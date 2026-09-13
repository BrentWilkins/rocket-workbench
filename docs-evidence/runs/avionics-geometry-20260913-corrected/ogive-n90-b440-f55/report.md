# Rocket Workbench report

Run: `ogive-n90-b440-f55`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `603f5f2eafc68e127197f5b6971477b1679d2604aee0673a1b09a6c331bf5f83`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |     6.47 |      6.32 |           2.56 | unavailable |       10.54 |    0.26 |            5.10 |             6.09 |              7.84 |
| empty-A8-3-wind2  | completed / outside configured limits |     6.45 |      6.31 |           1.17 | unavailable |        9.74 |    0.40 |            5.09 |             6.09 |              7.82 |
| empty-B4-4-wind0  | completed / outside configured limits |    22.97 |      8.00 |           2.42 |       15.31 |        9.79 |    0.09 |            6.85 |             7.85 |             16.14 |
| empty-B4-4-wind2  | completed / outside configured limits |    22.22 |      7.99 |           1.30 | unavailable |       19.54 |    9.20 |            6.85 |             7.85 |             15.91 |
| empty-C6-3-wind0  | completed / outside configured limits |    82.96 |      8.79 |           2.39 |        0.52 |        4.93 |    0.04 |            7.48 |             8.48 |             33.09 |
| empty-C6-3-wind2  | completed / outside configured limits |    78.94 |      8.78 |           1.66 |        6.45 |        4.93 |    2.71 |            7.47 |             8.47 |             32.95 |
| empty-C6-5-wind0  | completed / outside configured limits |    82.96 |      8.79 |           1.92 |       12.60 |        4.93 |    0.72 |            7.48 |             8.48 |             33.09 |
| empty-C6-5-wind2  | completed / outside configured limits |    78.94 |      8.78 |           1.66 |       19.91 |        4.93 |   17.24 |            7.47 |             8.47 |             32.95 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    67.04 |     12.90 |           2.25 |        5.59 |        4.94 |    0.02 |           11.32 |            12.32 |             25.31 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    65.23 |     12.90 |           1.77 |        6.72 |        4.94 |    7.77 |           11.32 |            12.32 |             25.15 |
| dummy-A8-3-wind0  | completed / outside configured limits |     4.78 |      5.43 |           3.03 | unavailable |        9.45 |    0.12 |            4.41 |             5.41 |              6.31 |
| dummy-A8-3-wind2  | completed / outside configured limits |     4.77 |      5.43 |           1.64 | unavailable |        8.92 |    0.37 |            4.41 |             5.41 |              6.30 |
| dummy-B4-4-wind0  | completed / outside configured limits |    17.43 |      7.09 |           2.62 | unavailable |       15.49 |    0.54 |            5.98 |             6.98 |             13.36 |
| dummy-B4-4-wind2  | completed / outside configured limits |    16.80 |      7.11 |           1.90 | unavailable |       17.41 |    7.21 |            5.98 |             6.98 |             13.13 |
| dummy-C6-3-wind0  | completed / outside configured limits |    65.85 |      7.90 |           2.34 |        3.21 |        5.24 |    0.02 |            6.56 |             7.56 |             28.05 |
| dummy-C6-3-wind2  | completed / outside configured limits |    61.49 |      7.89 |           2.08 |        8.36 |        5.24 |    8.29 |            6.56 |             7.56 |             27.96 |
| dummy-C6-5-wind0  | completed / outside configured limits |    65.85 |      7.90 |           2.34 |       17.91 |        5.24 |    1.08 |            6.56 |             7.56 |             28.05 |
| dummy-C6-5-wind2  | completed / outside configured limits |    61.49 |      7.89 |           2.08 |       23.57 |        5.24 |   31.86 |            6.56 |             7.56 |             27.96 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    52.55 |     12.13 |           2.60 |        9.06 |        5.25 |    0.22 |            9.99 |            10.98 |             20.96 |
| dummy-C5-3-wind2  | completed / outside configured limits |    50.56 |     12.13 |           2.31 |       10.48 |        5.25 |    2.34 |            9.98 |            10.98 |             20.83 |
| actual-A8-3-wind0 | completed / outside configured limits |     4.78 |      5.43 |           3.03 | unavailable |        9.45 |    0.12 |            4.41 |             5.41 |              6.31 |
| actual-A8-3-wind2 | completed / outside configured limits |     4.77 |      5.43 |           1.64 | unavailable |        8.92 |    0.37 |            4.41 |             5.41 |              6.30 |
| actual-B4-4-wind0 | completed / outside configured limits |    17.43 |      7.09 |           2.62 | unavailable |       15.49 |    0.54 |            5.98 |             6.98 |             13.36 |
| actual-B4-4-wind2 | completed / outside configured limits |    16.80 |      7.11 |           1.90 | unavailable |       17.41 |    7.21 |            5.98 |             6.98 |             13.13 |
| actual-C6-3-wind0 | completed / outside configured limits |    65.85 |      7.90 |           2.34 |        3.21 |        5.24 |    0.02 |            6.56 |             7.56 |             28.05 |
| actual-C6-3-wind2 | completed / outside configured limits |    61.49 |      7.89 |           2.08 |        8.36 |        5.24 |    8.29 |            6.56 |             7.56 |             27.96 |
| actual-C6-5-wind0 | completed / outside configured limits |    65.85 |      7.90 |           2.34 |       17.91 |        5.24 |    1.08 |            6.56 |             7.56 |             28.05 |
| actual-C6-5-wind2 | completed / outside configured limits |    61.49 |      7.89 |           2.08 |       23.57 |        5.24 |   31.86 |            6.56 |             7.56 |             27.96 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    52.55 |     12.13 |           2.60 |        9.06 |        5.25 |    0.22 |            9.99 |            10.98 |             20.96 |
| actual-C5-3-wind2 | completed / outside configured limits |    50.56 |     12.13 |           2.31 |       10.48 |        5.25 |    2.34 |            9.98 |            10.98 |             20.83 |

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
- dummy-A8-3-wind2: Large angle of attack encountered (19.4°); Flight Event occurred after landing: Ejection charge;
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
- actual-A8-3-wind2: Large angle of attack encountered (19.4°); Flight Event occurred after landing: Ejection charge;
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

- empty-A8-3-wind0: launch_mass_g=163.9828170809914 g (allowed None … 85.0); apogee_m=6.471488739052286 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.318875030881725 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.544991925354477 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=163.9828170809914 g (allowed None … 85.0); apogee_m=6.451202912019071 m (allowed 30.0
  … 120.0); guide_departure_m_s=6.31248464856964 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=9.742816751340117 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=166.53281708099138 g (allowed None … 99.0); apogee_m=22.972868610523737 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.000893543853659 m/s (allowed 12.0 … None); deployment_speed_m_s=15.31422754599136
  m/s (allowed None … 10.0); landing_descent_m_s=9.788698812896675 m/s (allowed None … 6.0)
- empty-B4-4-wind2: launch_mass_g=166.53281708099138 g (allowed None … 99.0); apogee_m=22.22046082111661 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.994019617004999 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=19.541163378765383 m/s (allowed None … 6.0)
- empty-C6-3-wind0: launch_mass_g=170.7328170809914 g (allowed None … 113.0); guide_departure_m_s=8.78526660175958 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=170.7328170809914 g (allowed None … 113.0); guide_departure_m_s=8.77864016909047 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=170.7328170809914 g (allowed None … 113.0); guide_departure_m_s=8.78526660175958 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.601489016051659 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=170.7328170809914 g (allowed None … 113.0); guide_departure_m_s=8.77864016909047 m/s
  (allowed 12.0 … None); deployment_speed_m_s=19.912019052524855 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=184.63281708099137 g (allowed None … 85.0); apogee_m=4.7810065897883645 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.433272416302563 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.446783693370199 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=184.63281708099137 g (allowed None … 85.0); apogee_m=4.774385916094141 m (allowed 30.0
  … 120.0); guide_departure_m_s=5.428070002484192 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=8.920780226674978 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=187.18281708099138 g (allowed None … 99.0); apogee_m=17.434368995331372 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.089491722690375 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.488756514143077 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=187.18281708099138 g (allowed None … 99.0); apogee_m=16.79695643975075 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.107154677876772 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=17.41118205284743 m/s (allowed None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8969769884846075 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8911432297341735 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8969769884846075 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.911208177685918 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8911432297341735 m/s
  (allowed 12.0 … None); deployment_speed_m_s=23.574205991423835 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: deployment_speed_m_s=10.479709076646111 m/s (allowed None … 10.0)
- actual-A8-3-wind0: launch_mass_g=184.63281708099137 g (allowed None … 85.0); apogee_m=4.7810065897883645 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.433272416302563 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=9.446783693370199 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=184.63281708099137 g (allowed None … 85.0); apogee_m=4.774385916094141 m (allowed
  30.0 … 120.0); guide_departure_m_s=5.428070002484192 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=8.920780226674978 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=187.18281708099138 g (allowed None … 99.0); apogee_m=17.434368995331372 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.089491722690375 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=15.488756514143077 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=187.18281708099138 g (allowed None … 99.0); apogee_m=16.79695643975075 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.107154677876772 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=17.41118205284747 m/s (allowed None … 6.0)
- actual-C6-3-wind0: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8969769884846075
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8911432297341735
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8969769884846075
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.911208177685914 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=191.3828170809914 g (allowed None … 113.0); guide_departure_m_s=7.8911432297341735
  m/s (allowed 12.0 … None); deployment_speed_m_s=23.574205991423845 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: deployment_speed_m_s=10.47970907664611 m/s (allowed None … 10.0)

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
