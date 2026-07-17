# Obsidian Vault — Agent Operating Rules

This vault has two trees. Read this before touching anything.

| Tree | What it is | Rules file |
|---|---|---|
| `wiki/` | Knowledge wiki (Karpathy LLM-wiki pattern) — compiled knowledge, compounding | `wiki/SCHEMA.md` |
| `hermes/` | Routing (`hermes/CLAUDE.md`), agent profiles, study notes. Folder name is historical; it is not Hermes-only. Ops journal is now at `memory.md` (root). | `hermes/CLAUDE.md` |

## Session start (any tool: Claude Code, Codex, Cursor, Hermes)

1. Read `wiki/SCHEMA.md` (conventions + capture/ingest rules) and `wiki/index.md` (page catalog).
2. Check recent wiki activity: `grep "^## \[" wiki/log.md | tail -5`.
3. Check recent **shared** decisions: `tail -20 memory.md` (same file every tool appends to at `${WIKI_PATH}/memory.md`).

## Non-negotiable discipline

- **Capture ≠ Ingest (Karpathy).** Drop sources into `wiki/raw/` automatically. Compiling into wiki pages requires a short takeaway discussion with 곽경준 (or an explicit “알아서/배치”). Never silently full-ingest just because a file appeared in raw/.
- **raw/ is immutable.** Never edit files under `wiki/raw/`. Inbox = flat `wiki/raw/` (optional `raw/assets/` for images only).
- **Page template**: 🌱 쉽게(비유, 한국어) / ⚙️ 정확히(경로·수치·출처) / 🔗 연결([[wikilinks]]) / 📌 미해결. Every new page gets an `index.md` line — no orphans.
- **Contradictions**: never silently overwrite; add `> ⚠️ 상충:` with both sources.
- **Query filing still auto:** comparisons/analyses/discovered connections → `wiki/queries/` or `wiki/comparisons/` without asking (not the same as source ingest).
- **Taste & ideas capture.** Praise/complaints/preferences → `wiki/entities/kkj-taste.md`; casually dropped ideas → `wiki/ideas/ideas-inbox.md`. Both without asking.
- **Two trees, one vault (all tools):** knowledge → `wiki/`; session decisions → `memory.md` (`date | tool-or-persona | decision | next`). Path is always `${WIKI_PATH}/memory.md`.
- Answer 곽경준 in Korean, reason in English. Personas SoT: `~/.hermes/profiles/*/SOUL.md`; work standards: each repo's `hermes/*.md` — wiki summarizes and links, never forks.

## Project repos (knowledge lives with the code)

`~/Desktop/dev/MantisAlgo` (AGENTS.md) · `~/Desktop/dev/ShiftTrade` (DEVELOPMENT_MAP.md) · `~/Desktop/dev/AccountingGo` (README.md) — each points back here.
