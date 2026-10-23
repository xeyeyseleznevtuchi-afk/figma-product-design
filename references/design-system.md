# Design system architecture, creation and governance
## From scratch
Start from the minimum screen and flow inventory. Define primitive scales (colors, number/spacing, radius, sizes, typography), semantic roles (surface, text, border, action, status), relevant modes (light/dark/brand/contrast only when demanded), and component-level aliases where helpful. Reuse existing style/tokens before creating new ones; brand kit and product UI system are different deliverables.

Prefer interoperable DTCG concepts for exported tokens but match current Figma capabilities: typed values, semantic aliases, modes, stable naming; avoid representing the DTCG report as an official W3C standard. Use code syntax mapping only if real code names exist; never fabricate production variable names.

## Components
- Identify candidate from repeated demand and shared tasks. Test using the Curtis contribution lens: cross-product reuse, system vision, cost, future direction, documented guidance and timing.
- Create foundations first, then primitives, composite controls and complex patterns in dependency order.
- Properties: TEXT for editable labels, BOOLEAN for optional elements, INSTANCE_SWAP for icons and compatible slots, VARIANT for meaningful size/style/state axes. Avoid Cartesian variant explosion; favor composition and smaller component families.
- Build component states grounded in UX requirements; disabled ≠ loading; hover/focus/selected/error need intentional distinctions. Include large/translated label tests.
- Keep main components separate from specimen instances. Document purpose, when-not-to-use, anatomy, properties, variants, behavior, content, accessibility and examples for designers/developers/QA.
- Prefer functional composition: a reusable data-grid cell/row/pagination is better than a huge inflexible one-off entire table if demands vary.
- Avoid preemptive full component catalog for a young system. Keep a proposed-only backlog.

## Figma implementation
Follow official `figma-use` and `figma-generate-library` instructions for font loading, variable scopes, aliasing, `setBoundVariable`, styles, library discovery, page context, ID returns and retry safety. Local variable collection empty does NOT imply no remote variables. Discover libraries and existing screen instances before recreating components. Never detach imported components by default.

## System maintenance
Version breaking changes, distinguish deprecation from deletion, keep adoption/use examples, and document provenance. On reconciliation preserve node IDs/bindings where feasible and validate dependents. Think of the design system as a product serving multiple product teams, not a one-time static page.
