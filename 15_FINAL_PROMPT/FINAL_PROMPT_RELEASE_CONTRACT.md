# Final Prompt Release Contract

## Required release artifacts

Every successful execution returns:

1. `final_prompt` — the complete model-neutral prompt;
2. `negative_constraints` — risk-derived exclusions;
3. `identity_binding` — canonical reference and identity-lock status;
4. `execution_summary` — compact explanation of selected decisions;
5. `validation_summary` — QA outcome and release eligibility;
6. `provenance` — framework version, contracts, and trace identifiers.

## Final prompt properties

The final prompt must be:

- identity-preserving;
- internally coherent;
- context-complete;
- physically plausible;
- culturally respectful;
- deterministic in section order;
- free from unsupported identity attributes;
- model-neutral until an adapter is applied;
- concise enough to avoid semantic dilution while complete enough to preserve intent.

## Blocked result

A blocked result must contain:

- `release_eligible: false`;
- the earliest failing stage;
- stable failure codes;
- unresolved constraints;
- the required recovery action;
- no final prompt presented as production-ready.
