# Rocket Workbench report

Run: `stress-20260913T040736Z-ead8ec46`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `6e976b8bdb97b87d54ef0ff38071be05e74a912decec08f9e624bb4b14e34055`

## Cases

| Case                | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| ------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        5.38 |    0.00 |           11.96 |            12.96 |             26.99 |
| 0-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        5.38 |    8.48 |           11.95 |            12.95 |             26.82 |
| 0-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        5.38 |   16.37 |           11.94 |            12.94 |             26.39 |
| 0-dummy-C5-3-wind0  | completed / incomplete inputs         |    51.82 |     12.12 |           2.51 |       9.27 |        5.87 |    0.27 |            9.97 |            10.97 |             20.74 |
| 0-dummy-C5-3-wind2  | completed / outside configured limits |    49.71 |     12.11 |           2.23 |      10.90 |        5.87 |    5.30 |            9.96 |            10.96 |             20.60 |
| 0-dummy-C5-3-wind4  | completed / outside configured limits |    44.61 |     12.11 |           1.95 |      14.23 |        5.87 |   11.44 |            9.96 |            10.96 |             20.26 |
| 0-actual-C5-3-wind0 | completed / incomplete inputs         |    51.82 |     12.12 |           2.51 |       9.27 |        5.87 |    0.27 |            9.97 |            10.97 |             20.74 |
| 0-actual-C5-3-wind2 | completed / outside configured limits |    49.71 |     12.11 |           2.23 |      10.90 |        5.87 |    5.30 |            9.96 |            10.96 |             20.60 |
| 0-actual-C5-3-wind4 | completed / outside configured limits |    44.61 |     12.11 |           1.95 |      14.23 |        5.87 |   11.44 |            9.96 |            10.96 |             20.26 |
| 1-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        4.39 |    0.01 |           11.96 |            12.96 |             26.99 |
| 1-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        4.39 |   14.83 |           11.95 |            12.95 |             26.82 |
| 1-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        4.39 |   27.95 |           11.94 |            12.94 |             26.39 |
| 1-dummy-C5-3-wind0  | completed / incomplete inputs         |    51.82 |     12.12 |           2.51 |       9.27 |        4.79 |    0.22 |            9.97 |            10.97 |             20.74 |
| 1-dummy-C5-3-wind2  | completed / outside configured limits |    49.71 |     12.11 |           2.23 |      10.90 |        4.79 |    1.34 |            9.96 |            10.96 |             20.60 |
| 1-dummy-C5-3-wind4  | completed / outside configured limits |    44.61 |     12.11 |           1.95 |      14.23 |        4.79 |    4.78 |            9.96 |            10.96 |             20.26 |
| 1-actual-C5-3-wind0 | completed / incomplete inputs         |    51.82 |     12.12 |           2.51 |       9.27 |        4.79 |    0.22 |            9.97 |            10.97 |             20.74 |
| 1-actual-C5-3-wind2 | completed / outside configured limits |    49.71 |     12.11 |           2.23 |      10.90 |        4.79 |    1.34 |            9.96 |            10.96 |             20.60 |
| 1-actual-C5-3-wind4 | completed / outside configured limits |    44.61 |     12.11 |           1.95 |      14.23 |        4.79 |    4.78 |            9.96 |            10.96 |             20.26 |
| 2-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        5.38 |    0.00 |           11.96 |            12.96 |             26.99 |
| 2-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        5.38 |    8.48 |           11.95 |            12.95 |             26.82 |
| 2-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        5.38 |   16.37 |           11.94 |            12.94 |             26.39 |
| 2-dummy-C5-3-wind0  | completed / incomplete inputs         |    51.82 |     12.12 |           2.47 |       9.27 |        5.87 |    0.27 |            9.97 |            10.97 |             20.74 |
| 2-dummy-C5-3-wind2  | completed / outside configured limits |    49.71 |     12.11 |           2.19 |      10.90 |        5.87 |    5.32 |            9.96 |            10.96 |             20.60 |
| 2-dummy-C5-3-wind4  | completed / outside configured limits |    44.62 |     12.11 |           1.92 |      14.22 |        5.87 |   11.43 |            9.96 |            10.96 |             20.26 |
| 2-actual-C5-3-wind0 | completed / incomplete inputs         |    51.82 |     12.12 |           2.47 |       9.27 |        5.87 |    0.27 |            9.97 |            10.97 |             20.74 |
| 2-actual-C5-3-wind2 | completed / outside configured limits |    49.71 |     12.11 |           2.19 |      10.90 |        5.87 |    5.32 |            9.96 |            10.96 |             20.60 |
| 2-actual-C5-3-wind4 | completed / outside configured limits |    44.62 |     12.11 |           1.92 |      14.22 |        5.87 |   11.43 |            9.96 |            10.96 |             20.26 |
| 3-empty-C5-3-wind0  | completed / incomplete inputs         |    72.59 |     13.20 |           1.05 |       4.52 |        4.39 |    0.01 |           11.96 |            12.96 |             26.99 |
| 3-empty-C5-3-wind2  | completed / incomplete inputs         |    70.82 |     13.19 |           1.49 |       5.70 |        4.39 |   14.83 |           11.95 |            12.95 |             26.82 |
| 3-empty-C5-3-wind4  | completed / incomplete inputs         |    66.30 |     13.19 |           1.29 |       8.95 |        4.39 |   27.95 |           11.94 |            12.94 |             26.39 |
| 3-dummy-C5-3-wind0  | completed / incomplete inputs         |    51.82 |     12.12 |           2.47 |       9.27 |        4.79 |    0.22 |            9.97 |            10.97 |             20.74 |
| 3-dummy-C5-3-wind2  | completed / outside configured limits |    49.71 |     12.11 |           2.19 |      10.90 |        4.79 |    1.36 |            9.96 |            10.96 |             20.60 |
| 3-dummy-C5-3-wind4  | completed / outside configured limits |    44.62 |     12.11 |           1.92 |      14.22 |        4.79 |    4.77 |            9.96 |            10.96 |             20.26 |
| 3-actual-C5-3-wind0 | completed / incomplete inputs         |    51.82 |     12.12 |           2.47 |       9.27 |        4.79 |    0.22 |            9.97 |            10.97 |             20.74 |
| 3-actual-C5-3-wind2 | completed / outside configured limits |    49.71 |     12.11 |           2.19 |      10.90 |        4.79 |    1.36 |            9.96 |            10.96 |             20.60 |
| 3-actual-C5-3-wind4 | completed / outside configured limits |    44.62 |     12.11 |           1.92 |      14.22 |        4.79 |    4.77 |            9.96 |            10.96 |             20.26 |
| 4-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        5.65 |    0.10 |           10.78 |            11.78 |             23.34 |
| 4-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        5.65 |    0.68 |           10.77 |            11.77 |             23.17 |
| 4-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        5.65 |    0.77 |           10.76 |            11.76 |             22.75 |
| 4-dummy-C5-3-wind0  | completed / outside configured limits |    43.09 |     11.53 |           2.62 |      10.99 |        6.13 |    0.55 |            9.11 |            10.11 |             17.90 |
| 4-dummy-C5-3-wind2  | completed / outside configured limits |    40.89 |     11.53 |           2.24 |      13.41 |        6.13 |   10.94 |            9.11 |            10.10 |             17.81 |
| 4-dummy-C5-3-wind4  | completed / outside configured limits |    35.86 |     11.53 |           1.96 |      16.73 |        6.12 |   22.10 |            9.10 |            10.10 |             17.60 |
| 4-actual-C5-3-wind0 | completed / outside configured limits |    43.09 |     11.53 |           2.62 |      10.99 |        6.13 |    0.55 |            9.11 |            10.11 |             17.90 |
| 4-actual-C5-3-wind2 | completed / outside configured limits |    40.89 |     11.53 |           2.24 |      13.41 |        6.13 |   10.94 |            9.11 |            10.10 |             17.81 |
| 4-actual-C5-3-wind4 | completed / outside configured limits |    35.86 |     11.53 |           1.96 |      16.73 |        6.12 |   22.10 |            9.10 |            10.10 |             17.60 |
| 5-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        4.62 |    0.08 |           10.78 |            11.78 |             23.34 |
| 5-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        4.62 |    5.63 |           10.77 |            11.77 |             23.17 |
| 5-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        4.62 |    9.45 |           10.76 |            11.76 |             22.75 |
| 5-dummy-C5-3-wind0  | completed / outside configured limits |    43.09 |     11.53 |           2.62 |      10.99 |        5.00 |    0.48 |            9.11 |            10.11 |             17.90 |
| 5-dummy-C5-3-wind2  | completed / outside configured limits |    40.89 |     11.53 |           2.24 |      13.41 |        5.00 |    7.95 |            9.11 |            10.10 |             17.81 |
| 5-dummy-C5-3-wind4  | completed / outside configured limits |    35.86 |     11.53 |           1.96 |      16.73 |        5.00 |   17.47 |            9.10 |            10.10 |             17.60 |
| 5-actual-C5-3-wind0 | completed / outside configured limits |    43.09 |     11.53 |           2.62 |      10.99 |        5.00 |    0.48 |            9.11 |            10.11 |             17.90 |
| 5-actual-C5-3-wind2 | completed / outside configured limits |    40.89 |     11.53 |           2.24 |      13.41 |        5.00 |    7.95 |            9.11 |            10.10 |             17.81 |
| 5-actual-C5-3-wind4 | completed / outside configured limits |    35.86 |     11.53 |           1.96 |      16.73 |        5.00 |   17.47 |            9.10 |            10.10 |             17.60 |
| 6-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        5.65 |    0.10 |           10.78 |            11.78 |             23.34 |
| 6-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        5.65 |    0.68 |           10.77 |            11.77 |             23.17 |
| 6-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        5.65 |    0.77 |           10.76 |            11.76 |             22.75 |
| 6-dummy-C5-3-wind0  | completed / outside configured limits |    43.09 |     11.53 |           2.59 |      10.99 |        6.13 |    0.55 |            9.11 |            10.11 |             17.90 |
| 6-dummy-C5-3-wind2  | completed / outside configured limits |    40.89 |     11.53 |           2.20 |      13.41 |        6.13 |   10.95 |            9.11 |            10.10 |             17.81 |
| 6-dummy-C5-3-wind4  | completed / outside configured limits |    35.87 |     11.53 |           1.92 |      16.73 |        6.12 |   22.07 |            9.10 |            10.10 |             17.60 |
| 6-actual-C5-3-wind0 | completed / outside configured limits |    43.09 |     11.53 |           2.59 |      10.99 |        6.13 |    0.55 |            9.11 |            10.11 |             17.90 |
| 6-actual-C5-3-wind2 | completed / outside configured limits |    40.89 |     11.53 |           2.20 |      13.41 |        6.13 |   10.95 |            9.11 |            10.10 |             17.81 |
| 6-actual-C5-3-wind4 | completed / outside configured limits |    35.87 |     11.53 |           1.92 |      16.73 |        6.12 |   22.07 |            9.10 |            10.10 |             17.60 |
| 7-empty-C5-3-wind0  | completed / incomplete inputs         |    60.22 |     12.66 |           1.97 |       7.30 |        4.62 |    0.08 |           10.78 |            11.78 |             23.34 |
| 7-empty-C5-3-wind2  | completed / incomplete inputs         |    58.30 |     12.65 |           1.64 |       8.48 |        4.62 |    5.63 |           10.77 |            11.77 |             23.17 |
| 7-empty-C5-3-wind4  | completed / outside configured limits |    53.56 |     12.65 |           1.37 |      11.76 |        4.62 |    9.45 |           10.76 |            11.76 |             22.75 |
| 7-dummy-C5-3-wind0  | completed / outside configured limits |    43.09 |     11.53 |           2.59 |      10.99 |        5.00 |    0.48 |            9.11 |            10.11 |             17.90 |
| 7-dummy-C5-3-wind2  | completed / outside configured limits |    40.89 |     11.53 |           2.20 |      13.41 |        5.00 |    7.96 |            9.11 |            10.10 |             17.81 |
| 7-dummy-C5-3-wind4  | completed / outside configured limits |    35.87 |     11.53 |           1.92 |      16.73 |        5.00 |   17.45 |            9.10 |            10.10 |             17.60 |
| 7-actual-C5-3-wind0 | completed / outside configured limits |    43.09 |     11.53 |           2.59 |      10.99 |        5.00 |    0.48 |            9.11 |            10.11 |             17.90 |
| 7-actual-C5-3-wind2 | completed / outside configured limits |    40.89 |     11.53 |           2.20 |      13.41 |        5.00 |    7.96 |            9.11 |            10.10 |             17.81 |
| 7-actual-C5-3-wind4 | completed / outside configured limits |    35.87 |     11.53 |           1.92 |      16.73 |        5.00 |   17.45 |            9.10 |            10.10 |             17.60 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- 0-empty-C5-3-wind0: no engine warnings
- 0-empty-C5-3-wind2: no engine warnings
- 0-empty-C5-3-wind4: no engine warnings
- 0-dummy-C5-3-wind0: no engine warnings
- 0-dummy-C5-3-wind2: no engine warnings
- 0-dummy-C5-3-wind4: no engine warnings
- 0-actual-C5-3-wind0: no engine warnings
- 0-actual-C5-3-wind2: no engine warnings
- 0-actual-C5-3-wind4: no engine warnings
- 1-empty-C5-3-wind0: no engine warnings
- 1-empty-C5-3-wind2: no engine warnings
- 1-empty-C5-3-wind4: no engine warnings
- 1-dummy-C5-3-wind0: no engine warnings
- 1-dummy-C5-3-wind2: no engine warnings
- 1-dummy-C5-3-wind4: no engine warnings
- 1-actual-C5-3-wind0: no engine warnings
- 1-actual-C5-3-wind2: no engine warnings
- 1-actual-C5-3-wind4: no engine warnings
- 2-empty-C5-3-wind0: no engine warnings
- 2-empty-C5-3-wind2: no engine warnings
- 2-empty-C5-3-wind4: no engine warnings
- 2-dummy-C5-3-wind0: no engine warnings
- 2-dummy-C5-3-wind2: no engine warnings
- 2-dummy-C5-3-wind4: no engine warnings
- 2-actual-C5-3-wind0: no engine warnings
- 2-actual-C5-3-wind2: no engine warnings
- 2-actual-C5-3-wind4: no engine warnings
- 3-empty-C5-3-wind0: no engine warnings
- 3-empty-C5-3-wind2: no engine warnings
- 3-empty-C5-3-wind4: no engine warnings
- 3-dummy-C5-3-wind0: no engine warnings
- 3-dummy-C5-3-wind2: no engine warnings
- 3-dummy-C5-3-wind4: no engine warnings
- 3-actual-C5-3-wind0: no engine warnings
- 3-actual-C5-3-wind2: no engine warnings
- 3-actual-C5-3-wind4: no engine warnings
- 4-empty-C5-3-wind0: no engine warnings
- 4-empty-C5-3-wind2: no engine warnings
- 4-empty-C5-3-wind4: no engine warnings
- 4-dummy-C5-3-wind0: no engine warnings
- 4-dummy-C5-3-wind2: no engine warnings
- 4-dummy-C5-3-wind4: no engine warnings
- 4-actual-C5-3-wind0: no engine warnings
- 4-actual-C5-3-wind2: no engine warnings
- 4-actual-C5-3-wind4: no engine warnings
- 5-empty-C5-3-wind0: no engine warnings
- 5-empty-C5-3-wind2: no engine warnings
- 5-empty-C5-3-wind4: no engine warnings
- 5-dummy-C5-3-wind0: no engine warnings
- 5-dummy-C5-3-wind2: no engine warnings
- 5-dummy-C5-3-wind4: no engine warnings
- 5-actual-C5-3-wind0: no engine warnings
- 5-actual-C5-3-wind2: no engine warnings
- 5-actual-C5-3-wind4: no engine warnings
- 6-empty-C5-3-wind0: no engine warnings
- 6-empty-C5-3-wind2: no engine warnings
- 6-empty-C5-3-wind4: no engine warnings
- 6-dummy-C5-3-wind0: no engine warnings
- 6-dummy-C5-3-wind2: no engine warnings
- 6-dummy-C5-3-wind4: no engine warnings
- 6-actual-C5-3-wind0: no engine warnings
- 6-actual-C5-3-wind2: no engine warnings
- 6-actual-C5-3-wind4: no engine warnings
- 7-empty-C5-3-wind0: no engine warnings
- 7-empty-C5-3-wind2: no engine warnings
- 7-empty-C5-3-wind4: no engine warnings
- 7-dummy-C5-3-wind0: no engine warnings
- 7-dummy-C5-3-wind2: no engine warnings
- 7-dummy-C5-3-wind4: no engine warnings
- 7-actual-C5-3-wind0: no engine warnings
- 7-actual-C5-3-wind2: no engine warnings
- 7-actual-C5-3-wind4: no engine warnings

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

