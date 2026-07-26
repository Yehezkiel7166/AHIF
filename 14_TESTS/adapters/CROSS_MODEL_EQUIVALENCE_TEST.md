# Cross-Model Semantic Equivalence Test

## Baseline Case

Use the same release-eligible Kyoto cold-morning Final Prompt Package for OpenAI Images v1, Midjourney v1, and SDXL Diffusers v1.

## Assertions

- all adapter results reference the same source package hash;
- identity lock and canonical image reference remain present or execution blocks;
- Gion scene, calm autumn morning, coat decision, natural cold response, activity, and story beat remain traceable;
- negative constraints remain complete;
- unsupported controls produce declared variance rather than silent omission;
- compatibility classification is deterministic;
- no adapter invents a new visual decision.

## Expected Result

`equivalent_with_declared_variance` is acceptable when mandatory semantics are preserved and target-native control differences are disclosed. Pixel-level similarity is outside this test.
