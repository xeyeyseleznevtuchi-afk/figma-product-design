# Example: multi-selection in a generic record picker
Task: select multiple items, apply the selection, modify it and handle empty results.
Roles: editor and read-only participant where relevant to the brief.
Flow: open selection → search → select multiple → confirm → selected items displayed → edit/remove → reset.
States: default, pending, populated, empty, selected, disabled action, validation error, success; include overflow behavior when specified.
Build: inspect picker, dialog, search field, checkbox, tag, button and feedback components in the active system. Use instances. Show transitions and document missing components. Validate long labels, localization and component states against screenshots.
