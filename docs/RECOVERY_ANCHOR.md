# Recovery anchor integration — provisional decision

Custom integration is allowed, but no new printed recovery anchor is selected or qualified yet. The current simulations
use an estimated harness budget, not a measured EST3052 anchor or a verified custom-anchor assembly.

## Preferred layout to develop

- **Nose end:** retain the existing through-bolted recovery eye in the printed bay bulkhead, with washers and a locking
  nut. Do not transfer the recovery load to the electronics sled or its board-retention features.
- **Airframe end:** retain a Kevlar leader captured by the motor mount's forward centering ring. Develop a rounded
  routing relief in that assembly if needed, after measuring the commercial mount and ring. This integrates cord
  management without adding an obstruction near the mouth of the body tube.
- **Alternative:** evaluate the Estes 003052 adhesive BT-60 anchor if the measured installation offers better assembly
  access and a clear recovery path. It is an alternative attachment scheme, not an additional required anchor.

The proposed load path remains centering-ring/mount assembly → leader → elastic → recovery eye → bulkhead → nose
retention screws/bosses. Each interface needs inspection and a representative physical test. Integration reduces part
count; it does not remove the need to establish strength or retention.

## Design gates

1. Confirm the commercial 24 mm mount's ring material, thickness, spacing and installed position. Do not replace the
   motor tube, thrust block or retention hardware with an unqualified printed part.
2. Check that the leader routing neither prevents the ring seating nor introduces a sharp edge or a weak narrow section.
   Avoid an exposed printed loop immediately beside the ejection outlet; thermal exposure is unqualified.
3. Keep the 145 mm avionics bay insertion envelope clear. Verify that the anchor, knot and cord do not snag the packed
   chute, wadding, bulkhead eye or nose during separation. Model the occupied space, not just the anchor's nominal size.
4. Account for the chosen anchor and cord assembly once in the measured mass/CG ledger. Reconcile it with the current
   provisional harness and mount allowances before rerunning the selected configuration.
5. Verify representative retention, separation and thermal protection physically before flight. OpenRocket and external
   CFD do not validate the anchor bond, ring strength, printed eye strength or ejection deployment.

