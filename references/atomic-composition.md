# Atomic composition and component-driven Figma architecture

## Canonical model
Brad Frost: **atoms → molecules → organisms → templates → pages** are conceptual levels, **not** a literal five-step linear production order, universal naming convention, or requirement that every nested element be a published Figma component.

- **Foundations/tokens (cross-cutting):** semantic colors, type, space, sizes, radii, effects, modes. Tokens are not automatically UI atoms.
- **Atoms:** indivisible functional UI controls/elements in a given scope: text label, icon, button, field, checkbox, badge.
- **Molecules:** small single-purpose combinations: search field with label and action, filter chip group, form row.
- **Organisms:** composed product regions: application sidebar, search toolbar, data table with toolbar, form panel.
- **Templates:** layout/content structure and responsive behavior without pretending final representative data exists.
- **Pages/screens:** templates instantiated with representative content and realistic scenarios/states to validate resilience.

## Structure rules in Figma
1. Inventory components needed by user tasks before library work, mapping each to a consumer screen and expected reuse; no speculative huge library.
2. For each reusable atom/molecule/organism create a master ComponentNode or ComponentSetNode; document a contract covering purpose, input/content, slots, properties, states, dimensions, constraints, accessibility intent and usage examples.
3. Compose **instances**, preserving main-component links. Use nested instance swaps/slots where actually appropriate, and avoid detach-and-copy patterns.
4. Visual variants must be actual variants with a ComponentSet where requested, not independent named layers masquerading as a variant family.
5. Publish semantic variables and bind actual component paints/typography/spacing when supported; report bound nodes separate from declared variable counts.
6. Create isolated specimens for default/hover/focus/disabled/loading/empty/error when applicable, following Storybook's stories-as-variations concept. Note static Figma specimens are not proof of actual interactive behavior.
7. Organisms should be assembled out of smaller components; if a region is uniquely coupled to one screen, local composition may remain a frame until reuse justifies a published component.
8. Use content-driven, realistic fixture values. Contrast and responsive test each context and long strings. Trace page defects to owning master/token instead of patching each instance.

## Domain-neutral traceability example
Task: locate and inspect a record → wireflow: collection → query and filters → record details → complete action or recover from failure.
Atoms: button, input, checkbox, status indicator, label.
Molecules: labeled search, filter selection, sortable column header.
Organisms: filter toolbar, data collection, detail panel.
Template: collection workspace with responsive content zones and rules.
Pages: populated collection, empty search result, loading, permission error, long record title.
Any published component needs a demonstrated screen or pattern consumer.

## Anti-patterns
- Building the whole screen from raw rectangles/text without masters.
- Naming arbitrary groups 'organisms' without defining their contract/reuse.
- Creating token names with no actual binding.
- Treating atomic taxonomy as UI file-folder law; composing bottom-up blindly with no task/content model.
- Creating full patterns from screenshots and claiming editability.
- Over-componentization: evaluate future use, coherence, burden and dependency cost.

## References
- Brad Frost https://atomicdesign.bradfrost.com/chapter-2/
- Storybook https://storybook.js.org/docs/9/get-started/why-storybook
- Storybook example https://storybook.js.org/tutorials/intro-to-storybook/react/en/simple-component
- Nathan Curtis https://eightshapes.com/articles/i-made-this-does-it-go-in-the-system/
- Figma component props https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties
- Figma developer component props https://developers.figma.com/docs/plugins/working-with-component-properties/
