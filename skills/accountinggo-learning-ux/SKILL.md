---
name: accountinggo-learning-ux
description: "Use when designing AccountingGo screens, reward loops, storyboards, or explainer animations. Enforces the NOT_IMPLEMENTED pre-check, build-on-existing-systems rule, 3–5 minute session shape, and the storyboard deliverable format."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [accountinggo, ux, gamification, storyboard, duolingo]
    related_skills: [accountinggo-question-authoring]
---

# AccountingGo Learning UX Design

## Overview

Duolingo is the baseline, reinterpreted for accounting — never copied. The app is a Flutter Phase-1 MVP (offline, no backend, no ads/IAP by design). Standards: `../AccountingGo/hermes/learning-ux-designer.md`.

## When to Use

- Designing screens, flows, reward mechanics, or progress UI
- Storyboarding a concept-explainer animation
- Reviewing a proposed learning flow

Don't use for: writing question content (quiz-writer), implementing Flutter code without a design pass.

## Pre-flight (before any design)

1. Read `docs/NOT_IMPLEMENTED.md` + `lib/core/config/app_features.dart`. **Never design against intentionally-unbuilt features** (e.g., server features). Done when: the design's dependencies are confirmed implemented or flagged.
2. Inventory existing systems to build on, never duplicate: celebration service, mastery system (`docs/MASTERY.md`), analytics + AI coach (`docs/QUESTION_ANALYTICS.md`, `docs/AI_COACH_OPERATIONS.md`), feature flags. Done when: each design element maps to an existing system or is explicitly new.
3. Question formats must match the 13 implemented types — coordinate with quiz-writer.

## Design Rules

- Session = 3–5 minutes; one lesson = 8–12 questions.
- Instant feedback: verdict within 0.5s — color, sound, haptics.
- Reward loop: streaks, XP, levels, chapter completion. Recovery devices (streak freeze) over punishment.
- Progress visible: chapter map, progress bar, "N questions left".
- Wrong answers → spaced-repetition queue, never a penalty box (aligns with mastery system).
- No walls of text; every screen one-thumb operable; visuals map logically to accounting concepts.

## Explainer Animations

- One concept = one metaphor (debit/credit = a scale; a transaction = weights on both sides).
- ≤ 15 seconds; one sentence of text per screen.
- Immediately followed by 1 applied question — no watch-and-forget videos.

## Deliverables

- **Storyboard**: table of `scene # | screen | motion | caption`.
- **Wireframes**: format-compatible with the 13 question types.

Done when: deliverable uses these exact formats and names the existing systems it plugs into.

## Quality Bar (definition of done)

- One-thumb operable, mobile-first
- First correct-answer experience within 3 minutes of first launch
- Visuals map to accounting concepts (not decoration)
- Dark mode + color-blind contrast addressed
- Uses existing services/flags, no parallel systems

## Common Pitfalls

1. Designing on top of NOT_IMPLEMENTED features.
2. Cloning Duolingo mechanics uncritically (heart-gating churn) instead of reinterpreting.
3. Metaphor-free animations that explain terms with terms.
4. Inventing a parallel celebration/analytics system.
5. Textbook-on-a-screen walls of text.

## Verification Checklist

- [ ] NOT_IMPLEMENTED + feature flags checked before design
- [ ] Every element mapped to an existing system or flagged as new
- [ ] Session/feedback/reward rules respected
- [ ] Storyboard/wireframe in the required format
- [ ] Quality bar fully met; logged to `${WIKI_PATH}/memory.md`
