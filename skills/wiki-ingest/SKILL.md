---
name: wiki-ingest
description: "Use when 곽경준 drops a source into wiki/raw or says 넣어줘/소화/ingest. Collaborative: discuss 3–5 takeaways and emphasis first, then compile into wiki pages. Capture to raw is automatic; full ingest is not silent."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [wiki, ingest, knowledge-base, obsidian, karpathy]
    related_skills: [wiki-query, wiki-lint, llm-wiki, obsidian]
---

# Wiki Ingest

## Overview

Knowledge wiki at `$WIKI_PATH` (`${WIKI_PATH}/wiki`).

**Capture ≠ Ingest.** Saving to `raw/` is automatic. Ingest = compile into interlinked wiki pages **after** 곽경준 steers emphasis (Karpathy: stay involved; guide what to emphasize). Structure contract: `SCHEMA.md`.

## When to Use

- 곽경준 says 넣어줘 / 정리해줘 / 소화해줘 / ingest
- A new file is in `wiki/raw/` **and** this session is doing ingest (do not auto-ingest every new raw file)
- Batch ingest only when he asks — still one source at a time unless he says skip discussion

Don't use for: answering questions (`wiki-query`), health checks (`wiki-lint`), ops journal (`${WIKI_PATH}/memory.md`).

## Ingest Workflow (per source)

1. **Orient.** Read `SCHEMA.md`, `index.md`, last ~5 `log.md` entries. Done when: you know which pages this source may touch.
2. **Secure the raw file.** Must already live under `wiki/raw/` (flat inbox). If URL/paste only, save there first — raw is immutable. Done when: file exists and you read it fully.
3. **Discuss takeaways (required).** Give 곽경준 3–5 key takeaways in Korean. Ask what to emphasize / ignore / connect. Done when: emphasis confirmed **or** he says 알아서 / 배치로 그냥.
4. **Write / update wiki pages** only after step 3: summary if useful, entity/concept updates, two-way `[[wikilinks]]`. Never silently overwrite contradictions — `> ⚠️ 상충:`.
5. **Update `index.md`** — one line per new/renamed page.
6. **Append `log.md`:** `## [YYYY-MM-DD] ingest | <title>` + pages touched + emphasis notes.

## Agent-fetched sources mid-task

1. Save to `wiki/raw/` without asking (capture).
2. Tell 곽경준 it was captured; ask whether to ingest now.
3. Do **not** full-ingest unprompted unless he already said 알아서 ingest this session.

## Common Pitfalls

1. Editing `raw/`.
2. Silent full ingest on every clip (violates Karpathy collaboration).
3. Summary-only with no cross-links.
4. Silent contradiction resolution.
5. Skipping index/log.
6. Answering discussion in English — Korean for 곽경준.

## Verification Checklist

- [ ] Raw untouched under `wiki/raw/`
- [ ] Takeaway discussion happened (or explicit 알아서)
- [ ] Touched pages + two-way links; ⚠️ for contradictions
- [ ] index.md + log.md updated
- [ ] Touched-page list reported
