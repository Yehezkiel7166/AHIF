# Adapter Promotion Regression

## Baseline

All existing target adapters begin this sprint at `contract_validated_experimental`.

## Regression assertions

- no adapter is promoted without accepted external evidence;
- no evidence fixture is presented as an actual model execution;
- identity failures override aggregate semantic scores;
- missing target-version metadata is disclosed;
- target-native variance cannot excuse identity drift;
- one successful output cannot establish stable support;
- downgrade decisions preserve prior evidence history;
- stable 2.0 adapter contracts remain backward compatible.

## Expected repository state

At release 2.1.0, support tiers remain unchanged until users add valid evidence bundles and complete independent review.
