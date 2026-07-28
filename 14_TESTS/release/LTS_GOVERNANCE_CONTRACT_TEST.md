# LTS Governance Contract Test

## Assertions

1. LTS0–LTS9 stages exist in order.
2. Missing required evidence produces `hold`, never `designated`.
3. Repository, governance, operational, and empirical evidence remain distinct.
4. All prior compatibility guarantees and identity invariants are retained.
5. Breaking changes are prohibited on an existing LTS line.
6. Backports require origin, scope, compatibility review, tests, approval, rollback, and an append-only event.
7. Deprecation requires replacement, migration, a compatibility window, and a removal major version.
8. Empty registries do not imply maintenance success or support readiness.
9. Maintenance events are ordered and digest-linked.
10. LTS designation cannot mutate adapter tiers or empirical status.
11. Repository validation cannot assert adoption, SLA achievement, deployment, production health, or operational support.
12. Release metadata changes only after all required repository validation passes.
