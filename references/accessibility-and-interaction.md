# Accessible UX acceptance (WCAG-aligned, not compliance certification)

## Design-stage checks
- Contrast: normal text 4.5:1, large text 3:1 under WCAG AA, except applicable exceptions; non-text UI boundaries/meaningful graphical objects 3:1. Calculate from actual foreground/background including overlays.
- Keyboard: logical order, meaningful labels, visible focus, avoid keyboard traps, escape/close where appropriate. Focus Appearance 2.4.13 is **AAA**, not AA; focus visible 2.4.7 is AA.
- Pointer targets: WCAG 2.2 AA 2.5.8 is minimum 24x24 CSS px with exceptions; 2.5.5 44x44 is AAA; use generous targets in practice without mislabelling a recommendation as criterion.
- Status/error: locate errors beside fields, give repair path; do not rely on color alone; announce asynchronous changes in implementation handoff.
- State contract: default, hover, focus, pressed/selected, disabled, loading, success, validation error, empty, offline where relevant.
- Motion: no essential information conveyed solely by animation; provide reduced-motion treatment and avoid flicker.
- If design-level evidence cannot establish DOM semantics, screen-reader announcements, responsive browser behavior or focus mechanics, mark **requires implementation test**, never say WCAG compliant.

Sources: https://www.w3.org/TR/WCAG22/ ; https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance ; https://designsystem.digital.gov/components/
