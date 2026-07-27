# Adapter Incident Registry Regression

Baseline assertions:

1. Registry exists and parses as JSON.
2. `append_only` is `true`.
3. Incident count is zero.
4. Executed recovery count is zero.
5. Executed rollback count is zero.
6. Adapter tier changes are zero.
7. Production health certifications are zero.
8. No existing release, observation, promotion, evaluation, or evidence record is mutated.
