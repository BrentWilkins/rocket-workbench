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
    <p class="rw-card__value">D12-5 / E12-6 · BT-60</p>
    <p>500 mm body, integrated fin collar, removable camera/logger bay. The raw collar print weighs 27 g.</p>
  </article>
  <article class="rw-card">
    <p class="rw-card__label">Launch guide</p>
    <p class="rw-card__value">3/16-inch Maxi rod</p>
    <p>Matching rocket guides still need to be built and checked on the actual rod.</p>
  </article>
  <article class="rw-card">
    <p class="rw-card__label">Flight-model status</p>
    <p class="rw-card__value">Provisional</p>
    <p>Both motors pass the current numerical screen, but finished mass, CG and recovery must be verified.</p>
  </article>
</section>

<section class="rw-copy">
  <div>
    <p class="rw-eyebrow">CURRENT BUILD</p>
    <h2>The printed collar is real; the assembled rocket is not yet measured.</h2>
  </div>
  <div>
    <p>The next gates are a dry fit of the two-tube airframe and coupler, a 3/16-inch guide interface, recovery packing and extraction, then measured mass and CG in a fresh D12-5/E12-6 simulation.</p>
    <p class="rw-links">
      <a href="docs/CURRENT_DESIGN/">Current configuration →</a>
      <a href="docs/MEASUREMENTS/">Measurement checklist →</a>
      <a href="docs/SHOPPING/">Hardware sourcing →</a>
      <a href="docs/INTEGRATED_FIN_COLLAR/">Fin collar →</a>
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
