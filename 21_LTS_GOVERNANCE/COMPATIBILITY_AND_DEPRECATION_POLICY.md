# LTS Compatibility and Deprecation Policy

## Compatibility baseline

AHIF 3.x retains the canonical identity authority, identity-first pipeline, 2.x stable framework contracts, adapter contracts, evidence separation, append-only governance records, and every established claim boundary. Existing valid 2.x artifacts remain interpretable unless a versioned migration rule explicitly says otherwise.

## Prohibited silent changes

An LTS maintenance change must not silently:

- weaken identity invariants or replace the master photo as canonical authority;
- reinterpret required schema fields or stable identifiers;
- remove supported modules, adapters, tests, or registry history;
- change adapter support tiers;
- convert `not-evaluated`, unknown, blocked, or missing evidence into pass;
- inflate repository validation into empirical or production certification.

## Deprecation

Deprecation requires a stable identifier, affected surface, rationale, replacement, migration path, announcement version, minimum compatibility window, owner, review date, and removal major version. Deprecation is non-breaking until the declared removal major version. Removal without this record is blocked.

## Compatibility decision

If compatibility cannot be verified, the LTS decision is `hold`. A major version permits deliberate contract evolution, but it does not erase historical compatibility obligations or evidence boundaries.
