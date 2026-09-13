# Commercial 24 mm / BT-60 motor comparison

Current 50 mm cone, 410 mm BT-60 body, 45 mm fins, 145 mm bay and 18-inch chute; passive logger only.
405 flights: nine motor/delay cases × five mass scenarios × three loadings × three winds.
Nominal/upper/heavy-build scenarios and hypothetical +20/+40 g payload sensitivity are distinct.
Extra payload is mass-only at the existing payload CG: no additional hardware packaging or active-control claim.
All numeric passes remain provisional. No site clearance, physical validation, motor purchase or new print-project approval.

## Changed criterion and mount assumptions

This NEW study removes only the inherited 120 m apogee maximum. The 30 m minimum and all guide, stability,
deployment, descent and manufacturer mass limits remain. Historical study results are untouched.
There is no assessed site altitude ceiling or drift boundary; numeric passes do not establish field suitability.
The common long 24 mm mount is estimated at 12 g (18 g heavy-build), with an additional 1 g CD spacer
(1.5 g heavy-build), at explicit axial CGs. Mount ID/OD/length are 24.1/24.8/95 mm, not measured kit dimensions.
Heavy-build combines upper avionics, +20% print mass and +50% mount mass. It is not a full uncertainty sweep.
Chute Cd, payload CG, guide and motor curves are otherwise fixed. The short-motor spacer is lumped in the mount
mass/CG, not a separately modeled printable part. The long mount leaves a tight recovery-wadding gap.
CAD fit checks cover existing avionics only, not the hypothetical extra payload.

## Sources and motor identity

