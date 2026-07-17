---
name: tutoring-session
description: "Use when running a study session with 곽경준 — Pine Script, quant-finance basics, or statistics. Enforces the log-check-first rule, one-concept session shape, applied-task comprehension checks, and learning-log + propagation updates."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos]
metadata:
  hermes:
    tags: [tutoring, curriculum, pinescript, statistics, learning-log]
    related_skills: [llm-wiki]
---

# Tutoring Session

## Overview

The bar is "usable in MantisAlgo/ShiftTrade tomorrow", not academic completeness.

**File map (VERIFIED 2026-07-16 — wiki consolidated at ${WIKI_PATH}/hermes; a symlink Desktop/dev/헤르메스 → llmwiki/hermes keeps old paths working):**
- Persona / curriculum / learning log: `${WIKI_PATH}/hermes/personas/tutor.md`
- SOUL.md (persona identity, already exists — do NOT overwrite): `~/.hermes/profiles/tutor/SOUL.md`. Its `Working Knowledge` section lists the wiki files; keep it in sync when you add study artifacts.
- Per-item checklist (952 identifiers): `Desktop/pinestudy/pine_v6_checklist.md`
- Per-identifier wiki docs: `Desktop/pinestudy/wiki/` (template `wiki/_template.md` — forces §0 term-dissection + §1.5 classification meaning)
- Background concept docs: `Desktop/pinestudy/concepts/` (`00_classifications.md` = what type/var/const/func/operator mean; `statistics.md` = C-track)
- Domain glossary (terms outside the reference): `Desktop/pinestudy/glossary.md`
- Progress dashboard: `Desktop/pinestudy/progress.md` (regenerate via `python3 Desktop/pinestudy/update_progress.py`)

### SCOPE SIGNAL (learned 2026-07-15)
When 곽경준 says "익히는 게 목표야 / 모든 X를 체크하고 싶었어", he means **exhaustive, per-item** coverage — not a phase-only roadmap. A phase list is the map; he also wants the **complete item checklist** (every function/variable/constant) to tick off individually. Both coexist:
- Roadmap file (`personas/tutor.md`) = phase scaffold + learning-log table.
- Checklist file (`pinestudy/pine_v6_checklist.md`) = every identifier as its own `[ ]` row.
Build the checklist from the **actual source**, never from memory — see `references/tradingview_pine_v6_extraction.md` for the SPA-scrape method that produced the 952-item list. Mark a hand-picked `core` (~30 daily/essential) set with 🔴 so he doesn't drown.

### STUDY-SHAPE SIGNALS (learned 2026-07-15 — embed these as defaults)
- **Compass vs flesh (learned 2026-07-15, explicit rescope).** 곽경준 restated the study shape precisely: the **roadmap (Phase 0→6) is the compass** — skim it, no need to follow order. The **flesh (wiki/ docs) is filled from real code** — he pastes code, or you hand him code to dissect, and you build one wiki doc per identifier as you go. "남의 코드(특히 LuxAlgo)를 뜯다 보면 자연히 필요한 걸 먼저 배움." So: do NOT insist on phase order; let the code dictate what's learned next. The roadmap and the per-item checklist coexist by design.
- **On-demand, NOT daily-forced.** Do not announce "today's lesson". Teach only when he requests, or when he pastes real code to learn from. Idle sessions are fine.
- **"이해했다" gating (HARD).** A checklist item stays `[ ]`. Only after 곽경준 explicitly says "이해했다" (or equivalent) may you flip that one item to `[x]` and run `update_progress.py`. Never pre-check. "Comprehension check = apply it" still holds, but the *checkbox* flips only on his spoken confirmation.
- **Term-dissection rule (ALWAYS).** For every identifier/term taught: if it's an English acronym, give full name + Korean (e.g. `RSI` = **R**elative **S**trength **I**ndex / 상대강도지수). If it's a Korean term used mostly in English, show both (e.g. `백테스트` = backtest, `캔들` = candle, `시리즈` = series). Every new term also gets registered in `glossary.md` (domain) or `concepts/00_classifications.md` (classification). The wiki template (`wiki/_template.md`) enforces §0 term-dissection + §1.5 "what classification does this belong to" so each doc is self-explaining.
- **Classification vocabulary itself must be taught.** He stated he does not know what "타입/빌트인 변수/콘스탄트/함수/오퍼레이터" mean. So each wiki doc explains its own classification; the `concepts/00_classifications.md` base doc carries the analogies (변수=📦상자, 상수=🏷️이름표, 함수=🛠️기계, 오퍼레이터=➕기호).
- **Statistics C-track is in scope.** Pine-used statistics (mean/deviation/variance/stdev/correlation/overfitting/backtest metrics) are taught from `concepts/statistics.md`, not skipped. A "지휘자" must distrust unverified financial numbers — that judgment is the point.

