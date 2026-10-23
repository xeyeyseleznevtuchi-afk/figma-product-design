# Recovering from Figma MCP and Plugin API failures

## Core principle
A tool error does **not** prove a transaction was rolled back. A safety block does **not** authorize repeated attempts with rewritten scripts. Inspect current state before doing anything else.

## Failure categories
- **Preflight / permission / policy block**: do not retry in disguised form; report the constraint and stop writing until the cause is resolved through an authorized workflow.
- **API argument / font / node-type error**: stop the batch; use read-only inspection of exact target page and subtree; compare actual nodes to baseline; repair the smallest missing or invalid piece.
- **Timeout / unknown completion state**: assume partial success is possible. Inspect before retry, searching by stable IDs and unique deterministic names.
- **Partial component or variable construction**: retain valid previously created objects; never make duplicates on retry. Find by ID first, then by unique name within known scope.
- **Visual QA failure**: preserve master components and approved assets. Fix targeted layouts, then inspect screenshot again.

## Idempotent construction protocol
1. Record target file/page ID and a baseline inventory: child IDs, component masters, variables, bound node counts, and intended output IDs.
2. Split logically into foundations → component family → specimen instances → responsive screens → QA, with explicit outcome evidence from each successful phase.
3. Before creating a named page/section/component/variable, check whether it already exists in its scoped parent. Reuse or update; do not blindly append.
4. Load the exact font styles **before** text edits; use numeric font sizes and check arguments; set text width then auto-resize; measure resulting bounds.
5. Use the documented API signatures; isolate unsupported operations in a small non-destructive test before scaling.
6. Return IDs, counts, binding details and errors; inspect the actual document after failures.
7. Do not interpret successful JSON return as proof of visually valid output. Screenshot and structural review are separate gates.

## Handling failed operations
Capture: action, expected nodes, observed nodes, error class, whether mutation occurred, recovery decision and verification. Mark uncertain results NOT TESTED rather than PASS.

## Recovery acceptance test
- Create a disposable, uniquely named component in a sandbox.
- Intentionally simulate an API-argument failure in a *safe isolated test* before modifying approved content.
- Read document state and prove no duplicate component exists after a corrected retry.
- Demonstrate that an authorization/policy block causes a stop, not a workaround.
- Produce before/after inventory and final screenshot evidence.

This document is team process guidance, not a guarantee of Figma Plugin API transaction semantics.
