# Adapter Promotion Gate

## Support tiers

- `contract_validated_experimental`
- `empirically_validated_preview`
- `empirically_validated_stable`
- `production_certified`
- `blocked`

## Minimum promotion evidence

### Empirically validated preview

- accepted evidence for all mandatory baseline scenarios;
- no critical identity failures;
- reproducibility level at least R3;
- independent evaluator agreement;
- complete loss disclosure.

### Empirically validated stable

- preview requirements;
- expanded scenario coverage;
- no unresolved high-severity semantic failures;
- repeated evidence across at least two execution dates;
- compatibility regression acceptance.

### Production certified

- stable requirements;
- R4 repeated identity evidence;
- operational support policy;
- target-version monitoring;
- documented rollback and deprecation path.

## Downgrade triggers

A target is downgraded when:

- a target update invalidates its capability profile;
- identity failure exceeds the accepted threshold;
- request serialization changes without conformance review;
- evidence integrity is compromised;
- a blocking regression remains unresolved.

## Decision authority

Promotion and downgrade decisions are recorded as versioned release evidence. No adapter may self-promote based on one successful output.


## Sprint 017 dossier boundary

Promotion-gate outputs must enter `ADAPTER_PROMOTION_DECISION_DOSSIER.md` before any support-tier decision is authorized. The dossier preserves exact evidence scope, adverse findings, independent reviews, and authorization. An authorized dossier is not a registry mutation; application requires a separate governed release action.
