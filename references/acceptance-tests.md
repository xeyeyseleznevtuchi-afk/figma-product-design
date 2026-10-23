# Acceptance tests and release evidence

## Gates
G0 Brief/provenance — requirement scope, authorized file, source of truth, existing/greenfield classification.
G1 UX — role-task-flow, state matrix, information structure, realistic content, recovery, clear action vocabulary.
G2 Visual — distinct deliberate direction or strict existing-brand matching, screenshots at supported viewports, typography sanity.
G3 System — real component masters/instances, variable scopes and aliases, variants/slots/ownership, no unnecessary duplicates.
G4 Figma integrity — native editable nodes, Auto Layout flex/resizing, proper text width/height, no missing media, no orphaned nodes.
G5 Accessibility — focus visibility, contrast checks where measurable, target sizes, error labels; avoid claiming certification from static mockups.
G6 Handoff — screen IDs, behavior/state coverage, implementation notes, open assumptions, exact remaining defects.

## Recording
Each gate: PASS with evidence / FAIL with defect+node ID / NOT TESTED with honest reason. Any fail on requested in-scope core output means not done. Figma API success + packaging validator PASS means only technical operation completion.

## Anti-regression task suite
A. Greenfield application: multiple roles, collection actions, filtering, error/empty/loading states; optional dark mode.
B. Existing app change: change one control; prove no unrelated source layers changed.
C. Component library: button/field/select with states, props, real instances, typed semantic variables.
D. Brand kit: source assets only; explicit override wins stale existing token; logo source fidelity.
E. Localization: long Russian/German text, narrow viewport, right-to-left if product requirement.
F. Recovery: simulate failed partial write and show inspect-before-retry behavior.