For EST3052, the manufacturer identifies injection-molded ABS, pre-applied 3M adhesive and BT-60 compatibility. It does
not establish fit around our long avionics sleeve or the strength of this complete recovery system.
[Estes product information](https://estesrockets.com/products/bt60-shock-cord-anchors)

## Bay-cap fastener sourcing — checked 2026-09-13

### Cap screw stack: provisional, not a released fastener kit

Accu lists an M2 × 6 mm full-thread A2 cap screw, **SSCF-M2-6-A2-R360**, with 0.4 mm pitch, 3.8 mm head diameter, 2 mm
head height, 1.5 mm hex drive and 22 g per 100 screws (0.22 g each). This is a dimensional sourcing reference; stock,
delivered price and its thread-locking coating's suitability for this joint are unconfirmed.
[Supplier specification](https://www.accu.co.uk/metric-cap-head-screws/250399-SSCF-M2-6-A2-R360)

For a flush 3 mm insert behind a 3 mm cap, a nominal 6 mm screw reaches 3 mm past the cap without a washer. Adding a 0.5
mm washer reduces that to 2.5 mm; a 7 mm screw with the same washer reaches 3.5 mm. These are geometric calculations,
not recommended engagement limits. Actual cap thickness, insert seating, thread lead-in and clearance behind the insert
must be checked. Do not substitute a longer screw merely to compensate for a loose joint, and do not assume the sled's
two printed-pilot screws need the same length. The current clearance analysis does not model every fastener head, washer
and driver envelope. Complete joint mass and tool access remain release checks.

The insert manufacturer also has a
[US product listing](https://cnckitchenus.store/products/heat-set-insert-m2-x-3-100-pieces). Verify delivered price and
stock there before ordering; nothing has been purchased.

A local 10-degree placement screen found 21 three-boss patterns clearing the existing conservative sled insertion
projection by at least 0.2 mm, with the recovery eye inside the support triangle. The subsequent full CAD check rejected
all three tested layouts with the original wire/strain-relief routing: clearing the sled alone was insufficient.

A second trial rotates the two 4 × 10 mm routing cross-sections to 10 × 4 mm, above the boards, retaining their volume,
axial positions and mass allowances. With that change, layouts **0/100/260 degrees** and **10/170/270 degrees** clear
the modeled installed and straight-insertion paths. The original 30/150/270-degree pattern still fails. The revised
printed nose/cap adds approximately **0.366 g**, excluding insert, screw and washer changes. All trial printed parts are
valid single CAD solids. Routing bend radius, tool access and physical retention remain unverified.

These are experimental CAD exports, not production selections. Evidence is retained in `runs/cap-boss-screen-20260913`,
`runs/cap-insert-fit-20260913` and `runs/cap-insert-rerouted-fit-20260913`. The production geometry, avionics layout and
sealed flight studies remain unchanged. A separate configured integration is now available for evaluation, below.

### Configured insert integration — local, pending review

The explicit `m2-insert-trial-v1` configuration selects the 10/170/270-degree bosses and matching rerouted wiring
envelopes. Default configurations still use printed pilots. The corrected integration screen in
`runs/sourced24-insert-corrected-20260913` completed all 36 flights, with all 24 planned dummy/logger cases meeting the
configured criteria. Loaded apogee spans approximately 145–187 m across the screened mass and canopy-drag bounds.

The ledger adds an unmeasured 0.7 g nominal / 1.4 g upper insert-joint allowance in addition to the CAD-derived printed
mass change and existing cap hardware. This is an allowance, not a measured bill of materials. The broader uncertainty
rerun in `runs/insert-recovery-wide-20260913` completed 288 flights: all 192 planned dummy/logger cases pass, with 96
empty diagnostic cases retained separately. Loaded altitude spans 144.64–186.62 m, powered speed 50.33–60.29 m/s,
descent 3.45–5.24 m/s and landing displacement 0.04–163.02 m. Upper avionics, chute and joint mass are paired; scenario
counts are not reliability probabilities. See the
[integrated uncertainty report](../runs/insert-wide-summary-20260913/report.md).

The earlier `runs/sourced24-insert-integration-20260913` is retained but not a release source: its CAD used the revised
routing while exported component metadata still described the old routing. The fresh corrected run exports the
configured component layout, with a regression test checking metadata against that layout. Physical fit, installation,
thread engagement, service access and recovery-load strength remain unverified.

The current CAD uses three M2 screws in 1.6 mm printed pilots, not threaded inserts. The cap is 3 mm thick; the
avionics-profile bosses are 8 mm long with nominal 4.4 mm diameter, clipped at the sleeve boundary. These joints carry
recovery load as well as retaining the cap. Repeated service and pull-out strength remain untested.

A specific insert candidate is CNC Kitchen **TC-M2x3.0**, brass M2, 3 mm long, sold in packs of 100. The manufacturer
lists €9.90 per pack before shipping; availability and delivered US price are not confirmed.
[Product page](https://cnckitchen.store/products/heat-set-insert-m2-x-3-100-pieces)

Its manufacturer drawing specifies a 3.6 mm insert diameter, 3.2 mm receiving hole, 1.3 mm minimum wall and at least 4
mm blind-hole depth. Therefore it is **not a drop-in upgrade** to the current boss. Even an unclipped 4.4 mm boss leaves
only 0.6 mm around a 3.2 mm hole, below that guideline. The drawing also provides a basis for installation geometry, not
a rocket recovery-load rating.
[Manufacturer dimensions and design guidelines](https://cdn.shopify.com/s/files/1/0654/4821/4767/files/Poster_Dimensions-Guidlines.pdf?v=1751444185)

For comparison, Lawson's M2-0.4 A2 stainless full nut (27763) is 4 mm across flats and 1.6 mm thick. A regular hexagon
of that width is approximately 4.62 mm across corners, already wider than the nominal boss before adding pocket
clearance or retaining walls. A captive-nut revision also needs new CAD; simply changing the hole is insufficient.
[Supplier specification](https://www.lawsonproducts.com/en-ca/products/hex-nut-grade-a2-stainless-steel-m2-0-4-27763)

**Development decision:** compare enlarged, inward-relocated insert bosses with mechanically captured nuts before
selecting cap hardware. Preserve the outer tube fit and check the antenna, board, cable, sled and seal envelopes. For an
insert trial, use a conservative 6.2 mm nominal boss diameter (3.6 + 2 × 1.3 mm), then verify actual minimum wall after
unions and clipping. This is a proposed test geometry, not a released part or a strength claim. Screw length must follow
the final cap/washer/engagement stack, not the current pilot depth alone.

No insert, nut or screw mass has been silently substituted into the sealed flight studies. Once the joint is selected,
update the hardware ledger and printed mass/CG, rerun the affected cases, and inspect a representative retention test
before flight. Manufacturer STEP/STL insert models are available from the
[download page](https://cnckitchen.store/pages/insert-cad-models); downloading a model is not proof of installed fit.
