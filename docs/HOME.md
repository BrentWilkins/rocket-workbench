---
hide:
  - navigation
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
        <a class="rw-button" href="docs/BUILD/">Build and hardware</a>
      </div>
    </div>
    <p class="rw-hero__caption">Velocity-colored streamlines from the retained swept-fin OpenFOAM case</p>
  </section>

  <section class="rw-summary" aria-label="Current engineering status">
    <article class="rw-card">
      <p class="rw-card__label">Current platform</p>
      <p class="rw-card__value">D12-5 / BT-60</p>
      <p>Passive clipped-delta configuration with a 500 mm body, removable avionics bay, organic fin-collar v2, and 192/192 simulated D12 cases meeting the earlier bounded screens.</p>
    </article>
    <article class="rw-card">
      <p class="rw-card__label">Stock-pad finding</p>
      <p class="rw-card__value">11.43–11.51 m/s</p>
      <p>The 30-inch rod misses the project’s 12 m/s guide-departure screen across every 30–50 mm nose tested.</p>
    </article>
    <article class="rw-card">
      <p class="rw-card__label">Next physical gate</p>
      <p class="rw-card__value">Measure, fit, verify</p>
      <p>Use a stiffer 36-inch guide, then measure assembled mass, balance, retention, and recovery packing.</p>
    </article>
  </section>

  <section class="rw-copy">
    <div>
      <p class="rw-eyebrow">CURRENT DECISION</p>
      <h2>The small pad can stay. The stock rod should not.</h2>
    </div>
    <div>
      <p>
        The Porta-Pad II base accepts Estes’ 36-inch, 3/16-inch Maxi rod. The current printed lug sleeves assume 1/8-inch paper lugs, so both lugs must be resized or replaced together and checked for free, coaxial travel on the actual rod.
      </p>
      <p>
        The commercial 24 mm motor mount remains bonded inside the paper BT-60 tube; the printed fin collar bonds around the tube and does not retain the motor.
      </p>
      <p class="rw-links">
        <a href="docs/MEASUREMENTS/">Measurement checklist →</a>
        <a href="docs/SHOPPING/">Hardware and sourcing →</a>
        <a href="docs/FIN_COLLAR_V2/">Fin-collar v2 →</a>
        <a href="runs/d12-nose-length-screen-20260916/report/">30–50 mm nose screen →</a>
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

The loop is the development workflow—not automated approval for physical flight. CFD remains exploratory until its
validation gates pass.

[Browse archived and superseded studies](ARCHIVE.md)
