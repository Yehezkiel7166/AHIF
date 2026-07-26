# Reasoning Contract Test

## Required assertions

1. Every accepted major decision references at least one premise.
2. Every premise has a declared evidence type and source.
3. Identity-sensitive decisions reference identity constraints.
4. Rejected alternatives use the canonical rejection vocabulary.
5. Aggregate confidence follows the propagation policy.
6. Identity confidence below `0.85` blocks compilation.
7. A compiler directive cannot introduce an unreasoned material detail.
8. The same normalized input produces materially equivalent reasoning.
9. Missing information remains explicit and is never fabricated.
10. The final status matches QA findings.
