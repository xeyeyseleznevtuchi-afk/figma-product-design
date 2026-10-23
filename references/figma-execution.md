# Native Figma execution contract
Prerequisite: load official Figma use skill before writing. `figma-generate-design` for screens and `figma-generate-library` for reusable components. Read actual available API schemas, not remembered examples.

1. Inspect target file and relevant existing pages, asset IDs, fonts, components, styles, local AND linked variables. For code-first work inspect source component definitions/Code Connect when available.
2. Record IDs and selected page explicitly. Respect single-page-context-per-script guidance and supported Figma API. Do not mutate other pages.
3. Create an Auto Layout wrapper first and build children inside it; use x/y to place top-level structures, not to lay out relational content.
4. Typography: verify real font availability, `await figma.loadFontAsync` BEFORE mutations, set textAutoResize intentionally, size text frames to actual content, read back after mutation. A fixed 25-pixel text height for a 56px title is a critical defect.
5. Read component property names, import master and instantiate, prefer setProperties and INSTANCE_SWAP rather than hand-drawn replacements.
6. Use variables for available semantic fills, strokes, gaps and radii; preserve modes and scopes. Avoid hard-coded values when existing tokens cover property.
7. Use source SVG for icons, original logo assets or existing library icons. Avoid manual primitive imitation or fabricated logos.
8. Return ALL created/mutated node IDs, section counts, dimensions and any error. On failures, check canvas state before retry unless error explicitly safe to retry.
9. Capture composition screenshots after meaningful build phases, inspect at readable scale; follow with targeted fixes and one post-fix check. Do not overrun huge canvases without staged inspection.
10. Final pass: native editability, no full-UI raster, no clipped text, no overflow, no mistaken fonts, no orphan nodes, no destructive changes, accurate links.

Read Figma MCP docs dynamically: https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/ and https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/ . This file describes quality obligations, not a substitute API spec.
