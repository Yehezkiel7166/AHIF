# Compatibility Report Schema

## Required Object

```json
{
  "schema_version": "1.0",
  "report_id": "compatibility-report-id",
  "source_package_hash": "sha256",
  "adapter_results": [],
  "domain_comparisons": [],
  "pairwise_variances": [],
  "aggregate_status": "equivalent",
  "release_recommendation": "retain_experimental",
  "generated_at": "ISO-8601",
  "provenance": {}
}
```

## Adapter Result Reference

Each entry identifies exact adapter ID, adapter version, capability-profile version, result hash, request hash, and validation status.

## Domain Comparison

Required fields:

- `domain_id`
- `criticality`
- `canonical_directive_ids`
- `adapter_evidence`
- `preservation_status`
- `variance_type`
- `confidence`
- `release_effect`

## Aggregate Status

Allowed values:

- `equivalent`
- `equivalent_with_declared_variance`
- `degraded`
- `incompatible`
- `blocked`

## Integrity Rules

Unknown fields may be retained as extensions, but required fields may not be omitted. Hashes and exact adapter identifiers are mandatory for auditable comparison.
