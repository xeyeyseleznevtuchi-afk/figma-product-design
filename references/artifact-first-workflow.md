# Artifact-first product design: required evidence before high-fidelity screens

## Intent
Prevent screen-first, code-first, or decorative-first production without a traceable UX and design-system foundation. **Artifact-first is a team execution contract**, not a direct quotation from Atomic Design. Distinguish planned documents from actually created deliverables.

## Artifacts and acceptance gates (greenfield complex UI)
A0 **Design brief and evidence register** — scope, user groups, goals, constraints, device targets, success criteria; known facts vs assumptions; explicit non-goals. Use `templates/design-brief.md`.
A1 **Task inventory and information architecture** — roles, task decomposition, entities and relationships, sitemap/navigation model, priority and frequency of operations. Do not invent user interviews.
A2 **User flows / wireflows / state matrix** — primary, secondary, recovery paths, transitions, action triggers, empty/loading/error/success/permissions and edge cases. Use `templates/state-matrix.md` plus task and wireflow diagrams. Wireflows are especially suitable for dynamic applications where the same page changes based on actions.
A3 **Content model / low-fidelity templates** — real field inventory, sample data, data density, key hierarchy, display rules, content bounds, long labels and representative cases. Do not mistake lorem ipsum for a tested content model.
A4 **Visual direction artifact** — verified brand assets or explicitly proposed mood/visual direction, rationale and comparison, type, layout/density and accessibility targets. Use `templates/visual-direction.md`.
A5 **Design-system plan** — inventory of semantic/primitive/component tokens, component dependency graph, reuse rationale, states and ownership. Include a deferred list; build only demanded parts.
A6 **Figma foundations and isolated specimens** — native variables **with audited bindings**, styles, genuine main components, component properties and variant sets, documented component contracts, specimen states.
A7 **Composed templates and populated pages** — organisms made of actual instances, responsive templates, realistic page content, variants and layout modes, traceability to requirements and component masters.
A8 **QA and handoff evidence** — visual screenshots, structure/binding audit, behavior and responsive check results, explicit PASS/FAIL/NOT TESTED.

## What counts as an artifact
A durable inspectable file, Figma page/section, diagram, explicit structured table, or documented specification with stable path/node ID and purpose. A vague plan in chat is not equivalent to a created artifact. Each in-scope stage must have concrete output and citation/path/node link in handoff.

## Figma page architecture (recommended, not mandatory)
00 Brief & evidence; 01 UX / task maps; 02 Wireflows & state matrix; 03 Foundations / tokens; 04 Components / isolated fixtures; 05 Patterns & templates; 06 Screens; 07 QA / handoff. Smaller tasks may reuse existing artifacts and skip irrelevant stages if this is documented. Do not create empty decorative pages just to tick a checklist.

## Gate before high-fidelity
Do not begin a substantial final-screen build until A0–A5 exist or have verified equivalents. Build component specimens before repeatedly placing raw UI primitives on final screens. Each final screen references the relevant flow, template and instances. If blocked by missing critical information, mark assumptions and limit claims.

## Iterate across levels
Brad Frost explicitly describes Atomic Design as a non-linear mental model. Do not interpret gates as waterfall sign-offs that forbid feedback. A page can reveal missing atoms or content constraints: revise foundational artifacts and propagate to instances, document change and recheck.

## Sources
- NN/g Task Analysis https://www.nngroup.com/articles/task-analysis/
- NN/g Wireflows https://www.nngroup.com/articles/wireflows/
- Figma Design Systems 102 https://www.figma.com/blog/design-systems-102-how-to-build-your-design-system/
- Brad Frost Atomic Design https://atomicdesign.bradfrost.com/chapter-2/
- Storybook Component Driven Development https://storybook.js.org/docs/9/get-started/why-storybook
