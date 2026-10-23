# Responsive composition and real-content constraints

## Required breakpoint matrix (choose based on context, not stock sizes)
- Define supported containers and min/max widths; identify where information priority changes.
- For each major screen test wide desktop, constrained desktop, mobile where in scope; use real text and data.
- Layout uses semantic nesting with auto-layout; set container direction, wrap, min/max, padding, gap, alignment, overflow and sizing **in valid order**. Do not treat absolute positions as responsive layout.
- Translation stress test: 1.5–2x text length, long unbroken string, mixed digits, empty value, multiline notes. Check text width/height and clipping; inspect visually at actual viewport.
- Tables: distinguish horizontal overflow, column hiding, record stacking and drill-down; never silently drop essential values or actions.
- For variable density: ensure essential controls remain discoverable at constrained widths; allow sensible reflow.
- Verify modal, drawer and menu positioning with focus/keyboard, long content and internal scrolling.
- A 400% zoom / reflow audit follows WCAG expectations for web; static Figma nodes alone cannot prove browser behavior.

Sources: https://developers.figma.com/docs/plugins/api/properties/nodes-layoutmode/ ; https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
