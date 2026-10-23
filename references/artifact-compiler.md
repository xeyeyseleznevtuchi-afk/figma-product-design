# Artifact compiler: deterministic design assembly contract

## Goal
Turn user goals and evidence into *inspectable, versioned* contracts which govern actual Figma execution. These are team-designed conventions informed by Atomic Design, wireflows, component specifications, stories and design-token specifications. Do not attribute this compiler to those authors.

## Domain-neutral manifest
Maintain a single source-of-truth manifest for each project:
- artifact ID, kind, revision, status (proposed/reviewed/approved), owner, provenance and artifact file/Figma node ID
- references: dependsOn IDs, consumedBy IDs, impactedBy changes, validation fixture IDs
- build fingerprint: normalized contract fields, component/variable references, viewport, fixture seed
- missing/unknown claims flagged separately from confirmed requirements

Kinds: PRODUCT, ENTITY, TASK, FLOW, SCREEN, CONTENT, VISUAL, TOKEN, COMPONENT, PATTERN, TEMPLATE, FIXTURE, QA.
Use structured schema rather than free-form language when generating repeatably.

## Preflight compiler: 7 gates
1. Contract schema valid: required IDs, types, status and dependencies.
2. References resolve; no dangling tokens/component IDs; detect accidental cyclic *construction* dependencies. A screen–component usage graph can be many-to-many.
3. Each planned SCREEN maps to a FLOW (or explicit static-content exception), CONTENT contract, TEMPLATE, fixtures and viewport definitions.
4. Each COMPONENT maps to its consumers, anatomy, variant axes, typed props, content bounds and fixtures.
5. TOKEN values/type/mode/semantic role are valid; actual rendered-bound-variable evidence is separate from declaration.
6. Approved/reviewed decisions override suggestions; unresolved blockers prevent claiming validated production build.
7. Generate change plan and acceptance criteria; never silently invent new UI patterns during screen assembly.

## Two-pass generation
**Pass A — architecture**: derive minimum required atoms/molecules/organisms from task/screen content demand, document component contracts and appearance/interaction constraints. Instantiate isolated specimens for key states. Review and adjust through realistic data.
**Pass B — rendering**: build responsive templates and populated screens using approved master instances, bound semantic tokens and stable data fixtures. Deviations must generate a contract change proposal.

Brad Frost's atomic stages are conceptual and non-linear: the gates protect traceability, but composition may reveal new needs that revise earlier contracts.

## Predictability test
Run the same artifact bundle in **two isolated Figma files**, not repeatedly on a mutated canvas. Compare:
- contract coverage (screen/state IDs), unresolved assumptions
- variable names, types and actual bound-node ratios
- main-component/variant/instance topology
- screen node hierarchy by semantic path (exclude unstable generated Figma IDs)
- viewports and text-overflow failures
- screenshots and visual discrepancy categories

The output is structurally reproducible, not expected to be pixel-identical across changing renderer/font versions. Record both versions and screenshots. Never claim convergence without a measured baseline.

## Change impact analysis
Trace changed IDs outward through reverse dependency edges. Rebuild the smallest affected component masters/templates/screens; preserve approved unrelated nodes. Re-run fixtures from the affected dependency cone. Report unchanged vs changed contract fingerprints.

## Hard-stop criteria
- Screen-first build with no inspectable architecture artifact in complex greenfield work
- reusable component copied as detached primitives despite compatible master
- token collection created with zero actual expected render bindings
- generated screen lacking source contract IDs or state fixture evidence
- broken references, unresolved required rules, missing viewport screenshot
- unsupported claims about runtime behavior from static Figma

Primary sources:
https://atomicdesign.bradfrost.com/chapter-2/
https://www.nngroup.com/articles/wireflows/
https://nathanacurtis.substack.com/p/component-specifications-1492ca4c94c
https://storybook.js.org/docs/9/writing-tests/interaction-testing
https://www.designtokens.org/TR/2025.10/format/
