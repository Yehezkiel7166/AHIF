# OpenAI Images Request Serializer

## Section Mapping

1. Canonical identity lock and master-photo instruction.
2. Human realism and invariant traits.
3. Contextual appearance, action, and interaction.
4. Environment, weather, and cultural constraints.
5. Photography, lighting, and composition.
6. Explicit avoidance instructions derived from canonical negative constraints.

## Parameter Mapping

- aspect ratio becomes an approved target size or runtime-supported geometry value;
- quality intent maps only when the selected target model declares a quality control;
- seed is omitted unless the runtime capability profile explicitly supports it;
- negative constraints remain textual and auditable;
- reference image metadata is required for identity-preserving release.

## Failure Rules

Block on missing master photo when identity preservation is required, unsupported requested geometry without approved crop policy, or runtime fields absent from the selected capability snapshot.
