# Decision Output Schema

```yaml
identity_lock: string
scene:
  location: string
  place: string
  time: string
  weather: string
activity:
  primary: string
human:
  pose: string
  body_language: string
  expression: string
styling:
  outfit: string
  footwear: string
  hair: string
  makeup: string
  accessories: []
photography:
  camera_intent: string
  lens_logic: string
  composition: string
  lighting: string
story:
  beat: string
risk:
  identity: low|medium|high
qa:
  status: pass|revise|fail
```
