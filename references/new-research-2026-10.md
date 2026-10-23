# Research addendum: artifacts, contracts and predictable composition (23 Oct 2026)

These links are direct original documentation or author materials. The implementation guidance in this project is a synthesis, not a claim that every author mandates our artifact gate.

1. Nathan Curtis, **Component Specifications** (2023). Detailed specs are valuable for scaling design-system delivery; turn anatomy, behavior, responsive usage and handoff criteria into component contract fields. https://nathanacurtis.substack.com/p/component-specifications-1492ca4c94c
2. NN/g, **Wireflows** (2016). Wireframes+flowcharts for interactive applications; create screen-and-transition artifacts prior to committing to full visual design. https://www.nngroup.com/articles/wireflows/
3. Storybook, **How to write stories**. Stories are component states parameterized by args; translate into Figma fixture instances. https://storybook.js.org/docs/8/writing-stories/index
4. Storybook, **Interaction testing**. Simulated interactions + assertions validate transitions in running code. Do not claim static Figma proves behavior. https://storybook.js.org/docs/9/writing-tests/interaction-testing
5. Figma, **Design Systems 102**. Shared semantics in names, styles, component properties and code handoff. https://www.figma.com/blog/design-systems-102-how-to-build-your-design-system/
6. Figma, **Design tokens: sync design and code**. Named reusable decisions and consistent reference/binding strategy. https://www.figma.com/resource-library/design-tokens/
7. DTCG, **Format Module 2025.10**. Platform-neutral token serialization; format is a Community Group specification, not a W3C Recommendation. https://www.designtokens.org/TR/2025.10/format/
8. Figma, **Guide to variables**. Verify actual variable usage/modes in designs; creating variables alone is not a working token system. https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma

## Research-to-rule translation
- Source-backed: parameterized state specimens; explicit component specifications; flow/screen combined artifacts; semantic reusable values.
- Team-created: stable contract IDs, mandatory artifact-first gate, provenance statuses, dependency-led regeneration and PASS/FAIL/NOT TESTED releases.
- Limits: Atomic Design is non-linear; Figma prototypes ≠ runtime interaction verification; visual repeatability ≠ pixel determinism; DTCG token JSON ≠ automatic synchronization into Figma variables.
