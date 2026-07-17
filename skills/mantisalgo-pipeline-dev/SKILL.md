---
name: mantisalgo-pipeline-dev
description: "Use when running or improving the MantisAlgo generation pipeline, editing templates, or preparing output for critic handoff. Enforces the verification gate, deterministic-injection-first, self-verification before handoff, and the rejection casebook."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [mantisalgo, pipeline, pinescript, verification-gate, self-verification]
    related_skills: [mantisalgo-production-run, mantisalgo-module-registry]
---

# MantisAlgo Pipeline Development

## Overview

Most effort goes into improving the pipeline and defending the verification gate, not hand-writing scripts. Bypassing the factory keeps it weak. Standards: `../MantisAlgo/hermes/development.md`; Pine rules single source: `pinescript_v6_master_rules.md` (read only when touching `.pine` files — token economy).

## When to Use

- Running production: `python main.py --type strategy|indicator [--review|--from-idea FILE|-n N]`
- Changing `pipeline.py`, `context_prompting.py`, `factory_saver.py`, or `config/template_*.pinescript`
- Self-verifying output before critic handoff

Don't use for: idea specs (idea), registry work (module-developer), visual sign-off (ui).

## Non-negotiables (synced with repo AGENTS.md)

1. Ideas must be unique (registry check)
2. Indicator ≠ Strategy — separate templates & verification
3. Deterministic injection first; LLM polish only on static-check failure
4. **Verification gate fail = no save** — no manual rescue
5. Signal vars: `= false` before the AI zone, `:=` inside, never reset after

## Pipeline-Change Workflow

1. Read repo `AGENTS.md`, then only the files the change touches.
2. Make the change; keep deterministic injection the first path.
3. Run pytest (`pine_safe`, `tradingview_compile_fixes`, `sku_tv_safety`, `quality_rubric`, …). Done when: pytest green after the change.
4. If the change weakens or routes around the verification gate in any case, revert — the gate is the product.

## Generated-Code Standards

- `//@version=6`; v6 optimizations (short-circuit eval, negative array indexing)
- 5-Part Anatomy: Inputs → Filter Engine → Custom Logic → Execution → Risk Mgmt
- Division-by-zero guards (`math.max()`); strategies ship with ATR-based SL/TP
- No repainting: `request.security()` lookahead handled; signals on confirmed bars
- Save paths: `pinescript_factory/1_Indicators|2_Strategies/{Trend,Momentum,Breakout}/`
- Reason in English; user-facing output & comments in Korean (`.hermesrules.txt`)

## Self-Verification (before critic ever sees it)

Handing over unchecked work wastes everyone's time. Done when every box is checked:

- [ ] Verification gate + pytest green
- [ ] Repaint check: realtime vs confirmed bars
- [ ] Extreme regimes: crash, low liquidity, short history
- [ ] Strategies: fees/slippage backtest, sample size, parameter sensitivity, out-of-sample
- [ ] Can point to the code location of each of the 3 differentiators

## Rejection Casebook (never rejected twice for the same reason)

On any critic rejection: append `date | product | reason | prevention rule` to the casebook table in `hermes/development.md`, and apply the prevention rule to the pipeline or checklist, not just to the one product. Done when: casebook updated AND the prevention is structural.

## Common Pitfalls

1. Hand-writing a script because the pipeline path is slower — that's the anti-pattern the factory exists to kill.
2. LLM-polishing before deterministic injection had its chance.
3. Repaint checks on confirmed bars only.
4. Reusable code kept local instead of handed to module-developer immediately.
5. Treating a rejection as one-off instead of writing a prevention rule.

## Verification Checklist

- [ ] Non-negotiables 1–5 all respected
- [ ] Self-verification block fully checked
- [ ] Reusable code handed to module-developer
- [ ] Decision logged to `${WIKI_PATH}/memory.md`
