---
name: figma-product-design
description: Design, build, evolve, and validate native Figma product UI, brand kits and scalable design systems, from zero or existing files. Select the smallest fitting workflow: discovery, UX architecture, visual direction, tokens/components, screens, changes, brand assets, or QA.
version: 2.7.0
---
# Figma Product Design v2.7 — workflow orchestrator

## Goal and precedence
Deliver high-quality, genuinely editable Figma artifacts, not persuasive prose, placeholder screenshots, or surface-level AI decoration. Respect user instructions, established design, and directly observed file/code evidence above generic advice. This skill **does not replace** `human-first-design`, `human-first-web-audit`, or official Figma capabilities. Invoke official `figma-use` before any Figma API write; `figma-generate-design` for composed screens, `figma-generate-library` for tokens/components, and `figma-create-new-file` when creating a file. If these skills/tools are unavailable, explicitly report limitations; never claim canvas modifications.

## Task router (choose ONE primary lane)
- **new-product**: problem → research assumptions → IA + workflows → visual direction → minimum viable foundations/components → screens → QA → handoff.
- **design-system-from-zero**: target product and demand inventory → foundations → component dependency graph → build → usage examples → QA.
- **existing-system**: inspect → gap/drift report → smallest scoped modification → validate, preserve approved assets.
- **screen / flow**: behavior & state matrix → library reuse → native screen build → visual + structural QA.
- **brand-kit**: brand source audit → verified identity assets → color + typography + graphic language → credible real applications → usage rules. Do not turn into UI-component library unless requested.
- **audit-only**: read-only audit and prioritized findings; no mutation unless requested.
- **single-component**: inspect foundations → create missing dependency only → states/properties → test.

## Non-negotiable gates
1. **Understand scope.** Identify product, audience, workflows, delivery medium, file, and protected areas. If input is sufficient, proceed without unnecessary questions. Distinguish source evidence, explicit user decisions, interpretation, and unknowns.
2. **Inspect before building.** For existing files, find relevant pages/frames, fonts, tokens, source components, screens, libraries, and approved references; record IDs and provenance. In new files explicitly flag that foundations are newly proposed, not existing brand fact.
3. **UX before UI for complex flows.** Map roles, triggers, primary and recovery paths, empty/loading/error/success/permission states, responsive constraints. See `references/ux-architecture.md`.
4. **Visual direction before styling.** Describe audience-appropriate hierarchy, density, reference qualities, contrast, type, imagery and anti-patterns. Ground references; avoid stock AI dashboard visual treatment. See `references/visual-direction.md`.
5. **Tokens/components before screen duplication.** First inspect; use existing libraries. From scratch, build only demanded foundations and components, document their role and dependency. See `references/design-system.md`.
6. **Native editable Figma as required output.** Use real text, frames, auto-layout, components/instances, bound variables. Never simulate a full screen using one image. Original logos/photos can be image/vector assets; UI itself remains editable. See `references/figma-execution.md`.
7. **Visual/structural evaluation.** Inspect screenshot AND node tree. Reject clipped text, cramped hierarchy, overlapping nodes, detached copies, incorrect font, invented brand, dummy content and unrelated edits. See `references/quality-gates.md`.
8. **Evidence-based completion.** Report exact node/page links, made-vs-planned changes, remaining uncertainties, and validation evidence. If anything fails, fix before claiming done.

## Execution protocol
- Choose minimal workflow; do not run full discovery for a single button or expand brief into an entire system.
- Preflight inventory + design brief (use `templates/design-brief.md`); for existing files produce change scope (`templates/change-plan.md`).
- For new products document tasks/IA/flows and a state matrix (`templates/state-matrix.md`). Avoid invented user-research findings or fabricated validated personas.
- Define visual direction with explicit tradeoffs, using `templates/visual-direction.md`; default to established visual language in existing projects.
- Define demanded token/component inventory, dependencies, stable names, bindings, variant/instance-swap policies, usage scenarios and exclusions.
- Build safe, coherent batches; identify stable node IDs; return created/mutated IDs; limit changes to permitted page/section. Keep main components separate from specimen instances when useful.
- Preview real resulting compositions at usable scale. Inspect text fit, visual rhythm and cross-screen coherence, not just API success. Correct targeted defects and re-check.
- Deliver `templates/qa-report.md` and `templates/handoff.md` as appropriate.

## Mandatory prohibitions
- No claims of brand-approved graphics from synthesized examples; no default fonts/colors substituted for source without explicitly flagging a proposal.
- No generic three-card grids, decorative gradients, unrelated abstract 3D, excessive badges and filler for visual effect.
- No overcomponentization: promote a pattern only after reuse/relevance, vision fit, cost, composability and documentation review.
- Never recreate icons with rotated primitives when source SVG/components are available.
- Never detach imported library components solely for convenience.
- Never assume a successful `use_figma` run proves visual quality; **textAutoResize, rendered text bounds, image assets, correct fonts and screenshots must be checked**.
- Never modify other pages or existing approved components without scope authorization.
- Never invent successful tool use, researched facts or user validation.

## Reference map
- `references/source-review.md` — audited reading inventory, provenance, confidence and source limits.
- `references/ux-architecture.md` — discovery, IA, task flows and state planning.
- `references/visual-direction.md` — visual taste, brand continuity, design feedback memory.
- `references/design-system.md` — architecture of tokens, variant sets and component governance.
- `references/figma-execution.md` — implementation specifics and Figma safety.
- `references/quality-gates.md` — acceptance gates, accessibility, screenshot and regression review.
- `references/brand-kit.md` — dedicated brand kit workflow (not UI kit).
- `references/tests.md` — evaluation scenarios and regression suite.

