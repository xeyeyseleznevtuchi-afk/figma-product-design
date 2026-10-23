# Component contracts: design + behavior + implementation

Every reusable component receives a contract rather than a screenshot gallery.

## Contract fields
- Problem and user intent; where component belongs; when **not** to use it.
- Public API: boolean, text, instance swap, slot (when supported), variant axes; default values and naming convention.
- Semantic roles; keyboard operation; focus order and focus appearance; labels and feedback.
- Dimensions and responsive constraints: hug/fill/fixed and content overflow, localization expansion.
- Visual states and state transitions; disabled behavior; async progress and cancellation.
- Dependencies: tokens, styles, nested components, icons and their provenance.
- Test fixtures: typical, long translation, missing content, narrow width, density variants, contrast modes.

## Decision process
1. Count real usage sites and distinguish structural reuse from superficial resemblance.
2. Verify one source component vs narrow purpose-specific components; avoid a combinatorial variant explosion.
3. Make variants for meaningful appearance/state axes; use TEXT, BOOLEAN, INSTANCE_SWAP or SLOT for content variation, not new variants.
4. Create foundations first, component after; use named, documented props. Instantiate in approved usage contexts.
5. Review actual specimen at natural size; reject unreadable truncation, arbitrary defaults or disconnected tokens.

## Naming and upgrade safety
Do not rename published component properties casually: property IDs can change, breaking overrides. Prefer additive changes with migration plan, usage scan and rollback. Record source node/component IDs and library keys; never guess IDs.

Primary references: https://developers.figma.com/docs/plugins/working-with-component-properties/ ; https://eightshapes.com/articles/documenting-components/
