# figma-product-design 2.0
A skill workflow for designing from scratch, design systems, scoped Figma edits, brand kits and QA. Documentation is in `SKILL.md`; source evidence/limitations in `references/source-review.md`.

Install into `~/.claude/skills/figma-product-design` for Claude Code and `~/.agents/skills/figma-product-design` for Codex. **Backup v1 before replacement**. Requires a Figma MCP connection for actual canvas writing. Loading the skill does not install or authenticate Figma MCP.

Validation: `python3 scripts/validate-package.py`. No actual Figma build is implied by this validator.

## v2.2 deep-engineering update
Adds six focused reference files for component contracts, responsive content, accessible interaction, Figma transaction safety, evidence provenance, and release QA scorecard. This is a methodology update, not proof of successful real-world Figma design.
