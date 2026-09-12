# Rocket Workbench report

Run: `design-012`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `2657497cf916f882db4b5c512d6a747eed96b4bdf3e210e81fb8063f40e22922`

## Cases

| Case              | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal |  Deploy m/s | Descent m/s | Drift m |
| ----------------- | ------------------------------------- | -------: | --------: | -------------: | ----------: | ----------: | ------: |
| empty-A8-3-wind0  | completed / outside configured limits |    14.40 |      9.08 |           0.90 |       13.13 |        9.08 |    1.56 |
| empty-A8-3-wind2  | completed / outside configured limits |    14.23 |      9.07 |           0.33 |       14.10 |       10.51 |    1.30 |
| empty-B4-4-wind0  | completed / outside configured limits |    46.32 |     10.96 |           0.45 |       12.36 |        6.22 |    1.77 |
| empty-B4-4-wind2  | completed / outside configured limits |    45.44 |     10.95 |           0.38 |       12.59 |        6.22 |    1.41 |
| empty-C6-3-wind0  | completed / outside configured limits |   137.85 |     11.58 |           0.79 |        9.78 |        6.21 |    0.05 |
| empty-C6-3-wind2  | completed / outside configured limits |   134.88 |     11.58 |           0.53 |       10.30 |        6.21 |   18.19 |
| empty-C6-5-wind0  | completed / outside configured limits |   140.33 |     11.58 |           0.68 |        9.49 |        6.21 |    0.36 |
| empty-C6-5-wind2  | completed / outside configured limits |   137.26 |     11.58 |           0.53 |       10.62 |        6.21 |    8.64 |
| dummy-A8-3-wind0  | completed / outside configured limits |    10.39 |      7.86 |           1.35 | unavailable |       11.60 |    0.58 |
| dummy-A8-3-wind2  | completed / outside configured limits |    10.27 |      7.86 |           0.75 | unavailable |       11.76 |    0.19 |
| dummy-B4-4-wind0  | completed / outside configured limits |    35.11 |      9.65 |           1.24 |       12.49 |        6.70 |    0.58 |
| dummy-B4-4-wind2  | completed / outside configured limits |    34.15 |      9.64 |           0.85 |       17.27 |        6.70 |    7.66 |
| dummy-C6-3-wind0  | completed / outside configured limits |   115.50 |     10.33 |           1.21 |        6.52 |        6.68 |    0.05 |
| dummy-C6-3-wind2  | completed / outside configured limits |   111.57 |     10.33 |           0.93 |        8.20 |        6.68 |    3.02 |
| dummy-C6-5-wind0  | completed / outside configured limits |   116.21 |     10.33 |           0.96 |       11.15 |        6.68 |    0.78 |
| dummy-C6-5-wind2  | completed / outside configured limits |   112.26 |     10.33 |           0.93 |       14.48 |        6.68 |   10.24 |
| actual-A8-3-wind0 | completed / outside configured limits |    10.39 |      7.86 |           1.35 | unavailable |       11.60 |    0.58 |
| actual-A8-3-wind2 | completed / outside configured limits |    10.27 |      7.86 |           0.75 | unavailable |       11.76 |    0.19 |
| actual-B4-4-wind0 | completed / outside configured limits |    35.11 |      9.65 |           1.24 |       12.49 |        6.70 |    0.58 |
| actual-B4-4-wind2 | completed / outside configured limits |    34.15 |      9.64 |           0.85 |       17.27 |        6.70 |    7.66 |
| actual-C6-3-wind0 | completed / outside configured limits |   115.50 |     10.33 |           1.21 |        6.52 |        6.68 |    0.05 |
| actual-C6-3-wind2 | completed / outside configured limits |   111.57 |     10.33 |           0.93 |        8.20 |        6.68 |    3.02 |
| actual-C6-5-wind0 | completed / outside configured limits |   116.21 |     10.33 |           0.96 |       11.15 |        6.68 |    0.78 |
| actual-C6-5-wind2 | completed / outside configured limits |   112.26 |     10.33 |           0.93 |       14.48 |        6.68 |   10.24 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- empty-A8-3-wind0: no engine warnings
- empty-A8-3-wind2: Large angle of attack encountered (21.3°)
- empty-B4-4-wind0: no engine warnings
- empty-B4-4-wind2: no engine warnings
- empty-C6-3-wind0: no engine warnings
- empty-C6-3-wind2: no engine warnings
- empty-C6-5-wind0: no engine warnings
- empty-C6-5-wind2: no engine warnings
- dummy-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- dummy-A8-3-wind2: Large angle of attack encountered (19.5°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
- dummy-B4-4-wind0: no engine warnings
- dummy-B4-4-wind2: no engine warnings
- dummy-C6-3-wind0: no engine warnings
- dummy-C6-3-wind2: no engine warnings
- dummy-C6-5-wind0: no engine warnings
- dummy-C6-5-wind2: no engine warnings
- actual-A8-3-wind0: Flight Event occurred after landing: Ejection charge; Flight Event occurred after landing: Recovery
  device deployment
- actual-A8-3-wind2: Large angle of attack encountered (19.5°); Flight Event occurred after landing: Ejection charge;
  Flight Event occurred after landing: Recovery device deployment
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

- empty-A8-3-wind0: launch_mass_g=116.91628030862944 g (allowed None … 85.0); apogee_m=14.39617097077435 m (allowed 30.0
  … 120.0); guide_departure_m_s=9.077003987102756 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.9035141517080812 cal (allowed 1.0 … None); deployment_speed_m_s=13.125519734178628 m/s
  (allowed None … 10.0); landing_descent_m_s=9.079159595852337 m/s (allowed None … 6.0)
- empty-A8-3-wind2: launch_mass_g=116.91628030862944 g (allowed None … 85.0); apogee_m=14.229833032907017 m (allowed
  30.0 … 120.0); guide_departure_m_s=9.068342269350564 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.32960411175523935 cal (allowed 1.0 … None); deployment_speed_m_s=14.095496470976123 m/s
  (allowed None … 10.0); landing_descent_m_s=10.511110363868855 m/s (allowed None … 6.0)
- empty-B4-4-wind0: launch_mass_g=119.46628030862944 g (allowed None … 99.0); guide_departure_m_s=10.960145817236258 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.45236150107220174 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.363981126700695 m/s (allowed None … 10.0); landing_descent_m_s=6.223107171217801 m/s (allowed
  None … 6.0)
- empty-B4-4-wind2: launch_mass_g=119.46628030862944 g (allowed None … 99.0); guide_departure_m_s=10.95180003784967 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.37969999587751524 cal (allowed 1.0 … None);
  deployment_speed_m_s=12.58611412228553 m/s (allowed None … 10.0); landing_descent_m_s=6.2230363289847705 m/s (allowed
  None … 6.0)
- empty-C6-3-wind0: launch_mass_g=123.66628030862942 g (allowed None … 113.0); apogee_m=137.85238752470835 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.583817349677364 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7914822256869242 cal (allowed 1.0 … None); landing_descent_m_s=6.206628666808584 m/s
  (allowed None … 6.0)
- empty-C6-3-wind2: launch_mass_g=123.66628030862942 g (allowed None … 113.0); apogee_m=134.88019582254307 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.575730331268584 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5338098060986431 cal (allowed 1.0 … None); deployment_speed_m_s=10.298224476034004 m/s
  (allowed None … 10.0); landing_descent_m_s=6.206557915505226 m/s (allowed None … 6.0)
- empty-C6-5-wind0: launch_mass_g=123.66628030862942 g (allowed None … 113.0); apogee_m=140.33468878481395 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.583817349677364 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.6755394130910677 cal (allowed 1.0 … None); landing_descent_m_s=6.206628687801472 m/s
  (allowed None … 6.0)
- empty-C6-5-wind2: launch_mass_g=123.66628030862942 g (allowed None … 113.0); apogee_m=137.2621724936504 m (allowed
  30.0 … 120.0); guide_departure_m_s=11.575730331268584 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.5338098060986431 cal (allowed 1.0 … None); deployment_speed_m_s=10.619101205821591 m/s
  (allowed None … 10.0); landing_descent_m_s=6.206557787533874 m/s (allowed None … 6.0)
- dummy-A8-3-wind0: launch_mass_g=134.91628030862944 g (allowed None … 85.0); apogee_m=10.388392335754927 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.86318277260691 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.59631718673924 m/s (allowed None … 6.0)
- dummy-A8-3-wind2: launch_mass_g=134.91628030862944 g (allowed None … 85.0); apogee_m=10.268103809514685 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.855574354355599 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7521894420459128 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.762934153590466 m/s (allowed None … 6.0)
- dummy-B4-4-wind0: launch_mass_g=137.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.648633758404237 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.49359152034993 m/s (allowed None … 10.0);
  landing_descent_m_s=6.698656334830726 m/s (allowed None … 6.0)
- dummy-B4-4-wind2: launch_mass_g=137.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.640910200305676 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8450524823655653 cal (allowed 1.0 … None);
  deployment_speed_m_s=17.270559336809963 m/s (allowed None … 10.0); landing_descent_m_s=6.698573386247639 m/s (allowed
  None … 6.0)
- dummy-C6-3-wind0: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.33330134435208 m/s
  (allowed 12.0 … None); landing_descent_m_s=6.683349495829965 m/s (allowed None … 6.0)
- dummy-C6-3-wind2: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.326098433408148
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9316843309224474 cal (allowed 1.0 … None);
  landing_descent_m_s=6.68327330800829 m/s (allowed None … 6.0)
- dummy-C6-5-wind0: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.33330134435208 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.964867643311726 cal (allowed 1.0 … None);
  deployment_speed_m_s=11.15019872095567 m/s (allowed None … 10.0); landing_descent_m_s=6.683349529068777 m/s (allowed
  None … 6.0)
- dummy-C6-5-wind2: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.326098433408148
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9316843309224474 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.475609778441578 m/s (allowed None … 10.0); landing_descent_m_s=6.683273330974279 m/s (allowed
  None … 6.0)
- actual-A8-3-wind0: launch_mass_g=134.91628030862944 g (allowed None … 85.0); apogee_m=10.388392335754927 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.86318277260691 m/s (allowed 12.0 … None); deployment_speed_m_s=None m/s (allowed
  None … 10.0); landing_descent_m_s=11.596317186739242 m/s (allowed None … 6.0)
- actual-A8-3-wind2: launch_mass_g=134.91628030862944 g (allowed None … 85.0); apogee_m=10.268103809514685 m (allowed
  30.0 … 120.0); guide_departure_m_s=7.855574354355599 m/s (allowed 12.0 … None);
  minimum_ascent_stability_cal=0.7521894420459114 cal (allowed 1.0 … None); deployment_speed_m_s=None m/s (allowed None
  … 10.0); landing_descent_m_s=11.762934153590466 m/s (allowed None … 6.0)
- actual-B4-4-wind0: launch_mass_g=137.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.648633758404237 m/s
  (allowed 12.0 … None); deployment_speed_m_s=12.493591520349932 m/s (allowed None … 10.0);
  landing_descent_m_s=6.698656334830726 m/s (allowed None … 6.0)
- actual-B4-4-wind2: launch_mass_g=137.46628030862942 g (allowed None … 99.0); guide_departure_m_s=9.640910200305676 m/s
  (allowed 12.0 … None); minimum_ascent_stability_cal=0.8450524823655826 cal (allowed 1.0 … None);
  deployment_speed_m_s=17.270559336810162 m/s (allowed None … 10.0); landing_descent_m_s=6.698573386247641 m/s (allowed
  None … 6.0)
- actual-C6-3-wind0: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.33330134435208
  m/s (allowed 12.0 … None); landing_descent_m_s=6.683349495829965 m/s (allowed None … 6.0)
- actual-C6-3-wind2: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.326098433408148
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9316843309224474 cal (allowed 1.0 … None);
  landing_descent_m_s=6.68327330800829 m/s (allowed None … 6.0)
- actual-C6-5-wind0: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.33330134435208
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.964867643311726 cal (allowed 1.0 … None);
  deployment_speed_m_s=11.15019872095567 m/s (allowed None … 10.0); landing_descent_m_s=6.683349529068777 m/s (allowed
  None … 6.0)
- actual-C6-5-wind2: launch_mass_g=141.66628030862944 g (allowed None … 113.0); guide_departure_m_s=10.326098433408148
  m/s (allowed 12.0 … None); minimum_ascent_stability_cal=0.9316843309224474 cal (allowed 1.0 … None);
  deployment_speed_m_s=14.475609778441717 m/s (allowed None … 10.0); landing_descent_m_s=6.683273330974279 m/s (allowed
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