- 0-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 0-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 0-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-dummy-C5-3-wind2: deployment_speed_m_s=10.896154982803303 m/s (allowed None … 10.0)
- 0-dummy-C5-3-wind4: deployment_speed_m_s=14.226651453715391 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-actual-C5-3-wind2: deployment_speed_m_s=10.896154982803308 m/s (allowed None … 10.0)
- 0-actual-C5-3-wind4: deployment_speed_m_s=14.22665145371544 m/s (allowed None … 10.0)
- 1-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-C5-3-wind2: deployment_speed_m_s=10.89615498280337 m/s (allowed None … 10.0)
- 1-dummy-C5-3-wind4: deployment_speed_m_s=14.226651453715384 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-C5-3-wind2: deployment_speed_m_s=10.89615498280337 m/s (allowed None … 10.0)
- 1-actual-C5-3-wind4: deployment_speed_m_s=14.226651453715382 m/s (allowed None … 10.0)
- 2-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-dummy-C5-3-wind2: deployment_speed_m_s=10.89829819081364 m/s (allowed None … 10.0)
- 2-dummy-C5-3-wind4: deployment_speed_m_s=14.223547719269536 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-actual-C5-3-wind2: deployment_speed_m_s=10.898298190813636 m/s (allowed None … 10.0)
- 2-actual-C5-3-wind4: deployment_speed_m_s=14.223547719269735 m/s (allowed None … 10.0)
- 3-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-C5-3-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-C5-3-wind2: deployment_speed_m_s=10.898298190813627 m/s (allowed None … 10.0)
- 3-dummy-C5-3-wind4: deployment_speed_m_s=14.223547719269613 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-C5-3-wind2: deployment_speed_m_s=10.89829819081363 m/s (allowed None … 10.0)
- 3-actual-C5-3-wind4: deployment_speed_m_s=14.223547719269593 m/s (allowed None … 10.0)
- 4-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638697 m/s (allowed None … 10.0)
- 4-dummy-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.994265817266994 m/s (allowed None … 10.0); landing_descent_m_s=6.125096716542976 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.405995892746148 m/s (allowed None … 10.0); landing_descent_m_s=6.12502685762665 m/s (allowed
  None … 6.0)
