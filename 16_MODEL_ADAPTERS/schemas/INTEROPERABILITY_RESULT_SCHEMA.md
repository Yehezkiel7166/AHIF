# Interoperability Result Schema

## Purpose

Defines the output of testing one canonical package across multiple registered adapters.

## Required Fields

```json
{
  "schema_version": "1.0",
  "case_id": "case-id",
  "source_package_hash": "sha256",
  "adapter_ids": [],
  "execution_results": [],
  "compatibility_report_id": "report-id",
  "contract_failures": [],
  "status": "pass",
  "reproducibility_key": "sha256"
}
```

## Status Values

- `pass`
- `pass_with_declared_variance`
- `revise`
- `fail`
- `blocked`

## Reproducibility Key

The key is derived from the source package hash, ordered adapter identifiers, capability profile hashes, and test configuration hash.
