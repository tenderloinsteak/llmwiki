---
name: hermes-wiki-maintenance
description: "Use when maintaining the Hermes workspace at ${WIKI_PATH} — link/orphan checks, memory.md compaction, repo-wiki drift sync, or a periodic health check. Structure only, never content; ends with a 3-line report."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [wiki, obsidian, maintenance, index, memory-compaction]
    related_skills: [llm-wiki, obsidian]
---

# Hermes Wiki Maintenance

## Overview

The librarian creates no content and defends structure. Goal: "read the index (CLAUDE.md) and the whole system is visible." The wiki lives at `${WIKI_PATH}` — see its `SCHEMA.md` for the structure contract (CLAUDE.md = index, memory.md = log at root, personas/ = wiki-owned knowledge; project knowledge lives in each repo's `hermes/` folder). Full rules: `personas/librarian.md`.

## When to Use

- Periodic check (on request or after any large piece of work)
- memory.md is growing / needs compaction
- A note, link, or persona file was added or renamed
- Suspected drift between repo rule files and the wiki

Don't use for: editing note content (content belongs to its owner persona), large reorganizations without approval.

## Periodic Check Workflow

1. **Orient**: read `SCHEMA.md`, `CLAUDE.md`, and the last ~30 lines of `memory.md`. Done when: current structure and recent activity are loaded.
2. **Orphans & links**: scan for notes not reachable from CLAUDE.md's routing/file map or a persona's references, and for broken `[[wikilinks]]`. Done when: a fix list exists (possibly empty) — never "clean up later".
3. **Memory compaction**: if `memory.md` exceeds 50 entries, compact old ones into per-project summaries. Decisions are preserved in summary form, never deleted. Done when: entry count ≤ 50 with decisions intact.
4. **Format consistency**: check tabular notes (learning log in `personas/tutor.md`, rejection casebook in `Mantis Algo/hermes/development.md`) still match their table formats.
5. **Repo-wiki sync**: watch list = this wiki, each repo's `hermes/` folder, `AGENTS.md`, `.hermesrules.txt`, `docs/`. On conflict, **repo wins** — update the wiki, then flag the drift. Done when: zero known conflicts or each is flagged with its fix.
6. **Bloat watch**: persona file over 150 lines or internally conflicting standards → propose a split (proposal only; splitting needs approval).
7. **Report in 3 lines**: findings / actions taken / approvals needed. Append the session to `memory.md`.

## Fix Rules

- Duplicated concept across two notes → merge, leave a redirect link.
- Every new note gets linked from the index or a persona's references — no orphans survive a check.
- Large reorganizations require 곽경준's approval before touching files.

## Common Pitfalls

1. Editing content while "fixing structure" — structure only.
2. Deferring findings ("clean up later") instead of listing them immediately.
3. Deleting old memory entries instead of compacting to summaries.
4. Updating the wiki against repo rules instead of the other way around.
5. Reports longer than 3 lines.

## Verification Checklist

- [ ] Zero orphan notes and broken wikilinks (or fix list delivered)
- [ ] memory.md ≤ 50 entries, decisions preserved
- [ ] Repo-wiki conflicts resolved repo-first and flagged
- [ ] No content edited; big changes only proposed
- [ ] 3-line report delivered and memory.md updated
