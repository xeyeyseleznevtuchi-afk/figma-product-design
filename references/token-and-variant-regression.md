# Design-system integration regression: tokens, variants, responsive screens

## Test fixture: new B2B SaaS workspace
Build a minimal desktop (1440px) and mobile (390px) workflow in an isolated Figma file. Show realistic distinct metric values and record content rationale; avoid duplicating placeholder metrics across cards.

## Foundation assertions
- Local COLOR collection contains semantic background, surface, primary/secondary text, border, action tokens, and (only if necessary) base primitives.
- Inspect aliases and mode values; distinguish created variables from actual paint/text bindings.
- Record `variablesCreated`, `boundNodes`, `boundPaints`, `unboundExpectedNodes`.
- Pass requires **actual boundVariables references on rendered nodes**. Matching RGB alone FAILS. If API supports local paint binding, use official Plugin API, inspect post-write `boundVariables`.
- Existing approved variable names/values must not be repainted by accident.

## Component assertions
- Button family: at least primary, secondary and disabled specimens, or explicit justification for a narrower scope.
- Build true ComponentSet variant property when required; verify each variant's component property definitions, usable instances, and text overrides.
- Do not mistake separate named components for a verified variant set.
- Record master IDs, set ID, variant property names, each sample instance's `mainComponent` ancestry, and any detached instances.
- Distinguish states that are static visual specimens from functional behavior in a running app.

## Responsive/content assertions
- Desktop and mobile share semantic tokens and components where suitable.
- For mobile 390px: no horizontal clipping, no elements beyond screen bounds, readable copy, intact hierarchy, accessible tap target intent.
- Test one 320px layout or document why not in scope; test long labels and mixed Russian/English content.
- Verify numeric properties are numbers, Figma font styles are loaded, text boxes fit content, and small-screen layouts are not merely desktop scaled down.

## Visual and structural QA
1. Capture screenshot of every requested viewport at legible resolution.
2. Inspect text collisions, clipping, spacing, component styling, density, grid rhythm, realistic content and empty states.
3. Audit variable bindings and instance links with a read-only node traversal.
4. Record each gate as PASS/FAIL/NOT TESTED with actual evidence and node IDs.
5. Release only when there are no unresolved critical or major defects for declared in-scope deliverables.

## Baseline from October 2026 sandbox
Initial test created 6 COLOR variables, 2 master components, 4 instances and a 1440px editable desktop screen. Structural audit found **0 bound nodes** and duplicate metric content. Attempted mobile/variant remediation did not yield a verified successful write. Therefore do **not** call this regression passed or claim the plugin skill is fully validated.

## Minimal report
| Check | Status | Evidence |
|---|---|---|
| Variables declared | | |
| Variables bound to rendered nodes | | |
| Component set and actual variants | | |
| Instance links | | |
| Desktop screenshot | | |
| Mobile screenshot | | |
| Long-content/overflow | | |
| Failure recovery and retries | | |
