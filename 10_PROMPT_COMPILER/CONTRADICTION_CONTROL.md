# Contradiction Control

## Contradiction classes

- **identity** — canonical identity versus redesign, replacement, age shift, or ethnicity drift
- **scene** — incompatible location, time, season, weather, or architecture
- **activity** — mutually exclusive dominant actions
- **human** — pose, balance, gesture, expression, or object-use conflict
- **styling** — climate, activity, cultural, or continuity mismatch
- **photography** — incompatible viewpoint, lens behavior, framing, focus, or motion treatment
- **lighting** — conflicting source direction, time cues, shadow behavior, or color temperature
- **story** — multiple dominant narrative beats
- **constraints** — required and prohibited instructions targeting the same visual property

## Gate behavior

1. detect conflicts before natural-language rendering
2. map each conflict to its source directives
3. apply the repository priority hierarchy
4. auto-resolve only when one directive is explicitly subordinate and no identity or user constraint is affected
5. otherwise return `revision-required`
6. return `blocked` for identity replacement, unsupported canonical identity claims, or invalid source status

## Required diagnostic

```yaml
code: compiler-contradiction
class: lighting
units: [C-014, C-021]
resolution: revision-required
reason: "Direct noon sunlight conflicts with diffuse overcast illumination."
```

The compiler must never hide a contradiction through vague wording.
