# Model Adapter Support Policy

## Support tiers

### Stable contract

The adapter contract, profile format, transformation plan, result schema, loss disclosure, and conformance behavior are stable.

### Contract-validated target

The target adapter has deterministic request serialization, capability mapping, semantic comparison, and regression fixtures.

### Empirically validated target

The target additionally has reproducible external image evidence reviewed under the identity-preservation protocol.

### Experimental target

The target is usable for evaluation but may change as provider behavior or evidence evolves.

## AHIF 2.0 target status

OpenAI Images, Midjourney, and SDXL/Diffusers are **contract-validated experimental targets**. Their adapter contracts are stable, but empirical image-output equivalence is not claimed by the repository.

## Promotion requirements

Promotion to empirically validated support requires:

1. immutable execution metadata;
2. model and provider version capture;
3. canonical master-photo binding;
4. representative scenario coverage;
5. identity-comparison reports;
6. degradation review;
7. reproducibility evidence;
8. no unresolved critical identity failure.

## Provider drift

Provider or model changes must trigger capability-profile review and regression revalidation.
