# Engineering design tokens without inventing brand values

## Layers
Primitive ramp (base values) -> semantic roles (background/text/border/action) -> component roles only when justified. Token taxonomy is independent from Figma page/file taxonomy. Use meaningful scopes and variable modes; avoid exposing every primitive to every property picker.

## DTCG 2025.10 interchange (different from Figma native variables)
Tokens in interchange JSON have `$value` and `$type`; groups can supply shared `$type`; aliases reference other token paths. Example (illustrative only):
```json
{"color":{"brand":{"accent":{"$type":"color","$value":{"colorSpace":"srgb","components":[0.6745,0.898,0],"alpha":1}}}}}
```
Do not infer this JSON can be pasted into Figma variable API unmodified. Build adapter for names, resolved types, mode values, alias chains and dimensional units. Consult DTCG final 2025.10 documentation for syntax before serializing export.

## Technical validations
- No alias cycles / orphan alias targets.
- No hidden token used as exposed semantic role.
- Semantic light/dark modes do not force contrast inversion of branded assets.
- Color values from product source or explicit approved user instruction (not common template palette).
- Typography and spacing support actual locales and data lengths.
- Compare design tokens to code tokens with provenance before overwriting either.
