# Acceptance and QA gates
## Hard failures (block completion)
- Wrong source file/page, unauthorized mutation, missing agreed scenario/section, invented approved brand facts.
- Flat screenshot masquerading as editable design; broken/detached components when expected to be linked.
- Cropped, overlaid, invisible or unreadable important text; incorrect font family; placeholder content where source provides actual text; missing original assets.
- Missing key decision/error/loading state in an agreed flow; unusable fundamental task or unaddressed permission problem.

## Major issues (fix before handoff)
- Inconsistent spacing/type scale/color roles, unsupported variants, wrong density, visually incoherent layout, responsive overflow, insufficient contrast, accessibility concerns, inconsistent terminology, too much decoration or filler.
- Repeated one-off UI instead of instances when component was available.

## Review sequence
1. Structural: inventory node types, names, hierarchy, Auto Layout, variants, components, variables, dimensions, affected IDs.
2. Content: title/copy/link accuracy, localized long text, number formats, empty and error copy.
3. Visual: screenshot in context at practical scale for every representative template/state; detect cropped title, accidental overlaps, hierarchy, contrast, alignment, shadows, brand graphic fidelity and white space.
4. Functional: check main/alternative task paths, accessible focus, keyboard, target sizes where relevant; do not claim working prototype unless prototype actually set and tested.
5. Regression: existing approved frames/screens unchanged unless scope permits.
6. Rate severities; fix blocker/major; document minor residual issues with exact affected nodes, owner and proposal.
7. Reinspect after fixes. Successful script execution is NOT proof of screenshot acceptance.

## Definition of done
No unresolved hard/major issues in scoped screens and components; relevant screenshots inspected; original designs preserved; truthful direct link; no extrapolated claims. If access or validation impossible, state PARTIAL.
