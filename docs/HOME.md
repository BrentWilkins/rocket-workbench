# Rocket Workbench

Reproducible model-rocket geometry, CAD exports, OpenRocket simulations, and design comparisons.

**Simulation evidence only: provisional hardware inputs, no physical validation or flight approval.**

Start with [current avionics designs and downloads](CURRENT_DESIGN.md): corrected hardware-specific simulations,
performance tradeoffs, stress limits, CAD and the V5 X1C project. The [original MVP review](REVIEW.md) is historical.

```mermaid
flowchart TD
    Inputs[Geometry and provisional hardware inputs] --> Config[Validated configuration]
    Config --> CAD[CAD parts and mass ledger]
    CAD --> Model[OpenRocket flight model]
    Model --> Cases[Motor, payload, and wind cases]
    Cases --> Criteria[Metrics and feasibility criteria]
    Criteria --> Shortlist[Shortlist and tradeoffs]
    Shortlist --> Review[Human review and as-built measurements]
    Review --> Config
```

The loop represents the development workflow, not automated approval for physical flight.
