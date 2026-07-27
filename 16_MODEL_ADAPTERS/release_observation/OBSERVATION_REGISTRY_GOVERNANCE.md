# Release Observation Registry Governance

## Purpose

Maintain an append-only index of post-release observation plans, evaluated outcomes, rollback-assurance results, and response authorizations.

## Registry properties

- zero or more observation records;
- unique `observation_id` and `observation_scope_fingerprint`;
- immutable release, package, snapshot, and governed-version references;
- append-only events ordered by sequence;
- explicit observation window, signal inventory, outcome, and response state;
- no deletion or rewriting of healthy, watch, contain, blocked, cancelled, or rollback-recommended history.

## Duplicate control

Only one active observation may own the same completed release fingerprint and observation window. A duplicate must be cancelled with `AHIF-OBS-012`.

## Claim boundary

A healthy repository-level observation does not prove production quality, model-output quality, or empirical support. Such claims require accepted external evidence through the existing evidence pipeline.

## Baseline

`registry/RELEASE_OBSERVATION_REGISTRY.json` intentionally contains zero records in AHIF 2.7.0.
