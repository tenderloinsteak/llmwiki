---
name: mantisalgo-idea-spec
description: "Use when creating a MantisAlgo product idea, writing an idea JSON, or writing sales copy for a finished product. Enforces external idea sources, 3 concrete differentiators, named benchmarks, and pipeline-consumable output."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [mantisalgo, idea, spec, sales-copy, differentiation]
    related_skills: [mantisalgo-production-run]
---

# MantisAlgo Idea Spec & Sales Copy

## Overview

The idea part owns the start (idea JSON) and end (sales copy) of every product. A weak idea means a well-made product nobody buys. Standards live in `Desktop/dev/MantisAlgo/hermes/idea.md`; this skill is the authoring workflow.

## When to Use

- "What should we build next?" / new product planning
- Turning a rough concept into `config/ideas/*.json`
- Writing the description/sales copy after a product passes critic

Don't use for: implementing the idea (development), module gap analysis (module-developer).

## Idea Workflow

1. **Name the external source.** Pick at least one: TradingView gap analysis (popular scripts with complaints), community pain points, new concepts from tutor, module gap map. A variation of an existing SKU alone is NOT an idea. Done when: the source is written into the spec.
2. **Check what exists.** Read `config/product_skus/` (SKU-01..08) and the module registry. Done when: overlap with existing SKUs is assessed.
3. **Write the spec.** Required fields: target user & situation, 1–2 *named* benchmark scripts (never vague categories), **3 concrete differentiators** ("more accurate"/"better" are invalid), one-line selling point, required modules (existing vs new per registry).
4. **Author the JSON** per `idea_schema.py` / `config/idea_schema/` into `config/ideas/*.json`. Run `idea_advisor.py` for quality advice — advice, not verdict. Done when: file is consumable via `python main.py --from-idea FILE`.
5. **Pass the registry check.** `idea_registry.py` uniqueness is the floor, not proof of differentiation.

An idea left in chat is not an idea.

## Sales Copy Workflow (after critic approval)

Structure: one-line hook → what it shows → how to use in 3 steps → settings → honest limitations.

- The 3 differentiators must survive **verbatim** into the copy.
- Never hide limitations — refunds and reputation cost more than honesty.
- Done when: copy registered with the SKU in `config/product_skus/` and logged to `/memory.md`.

## Common Pitfalls

1. Looking only inward — recombining existing modules and calling it new.
2. Vague benchmarks ("momentum indicators") instead of named scripts.
3. Differentiators that can't be pointed to in code — critic rejects these.
4. Leaving the idea in chat instead of a pipeline-consumable JSON.
5. Sales copy that oversells — omitted limitations become refunds.

## Verification Checklist

- [ ] External idea source named in the spec
- [ ] 3 differentiators, each concrete and code-verifiable
- [ ] Benchmark scripts named, not categorized
- [ ] JSON validates against the schema and passes registry uniqueness
- [ ] (Copy) differentiators verbatim + limitations stated
