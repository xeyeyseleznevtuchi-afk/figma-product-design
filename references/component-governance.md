# Design system architecture and governance

Use Atomic Design as useful composition vocabulary, not a command to build atom/molecule/organism pages. Nathan Curtis' scope and documentation thinking is a stronger guide for maintenance cost.

## Candidate → accepted component
Require: actual consumer(s), repeated or strategically standardized use, behavioral responsibility, stable API, variants / slots, accessibility semantics, responsive rules, content limits, owner. Reject as global component if single-use and uncertain; keep local/experimental.

## Build order
1. Primitives and semantic token modes. 2. Typography and effects. 3. Basic controls/icons. 4. Composite fields and navigation. 5. Product-specific patterns. 6. Screen templates. 7. Consumer examples.

## Every documented component
Purpose, anatomy, do/don't, props, variants/state coverage, keyboard/focus, text expansion, 320-ish compact behavior if applicable, system token bindings, nested instances, sample real-world copy, maintenance owner, accepted consumer screens.

## Variant hygiene
Variant axes describe meaningful behavior, not every combinatorial combination. Use instance swap for icon choice, text properties for labels, boolean properties for optional affordances. Split excessive matrices. Do not detach library instances for convenience.

## QA
Verify master+instances, correct variant labels and properties, binding to semantic variables, updates propagate, use in a real screen, and no unnecessary duplicate components.
