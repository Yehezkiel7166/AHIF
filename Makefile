.PHONY: validate regression test release-check health failure-injection
validate:
	@./scripts/validate_repository.sh
regression:
	@./scripts/run_regression.sh
test:
	@./scripts/test_all.sh
release-check: validate regression health
	@./scripts/release_gate.sh
health:
	@python3 scripts/repository_health.py >/dev/null
failure-injection:
	@python3 scripts/test_failure_injection.py
