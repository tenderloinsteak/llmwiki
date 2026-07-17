# Obsidian Vault — Agent Operating Rules

This vault has two trees. Read this before touching anything.

| Tree | What it is | Rules file |
|---|---|---|
| `wiki/` | Knowledge wiki (Karpathy LLM-wiki pattern) — compiled knowledge, compounding | `wiki/SCHEMA.md` |
| `hermes/` | **Shared ops journal for every tool** (Cursor / Claude Code / Codex / Hermes) — routing (`hermes/CLAUDE.md`), team journal (`hermes/memory.md`), study notes. Folder name is historical; it is not Hermes-only. | `hermes/CLAUDE.md` |

## Session start (any tool: Claude Code, Codex, Cursor, Hermes)

1. Read `wiki/SCHEMA.md` (conventions + auto-accumulation rules) and `wiki/index.md` (page catalog).
2. Check recent wiki activity: `grep "^## \[" wiki/log.md | tail -5`.
3. Check recent **shared** decisions: `tail -20 hermes/memory.md` (same file every tool appends to).

## Non-negotiable discipline

- **Auto-accumulate.** Fetched external content → save to `wiki/raw/` and ingest, without asking. Substantial answers (comparisons, analyses, discovered connections) → file into `wiki/queries/` or `wiki/comparisons/`, update `index.md`, append to `log.md`. Don't file one-off fact checks.
- **raw/ is immutable.** Never edit files under `wiki/raw/`.
- **Page template**: 🌱 쉽게(비유, 한국어) / ⚙️ 정확히(경로·수치·출처) / 🔗 연결([[wikilinks]]) / 📌 미해결. Every new page gets an `index.md` line — no orphans.
- **Contradictions**: never silently overwrite; add `> ⚠️ 상충:` with both sources.
- **External code analysis** (Pine marketplace / reference scripts): code → `wiki/raw/code/` → analysis page → compare against MantisAlgo `config/module_registry/registry.json` → list missing modules in 📌.
- **Taste & ideas capture.** Praise/complaints/preferences (esp. UI/UX) → append to `wiki/entities/kkj-taste.md`; casually dropped ideas → `wiki/ideas/ideas-inbox.md`. Both without asking.
- **Two trees, one vault (all tools):** knowledge → `wiki/`; session decisions → `hermes/memory.md` (`date | tool-or-persona | decision | next`). Path is always `~/Desktop/dev/llmwiki/hermes/memory.md` regardless of which IDE/agent ran the session.
- Answer 곽경준 in Korean, reason in English. Source of truth for personas is `~/.hermes/profiles/*/SOUL.md`; for work standards, each repo's `hermes/*.md` — wiki pages summarize and link, never fork.

## Project repos (knowledge lives with the code)

`~/Desktop/dev/MantisAlgo` (AGENTS.md) · `~/Desktop/dev/ShiftTrade` (DEVELOPMENT_MAP.md) · `~/Desktop/dev/AccountingGo` (README.md) — each points back here.
