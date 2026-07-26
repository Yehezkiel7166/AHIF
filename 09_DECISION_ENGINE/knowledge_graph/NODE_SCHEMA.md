# Knowledge Graph Node Schema

Each node should include:

```text
id:
type:
label:
description:
inputs:
outputs:
constraints:
confidence:
source:
version:
```

## Example

```text
id: weather.rain.light
type: weather
label: Light rain
inputs:
  - precipitation
  - cloud cover
outputs:
  - umbrella_possible
  - wet_ground
  - reduced_contrast
constraints:
  - avoid_heavy_storm_behavior
confidence: inferred
source: context
version: 1.2
```
