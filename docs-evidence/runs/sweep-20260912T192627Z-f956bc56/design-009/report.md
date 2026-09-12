# Rocket Workbench report

Run: `design-009`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `85494b0804c805eecc730339d3c184fcfb22b7a44669364a1d3f5f6c30183b8e`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    15.24 |      9.32 |           0.48 |       14.04 |        8.10 |    1.37 |
| empty-A8-3-wind2  | completed / outside configured limits |    15.14 |      9.31 |           0.04 |       14.69 |        8.89 |    2.10 |
| empty-B4-4-wind0  | completed / outside configured limits |    48.93 |     11.17 |           0.36 |       12.90 |        6.15 |    1.30 |
| empty-B4-4-wind2  | completed / outside configured limits |    48.31 |     11.16 |           0.04 |       13.72 |        6.15 |    6.09 |
| empty-C6-3-wind0  | completed / outside configured limits |   144.55 |     11.81 |           0.38 |       11.14 |        6.13 |    0.05 |
| empty-C6-3-wind2  | completed / outside configured limits |   142.77 |     11.80 |           0.15 |       11.25 |        6.13 |   29.25 |
| empty-C6-5-wind0  | completed / outside configured limits |   148.11 |     11.81 |           0.38 |        8.47 |        6.13 |    0.11 |
| empty-C6-5-wind2  | completed / outside configured limits |   146.28 |     11.80 |           0.08 |        8.02 |        6.13 |   23.62 |
| dummy-A8-3-wind0  | completed / outside configured limits |    10.93 |      8.03 |           0.93 | unavailable |       12.44 |    0.63 |
| dummy-A8-3-wind2  | completed / outside configured limits |    10.86 |      8.02 |           0.46 | unavailable |       13.40 |    0.78 |
| dummy-B4-4-wind0  | completed / outside configured limits |    36.89 |      9.84 |           0.88 |       13.87 |        6.63 |    2.46 |
| dummy-B4-4-wind2  | completed / outside configured limits |    36.09 |      9.84 |           0.48 |       15.06 |        6.63 |    2.26 |
| dummy-C6-3-wind0  | completed / outside configured limits |   121.01 |     10.52 |           0.80 |        7.69 |        6.61 |    0.05 |
| dummy-C6-3-wind2  | completed / outside configured limits |   117.89 |     10.51 |           0.55 |        8.69 |        6.61 |    9.60 |
| dummy-C6-5-wind0  | completed / outside configured limits |   122.20 |     10.52 |           0.50 |       11.15 |        6.61 |    0.54 |
| dummy-C6-5-wind2  | completed / outside configured limits |   119.08 |     10.51 |           0.55 |       12.74 |        6.61 |    1.31 |
| actual-A8-3-wind0 | completed / outside configured limits |    10.93 |      8.03 |           0.93 | unavailable |       12.44 |    0.63 |
| actual-A8-3-wind2 | completed / outside configured limits |    10.86 |      8.02 |           0.46 | unavailable |       13.40 |    0.78 |
| actual-B4-4-wind0 | completed / outside configured limits |    36.89 |      9.84 |           0.88 |       13.87 |        6.63 |    2.46 |
| actual-B4-4-wind2 | completed / outside configured limits |    36.09 |      9.84 |           0.48 |       15.06 |        6.63 |    2.26 |
| actual-C6-3-wind0 | completed / outside configured limits |   121.01 |     10.52 |           0.80 |        7.69 |        6.61 |    0.05 |
| actual-C6-3-wind2 | completed / outside configured limits |   117.89 |     10.51 |           0.55 |        8.69 |        6.61 |    9.60 |
| actual-C6-5-wind0 | completed / outside configured limits |   122.20 |     10.52 |           0.50 |       11.15 |        6.61 |    0.54 |
| actual-C6-5-wind2 | completed / outside configured limits |   119.08 |     10.51 |           0.55 |       12.74 |        6.61 |    1.31 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: no engine warnings
- empty-A8-3-wind2: no engine warnings
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
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

## Missing measurements / physical checks

- Exact XIAO board/camera/antenna identity and measured envelope
- Battery identity, connector/wire envelopes and retention measurements
- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: 18 mm motor mount tube, thrust ring, hook, two centering rings and adhesive
- Measured mass and balance: Nominal 305 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=114.14866032498868 g (allowed None … 85.0); apogee_m=15.23772448549372 m (allowed 30.0
  … 120.0); guide_departure_m_s=9.318030070225483 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.48145907300865687 cal (allowed 1.0 … None); deployment_speed_m_s=14.044334931695037 m/s
  (allowed None … 10.0); landing_descent_m_s=8.100313062352443 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=114.14866032498868 g (allowed None … 85.0); apogee_m=15.13655107486967 m (allowed 30.0
  … 120.0); guide_departure_m_s=9.309768536019142 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.03957310825943255 cal (allowed 1.0 … None); deployment_speed_m_s=14.688575609738551 m/s
  (allowed None … 10.0); landing_descent_m_s=8.893651056245336 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=116.69866032498868 g (allowed None … 99.0); guide_departure_m_s=11.172467874678654 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.36458058123364195 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.90460805830642 m/s (allowed None … 10.0); landing_descent_m_s=6.146728530118448 m/s (allowed
  None … 6.0)
- empty-B4-4-wind2: launch_mass_g=116.69866032498868 g (allowed None … 99.0); guide_departure_m_s=11.164324846476294 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.04179594501305545 cal (allowed 1.0 … None);
  deployment_speed_m_s=13.72089224802069 m/s (allowed None … 10.0); landing_descent_m_s=6.146658453398357 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=120.89866032498868 g (allowed None … 113.0); apogee_m=144.54746123384206 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.811948187323546 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.3814552222104303 cal (allowed 1.0 … None); deployment_speed_m_s=11.139344710430828 m/s
  (allowed None … 10.0); landing_descent_m_s=6.1300448547722315 m/s (allowed None … 6.0)