[Commercial mount kit](https://estesrockets.com/products/d-and-e-engine-mount-kit).
Curve digests, thrust/mass histories and engine versions are retained in each results.json.
The bundled C11/D12/E12 curves derive from older NAR data, not measurements of current inventory;
manufacturer advertised impulse/mass may differ. Do not substitute marketing impulse for the simulated curve.
**E12 purchasing hold:** [manufacturer affected-lot bulletin](https://estesrockets.com/pages/e12-service-bulletin),
lots 2K1 25336 00 and 2I3 25303 00; E12 is compared computationally, not recommended for purchase here.

- [C11-3 manufacturer limit](https://estesrockets.com/products/c11-3-engines): 170 g; checked 2026-09-13.
- [C11-5 manufacturer limit](https://estesrockets.com/products/c11-5-engines): 142 g; checked 2026-09-13.
- [D12-3 manufacturer limit](https://estesrockets.com/products/d12-3-engines): 396 g; checked 2026-09-13.
- [D12-5 manufacturer limit](https://estesrockets.com/products/d12-5-engines): 283 g; checked 2026-09-13.
- [D12-7 manufacturer limit](https://estesrockets.com/products/d12-7-engines): 226 g; checked 2026-09-13.
- [E12-4 manufacturer limit](https://estesrockets.com/products/e12-4-engines): 482 g; checked 2026-09-13.
- [E12-6 manufacturer limit](https://estesrockets.com/products/e12-6-engines): 397 g; checked 2026-09-13.
- [E12-8 manufacturer limit](https://estesrockets.com/products/e12-8-engines): 340 g; checked 2026-09-13.

## Loaded performance at winds 0/2 m/s

Pass counts include empty/dummy/actual: six cases at winds 0/2, nine at winds 0/2/4. They are not probabilities.
Dummy and actual use identical mass/CG. The mass-only growth allowance is absent from empty cases.

| Mass scenario | Motor | Apogee m | Powered speed m/s | Guide m/s | Min stability cal | Deployment m/s | Descent m/s | Pass /6 | Pass /9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [nominal](bt60-18-c5-nominal/report.md) | C5-3 | 57.62–59.50 | 22.95–23.10 | 12.51–12.52 | 1.68–1.97 | 7.43–8.62 | 5.08–5.08 | 6/6 | 6/9 |
| [nominal](bt60-24-cd-nominal/report.md) | C11-3 | 74.02–74.74 | 37.08–37.21 | 12.07–12.08 | 1.35–1.79 | 3.77–3.88 | 5.31–5.31 | 0/6 | 0/9 |
| [nominal](bt60-24-cd-nominal/report.md) | C11-5 | 74.22–74.91 | 37.08–37.21 | 12.07–12.08 | 0.91–1.68 | 11.77–12.64 | 5.31–5.31 | 0/6 | 0/9 |
| [nominal](bt60-24-cd-nominal/report.md) | D12-3 | 181.14–182.53 | 63.12–63.27 | 13.02–13.02 | 1.24–1.66 | 19.74–19.78 | 5.28–5.28 | 0/6 | 0/9 |
| [nominal](bt60-24-cd-nominal/report.md) | D12-5 | 196.07–197.85 | 63.12–63.27 | 13.02–13.02 | 1.08–1.55 | 0.49–2.75 | 5.28–5.28 | 5/6 | 5/9 |
| [nominal](bt60-24-cd-nominal/report.md) | D12-7 | 196.07–197.85 | 63.12–63.27 | 13.02–13.02 | 1.08–1.55 | 13.25–18.04 | 5.28–5.28 | 0/6 | 0/9 |
| [nominal](bt60-24-e-nominal/report.md) | E12-4 | 324.52–326.77 | 87.80–87.94 | 13.32–13.32 | 1.05–1.46 | 19.74–19.75 | 5.31–5.31 | 0/6 | 0/9 |
| [nominal](bt60-24-e-nominal/report.md) | E12-6 | 339.30–342.00 | 87.80–87.94 | 13.32–13.32 | 1.05–1.28 | 0.51–3.23 | 5.31–5.31 | 4/6 | 4/9 |
| [nominal](bt60-24-e-nominal/report.md) | E12-8 | 339.30–342.00 | 87.80–87.94 | 13.32–13.32 | 1.05–1.28 | 13.31–18.77 | 5.31–5.31 | 0/6 | 0/9 |
| [upper-avionics](bt60-18-c5-upper-avionics/report.md) | C5-3 | 51.89–53.85 | 21.23–21.37 | 12.17–12.18 | 1.86–2.18 | 8.81–10.10 | 5.21–5.21 | 4/6 | 4/9 |
| [upper-avionics](bt60-24-cd-upper-avionics/report.md) | C11-3 | 68.85–69.56 | 35.27–35.40 | 11.85–11.85 | 1.48–1.97 | 2.57–2.83 | 5.43–5.43 | 0/6 | 0/9 |
| [upper-avionics](bt60-24-cd-upper-avionics/report.md) | C11-5 | 68.92–69.60 | 35.27–35.40 | 11.85–11.85 | 1.08–1.80 | 12.99–14.44 | 5.43–5.43 | 0/6 | 0/9 |
| [upper-avionics](bt60-24-cd-upper-avionics/report.md) | D12-3 | 173.54–175.02 | 60.44–60.58 | 12.89–12.90 | 1.42–1.84 | 18.74–18.76 | 5.41–5.41 | 0/6 | 0/9 |
| [upper-avionics](bt60-24-cd-upper-avionics/report.md) | D12-5 | 186.72–188.58 | 60.44–60.58 | 12.89–12.90 | 1.30–1.64 | 1.39–3.23 | 5.41–5.41 | 5/6 | 7/9 |
| [upper-avionics](bt60-24-cd-upper-avionics/report.md) | D12-7 | 186.72–188.58 | 60.44–60.58 | 12.89–12.90 | 1.30–1.64 | 15.78–19.48 | 5.41–5.41 | 0/6 | 0/9 |
| [upper-avionics](bt60-24-e-upper-avionics/report.md) | E12-4 | 315.22–317.66 | 84.89–85.03 | 13.24–13.24 | 1.22–1.64 | 19.39–19.43 | 5.43–5.43 | 0/6 | 0/9 |
| [upper-avionics](bt60-24-e-upper-avionics/report.md) | E12-6 | 329.30–332.21 | 84.89–85.03 | 13.24–13.24 | 1.22–1.43 | 0.81–3.62 | 5.43–5.43 | 4/6 | 4/9 |
| [upper-avionics](bt60-24-e-upper-avionics/report.md) | E12-8 | 329.30–332.21 | 84.89–85.03 | 13.24–13.24 | 1.22–1.43 | 15.27–19.48 | 5.43–5.43 | 0/6 | 0/9 |
| [heavy-build](bt60-18-c5-heavy-build/report.md) | C5-3 | 40.88–42.97 | 17.74–17.85 | 11.48–11.49 | 1.79–2.17 | 11.34–13.25 | 5.49–5.49 | 2/6 | 2/9 |
| [heavy-build](bt60-24-cd-heavy-build/report.md) | C11-3 | 57.17–57.75 | 31.21–31.34 | 11.35–11.36 | 1.01–1.82 | 0.36–1.35 | 5.73–5.73 | 0/6 | 0/9 |
| [heavy-build](bt60-24-cd-heavy-build/report.md) | C11-5 | 57.17–57.75 | 31.21–31.34 | 11.35–11.36 | 1.01–1.82 | 14.10–15.91 | 5.73–5.73 | 0/6 | 0/9 |
| [heavy-build](bt60-24-cd-heavy-build/report.md) | D12-3 | 154.91–156.53 | 54.17–54.32 | 12.59–12.60 | 1.38–1.80 | 15.93–15.99 | 5.71–5.71 | 0/6 | 0/9 |
| [heavy-build](bt60-24-cd-heavy-build/report.md) | D12-5 | 163.79–165.70 | 54.17–54.32 | 12.59–12.60 | 1.24–1.35 | 3.97–4.97 | 5.71–5.71 | 4/6 | 6/9 |
| [heavy-build](bt60-24-cd-heavy-build/report.md) | D12-7 | 163.79–165.70 | 54.17–54.32 | 12.59–12.60 | 1.24–1.35 | 17.17–21.88 | 5.71–5.71 | 0/6 | 0/9 |
| [heavy-build](bt60-24-e-heavy-build/report.md) | E12-4 | 291.75–294.48 | 77.95–78.09 | 12.89–12.90 | 1.21–1.63 | 18.04–18.19 | 5.72–5.72 | 0/6 | 0/9 |
| [heavy-build](bt60-24-e-heavy-build/report.md) | E12-6 | 303.50–306.69 | 77.95–78.09 | 12.89–12.90 | 1.21–1.32 | 1.99–4.54 | 5.72–5.72 | 4/6 | 4/9 |
| [heavy-build](bt60-24-e-heavy-build/report.md) | E12-8 | 303.50–306.69 | 77.95–78.09 | 12.89–12.90 | 1.21–1.32 | 15.52–20.82 | 5.72–5.72 | 0/6 | 0/9 |
| [inert-plus20](bt60-18-c5-inert-plus20/report.md) | C5-3 | 45.09–47.18 | 19.13–19.25 | 11.75–11.75 | 2.05–2.37 | 10.40–12.11 | 5.37–5.37 | 2/6 | 2/9 |
| [inert-plus20](bt60-24-cd-inert-plus20/report.md) | C11-3 | 62.46–63.14 | 33.06–33.20 | 11.49–11.50 | 1.38–2.18 | 1.02–1.73 | 5.59–5.59 | 0/6 | 0/9 |
| [inert-plus20](bt60-24-cd-inert-plus20/report.md) | C11-5 | 62.47–63.14 | 33.06–33.20 | 11.49–11.50 | 1.28–2.09 | 14.61–16.23 | 5.59–5.59 | 0/6 | 0/9 |
| [inert-plus20](bt60-24-cd-inert-plus20/report.md) | D12-3 | 163.68–165.27 | 57.08–57.22 | 12.82–12.83 | 1.62–2.04 | 17.32–17.34 | 5.56–5.56 | 0/6 | 0/9 |
| [inert-plus20](bt60-24-cd-inert-plus20/report.md) | D12-5 | 174.55–176.51 | 57.08–57.22 | 12.82–12.83 | 1.56–1.69 | 2.69–4.15 | 5.56–5.56 | 5/6 | 7/9 |
| [inert-plus20](bt60-24-cd-inert-plus20/report.md) | D12-7 | 174.55–176.51 | 57.08–57.22 | 12.82–12.83 | 1.56–1.69 | 17.24–21.03 | 5.56–5.56 | 0/6 | 0/9 |
| [inert-plus20](bt60-24-e-inert-plus20/report.md) | E12-4 | 302.68–305.38 | 81.14–81.28 | 12.98–12.99 | 1.42–1.84 | 18.75–18.85 | 5.58–5.58 | 0/6 | 0/9 |
| [inert-plus20](bt60-24-e-inert-plus20/report.md) | E12-6 | 315.59–318.78 | 81.14–81.28 | 12.98–12.99 | 1.42–1.77 | 1.36–4.21 | 5.58–5.58 | 4/6 | 6/9 |
| [inert-plus20](bt60-24-e-inert-plus20/report.md) | E12-8 | 315.59–318.78 | 81.14–81.28 | 12.98–12.99 | 1.42–1.77 | 16.57–20.33 | 5.58–5.58 | 0/6 | 0/9 |
| [inert-plus40](bt60-18-c5-inert-plus40/report.md) | C5-3 | 35.26–37.57 | 15.93–15.99 | 10.92–10.93 | 2.33–2.40 | 12.04–15.23 | 5.65–5.65 | 2/6 | 2/9 |
| [inert-plus40](bt60-24-cd-inert-plus40/report.md) | C11-3 | 52.83–53.46 | 29.71–29.84 | 11.14–11.14 | 1.62–2.46 | 1.51–2.19 | 5.85–5.85 | 0/6 | 0/9 |
| [inert-plus40](bt60-24-cd-inert-plus40/report.md) | C11-5 | 52.83–53.46 | 29.71–29.84 | 11.14–11.14 | 1.62–2.46 | 16.70–19.00 | 5.85–5.85 | 0/6 | 0/9 |
| [inert-plus40](bt60-24-cd-inert-plus40/report.md) | D12-3 | 147.30–149.12 | 51.78–51.93 | 12.47–12.47 | 1.93–2.36 | 14.69–14.82 | 5.83–5.83 | 0/6 | 0/9 |
| [inert-plus40](bt60-24-cd-inert-plus40/report.md) | D12-5 | 154.51–156.61 | 51.78–51.93 | 12.47–12.47 | 1.93–2.03 | 5.13–6.26 | 5.83–5.83 | 5/6 | 7/9 |
| [inert-plus40](bt60-24-cd-inert-plus40/report.md) | D12-7 | 154.51–156.61 | 51.78–51.93 | 12.47–12.47 | 1.93–2.03 | 19.43–23.55 | 5.83–5.83 | 0/6 | 0/9 |
| [inert-plus40](bt60-24-e-inert-plus40/report.md) | E12-4 | 280.82–283.97 | 74.99–75.13 | 12.54–12.55 | 1.72–2.15 | 17.26–17.51 | 5.85–5.85 | 0/6 | 0/9 |
| [inert-plus40](bt60-24-e-inert-plus40/report.md) | E12-6 | 291.27–294.91 | 74.99–75.13 | 12.54–12.55 | 1.71–1.72 | 2.71–5.50 | 5.85–5.85 | 4/6 | 6/9 |
| [inert-plus40](bt60-24-e-inert-plus40/report.md) | E12-8 | 291.27–294.91 | 74.99–75.13 | 12.54–12.55 | 1.71–1.72 | 17.51–21.97 | 5.85–5.85 | 0/6 | 0/9 |

## Failure counts by metric

- nominal / C5-3: {'minimum_ascent_stability_cal': 1, 'deployment_speed_m_s': 2}
- nominal / C11-3: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 2}
- nominal / C11-5: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 5, 'deployment_speed_m_s': 9}
- nominal / D12-3: {'deployment_speed_m_s': 9, 'minimum_ascent_stability_cal': 4}
- nominal / D12-5: {'minimum_ascent_stability_cal': 4}
- nominal / D12-7: {'minimum_ascent_stability_cal': 5, 'deployment_speed_m_s': 9}
- nominal / E12-4: {'minimum_ascent_stability_cal': 5, 'deployment_speed_m_s': 9}
- nominal / E12-6: {'minimum_ascent_stability_cal': 5}
- nominal / E12-8: {'minimum_ascent_stability_cal': 5, 'deployment_speed_m_s': 9}
- upper-avionics / C5-3: {'minimum_ascent_stability_cal': 1, 'deployment_speed_m_s': 4}
- upper-avionics / C11-3: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 2, 'guide_departure_m_s': 6}
- upper-avionics / C11-5: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9, 'guide_departure_m_s': 6}
- upper-avionics / D12-3: {'deployment_speed_m_s': 9, 'minimum_ascent_stability_cal': 2}
- upper-avionics / D12-5: {'minimum_ascent_stability_cal': 2}
- upper-avionics / D12-7: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9}
- upper-avionics / E12-4: {'minimum_ascent_stability_cal': 5, 'deployment_speed_m_s': 9}
- upper-avionics / E12-6: {'minimum_ascent_stability_cal': 5}
- upper-avionics / E12-8: {'minimum_ascent_stability_cal': 5, 'deployment_speed_m_s': 9}
- heavy-build / C5-3: {'minimum_ascent_stability_cal': 1, 'deployment_speed_m_s': 7, 'guide_departure_m_s': 6}
- heavy-build / C11-3: {'launch_mass_g': 9, 'guide_departure_m_s': 9, 'minimum_ascent_stability_cal': 2}
- heavy-build / C11-5: {'launch_mass_g': 9, 'guide_departure_m_s': 9, 'deployment_speed_m_s': 9, 'minimum_ascent_stability_cal': 2}
- heavy-build / D12-3: {'deployment_speed_m_s': 9, 'minimum_ascent_stability_cal': 2}
- heavy-build / D12-5: {'minimum_ascent_stability_cal': 3}
- heavy-build / D12-7: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9, 'launch_mass_g': 6}
- heavy-build / E12-4: {'deployment_speed_m_s': 9, 'minimum_ascent_stability_cal': 4}
- heavy-build / E12-6: {'minimum_ascent_stability_cal': 5}
- heavy-build / E12-8: {'minimum_ascent_stability_cal': 5, 'deployment_speed_m_s': 9}
- inert-plus20 / C5-3: {'minimum_ascent_stability_cal': 1, 'guide_departure_m_s': 6, 'deployment_speed_m_s': 6}
- inert-plus20 / C11-3: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 2, 'guide_departure_m_s': 6}
- inert-plus20 / C11-5: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9, 'guide_departure_m_s': 6}
- inert-plus20 / D12-3: {'deployment_speed_m_s': 9, 'minimum_ascent_stability_cal': 2}
- inert-plus20 / D12-5: {'minimum_ascent_stability_cal': 2}
- inert-plus20 / D12-7: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9}
- inert-plus20 / E12-4: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9}
- inert-plus20 / E12-6: {'minimum_ascent_stability_cal': 3}
- inert-plus20 / E12-8: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9}
- inert-plus40 / C5-3: {'minimum_ascent_stability_cal': 1, 'guide_departure_m_s': 6, 'deployment_speed_m_s': 6}
- inert-plus40 / C11-3: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 2, 'guide_departure_m_s': 6}
- inert-plus40 / C11-5: {'launch_mass_g': 9, 'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9, 'guide_departure_m_s': 6}
- inert-plus40 / D12-3: {'deployment_speed_m_s': 9, 'minimum_ascent_stability_cal': 2}
- inert-plus40 / D12-5: {'minimum_ascent_stability_cal': 2}
- inert-plus40 / D12-7: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9, 'launch_mass_g': 6}
- inert-plus40 / E12-4: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9}
- inert-plus40 / E12-6: {'minimum_ascent_stability_cal': 3}
- inert-plus40 / E12-8: {'minimum_ascent_stability_cal': 3, 'deployment_speed_m_s': 9}

## Downloads

[Machine-readable comparison](comparison.json) | [Flat comparison CSV](comparison.csv)

Each linked case report has corresponding config.yaml, results.json, results.csv, mass-ledger.json,
cad/assembly.step and individual motor/load/wind ORK files in the same directory.
