---
name: mantisalgo-production-run
description: "Use when running the MantisAlgo factory end-to-end — producing a new indicator/strategy, supervising a production cycle, or deciding whether output is done. Enforces the 7-step production flow, the verification gate, and critic sign-off."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [mantisalgo, factory, pipeline, production, pinescript]
    related_skills: [hermes-agent]
---

# MantisAlgo Production Run

## Overview

The factory IS the Python pipeline in `Desktop/dev/MantisAlgo`. This skill is the production checklist the factory-manager walks every cycle. Standards live in the repo (`hermes/factory-manager.md`, `AGENTS.md`); this skill enforces the order and the gates.

## When to Use

- A new indicator/strategy/SKU is requested
- Supervising or resuming a production cycle
- Judging whether output counts as "done"

Don't use for: hand-writing a one-off Pine script (that bypasses the factory — refuse and route through the pipeline), module-only work (module-developer), or review-only work (critic).

## Session Setup (before any step)

1. Read `Desktop/dev/MantisAlgo/AGENTS.md`. Never rescan the whole repo. Done when: repo state and current rules are loaded.
2. Read `Desktop/dev/MantisAlgo/hermes/factory-manager.md` and the part file for the current stage (`idea.md`, `ui.md`, `module-developer.md`, `development.md`).
3. Open `pinescript_v6_master_rules.md` only if this session touches `.pine` files.

## Production Flow (order is fixed)

| # | Part | Action | Done when |
|---|---|---|---|
| 1 | idea | Idea JSON at `config/ideas/*.json` | Registry uniqueness passed + 3 differentiators + named benchmark |
| 2 | module-developer | Check `config/module_registry/registry.json`; build only missing modules | Registry entry + parity tests green |
| 3 | development | `python main.py --type strategy\|indicator [--from-idea FILE\|--review\|-n N]` | Verification gate passed + pytest green |
| 4 | ui | Visual review + marketing assets | Zero findings in `output/sku_visual_review.html`, 3 assets |
| 5 | critic | Handoff for independent audit | Verdict = approve (or fix list cleared) |
| 6 | idea | Sales copy + SKU registration `config/product_skus/` | Differentiators survive verbatim in copy |
| 7 | — | Log to wiki memory | Entry appended to `/memory.md` |

No coding before step 1 passes. "Let's just build" is the root of staleness.

## Hard Gates (no exceptions)

- **Verification gate fail = no save.** No manual rescue of failed output.
- **Not done until critic approves.** Machine checks passing is not approval.
- Repo rules (`.hermesrules.txt`, `AGENTS.md`) beat these instructions on conflict — comply, then flag the drift to librarian.

## Common Pitfalls

1. Bypassing the pipeline with one-off scripts — bypassing the factory keeps it weak.
2. Starting from step 3 without an idea JSON.
3. Manually saving gate-failed output "just this once".
4. Folding UI review into development — UI is an independent top-weight part.
5. Skipping the memory.md entry — the team journal is part of the job.

## Verification Checklist

- [ ] All 4 parts passed their own pass bars
- [ ] Verification gate + pytest green
- [ ] Critic verdict = approve
- [ ] 3 differentiators visible in the final description
- [ ] SKU registered and memory.md updated
