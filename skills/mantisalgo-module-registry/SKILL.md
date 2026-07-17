---
name: mantisalgo-module-registry
description: "Use when creating, registering, or auditing MantisAlgo modules — new module production, registry.json changes, gap-map analysis, or splitting reusable code out of product work. Enforces registry entry + generator-parity tests as the definition of done."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [mantisalgo, modules, registry, gap-map, parity-tests]
    related_skills: [mantisalgo-production-run]
---

# MantisAlgo Module & Registry Work

## Overview

Modules and their registry are owned independently of product deadlines, because parts always lose to products on a shared schedule — the root of staleness. Single source of truth: `config/module_registry/registry.json` (163 modules). Standards: `../MantisAlgo/hermes/module-developer.md`.

## When to Use

- A new product needs modules (step 2 of the production flow)
- Producing or editing a module; any `registry.json` change
- Quarterly gap-map / `planned`-module audit
- Reusable code discovered during product work

Don't use for: assembling final products (development), deciding what product to build (idea).

## New-Module Workflow

1. **Registry first.** Search `registry.json` (live, planned, legacy aliases, SKU mapping) before building anything. Done when: confirmed the module doesn't already exist under any alias.
2. **Deconstruct & Scan (외부 소스 분석 시)**: 외부 참고 지표/전략 스크립트로부터 로직을 추출하여 신규 모듈을 도출할 경우, `llmwiki/wiki/concepts/pine-script-analysis-framework.md` 정본 분석 규격을 준수하여 `example_analysis_REF-XXX.json`을 먼저 설계하고 검토합니다. 
3. **Design to the quality bar.** One module = one responsibility; explicit interface (input series, return types); classified into its 5-Part Anatomy slot; **repainting behavior declared in metadata** — the consumer must never be surprised.
3. **Implement** alongside `premium_modules.py` / `premium_assembler.py` / `architecture_catalog.py` conventions.
4. **Register + test.** Add the registry entry, then run `tests/test_module_registry.py` and `tests/test_registry_generator_parity.py`. Done when: entry exists AND parity tests are green. Both, or it isn't done.
5. **Confirm standalone behavior** before handing to product work.

## Product-Support Workflow

- Before any new product: check the registry, list what's missing, build only that.
- Reusable code found in product work gets split into a module **immediately**, not "later".
- If the new product's module combination heavily overlaps recent SKUs, raise the warning yourself — before critic sees it.

## Gap Map (anti-staleness, quarterly)

1. Tally the registry by category; list weak categories as production priorities.
2. Evaluate moduleizing new concepts arriving from tutor.
3. Audit `planned` modules that never ship — accumulating plans is also inertia.

Done when: gap map updated in `MASTER_PLAN.md` and priorities logged to `${WIKI_PATH}/memory.md`.

## Common Pitfalls

1. Registered but untested (or tested but unregistered) — half-done is not done.
2. Undeclared repainting behavior surprising a consumer product.
3. Multi-responsibility modules that resist reuse.
4. Assembling products only from parts that already exist — the habit the gap map exists to break.
5. Keeping reusable code inside a product "for now".

## Verification Checklist

- [ ] Registry entry present with correct metadata (incl. repaint declaration)
- [ ] `test_module_registry.py` + `test_registry_generator_parity.py` green
- [ ] Single responsibility + explicit interface + anatomy slot assigned
- [ ] Standalone behavior confirmed
- [ ] Overlap warning raised if module combo ≈ recent SKUs