- 4-dummy-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.73390741987006 m/s (allowed None … 10.0); landing_descent_m_s=6.12495719418571 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.994265817266994 m/s (allowed None … 10.0); landing_descent_m_s=6.125096716542976 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.405995892746148 m/s (allowed None … 10.0); landing_descent_m_s=6.12502685762665 m/s (allowed
  None … 6.0)
- 4-actual-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.733907419870143 m/s (allowed None … 10.0); landing_descent_m_s=6.12495719418571 m/s (allowed
  None … 6.0)
- 5-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638791 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.994265817266994 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.40599589274616 m/s (allowed None … 10.0)
- 5-dummy-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.73390741987016 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.994265817266994 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.40599589274616 m/s (allowed None … 10.0)
- 5-actual-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.73390741987016 m/s (allowed None … 10.0)
- 6-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638791 m/s (allowed None … 10.0)
- 6-dummy-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.989449045997493 m/s (allowed None … 10.0); landing_descent_m_s=6.1250967166179775 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.40505001841872 m/s (allowed None … 10.0); landing_descent_m_s=6.125026857511341 m/s (allowed
  None … 6.0)
- 6-dummy-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.72892239865407 m/s (allowed None … 10.0); landing_descent_m_s=6.124957204096661 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.989449045997493 m/s (allowed None … 10.0); landing_descent_m_s=6.1250967166179775 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.405050018418704 m/s (allowed None … 10.0); landing_descent_m_s=6.125026857511341 m/s (allowed
  None … 6.0)
