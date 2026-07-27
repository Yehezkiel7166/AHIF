# Audit Snapshot Specification

An immutable audit snapshot records:

- repository version and source fingerprint;
- governed file inventory;
- SHA-256 per governed file;
- active rule-set version;
- manifest path-resolution result;
- JSON parse result;
- Markdown-link result;
- registry baseline counters;
- unresolved exceptions and prior findings.

Snapshots are evidence of repository state only. They are not empirical model evidence or production telemetry.
