# Photographic Realism Contract

## Scope and authority

This contract owns cross-domain photographic plausibility. Canonical identity remains owned by
`02_CORE_IDENTITY/`: the master photo is the sole identity authority, while pose, wardrobe,
accessories, hairstyle, expression, camera, and framing are mutable context decisions. Generated
images and text are never identity authorities.

The governing principle is **photographically plausible, not maximally decorated**. Positive
directives define the intended capture; negative constraints only bound credible failure risks.

## Required inputs and decisions

Reasoning resolves location, place, time, weather, activity, atmosphere, framing, intended capture,
available light, and environmental interaction. Its auditable handoff contains:

- intended photographic capture;
- human-surface and anatomical realism;
- one lighting model and camera plausibility model;
- environmental integration and controlled imperfections;
- artifact risks, confidence, unresolved uncertainties, compiler directives, and QA flags.

Every material directive has a context basis and `compiler_ready: true`. Unresolved material
uncertainty blocks compilation; it is not guessed by the compiler.

## Invariants

1. Preserve identity geometry, age presentation, recognizability, and other identity invariants.
2. Surface detail is restrained: pores, peach fuzz, fine lines, lip and under-eye texture, tonal
   variation, highlights, hair strands, and flyaways must remain scale- and context-plausible.
3. Anatomy, hands, joints, posture, contact pressure, gravity, balance, and expression tension are
   physically plausible rather than mannequin-perfect.
4. Perspective, exposure, dynamic range, depth, bokeh, sharpening, motion blur, and sensor behavior
   form one coherent capture model.
5. Key, fill, environment, shadow, reflection, skin response, and color temperature agree.
6. Subject and environment share light, atmosphere, scale, edges, contact shadows, and reflections.

## Prohibited over-specification and failure conditions

Do not default to a camera brand, DSLR, 85 mm, f/1.2, cinematic treatment, chromatic aberration,
sensor noise, or shallow depth of field. Use a specific treatment only when reasoning establishes
its relevance. Block non-ready directives, contradictory optics or lighting, keyword stuffing,
unsupported camera parameters, copied master-photo appearance, beautification drift, synthetic
surface instructions, weak compositing, and unsupported empirical claims.

## Compiler, QA, adapter, and empirical boundaries

The compiler serializes and deduplicates accepted semantics in canonical section order; it makes no
visual decision. QA owns identity dominance, anatomy, surface, optics, lighting, environment,
excessive perfection, compiler integrity, and claim checks. Identity failure is non-compensable.

Adapters preserve model-neutral meaning, disclose every lossy or unsupported mapping, and block
identity-critical loss. Semantic preservation is not evidence of image quality. Only externally
supplied generated artifacts can support empirical evaluation; repository conformance, prompt
inspection, or adapter preparation cannot establish empirical success, certification, production
readiness, Release Eligibility, or LTS designation.
