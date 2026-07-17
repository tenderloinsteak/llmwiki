---
name: wiki-lint
description: "Use when health-checking the knowledge wiki — periodically, after heavy ingesting, or when 곽경준 says 점검/lint/청소해줘. Finds contradictions, stale claims, orphans, missing pages and cross-references, and data gaps; delivers a fix list and applies approved fixes."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [wiki, lint, health-check, maintenance, obsidian]
    related_skills: [wiki-ingest, wiki-query, hermes-wiki-maintenance]
---

# Wiki Lint

## Overview

The wiki lives at `$WIKI_PATH` (`Desktop/dev/llmwiki/wiki`). Lint keeps the wiki healthy as it grows: humans abandon wikis because maintenance outgrows value — here maintenance is the LLM's job. Distinct from `hermes-wiki-maintenance`, which covers the ops journal at `${WIKI_PATH}/memory.md`.

## When to Use

- Periodic health check (good default: after every ~10 ingests, or on request)
- After a large batch ingest
- Before relying on the wiki for an important synthesis

Don't use for: ingesting (wiki-ingest), answering content questions (wiki-query).

## Lint Workflow

1. **Orient.** Read `SCHEMA.md`, `index.md`, recent `log.md`. Done when: page inventory and recent activity loaded.
2. **Structural pass.**
   - Orphans: pages with no inbound `[[wikilinks]]` and no `index.md` line
   - Broken links: `[[targets]]` that don't resolve to a file
   - Index drift: pages missing from index, or index lines pointing nowhere
   - Frontmatter: missing tags/created/sources fields
   Done when: each defect is listed with file path.
3. **Content pass.**
   - Contradictions between pages that no ⚠️ callout acknowledges
   - Stale claims superseded by newer ingested sources
   - Concepts mentioned on ≥3 pages but lacking their own page
   - Missing cross-references between obviously related pages
   Done when: each finding names the pages involved.
4. **Gap pass.** Questions the wiki nearly-but-can't answer; suggest concrete new sources or web searches worth ingesting. This is where lint feeds the reading list.
5. **Fix list → approval → apply.** Small mechanical fixes (broken links, index lines, missing frontmatter) apply directly. Merges, splits, and deletions need 곽경준's approval first — decisions preserved via redirect links, never lost. Done when: applied fixes listed, pending fixes await approval.
6. **Report in Korean, short**: findings / fixed now / needs approval / suggested next sources. Append `## [YYYY-MM-DD] lint | summary` to `log.md`.

## Common Pitfalls

1. "Clean up later" — every finding goes on the list now, however small.
2. Merging or deleting pages without approval.
3. Fixing structure while silently rewriting content — content changes are findings, not lint fixes.
4. Skipping the gap pass — lint that only fixes links wastes its best output: what to read next.
5. Forgetting the log entry, so the next lint re-audits everything.

## Verification Checklist

- [ ] Zero unlisted orphans, broken links, index drift
- [ ] Contradiction/stale findings name their pages and sources
- [ ] Mechanical fixes applied; destructive changes only proposed
- [ ] Suggested sources/questions delivered
- [ ] log.md lint entry appended
