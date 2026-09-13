# Powered-flight acceleration study

50 mm conical nose, revised lug saddles, provisional 18 g loaded payload; no physical validation.

[Nominal-step full report](nominal/report.md) | [Half-step full report](half-step/report.md)

All 30 motor/loading/wind cases remain visible, including failed criteria. Half-step differences check numerical
sensitivity, not uncertainty in the hardware or thrust curve.

| Case              | Peak trajectory g | Estimated load g | Peak powered m/s | Load change on halving step g |
| ----------------- | ----------------: | ---------------: | ---------------: | ----------------------------: |
| empty-A8-3-wind0  |             6.671 |            7.670 |           11.343 |                         0.000 |
| empty-A8-3-wind2  |             6.665 |            7.663 |           11.289 |                         0.000 |
| empty-B4-4-wind0  |             8.840 |            9.839 |           22.274 |                         0.000 |
| empty-B4-4-wind2  |             8.836 |            9.835 |           22.065 |                         0.000 |
| empty-C6-3-wind0  |             9.562 |           10.561 |           43.173 |                         0.000 |
| empty-C6-3-wind2  |             9.553 |           10.552 |           42.979 |                         0.000 |
| empty-C6-5-wind0  |             9.562 |           10.561 |           43.173 |                         0.000 |
| empty-C6-5-wind2  |             9.553 |           10.552 |           42.979 |                         0.000 |
| empty-C5-3-wind0  |            14.352 |           15.351 |           33.863 |                         0.000 |
| empty-C5-3-wind2  |            14.341 |           15.340 |           33.686 |                         0.000 |
| dummy-A8-3-wind0  |             5.736 |            6.735 |            9.263 |                         0.000 |
| dummy-A8-3-wind2  |             5.732 |            6.731 |            9.224 |                         0.000 |
| dummy-B4-4-wind0  |             7.662 |            8.661 |           18.645 |                         0.000 |
| dummy-B4-4-wind2  |             7.659 |            8.658 |           18.414 |                         0.000 |
| dummy-C6-3-wind0  |             8.330 |            9.329 |           37.222 |                         0.000 |
| dummy-C6-3-wind2  |             8.324 |            9.323 |           37.053 |                         0.000 |
| dummy-C6-5-wind0  |             8.330 |            9.329 |           37.222 |                         0.000 |
| dummy-C6-5-wind2  |             8.324 |            9.323 |           37.053 |                         0.000 |
| dummy-C5-3-wind0  |            12.561 |           13.560 |           28.823 |                         0.000 |
| dummy-C5-3-wind2  |            12.550 |           13.549 |           28.645 |                         0.000 |
| actual-A8-3-wind0 |             5.736 |            6.735 |            9.263 |                         0.000 |
| actual-A8-3-wind2 |             5.732 |            6.731 |            9.224 |                         0.000 |
| actual-B4-4-wind0 |             7.662 |            8.661 |           18.645 |                         0.000 |
| actual-B4-4-wind2 |             7.659 |            8.658 |           18.414 |                         0.000 |
| actual-C6-3-wind0 |             8.330 |            9.329 |           37.222 |                         0.000 |
| actual-C6-3-wind2 |             8.324 |            9.323 |           37.053 |                         0.000 |
| actual-C6-5-wind0 |             8.330 |            9.329 |           37.222 |                         0.000 |
| actual-C6-5-wind2 |             8.324 |            9.323 |           37.053 |                         0.000 |
| actual-C5-3-wind0 |            12.561 |           13.560 |           28.823 |                         0.000 |
| actual-C5-3-wind2 |            12.550 |           13.549 |           28.645 |                         0.000 |

Estimated load restores local gravity to trajectory acceleration; neglects Coriolis and sensor-offset rotation. Not a
per-axis IMU prediction, shock rating, or certification. See full reports for definitions.
