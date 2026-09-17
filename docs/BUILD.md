# D12 / BT-60 provisional build guide

This guide describes the **500 mm body, 24-inch recovery, insert-bay review candidate**, not a flight-qualified kit. Use
its matching configuration, CAD and print project from [current designs](CURRENT_DESIGN.md). The 460 mm / 22-inch
alternative is separate. Earlier 18 mm cut lengths are in the [archived build guide](BUILD_18MM.md).

## Configuration and parts

| Item                    | Current modeled value                                             | Required check                                       |
| ----------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| BT-60 body              | 500 mm long, OD 41.6 / ID 40.5 mm                                 | Delivered dimensions; keep uncut until dry fit       |
| Nose / internal bay     | 50 / 145 mm                                                       | Sliding fit, antenna clearance, seals and extraction |
| Clipped-delta collar v2 | 65 mm root/collar, 53.65 mm span, 2.0 mm fins, tangent root coves | Printed root strength and bond                       |
| Commercial motor mount  | 24 mm, provisional 95 mm length                                   | Actual rings, hook, block, spacer, installed mass    |
| Recovery                | Apogee 29093 24-inch canopy                                       | Actual mass, packing and deployment                  |
| Canopy packing envelope | 32 mm diameter × 228.22 mm long                                   | Not proof of actual packing                          |
| Bay cap                 | 3 mm, three relocated M2 insert bosses                            | Installation, engagement, mass and strength          |

Print six parts: nose-bay, bay-bulkhead, payload-sled, fin-collar and two lug sleeves. Electronics, paper tube, mount
and recovery envelopes in the assembly STEP are **not printable parts**. The X1C project uses a 0.4 mm nozzle, Textured
PEI and provisional PLA. CAD mass assumes solid material; slicer support/brim waste is not installed flight mass. Local
slicing and placement checks passed, but inspect toolpaths and removable supports before printing.

The current standalone [organic fin-collar v2](FIN_COLLAR_V2.md) replaces only the older 1.6 mm square-edge collar in
the six-part project. Import its STL into Bambu Studio separately. Its 2.0 mm fins have rounded leading/tip edges, a 0.7
mm trailing edge, and true cylinder-to-fin tangent root coves. The older project remains useful for the other five
parts, but its fin collar is superseded. Native slicing of v2 has not been run on this Linux workstation.

## Dry assembly sequence

1. Work without a motor or powered battery. Measure purchased parts, update inputs and rerun when they differ. Start
   with fit samples; reject cracked or delaminated prints.
2. Dry-fit the complete bay, recovery bundle, mount and leader before cutting the body. The modeled 500 mm length does
   not override interference found with delivered hardware.
3. Follow the commercial 24 mm mount instructions, including the appropriate D-length spacer. Do not print substitutes
   for the motor tube, thrust block or retention hardware. Reconcile actual hook access, ring positions and the modeled
   3.2 mm overhang before bonding; do not force the kit to match an assumed mount length.
4. Fit the proposed motor-ring-captured Kevlar leader before installing the mount. Keep it clear of seating surfaces,
   sharp edges and the motor path. Check the [whole recovery load path](RECOVERY_ANCHOR.md), not just the cord rating.
5. Bond collar and curved lug saddles using an adhesive checked on representative plastic/paper coupons. Do not rely on
   friction or crush the tube. Fit purchased paper lugs and align the whole rocket on the actual guide, checking fins,
   collar, hook and fillets. Use this configuration's CAD `interfaces.json`, not shorter-airframe positions.
6. The insert trial uses TC-M2x3.0 receiving geometry at 10/170/270 degrees. Test installation in a representative spare
   boss first. The printed-pilot cap is a different configuration, not a drop-in insert part. Screw length must account
   for the real cap, washer, insert seating and engagement; see [fastener sourcing](RECOVERY_ANCHOR.md).
7. Attach the sled foot with its two M2 fasteners. Install the central recovery eye with washers and locking nut,
   checking real shank length and clearance. Exact hardware remains provisional. Secure the unpowered logger or
   mass/CG-matched dummy with insulation and independent retention.
8. Follow the revised wire-routing envelopes when inserting the sled; arbitrary cable loops can invalidate the clearance
   check. Verify bend radius, tool access and repeated removal with real connectors. Close without forcing or
   overtightening the joint.
9. Keep recovery lines aft of the cap and out of the sliding nose interface. Join the short internal Kevlar leader to
   replaceable elastic, with the transition below the tube lip as described in the sourced harness guide. Final lengths
   and complete harness mass are not established by the current 5 g allowance.

## Pressure, recovery and inspection gates

The printed sleeve ports also require matching holes in the paper airframe: three 1.0 mm holes, 120° apart, 125 mm aft
of the shoulder (175 mm from this nose tip). Mark their alignment during dry fit and remove electronics before drilling.
Deburr and verify both layers remain aligned in the assembled position. Otherwise the paper tube can block an apparently
open printed port. Check sleeve-annulus seals as well as the cap seam and fastener penetrations; the seal grooves are
not proof that a purchased seal will fit or permit free nose separation.

Preserve the three modeled static ports and isolated sensing region; do not seal the ports with paint, tape or glue.
Seal unintended paths from the recovery space into electronics. Port presence does not prove dynamic pressure accuracy.
See [avionics details](AVIONICS_DESIGN.md).

Use commercial flame-resistant recovery protection and manufacturer packing instructions. PLA and seam tape are not
qualified ejection-heat barriers. Ledger thermal/wadding masses are estimates, not prescribed gram quantities. Check
repeated hand extraction of the packed nose/chute/cord without a motor or powered battery; modeled clearance does not
prove deployment.

Before flight consideration, measure complete empty, dummy and logger mass/CG, verify representative retention/bond
strength, pressure response and recovery separation, then rerun measured inputs. Inspect after recovery. Follow
commercial instructions and obtain an experienced club/range review; simulations do not determine site legality, weather
suitability or launch clearance. No active-control system is included.

Use [shopping/sourcing](SHOPPING.md) and the [measurement checklist](MEASUREMENTS.md). Substituting the owned 15-inch
chute or a different motor/delay requires another comparison. No printer commands or purchases have been made.
