---
name: mantis-strategy-module-lint
description: "Point-check MantisAlgo's logic-kind Pine Script modules (registry.json kind=\"logic\" — structure, momentum, volume, session, pattern, quant, execution, imbalance, liquidity, blocks, signal — 134 modules used by both indicators and strategies, referred to as '전략모듈' by 곽경준). Use whenever 곽경준 says '린트해줘', '점검해줘', '전략모듈 린트', '로직 점검' in the MantisAlgo project, before shipping a SKU, after touching any file under generators/families/{structure,momentum,volume,session,pattern,quant,execution,imbalance,liquidity,blocks,signal}/, or after editing registry.json. READ-ONLY diagnostic — for adding/changing a module use mantis-strategy-module-update instead."
license: MIT
metadata:
  mantisalgo:
    tags: [pine-script, logic, strategy, lint, module-registry]
    related_skills: [mantis-strategy-module-update, mantis-ui-module-lint, mantis-ui-module-update]
    cursor_command: strategy-module-lint
---

# MantisAlgo — Strategy/Logic Module Lint

## Overview

MantisAlgo's module registry (`config/module_registry/registry.json`) splits every module into a first-class `kind`: **ui** (chart display), **logic** (factory analysis/signal engines — what 곽경준 calls "전략모듈"), **infra** (assembly plumbing). This skill covers **logic** — 134 modules as of 2026-07-17, spanning the families `structure`, `momentum` (`mt_*`), `volume` (`vol_*`), `session` (`sess_*`), `pattern` (`pat_*`), `quant` (`qx_*`), `execution` (`exec_*`), `imbalance` (`imb_*`), `liquidity` (`liq_*`), `blocks` (`block_*`), `signal` (`sig_*`), and the generic `premium` toggles (`risk`, `alerts`, `filters`, `staged_signals`...).

Naming note: "전략모듈" here is broader than Pine's `strategy()` script type — these logic modules feed **both** indicators (structure/momentum/volume analysis with no orders) and strategies (the same analysis plus `exec_*`/`risk` order-placement modules). If 곽경준 means something narrower ("just the modules that place orders"), that's the `exec_*` family specifically — say so and scope the run to those.

## When to Use

- 곽경준 says anything like "전략모듈 린트해줘", "로직 모듈 점검해줘", "구조/모멘텀/볼륨 모듈 확인해줘"
- Before `scripts/factory_gate.py` or shipping/regenerating a SKU
- Right after adding or editing a module in any of the families above
- Periodic health check across the whole logic kind

Not for: adding/changing a module's Pine logic — that's `mantis-strategy-module-update`. Not for `ui`/`infra` kind modules — that's `mantis-ui-module-lint`.

## How to Run

```bash
python3 scripts/module_lint.py --kind logic              # full report, all 134
python3 scripts/module_lint.py --kind logic --quiet       # only non-clean modules
python3 scripts/module_lint.py --module mt_squeeze_detector
python3 scripts/module_lint.py --kind logic --json
```

## What This Checks — and What It Doesn't

`module_lint.py` runs each module's generator in isolation with a minimal smoke idea and checks its **metadata and embedded UI hygiene**: registry `description` present, `kind` valid, every `input.*` the module defines has `group=`/`tooltip=`, any marker (`plotshape`/`plotchar`) it draws sits behind a `showTier*`/`show*` display gate, no ungated `bgcolor`, and `est_lines` hasn't drifted far from the actual generated line count. It does **not** run full Pine syntax/type-checking on a module in isolation — a module is a code snippet, not a compilable script, so `ta.*` namespace validity, undefined-reference checks, and signal-variable ordering can only be verified once the module is assembled into a real script.

For that assembled-level correctness, this skill hands off to two things:
1. **`scripts/factory_gate.py`** — assembles every shipping SKU idea, runs `verify_v2.py`'s full static gate (hallucinated `ta.*` calls, duplicate assignments, undefined refs, signal-declaration order, truncation heuristics) plus the UI audit, and fails the build on any violation.
2. **A one-off smoke assembly** for a single new/changed module — see `tests/test_new_modules_smoke.py` for the pattern (build a minimal `PremiumIdea` with `platform.features=[<module_id>]`, assemble against the platform template, run `static_verify_v2`). Use this to sanity-check one module without waiting on a full SKU regen.

## Reading Findings

- **`registry description 비어 있음`** — every module needs a one-line Korean description; it's what shows up in `wiki/modules/<id>.md` and the family hub
- **`kind '<x>' 무효`** — `kind` must be `ui`, `logic`, or `infra`
- **`group=`/`tooltip= 없는 input`** — logic modules define inputs too (lengths, multipliers, thresholds); these get the exact same UI-contract treatment as UI-kind modules
- **`게이트 없는 bgcolor`** — logic modules that paint background context (e.g. regime/ADX/pattern-state bgcolor) must gate it behind `showSigBg` or similar, same declutter rule as UI kind
- **`표시 게이트(showTier*/show*) 없는 마커`** (advisory) — a `plotshape`/`plotchar` without a tier/show gate always renders; fine for a module's primary signal, worth a second look for secondary/confirmation markers

## Theory & Repaint Notes Specific to Logic Modules

- **Indicators**: per `context_prompting.py`'s theory contract, a logic module feeding an indicator idea should be explainable — the market mechanism it exploits, the exact math, and where it degrades. Repainting/intrabar values are **acceptable** for indicators as of 2026-07-17 (곽경준's explicit call: indicators aren't backtested, so visual persuasiveness outranks strict signal timing).
- **Strategies**: the repaint tolerance above does **not** extend to strategy prompts or `exec_*`/`risk` modules — those still get backtested, so repaint distorts real results. If you're touching an `exec_*` module, keep the conservative self-check list from `hermes/development.md`: repaint, extreme regimes, fees/slippage, sample size, parameter sensitivity, out-of-sample.
- If a new logic module calls a `ta.*` function not in the whitelist (`_VALID_TA_FUNCTIONS` in `pipeline.py`, extended by `_EXTRA_VALID_TA` in `verify_v2.py`), `factory_gate.py`/smoke assembly will flag it as hallucinated — add it to the whitelist only if it's a real Pine v6 function.

## After Findings Are Fixed

1. Re-run the lint, confirm `findings=0`.
2. Run a smoke assembly (single module) or `scripts/factory_gate.py` (whole factory) to catch what module-level lint can't.
3. If a shipping SKU changed, `scripts/regenerate_sku_factory.py` then `scripts/visual_sku_review.py`.
