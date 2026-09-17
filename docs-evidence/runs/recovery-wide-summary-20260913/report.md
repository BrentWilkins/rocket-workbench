# Expanded recovery uncertainty comparison

864 deterministic flights; 192 planned dummy/logger and 96 empty diagnostics per design. Scenario counts are not
reliability probabilities.

Bounds: print mass ×1/1.2, payload CG ±5 mm, wind 0/2/4 m/s, chute Cd 0.53/1.04, mount mass ×1/1.5. Upper avionics and
+20% chute mass are paired, not independently varied. Generic packing remains provisional; sourced chute mass is a
literature specimen, not our hardware.

| Design                        | Planned passes / 192 | Altitude m    | Speed m/s   | Descent m/s | Drift m     |
| ----------------------------- | -------------------- | ------------- | ----------- | ----------- | ----------- |
| apogee24-body500-heavy0-cd053 | 192                  | 146.40–187.74 | 50.78–60.61 | 3.44–5.22   | 0.04–165.24 |
| delta-chute20-body430-nominal | 156                  | 151.00–193.99 | 51.87–62.00 | 4.08–6.21   | 0.05–135.75 |
| delta-chute22-body460-nominal | 192                  | 145.12–187.64 | 50.40–60.36 | 3.76–5.72   | 0.04–145.07 |

Drift is horizontal landing displacement from the pad under the modeled uniform winds. It is not a landing-zone
guarantee. CFD, final retention hardware and physical validation remain separate.
