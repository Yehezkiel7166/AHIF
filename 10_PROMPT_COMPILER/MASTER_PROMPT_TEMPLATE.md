# Master Prompt Template

## Model-neutral positive prompt

```text
Use the uploaded master photo as the sole canonical identity reference. Preserve the exact same person, facial geometry, proportional relationships, age presentation, skin-tone family, and recognizability. Do not redesign, average, over-beautify, or replace the face.

Create one believable scene in [LOCATION], specifically [PLACE], during [TIME, SEASON, AND WEATHER]. The atmosphere is [ATMOSPHERE], supported by physically accurate environmental details.

She is [PRIMARY ACTIVITY]. Her pose is [POSE], with [BODY LANGUAGE], [GESTURE OR OBJECT INTERACTION], [EYE FOCUS], and [EXPRESSION]. The action must obey balance, anatomy, gravity, and the physical properties of nearby surfaces and objects.

She wears [OUTFIT AND FOOTWEAR], selected for the climate, activity, cultural context, and established character style. Her hair is [HAIR], makeup is [MAKEUP], and accessories are [ACCESSORIES], each serving a coherent visual or functional purpose.

Show [ENVIRONMENT INTERACTION] so the subject appears physically and socially present in the location. Use [CAMERA INTENT], [LENS LOGIC], [VIEWPOINT], [COMPOSITION], and [DEPTH OF FIELD]. Light the scene with [LIGHTING], consistent with the time, weather, architecture, practical sources, shadows, reflections, and color temperature.

Preserve realistic skin texture, hands, joints, fabric behavior, wind or moisture response, object weight, surface contact, location scale, and shadow continuity. Maintain one dominant visual story beat: [STORY BEAT].
```

## Negative constraints

Append only risk-relevant constraints selected under `NEGATIVE_CONSTRAINT_SYNTHESIS.md`.

## Compiler rule

Every resolved placeholder must originate from an accepted reasoning directive. The compiler may improve expression but may not invent the underlying decision.
