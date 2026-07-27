# Promotion Decision Registry Governance

## Purpose

Define the append-only registry for adapter promotion, hold, downgrade, and block dossiers.

## Registry rules

- registry entries are created only from schema-valid dossiers;
- active dossier scope fingerprints are unique;
- events are append-only and monotonically sequenced;
- authorization never implies that the adapter registry has already changed;
- every applied registry mutation must reference an authorized dossier and a release record;
- rejected, blocked, cancelled, and superseded dossiers remain queryable;
- adverse evidence and dissenting reviews may not be deleted;
- timestamps, actors, and external evidence are owner-supplied operational data and are not fabricated in the repository baseline.

## Decision scope fingerprint

The fingerprint is SHA-256 over the canonical serialization of:

- adapter ID and exact version;
- current and requested support tier;
- evidence cutoff;
- sorted evaluation job IDs;
- aggregate IDs;
- support policy version;
- promotion-gate version;
- dossier policy version.

## Registry mutation boundary

`adapter_registry_changed` must remain `false` throughout dossier review. A later release action may change the adapter registry only when all of the following exist:

1. authorized dossier;
2. explicit release action ID;
3. before-and-after registry snapshots;
4. rollback instructions;
5. stable-release QA pass;
6. changelog and manifest update.

## Baseline

The canonical baseline registry contains zero dossiers and zero decisions.
