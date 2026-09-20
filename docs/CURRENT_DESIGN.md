# Current design

The **recommended study candidate is a 530 mm BT-60 body with a 40 mm ogive**, 24 mm Estes D/E motor mount, removable
camera/logger bay, and the existing [one-piece integrated fin collar](INTEGRATED_FIN_COLLAR.md). The
[final robustness report](FLIGHT_ROBUSTNESS.md) finds more modeled stability margin for only **2.35 m less D12 altitude
/ 4.02 m less E12 altitude** than the 500 mm ogive. Better real-world wind handling is not established. This is **not
flight-cleared**.

The existing build baseline and manufacturing artifacts remain **500 mm body / 50 mm conical nose**; the recommendation
is not an as-built claim or an updated print release. The raw collar weighs **27 g** and the raw XIAO ESP32-S3 Sense
with camera and antenna weighs **6 g**. Finish, remaining hardware and assembled CG still need measurement.

| Item         | Current choice                                                                                            | Still to verify                                                                                                        |
| ------------ | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Airframe     | Recommended 530 mm joined BT-60 body and 40 mm ogive; existing baseline is 500 mm                         | Update build configuration/CAD before cutting or printing; verify delivered dimensions, joint, bay and chute clearance |
| Motors       | **D12-5** first; **E12-6** also modeled                                                                   | Finished mass/CG, recovery deployment speed, guide departure, launch-field conditions                                  |
| Recovery     | 24-inch parachute; Estes EST2271 plastic is a local trial part                                            | Actual packed fit, extraction, mass, descent and drift; earlier runs used a different characterized canopy             |
| Launch guide | Investigate a compatible 60-inch guide; 36-inch cases miss the departure-speed screen                     | Actual diameter, stiffness, usable travel and friction; older sleeves fit 1/8 inch, not the planned 3/16 inch          |
| Avionics     | XIAO ESP32-S3 Sense camera/SD logger, LIS331 ±24 g accelerometer, LPS28 barometer, protected 400 mAh LiPo | Physical board/battery fit, camera window, pressure ports, wiring and complete installed mass/CG                       |

The [paired flight-robustness study](FLIGHT_ROBUSTNESS.md) finds that corrected **36-inch guide-exit speeds fall below
the configured 12 m/s planning screen**. A 60-inch guide improves the heavier-construction cases to **15.84–16.65 m/s**,
but their 6 m/s crosswind deployment speeds still exceed the **10 m/s screen**. The rocket is **not flight-cleared**:
guide fit, finished mass/CG, recovery timing and actual field conditions remain consequential.

The study compares this physical baseline with 500 mm and 530 mm ogive candidates, correcting usable guide travel for
the aft-lug offset and separating powered-flight attitude from apogee. The [geometry sweep](PAYLOAD_SWEEP.md) remains
useful preliminary design context, not current launch-clearance evidence. See
[what OpenRocket calculates](OPENROCKET.md) for the model boundaries; simulation does not prove structural strength or
recovery-system reliability.

## Build and verification

- [Shopping list](SHOPPING.md) — current HobbyTown cart and items still needed.
- [Build guide](BUILD.md) and [re-verification checklist](REVERIFICATION.md) — dry assembly, measurements and rerun
  gates before flight.
- [Avionics design](AVIONICS_DESIGN.md) and [measurement ledger](MEASUREMENTS.md) — physical fit and mass inputs.
- [Fin collar STEP, editable CAD and unsliced X1C project](INTEGRATED_FIN_COLLAR.md) — the actual print candidate.

Older 18 mm designs and earlier collar iterations are retained in the [archive](ARCHIVE.md) and repository history, but
are not shopping or flight guidance for this build.
