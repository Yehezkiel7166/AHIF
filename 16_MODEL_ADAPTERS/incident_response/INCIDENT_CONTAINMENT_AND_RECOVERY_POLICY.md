# Incident Containment and Recovery Policy

## Containment principles

Containment must be minimal, reversible, scope-pinned, and independently authorized. Every action requires an owner, exact mutation set, expected effect, rollback instruction, expiry condition, and verification step.

## Recovery paths

1. **Restore from snapshot** — restores the signed pre-change state.
2. **Authorized rollback** — uses the exact rollback package attached to the release record.
3. **Forward fix** — creates a new release candidate and re-enters release governance; it is not an in-place undocumented repair.
4. **Profile hold** — blocks new promotion or release activity while preserving registry history.
5. **No action** — allowed only when validation demonstrates no declared contract defect.

## Prohibited shortcuts

- editing canonical files without a release or recovery record;
- replacing a signed package after authorization;
- changing severity to avoid approval requirements;
- using observation notes as empirical evidence;
- closing an incident without residual-risk and follow-up declarations.

## Recovery completion gate

Recovery is complete only when repository conformance, package fingerprints, compatibility contracts, QA gates, snapshot comparison, and documentation reconciliation all pass or are explicitly recorded as blocked.
