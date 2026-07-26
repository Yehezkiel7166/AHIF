# Execution Orchestration

## Execution stages

| Stage | Input | Required output | Blocking condition |
|---|---|---|---|
| F0 Intake | compact request | normalized execution request | missing location, place, or atmosphere when not inferable |
| F1 Context | execution request | normalized context | incompatible or unsafe context |
| F2 Decision | normalized context and knowledge graph | accepted decision set | unresolved identity conflict |
| F3 Reasoning | decision set and evidence | compiler-ready reasoning record | weak causal support or identity confidence below floor |
| F4 Compile | reasoning record | compiled prompt package | contradiction, missing mandatory section, invented directive |
| F5 Validate | compiled package | QA report | mandatory gate failure |
| F6 Recover | failed stage and report | corrected upstream artifact | recovery budget exhausted |
| F7 Release | validated package | final prompt package | release eligibility is false |

## Deterministic orchestration

Execution follows the stage order above. A later stage cannot repair an upstream semantic decision by rewriting it locally. Corrections must return to the earliest responsible stage.

## Recovery budget

A single execution permits:

- up to two non-identity correction cycles;
- one identity correction cycle;
- zero automatic overrides of critical identity failure;
- zero silent deletion of required user constraints.

When the budget is exhausted, the engine returns a blocked result with explicit failure codes and required human input.

## Idempotence

Given the same canonical identity reference, normalized input, framework version, and model-neutral profile, the engine must produce the same decision order, reasoning trace structure, prompt section order, validation outcome, and release metadata.
