# Identity Entropy

Identity entropy is the gradual accumulation of small visual deviations across repeated generations.

## Common causes

- repeatedly regenerating from prior outputs instead of the master photo
- excessive stylization
- changing model or rendering pipeline
- strong beauty filtering
- extreme focal lengths
- heavy makeup or facial accessories
- profile angles that hide key landmarks
- inconsistent age cues

## Control protocol

1. Always return to the original master photo.
2. Reassert the identity lock in every compiled prompt.
3. Keep one neutral identity benchmark image.
4. Test difficult scenes against the benchmark.
5. Reject outputs that are merely attractive but not clearly the same person.
6. Treat accumulated drift as a system failure, not a cosmetic issue.
