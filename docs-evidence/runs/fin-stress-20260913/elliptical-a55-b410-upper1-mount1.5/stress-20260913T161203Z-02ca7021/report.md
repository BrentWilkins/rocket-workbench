# Rocket Workbench report

Run: `stress-20260913T161203Z-02ca7021`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `8dc55e1745a9e81aa7d98a5bfcec768af074c19ea35df2ae5503c6abc2bd8f60`

## Cases

| Case                 | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| -------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-D12-5-wind0  | completed / incomplete inputs         |   208.14 |     13.39 |           1.22 |       0.18 |        5.72 |    0.09 |           14.98 |            15.98 |             66.85 |
| 0-empty-D12-5-wind2  | completed / outside configured limits |   206.56 |     13.39 |           0.58 |       2.27 |        5.72 |   50.00 |           14.97 |            15.97 |             66.71 |
| 0-empty-D12-5-wind4  | completed / outside configured limits |   202.39 |     13.38 |           0.58 |       4.39 |        5.72 |  101.57 |           14.96 |            15.96 |             66.35 |
| 0-dummy-D12-5-wind0  | completed / outside configured limits |   177.25 |     12.73 |           1.74 |       2.76 |        6.19 |    0.08 |           12.86 |            13.86 |             57.68 |
| 0-dummy-D12-5-wind2  | completed / outside configured limits |   175.31 |     12.73 |           1.40 |       4.10 |        6.19 |   30.55 |           12.85 |            13.85 |             57.53 |
| 0-dummy-D12-5-wind4  | completed / outside configured limits |   169.95 |     12.73 |           1.22 |       7.19 |        6.19 |   60.74 |           12.84 |            13.84 |             57.13 |
| 0-actual-D12-5-wind0 | completed / outside configured limits |   177.25 |     12.73 |           1.74 |       2.76 |        6.19 |    0.08 |           12.86 |            13.86 |             57.68 |
| 0-actual-D12-5-wind2 | completed / outside configured limits |   175.31 |     12.73 |           1.40 |       4.10 |        6.19 |   30.55 |           12.85 |            13.85 |             57.53 |
| 0-actual-D12-5-wind4 | completed / outside configured limits |   169.95 |     12.73 |           1.22 |       7.19 |        6.19 |   60.74 |           12.84 |            13.84 |             57.13 |
| 1-empty-D12-5-wind0  | completed / incomplete inputs         |   208.14 |     13.39 |           1.22 |       0.18 |        4.67 |    0.09 |           14.98 |            15.98 |             66.85 |
| 1-empty-D12-5-wind2  | completed / outside configured limits |   206.56 |     13.39 |           0.58 |       2.27 |        4.67 |   66.70 |           14.97 |            15.97 |             66.71 |
| 1-empty-D12-5-wind4  | completed / outside configured limits |   202.39 |     13.38 |           0.58 |       4.39 |        4.67 |  134.05 |           14.96 |            15.96 |             66.35 |
| 1-dummy-D12-5-wind0  | completed / incomplete inputs         |   177.25 |     12.73 |           1.74 |       2.76 |        5.05 |    0.08 |           12.86 |            13.86 |             57.68 |
| 1-dummy-D12-5-wind2  | completed / incomplete inputs         |   175.31 |     12.73 |           1.40 |       4.10 |        5.05 |   43.86 |           12.85 |            13.85 |             57.53 |
| 1-dummy-D12-5-wind4  | completed / incomplete inputs         |   169.95 |     12.73 |           1.22 |       7.19 |        5.05 |   86.27 |           12.84 |            13.84 |             57.13 |
| 1-actual-D12-5-wind0 | completed / incomplete inputs         |   177.25 |     12.73 |           1.74 |       2.76 |        5.05 |    0.08 |           12.86 |            13.86 |             57.68 |
| 1-actual-D12-5-wind2 | completed / incomplete inputs         |   175.31 |     12.73 |           1.40 |       4.10 |        5.05 |   43.86 |           12.85 |            13.85 |             57.53 |
| 1-actual-D12-5-wind4 | completed / incomplete inputs         |   169.95 |     12.73 |           1.22 |       7.19 |        5.05 |   86.27 |           12.84 |            13.84 |             57.13 |
| 2-empty-D12-5-wind0  | completed / incomplete inputs         |   208.14 |     13.39 |           1.22 |       0.18 |        5.72 |    0.09 |           14.98 |            15.98 |             66.85 |
| 2-empty-D12-5-wind2  | completed / outside configured limits |   206.56 |     13.39 |           0.58 |       2.27 |        5.72 |   50.00 |           14.97 |            15.97 |             66.71 |
| 2-empty-D12-5-wind4  | completed / outside configured limits |   202.39 |     13.38 |           0.58 |       4.39 |        5.72 |  101.57 |           14.96 |            15.96 |             66.35 |
| 2-dummy-D12-5-wind0  | completed / outside configured limits |   177.25 |     12.73 |           1.71 |       2.76 |        6.19 |    0.08 |           12.86 |            13.86 |             57.68 |
| 2-dummy-D12-5-wind2  | completed / outside configured limits |   175.31 |     12.73 |           1.37 |       4.10 |        6.19 |   30.54 |           12.85 |            13.85 |             57.53 |
| 2-dummy-D12-5-wind4  | completed / outside configured limits |   169.96 |     12.73 |           1.19 |       7.18 |        6.19 |   60.79 |           12.84 |            13.84 |             57.13 |
| 2-actual-D12-5-wind0 | completed / outside configured limits |   177.25 |     12.73 |           1.71 |       2.76 |        6.19 |    0.08 |           12.86 |            13.86 |             57.68 |
| 2-actual-D12-5-wind2 | completed / outside configured limits |   175.31 |     12.73 |           1.37 |       4.10 |        6.19 |   30.54 |           12.85 |            13.85 |             57.53 |
| 2-actual-D12-5-wind4 | completed / outside configured limits |   169.96 |     12.73 |           1.19 |       7.18 |        6.19 |   60.79 |           12.84 |            13.84 |             57.13 |
| 3-empty-D12-5-wind0  | completed / incomplete inputs         |   208.14 |     13.39 |           1.22 |       0.18 |        4.67 |    0.09 |           14.98 |            15.98 |             66.85 |
| 3-empty-D12-5-wind2  | completed / outside configured limits |   206.56 |     13.39 |           0.58 |       2.27 |        4.67 |   66.70 |           14.97 |            15.97 |             66.71 |
| 3-empty-D12-5-wind4  | completed / outside configured limits |   202.39 |     13.38 |           0.58 |       4.39 |        4.67 |  134.05 |           14.96 |            15.96 |             66.35 |
| 3-dummy-D12-5-wind0  | completed / incomplete inputs         |   177.25 |     12.73 |           1.71 |       2.76 |        5.05 |    0.08 |           12.86 |            13.86 |             57.68 |
| 3-dummy-D12-5-wind2  | completed / incomplete inputs         |   175.31 |     12.73 |           1.37 |       4.10 |        5.05 |   43.86 |           12.85 |            13.85 |             57.53 |
| 3-dummy-D12-5-wind4  | completed / incomplete inputs         |   169.96 |     12.73 |           1.19 |       7.18 |        5.05 |   86.32 |           12.84 |            13.84 |             57.13 |
| 3-actual-D12-5-wind0 | completed / incomplete inputs         |   177.25 |     12.73 |           1.71 |       2.76 |        5.05 |    0.08 |           12.86 |            13.86 |             57.68 |
| 3-actual-D12-5-wind2 | completed / incomplete inputs         |   175.31 |     12.73 |           1.37 |       4.10 |        5.05 |   43.86 |           12.85 |            13.85 |             57.53 |
| 3-actual-D12-5-wind4 | completed / incomplete inputs         |   169.96 |     12.73 |           1.19 |       7.18 |        5.05 |   86.32 |           12.84 |            13.84 |             57.13 |
| 4-empty-D12-5-wind0  | completed / outside configured limits |   190.82 |     12.92 |           0.75 |       1.35 |        5.98 |    0.09 |           13.73 |            14.73 |             61.55 |
| 4-empty-D12-5-wind2  | completed / outside configured limits |   189.12 |     12.91 |           0.69 |       2.90 |        5.98 |   39.62 |           13.73 |            14.72 |             61.41 |
| 4-empty-D12-5-wind4  | completed / outside configured limits |   184.58 |     12.91 |           0.68 |       5.48 |        5.98 |   80.30 |           13.72 |            14.71 |             61.04 |
| 4-dummy-D12-5-wind0  | completed / outside configured limits |   161.20 |     12.39 |           1.57 |       4.65 |        6.43 |    0.05 |           11.91 |            12.91 |             53.32 |
| 4-dummy-D12-5-wind2  | completed / outside configured limits |   159.20 |     12.38 |           1.47 |       5.61 |        6.43 |   22.43 |           11.90 |            12.90 |             53.17 |
| 4-dummy-D12-5-wind4  | completed / outside configured limits |   153.68 |     12.38 |           1.27 |       8.77 |        6.43 |   44.22 |           11.90 |            12.90 |             52.76 |
| 4-actual-D12-5-wind0 | completed / outside configured limits |   161.20 |     12.39 |           1.57 |       4.65 |        6.43 |    0.05 |           11.91 |            12.91 |             53.32 |
| 4-actual-D12-5-wind2 | completed / outside configured limits |   159.20 |     12.38 |           1.47 |       5.61 |        6.43 |   22.43 |           11.90 |            12.90 |             53.17 |
| 4-actual-D12-5-wind4 | completed / outside configured limits |   153.68 |     12.38 |           1.27 |       8.77 |        6.43 |   44.22 |           11.90 |            12.90 |             52.76 |
| 5-empty-D12-5-wind0  | completed / outside configured limits |   190.82 |     12.92 |           0.75 |       1.35 |        4.89 |    0.09 |           13.73 |            14.73 |             61.55 |
| 5-empty-D12-5-wind2  | completed / outside configured limits |   189.12 |     12.91 |           0.69 |       2.90 |        4.89 |   54.35 |           13.73 |            14.72 |             61.41 |
| 5-empty-D12-5-wind4  | completed / outside configured limits |   184.58 |     12.91 |           0.68 |       5.48 |        4.89 |  108.82 |           13.72 |            14.71 |             61.04 |
| 5-dummy-D12-5-wind0  | completed / incomplete inputs         |   161.20 |     12.39 |           1.57 |       4.65 |        5.25 |    0.06 |           11.91 |            12.91 |             53.32 |
| 5-dummy-D12-5-wind2  | completed / incomplete inputs         |   159.20 |     12.38 |           1.47 |       5.61 |        5.25 |   34.11 |           11.90 |            12.90 |             53.17 |
| 5-dummy-D12-5-wind4  | completed / incomplete inputs         |   153.68 |     12.38 |           1.27 |       8.77 |        5.25 |   66.48 |           11.90 |            12.90 |             52.76 |
| 5-actual-D12-5-wind0 | completed / incomplete inputs         |   161.20 |     12.39 |           1.57 |       4.65 |        5.25 |    0.06 |           11.91 |            12.91 |             53.32 |
| 5-actual-D12-5-wind2 | completed / incomplete inputs         |   159.20 |     12.38 |           1.47 |       5.61 |        5.25 |   34.11 |           11.90 |            12.90 |             53.17 |
| 5-actual-D12-5-wind4 | completed / incomplete inputs         |   153.68 |     12.38 |           1.27 |       8.77 |        5.25 |   66.48 |           11.90 |            12.90 |             52.76 |
| 6-empty-D12-5-wind0  | completed / outside configured limits |   190.82 |     12.92 |           0.75 |       1.35 |        5.98 |    0.09 |           13.73 |            14.73 |             61.55 |
| 6-empty-D12-5-wind2  | completed / outside configured limits |   189.12 |     12.91 |           0.69 |       2.90 |        5.98 |   39.62 |           13.73 |            14.72 |             61.41 |
| 6-empty-D12-5-wind4  | completed / outside configured limits |   184.58 |     12.91 |           0.68 |       5.48 |        5.98 |   80.30 |           13.72 |            14.71 |             61.04 |
| 6-dummy-D12-5-wind0  | completed / outside configured limits |   161.20 |     12.39 |           1.53 |       4.65 |        6.43 |    0.05 |           11.91 |            12.91 |             53.32 |
| 6-dummy-D12-5-wind2  | completed / outside configured limits |   159.20 |     12.38 |           1.44 |       5.61 |        6.43 |   22.43 |           11.90 |            12.90 |             53.17 |
| 6-dummy-D12-5-wind4  | completed / outside configured limits |   153.69 |     12.38 |           1.24 |       8.76 |        6.43 |   44.27 |           11.90 |            12.90 |             52.76 |
| 6-actual-D12-5-wind0 | completed / outside configured limits |   161.20 |     12.39 |           1.53 |       4.65 |        6.43 |    0.05 |           11.91 |            12.91 |             53.32 |
| 6-actual-D12-5-wind2 | completed / outside configured limits |   159.20 |     12.38 |           1.44 |       5.61 |        6.43 |   22.43 |           11.90 |            12.90 |             53.17 |
| 6-actual-D12-5-wind4 | completed / outside configured limits |   153.69 |     12.38 |           1.24 |       8.76 |        6.43 |   44.27 |           11.90 |            12.90 |             52.76 |
| 7-empty-D12-5-wind0  | completed / outside configured limits |   190.82 |     12.92 |           0.75 |       1.35 |        4.89 |    0.09 |           13.73 |            14.73 |             61.55 |
| 7-empty-D12-5-wind2  | completed / outside configured limits |   189.12 |     12.91 |           0.69 |       2.90 |        4.89 |   54.35 |           13.73 |            14.72 |             61.41 |
| 7-empty-D12-5-wind4  | completed / outside configured limits |   184.58 |     12.91 |           0.68 |       5.48 |        4.89 |  108.82 |           13.72 |            14.71 |             61.04 |
| 7-dummy-D12-5-wind0  | completed / incomplete inputs         |   161.20 |     12.39 |           1.53 |       4.65 |        5.25 |    0.06 |           11.91 |            12.91 |             53.32 |
| 7-dummy-D12-5-wind2  | completed / incomplete inputs         |   159.20 |     12.38 |           1.44 |       5.61 |        5.25 |   34.10 |           11.90 |            12.90 |             53.17 |
| 7-dummy-D12-5-wind4  | completed / incomplete inputs         |   153.69 |     12.38 |           1.24 |       8.76 |        5.25 |   66.53 |           11.90 |            12.90 |             52.76 |
| 7-actual-D12-5-wind0 | completed / incomplete inputs         |   161.20 |     12.39 |           1.53 |       4.65 |        5.25 |    0.06 |           11.91 |            12.91 |             53.32 |
| 7-actual-D12-5-wind2 | completed / incomplete inputs         |   159.20 |     12.38 |           1.44 |       5.61 |        5.25 |   34.10 |           11.90 |            12.90 |             53.17 |
| 7-actual-D12-5-wind4 | completed / incomplete inputs         |   153.69 |     12.38 |           1.24 |       8.76 |        5.25 |   66.53 |           11.90 |            12.90 |             52.76 |

