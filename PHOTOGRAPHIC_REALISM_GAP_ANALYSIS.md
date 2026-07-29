# Photographic Realism Gap Analysis — 2026-07-29

Inspection baseline: local `work` at `834ed83a5a2f6a400c30f176d4783182b95fb5da`; no configured
remote was available for a remote-HEAD comparison. The working tree was clean. AHIF remains 3.7.0,
Release Eligibility `HOLD`, LTS `hold`, and all adapters experimental.

## Evidence classification before implementation

| Capability group | Baseline | Existing owner | Gap and integrated impact |
|---|---|---|---|
| Surface: pores, undertone, highlights, non-waxy skin | incomplete | `02_CORE_IDENTITY/SKIN_REALISM.md` | Fine lines, lips, under-eye transition, peach fuzz, flyaways, restrained retouching and positive runtime handoff were incomplete. Reasoning/compiler/QA/runtime/adapter needed structured preservation; additive output is backward compatible. |
| Structure: posture, joints, hands, contact, gravity | incomplete | `03_HUMAN_SIMULATION/` | Core anatomy existed; asymmetry, expression tension and explicit compiler/QA handoff were incomplete. |
| Camera and optics | incomplete | `07_PHOTOGRAPHY/` | Perspective and story-driven camera existed; coherent exposure, optical depth/bokeh, roll-off, sharpening, blur/noise conditions and contradiction blocking were incomplete. |
| Lighting | incomplete | `07_PHOTOGRAPHY/LIGHTING_COMPOSITION.md` | Context matching existed; one explicit key/fill/environment model, skin response, reflection and temperature checks were incomplete. |
| Environmental integration | incomplete | `07_PHOTOGRAPHY/` and `08_STORY/` | Non-composited intent existed; atmosphere, edges, contact shadows, reflections and scale were not a structured runtime contract. |
| Anti-AI artifacts | incomplete | identity/human/photography modules and negative synthesis | Plastic skin, symmetry, floating accessories and compositing had partial coverage; fake pores, eyes, microcontrast/sharpening halos, synthetic bokeh, repeated people, text and geometry risks lacked one canonical vocabulary and stable runtime checks. |

## Contract impact

- **Inputs:** existing context fields are reused; no required request field was added.
- **Reasoning output:** additive `realism` decision record with compiler readiness, confidence and
  uncertainties; no private chain-of-thought.
- **Compiler/output:** additive realism section and metadata; canonical identity-first order remains.
- **QA:** stable `AHIF-QA-REALISM-*` failures supplement, never compensate for, identity gates.
- **Runtime:** existing stages and state transitions remain unchanged; blocked QA still prevents an
  adapter request, external invocation stays false, and empirical records stay not evaluated.
- **Adapters:** prepared packages disclose experimental status and semantic-only realism mapping;
  no capability, tier, certification, or production claim changes.