- empty-C6-3-wind2: launch_mass_g=120.89866032498868 g (allowed None … 113.0); apogee_m=142.7709832297924 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.804326898286746 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.15182851605148984 cal (allowed 1.0 … None); deployment_speed_m_s=11.249746635054873 m/s
  (allowed None … 10.0); landing_descent_m_s=6.129974913677963 m/s (allowed None … 6.0)
- empty-C6-5-wind0: launch_mass_g=120.89866032498868 g (allowed None … 113.0); apogee_m=148.1075555537224 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.811948187323546 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.3803666357410296 cal (allowed 1.0 … None); landing_descent_m_s=6.130044766886081 m/s
  (allowed None … 6.0)
- empty-C6-5-wind2: launch_mass_g=120.89866032498868 g (allowed None … 113.0); apogee_m=146.27654465747068 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.804326898286746 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.0752186472797564 cal (allowed 1.0 … None); landing_descent_m_s=6.129974889593245 m/s
  (allowed None … 6.0)
- dummy-A8-3-wind0: launch_mass_g=132.14866032498867 g (allowed None … 85.0); apogee_m=10.928686398928152 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.02784417628604 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9346948794317392 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=12.43773331951871 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=132.14866032498867 g (allowed None … 85.0); apogee_m=10.856148124168655 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.020724321102746 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.46476733559993755 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=13.402435675047037 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=134.69866032498868 g (allowed None … 99.0); guide_departure_m_s=9.843346504785293 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8837836175895379 cal (allowed 1.0 … None);
  deployment_speed_m_s=13.865113950557854 m/s (allowed None … 10.0); landing_descent_m_s=6.62775449836057 m/s (allowed
  None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=134.69866032498868 g (allowed None … 99.0); guide_departure_m_s=9.83606101320696 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.4786078295888109 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.055489292445776 m/s (allowed None … 10.0); landing_descent_m_s=6.627679883679546 m/s (allowed
  None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=138.89866032498867 g (allowed None … 113.0); apogee_m=121.00735781493694 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.517624363695043 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8045507097800424 cal (allowed 1.0 … None); landing_descent_m_s=6.612285101261056 m/s
  (allowed None … 6.0)
- dummy-C6-3-wind2: launch_mass_g=138.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.511086301450836
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5543791240386026 cal (allowed 1.0 … None);
  landing_descent_m_s=6.612209694466448 m/s (allowed None … 6.0)
- dummy-C6-5-wind0: launch_mass_g=138.89866032498867 g (allowed None … 113.0); apogee_m=122.19613663851956 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.517624363695043 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5010456635323461 cal (allowed 1.0 … None); deployment_speed_m_s=11.150642149805568 m/s
  (allowed None … 10.0); landing_descent_m_s=6.612285099441378 m/s (allowed None … 6.0)
- dummy-C6-5-wind2: launch_mass_g=138.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.511086301450836
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5543791240386026 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.74476128687045 m/s (allowed None … 10.0); landing_descent_m_s=6.612209694216728 m/s (allowed
  None … 6.0)
- actual-A8-3-wind0: launch_mass_g=132.14866032498867 g (allowed None … 85.0); apogee_m=10.928686398928152 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.02784417628604 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9346948794317392 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=12.43773331951871 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=132.14866032498867 g (allowed None … 85.0); apogee_m=10.856148124168655 m (allowed
  30.0 … 120.0); guide_departure_m_s=8.020724321102746 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.4647673355999369 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=13.402435675047037 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=134.69866032498868 g (allowed None … 99.0); guide_departure_m_s=9.843346504785293 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8837836175895379 cal (allowed 1.0 … None);
  deployment_speed_m_s=13.865113950557854 m/s (allowed None … 10.0); landing_descent_m_s=6.62775449836057 m/s (allowed
  None … 6.0)
- actual-B4-4-wind2: launch_mass_g=134.69866032498868 g (allowed None … 99.0); guide_departure_m_s=9.83606101320696 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.47860782958881287 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.055489292445714 m/s (allowed None … 10.0); landing_descent_m_s=6.627679883679546 m/s (allowed
  None … 6.0)
- actual-C6-3-wind0: launch_mass_g=138.89866032498867 g (allowed None … 113.0); apogee_m=121.00735781493694 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.517624363695043 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.8045507097800424 cal (allowed 1.0 … None); landing_descent_m_s=6.612285101261056 m/s
  (allowed None … 6.0)
- actual-C6-3-wind2: launch_mass_g=138.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.511086301450836
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5543791240386026 cal (allowed 1.0 … None);
  landing_descent_m_s=6.612209694466448 m/s (allowed None … 6.0)
- actual-C6-5-wind0: launch_mass_g=138.89866032498867 g (allowed None … 113.0); apogee_m=122.19613663851956 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.517624363695043 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5010456635323441 cal (allowed 1.0 … None); deployment_speed_m_s=11.150642149805568 m/s
  (allowed None … 10.0); landing_descent_m_s=6.612285099441378 m/s (allowed None … 6.0)
- actual-C6-5-wind2: launch_mass_g=138.89866032498867 g (allowed None … 113.0); guide_departure_m_s=10.511086301450836
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.5543791240386026 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.744761286870384 m/s (allowed None … 10.0); landing_descent_m_s=6.6122096942167286 m/s (allowed
  None … 6.0)

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
  "repository_revision": null
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
