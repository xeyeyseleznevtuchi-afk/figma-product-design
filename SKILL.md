---
name: figma-product-design
description: Design, build, evolve, and validate native Figma product UI, brand kits and scalable design systems, from zero or existing files. Select the smallest fitting workflow: discovery, UX architecture, visual direction, tokens/components, screens, changes, brand assets, or QA.
version: 2.2.0
---
# Figma Product Design v2.2 — workflow orchestrator

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
