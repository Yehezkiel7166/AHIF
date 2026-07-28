# AHIF Verification Report Format 1.0

Every JSON report uses schema identifier `ahif.verification-report` and `schema_version` `1.0`. Common required fields are `report_type`, UTC `timestamp`, `commit_sha`, `branch`, `checks_executed` (ordered name/status objects), overall `status` (`pass`, `fail`, or `hold`), string arrays `warnings` and `failures`, and integer `exit_code`.

Exit code `0` means the requested deterministic repository checks completed without a critical error; `1` means one or more checks failed; `2` is reserved for invocation or internal errors. A `hold` report may exit zero when repository conformance succeeds but release/LTS designation is deliberately withheld. Reports contain repository observations only and never fabricate external telemetry or operational evidence.
