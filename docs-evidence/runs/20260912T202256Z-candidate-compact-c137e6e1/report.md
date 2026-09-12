# Rocket Workbench report

Run: `20260912T202256Z-candidate-compact-c137e6e1`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `8209cbca95caf032b329156beeac7df9d19e307c3bfd6708a18924b921c89a4e`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    12.33 |      8.50 |           1.34 | unavailable |       11.29 |    1.02 |
| empty-A8-3-wind2  | completed / outside configured limits |    12.16 |      8.49 |           0.69 | unavailable |       12.06 |    0.62 |
| empty-B4-4-wind0  | completed / outside configured limits |    40.36 |     10.34 |           1.13 |       11.45 |        5.16 |    1.51 |
| empty-B4-4-wind2  | completed / outside configured limits |    39.41 |     10.33 |           0.85 |       15.11 |        5.16 |    1.91 |
| empty-C6-3-wind0  | completed / outside configured limits |   124.12 |     10.98 |           1.33 |        7.44 |        5.14 |    0.05 |
| empty-C6-3-wind2  | completed / outside configured limits |   120.57 |     10.97 |           0.99 |        8.55 |        5.14 |   19.55 |
| empty-C6-5-wind0  | completed / outside configured limits |   125.51 |     10.98 |           1.11 |       10.50 |        5.14 |    0.73 |
| empty-C6-5-wind2  | completed / outside configured limits |   121.86 |     10.97 |           0.99 |       13.21 |        5.14 |    6.93 |
| empty-C5-3-wind0  | completed / incomplete inputs         |   105.25 |     14.37 |           1.33 |        1.69 |        5.15 |    0.05 |
| empty-C5-3-wind2  | completed / incomplete inputs         |   103.75 |     14.36 |           1.06 |        3.03 |        5.15 |   25.29 |
| dummy-A8-3-wind0  | completed / outside configured limits |     9.03 |      7.36 |           1.85 | unavailable |       11.14 |    0.48 |
| dummy-A8-3-wind2  | completed / outside configured limits |     8.91 |      7.36 |           1.16 | unavailable |       10.91 |    0.28 |
| dummy-B4-4-wind0  | completed / outside configured limits |    30.87 |      9.12 |           1.86 |       15.93 |        5.53 |    1.06 |
| dummy-B4-4-wind2  | completed / outside configured limits |    29.88 |      9.11 |           1.36 |       19.14 |        5.53 |    9.11 |
| dummy-C6-3-wind0  | completed / outside configured limits |   103.77 |      9.83 |           1.80 |        4.29 |        5.51 |    0.04 |
| dummy-C6-3-wind2  | completed / outside configured limits |    99.41 |      9.82 |           1.43 |        7.19 |        5.51 |    5.00 |
| dummy-C6-5-wind0  | completed / outside configured limits |   104.02 |      9.83 |           1.74 |       12.00 |        5.51 |    0.40 |
| dummy-C6-5-wind2  | completed / outside configured limits |    99.64 |      9.82 |           1.43 |       16.65 |        5.51 |   11.43 |
| dummy-C5-3-wind0  | completed / incomplete inputs         |    85.58 |     13.67 |           1.73 |        1.71 |        5.52 |    0.04 |
| dummy-C5-3-wind2  | completed / incomplete inputs         |    83.83 |     13.66 |           1.53 |        3.83 |        5.52 |   12.89 |
| actual-A8-3-wind0 | completed / outside configured limits |     9.03 |      7.36 |           1.85 | unavailable |       11.14 |    0.48 |
| actual-A8-3-wind2 | completed / outside configured limits |     8.91 |      7.36 |           1.16 | unavailable |       10.91 |    0.28 |
| actual-B4-4-wind0 | completed / outside configured limits |    30.87 |      9.12 |           1.86 |       15.93 |        5.53 |    1.06 |
| actual-B4-4-wind2 | completed / outside configured limits |    29.88 |      9.11 |           1.36 |       19.14 |        5.53 |    9.11 |
| actual-C6-3-wind0 | completed / outside configured limits |   103.77 |      9.83 |           1.80 |        4.29 |        5.51 |    0.04 |
| actual-C6-3-wind2 | completed / outside configured limits |    99.41 |      9.82 |           1.43 |        7.19 |        5.51 |    5.00 |
| actual-C6-5-wind0 | completed / outside configured limits |   104.02 |      9.83 |           1.74 |       12.00 |        5.51 |    0.40 |
| actual-C6-5-wind2 | completed / outside configured limits |    99.64 |      9.82 |           1.43 |       16.65 |        5.51 |   11.43 |
| actual-C5-3-wind0 | completed / incomplete inputs         |    85.58 |     13.67 |           1.73 |        1.71 |        5.52 |    0.04 |
| actual-C5-3-wind2 | completed / incomplete inputs         |    83.83 |     13.66 |           1.53 |        3.83 |        5.52 |   12.89 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- empty-A8-3-wind2: Large angle of attack encountered (21.9°); Flight Event occurred after landing: Ejection charge;
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
- dummy-A8-3-wind2: Large angle of attack encountered (18.9°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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
- actual-A8-3-wind2: Large angle of attack encountered (18.9°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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
- Measured mass and balance: Nominal 381 mm parachute and lines
- Measured mass and balance: Kevlar leader, elastic harness, swivel and knots
- Measured mass and balance: Recovery wadding
- Measured mass and balance: Two paper launch lugs and adhesive
- Measured mass and balance: Bulkhead eye bolt, washers, nuts, sled screws and cable ties
- Measured mass and balance: Fin collar adhesive and tapered lip fillet
- Measured mass and balance: Flame-resistant bay shield and perimeter seal allowance
- Assembled mass/CG, print fit, attachment strength and recovery separation checks

## Per-case criterion failures

- empty-A8-3-wind0: launch_mass_g=125.0466309472131 g (allowed None … 85.0); apogee_m=12.330894729899434 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.500065684026053 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.2882499907201 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=125.0466309472131 g (allowed None … 85.0); apogee_m=12.15925087394796 m (allowed 30.0
  … 120.0); guide_departure_m_s=8.490997172661192 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6857000192950468 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=12.055553429663567 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=127.59663094721313 g (allowed None … 99.0); guide_departure_m_s=10.342164786549672 m/s
  (allowed 12.0 … None); deployment_speed_m_s=11.44623551438998 m/s (allowed None … 10.0)
- empty-B4-4-wind2: launch_mass_g=127.59663094721313 g (allowed None … 99.0); guide_departure_m_s=10.332988763560278 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8477681026780299 cal (allowed 1.0 … None);
  deployment_speed_m_s=15.105986096532915 m/s (allowed None … 10.0)
- empty-C6-3-wind0: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=124.12451081286807 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.980537639429194 m/s (allowed 12.0 … None)
- empty-C6-3-wind2: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=120.5701819441699 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.972077614174976 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9932853419794886 cal (allowed 1.0 … None)
- empty-C6-5-wind0: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=125.50745671415203 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.980537639429194 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.49623164879077 m/s (allowed None … 10.0)
- empty-C6-5-wind2: launch_mass_g=131.79663094721312 g (allowed None … 113.0); apogee_m=121.8596880732461 m (allowed
  30.0 … 120.0); guide_departure_m_s=10.972077614174976 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9932853419794886 cal (allowed 1.0 … None); deployment_speed_m_s=13.210769943620125 m/s
  (allowed None … 10.0)
- empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- dummy-A8-3-wind0: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=9.025341909994976 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.363271703590972 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.136941855786377 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=8.907970602356652 m (allowed 30.0
  … 120.0); guide_departure_m_s=7.355562876760579 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=10.905662360126703 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=145.59663094721313 g (allowed None … 99.0); guide_departure_m_s=9.118282704660938 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.932908260130912 m/s (allowed None … 10.0)
- dummy-B4-4-wind2: launch_mass_g=145.59663094721313 g (allowed None … 99.0); apogee_m=29.880206310462455 m (allowed
  30.0 … 120.0); guide_departure_m_s=9.110287425180893 m/s (allowed 12.0 … None);
  deployment_speed_m_s=19.143627206973008 m/s (allowed None … 10.0)
- dummy-C6-3-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788 m/s
  (allowed 12.0 … None)
- dummy-C6-3-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342 m/s
  (allowed 12.0 … None)
- dummy-C6-5-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.004868939369821 m/s (allowed None … 10.0)
- dummy-C6-5-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342 m/s
  (allowed 12.0 … None); deployment_speed_m_s=16.65300581955413 m/s (allowed None … 10.0)
- dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- dummy-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- actual-A8-3-wind0: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=9.025341909994976 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.363271703590972 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.136941855786379 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=143.04663094721312 g (allowed None … 85.0); apogee_m=8.907970602356652 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.355562876760579 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=10.905662360126703 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=145.59663094721313 g (allowed None … 99.0); guide_departure_m_s=9.118282704660938 m/s
  (allowed 12.0 … None); deployment_speed_m_s=15.932908260130912 m/s (allowed None … 10.0)
- actual-B4-4-wind2: launch_mass_g=145.59663094721313 g (allowed None … 99.0); apogee_m=29.88020631046247 m (allowed
  30.0 … 120.0); guide_departure_m_s=9.110287425180893 m/s (allowed 12.0 … None); deployment_speed_m_s=19.143627206973
  m/s (allowed None … 10.0)
- actual-C6-3-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788
  m/s (allowed 12.0 … None)
- actual-C6-3-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342
  m/s (allowed 12.0 … None)
- actual-C6-5-wind0: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.830917164420788
  m/s (allowed 12.0 … None); deployment_speed_m_s=12.004868939369816 m/s (allowed None … 10.0)
- actual-C6-5-wind2: launch_mass_g=149.79663094721312 g (allowed None … 113.0); guide_departure_m_s=9.823405148400342
  m/s (allowed 12.0 … None); deployment_speed_m_s=16.653005819554092 m/s (allowed None … 10.0)
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
