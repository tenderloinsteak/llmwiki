---
name: mantis-ui-module-update
description: "Add a new UI-kind module or change an existing one in the MantisAlgo Pine Script factory (dashboards, legends, gauges, color grammar, display toggles — anything in generators/families/ui/ or tagged \"kind\": \"ui\" in registry.json). Use whenever 곽경준 says 'UI모듈 업데이트', 'UI모듈 추가/수정해줘', '대시보드 추가해줘', '패널 만들어줘' in the MantisAlgo project. Ends by linting the change and, if the llmwiki folder is reachable, syncing it into the knowledge wiki automatically. For a read-only check with no code changes, use mantis-ui-module-lint instead."
license: MIT
metadata:
  mantisalgo:
    tags: [pine-script, ui, module-registry, factory]
    related_skills: [mantis-ui-module-lint, mantis-strategy-module-update, mantis-strategy-module-lint]
    cursor_command: ui-module-update
---

# MantisAlgo — UI Module Update

## Overview

Walks the add/change workflow for a **ui**-kind module: something that changes what a buyer sees on the chart (a panel, a legend, a gauge, a color scheme, a display toggle) rather than what the factory calculates. UI is the top sales lever here — `hermes/ui.md` states it outranks raw performance for indicators, since buyers judge by screenshot first. This skill exists so that standard is followed mechanically every time, not just remembered.

## When to Use

- "UI모듈 업데이트/추가/수정해줘", "대시보드/패널/범례 만들어줘"
- Any direct edit to a file under `generators/families/ui/`, or to a module whose `registry.json` entry has `"kind": "ui"`

Not for read-only checks (`mantis-ui-module-lint`) or logic/analysis modules (`mantis-strategy-module-update`).

## Workflow

1. **Design against the UI contract, not just the feature.** Every input needs `group=` and a Korean `tooltip=`. Color roles come from the signature palette only: bull = `color.teal`, bear = `color.orange`, neutral = `color.gray` (fixed 2026-07-16, see `hermes/ui.md`) — don't introduce a new hue without a strong reason. Anything that adds visual clutter beyond the module's core purpose (an extra background wash, an optional marker) must default to **off** behind its own `input.bool(false, ...)` or an existing `showTier*`/`show*` gate — this is the single most common way a "Christmas-tree chart" anti-pattern creeps in.

2. **Write or edit the generator.** New modules go in `generators/families/ui/<module_id>.py`, one `gen_<module_id>(ctx: GenContext) -> str` function using `sec()` for the section header. Look at a recent example before writing your own — `generators/families/ui/ui_perf_stats_panel.py` (a `table.new` stats panel) and `generators/families/ui/ui_signal_legend.py` (a static legend built from which sibling modules are enabled) are good templates for "reads other modules' state" vs "self-contained" UI modules respectively.

3. **Register it.** Add the import + `REGISTRY` dict entry in `generators/families/ui/__init__.py`. The router (`generators/router.py`) picks up every family's `REGISTRY` automatically — nothing else to wire.

4. **Add the registry.json entry.** In `config/module_registry/registry.json`, append an object: `id`, `family` (usually `"ui"`), `status: "live"`, `est_lines` (rough line count), `depends_on` (list any module id it reads state from, e.g. `sig_confluence_score` if it reports on confluence signals), `description` (one Korean line — this is what shows up in the wiki), `kind: "ui"`.

5. **Lint it standalone**: `python3 scripts/module_lint.py --module <module_id>`. Fix anything that comes back `[FAIL]` before moving on.

6. **Decide where it ships.** If it should appear in a product, add its id to that SKU's feature list — either `SKU_BASE_FEATURES` in `module_registry.py` or the SKU's `config/product_skus/SKU-XX.json` `features` array. If it's experimental, a one-off smoke idea (pattern in `tests/test_new_modules_smoke.py`) is enough to prove it assembles cleanly without shipping it anywhere yet.

7. **Verify at factory level**: `python3 scripts/factory_gate.py`. This re-checks every shipping SKU (compile-safety + the UI audit) — a module that's clean alone can still crowd a chart once assembled next to everything else in a platform SKU.

8. **Regenerate what changed**: if a shipping SKU picked up the module, `python3 scripts/regenerate_sku_factory.py` (writes the `.pine` file), then `python3 scripts/visual_sku_review.py` (refreshes `output/sku_visual_review.html` so the visual diff is easy to eyeball).

9. **Sync the knowledge wiki — do this without asking, if reachable.** MantisAlgo's registry has a mirror in the llmwiki knowledge base (`~/Desktop/dev/llmwiki/wiki/modules/`). If that folder is accessible in this session:
   - Run `python3 ~/Desktop/dev/llmwiki/hermes/scripts/registry_to_wiki.py` — it reads `registry.json` fresh and regenerates every module page + the `modules-map` hub. This is the **only** way module changes reach the wiki; nothing does it automatically (no file watcher, no git hook — it's a plain script that has to be run).
   - Append one line to `~//memory.md` in the existing format: `date | factory-module-developer | what changed | next`.
   - If the folder is **not** reachable (not mounted/connected in this session), say so plainly instead of silently skipping it — the wiki will drift out of sync with the registry until someone runs the sync script.

## Common Pitfalls

- Forgetting `kind: "ui"` on the new registry entry — it'll default to `"logic"` and throw off the ui/logic split's accuracy.
- Adding a visual that's on by default "just this once" — `hermes/ui.md`'s declutter cap exists precisely because every module's author thinks their one addition is the exception.
- Hand-editing `wiki/modules/*.md` instead of running `registry_to_wiki.py` — those pages say "AUTO-GENERATED, do not hand-edit" for a reason; the next sync overwrites manual changes silently.
