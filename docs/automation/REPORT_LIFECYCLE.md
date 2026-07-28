# Report Lifecycle

Committed evidence belongs in `docs/releases/` and `docs/repository-health/`; it is historical baseline documentation, not a live run. Local and CI JSON is generated under ignored `.artifacts/reports/`. Failure mutations use operating-system temporary directories and are deleted. Legacy `reports/` remains ignored for compatibility.

Every generated report contains a UTC `generated_at` timestamp and checked-out `commit_sha`; repository paths use POSIX repository-relative form. Lists and JSON keys are sorted. Semantic reproducibility comparisons omit only `generated_at`. The release gate rejects evidence whose commit differs from the current checkout, preventing stale files from being treated as current proof. `make clean-reports` removes generated output.
