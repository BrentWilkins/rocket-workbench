---
hide:
  - toc
  - path
---

<div class="rw-home">
  <section class="rw-hero" aria-labelledby="rw-hero-title">
    <img
      class="rw-hero__image"
      src="docs/assets/cfd/swept-fin-desktop-hero.webp"
      alt="Swept-fin rocket surrounded by velocity-colored OpenFOAM streamlines"
      width="2560"
      height="1120"
      fetchpriority="high"
    >
    <div class="rw-hero__shade" aria-hidden="true"></div>
    <div class="rw-hero__content">
      <p class="rw-eyebrow">MODEL ROCKET DEVELOPMENT / REPRODUCIBLE EVIDENCE</p>
      <h1 id="rw-hero-title">Rocket Workbench</h1>
      <p class="rw-hero__lede">
        Parametric CAD, OpenRocket flight studies, and bounded CFD—kept together so every design decision can be inspected and reproduced.
      </p>
      <div class="rw-chips" aria-label="Project status">
        <span class="rw-chip rw-chip--warning">Not flight-cleared</span>
        <span class="rw-chip">D12-5 / BT-60</span>
        <span class="rw-chip">OpenRocket 24.12</span>
        <span class="rw-chip">OpenFOAM v2512</span>
      </div>
      <div class="rw-actions">
        <a class="rw-button rw-button--primary" href="docs/CURRENT_DESIGN/">Current design</a>
        <a class="rw-button" href="docs/BUILD/">Build hardware</a>
      </div>
    </div>
    <p class="rw-hero__caption">Velocity-colored streamlines from the retained swept-fin OpenFOAM case</p>
  </section>

  <section class="rw-summary" aria-label="Current engineering status">
    <article class="rw-card">
      <p class="rw-card__label">Current platform</p>
      <p class="rw-card__value">D12-5 / BT-60</p>
      <p>Passive clipped-delta configuration, 500 mm body, removable avionics bay, and organic fin-collar v2.</p>
    </article>
    <article class="rw-card">
      <p class="rw-card__label">Selected launch guide</p>
      <p class="rw-card__value">36 × 3/16 inches</p>
      <p>Estes’ two-piece <a href="https://estesrockets.com/products/3-16-two-piece-maxi-launch-rod">Maxi rod</a> fits the existing <a href="https://estesrockets.com/products/porta-pad-ii-launch-pad">Porta-Pad II</a> and provides a longer, stiffer guide.</p>
    </article>
    <article class="rw-card">
      <p class="rw-card__label">Modeled guide departure</p>
      <p class="rw-card__value">12.91–12.92 m/s</p>
      <p>The current loaded cases clear the project’s 12 m/s screen on the 36-inch guide.</p>
    </article>
  </section>

  <section class="rw-copy">
    <div>
      <p class="rw-eyebrow">CURRENT LAUNCH SETUP</p>
      <h2>The pad stays. The guide gets longer and stiffer.</h2>
    </div>
    <div>
      <p>
        The stock 1/8-inch rod lifts out of the Porta-Pad II and the two-piece 3/16-inch Maxi rod installs in the same pad. Two aligned launch lugs keep the rocket pointed on the selected path while the D12 builds enough airspeed for the fins to take over.
      </p>
      <p>
        The current simulation predicts 12.91–12.92 m/s at guide departure. That is a useful modeled margin, not flight clearance: the printed lug sleeves still need to be resized from 1/8 inch, and the assembled rocket must slide freely over the straight, clean rod with both lugs coaxial. Actual usable guide travel, loaded mass, balance, wind, and pad setup remain physical checks.
      </p>
      <p class="rw-links">
        <a href="docs/CURRENT_DESIGN/">Current configuration →</a>
        <a href="docs/MEASUREMENTS/">Measurement checklist →</a>
        <a href="docs/SHOPPING/">Hardware sourcing →</a>
        <a href="docs/FIN_COLLAR_V2/">Fin-collar v2 →</a>
      </p>
    </div>
  </section>
</div>

## Evidence loop

```mermaid
flowchart TD
    Inputs[Geometry + provisional hardware inputs] --> Config[Validated configuration]
    Config --> CAD[CAD parts + mass ledger]
    CAD --> Model[OpenRocket flight model]
    Model --> Cases[Motor, payload + wind cases]
    Cases --> Criteria[Metrics + feasibility criteria]
    Criteria --> Shortlist[Shortlist + tradeoffs]
    Shortlist --> Review[As-built measurements + human review]
    Review --> Config
```

This loop is a development workflow—not automated approval for physical flight. CFD remains exploratory until its
validation gates pass.

[Browse archived and superseded studies](ARCHIVE.md)
