# Provisional print and build guide

This is a reviewable design and assembly plan, not a tested kit. Start with fit coupons and a dry mock-up. Do not load a
motor or powered battery during fabrication/fit work. The [avionics specification](AVIONICS_DESIGN.md) now identifies a
provisional XIAO/GNSS/barometer stack and battery. Its detailed models remain approximations until hardware is measured.

Use one complete candidate's resolved inputs and CAD/ORK files together. Never mix the 15-inch and 18-inch chute
configurations. Dimensions below are the v1 interfaces; the chosen run's files are authoritative for candidate
dimensions. The avionics variant adds locating rails, an antenna shelf, pressure ports and sealing interfaces; follow
its dedicated specification rather than the older generic-tray dimensions below.

## Parts and interfaces

| Generated part                         | Quantity | Function / interface                                                                                           |
| -------------------------------------- | -------: | -------------------------------------------------------------------------------------------------------------- |
| `nose-bay.stl`                         |        1 | Conical nose with integral internal bay sleeve; slides into measured BT-60 ID with configured radial clearance |
| `bay-bulkhead.stl`                     |        1 | 3 mm removable aft cap; three M2 clearance holes to nose bosses, central M3 recovery eye hole                  |
| `payload-sled.stl`                     |        1 | Removable generic 2 mm tray with tie slots and foot; two M2 screws attach it to the cap                        |
| `fin-collar.stl`                       |        1 | Three fins and external tube sleeve; 8 mm tapered leading fairing, bonded to paper airframe                    |
| `lug-sleeve-1.stl`, `lug-sleeve-2.stl` |   1 each | Raised sleeves holding purchased paper lugs; align at 60° between fins, not at a fin's azimuth                 |

The complete STEP includes purchased tube, motor-mount and ring envelopes, chute packing envelope and paper lugs. These
colored envelopes are **not** additional printable parts. `assembly.svg` is a labeled schematic, not a dimensioned
fabrication drawing. `interfaces.json` specifies guide geometry. The open aft end accepts the commercial motor; its
mount block resists thrust and its hook retains the motor. Do not substitute a printed motor tube/block.

## Printing assumptions

PLA is the demonstration material at 1.24 g/cm³. PETG is supported by selecting `material: PETG` and an explicit
appropriate density; rerun mass and flight checks. Neither material name establishes strength or thermal suitability.

For an X1 Carbon, provisional starting settings are 0.4 mm nozzle, 0.2 mm layers, three walls for the 1.2 mm shell, and
solid thin fins/bosses/cap. Slice and inspect every layer; thin features may need adjusted line widths. A local unsliced
fit-check Bambu Studio project can be generated with `scripts/package_bambu.py`; no G-code is validated. CAD volume ×
density assumes solid modeled material, not sparse infill. Record the slicer estimate and actual printed mass.

Current STLs place the nose shoulder-down, cap flat, sled broad-back-down, collar aft-down and lug sleeves vertically.
Earlier exports incorrectly left the collar forward-down and the sled on its small foot; use regenerated files. See
[print-orientation analysis](PRINT_ORIENTATION.md). Use a brim as needed. Inspect shoulder-to-nose bridging, boss
support, the sled foot and fin leading edges; supports, if required, must be fully removable without gouging critical
fits. The nose screws load printed bosses and layer bonds; the collar fins can fail at their roots. Layer orientation is
not a substitute for pull/bend/separation tests.

## Dry fit and assembly order

1. Measure the tube, mount, lugs, recovery hardware and selected payload or dummy. Update inputs before printing. Print
   a short fit sample or spare sleeve/cap first. Deburr without enlarging holes indiscriminately. Reject cracked, porous
   or delaminated pieces. The nose must slide freely without a forced fit.
2. Cut the chosen BT-60 length square: 340 mm compact or 380 mm longer variants. Test fit the external collar and mark
   its axial position. The fairing starts 8 mm ahead of the collar. Fill the tiny clearance-created leading lip with a
   smooth adhesive fillet; OpenRocket approximates it as a continuous taper.
3. Assemble the commercial 18 mm mount following the kit instructions, selecting the BT-60 centering rings. Locate it
   from the chosen configuration; nominal review dimensions are 69.85 mm mount length with 3.2 mm motor overhang beyond
   the mount, and the motor aft end at the airframe aft end. Kit hook access and actual thrust-block location take
   precedence: if they require a different position, update the model and rerun rather than forcing the kit to match.
4. Before bonding the mount into the airframe, attach the Kevlar leader around the mount tube immediately ahead of its
   forward centering ring, with the ring capturing the loop. Route it along the outer edge into the recovery space,
   clear of the motor exhaust/ejection opening and hook. Check that the ring can seat fully without cutting or pinching
   the leader; account for any necessary small routing relief in the actual assembly. This attachment is a design
   proposal requiring a pull test, not a certified load rating.
