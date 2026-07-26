# Model-Specific Adapter QA

## Mandatory Gates

1. Exact adapter and profile resolution.
2. Source Final Prompt release eligibility.
3. Canonical identity reference retention.
4. Semantic section coverage.
5. Parameter allowlist compliance.
6. Negative constraint coverage.
7. Loss disclosure completeness.
8. Deterministic serialization.
9. Target request schema validity.
10. Experimental-status disclosure.

## Release Decision

Sprint 008 adapters may return executable experimental requests, but they cannot be labeled production-equivalent. Any identity-critical degradation returns `blocked`; semantic-required degradation returns `revise`; quality-optional loss may return `pass_with_disclosure`.
