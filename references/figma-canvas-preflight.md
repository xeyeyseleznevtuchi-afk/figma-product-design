# Figma canvas execution: transaction preflight and postflight

## Mandatory before every mutation batch
1. Confirm target file, page ID, intended section/frame ID and allowed mutation set. Never assume page context persists across calls.
2. Inspect affected subtree and identify component owners/instances; check locked/remote styles, local vs published variables, fonts.
3. Use canonical `figma-use` font-load recipe for **current** font family/styles before any text-related edit. Do not assume Inter or auto-load.
4. Decide retry recovery: if an error can happen after mutation, read canvas before reattempt. Track precise returned node IDs.
5. Compose a wrapper/container first and children inside it; respect required context before FILL/HUG; resizing may reset sizing mode.
6. For batch edits, only modify vetted nodes; do not recursively repaint entire page without examining token/binding provenance.

## Structural assertions after mutation
- Every intended node exists once, correct type, parent, page and width/height >0.
- Every expected variant/property exists with valid owner; variables correctly bound; no detached instances unless intended.
- Text is not fixed to a line-height of 25px regardless of font size. Inspect actual height vs content, multilingual overflow, line height and clipping. Successful API call is not proof.
- Check fill and text style bindings, correct font, image nodes, vector originals and screen composition screenshot.
- Existing approved sections have unchanged IDs/properties where required.
- Screenshot at useful resolution, correct actual defects and screenshot after repair. Do not claim reviewed if no usable image inspected.

## Explicit failure cases from Metamentor
- A function created `textAutoResize = HEIGHT` before `resize()`, causing `resize()` to reset text fitting: correct order is resize then autoResize and verify returned height.
- Font-load failures can halt a script after partial mutations; read state and retry only missing operations.
- Bulk substitutions must not alter every bound variable or unrelated branded asset; change scoped semantic role and verify use sites.
- Do not invent applications and present them as approved brand guidelines.

Source: https://developers.figma.com/docs/plugins/api/properties/nodes-layoutmode/ and installed `figma-use` documentation.
