# Final Validation

## Release gate

Final validation is the terminal QA gate. It consumes a complete QA package and returns `pass`, `revise`, or `fail`.

## Mandatory checks

- canonical identity lock is present, exact, and unweakened
- identity fidelity score is 100
- anatomy, balance, grip, contact, fabric, and object physics are plausible
- styling fits weather, place, activity, culture, and character continuity
- camera perspective and lens logic protect identity
- lighting, shadows, reflections, and color temperature agree
- the subject is physically integrated with the environment
- one dominant activity and one dominant story beat remain
- every material directive has accepted provenance
- no unresolved contradiction remains
- final prompt, negative constraints, compiler metadata, and QA report are complete

## Decision

- `pass`: all mandatory gates pass and release thresholds are met
- `revise`: defects are repairable and a recovery route is defined
- `fail`: identity, safety, evidence, contradiction, or output-contract failure is unrecoverable

Never release an artifact solely because it is visually attractive.
