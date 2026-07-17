---
name: wiki-query
description: "Use when 곽경준 asks a question the knowledge wiki might answer, or asks for a comparison/analysis/synthesis over ingested material. Answers from wiki pages with citations, and files valuable answers back into the wiki so explorations compound."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [wiki, query, synthesis, knowledge-base, obsidian]
    related_skills: [wiki-ingest, wiki-lint, llm-wiki]
---

# Wiki Query

## Overview

Knowledge wiki at `$WIKI_PATH` (`Desktop/dev/llmwiki/wiki`). Queries run against the compiled wiki, not the raw sources — the cross-references and contradiction flags are already there. Good answers get filed back as pages so they don't evaporate into chat history.

## When to Use

- Any question about material that has been ingested ("우리 위키에서 ~가 뭐였지?", "X랑 Y 비교해줘")
- Requests for synthesis: comparison tables, analyses, an evolving thesis
- "이 답변 저장해줘" after any wiki-grounded answer

Don't use for: fresh web research with nothing ingested (offer to ingest findings instead), Hermes ops questions (memory.md), Pine identifier lookups (`Desktop/pinestudy/wiki/`).

## Query Workflow

1. **Index first.** Read `index.md` to find candidate pages; drill into only those. At moderate scale this beats any search infra. If index lines are ambiguous, grep page contents. Done when: relevant pages identified or confirmed absent.
2. **Read and synthesize.** Answer in Korean, citing pages as `[[wikilinks]]`. Where a page carries a `⚠️ 상충` flag, surface the contradiction rather than picking a side silently. Done when: every claim in the answer traces to a cited page (or is marked as gap).
3. **Mark the gaps.** If the wiki can't fully answer, say exactly what's missing and suggest sources to ingest — don't pad with training-data guesses presented as wiki content.
4. **Auto-file.** If the answer is a synthesis worth keeping (comparison, analysis, discovered connection), save it under `queries/` (or `comparisons/`) WITHOUT asking — write the page with frontmatter + links to its source pages, add an `index.md` line, append `## [YYYY-MM-DD] query | <title>` to `log.md`, and tell 곽경준 it was filed. Skip filing only for one-off fact checks and chit-chat. If the answer required fetching external content, that content goes to `raw/` first (SCHEMA auto-accumulation rule 1). Done when: filed page passes the same linking rules as any other page.

## Answer Formats

Default: markdown in chat. On request: a filed markdown page, comparison table, Marp slide deck, or matplotlib chart — filed outputs live in the wiki like everything else.

## Common Pitfalls

1. Rediscovering from `raw/` when compiled pages exist — that's the RAG habit this wiki replaces. Raw is for ingest-time and citation-checking only.
2. Blending wiki content with unmarked training-data knowledge — cite pages, flag gaps.
3. Letting a good synthesis die in chat history — always offer to file substantial answers.
4. Filing trivial Q&A — `queries/` is for answers with reuse value, not every reply.
5. Ignoring ⚠️ contradiction flags when they bear on the question.

## Verification Checklist

- [ ] index.md consulted before answering
- [ ] Every claim cited to a page or marked as a gap
- [ ] Contradiction flags surfaced where relevant
- [ ] Filing offered for substantial syntheses; filed pages linked + indexed + logged
