---
hide:
  - toc
  - path
---

<div class="rw-home">
  <section class="rw-hero" aria-labelledby="rw-hero-title">
    <img
      class="rw-hero__image"
      src="docs/assets/500-ogive-review/500-ogive-streamlines.png"
      alt="500 mm ogive candidate surrounded by computed OpenFOAM streamlines"
      width="3200"
      height="1100"
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
  <p class="rw-hero__caption">500 mm ogive comparison candidate · exploratory CFD · guides and ports omitted</p>
  </section>

<section class="rw-summary" aria-label="Current engineering status">
  <article class="rw-card">
    <p class="rw-card__label">Current platform</p>
    <p class="rw-card__value">D12-5 / E12-6 · BT-60</p>
    <p>Recommended: 530 mm body, 40 mm ogive, existing 27 g fin collar and camera/logger payload. Not yet an as-built configuration.</p>
  </article>
  <article class="rw-card">
    <p class="rw-card__label">Launch guide</p>
    <p class="rw-card__value">Longer usable guide</p>
    <p>The 36-inch cases miss our 12 m/s departure screen. A 60-inch guide improves exit speed; diameter, stiffness, fit and friction still need checking.</p>
  </article>
  <article class="rw-card">
    <p class="rw-card__label">Flight-model status</p>
    <p class="rw-card__value">12,120 flights studied</p>
    <p>More stability margin for little altitude cost—not an all-pass result. Windy, heavier cases still exceed the deployment-speed screen.</p>
  </article>
</section>

<section class="rw-copy">
  <div>
    <p class="rw-eyebrow">LATEST RESULTS</p>
    <h2>Keep the collar. Buy margin with length. Verify launch and recovery.</h2>
  </div>
  <div>
    <p>The 530 mm ogive gains about 0.16 caliber on D12 and 0.14 on E12, costing only 2.35 m and 4.02 m of altitude versus the 500 mm ogive. Better wind handling is not established. Next: measured mass/CG, a compatible longer guide, and recovery verification.</p>
    <p class="rw-links">
      <a href="docs/FLIGHT_ROBUSTNESS/">Final robustness report →</a>
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
