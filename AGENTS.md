# Obsidian Vault — Agent Operating Rules

This vault has two trees. Read this before touching anything.

| Tree | What it is | Rules file |
|---|---|---|
| `wiki/` | Knowledge wiki (Karpathy LLM-wiki pattern) — compiled knowledge, compounding | `wiki/SCHEMA.md` |
| `hermes/` | Hermes ops journal — routing (`hermes/CLAUDE.md`), team journal (`hermes/memory.md`), persona knowledge | `hermes/CLAUDE.md` |

## Session start (any tool: Claude Code, Codex, Cursor, Hermes)

1. Read `wiki/SCHEMA.md` (conventions + auto-accumulation rules) and `wiki/index.md` (page catalog).
2. Check recent activity: `grep "^## \[" wiki/log.md | tail -5`.

## Non-negotiable discipline

- **Auto-accumulate.** Fetched external content → save to `wiki/raw/` and ingest, without asking. Substantial answers (comparisons, analyses, discovered connections) → file into `wiki/queries/` or `wiki/comparisons/`, update `index.md`, append to `log.md`. Don't file one-off fact checks.
- **raw/ is immutable.** Never edit files under `wiki/raw/`.
- **Page template**: 🌱 쉽게(비유, 한국어) / ⚙️ 정확히(경로·수치·출처) / 🔗 연결([[wikilinks]]) / 📌 미해결. Every new page gets an `index.md` line — no orphans.
- **Contradictions**: never silently overwrite; add `> ⚠️ 상충:` with both sources.
- **External code analysis** (Pine/LuxAlgo etc.): code → `wiki/raw/code/` → analysis page → compare against MantisAlgo `config/module_registry/registry.json` → list missing modules in 📌.
- **Taste & ideas capture.** Praise/complaints/preferences (esp. UI/UX) → append to `wiki/entities/kkj-taste.md`; casually dropped ideas → `wiki/ideas/ideas-inbox.md`. Both without asking.
- **Journal separation**: knowledge goes in `wiki/`; session decisions go in `hermes/memory.md` (`date | persona | decision | next`).
- Answer 곽경준 in Korean, reason in English. Source of truth for personas is `~/.hermes/profiles/*/SOUL.md`; for work standards, each repo's `hermes/*.md` — wiki pages summarize and link, never fork.

## Project repos (knowledge lives with the code)

`~/Desktop/dev/MantisAlgo` (AGENTS.md) · `~/Desktop/dev/ShiftTrade` (DEVELOPMENT_MAP.md) · `~/Desktop/dev/AccountingGo` (README.md) — each points back here.
