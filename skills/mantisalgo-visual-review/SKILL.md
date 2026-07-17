---
name: mantisalgo-visual-review
description: "Use when reviewing or designing the visual layer of a MantisAlgo product — chart aesthetics, palette, input UX, or marketing screenshots. Enforces the signature palette, color grammar, declutter cap, and the 3-asset marketing set."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [mantisalgo, ui, visual-review, palette, marketing-assets]
    related_skills: [mantisalgo-production-run]
---

# MantisAlgo Visual Review

## Overview

Buyers can't read code — screenshots and first impressions are half the purchase decision. The factory already has a visual layer (visual director, declutter tests, `output/sku_visual_review.html`); this skill is the sign-off workflow that defends its standards. Full standards: `Desktop/dev/MantisAlgo/hermes/ui.md`.

## When to Use

- A product reaches step 4 of the production flow (visual review)
- Palette or color-grammar decisions
- Producing marketing screenshots for a SKU

Don't use for: implementing indicator logic (development), writing sales copy text (idea).

## Review Workflow

1. **Palette & color grammar.** One signature palette across all SKUs. Bull/bear/neutral roles are fixed and never remapped per product. Done when: every color on screen maps to its fixed role.
2. **Default-settings render.** Load the product with defaults only. Done when: the default chart is marketing-grade without tweaking. If it only looks good after tweaking, the defaults are the defect.
3. **Dark/light check.** Dark chart is default; verify readability on both. Done when: both themes pass.
4. **Declutter cap.** Count on-screen elements at defaults. A 20-line Christmas-tree chart is a defect. Done when: element count is within the cap tied to `tests/test_visual_declutter.py`.
5. **Overlay vs pane.** Same units as price → overlay; otherwise pane. Labels/tables/background highlights all have on/off inputs, restrained defaults.
6. **Input UX.** `input.*` grouped core → visual → advanced; tooltip on every input (the settings panel is also UI — no manual needed). Done when: zero tooltip-less inputs.
7. **Report.** Regenerate/inspect `output/sku_visual_review.html`. Done when: zero findings.

## Marketing Assets (per SKU)

- 2 default-setting screenshots: context shot + signal close-up
- 1 benchmark comparison shot
- Use the unified symbol/timeframe presets for consistency across the product line.

Done when: 3 assets saved and referenced by the SKU.

## Common Pitfalls

1. Approving a chart that needed manual tweaks to look good.
2. Remapping bull/bear colors "just for this product" — brand consistency is product-line trust.
3. Decoration creep — every added element must earn its place.
4. Checking dark mode only.
5. Treating UI as a sub-task of development instead of an independent pass bar.

## Verification Checklist

- [ ] Signature palette + fixed color roles respected
- [ ] Marketing-grade at default settings, dark AND light
- [ ] Declutter cap respected; visual tests green
- [ ] Every input grouped and tooltipped
- [ ] `sku_visual_review.html` zero findings; 3 marketing assets secured
- [ ] Verdict logged to `/memory.md`
