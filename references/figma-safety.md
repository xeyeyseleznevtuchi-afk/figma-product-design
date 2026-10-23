# Figma MCP safe edit contract

1. Before `use_figma` load latest official `figma-use`; for screens also `figma-generate-design`, components and variables `figma-generate-library`. Do not assume generic Figma API examples run unchanged in this environment.
2. Return all created/mutated node IDs, counts and bounds. Mark exact target page and protected source IDs; preserve all other pages.
3. Fonts: `await figma.loadFontAsync` for exact current fonts BEFORE text/appendChild/auto-resize mutation. Use getStyledTextSegments for mixed text; never assume Inter fallback or guessed font style spelling.
4. Text: explicit meaningful width; verify `textAutoResize`, glyph height and overflow after creation. Setting fontSize does NOT guarantee glyph bounds update.
5. Container hierarchy: create wrapper first, use Auto Layout for meaningful relation, set FILL only after appended to compatible parent; resize BEFORE sizing mode finalization.
6. Variables: inspect local plus published sources; bind fills/strokes/padding/radius to correct scope; a successful search for style does not prove it is linked to the current file.
7. Source media: copy original logo/vector, not synthesize; when media unavailable, mark unresolved rather than falsely claiming brand consistency. Do not flatten screens to raster.
8. Failure: inspect page to determine partial mutations before retry; retries should be idempotent and non-destructive. Remove by verified IDs, not approximate name prefixes.
9. Screenshot after composition at legible zoom. Compare to source, scan clipping, hierarchy, blank assets and off-canvas placement. Screenshot alone never verifies interactions.
10. Final report: links to page/nodes, verified count, QA defects fixed, constraints, unresolved asset questions. Beta tool success does not equal design approval.