No case is ranked or cleared for flight. Dummy and provisional actual loads use the same mass and CG.

## Warnings and failures

- 0-empty-D12-5-wind0: no engine warnings
- 0-empty-D12-5-wind2: no engine warnings
- 0-empty-D12-5-wind4: no engine warnings
- 0-dummy-D12-5-wind0: no engine warnings
- 0-dummy-D12-5-wind2: no engine warnings
- 0-dummy-D12-5-wind4: no engine warnings
- 0-actual-D12-5-wind0: no engine warnings
- 0-actual-D12-5-wind2: no engine warnings
- 0-actual-D12-5-wind4: no engine warnings
- 1-empty-D12-5-wind0: no engine warnings
- 1-empty-D12-5-wind2: no engine warnings
- 1-empty-D12-5-wind4: no engine warnings
- 1-dummy-D12-5-wind0: no engine warnings
- 1-dummy-D12-5-wind2: no engine warnings
- 1-dummy-D12-5-wind4: no engine warnings
- 1-actual-D12-5-wind0: no engine warnings
- 1-actual-D12-5-wind2: no engine warnings
- 1-actual-D12-5-wind4: no engine warnings
- 2-empty-D12-5-wind0: no engine warnings
- 2-empty-D12-5-wind2: no engine warnings
- 2-empty-D12-5-wind4: no engine warnings
- 2-dummy-D12-5-wind0: no engine warnings
- 2-dummy-D12-5-wind2: no engine warnings
- 2-dummy-D12-5-wind4: no engine warnings
- 2-actual-D12-5-wind0: no engine warnings
- 2-actual-D12-5-wind2: no engine warnings
- 2-actual-D12-5-wind4: no engine warnings
- 3-empty-D12-5-wind0: no engine warnings
- 3-empty-D12-5-wind2: no engine warnings
- 3-empty-D12-5-wind4: no engine warnings
- 3-dummy-D12-5-wind0: no engine warnings
- 3-dummy-D12-5-wind2: no engine warnings
- 3-dummy-D12-5-wind4: no engine warnings
- 3-actual-D12-5-wind0: no engine warnings
- 3-actual-D12-5-wind2: no engine warnings
- 3-actual-D12-5-wind4: no engine warnings
- 4-empty-D12-5-wind0: no engine warnings
- 4-empty-D12-5-wind2: no engine warnings
- 4-empty-D12-5-wind4: no engine warnings
- 4-dummy-D12-5-wind0: no engine warnings
- 4-dummy-D12-5-wind2: no engine warnings
- 4-dummy-D12-5-wind4: no engine warnings
- 4-actual-D12-5-wind0: no engine warnings
- 4-actual-D12-5-wind2: no engine warnings
- 4-actual-D12-5-wind4: no engine warnings
- 5-empty-D12-5-wind0: no engine warnings
- 5-empty-D12-5-wind2: no engine warnings
- 5-empty-D12-5-wind4: no engine warnings
- 5-dummy-D12-5-wind0: no engine warnings
- 5-dummy-D12-5-wind2: no engine warnings
- 5-dummy-D12-5-wind4: no engine warnings
- 5-actual-D12-5-wind0: no engine warnings
- 5-actual-D12-5-wind2: no engine warnings
- 5-actual-D12-5-wind4: no engine warnings
- 6-empty-D12-5-wind0: no engine warnings
- 6-empty-D12-5-wind2: no engine warnings
- 6-empty-D12-5-wind4: no engine warnings
- 6-dummy-D12-5-wind0: no engine warnings
- 6-dummy-D12-5-wind2: no engine warnings
- 6-dummy-D12-5-wind4: no engine warnings
- 6-actual-D12-5-wind0: no engine warnings
- 6-actual-D12-5-wind2: no engine warnings
- 6-actual-D12-5-wind4: no engine warnings
- 7-empty-D12-5-wind0: no engine warnings
- 7-empty-D12-5-wind2: no engine warnings
- 7-empty-D12-5-wind4: no engine warnings
- 7-dummy-D12-5-wind0: no engine warnings
- 7-dummy-D12-5-wind2: no engine warnings
- 7-dummy-D12-5-wind4: no engine warnings
- 7-actual-D12-5-wind0: no engine warnings
- 7-actual-D12-5-wind2: no engine warnings
- 7-actual-D12-5-wind4: no engine warnings

