# Rocket Workbench report

Run: `stress-20260913T161255Z-e73950df`

Provisional software demonstration. Physical assembly and flight validation are pending.

Configuration SHA256: `ab7fb99cc1b73f717a90093f52f10ef70263e25ef93fa2e8539bbbf01ab67c26`

## Cases

| Case                 | Execution / evaluation                | Apogee m | Guide m/s | Min ascent cal | Deploy m/s | Descent m/s | Drift m | Powered accel g | Estimated load g | Powered speed m/s |
| -------------------- | ------------------------------------- | -------: | --------: | -------------: | ---------: | ----------: | ------: | --------------: | ---------------: | ----------------: |
| 0-empty-D12-5-wind0  | completed / incomplete inputs         |   215.19 |     13.35 |           1.44 |       1.15 |        5.68 |    0.10 |           15.22 |            16.22 |             68.24 |
| 0-empty-D12-5-wind2  | completed / outside configured limits |   213.50 |     13.35 |           0.89 |       2.66 |        5.68 |   51.88 |           15.21 |            16.21 |             68.11 |
| 0-empty-D12-5-wind4  | completed / outside configured limits |   209.02 |     13.35 |           0.73 |       4.73 |        5.68 |  104.97 |           15.20 |            16.20 |             67.75 |
| 0-dummy-D12-5-wind0  | completed / outside configured limits |   192.11 |     13.04 |           1.69 |       0.90 |        6.01 |    0.09 |           13.61 |            14.61 |             61.34 |
| 0-dummy-D12-5-wind2  | completed / outside configured limits |   190.17 |     13.04 |           1.37 |       3.17 |        6.01 |   37.22 |           13.61 |            14.61 |             61.19 |
| 0-dummy-D12-5-wind4  | completed / outside configured limits |   184.83 |     13.03 |           1.21 |       6.23 |        6.01 |   74.51 |           13.60 |            14.60 |             60.79 |
| 0-actual-D12-5-wind0 | completed / outside configured limits |   192.11 |     13.04 |           1.69 |       0.90 |        6.01 |    0.09 |           13.61 |            14.61 |             61.34 |
| 0-actual-D12-5-wind2 | completed / outside configured limits |   190.17 |     13.04 |           1.37 |       3.17 |        6.01 |   37.22 |           13.61 |            14.61 |             61.19 |
| 0-actual-D12-5-wind4 | completed / outside configured limits |   184.83 |     13.03 |           1.21 |       6.23 |        6.01 |   74.51 |           13.60 |            14.60 |             60.79 |
| 1-empty-D12-5-wind0  | completed / incomplete inputs         |   215.19 |     13.35 |           1.44 |       1.15 |        4.63 |    0.10 |           15.22 |            16.22 |             68.24 |
| 1-empty-D12-5-wind2  | completed / outside configured limits |   213.50 |     13.35 |           0.89 |       2.66 |        4.63 |   69.28 |           15.21 |            16.21 |             68.11 |
| 1-empty-D12-5-wind4  | completed / outside configured limits |   209.02 |     13.35 |           0.73 |       4.73 |        4.63 |  138.78 |           15.20 |            16.20 |             67.75 |
| 1-dummy-D12-5-wind0  | completed / incomplete inputs         |   192.11 |     13.04 |           1.69 |       0.90 |        4.91 |    0.09 |           13.61 |            14.61 |             61.34 |
| 1-dummy-D12-5-wind2  | completed / incomplete inputs         |   190.17 |     13.04 |           1.37 |       3.17 |        4.91 |   52.05 |           13.61 |            14.61 |             61.19 |
| 1-dummy-D12-5-wind4  | completed / incomplete inputs         |   184.83 |     13.03 |           1.21 |       6.23 |        4.91 |  103.02 |           13.60 |            14.60 |             60.79 |
| 1-actual-D12-5-wind0 | completed / incomplete inputs         |   192.11 |     13.04 |           1.69 |       0.90 |        4.91 |    0.09 |           13.61 |            14.61 |             61.34 |
| 1-actual-D12-5-wind2 | completed / incomplete inputs         |   190.17 |     13.04 |           1.37 |       3.17 |        4.91 |   52.05 |           13.61 |            14.61 |             61.19 |
| 1-actual-D12-5-wind4 | completed / incomplete inputs         |   184.83 |     13.03 |           1.21 |       6.23 |        4.91 |  103.02 |           13.60 |            14.60 |             60.79 |
| 2-empty-D12-5-wind0  | completed / incomplete inputs         |   215.19 |     13.35 |           1.44 |       1.15 |        5.68 |    0.10 |           15.22 |            16.22 |             68.24 |
| 2-empty-D12-5-wind2  | completed / outside configured limits |   213.50 |     13.35 |           0.89 |       2.66 |        5.68 |   51.88 |           15.21 |            16.21 |             68.11 |
| 2-empty-D12-5-wind4  | completed / outside configured limits |   209.02 |     13.35 |           0.73 |       4.73 |        5.68 |  104.97 |           15.20 |            16.20 |             67.75 |
| 2-dummy-D12-5-wind0  | completed / outside configured limits |   192.11 |     13.04 |           1.66 |       0.90 |        6.01 |    0.09 |           13.61 |            14.61 |             61.34 |
| 2-dummy-D12-5-wind2  | completed / outside configured limits |   190.17 |     13.04 |           1.34 |       3.17 |        6.01 |   37.22 |           13.61 |            14.61 |             61.19 |
| 2-dummy-D12-5-wind4  | completed / outside configured limits |   184.84 |     13.03 |           1.19 |       6.23 |        6.01 |   74.54 |           13.60 |            14.60 |             60.80 |
| 2-actual-D12-5-wind0 | completed / outside configured limits |   192.11 |     13.04 |           1.66 |       0.90 |        6.01 |    0.09 |           13.61 |            14.61 |             61.34 |
| 2-actual-D12-5-wind2 | completed / outside configured limits |   190.17 |     13.04 |           1.34 |       3.17 |        6.01 |   37.22 |           13.61 |            14.61 |             61.19 |
| 2-actual-D12-5-wind4 | completed / outside configured limits |   184.84 |     13.03 |           1.19 |       6.23 |        6.01 |   74.54 |           13.60 |            14.60 |             60.80 |
| 3-empty-D12-5-wind0  | completed / incomplete inputs         |   215.19 |     13.35 |           1.44 |       1.15 |        4.63 |    0.10 |           15.22 |            16.22 |             68.24 |
| 3-empty-D12-5-wind2  | completed / outside configured limits |   213.50 |     13.35 |           0.89 |       2.66 |        4.63 |   69.28 |           15.21 |            16.21 |             68.11 |
| 3-empty-D12-5-wind4  | completed / outside configured limits |   209.02 |     13.35 |           0.73 |       4.73 |        4.63 |  138.78 |           15.20 |            16.20 |             67.75 |
| 3-dummy-D12-5-wind0  | completed / incomplete inputs         |   192.11 |     13.04 |           1.66 |       0.90 |        4.91 |    0.09 |           13.61 |            14.61 |             61.34 |
| 3-dummy-D12-5-wind2  | completed / incomplete inputs         |   190.17 |     13.04 |           1.34 |       3.17 |        4.91 |   52.04 |           13.61 |            14.61 |             61.19 |
| 3-dummy-D12-5-wind4  | completed / incomplete inputs         |   184.84 |     13.03 |           1.19 |       6.23 |        4.91 |  103.06 |           13.60 |            14.60 |             60.80 |
| 3-actual-D12-5-wind0 | completed / incomplete inputs         |   192.11 |     13.04 |           1.66 |       0.90 |        4.91 |    0.09 |           13.61 |            14.61 |             61.34 |
| 3-actual-D12-5-wind2 | completed / incomplete inputs         |   190.17 |     13.04 |           1.34 |       3.17 |        4.91 |   52.04 |           13.61 |            14.61 |             61.19 |
| 3-actual-D12-5-wind4 | completed / incomplete inputs         |   184.84 |     13.03 |           1.19 |       6.23 |        4.91 |  103.06 |           13.60 |            14.60 |             60.80 |
| 4-empty-D12-5-wind0  | completed / outside configured limits |   197.67 |     13.16 |           0.97 |       0.36 |        5.93 |    0.09 |           13.98 |            14.98 |             62.94 |
| 4-empty-D12-5-wind2  | completed / outside configured limits |   195.86 |     13.16 |           0.89 |       2.79 |        5.93 |   41.37 |           13.97 |            14.97 |             62.79 |
| 4-empty-D12-5-wind4  | completed / outside configured limits |   191.01 |     13.16 |           0.85 |       5.52 |        5.93 |   83.61 |           13.96 |            14.96 |             62.41 |
| 4-dummy-D12-5-wind0  | completed / outside configured limits |   175.39 |     12.68 |           1.35 |       2.72 |        6.25 |    0.08 |           12.60 |            13.60 |             56.73 |
| 4-dummy-D12-5-wind2  | completed / outside configured limits |   173.38 |     12.68 |           1.46 |       4.24 |        6.25 |   28.49 |           12.59 |            13.59 |             56.58 |
| 4-dummy-D12-5-wind4  | completed / outside configured limits |   167.85 |     12.68 |           1.28 |       7.49 |        6.25 |   56.73 |           12.58 |            13.58 |             56.18 |
| 4-actual-D12-5-wind0 | completed / outside configured limits |   175.39 |     12.68 |           1.35 |       2.72 |        6.25 |    0.08 |           12.60 |            13.60 |             56.73 |
| 4-actual-D12-5-wind2 | completed / outside configured limits |   173.38 |     12.68 |           1.46 |       4.24 |        6.25 |   28.49 |           12.59 |            13.59 |             56.58 |
| 4-actual-D12-5-wind4 | completed / outside configured limits |   167.85 |     12.68 |           1.28 |       7.49 |        6.25 |   56.73 |           12.58 |            13.58 |             56.18 |
| 5-empty-D12-5-wind0  | completed / outside configured limits |   197.67 |     13.16 |           0.97 |       0.36 |        4.84 |    0.09 |           13.98 |            14.98 |             62.94 |
| 5-empty-D12-5-wind2  | completed / outside configured limits |   195.86 |     13.16 |           0.89 |       2.79 |        4.84 |   56.79 |           13.97 |            14.97 |             62.79 |
| 5-empty-D12-5-wind4  | completed / outside configured limits |   191.01 |     13.16 |           0.85 |       5.52 |        4.84 |  113.38 |           13.96 |            14.96 |             62.41 |
| 5-dummy-D12-5-wind0  | completed / incomplete inputs         |   175.39 |     12.68 |           1.35 |       2.72 |        5.11 |    0.08 |           12.60 |            13.60 |             56.73 |
| 5-dummy-D12-5-wind2  | completed / incomplete inputs         |   173.38 |     12.68 |           1.46 |       4.24 |        5.11 |   41.57 |           12.59 |            13.59 |             56.58 |
| 5-dummy-D12-5-wind4  | completed / incomplete inputs         |   167.85 |     12.68 |           1.28 |       7.49 |        5.11 |   81.75 |           12.58 |            13.58 |             56.18 |
| 5-actual-D12-5-wind0 | completed / incomplete inputs         |   175.39 |     12.68 |           1.35 |       2.72 |        5.11 |    0.08 |           12.60 |            13.60 |             56.73 |
| 5-actual-D12-5-wind2 | completed / incomplete inputs         |   173.38 |     12.68 |           1.46 |       4.24 |        5.11 |   41.57 |           12.59 |            13.59 |             56.58 |
| 5-actual-D12-5-wind4 | completed / incomplete inputs         |   167.85 |     12.68 |           1.28 |       7.49 |        5.11 |   81.75 |           12.58 |            13.58 |             56.18 |
| 6-empty-D12-5-wind0  | completed / outside configured limits |   197.67 |     13.16 |           0.97 |       0.36 |        5.93 |    0.09 |           13.98 |            14.98 |             62.94 |
| 6-empty-D12-5-wind2  | completed / outside configured limits |   195.86 |     13.16 |           0.89 |       2.79 |        5.93 |   41.37 |           13.97 |            14.97 |             62.79 |
| 6-empty-D12-5-wind4  | completed / outside configured limits |   191.01 |     13.16 |           0.85 |       5.52 |        5.93 |   83.61 |           13.96 |            14.96 |             62.41 |
| 6-dummy-D12-5-wind0  | completed / outside configured limits |   175.39 |     12.68 |           1.33 |       2.72 |        6.25 |    0.08 |           12.60 |            13.60 |             56.73 |
| 6-dummy-D12-5-wind2  | completed / outside configured limits |   173.38 |     12.68 |           1.44 |       4.24 |        6.25 |   28.48 |           12.59 |            13.59 |             56.58 |
| 6-dummy-D12-5-wind4  | completed / outside configured limits |   167.85 |     12.68 |           1.26 |       7.49 |        6.25 |   56.76 |           12.58 |            13.58 |             56.18 |
| 6-actual-D12-5-wind0 | completed / outside configured limits |   175.39 |     12.68 |           1.33 |       2.72 |        6.25 |    0.08 |           12.60 |            13.60 |             56.73 |
| 6-actual-D12-5-wind2 | completed / outside configured limits |   173.38 |     12.68 |           1.44 |       4.24 |        6.25 |   28.48 |           12.59 |            13.59 |             56.58 |
| 6-actual-D12-5-wind4 | completed / outside configured limits |   167.85 |     12.68 |           1.26 |       7.49 |        6.25 |   56.76 |           12.58 |            13.58 |             56.18 |
| 7-empty-D12-5-wind0  | completed / outside configured limits |   197.67 |     13.16 |           0.97 |       0.36 |        4.84 |    0.09 |           13.98 |            14.98 |             62.94 |
| 7-empty-D12-5-wind2  | completed / outside configured limits |   195.86 |     13.16 |           0.89 |       2.79 |        4.84 |   56.79 |           13.97 |            14.97 |             62.79 |
| 7-empty-D12-5-wind4  | completed / outside configured limits |   191.01 |     13.16 |           0.85 |       5.52 |        4.84 |  113.38 |           13.96 |            14.96 |             62.41 |
| 7-dummy-D12-5-wind0  | completed / incomplete inputs         |   175.39 |     12.68 |           1.33 |       2.72 |        5.11 |    0.08 |           12.60 |            13.60 |             56.73 |
| 7-dummy-D12-5-wind2  | completed / incomplete inputs         |   173.38 |     12.68 |           1.44 |       4.24 |        5.11 |   41.56 |           12.59 |            13.59 |             56.58 |
| 7-dummy-D12-5-wind4  | completed / incomplete inputs         |   167.85 |     12.68 |           1.26 |       7.49 |        5.11 |   81.77 |           12.58 |            13.58 |             56.18 |
| 7-actual-D12-5-wind0 | completed / incomplete inputs         |   175.39 |     12.68 |           1.33 |       2.72 |        5.11 |    0.08 |           12.60 |            13.60 |             56.73 |
| 7-actual-D12-5-wind2 | completed / incomplete inputs         |   173.38 |     12.68 |           1.44 |       4.24 |        5.11 |   41.56 |           12.59 |            13.59 |             56.58 |
| 7-actual-D12-5-wind4 | completed / incomplete inputs         |   167.85 |     12.68 |           1.26 |       7.49 |        5.11 |   81.77 |           12.58 |            13.58 |             56.18 |

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
- 0-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8869077205779548 cal (allowed 1.0 … None)
- 0-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7314138232418647 cal (allowed 1.0 … None)
- 0-dummy-D12-5-wind0: landing_descent_m_s=6.0116538899784056 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind2: landing_descent_m_s=6.011585374155852 m/s (allowed None … 6.0)
- 0-dummy-D12-5-wind4: landing_descent_m_s=6.011516811630715 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind0: landing_descent_m_s=6.0116538899784056 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind2: landing_descent_m_s=6.011585374155852 m/s (allowed None … 6.0)
- 0-actual-D12-5-wind4: landing_descent_m_s=6.011516811630715 m/s (allowed None … 6.0)
- 1-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8869077205780602 cal (allowed 1.0 … None)
- 1-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7314138232418647 cal (allowed 1.0 … None)
- 1-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 1-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 2-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8869077205783444 cal (allowed 1.0 … None)
- 2-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7314138232418647 cal (allowed 1.0 … None)
- 2-dummy-D12-5-wind0: landing_descent_m_s=6.011653889978533 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind2: landing_descent_m_s=6.011585374127307 m/s (allowed None … 6.0)
- 2-dummy-D12-5-wind4: landing_descent_m_s=6.011516811154484 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind0: landing_descent_m_s=6.011653889978533 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind2: landing_descent_m_s=6.011585374127307 m/s (allowed None … 6.0)
- 2-actual-D12-5-wind4: landing_descent_m_s=6.011516811154483 m/s (allowed None … 6.0)
- 3-empty-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8869077205779548 cal (allowed 1.0 … None)
- 3-empty-D12-5-wind4: minimum_ascent_stability_cal=0.7314138232418647 cal (allowed 1.0 … None)
- 3-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 3-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 4-empty-D12-5-wind0: minimum_ascent_stability_cal=0.9744037619826157 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8901885110949085 cal (allowed 1.0 … None)
- 4-empty-D12-5-wind4: minimum_ascent_stability_cal=0.85304437002727 cal (allowed 1.0 … None)
- 4-dummy-D12-5-wind0: landing_descent_m_s=6.253585548285305 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind2: landing_descent_m_s=6.253514200757778 m/s (allowed None … 6.0)
- 4-dummy-D12-5-wind4: landing_descent_m_s=6.253442910356471 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind0: landing_descent_m_s=6.253585548285305 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind2: landing_descent_m_s=6.253514200757778 m/s (allowed None … 6.0)
- 4-actual-D12-5-wind4: landing_descent_m_s=6.253442910356471 m/s (allowed None … 6.0)
- 5-empty-D12-5-wind0: minimum_ascent_stability_cal=0.9744037619826144 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8901885110949699 cal (allowed 1.0 … None)
- 5-empty-D12-5-wind4: minimum_ascent_stability_cal=0.85304437002727 cal (allowed 1.0 … None)
- 5-dummy-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-dummy-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind0: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind2: no numeric criterion failures; consult warnings and missing inputs
- 5-actual-D12-5-wind4: no numeric criterion failures; consult warnings and missing inputs
- 6-empty-D12-5-wind0: minimum_ascent_stability_cal=0.9744037619826157 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8901885110947217 cal (allowed 1.0 … None)
- 6-empty-D12-5-wind4: minimum_ascent_stability_cal=0.85304437002727 cal (allowed 1.0 … None)
- 6-dummy-D12-5-wind0: landing_descent_m_s=6.2535855482848275 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind2: landing_descent_m_s=6.253514200692502 m/s (allowed None … 6.0)
- 6-dummy-D12-5-wind4: landing_descent_m_s=6.253442910195881 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind0: landing_descent_m_s=6.2535855482848275 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind2: landing_descent_m_s=6.253514200692501 m/s (allowed None … 6.0)
- 6-actual-D12-5-wind4: landing_descent_m_s=6.25344291019588 m/s (allowed None … 6.0)
- 7-empty-D12-5-wind0: minimum_ascent_stability_cal=0.9744037619826157 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind2: minimum_ascent_stability_cal=0.8901885110948098 cal (allowed 1.0 … None)
- 7-empty-D12-5-wind4: minimum_ascent_stability_cal=0.8530443700272713 cal (allowed 1.0 … None)
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
