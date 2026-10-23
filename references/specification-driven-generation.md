# Specification-driven, artifact-constrained generation

## Purpose
Generation must implement a finite explicit contract, not invent product meaning, layouts, props or styles at the last moment. This is a synthesized team workflow informed by UX deliverables, design-system specification practice, and component-driven development; it is not a standalone published standard.

## Contract graph
- Product contract: roles, entities, operations, rules and permissions.
- Flow contract: triggers, branching, transition IDs, recoveries.
- Screen contract: purpose, regions, data fields, actions, interaction states, content limits, accessibility constraints and supported viewports.
- Pattern/component contract: anatomy, slots, props, variants, behavior, dependencies, layout rules and fixture datasets.
- Token contract: primitive/semantic references, types, modes, owner and real Figma bindings.
- Render contract: screen contains real master instances, populated fixtures and traceable layout containers.
- QA contract: each constraint maps to structural, screenshot, behavioral or manual evidence.

## Stable IDs and dependencies
Use stable human-readable IDs per project, e.g. FLOW-001 → SCREEN-003 → PATTERN-002 → COMPONENT-007 → TOKEN-004. The chain is a *dependency graph*, not necessarily a strict hierarchy: one component serves several screens, and a flow spans many screens. Store links to Figma node IDs, source artifacts and version/revision, not just labels.

## Generation stages
1. **Compile** task/model/flow/screen contracts into a demanded component dependency inventory.
2. **Resolve** verified existing masters and tokens first; propose missing contracts before creation.
3. **Instantiate** only approved component APIs and semantic tokens, using deterministic variant/property/fixture choices.
4. **Render** into templates with declared responsive and content policies.
5. **Verify** link integrity, variable bindings, text overflow, state coverage and real screenshots.
6. **Report changes** to contracts and all potentially impacted consumers. Do not patch each instance when the contract itself is wrong.

## No invented constraints
If a contract omits an important interaction or content rule, mark UNRESOLVED and make a scoped explicit proposal; never silently present a guess as validated requirements. Design exploration remains possible, but label explorations as proposals until selected.

## Determinism and stability
The goal is constrained reproducibility, not bit-identical screenshots. Preserve IDs, master-instance connections, semantic tokens, naming, fixture seeds, visual rules and scope. Build scripts should first inspect by stable IDs/known parent, and avoid recreating identical named components.

## Verification checklist
- Every screen references a flow and screen contract.
- Every reusable component has a contract and at least one consumer.
- All requested states have fixtures; empty/error/loading are not decorative stand-ins.
- No unapproved new visual token or component family was introduced while assembling an existing system.
- All declared bindings appear on target nodes, with no unexplained detached instances.
- Every change records affected dependencies and results of targeted regression checks.

## Sources / relationship
Nathan Curtis, Component Specifications: https://nathanacurtis.substack.com/p/component-specifications-1492ca4c94c
NN/g Wireflows: https://www.nngroup.com/articles/wireflows/
Storybook stories: https://storybook.js.org/docs/8/writing-stories/index
Storybook interaction tests: https://storybook.js.org/docs/9/writing-tests/interaction-testing
Figma Design Systems 102: https://www.figma.com/blog/design-systems-102-how-to-build-your-design-system/
DTCG 2025.10: https://www.designtokens.org/TR/2025.10/format/
