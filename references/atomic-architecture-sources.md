# Source review: artifact-first and Atomic Design

## Verified first-party readings
1. Brad Frost, Atomic Design chapter 2. Main claim: five levels; explicitly non-linear, whole and parts mutually inform each other. https://atomicdesign.bradfrost.com/chapter-2/
2. Nielsen Norman Group, Task Analysis. Tasks must be researched or assumptions labelled; decomposition into tasks/subtasks guides interface architecture. https://www.nngroup.com/articles/task-analysis/
3. Nielsen Norman Group, Wireflows. Combines wireframes and flowchart transitions for dynamic applications; documents states and interaction hotspots. https://www.nngroup.com/articles/wireflows/
4. Storybook, Why Storybook? Isolated component stories with mocked variants, then composition into pages. Translate to Figma as instance fixture boards, do not claim a Figma file *is* Storybook. https://storybook.js.org/docs/9/get-started/why-storybook
5. Storybook, simple component tutorial. Start with component's data and variation states, then build in isolation. https://storybook.js.org/tutorials/intro-to-storybook/react/en/simple-component
6. Figma, How to Build a Design System. Start with inventory and production alignment when possible; variables/styles/components support reuse. https://www.figma.com/blog/design-systems-102-how-to-build-your-design-system/
7. Figma, Tokens / variables / styles. Primitive/semantic/component-specific tiers; don't require component tier for small systems. https://help.figma.com/hc/en-us/articles/18490793776023-Update-1-Tokens-variables-and-styles
8. Figma, Explore component properties. Boolean/text/instance-swap/variant/slot controls; choose by actual consumer needs. https://help.figma.com/hc/en-us/articles/5579474826519-Explore-component-properties
9. Nathan Curtis, I Made This, Does It Go In The System? Not every pattern belongs in a central library; test reuse and vision fit. https://eightshapes.com/articles/i-made-this-does-it-go-in-the-system/

## Interpretation vs source
- An explicit A0–A8 artifact manifest, mandatory pre-screen gate, recommended Figma page structure and traceability matrix are **our process design** synthesized from sources; do not attribute them verbatim to any author.
- Atoms/molecules/organisms are **conceptual composition levels**, not mandatory separate Figma libraries.
- A Figma specimen of hover/loading state documents appearance; real behavior requires development/prototyping checks.
- Every stage may be revisited. Small edits reuse existing artifacts and do not need new ceremonial documentation.
