# Build and first-outing shopping guide

Planning date: 2026-09-12. USD advertised prices/allowances, before tax/shipping; stock and local prices may differ.
Nothing has been purchased. Hardware fit, strength and final motor selection remain unverified. The basket below is the
original rocket-hardware budget, not a complete bill of materials for the newer
[XIAO/GNSS/barometer/battery specification](AVIONICS_DESIGN.md). Electronics, extra retention and bay seals are
additional.

## Rocket parts

Quantities below build one rocket; package quantities often leave spares.

| Item                                                                                        | Buy / use                                                                 |  Package cost | Source and qualification                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Estes BT-60 paper airframe #3089                                                            | One 3-tube pack / one tube                                                |        $11.29 | [Manufacturer](https://estesrockets.com/products/bt-60-body-tube); leave uncut until selecting the current candidate and measuring ID/OD                                                                                                             |
| Estes regular 18 mm mount #3158                                                             | One kit / BT-60 ring pair, one mount tube, block, hook and hold-down ring |         $7.99 | [Kit listing](https://www.erockets.biz/estes-flying-model-rocket-part-engine-mount-standard-18mm-to-bt-50-55-60-est-3158/); three mount sets but only one BT-60 ring pair; nominal tube length 2.75 in                                               |
| Estes 15-inch chute #2265 **or** 18-inch LDPE chute #2267                                   | One preassembled chute with lines                                         |         $6.49 | [15 inch](https://estesrockets.com/products/15-inch-printed-parachute), [18 inch](https://estesrockets.com/products/18-inch-printed-parachute); 18 inch is the larger-recovery alternative, not an automatic substitution in a 15-inch configuration |
| Estes Shock Cords & Mount Pack #2278                                                        | One pack / its 1/4 × 36 inch rubber cord                                  |         $6.99 | [Manufacturer](https://estesrockets.com/products/shock-cords-mount-pack); also contains two shorter cords and paper mounts                                                                                                                           |
| 100 lb Kevlar leader, Apogee #30325                                                         | 10 ft minimum order / approximately 2 ft plus knot allowance              |         $8.00 | [Product](https://www.apogeerockets.com/index.php?cPath=42_96&main_page=product_motor_info&page=1&products_id=192); $0.80/ft; strength rating is not an installed attachment rating                                                                  |
| Estes launch-lug pack #2320                                                                 | One pack / two 1/8-inch-rod lugs trimmed to 25 mm                         |         $6.99 | [Manufacturer](https://estesrockets.com/products/launch-lug-pack); measure actual OD before printing the sleeves                                                                                                                                     |
| Small locking snap swivel                                                                   | One, with documented rating above expected recovery load                  |  $3 allowance | Local fishing/model supplier; no exact product/fit verified; include its measured mass in harness ledger                                                                                                                                             |
| Bay fasteners and insulation                                                                | See quantities below                                                      |  $8 allowance | Generic sizes, not a verified retailer quote; buy after test fitting                                                                                                                                                                                 |
| PVA wood glue for paper-to-paper joints; compatible two-part epoxy for plastic/paper joints | Small bottles/pack, mixing sticks and gloves                              | $12 allowance | Follow the chosen adhesive manufacturer's material and ventilation instructions; bond coupons before committing                                                                                                                                      |
| Thin polyimide tape for removable cap seam sealing                                          | One small roll                                                            |  $6 allowance | Not a substitute for flame-resistant wadding or a thermal qualification                                                                                                                                                                              |

Rocket-related packages total
**$76.75**, including allowances and spares, before
filament. Estimated consumed filament is roughly $2 at a planning
rate of $25/kg;
use the actual slicer mass. Budget **about $80** for this package basket, or about
**$101.75** if a new $25 filament spool is needed. This is not the per-rocket consumed material cost; tube/cord/lug
packs and adhesives leave inventory for later builds.

Bay hardware design allowance: three M2 × 8 mm thread-forming screws for the cap, two M2 × 6 mm thread-forming screws
for the sled foot, one M3 closed-eye bolt with approximately 10 mm threaded shank, two M3 washers (8–10 mm OD), one M3
locking nut, two 2.5 mm cable ties and a thin nonconductive cushioning pad. The CAD has 1.6 mm screw pilots, 2.2 mm
clearance holes, and a 3.2 mm eye-bolt hole. Verify the particular screws' pilot requirements and eye-bolt projection;
do not assume all M2 screws are interchangeable. Recovery load passes through printed bosses and must be tested. No
battery is included in this historical basket; the separate avionics specification identifies a provisional 150 mAh
cell.

## Reusable launch equipment and three-flight consumables

| Item                                                | Planning quantity                                      |         Cost | Source / limits                                                                                                                                                                                                         |
| --------------------------------------------------- | ------------------------------------------------------ | -----------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Estes Porta-Pad II + Electron Beam controller #2222 | One set                                                |       $39.99 | [Manufacturer](https://estesrockets.com/products/porta-pad-ii-launch-pad-and-controller); includes 1/8-inch rod and blast deflector; measure usable guide length, do not infer it from this model's 0.9144 m assumption |
| AA alkaline cells                                   | Four installed plus four spare                         | $6 allowance | Controller supply, **not** an avionics battery                                                                                                                                                                          |
| Estes C5-3 engines #10022                           | One three-motor pack, only after measured-model review |       $14.99 | [Manufacturer](https://estesrockets.com/products/c5-3-engines); pack includes four starters and four plugs; no separate ignition hardware is designed here                                                              |
| Estes flame-resistant recovery wadding #2274        | One package, enough for three preparations with spares |        $5.99 | [Manufacturer](https://estesrockets.com/products/recovery-wadding); follow the package's tube-size packing instructions; includes extra layers shielding the bay cap                                                    |

Launch equipment plus the eight-cell allowance: **$45.99**. Initial consumable
packages: **$20.98**. Combined planning
basket is **$143.72 plus filament**, or
about **$170 with a new
$25 spool**, excluding tools, tax and shipping. A three-
flight plan is not permission to fly three times regardless of inspection.
Nominal recurring cost is roughly $5
per motor plus wadding; replace damaged cords/chutes/parts rather than treating them as unlimited-life consumables.

Also needed if not already owned: calipers, a 0.1 g scale, ruler, cutting mat, fine saw/knife, deburring tools, small
drivers, eye protection, suitable gloves, and field fire-safety supplies. Allow $40–80 for basic measuring/build tools;
this is an unresearched planning allowance, not included above. Adult handling of cutting, hot printing, adhesives and
launch preparation is assumed.

## Purchase gates

BT-60 tubes (uncut), commercial recovery wadding, the shock-cord pack and reusable launch equipment are broadly
reusable. The correct 18 mm-to-BT-60 mount and either listed chute are sensible provisional supplies, but keep packaging
and measure them before fabrication. Do not buy 24 mm mounts or substitute a motor based only on its letter. Delay and
thrust-curve identity matter.

Hold the final motor/delay, battery, sensor stack and bay fasteners until their respective mass/fit checks. The nominal
C5-3 choice is a simulation result, not a physical launch approval. Consult the current
[NAR Model Rocket Safety Code](https://www.nar.org/ModelRocketSafetyCode), component instructions, local rules,
landowner permission and a local club/range officer. The workbench does not determine site legality or suitability.