## Definition of done
A complete deliverable must be visually credible, structurally native/editable, context-appropriate, and scoped; demonstrate selected states/variants; preserve approved material; and have no known critical or major QA failure. Missing tool access, evidence, or actual review must be reported as incomplete.

## Deep engineering gates (v2.2)
- For component creation/update follow `references/component-contracts.md`; explicitly document states, API, keyboard, content and responsive fixtures.
- For screens use `references/responsive-and-content.md` and `references/accessibility-and-interaction.md`. Do not certify WCAG compliance from Figma drawings.
- Before/after **each** modifying Figma tool call use `references/figma-canvas-preflight.md`; a successful write is insufficient evidence of a visually correct design.
- Apply `references/qa-scorecard.md` to complex deliverables. A zero on an applicable dimension blocks declaring finished.
- Review `references/evidence-register.md` to distinguish source-backed rules from original team process proposals.

## Failure recovery and integration regression (v2.3)
- Follow `references/recovery-protocol.md` whenever a Figma operation fails, times out or is blocked. An error is not evidence of rollback; inspect actual state before retry. Never try to evade a permissions or safety block.
- Follow `references/token-and-variant-regression.md` when claiming a working design system or responsive component library.
- Declaring a color variable is **not** equivalent to binding it. Report created variable counts separately from audited `boundVariables` references on target nodes.
- Separate real COMPONENT_SET variants from named standalone components. Verify instance ancestry, overrides and coverage against the requested state matrix.
- Distinguish desktop-only checks from a verified mobile implementation. Never say responsive QA passed without reviewing the target-width screenshot and bounds.
- Every test or release report must state PASS, FAIL or NOT TESTED with exact evidence; structural package validation alone does not establish design quality.

## Artifact-first and Atomic Design contract (v2.4)
- For **complex new-product and design-system-from-zero** work, read `references/artifact-first-workflow.md` and maintain `templates/artifact-manifest.md`. Create or locate inspectable brief, task/IA, user flows/wireflows/state matrix, content template, visual direction and component dependency inventory **before substantial high-fidelity screen construction**. List concrete artifact paths/IDs; ideas only stated in chat do not count.
- Follow `references/atomic-composition.md` to compose atoms → molecules → organisms → templates → populated pages through real Figma master components, component sets and instances, not disconnected shapes/text. Preserve links and audit actual bindings.
- Read `references/atomic-architecture-sources.md`; distinguish Brad Frost's **non-linear** conceptual Atomic Design from the team's artifact gate and recommended Figma file structure. Do not enforce an artificial waterfall; refine components from real page feedback.
- Component specimen fixtures and state coverage must precede duplication in final screens. Keep product-relevant local patterns local; do not publish every component by default.
- **Release blocker:** complex greenfield screen without an artifact manifest (or verified equivalents), screen constructed mainly from raw disconnected nodes, or unverified master-instance relationships cannot be declared a completed system.
- For a one-control edit or small scoped change, **reuse** existing evidence and avoid ceremonial over-documentation.

## Specification-driven composition and reproducibility (v2.5)
- Before creating nontrivial high-fidelity screens, read `references/specification-driven-generation.md`; produce or resolve explicit product/flow/screen/component/token contracts with stable IDs and dependencies.
- Use `templates/screen-contract.md` to define the screen's content schema, transitions, action permissions, state coverage, responsive composition and accepted components.
- Use `templates/component-fixtures.md` to describe each demanded component's variants, typed properties, content bounds, semantic tokens, specimen examples, and consuming screens. Build isolated fixture instances **before** duplicating components in final screens.
- Ground technical choices in `references/new-research-2026-10.md` and distinguish original source statements from our engineering requirements.
- Generate screens from explicit reusable instances and constrained properties; avoid improvising new component structures, styles or business rules at assembly time.
- Track flow → screen → pattern → component → token links as a directed dependency graph, not a rigid chain. When contracts change, identify impacted consumers and revalidate them.
- For small changes, reuse existing approved contracts; do not force a new discovery ritual.

## Artifact compiler integration (v2.6)

For complex greenfield projects:

1. Read `references/artifact-compiler.md` before building screens.
2. Create inspectable product, flow, screen, content, component and token contracts.
3. Maintain stable artifact IDs, revisions, provenance, approval status and dependencies.
4. Use `templates/contract-manifest.json` as the starting manifest.
5. Validate the manifest with `scripts/validate_contracts.py`.
6. Build isolated component specimens before composing final screens.
7. Assemble screens from reusable component instances and verified semantic tokens.
8. Verify master-instance links, variable bindings, states and responsive layouts.
9. When contracts change, identify affected components and screens.
10. Compare two independent builds before claiming reproducible generation.

A successful manifest validation does not prove visual quality.
Never claim completed Figma QA without inspecting actual screenshots.

## Reference Discovery (v2.7)
- For significant redesign or new visual direction, read `references/reference-discovery.md` after content and screen contracts, before UI composition.
- Search existing project assets first; next consult task-appropriate visual, UX, component, or AI-specific sources from `references/reference-source-registry.md`.
- Document selected references with `templates/reference-evaluation.md`, including exact URL, inspected evidence, transferred principle, rejected attributes, provenance and contract IDs.
- Create `templates/section-contract.md` for significant page sections: required slots, composition, density, responsive behavior, approved components and selected reference IDs.
- Only adopt relevant references; do not substitute generic galleries for task and brand evidence. Keep exploratory personal prototypes lightweight, while respecting applicable reuse restrictions.
- A page screen assembled without inspected composition references or an explicit existing-system rationale must not be called visually validated.
