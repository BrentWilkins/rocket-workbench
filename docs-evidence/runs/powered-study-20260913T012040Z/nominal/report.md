# Rocket Workbench report

Run: `nominal`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `c3bfce6b49d4e9f442dd5e5a21cb6a8331da3013cfbe5aa5ad1e7e2fd90f0677`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| empty-A8-3-wind0  | completed / outside configured limits |    11.15 |      8.13 |           1.75 | unavailable |       11.20 |    0.82 |            6.67 |             7.67 |             11.34 |
| empty-A8-3-wind2  | completed / outside configured limits |    11.00 |      8.12 |           0.84 | unavailable |       11.29 |    0.51 |            6.66 |             7.66 |             11.29 |
| empty-B4-4-wind0  | completed / outside configured limits |    36.81 |      9.94 |           1.70 |       11.54 |        4.39 |    1.05 |            8.84 |             9.84 |             22.27 |
| empty-B4-4-wind2  | completed / outside configured limits |    35.88 |      9.93 |           1.00 |       16.10 |        4.39 |    2.04 |            8.84 |             9.84 |             22.06 |
| empty-C6-3-wind0  | completed / outside configured limits |   115.02 |     10.60 |           1.60 |        5.75 |        4.38 |    0.04 |            9.56 |            10.56 |             43.17 |
| empty-C6-3-wind2  | completed / outside configured limits |   111.44 |     10.59 |           1.20 |        7.28 |        4.38 |   24.27 |            9.55 |            10.55 |             42.98 |
| empty-C6-5-wind0  | completed / outside configured limits |   115.80 |     10.60 |           1.36 |       10.95 |        4.38 |    0.84 |            9.56 |            10.56 |             43.17 |
| empty-C6-5-wind2  | completed / outside configured limits |   112.16 |     10.59 |           1.20 |       14.63 |        4.38 |    9.86 |            9.55 |            10.55 |             42.98 |
| empty-C5-3-wind0  | completed / incomplete inputs         |    96.89 |     13.99 |           1.53 |        0.08 |        4.39 |    0.04 |           14.35 |            15.35 |             33.86 |
| empty-C5-3-wind2  | completed / incomplete inputs         |    95.37 |     13.99 |           1.12 |        2.68 |        4.39 |   28.71 |           14.34 |            15.34 |             33.69 |
| dummy-A8-3-wind0  | completed / outside configured limits |     8.24 |      7.08 |           2.23 | unavailable |       10.90 |    0.43 |            5.74 |             6.73 |              9.26 |
| dummy-A8-3-wind2  | completed / outside configured limits |     8.15 |      7.07 |           1.37 | unavailable |       10.68 |    0.17 |            5.73 |             6.73 |              9.22 |
| dummy-B4-4-wind0  | completed / outside configured limits |    28.35 |      8.83 |           2.19 |       16.63 |        4.70 |    1.30 |            7.66 |             8.66 |             18.64 |
| dummy-B4-4-wind2  | completed / outside configured limits |    27.39 |      8.82 |           1.64 |       19.93 |        4.63 |    9.74 |            7.66 |             8.66 |             18.41 |
| dummy-C6-3-wind0  | completed / outside configured limits |    96.13 |      9.57 |           2.12 |        2.74 |        4.69 |    0.04 |            8.33 |             9.33 |             37.22 |
| dummy-C6-3-wind2  | completed / outside configured limits |    91.89 |      9.57 |           1.68 |        6.50 |        4.69 |    9.59 |            8.32 |             9.32 |             37.05 |
| dummy-C6-5-wind0  | completed / outside configured limits |    96.21 |      9.57 |           1.45 |       13.42 |        4.69 |    0.40 |            8.33 |             9.33 |             37.22 |
| dummy-C6-5-wind2  | completed / outside configured limits |    91.94 |      9.57 |           1.68 |       17.87 |        4.69 |    8.75 |            8.32 |             9.32 |             37.05 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    79.02 |     13.36 |           2.08 |        3.16 |        4.69 |    0.02 |           12.56 |            13.56 |             28.82 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    77.25 |     13.35 |           1.79 |        4.70 |        4.69 |   15.73 |           12.55 |            13.55 |             28.64 |
| actual-A8-3-wind0 | completed / outside configured limits |     8.24 |      7.08 |           2.23 | unavailable |       10.90 |    0.43 |            5.74 |             6.73 |              9.26 |
| actual-A8-3-wind2 | completed / outside configured limits |     8.15 |      7.07 |           1.37 | unavailable |       10.68 |    0.17 |            5.73 |             6.73 |              9.22 |
| actual-B4-4-wind0 | completed / outside configured limits |    28.35 |      8.83 |           2.19 |       16.63 |        4.70 |    1.30 |            7.66 |             8.66 |             18.64 |
| actual-B4-4-wind2 | completed / outside configured limits |    27.39 |      8.82 |           1.64 |       19.93 |        4.63 |    9.74 |            7.66 |             8.66 |             18.41 |
| actual-C6-3-wind0 | completed / outside configured limits |    96.13 |      9.57 |           2.12 |        2.74 |        4.69 |    0.04 |            8.33 |             9.33 |             37.22 |
| actual-C6-3-wind2 | completed / outside configured limits |    91.89 |      9.57 |           1.68 |        6.50 |        4.69 |    9.59 |            8.32 |             9.32 |             37.05 |
| actual-C6-5-wind0 | completed / outside configured limits |    96.21 |      9.57 |           1.45 |       13.42 |        4.69 |    0.40 |            8.33 |             9.33 |             37.22 |
| actual-C6-5-wind2 | completed / outside configured limits |    91.94 |      9.57 |           1.68 |       17.87 |        4.69 |    8.75 |            8.32 |             9.32 |             37.05 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    79.02 |     13.36 |           2.08 |        3.16 |        4.69 |    0.02 |           12.56 |            13.56 |             28.82 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    77.25 |     13.35 |           1.79 |        4.70 |        4.69 |   15.73 |           12.55 |            13.55 |             28.64 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Large angle of attack encountered (22.1°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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
- dummy-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- dummy-C5-3-wind0: no engine warnings
- dummy-C5-3-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-B4-4-wind0: no engine warnings
- actual-B4-4-wind2: no engine warnings
- actual-C6-3-wind0: no engine warnings
- actual-C6-3-wind2: no engine warnings
- actual-C6-5-wind0: no engine warnings
- actual-C6-5-wind2: no engine warnings
- actual-C5-3-wind0: no engine warnings
- actual-C5-3-wind2: no engine warnings

## Missing measurements / physical checks

- Exact XIAO board/camera/antenna identity and measured envelope
- Battery identity, connector/wire envelopes and retention measurements
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

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=130.475305144004 g (allowed None … 85.0); apogee_m=11.15477994720002 m (allowed 30.0 …
  120.0); guide_departure_m_s=8.128798352271614 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None …
  10.0); landing_descent_m_s=11.19994514303345 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=130.475305144004 g (allowed None … 85.0); apogee_m=11.004022328582218 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.119341931649707 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8440561196636488 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.290608346433524 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=133.02530514400402 g (allowed None … 99.0); guide_departure_m_s=9.936661114941419 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.542676007364925 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=133.02530514400402 g (allowed None … 99.0); guide_departure_m_s=9.927056367075027 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.10303628231713 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=137.225305144004 g (allowed None … 113.0); guide_departure_m_s=10.597563381925537 m/s
  (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=137.225305144004 g (allowed None … 113.0); guide_departure_m_s=10.588660518381571 m/s
  (allowed 12.0 … None)
- empty-C6-5-wind0: launch_mass_g=137.225305144004 g (allowed None … 113.0); guide_departure_m_s=10.597563381925537 m/s
  (allowed 12.0 … None); deployment_speed_m_s=10.94947326612487 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=137.225305144004 g (allowed None … 113.0); guide_departure_m_s=10.588660518381571 m/s
  (allowed 12.0 … None); deployment_speed_m_s=14.634684032553292 m/s (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=148.47530514400404 g (allowed None … 85.0); apogee_m=8.238153042770202 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.081512594776989 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.898256650040127 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=148.47530514400404 g (allowed None … 85.0); apogee_m=8.149066638349488 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.073369052220057 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.680575853084083 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=151.02530514400402 g (allowed None … 99.0); apogee_m=28.345940563122944 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.827046004888608 m/s (allowed 12.0 … None); deployment_speed_m_s=16.62636527833472
  m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=151.02530514400402 g (allowed None … 99.0); apogee_m=27.391813110185264 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.818537101352929 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.932890835053943 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.574908858199958 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.566791052078152 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.574908858199958 m/s
  (allowed 12.0 … None); deployment_speed_m_s=13.415964982304558 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.566791052078152 m/s
  (allowed 12.0 … None); deployment_speed_m_s=17.871886979204735 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=148.47530514400404 g (allowed None … 85.0); apogee_m=8.238153042770202 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.081512594776989 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.898256650040127 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=148.47530514400404 g (allowed None … 85.0); apogee_m=8.149066638349488 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.073369052220057 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.680575853084083 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=151.02530514400402 g (allowed None … 99.0); apogee_m=28.345940563122944 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.827046004888608 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.626365278334706 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=151.02530514400402 g (allowed None … 99.0); apogee_m=27.391813110185268 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.818537101352929 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.932890835053946 m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.574908858199958
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.566791052078152
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.574908858199958
  m/s (allowed 12.0 … None); deployment_speed_m_s=13.415964982304558 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=155.22530514400404 g (allowed None … 113.0); guide_departure_m_s=9.566791052078152
  m/s (allowed 12.0 … None); deployment_speed_m_s=17.871886979205424 m/s (allowed None … 10.0)
- actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- actual-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs

## Assumptions and boundaries

- Length origin: nose tip, +x aft; CAD +Z maps to axial +x. Flight position: OpenRocket local east/north/up, SI units.
- ISA atmosphere, constant wind at every height, zero turbulence; configured seed is retained. Displacement is
  scenario-dependent.
- Native OpenRocket aerodynamics; conical nose, cylindrical sections, three flat trapezoidal fins and tapered collar
  fairing. The thin fairing lip/glue fillet is an approximation documented in BUILD.md.
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
