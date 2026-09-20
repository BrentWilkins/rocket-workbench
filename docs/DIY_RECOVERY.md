# Shop-made recovery canopy — sourcing and construction notes

Research notes captured 2026-09-19. Nothing here is built, measured or flown. This page records why a homemade canopy
is worth considering for this airframe, where to buy suitable fabric locally, and which construction details are
reported failure points. It is not a build procedure and carries no flight-clearance claim.

## Why DIY is interesting here specifically

Packing volume, not canopy area, is the binding constraint on this build. The 500 mm airframe leaves **241.8 mm** after
the bay, mount, overhang and clearance, against a **228.2 mm** modeled packed length for a 24-inch canopy — roughly
**13.6 mm of margin**. Fabric weight is the main lever on that number, and the lightest finished 24-inch chute on the
market is 1.1 oz.

Sewing one is the only route to fabric lighter than any vendor sells finished. That is the entire argument for DIY here;
it is not a cost argument. See [the shopping list](SHOPPING.md) for the purchasable options.

## Fabric: local sources beat shipping

| Source                              | Weight         |          Price | Notes                                            |
| ----------------------------------- | -------------- | -------------: | ------------------------------------------------ |
| Into The Wind, 1408 Pearl St, Boulder | 0.75 oz       | $14.50/yd      | 54 in wide, 1 yd minimum per color, made in USA   |
| Ripstop by the Roll (online)        | 0.66–1.0 oz    | varies         | MEMBRANE 10 taffeta 0.66 oz; HyperD 1.0 oz        |
| Rockywoods Fabrics, Loveland        | 1.9 oz coated  | varies         | Local, but heavier than the commercial thin-mil   |

Into The Wind is the practical pick: 0.75 oz undercuts the 1.1 oz thin-mil, Boulder is a no-shipping errand, and the
fabric is described as coated, windproof, with little stretch, and cutting without fraying. It ships folded rather than
rolled if ordered rather than collected.

Commercial reference points for comparison: Top Flight thin-mil is **1.1 oz**, Top Flight standard is **1.7 oz**, and
the Apogee 29093 is **16.9 g** finished in a rip-stop described as feeling like silk.

### Yield and real cost

A 24-inch hexagon measured flat-to-flat spans 27.7 in vertex-to-vertex. Two nest comfortably across the 54-inch width
within a single 36-inch yard, so **one yard yields two canopies** with scrap remaining — about $7.25 of fabric each.

The first canopy still costs more than buying one: $14.50 of fabric plus line and hardware against a $13.50 finished
thin-mil. DIY breaks even only across multiple canopies, or buys packing margin the market does not sell.

## Construction details that are reported failure points

**Do not glue the shroud lines on.** Glued tape tabs and paper reinforcing disks are the documented tear-out mode —
builders report lines pulling straight through paper disks on first deployment. Plastic disks are stronger than paper,
and duct-tape V-tabs cut parallel to the tape's fiber direction are used as repairs, but neither is the primary method.

- **Sewn attachment is the standard.** Run the shroud line about an inch in from the edge, turn, and stitch back, so
  roughly two inches is anchored per line. The doubled-back stitch spreads load into the canopy instead of
  concentrating it at a point.
- **No sewing machine:** grommets set over a backing layer beat adhesive tabs. Expect to need a grommet plier and hole
  punch, and to thicken the grommet area with backing material or the grommet seats loose.
- **Edge treatment:** cut with a low-wattage soldering iron or a wood burner over a template. Searing the edge prevents
  fray propagation into the attachment points.
- **Line material:** braided nylon. A little stretch protects the canopy from ejection shock. Avoid Kevlar and Spectra
  here — inelastic line into a reinforced tab is the classic tear-out combination, and Kevlar's flame resistance is
  moot because the nylon canopy melts first.

Match the Apogee geometry if a starting point is wanted: hexagonal, 24 in flat-to-flat, 24 in shroud lines.

## Open items before this could be used

1. A shop-made canopy has **no published Cd**. The completed study sweeps Cd 0.53–1.04, which is wide enough to bracket
   a conventional hex canopy, but that is a modeling range — not a measurement of this chute.
2. It needs a **measured mass/CG and a physical pack test in the delivered tube**, exactly like any purchased
   substitute. It does not inherit the 192/192 recovery result.
3. **Ejection-gas protection is unresolved at this diameter.** Commercial parachute protectors are commonly sized for
   2–3 inch tubes; this airframe is 1.6 inch. Wadding or a suitably sized blanket needs to be chosen and its volume
   counted against the same 13.6 mm packing margin.
4. Sewn seams and grommets add bulk at the canopy edge. Whatever is built has to be packed and measured, not assumed
   to match the modeled envelope.

## Sources checked 2026-09-19

- [Into The Wind 0.75 oz ripstop, $14.50/yd](https://intothewind.com/products/75-oz-ripstop-nylon)
- [Ripstop by the Roll ultralight nylon](https://ripstopbytheroll.com/collections/ultralight-nylon-fabric/windproof) and
  [Rockywoods coated ripstop](https://rockywoods.com/products/coated-ripstop-nylon-fabric)
- Rocketry Forum threads on
  [shroud line attachment](https://www.rocketryforum.com/threads/parachute-shroud-line-attachment-to-canopy.175706/),
  [home made parachutes](https://www.rocketryforum.com/threads/home-made-parachutes.111362/),
  [ripstop without a sewing machine](https://www.rocketryforum.com/threads/ripstop-w-o-a-sewing-machine.166244/) and
  [shroud line material](https://www.rocketryforum.com/threads/parachute-shroud-line-material.190281/)
- [Apogee 29093 specification](https://www.apogeerockets.com/index.php?cpath=&main_page=product_supplies_info&products_id=2283)
  for the 16.9 g / hexagonal / 24 in shroud reference geometry
