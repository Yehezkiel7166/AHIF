# Metric Registry Regression

Validate on every release:

- all three metric registry JSON files parse;
- registry arrays never lose or rewrite accepted entries;
- declared counts equal actual array lengths;
- every snapshot references a known specification version;
- event hash chains remain ordered when events exist;
- empty baselines remain explicit and do not imply passing quality;
- dashboard entries reference immutable snapshot identifiers;
- no registry field asserts unsupported telemetry or KPI achievement.
