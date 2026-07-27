# Data Quality and Denominator Policy

Each calculation must declare:

- exact included and excluded record identifiers;
- deduplication key and duplicate handling;
- time or version window;
- null, missing, blocked, cancelled, and exception handling;
- denominator before and after exclusions;
- source fingerprints and schema versions;
- rounding and precision rules.

## Prohibited practices

- dropping adverse records without an explicit exclusion reason;
- mixing versions, models, cohorts, or support tiers without stratification;
- carrying forward stale values as current;
- replacing unavailable values with zero or success;
- selecting a denominator after seeing the result;
- publishing a percentage without numerator and denominator.
