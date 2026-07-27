# Semantic Evaluation Protocol

## Goal

Determine whether the generated output preserves the accepted meaning of the released Final Prompt Package after target adaptation.

## Evaluation domains

- location and place;
- atmosphere and weather;
- fashion and accessories;
- hair and makeup;
- pose, gesture, and expression;
- activity and environment interaction;
- camera, lens, and composition;
- lighting and color;
- story intent;
- negative constraints.

## Variance handling

Target-native visual variation is acceptable only when it remains inside the compatibility tolerance declared for that domain.

## Failure classes

- omission;
- contradiction;
- unsupported addition;
- severity amplification;
- identity-risk introduction;
- composition displacement;
- target-native rendering variance.

## Blocking conditions

Release evidence is blocked when a material identity constraint is omitted, a forbidden element appears, the requested location or activity is contradicted, or adapter loss was not disclosed.

## Output

The protocol emits a Semantic Evaluation Report with domain-level findings, accepted variances, failures, confidence, and release recommendation.
