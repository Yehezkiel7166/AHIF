# Identity Decision Tree

```text
Is a master photo available?
├─ No → Request one before identity-critical generation.
└─ Yes
   ├─ Is the requested style identity-safe?
   │  ├─ Yes → Continue.
   │  └─ No → Reduce style intensity or add recovery safeguards.
   ├─ Is the face visible enough?
   │  ├─ Yes → Continue.
   │  └─ No → Adjust angle, lighting, obstruction, or framing.
   ├─ Does makeup or expression risk changing identity?
   │  ├─ Yes → Reduce intensity.
   │  └─ No → Continue.
   └─ Compile prompt with identity lock and QA gate.
```
