# Rocket Workbench

Reproducible model-rocket geometry, CAD exports, OpenRocket simulations, and design comparisons.

**Simulation evidence only: provisional hardware inputs, no physical validation or flight approval.**

Use the navigation to read the review, inspect plots, or follow the build and measurement guides.

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
