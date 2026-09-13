# Current avionics designs and comparison

**Current development shortlist:** D12-5 in BT-60, 50 mm conical nose and small clipped-delta fins, with either a 460 mm
body / provisional 22-inch chute or a 500 mm body / literature-characterized Apogee 24-inch chute. Both pass **192/192
planned dummy/logger cases** in the completed expanded recovery study (Cd 0.53–1.04, including an upper chute-mass
allowance). This is a bounded comparison, not physical validation or a global optimum.

| Recovery / body                        | Loaded altitude m | Powered speed m/s | Descent m/s | Landing displacement m |
| -------------------------------------- | ----------------- | ----------------- | ----------- | ---------------------- |
| Generic 22 inch / 460 mm               | 145.12–187.64     | 50.40–60.36       | 3.76–5.72   | 0.04–145.07            |
| Sourced 24 inch / 500 mm               | 146.40–187.74     | 50.78–60.61       | 3.44–5.22   | 0.04–165.24            |
| Sourced 24 inch / 500 mm, insert joint | 144.64–186.62     | 50.33–60.29       | 3.45–5.24   | 0.04–163.02            |

The 24-inch option offers more modeled descent margin and a specific sourced canopy, with more drift and a longer body.
The small speed/altitude differences do not establish a decisive aerodynamic advantage. Its nominal mass is from a
published specimen, not our delivered hardware; packing is still provisional. The third row is the integrated review
candidate, including the revised printed bosses and provisional insert-joint mass. It also passes 192/192 planned cases.
Relative to the same canopy/body with printed pilots, its worst-case loaded altitude is 1.76 m lower and its worst-case
descent speed 0.02 m/s higher. This small modeled penalty buys a candidate serviceable joint, not proven strength. The
22-inch option has not received this insert integration, so do not interpret all differences as canopy effects alone.

The earlier 20-inch/430 mm leader passes only **156/192** expanded cases, with 36 descent-speed failures. Its historical
192/192 result applies only to the narrower Cd 0.6–0.9 study.

See the [fin, recovery and uncertainty comparison](FIN_SHAPES.md) for the 22-/24-inch recovery tradeoffs, failed designs
and actual study bounds. CFD has not been accepted, hardware mass/packing remain provisional, and recovery attachment
strength still requires physical checks. The separate D12 review project is described below.

**New comparison:** [24 mm motors in BT-60](MOTOR24.md) provides substantially more predicted altitude and payload
margin. Earlier 18 mm downloads are now confined to the archived review linked at the end of this page.

## D12 review files

[Download the integrated D12 review files](assets/d12-insert-review-20260913.zip) (about 2.5 MB): matching six-part X1C
project, CAD STEP/STL, OpenRocket files, configuration, nominal results, mass ledger and CAD renders. The archive has a
per-file hash manifest and does not contain a flight-clearance claim. Its SHA256 is
`529311affebab0e997b92dac64bc360a5256d2e01cc4d93533e5d7788530a77a`.

The newer insert-bay review project is `deliverables/d12-bt60-insert-review-20260913/D12-BT60-insert-X1C-review.3mf`. It
uses the corrected explicit insert configuration, enlarged relocated bosses and matching wire-routing envelopes. Its
completed uncertainty rerun passes 192/192 planned cases, with loaded altitude 144.64–186.62 m and descent 3.45–5.24
m/s. See [joint integration and limits](RECOVERY_ANCHOR.md). Insert/screw mass remains an allowance; physical strength
is unverified. This is a separate review file, not an overwrite of the earlier project below.

Local D12 inspection update: an unsliced six-part X1C project has been generated separately at
`deliverables/d12-bt60-sourced24-inspection-20260913/D12-BT60-sourced24-X1C-inspection.3mf`. It uses the sourced 24-inch
/ 500 mm study geometry and the unchanged production cap, not the experimental insert layout. The native archive and
transformed placement checks pass, and a local slice generates toolpaths for all six parts. The slicer estimates about 3
h 40 min and 95.48 g of PLA including supports/adhesion material; these are not measured print values or installed
flight mass. Local CLI preset-lookup warnings remain in the retained log, although the output still identifies X1C, 0.4
mm, Textured PEI and PLA. Review toolpaths/settings in Bambu Studio before any print. No printer command was sent. Final
hardware integration and print release remain pending.

## Earlier 18 mm work

The older C5-3 comparisons, historical altitude gates and V5 print downloads are retained in the
[archived 18 mm review](REVIEW_18MM.md). They are not the current D12 design or purchase guidance.
