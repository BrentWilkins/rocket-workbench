# Current design

The leading build is a **500 mm BT-60 rocket** with a 24 mm Estes D/E motor mount, 50 mm nose, removable camera/logger bay, and the [one-piece integrated fin collar](INTEGRATED_FIN_COLLAR.md). The user-printed raw collar weighs **27 g**; the raw XIAO ESP32-S3 Sense with camera and antenna weighs **6 g**. Finish, remaining hardware, and assembled CG have not been measured. This is a development candidate, **not flight-cleared**.

| Item | Current choice | Still to verify |
| --- | --- | --- |
| Airframe | Two roughly 250 mm sections from Estes BT-60 18-inch tubes, joined with a 3-inch BT-60 coupler | Delivered dimensions, straightness, adhesive mass, bay and chute clearance |
| Motors | **D12-5** first; **E12-6** also modeled | Finished mass/CG, recovery deployment speed, guide departure, launch-field conditions |
| Recovery | 24-inch parachute; Estes EST2271 plastic is a local trial part | Actual packed fit, extraction, mass, descent and drift; earlier runs used a different characterized canopy |
| Launch guide | 3/16-inch Maxi rod | Print or install matching 3/16-inch guides; older sleeves fit 1/8 inch |
| Avionics | XIAO ESP32-S3 Sense camera/SD logger, LIS331 ±24 g accelerometer, LPS28 barometer, protected 400 mAh LiPo | Physical board/battery fit, camera window, pressure ports, wiring and complete installed mass/CG |

The [weighed-part D12/E12 simulation screen](DE_GEOMETRY_SWEEP.md) predicts the nominal D12-5 and E12-6 cases meet the configured stability and deployment-speed checks. In the upper-mass sensitivity case, **E12-6 is close to the 10 m/s deployment-speed screen**, so small finishing or packing changes matter. OpenRocket results are conditional on the input geometry, masses, motor curves, wind and chute assumptions; they are not structural or recovery-system proof. See [what OpenRocket calculates](OPENROCKET.md).

## Build and verification

- [Shopping list](SHOPPING.md) — current HobbyTown cart and items still needed.
- [Build guide](BUILD.md) and [re-verification checklist](REVERIFICATION.md) — dry assembly, measurements and rerun gates before flight.
- [Avionics design](AVIONICS_DESIGN.md) and [measurement ledger](MEASUREMENTS.md) — physical fit and mass inputs.
- [Fin collar STEP, editable CAD and unsliced X1C project](INTEGRATED_FIN_COLLAR.md) — the actual print candidate.

Older 18 mm designs and earlier collar iterations are retained in the [archive](ARCHIVE.md) and repository history, but are not shopping or flight guidance for this build.
