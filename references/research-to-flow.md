# Discovery and UX architecture: design from evidence

## Inputs
Product outcome, audience and permissions; jobs-to-be-done; data entities, actions, audit trail, frequency, devices, operating constraints, accessibility and locale. Where no user research exists, mark hypothesis; do NOT invent interviews, statistics, personas or usage evidence.

## Task → information → workflow
1. Write task statements with measurable completion conditions. Distinguish new vs expert user.
2. Inventory entities and relations; map lifecycle/status and destructive operations.
3. Define IA: global nav vs local nav, naming by users' vocabulary, ownership of records, search/filter taxonomy.
4. Map primary success flow, alternative branch, empty, loading, partial success, conflict, rejected permissions, offline/error, confirmation and recovery.
5. Define screen/state matrix and realistic content before hi-fi. Add evidence link to source requirement for each unusual rule.
6. Validate with task walkthrough and 3–5 representative test cases before declaring architecture sound. Do not claim empirical usability testing if none occurred.

## SaaS / B2B density
Show records, statuses, filters, bulk actions and data ownership directly. Avoid forced marketing hero narratives. Prefer progressive disclosure over hiding critical controls. Plan keyboard reach, focus, sorting, search clear, pagination state, unsaved changes, and async feedback.

## Gate
Fail if essential action lacks start/end, if destructive actions lack outcome handling, if the interface uses unexplained domain jargon, or if real content constraints were not checked.
