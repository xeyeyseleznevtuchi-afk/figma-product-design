# Product discovery and UX architecture
1. Clarify user segments and permission models, goals, top tasks, jobs, business constraints, platform, data volume, accessibility and success measures. Distinguish facts and hypotheses.
2. Inventory entities and relationships, IA navigation model, routes, key tasks and cross-channel touchpoints.
3. Use journey map for multi-channel, temporal holistic experiences; user flow for discrete task interactions inside product. Avoid conflating the two.
4. For each important task, write trigger, prerequisites, entry, main path, alternate path, permissions, validation, recovery, exit and persistence.
5. Produce screens/state matrix with default, hover/focus where relevant, selected, loading/skeleton, empty, partial, permission denied, invalid/error, success, offline and long-content states as appropriate. Do not insist all states apply everywhere.
6. For B2B: check high-density tables, sorting, column overflow, bulk actions, mass selections, search syntax/filter chips, async processing, multiple user roles, audit trails, undo and large datasets.
7. Prioritize core path and highest-risk exceptions for v1; every screen must map to a user need, not decorative coverage.
8. If no user research exists, mark design hypotheses; propose validation tasks rather than asserting user desirability.

Deliverables: problem framing, role matrix, IA, flow diagrams/wireflows, state matrix, prioritized screen inventory. Use `templates/design-brief.md` and `templates/state-matrix.md`.
