---
name: mantis-strategy-module-update
description: "Add a new logic-kind module or change an existing one in the MantisAlgo Pine Script factory (structure, momentum, volume, session, pattern, quant, execution, imbalance, liquidity, blocks, signal — 곽경준's '전략모듈'; used by both indicators and strategies). Use whenever 곽경준 says '전략모듈 업데이트', '전략모듈 추가/수정해줘', '로직 모듈 만들어줘', 'oo 지표/시그널 추가해줘' in the MantisAlgo project. Ends by smoke-assembling the module and, if the llmwiki folder is reachable, syncing it into the knowledge wiki automatically. For a read-only check with no code changes, use mantis-strategy-module-lint instead."
license: MIT
metadata:
  mantisalgo:
    tags: [pine-script, logic, strategy, module-registry, factory]
    related_skills: [mantis-strategy-module-lint, mantis-ui-module-update, mantis-ui-module-lint]
    cursor_command: strategy-module-update
---

# MantisAlgo — Strategy/Logic Module Update

## Overview

Walks the add/change workflow for a **logic**-kind module — the analysis and signal engines that sit underneath the UI: structure (`struct_*`), momentum (`mt_*`), volume (`vol_*`), session (`sess_*`), pattern (`pat_*`), quant (`qx_*`), execution (`exec_*`), imbalance (`imb_*`), liquidity (`liq_*`), blocks (`block_*`), signal (`sig_*`), plus the generic `premium` toggles (`risk`, `alerts`, `filters`, `staged_signals`). 134 of the 173 registered modules as of 2026-07-17.

Naming note: 곽경준 calls this family "전략모듈", but it's broader than Pine `strategy()` scripts — the same structure/momentum/volume analysis feeds pure indicators too. Only `exec_*` and `risk` actually place or size orders. If the intent is narrower ("just order-placement modules"), scope the work to `exec_*` and say so.

## When to Use

- "전략모듈 업데이트/추가/수정해줘", "로직 모듈 만들어줘", a request for a new signal/pattern/filter that isn't purely visual

Not for read-only checks (`mantis-strategy-module-lint`) or UI/display modules (`mantis-ui-module-update`).

## Workflow

1. **Ground the idea in theory, not just novelty.** Per `context_prompting.py`'s theory contract for indicators: state the market mechanism being exploited (why it works), the exact math, and where it degrades (failure modes/regimes). This applies to a hand-written module too, not just LLM-generated ideas — a module nobody can explain the "why" of is a liability, even if it looks good.

2. **Write or edit the generator.** New modules go in `generators/families/<family>/<module_id>.py` (family = the prefix group above), one `gen_<module_id>(ctx: GenContext) -> str` function using `sec()` for the section header. Recent examples to copy the shape of: `generators/families/momentum/mt_squeeze_detector.py` (self-contained calculation + markers) and `generators/families/volume/vol_obv_divergence.py` (dual-series comparison via `ta.valuewhen`). Any input the module defines still needs `group=`/`tooltip=` — logic modules aren't exempt from the UI contract just because their main job is calculation.

3. **Register it.** Add the import + `REGISTRY` dict entry in `generators/families/<family>/__init__.py`. `generators/router.py` picks up every family automatically.

4. **Add the registry.json entry.** `id`, `family`, `status: "live"`, `est_lines`, `depends_on` (real dependencies — e.g. anything reading `structMarkBull`/`structMarkBear` depends on `struct_market_bos_choch`), `description` (one Korean line), `kind: "logic"`.

5. **Check the `ta.*` whitelist before you rely on a function.** `pipeline.py`'s `_VALID_TA_FUNCTIONS` (extended by `verify_v2.py`'s `_EXTRA_VALID_TA`) is the full list of Pine v6 `ta.*` calls the gate accepts — anything else gets flagged as hallucinated. If you're using a real v6 function that's missing from the list, add it there rather than working around the gate.

6. **Smoke-assemble it.** A module is a code snippet, not a compilable script — full Pine syntax/reference checking only happens once it's assembled. Follow the pattern in `tests/test_new_modules_smoke.py`: build a minimal `PremiumIdea` with `modules.platform.features=[<module_id>, ...]`, assemble against `default_template_for_idea`, run `static_verify_v2`, and (for anything with inputs/markers) `ui_audit.audit_ui`. This catches undefined references, signal-declaration order bugs, and duplicate assignments before they reach a real SKU.

7. **If this is a strategy-facing module** (`exec_*`, `risk`), the repaint-tolerance change from 2026-07-17 does **not** apply — strategies are still backtested for real, so keep the conservative self-check from `hermes/development.md`: repaint, extreme regimes, fees/slippage, sample size, parameter sensitivity, out-of-sample, before calling it done.

8. **Decide where it ships** — add to `SKU_BASE_FEATURES` (`module_registry.py`) or a `config/product_skus/SKU-XX.json` features array, or leave it smoke-tested only if experimental.

9. **Verify at factory level**: `python3 scripts/factory_gate.py`, then `python3 scripts/module_lint.py --module <module_id>` for the metadata/UI-hygiene half of the check.

10. **Regenerate what changed**: if a shipping SKU picked it up, `python3 scripts/regenerate_sku_factory.py` then `python3 scripts/visual_sku_review.py`.

11. **Sync the knowledge wiki — do this without asking, if reachable.** Same as the UI-update skill: if `~/Desktop/dev/llmwiki` is accessible, run `python3 ~/Desktop/dev/llmwiki/hermes/scripts/registry_to_wiki.py` (regenerates every `wiki/modules/*.md` + the hub from the fresh registry — nothing does this automatically, it's a plain script) and append one line to `~//memory.md` (`date | factory-module-developer | what changed | next`). If it's not reachable, say so explicitly rather than skipping silently.

## Common Pitfalls

- Adding a `ta.*` call that "should" exist but isn't real Pine v6 (a frequent LLM hallucination pattern) — the whitelist exists exactly to catch this; don't bypass it, extend it only when you've confirmed the function is real.
- Forgetting `kind: "logic"` on the registry entry (defaults are fine here since `"logic"` is the fallback, but be explicit).
- Treating a strategy-facing module's backtest-friendliness the same as an indicator's — the 2026-07-17 repaint-tolerance change is indicator-only; don't carry it into `exec_*`/`risk` work.
