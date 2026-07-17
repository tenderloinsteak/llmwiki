---
name: shifttrade-market-realism
description: "Use when working on ShiftTrade's price engine, order book, tape, trade strength, or tick data — engine changes, scenario injection, or realism verification. Enforces order-driven generation, stylized-facts statistical verification, and pipeline compatibility."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [shifttrade, microstructure, simulation, stylized-facts, order-book]
    related_skills: [hermes-agent]
---

# ShiftTrade Market Realism

## Overview

Owner of ShiftTrade's market realism. Core law: never generate a price and decorate a book around it — **generate order events; let price, book, and tape emerge together** so the three are always consistent. Standards: `Desktop/dev/ShiftTrade/hermes/microstructure-engineer.md`; data plan: `docs/user-data-and-rollup-plan.md`.

## When to Use

- Changing the price engine (`~/NemotronEngines/engine_4_good.py`, consumed by `scripts/generate_ticks.py`)
- Order book / tape / trade-strength / volume work
- Adding market scenarios (surge, capitulation, chop, limit-up/down)
- Verifying realism of generated data

Don't use for: Next.js/Supabase frontend work unrelated to market data.

## Engine-Change Workflow

1. **Map the pipeline first.** tick generation → `scripts/build_aggregates.py` → Supabase (`run_market_rollup.py`, `archive_ticks.py`, `upload_archive_to_supabase.py`). Any change must keep tick → aggregate → Supabase working. Done when: affected pipeline stages listed.
2. **Design order-driven.** Model agent mixes (market-order takers, limit-order providers, momentum chasers) rather than tuning a price path. Evaluate whether FinancialPriceEngine evolves or needs an order-driven layer on top.
3. **Implement** with a performance budget — scalping-grade tick replay is a requirement, not an afterthought.
4. **Verify statistically** (see below), then visually against real charts. "Looks right" without tests ≠ done.
5. **Regenerate & preview**: `preview_engine.py`, `preview_market_dynamics.py`; reseed via `generate_ticks.py` (6 months past + 6 months future into `public/data/`).

## Stylized Facts — the realism bar (test code required)

- Fat-tailed returns (non-Gaussian)
- Volatility clustering (spikes arrive in bunches)
- No return autocorrelation / long memory in absolute returns
- Positive volume–volatility correlation

Done when: each fact is verified by runnable test code on the generated data, not by eyeball.

## Consistency Invariants

- Book depth concentrates near best quotes; spread widens/narrows with volatility; depth recovers after large fills.
- Trade strength = buy-fill vs sell-fill volume; tape and book changes always consistent.
- Any book/tape/chart contradiction = work not finished.

## Common Pitfalls

1. Pure random walk + noise as the price process.
2. Book generated independently of fills — inconsistent tape/depth.
3. Eyeball-only validation.
4. Event loop built without a performance budget, discovered too slow at replay time.
5. Engine change that silently breaks `build_aggregates.py` or the Supabase rollup.

## Verification Checklist

- [ ] Stylized-facts tests green on newly generated data
- [ ] Book/tape/chart consistency spot-checked at fills and spikes
- [ ] Scenario injection still works (surge, capitulation, chop, limit-up/down)
- [ ] Tick replay meets scalping-grade speed
- [ ] tick → aggregate → Supabase pipeline runs end-to-end
- [ ] Decision logged to `/memory.md`
