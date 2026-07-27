# AHIF Quick Context

Use the uploaded master photo as the sole canonical identity.

Priority:
1. identity
2. anatomy
3. realism
4. cultural respect
5. explicit user request
6. story
7. fashion
8. visual style

When given location, place, and atmosphere, infer:
- weather and season
- practical outfit
- hairstyle and accessories
- makeup
- activity
- pose and body language
- expression
- environment interaction
- camera, lens, composition
- lighting and color
- one believable story beat

Never redesign the face, replace the person, average the identity, or let style override recognizability. Maintain natural hands, body balance, fabric physics, weather response, shadows, and location scale.

## Character

The subject is curious, composed, confident, culturally respectful, and visually refined without appearing theatrical. She prefers authentic travel moments.

## Styling

Style derives from location, climate, time, activity, culture, and character. Function comes before decoration. Avoid accessory overload.

## Photography

Use a lens and composition that support the story and preserve identity. Environmental portraits should reveal place without making the subject look pasted into it.

## QA

Reject identity drift, anatomy errors, impossible hands, contradictory weather, fake compositing, inappropriate cultural behavior, and excessive retouching.

## Decision engine

Resolve choices in this order: identity, anatomy, culture, explicit request, environment, activity, continuity, story, fashion, style. Infer missing information conservatively. Detect contradictions before compiling.


## Sprint 019 Adapter Release Observation Rule

Treat post-release observation as a separate governed process. Only completed and signed release records may enter O0–O9. Pin the exact release, package, snapshots, observation window, signal sources, thresholds, and roles. Observation may verify repository conformance and rollback reconstructability, but it must not fabricate telemetry, certify production health, create empirical evidence, mutate adapter tiers, or execute rollback. The AHIF 2.7.0 baseline contains zero observation records.

## Sprint 020 Adapter Incident Response Rule

Treat incident handling as a separate governed process after release observation. Require pinned release and observation provenance, immutable incident scope, bounded severity, reversible containment, independent authorization, recovery validation, append-only events, residual-risk disclosure, and closure signoff. Never fabricate telemetry or actors, execute rollback or deployment, mutate adapter tiers or canonical identity authority, or certify production health. The AHIF 2.8.0 baseline contains zero incident records.

