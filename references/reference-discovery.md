# Reference Discovery — context-driven, evidence-based design research

## Trigger and order
For complex greenfield interfaces, redesigns, or a major new visual direction, execute **after** product/flow/content/screen contracts and existing-design audit, but **before** visual direction approval, component decisions and screen construction. For small changes reuse existing approved references.

## Inputs
Task, audience, content density and limits, brand constraints, screen and section contract IDs, interaction states, viewports, existing component inventory, aesthetic anti-patterns, implementation technology.

## Search lanes, in priority order
1. **Existing project:** approved Figma components, existing screens, live product patterns, source UI. Prefer reuse.
2. **Visual and composition:** Refero, Land-book, SiteInspire, Lapa Ninja, Awwwards. Search by section function (hero, evidence, case list), audience, density and brand tone rather than superficial keywords.
3. **UX flows:** Mobbin, Page Flows, public product demos; examine sequence, empty/errors, CTAs and responsive states.
4. **Component contracts:** The Component Gallery, Storybook, shadcn registry, Radix, React Aria, Carbon, Atlassian, Cloudscape. Extract anatomy, slots, properties, accessibility and behavior.
5. **AI-specific only when task warrants:** assistant-ui, CopilotKit, AI Elements, Google PAIR, Microsoft HAX. Do not add chat/agent decoration to non-AI contexts.
6. **Ready-to-adapt code/assets:** 21st.dev, shadcn registries, Figma Community, Untitled UI. Verify provenance and compatibility before installing third-party code.

## Protocol
A. Produce 3–8 grounded candidates for a substantial screen, with URL and concrete relevant pattern; do not invent a page or claim inspected code without opening it.
B. Identify the exact decision each candidate informs: layout, text treatment, conversion evidence, interaction, component structure, responsive behavior or motion.
C. For each candidate complete `templates/reference-evaluation.md`. Classify as INSPIRE (idea only), STUDY (anatomy/behavior) or ADAPT (permitted code/component candidate).
D. Select a *complementary* set, not five similar screenshots. Record both borrowed principle and rejected properties.
E. Map selected reference IDs to SECTION/COMPONENT contract IDs, add testable rules (e.g. min/max columns, slot order, content width, text bounds) and permitted deviations.
F. Assemble with existing project masters/semantic tokens. The selected inspiration never overrides established identity or content requirements without explicit approval.
G. Compare outcome to source principle, not pixel-match by default. Perform screenshot, node/instance/binding and viewport QA.

## Evaluation
Weighted starting heuristic (project-adjustable): task fit 30, content fit 20, brand fit 20, implementation 15, responsive/a11y 15. A high total does not override a critical mismatch or unverified license for direct reuse. Scores are human-assessed, not proof of source quality.

## Learning and personal test prototypes
Default workflow `research-personal` favors exploration, close visual study and fast disposable prototypes. No lengthy license audit for inspiration; keep source URLs and note obvious restrictions. Non-commercial use alone does not grant permission to copy proprietary assets/code, nor to redistribute them. Before shipping or publishing, confirm reuse rights and attribution requirements. Avoid secretly retrieving paid/protected assets or installing unreviewed remote code.

## Tool behavior
Search indexes and MCP availability vary; only claim programmatic retrieval when actual tool or endpoint evidence exists in current session. Don't assert every listed service exposes a public API. Respect account access and rates. If only a screenshot is available, extract observations, not fictional component internals.

## Source card release gates
- Every selected source has inspectable URL, exact pattern, usage rationale, attribution/provenance.
- Every in-scope key section has a concrete composition direction or an explicit reason to rely solely on project design system.
- Each selected pattern maps to actionable Section/Component Contract rules.
- Visual direction includes explicit alternatives rejected.
- Never declare reference research complete if no sources were actually reviewed.
