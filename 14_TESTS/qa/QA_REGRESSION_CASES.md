# QA Regression Cases

| Case | Defect | Expected rule/code | Expected status |
|---|---|---|---|
| QA-001 | Identity lock omitted | AHIF-L001 / ID-LOCK-MISSING | fail |
| QA-002 | Prompt asks for a more attractive different face | AHIF-L002 / ID-FACE-REDESIGN | fail |
| QA-003 | Snow scene with summer sandals and bare legs | AHIF-L010 / CX-WEATHER-CONFLICT | revise |
| QA-004 | Subject simultaneously walking and seated as dominant activities | AHIF-L008 / CX-ACTIVITY-CONFLICT | revise |
| QA-005 | 14 mm close facial portrait without distortion protection | AHIF-L011 / PH-LENS-DISTORTION-RISK | revise |
| QA-006 | Sunset prompt with overhead noon shadows | AHIF-L012 / PH-SHADOW-CONFLICT | revise |
| QA-007 | Decorative sacred object used without cultural grounding | AHIF-L007 / CX-CULTURAL-INACCURACY | fail |
| QA-008 | Compiler invents a red umbrella absent from reasoning | AHIF-L003 / CP-UNSUPPORTED-DIRECTIVE | fail |
| QA-009 | Duplicate identity and lighting directives | AHIF-L009 / CP-DUPLICATE-DIRECTIVE | revise |
| QA-010 | Prompt is compliant and fully traceable | none | pass |
