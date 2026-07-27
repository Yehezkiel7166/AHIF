# Evidence Aggregation QA

## Gates

- **AGG-01** schema validity;
- **AGG-02** all source bundles exist and are eligible;
- **AGG-03** source bundle identifiers are unique;
- **AGG-04** cohort boundaries are explicit;
- **AGG-05** confidence calculation is reproducible;
- **AGG-06** critical identity failures block recommendation approval;
- **AGG-07** outliers and drift findings are retained;
- **AGG-08** claim boundary is present;
- **AGG-09** recommendation requires human approval;
- **AGG-10** provenance graph is complete.

## Failure codes

`AHIF-AGG-001` through `AHIF-AGG-010` correspond to the gates above. Any failure in AGG-02, AGG-05, AGG-06, or AGG-10 is release-blocking.