- 6-actual-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.728922398654046 m/s (allowed None … 10.0); landing_descent_m_s=6.124957204096661 m/s (allowed
  None … 6.0)
- 7-empty-C5-3-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-empty-C5-3-wind4: deployment_speed_m_s=11.760289371638821 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.989449045997493 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.40505001841871 m/s (allowed None … 10.0)
- 7-dummy-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.7289223986541 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind0: guide_departure_m_s=11.53298435373083 m/s (allowed 12.0 … None);
  deployment_speed_m_s=10.989449045997493 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind2: guide_departure_m_s=11.5270609764402 m/s (allowed 12.0 … None);
  deployment_speed_m_s=13.405050018418704 m/s (allowed None … 10.0)
- 7-actual-C5-3-wind4: guide_departure_m_s=11.525124190784117 m/s (allowed 12.0 … None);
  deployment_speed_m_s=16.728922398653992 m/s (allowed None … 10.0)

## Deterministic stress envelope

These are bounded scenario corners, not probabilities or reliability estimates.

```json
{
  "schema_version": 1,
  "print_mass_factors": [1.0, 1.2],
  "payload_cg_offsets_mm": [-5.0, 5.0],
  "chute_cd": [0.6, 0.9],
  "wind_m_s": [0.0, 2.0, 4.0],
  "max_cases": 72,
  "source": "Engineering stress envelope, not measured distributions: print mass +0/+20%, payload CG +/-5 mm, chute Cd 0.6/0.9, uniform wind 0/2/4 m/s"
}
```

Each case records its applied factors in results.json and has a resolved corner input file.

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
    "pydantic": "2.13.5"
  }
}
```

Exact motor curves, events and time series are retained in results.json. Null means unavailable; failures remain in the
table.
