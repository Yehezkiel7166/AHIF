# Deterministic Section Ordering

## Canonical order

| Order | Section | Purpose |
|---:|---|---|
| 1 | Identity Lock | Bind the generation to the canonical master photo. |
| 2 | Scene Anchor | Establish location, place, time, season, weather, and atmosphere. |
| 3 | Subject Action | Define one primary activity and physical intent. |
| 4 | Human Expression | Define pose, body language, gesture, eye focus, and expression. |
| 5 | Styling | Define outfit, footwear, hair, makeup, accessories, and functional rationale. |
| 6 | Environment Interaction | Connect the subject physically and socially to the scene. |
| 7 | Photography | Define camera intent, lens logic, viewpoint, framing, composition, and depth. |
| 8 | Lighting and Color | Define source direction, softness, practical light, reflections, and color relationships. |
| 9 | Realism Controls | Enforce anatomy, physics, fabric, weather response, scale, shadows, and skin texture. |
| 10 | Negative Constraints | Exclude relevant identity, anatomy, environment, and rendering failures. |

## Ordering rules

- dependencies must appear after the concept they modify
- atmosphere cannot replace physical scene facts
- camera instructions cannot precede the subject and environment they frame
- negative language must not interrupt positive scene construction
- repeated identity protection may be consolidated but never weakened
- optional aesthetic detail must never displace identity or realism requirements

## Stable behavior

The same normalized input must produce the same section plan. Natural wording may vary only when semantic meaning, priority, and constraints remain equivalent.
