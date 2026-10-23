# Example: mass selection in a B2B search picker
Task: select multiple classification codes, apply to search, edit selection and handle empty results.
Roles: standard editor and read-only (permission behavior confirmed from brief).
Flow: entry from search → picker opened → search/type → select multiple → confirm → chips appear → remove/reopen → reset.
States: default, search pending, results, no results, selected, disabled apply, validation error, success; account for chip overflow (up to three rows if project specifies).
Build: inspect design-system picker, modal, search field, checkbox, tags, button, toast. Reuse exact instances. Arrange sequence left-to-right if team convention calls for it. Build only missing elements and document why. Screenshots compare type, spacing and actual final chip behavior.
