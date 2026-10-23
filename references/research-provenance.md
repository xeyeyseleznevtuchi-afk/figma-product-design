# Research provenance / source reliability

This skill is a synthesis; links below are **not** wholesale imported rules. A cited article can be opinion, not a standard. For each principle: record source URL, title, publication date when known, what it actually says, where the inference begins, scope, conflicting guidance and verification status. Unknown/undated is not invented.

## Directly verified primary sources (October 2026 review)
1. OpenAI, *Designing delightful frontends with GPT-5.4* (2026-03-20): https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4 — early constraints, content-first, mood boards, useful imagery, visual testing. **Adaptation**: marketing-first full-bleed hero and motion defaults are *not* universal requirements for admin interfaces or a brand extraction task.
2. Anthropic, *Harness design for long-running application development* (2026-03-24): https://www.anthropic.com/engineering/harness-design-long-running-apps — agent work quality requires execution environment, feedback and evaluation. **Adaptation**: QA checkpoints for Figma; article discusses coding agents, not a validated Figma design workflow.
3. Anthropic, *Frontend Design Skill*: https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md — intentional differentiation, subject-driven typography, useful UI copy, visual plan and critique. **Adaptation**: preserve visual system in maintenance tasks.
4. Figma, *Write to canvas*: https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/ — native design editing, components, variables, auto layout; beta limitations include image/font handling and manual review. **Normative for supported tool behavior, not evidence of quality**.
5. Figma, *Create skills*: https://developers.figma.com/docs/figma-mcp-server/create-skills/ — clear task-oriented frontmatter, steps, examples, edge cases; test on duplicated files.
6. DTCG, *Design Tokens Format Module 2025.10*: https://www.designtokens.org/TR/2025.10/format/ — typed JSON format, $value/$type, groups, references. IMPORTANT: final Community Group Report is not a W3C Recommendation; avoid the draft labeled *Do not implement*.
7. Nathan Curtis, *Documenting Components*: https://eightshapes.com/articles/documenting-components/ — documentation audiences, examples, architecture, usage and process.
8. Nathan Curtis, *I Made This, Does It Go In The System?*: https://eightshapes.com/articles/i-made-this-does-it-go-in-the-system/ — explicit acceptance criteria for library contributions; useful pattern does not automatically deserve global publication.

## Further primary corpus / follow-up reading (topic-level; do not claim exhaustive page-by-page verification)
- Figma MCP: https://developers.figma.com/docs/figma-mcp-server/structure-figma-file/ ; https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/ ; https://developers.figma.com/docs/figma-mcp-server/code-connect-integration/ . Read currently installed `figma-use`, `figma-generate-design`, `figma-generate-library` guidance before code writes; these can evolve independently.
- Brad Frost, *Atomic Design*: https://atomicdesign.bradfrost.com/ . Interpret atomic vocabulary as a mental model, not mandatory file structure.
- NN/g research library: https://www.nngroup.com/articles/ . Its home/list page is not a single article and cannot be cited as if every method has been verified. Consult specific studies on task analysis, IA, journey maps, user flows and usability testing when those methods are used.
- OpenAI Academy, *Design context and iteration with Codex*: https://academy.openai.com/en/public/clubs/champions-ecqup/videos/design-context-and-iteration-with-codex-2026-07-09 ; context is a persistence mechanism, not a guarantee of UI quality.
- Figma design skills and generated design references are tool-installed / version dependent. Do not assume a public URL reproduces the tool's current private implementation exactly.

## Conflicts and resolution
- OpenAI vivid marketing compositions vs enterprise work surfaces: choose task and established brand constraints first.
- Anthropic taste/novelty vs strict consistency: novelty for greenfield, conservative reuse for production maintenance.
- Atomic Design hierarchy vs component governance: reusable composition should be promoted based on actual product reuse and maintenance cost, not only depth or number of nested atoms.
- DTCG token JSON vs Figma variables: treat as two representations; design an explicit mapping and test data types and modes, never claim they are interchangeable.
- Beta `use_figma` success vs finished design: pass both API structural checks AND screenshot review.

## Review protocol
Every newly consulted source entry: status `primary-read | partial | catalog-only | not-accessible`, extract actionable claim in own words, add counterexample, then translate to a pass/fail test. Never state 'nothing omitted' without bounded, enumerated scope and checks.
