# Multi-Model Compatibility Contract

## Purpose

This contract defines how AHIF determines whether different target-model adapters preserve the same canonical visual intent. Compatibility is semantic and identity-first; identical wording, parameter names, or rendering behavior are not required.

## Contract Inputs

A compatibility evaluation consumes:

- one release-eligible Final Prompt Package;
- two or more exact adapter versions;
- immutable capability-profile identifiers;
- deterministic adapter results;
- declared losses, fallbacks, and blocks;
- the canonical identity binding and source package hash.

## Required Invariants

Every non-blocked adapter result must preserve:

1. canonical subject identity and reference binding;
2. apparent age, ethnicity, recognizability, and facial-geometry constraints;
3. primary location, activity, and story beat;
4. human plausibility and anatomy constraints;
5. required outfit and weather-response decisions;
6. camera and lighting intent at the supported semantic level;
7. mandatory negative constraints;
8. provenance from the same Final Prompt Package.

## Compatibility Classes

- `equivalent`: all mandatory semantics and declared quality semantics are preserved.
- `equivalent_with_declared_variance`: mandatory semantics are preserved; model-native rendering variance is expected and documented.
- `degraded`: mandatory identity semantics are preserved, but one or more non-identity required semantics use an approved fallback.
- `incompatible`: a mandatory semantic cannot be represented safely.
- `blocked`: execution is prohibited because identity, safety, provenance, or contract validation fails.

## Comparison Rule

Compatibility is evaluated against the canonical package, never by treating one model output as the reference for another. Pairwise comparison is supplemental and cannot override canonical-package findings.

## Release Rule

A target family may not be promoted beyond `experimental` unless its adapter passes the compatibility matrix, interoperability regression, and identity-preservation floor defined by Sprint 009.
