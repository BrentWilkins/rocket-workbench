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

## Still needed or deliberately deferred

- **Recovery:** a shock cord/leader, attachment hardware, swivel, and flame-resistant wadding.
  [The recovery-anchor plan](RECOVERY_ANCHOR.md) covers the load path. The
  [Top Flight 24-inch thin-mil nylon chute](https://www.siriusrocketry.biz/ishop/top-flight-recovery-24-inch-thin-mil-parachute-72.html)
  remains a smaller-packing alternative if the Estes plastic chute does not work in the actual bay. The
  [Estes 30-inch nylon chute](https://www.hobbytown.com/estes-nylon-parachute-30-est2273/p608133) is a possible
  _larger-airframe_ option, not a drop-in substitute here.
- **Electronics:** owned XIAO ESP32-S3 Sense; [LIS331 ±24 g accelerometer](https://www.adafruit.com/product/4626),
  [LPS28 pressure board](https://www.adafruit.com/product/6067),
  [protected 400 mAh LiPo](https://www.adafruit.com/product/3898), and
  [JST-PH female-wire pigtail](https://www.adafruit.com/product/261). Verify the delivered battery connector **and
  polarity** before soldering. GPS is optional later. See [avionics design](AVIONICS_DESIGN.md).
- **Assembly:** paper launch guides sized for the 3/16-inch rod, compatible adhesive for paper-to-paper and PLA-to-paper
  joints, primer/paint if desired, and small M2 hardware once actual printed fit is checked. Test the collar bond on
  spare tube and printed material. Keep finish out of the camera window, pressure ports, coupler, motor mount, and
  guides.

## Before cutting or flying

Dry-fit the tube, 3-inch coupler, mount, 145 mm avionics bay, collar, and packed recovery system before cutting or
gluing. Two roughly 250 mm tube sections give about 38 mm coupler engagement per side, but their exact cuts depend on
delivered parts. The existing OpenRocket runs model the 500 mm body with **provisional masses**; they do not prove
splice alignment, joint strength, chute extraction, or the new guide interface. Weigh the finished collar, coupler and
adhesive, chute/harness, electronics, and complete assembled rocket; measure loaded CG and rerun D12-5 and E12-6 cases.
The E12-6 upper-mass deployment-speed margin is narrow. Follow the [build gates](BUILD.md),
[measurement list](MEASUREMENTS.md), and [re-verification checklist](REVERIFICATION.md).
