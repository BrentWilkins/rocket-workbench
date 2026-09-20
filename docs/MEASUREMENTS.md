# Measurement and physical review gates

## Measurements reported 2026-09-19

- Current one-piece fin collar: **27 g as printed**, including a tiny amount of brim still to remove. This is not a
  finished painted mass; primer, sanding, and paint may change it. Its axial CG has not been measured, so the
  STEP-derived 522.285 mm nose-tip station remains an estimate.
- XIAO ESP32-S3 Sense with camera and WiFi antenna: **6 g raw**. This excludes final solder, wiring, mounting,
  and any installed accessory not on the scale.

The measured-mass simulation uses 27 g for the bare collar and 6 g for the raw XIAO. Its upper case adds a
**provisional 3 g collar finish allowance**, while leaving other unmeasured masses at their existing upper bounds.
Record a cleaned/finished collar mass and complete assembled CG later; buying all remaining electronics is not a
prerequisite to continue design work.

Nothing below is claimed completed by the software tests. Record date, method, instrument resolution and uncertainty;
enter quantities with `provenance: measured` and a meaningful `source`. Keep untouched copies of original run inputs.

## Before final fabrication

- Each BT-60 section's ID/OD, roundness, actual cut length, and mass/CG; collar/nose fit on the tube.
- Selected 3-inch coupler's mass/CG and engagement depth on both sides; joint-adhesive mass/CG, assembled straightness,
  external seam, and repeated fit through the collar/nose/launch guide. The coupler is a new ledger item, not part of
  the earlier unjointed-body evidence. Record the combined coupler plus joint adhesive as the optional
  `airframe_joint` purchased-mass role, with its measured mass and nose-tip axial CG.
- Motor mount tube dimensions, kit ring spacing, hook access, motor thrust-block seating and retention. Never modify a
  commercial motor to make it fit.
- Actual launch-lug ID/OD and rod diameter/straightness. Measure effective usable rod travel with the pad/rocket
  mounted; the configured 0.9144 m is provisional.
- Exact payload or secured surrogate: all boards, sensor connectors, antenna, wire bends, battery protection/connector,
  cushioning and ties. Measure the [provisional component specification](AVIONICS_DESIGN.md), including the selected 400
  mAh battery, camera, and antenna. Servos are not part of this configuration.
- Screw pilot compatibility, washer/eye clearance, insulation and service access.
- Chute/line/cord/wadding packing, full nose insertion and repeatable extraction.

## Mass and balance feedback

Weigh each printed part and measure its axial CG relative to the assembled nose tip. The STL print origin is **not**
that coordinate. Optional `printed_measurements` entries are pairs of quantity objects:

```yaml
printed_measurements:
  bay-bulkhead:
    - { value: 4.8, unit: g, provenance: measured, source: "EXAMPLE ONLY — replace with your scale measurement" }
    - { value: 133.5, unit: mm, provenance: measured, source: "EXAMPLE ONLY — assembled nose-origin CG" }
```

The numbers above demonstrate syntax, not measurements. Supported keys are `nose-bay`, `bay-bulkhead`, `payload-sled`,
`fin-collar`, `lug-sleeve-1` and `lug-sleeve-2`. Mass estimates from slicing can use `provenance: estimate`. Geometry
sweeps reject reuse of measured printed masses because changed shapes invalidate them. PLA/PETG changes also require new
masses and physical checks.

Update the nine purchased-mass roles independently, including adhesives, knots, tape and protection. Update payload
mass/CG separately. Weigh and balance the assembled **dry** rocket without a motor for empty, dummy and installed
payload states; compare to `mass-ledger.json`. Resolve discrepancies by finding omitted or mislocated components, not by
disguising unknown mass as zero or arbitrary ballast. There is no assembled-total override that hides an inconsistent
ledger. Then compare launch mass with the intended commercial motor installed under appropriate handling procedures.
Motor mass in the simulation is already added from the curve: do not add it to the dry ledger again.

## Before selecting a motor/delay

Rerun all loading and wind cases with measured inputs. Review guide-departure speed, full-ascent stability (including
speed/angle at the minimum), deployment speed/time/altitude, vertical descent and displacement, and every engine
warning. Review manufacturer liftoff-mass limits separately. The demonstration criteria are engineering assumptions, not
standards or physical safety certification. Apply the actual site's altitude, weather and measured guide, with a
suitable margin; a forecast alone does not establish field conditions.

## Physical gates before any flight

- Inspect prints, fin roots, layer bonds, sleeve joints and all retention.
- Verify load paths and attachment strength with an experienced club/range officer; this package does not supply a
  validated proof-load specification.
- Check nose separation, packed extraction and thermal shielding with suitable commercial procedures. Do not create a
  custom ejection charge for this test.
- Verify launch-guide sliding and pad clearance of the whole assembled rocket.
- Confirm sealed bay isolation, unobstructed radial static ports and pressure response; inspect after recovery. The
  current LPS28 has modeled vents and seal interfaces, but neither sealing nor pressure accuracy is validated; see
  [current avionics](AVIONICS_DESIGN.md).
- Obtain site permission, check current local restrictions/fire conditions and applicable
  [NAR safety guidance](https://www.nar.org/ModelRocketSafetyCode).
- Adult supervision and commercial launch-system instructions govern the outing. A successful software run is never
  permission to bypass these gates.

Record observed flight results later; do not tune assumptions solely until the same simulated case passes. Use new
measured evidence and retain prior runs.
