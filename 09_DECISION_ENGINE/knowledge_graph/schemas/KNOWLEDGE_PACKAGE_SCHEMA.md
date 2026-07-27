# Knowledge Package Schema

## Root object

| Field | Type | Required | Rule |
|---|---:|:---:|---|
| `package_id` | string | yes | `AHIF-KP-<DOMAIN>-<NAME>` |
| `package_version` | string | yes | semantic version |
| `schema_version` | string | yes | exact supported schema |
| `status` | enum | yes | `draft`, `candidate`, `active`, `deprecated`, `blocked` |
| `domain` | string | yes | registered domain code |
| `canonical_sources` | array | yes | non-empty repository-relative paths |
| `records` | array | yes | one or more knowledge records |
| `validation` | object | yes | validation metadata |

## Knowledge record

| Field | Type | Required |
|---|---:|:---:|
| `id` | string | yes |
| `label` | string | yes |
| `domain` | string | yes |
| `type` | string | yes |
| `status` | string | yes |
| `conditions` | object | yes |
| `effects` | object | yes |
| `constraints` | array | yes |
| `priority` | integer | yes |
| `confidence` | number | yes |
| `provenance` | array | yes |
| `consumer_hints` | object | yes |

## Validation metadata

Validation metadata includes:

- `schema_validated`
- `semantic_reviewed`
- `identifier_unique`
- `provenance_resolved`
- `review_status`

A package is consumable only when all mandatory values are true and status is `candidate` or `active`.
