---
name: accountinggo-question-authoring
description: "Use when authoring, editing, or batch-producing AccountingGo quiz questions, explanations, or distractors. Enforces the offline generate→validate→bundle pipeline, English-first authoring, stable questionIds, and the one-defensible-answer bar."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [accountinggo, quiz, content-pipeline, i18n, validation]
    related_skills: [hermes-agent]
---

# AccountingGo Question Authoring

## Overview

The repo's offline pipeline is law: **generate offline → validate → bundle**. The app never invents questions at runtime. Standards: `../AccountingGo/hermes/quiz-writer.md`; before mass production read `docs/QUESTION_GENERATION.md`, `docs/CONTENT_SCHEMA.md`, `docs/CURRICULUM_V1.md`.

## When to Use

- Authoring or editing questions, explanations, or distractors
- Planning a batch (new lesson/chapter content)
- Reviewing draft questions for promotion to `approved`

Don't use for: screen/UX design (learning-ux-designer), curriculum restructuring without approval.

## Authoring Loop (per question)

1. **Pick type & slot.** Choose from the 13 reviewed templates (`tools/content/templates/*.json`) and locate the curriculum slot in `curriculum.json`. Done when: type + lesson slot fixed.
2. **Author in English** (authoring locale; Korean is a translation of the same IDs — `docs/I18N.md`). Copy the template, set `status: "draft"`, save one question per file at `assets/content/en/bank/questions/<id>.json`, append the id to its lesson manifest.
3. **Self-verify the answer.** Exactly one defensible answer; journal entries balance; the question tests the accounting concept, never arithmetic stamina; principles-level scope only. Done when: you can defend the answer and disqualify every distractor.
4. **Design distractors** from real learner mistakes — attractive wrong answers, not random noise.
5. **Write the explanation**: "why correct" + "why that distractor tempts", 2 lines. Prompt ≤ 2 sentences (mobile-first).
6. **Tag** type + difficulty (1–5); confirm `termIds ⊆ glossary.json`, `accountId ∈ accounts.json`.
7. **Validate**: `dart run tools/validate_content.dart --strict`. Done when: strict validation passes.
8. **Review & promote**: accounting + editorial review → `approved` → spot-check in app.

`questionId`s are stable forever — they power analytics, SRS, and future stats. Never recycle or rename.

## Batch Workflow

Before mass production: propose a type/difficulty distribution table and **get approval first**. Done when: 곽경준 approves the table. Then run the authoring loop per question.

## Common Pitfalls

1. Authoring in Korean first — breaks the i18n pipeline.
2. Bypassing validation or hand-editing `approved` files without re-review.
3. Numbers-only clones of existing questions counted as new content.
4. Distractors nobody would pick — they teach nothing.
5. Testing arithmetic stamina instead of the accounting concept.
6. Content above principles-level scope.

## Verification Checklist

- [ ] English-first, template-based, `status` flow respected
- [ ] Exactly one defensible answer, self-checked
- [ ] Distractors mistake-based; explanation covers correct + tempting
- [ ] Tags set; glossary/account references valid
- [ ] `validate_content.dart --strict` passes
- [ ] questionIds new and permanent; batch table approved (if batch)
- [ ] Session logged to `${WIKI_PATH}/memory.md`
