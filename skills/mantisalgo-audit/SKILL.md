---
name: mantisalgo-audit
description: "Use when auditing MantisAlgo output — reviewing a product draft, judging a SKU, or running the quarterly SKU audit. Enforces the three-axis review (freshness, marketability, technical integrity), independent re-verification, and reject-by-default."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [mantisalgo, audit, review, freshness, verdict]
    related_skills: [hermes-agent]
---

# MantisAlgo Critic Audit

## Overview

The critic is the judgment layer above the machine checks (`--review` flag, quality-rubric tests). It checks the factory and never helps it produce. With 163 modules and 8 SKUs accumulated, the gravity of existing assets is the enemy. Full checklist: `Desktop/dev/MantisAlgo/hermes/critic.md`; overlap baseline: `config/module_registry/registry.json`.

## When to Use

- Factory handoff: a product draft awaits verdict (production flow step 5)
- Quarterly audit of all SKUs
- Any "is this good enough to ship?" question about factory output

Don't use for: fixing the product yourself (that's helping production — hand findings back), pipeline changes (development).

## Audit Workflow — all three axes, always

Review targets: `output/` drafts, `pinescript_factory/` products, `config/product_skus/` definitions.

1. **Freshness (staleness detection).**
   - Compare the product's module combination against the registry: high overlap with existing SKUs → "not a new product".
   - Demand code locations for the idea JSON's 3 differentiators from factory-manager. Can't point → reject.
   - Registry uniqueness pass ≠ freshness. Is the *approach* new, or just the packaging?
   Done when: overlap quantified and differentiators located (or not).
2. **Marketability (benchmark comparison).**
   - Versus the *named* TradingView benchmark: is there a reason to pay?
   - Does the description alone make clear what it does?
   Done when: the pay-reason is stated in one sentence, or its absence is the rejection reason.
3. **Technical integrity — re-verify independently.** Machine checks passing is never sufficient grounds.
   - Repaint/lookahead check, re-run yourself
   - 5-Part Anatomy & signal-variable rules respected
   - Strategies: fees/slippage, sample size, parameter sensitivity, out-of-sample
   Done when: your own results, not the factory's, fill the checklist.

## Verdict

Approve / **Conditional approve** (numbered fix list) / **Reject** (reason + alternative direction — a rejection without both is incomplete). When in doubt, reject; approval is not the default.

Log the verdict to `/memory.md` and the rejection casebook in `Desktop/dev/MantisAlgo/hermes/development.md`. Done when: both entries written.

## Quarterly Audit

- Review all SKUs: propose removal of duplicates, aging, low quality.
- Report `planned`-module backlog and category skew (e.g., Momentum pile-up).

## Common Pitfalls

1. Rubber-stamping because machine checks passed — that's transcription, not judgment.
2. Transcribing factory-manager's own reasoning as the verdict.
3. Checking technical integrity only and skipping freshness/marketability.
4. Rejecting without an alternative direction — that stalls the factory instead of steering it.
5. Softening a verdict to be agreeable — independence is the job.

## Verification Checklist

- [ ] All three axes examined, none skipped
- [ ] Technical results independently reproduced
- [ ] Verdict is one of the three forms, complete with fix list or reason+direction
- [ ] memory.md and rejection casebook updated
