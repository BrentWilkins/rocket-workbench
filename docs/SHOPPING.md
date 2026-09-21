# D12 / BT-60 shopping list

This is the parts list for the **500 mm BT-60 development build** with the printed integrated fin collar. It is not
flight clearance. The cart below was shown for **HobbyTown Westminster (Denver Metro) on 2026-09-19**; its prices and
pickup selections are a snapshot, not confirmation that every item is on the shelf. Confirm availability before driving.

## Current HobbyTown cart

| Part                                                                                                                     | SKU     | Cart price | Decision                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------ | ------- | ---------: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| [BT-60 body tubes, 3 × 18 in](https://www.hobbytown.com/estes-bt60-body-tubes-3-est3089/p108068)                         | EST3089 |     $11.29 | Buy; cut two sections to about 250 mm each after a full dry fit.                                                                                    |
| [BT-55/BT-60 couplers, pack of 6](https://www.hobbytown.com/estes-bt55-bt60-rocket-body-tube-couplers-6-est3177/p608173) | EST3177 |      $5.99 | Buy; use one 3-inch BT-60 coupler.                                                                                                                  |
| [D/E motor mount kit](https://www.hobbytown.com/estes-model-rocket-d-e-engine-mount-kit-bt55-60-80-est3159/p38843)       | EST3159 |     $11.99 | Buy the **24 mm D/E** kit, not 19 mm EST3158. Check its D-motor spacer and retention against the actual motors.                                     |
| [Two-piece 3/16-inch Maxi rod](https://www.hobbytown.com/estes-two-piece-maxi-rod-3-16-est2244/p802204)                  | EST2244 |     $14.99 | Buy if it fits the launch pad. Matching **3/16-inch rocket guides are not yet built**; older printed sleeves are 1/8 inch.                          |
| D12-5, two motors                                                                                                        | EST1028 |     $14.99 | Current first motor candidate.                                                                                                                      |
| E12-6, three motors                                                                                                      | EST1693 |     $26.49 | Optional second motor candidate; the cart says **in-store pickup only**. Final mass and recovery checks matter particularly for E12-6.              |
| [Estes 24-inch plastic parachute](https://www.hobbytown.com/estes-parachute-24-est2271/p802207)                          | EST2271 |      $6.99 | Practical local **trial canopy**. Weigh it and test packing/ejection; it is not the nylon chute used to characterize the existing recovery results. |

The cart also includes **B6-4 (EST10021, $12.99)** and **C6-7 (EST10038, $13.99)**. Those are not motors for this 24 mm
D/E build; keep them only for another rocket. The seven current-build items above total **$92.73 before tax** at the
displayed prices. The cart's pickup setting does not establish physical stock.

## Avionics order (single order, vendor TBD)

Prices are Adafruit MSRP as of 2026-09-20. DigiKey resells these at MSRP, so the vendor choice is about shipping events
and stock, not unit price. Every DigiKey number below was **verified against the exported cart on 2026-09-20**, all in
stock with no backorders. The `1528-<PID>-ND` pattern holds for the newer boards but **not** for older parts: 3898 is
`1528-2731-ND`, 1131 is `1528-1494-ND`, 3658 is `1528-2528-ND`, and the wire colors are offset by 14. Search by Adafruit
PID and read the description rather than constructing a number.

| Item                                     | Adafruit PID | DigiKey        | Qty |    Ea. | Note                                            |
| ---------------------------------------- | ------------ | -------------- | --: | -----: | ----------------------------------------------- |
| ICM-20649 6-DoF IMU, ±30 g / ±4000 dps   | 4464         | `1528-4464-ND` |   1 | $14.95 | Replaces LIS331 4626: EOL, and ±24 g is tight   |
| LPS28DFW pressure sensor                 | 6067         | `1528-6067-ND` |   1 | $12.50 | Mount inside the pressure chamber               |
| LIS3MDL magnetometer                     | 4479         | `1528-4479-ND` |   1 |  $9.95 | Ground use for rail aiming; not flown initially |
| Protected 400 mAh LiPo, 3.7 V            | 3898         | `1528-2731-ND` |   1 |  $6.95 | 37 × 17.5 × 8.2 mm, 8.2 g                       |
| JST-PH extension, 500 mm                 | 1131         | `1528-1494-ND` |   1 |  $1.95 | Cut in half; **male** end solders to BAT pads   |
| STEMMA QT to male header, 150 mm         | 4209         | `1528-4209-ND` |   1 |  $0.95 | XIAO to first sensor board only                 |
| STEMMA QT to QT cable, 100 mm            | 4210         | `1528-4210-ND` |   2 |  $0.95 | Daisy-chain board to board                      |
| Silicone wire 30 AWG, 2 m, red           | 2001         | `1528-2015-ND` |   1 |  $0.75 | Hookup and strain-relief loops                  |
| Silicone wire 30 AWG, 2 m, blue          | 2002         | `1528-2016-ND` |   1 |  $0.75 |                                                 |
| Silicone wire 30 AWG, 2 m, black         | 2003         | `1528-2017-ND` |   1 |  $0.75 |                                                 |
| Silicone wire 30 AWG, 2 m, yellow        | 2004         | `1528-2018-ND` |   1 |  $0.75 |                                                 |
| Nylon M2.5 screw and standoff set, white | 3658         | `1528-2528-ND` |   1 | $14.95 | Breakout holes are 2.5 mm, not M2               |

**$67.10** as listed. Deliberately excluded: LIS331 4626 (superseded and EOL) and Adafruit 261 (female, will not mate
with the 3898).

The XIAO has no STEMMA QT connector, so exactly one QT-to-header cable is needed. Each sensor board carries two QT
connectors and chains to the next, so the bus runs XIAO to IMU to barometer, leaving a free jack for the magnetometer
during ground use. That lands **four wires on the XIAO pads instead of twelve** and cuts harness mass, at the same price
as three header cables. The 100 mm 4210 was chosen over the 50 mm 4399 because the sled layout is unfinished and the bay
is 145 mm. Chain order is a serviceability constraint, not a firmware one: unplugging a mid-chain board drops every
board behind it, so bench-test in flight order.

Adafruit's own listing for 4464 shows out of stock and at least one distributor reports the ICM-20649 as
**discontinued**; this is unconfirmed. DigiKey stock was the only source at time of order. Consider a spare if the part
is respun into the design.

Lithium cells ship ground-only from either vendor, so splitting the order across vendors adds a shipping event without
removing that constraint. Confirm the delivered battery connector **and polarity** before soldering.

### Ordered 2026-09-20

DigiKey web ID **376869941**, 12 lines, $67.10 subtotal + $8.49 shipping + $6.74 tax = **$82.33**. Every line was
verified against the exported cart before checkout; all in stock, no backorders.

**Weigh and measure on arrival.** Several ledger entries are allowances, not measurements, and the delivered parts
settle them:

| Part                     | Current ledger value                   | Why it matters                                                     |
| ------------------------ | -------------------------------------- | ------------------------------------------------------------------ |
| ICM-20649 4464           | 2.00 g nominal / 3.00 g upper, no STEP | Pure allowance inherited from the LIS331HH; envelope is unmodelled |
| LiPo 3898                | 8.20 g, approx. 37 × 17.5 × 8.2 mm     | 38% of payload mass; thickness drives the radial clearance         |
| JST-PH pigtail from 1131 | 0.50 g                                 | Measure after cutting to final length                              |
| LPS28 6067               | 1.80 g published                       | Confirm, and check connector proudness against the chamber design  |
| 4209 + 2 × 4210 harness  | inside the 1.50 g wiring allowance     | Weigh the made-up chain, not the loose cables                      |

The tightest modelled radial clearance is **0.465 mm** at the antenna corner, so delivered board thickness and connector
height are fit-critical, not just mass-critical. Update the mass table, payload CG and the D12-5 / E12-6 cases once
measured.

## Still needed or deliberately deferred

- **Recovery:** a shock cord/leader, attachment hardware, swivel, and flame-resistant wadding.
  [The recovery-anchor plan](RECOVERY_ANCHOR.md) covers the load path. The
  [Top Flight 24-inch thin-mil nylon chute](https://www.siriusrocketry.biz/ishop/top-flight-recovery-24-inch-thin-mil-parachute-72.html)
  remains a smaller-packing alternative if the Estes plastic chute does not work in the actual bay. The
  [Estes 30-inch nylon chute](https://www.hobbytown.com/estes-nylon-parachute-30-est2273/p608133) is a possible
  _larger-airframe_ option, not a drop-in substitute here.
- **Electronics:** owned XIAO ESP32-S3 Sense, plus the sensors, battery and cabling in the
  [avionics order](#avionics-order-single-order-vendor-tbd) above. GPS is optional later. The
  [avionics design](AVIONICS_DESIGN.md) and [firmware design](FIRMWARE.md) were updated to the ICM-20649 on 2026-09-20,
  replacing the EOL LIS331HH. The ICM board envelope and mass are **unmeasured allowances**: weigh and measure it on
  arrival before the layout and CAD pass.
- **Assembly:** paper launch guides sized for the 3/16-inch rod, compatible adhesive for paper-to-paper and PLA-to-paper
  joints, primer/paint if desired, and small **M2.5** nylon hardware once actual printed fit is checked (Adafruit
  breakouts use 2.5 mm mounting holes, not M2). Test the collar bond on spare tube and printed material. Keep finish out
  of the camera window, pressure ports, coupler, motor mount, and guides.

## Before cutting or flying

Dry-fit the tube, 3-inch coupler, mount, 145 mm avionics bay, collar, and packed recovery system before cutting or
gluing. Two roughly 250 mm tube sections give about 38 mm coupler engagement per side, but their exact cuts depend on
delivered parts. The existing OpenRocket runs model the 500 mm body with **provisional masses**; they do not prove
splice alignment, joint strength, chute extraction, or the new guide interface. Weigh the finished collar, coupler and
adhesive, chute/harness, electronics, and complete assembled rocket; measure loaded CG and rerun D12-5 and E12-6 cases.
The E12-6 upper-mass deployment-speed margin is narrow. Follow the [build gates](BUILD.md),
[measurement list](MEASUREMENTS.md), and [re-verification checklist](REVERIFICATION.md).
