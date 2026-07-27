# Empirical Evidence QA

## Mandatory gates

| Gate | Requirement | Blocking |
|---|---|---|
| EV-QA-01 | Canonical identity checksum present | Yes |
| EV-QA-02 | Final Prompt Package checksum present | Yes |
| EV-QA-03 | Exact adapter and profile versions recorded | Yes |
| EV-QA-04 | Request checksum and parameters recorded | Yes |
| EV-QA-05 | Output checksums present | Yes |
| EV-QA-06 | Identity report linked | Yes |
| EV-QA-07 | Semantic report linked | Yes |
| EV-QA-08 | Missing metadata disclosed | Yes |
| EV-QA-09 | No credential-bearing URI | Yes |
| EV-QA-10 | Promotion claim matches evidence tier | Yes |

## Failure codes

- `AHIF-EV-001` missing canonical reference checksum
- `AHIF-EV-002` missing or invalid prompt package reference
- `AHIF-EV-003` incomplete execution metadata
- `AHIF-EV-004` output integrity failure
- `AHIF-EV-005` missing identity evaluation
- `AHIF-EV-006` missing semantic evaluation
- `AHIF-EV-007` undisclosed missing metadata
- `AHIF-EV-008` unsafe external reference
- `AHIF-EV-009` unsupported promotion claim
- `AHIF-EV-010` generated output registered as identity authority

Any blocking failure sets the bundle status to `rejected` or returns it to `draft`.
