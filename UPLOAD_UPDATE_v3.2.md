# Upload Update — AHIF 3.2.0

1. Check out `sprint-027-executable-verification-hardening` from `main`.
2. Run `make test`; retain the generated `reports/` CI artifact for repository evidence.
3. Review the six negative-test results and confirm `reports/release-gate.json` and repository health resolve to `hold`, not operational approval.
4. Open a draft pull request to `main`; do not merge or mark ready without human review.

No secret, external telemetry, deployment evidence, or operational/LTS evidence is included.
