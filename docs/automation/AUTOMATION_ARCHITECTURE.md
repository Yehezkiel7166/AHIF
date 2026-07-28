# Automation Architecture

## Sprint 028 pre-change audit

The Sprint 027 baseline had seven executables, three workflows, six Make targets, six failure fixtures, and six generated report types. Findings recorded before implementation were: version, sprint, required-file, report-path, claim, and registry lists were hard-coded in Python; health independently repeated manifest, inventory, Git, and report serialization logic; wrappers embedded output paths; `reports/` mixed local and CI concerns; freshness was not checked; timestamps prevented byte determinism without a semantic comparison rule; failures used only `0/1/2` comments rather than a shared status contract; the manual regression workflow overlapped the full PR workflow; PR CI ran validation, regression, and failure injection twice; workflows lacked timeouts, concurrency, retention, and summaries. All scripts were referenced, so no executable was dead; the regression workflow was redundant and has been consolidated.

## Canonical execution hierarchy

`repository_checks.py` is the only implementation engine. It loads and validates `automation.config.json` once per process and supplies low-level JSON, link, manifest, metadata, registry, LTS, claim, and evidence-freshness checks. Its commands form the hierarchy: `verify-config` → `validate` → `regression` → `health` → `release`. `test_failure_injection.py` exercises the engine in isolated temporary copies. `test_all.sh` composes those commands and syntax checks without circular calls. Shell and Python compatibility entry points delegate; Make contains no validation logic.

`make release-check` creates validation, regression, and health evidence before the gate. `make test` is the full developer/PR harness. Concise output is default; pass `--verbose` to engine/wrapper commands, `--machine` for JSON-only engine output, or `AHIF_MACHINE=1` for the full harness.

## Inventory

- Commands: `verify-config`, `validate`, `regression`, `failure-injection`, `health`, `release-check`, `test`, `audit`, and `clean-reports`.
- Workflows: consolidated PR/main verification and tag/manual release gate.
- Generated artifacts: validation, regression, failure-injection, health, release-gate, and full-test JSON under `.artifacts/reports/`.
- Fixtures: temporary, isolated mutations for malformed state, bad config/path/exit mapping, invalid LTS, broken links, stale evidence, absolute-path leakage, ordering, and cleanliness.