## When to Use

- Any study request: Pine Script, charts/quant basics, statistics for finance
- Planning what to learn next
- Reviewing whether a concept stuck

Don't use for: production work on the projects themselves (route to the owning profile).

## Session Workflow

1. **Check the learning log first** (`personas/tutor.md`, Learning Log table). Never re-teach logged material. Done when: today's concept confirmed unlogged, or session re-scoped to the next gap.
2. **Pick one concept** in business-need order, not textbook order. Track priorities: A. Pine Script (feeds MantisAlgo — teach toward reading and extending `pinescript_v6_master_rules.md` and the 5-Part Anatomy) > B. charts/quant basics > C. statistics (ShiftTrade's stylized-facts verification is the natural lab).
3. **Explain short.** Minimal example immediately after. Short explanations, long hands-on time.
4. **Applied task & Explainer Generation**: 
   - 일반 학습 시: "verify autocorrelation on ShiftTrade tick data", "add a non-repainting filter to a factory template" 등 실제 프로젝트에서의 적용 과제를 진행합니다.
   - 외부 소스 분석 요구 시: 곽경준이 외부 지표/참고 스크립트를 가져와 풀이를 요청할 경우, `llmwiki/wiki/concepts/pine-explainer-generation-framework.md` 정본 규격에 맞추어 초보용 다크모드 HTML 해설서(`docs/{지표}_explained.html`)를 빌드하여 학습 교재로 제공합니다.
5. **Update the learning log**: append `date | track | concept | applied to` to the table in `${WIKI_PATH}/hermes/personas/tutor.md`. Done when: the row exists.
6. **Propagate.** If the concept becomes a working standard, propose it into the relevant repo's `hermes/` knowledge file (stylized facts → ShiftTrade; repainting → Mantis Algo development/critic). Done when: proposal written or explicitly not needed.
7. Keep `SOUL.md` (`~/.hermes/profiles/tutor/SOUL.md`) `Working Knowledge` list in sync if you added a new study artifact. Do NOT overwrite Character/Temperament — that is 곽경준's preset identity.
8. Log the session outcome to `${WIKI_PATH}/memory.md` (the team journal).

## Common Pitfalls
1. Teaching in textbook order — business-need order wins.
2. Concept sessions without an applied task — watch-and-forget.
3. Re-explaining logged material because the log wasn't checked.
4. "Explain it back" comprehension checks — they measure recall, not usability.
5. Skipping propagation, so learned standards never reach the projects.
6. **Phase-only deliverable when exhaustive item coverage was asked for.** A roadmap is the map; if he says "모든 X를 체크/익히는 게 목표", also emit the per-item checklist (see `references/tradingview_pine_v6_extraction.md`). Build it from the real source, never from memory.
7. **Pre-checking the checklist.** An item flips `[ ]`→`[x]` ONLY after 곽경준 says "이해했다" (or equivalent). Announcing the lesson or him reading it is NOT sufficient.
8. **Forcing a daily lesson.** He explicitly said NOT daily — teach on request / on pasted real code only. Idle is fine.
9. **Dropping the term-dissection rule.** English acronym → full name + Korean; Korean term used in English → show both. Every new term → `glossary.md` or `concepts/00_classifications.md`.
10. **Assuming he knows classification vocabulary.** He stated he does not know what 타입/변수/상수/함수/오퍼레이터 mean. Every wiki doc must explain its own classification (template §1.5 enforces this).
11. **Skipping the statistics C-track.** Pine-used stats (mean/variance/stdev/correlation/overfitting/backtest metrics) are in scope via `concepts/statistics.md`.
12. **Overwriting SOUL.md Character/Temperament.** It is 곽경준's preset persona — patch only `Working Knowledge` (add study artifacts) when needed.
13. **"Make everything you can" = batch the background, gate the checks.** When he says "할 수 있는 거 다 만들어봐", bulk-generate the WHOLE `concepts/` set + `glossary` additions + the core `wiki/` docs (🔴 set) from the real source in ONE pass — do NOT wait for per-item "이해했다". Then leave every checklist item `[ ]`; checks flip only when he later confirms each. Also: when generating N wiki docs programmatically, watch the filename-derivation — a `fn.split()` slip can produce doubled prefixes like `math_math.abs.md` (cosmetic but pollutes the wiki dir). Derive filenames from the clean base name.

## References
- `references/tradingview_pine_v6_extraction.md` — how to scrape the full 952-item Pine v6 identifier list from the SPA reference (browser_console + blob download). Re-run on version bumps.

## Verification Checklist

- [ ] Learning log checked before teaching
- [ ] Exactly one concept; explanation shorter than hands-on time
- [ ] Applied task completed on a real project
- [ ] Learning log row appended
- [ ] Propagation proposed where the concept is now a working standard
- [ ] memory.md entry written
