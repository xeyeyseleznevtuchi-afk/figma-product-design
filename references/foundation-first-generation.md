# Foundation-first generation — hard gate

For greenfield projects and broad redesigns, never begin with high-fidelity screens. Treat existing brand or production systems as authority; create missing foundations first. A few colors and loosely styled rectangles are NOT a kit.

## Dependency order
0. Product, IA, flow, content, and visual reference evidence.
1. **Design constraints / foundations**: approved or explicitly provisional palette; semantic color variables and bindings; typography families/styles/line heights/scale; grid/container/spacing; radii/borders/effects; light/dark modes only when needed; responsive breakpoints; motion and accessibility rules. Document explicit forbidden patterns.
2. **Illustration and media system**: inventory of needed illustrations by SECTION-ID; visual language (geometry, stroke, color, perspective, level of detail, imagery type), subject intent, reference and source, asset aspect ratio, framing, variants, export rules and fallback. Create actual specimens before screen composition. Reuse existing brand illustrations and product screenshots where possible. Generated raster images, editable vectors and diagram sources are different deliverable types: choose correctly, do not call a raster illustration a Figma vector.
3. **Atomic library**: actual tokens and text styles; atoms, molecules and organisms as Figma COMPONENT/COMPONENT_SET nodes with relevant variants/properties and token-bound paint values. At least representative states and long-content fixture instances. Record COMPONENT-ID and dependencies.
4. **Section kit**: assemble reusable section masters and explicit Section Contracts with container bounds, columns, responsive reflow, slots, proof/media treatment, CTA hierarchy, content length bounds and visual rationale. Show specimens with real content for desktop and mobile.
5. **Preflight quality gate**: audit real Figma counts and links; screenshots of foundation specimens and section kit; token bindings; typography styles; image/illustration specimens; components, component sets and instances; accessibility/overflow for 390/1440 or task breakpoints. Report PASS/FAIL/NOT TESTED. Do not silently pass incomplete gates.
6. Only after a PASS preflight, assemble screens from approved section and component instances; compare with Section Contracts. Audit again.

## Hard stop: do not render high-fidelity screens yet
Any missing required foundations, undefined media style for sections depending on media, no reusable section components, untested component variants, or unverified breakpoints. For exploratory prototypes, label the output **wireframe/provisional** and avoid claiming it is a completed design-system-driven screen.

## Important operating distinctions
- Do not require illustration generation when a section calls for real product UI, photographic evidence, or a purposeful text-only composition. The **media decision and inventory** are mandatory; assets themselves depend on user/task need.
- If vector editability is required, produce editable Figma vector/source geometry, not a flattened raster.
- A beautiful screenshot is insufficient evidence of atomic composition. Count actual COMPONENT, COMPONENT_SET, INSTANCE and bound variable references.
- Iteration is non-linear: changing a screen can reveal a new component requirement, but return to the foundation/section kit and update dependent contracts before treating the revised screen as valid.
- Keep source-of-truth designs untouched unless explicitly asked to modify them.