5. Bond paper-to-paper joints with suitable wood glue and the collar/lug sleeve joints with a verified plastic-to-paper
   adhesive. V2 sleeves have 12 mm-wide, 25 mm-long curved saddles with a provisional 0.15 mm radial adhesive gap,
   replacing the old tangent-contact cylinders. Match the saddle curvature to the measured tube OD; do not clamp hard
   enough to crush the paper or squeeze the joint dry. Add small side fillets and verify bond strength on representative
   tube/printed-saddle coupons. Inspect for paper-surface peeling as well as adhesive failure. Do not use friction alone
   for the collar or lug sleeves. These joints are the unavoidable glue-dependent portions; replacing the collar may
   damage the paper tube. The nose/cap/sled remain mechanically serviceable.
6. Trim two paper lugs to 25 mm, insert them in the sleeves, and align both on a straight rod while bonding, without
   bonding to the rod. Positions are nose-length + 0.30 and 0.65 times body length. The sleeves raise the rod clear of
   the wider collar. Test sliding the **whole rocket** along the actual guide, checking fins, hook, fillets and the pad
   blast-deflector arrangement too.
7. Fasten the sled foot to the cap with its two M2 screws. Fit the M3 recovery eye with a washer on each side and
   locking nut. Keep the eye aft and the short shank/nut inside the bay. Verify clearance to the tray, board and wiring.
   Tie the unpowered payload/dummy to the tray over a nonconductive pad; no loose battery or ballast. Match both dummy
   mass and CG. Installing a real battery later requires compatible protection/charging and independent retention.
8. Slide the sled into the nose bay, close the cap using three M2 screws into the pilots, and check access/removal. Do
   not overtighten into plastic. Apply a removable thin tape seal over the cap perimeter and seal any unused openings;
   verify that screw/eye penetrations do not leak directly onto electronics. The seal is not a thermal barrier or a
   pressure-sensor vent system.
9. Join the Kevlar leader to the 36-inch elastic shock cord using secure inspected loops/knots. Arrange the
   Kevlar-to-elastic junction to reach outside the mouth when extended, reducing the chance of a narrow Kevlar line
   cutting the rim. Tie the elastic to the bulkhead eye; connect the chute's line bundle through the locking swivel near
   the nose end. Confirm the swivel closes securely and cannot snag the cap. The load path is mount/ring → leader →
   elastic → eye/ washers → cap → three screws/bosses → nose. Every link needs inspection.

## Packing, separation and thermal protection

Use the selected Estes chute and its factory shroud lines. Follow the component packing instructions; keep lines
orderly, not wrapped tightly enough to bind. Place commercial
[flame-resistant recovery wadding](https://estesrockets.com/products/recovery-wadding) between the motor's ejection-gas
path and the chute/harness, following its tube-size instructions. Add replaceable wadding layers shielding the cap's hot
face and hardware; the separate 2 g thermal allowance includes this shield and seam tape, while the 2 g wadding item
accounts for the main recovery barrier. These are mass allowances, not instructions to use exactly that weight if the
manufacturer's required packing differs. Weigh and update the actual total.

Do not use ordinary tissue or assume the printed cap alone withstands ejection heat. Wadding is not gas-tight; the cap
seam/penetrations and layer integrity must also be checked. No custom ejection charge or motor modification is proposed.
The existing motor provides deployment; simulated deployment proves neither real separation nor electronics protection.
A club-supervised recovery check using appropriate commercial procedures is required before flight.

The modeled chute bundle is a 30 mm diameter cylinder: about 101 mm long for the 15-inch chute and 146 mm for the
18-inch chute. It begins 10 mm aft of the bay. The longer airframe leaves additional aft space and an annulus for loose
cord, but these geometric envelopes do not prove a real chute/cord/wadding bundle fits. Perform repeated hand extraction
and repacking checks without motors or powered batteries. Do not force the nose home against a compressed bundle. Keep
all recovery lines aft of the sealed cap, out of the nose sliding interface.

The intended separation is the nose shoulder sliding out of the paper tube; the fin collar and motor mount remain fixed.
After any added tape, seal or paint, recheck separation and guide sliding. Record actual mass/CG in empty, secured dummy
and installed configurations and rerun before motor/delay selection.

## Before a field outing

Use [SHOPPING](SHOPPING.md) and [MEASUREMENTS](MEASUREMENTS.md). Have an experienced club/range officer review the
unfamiliar printed structure and recovery joints. Follow commercial motor/controller instructions and the current
[NAR safety code](https://www.nar.org/ModelRocketSafetyCode); this document does not approve a launch site. Stop for any
binding, damage, loose hardware, overheated parts or uncertainty about retention. Inspect after each recovery; three
planned flights do not override the inspection gate.
