# Identity Reference Mapping

## Canonical Rule

`MASTER_PHOTO.jpg` remains the only canonical identity. Adapter syntax may bind or transport the asset but may not reinterpret it.

## Mapping Outcomes

- `native_reference`: the target accepts an identity or image reference mechanism.
- `image_conditioning`: the target accepts image-to-image or equivalent conditioning.
- `text_only_fallback`: allowed only for non-production experiments and always marked degraded.
- `blocked`: required when identity preservation depends on a reference mechanism that the target cannot represent.

## Strength Policy

Reference strength is never maximized blindly. It must balance identity preservation against pose, environment, and activity adaptation. Any strength parameter is recorded in the adapter result with its derivation reason.

## Prohibitions

- substituting a generated portrait for the master photo;
- converting identity into a generic demographic description;
- applying style references as identity references;
- silently dropping the identity asset;
- using multiple competing face references.
