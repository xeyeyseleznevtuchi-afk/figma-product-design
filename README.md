# figma-product-design v2.3
A skill workflow for designing from scratch, design systems, scoped Figma edits, brand kits and QA. Documentation is in `SKILL.md`; source evidence/limitations in `references/source-review.md`.

Install into `~/.claude/skills/figma-product-design` for Claude Code and `~/.agents/skills/figma-product-design` for Codex. **Backup v1 before replacement**. Requires a Figma MCP connection for actual canvas writing. Loading the skill does not install or authenticate Figma MCP.

Validation: `python3 scripts/validate-package.py`. No actual Figma build is implied by this validator.

## v2.2 deep-engineering update
Adds six focused reference files for component contracts, responsive content, accessible interaction, Figma transaction safety, evidence provenance, and release QA scorecard. This is a methodology update, not proof of successful real-world Figma design.

## v2.3 recovery and integration QA
- `references/recovery-protocol.md`: classifies errors, forbids policy-block workarounds, requires state inspection before retry, and describes idempotent recovery.
- `references/token-and-variant-regression.md`: audit true token bindings, component sets/instances, responsive screenshots and honest PASS/FAIL/NOT TESTED evidence.
- October 2026 sandbox baseline: **6 variables created, 0 verified bound nodes, desktop screen only**. v2.3 documents regression tests; it has not passed them yet.