## Missing measurements / physical checks

- Measured mass and balance: BT-60 cardboard airframe
- Measured mass and balance: Provisional commercial 24 mm mount assembly plus CD spacer
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

- 0-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 0-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5813133990545781 cal (allowed 1.0 … None)
- 0-empty-D12-5-wind4: minimum_ascent_stability_cal=0.575842548199853 cal (allowed 1.0 … None)
- 0-dummy-D12-5-wind0: landing_descent_m_s=6.187978438232689 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind2: landing_descent_m_s=6.187908002834348 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind4: landing_descent_m_s=6.187837326512483 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind0: landing_descent_m_s=6.187978438232689 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind2: landing_descent_m_s=6.187908002834347 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind4: landing_descent_m_s=6.187837326512483 m/s (allowed None … 6.0)
- 1-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5813133990542245 cal (allowed 1.0 … None)
- 1-empty-D12-5-wind4: minimum_ascent_stability_cal=0.575842548199853 cal (allowed 1.0 … None)
- 1-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5813133990546422 cal (allowed 1.0 … None)
- 2-empty-D12-5-wind4: minimum_ascent_stability_cal=0.575842548199853 cal (allowed 1.0 … None)
- 2-dummy-D12-5-wind0: landing_descent_m_s=6.187978438232609 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind2: landing_descent_m_s=6.1879080028034945 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind4: landing_descent_m_s=6.187837325501933 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind0: landing_descent_m_s=6.187978438232609 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind2: landing_descent_m_s=6.1879080028034945 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind4: landing_descent_m_s=6.187837325501933 m/s (allowed None … 6.0)
- 3-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-D12-5-wind2: minimum_ascent_stability_cal=0.5813133990545821 cal (allowed 1.0 … None)
- 3-empty-D12-5-wind4: minimum_ascent_stability_cal=0.575842548199853 cal (allowed 1.0 … None)
- 3-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind0: minimum_ascent_stability_cal=0.7479665612480764 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind2: minimum_ascent_stability_cal=0.6949459375996875 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6825913939346112 cal (allowed 1.0 … None)
- 4-dummy-D12-5-wind0: landing_descent_m_s=6.431461967187312 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind2: landing_descent_m_s=6.431388626049136 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind4: landing_descent_m_s=6.431315241136075 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind0: landing_descent_m_s=6.431461967187312 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind2: landing_descent_m_s=6.431388626049136 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind4: landing_descent_m_s=6.431315241136075 m/s (allowed None … 6.0)
- 5-empty-D12-5-wind0: minimum_ascent_stability_cal=0.747966561248079 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind2: minimum_ascent_stability_cal=0.6949459375997916 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6825913939346112 cal (allowed 1.0 … None)
- 5-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind0: minimum_ascent_stability_cal=0.7479665612480777 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind2: minimum_ascent_stability_cal=0.6949459375996861 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6825913939346112 cal (allowed 1.0 … None)
- 6-dummy-D12-5-wind0: landing_descent_m_s=6.431461967187587 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind2: landing_descent_m_s=6.431388626031216 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind4: landing_descent_m_s=6.431315240863 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind0: landing_descent_m_s=6.431461967187587 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind2: landing_descent_m_s=6.431388626031217 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind4: landing_descent_m_s=6.431315240863 m/s (allowed None … 6.0)
- 7-empty-D12-5-wind0: minimum_ascent_stability_cal=0.747966561248079 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind2: minimum_ascent_stability_cal=0.6949459375998623 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind4: minimum_ascent_stability_cal=0.6825913939346112 cal (allowed 1.0 … None)
- 7-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 7-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 7-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 7-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs

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

- apogee_m: 30.0 … None m; engineering assumption; New motor comparison: report altitude without inherited 120 m
  ceiling; retain 30 m minimum. Site altitude clearance is unassessed.
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
