---
tags: [query, accountinggo, accounting-edu]
created: 2026-07-17
updated: 2026-07-17
sources: ["repo: Desktop/dev/AccountingGo/docs/MASTER_POLISH_PLAN.md"]
---
# AccountingGo Master Polish Phase 2–4 마감

> 2026-07-17 Cursor 세션에서 Master Polish Plan Phase 2 잔여 → 3 → 4를 일괄 마감.

## 🌱 쉽게

앱을 “출시 직전” 느낌으로 다듬는 작업의 뒷부분을 끝냈다. 홈에서 이어하기가 맨 위에 오고, 설정에서 소리·진동을 끌 수 있고, 깃허브에서 자동으로 검사한다.

## ⚙️ 정확히

- Phase 2: Home Continue-first + weak-concept teaser, result retention copy
- Phase 3: `.github/workflows/ci.yml`, `docs/RELEASE_CHECKLIST.md`, grader golden tests, a11y Semantics on hearts/progress, `NOT_IMPLEMENTED.md` sync
- Phase 4: FeedbackPrefs + Settings toggles, coin `AgMascotSlot`, AgMotion hotspots, dark progress track
- Bugfix: `JournalEntryGrader` List `==` identity → element-wise compare
- Tests: 46 passed

## 🔗 연결

[[entities/accountinggo]] · [[queries/accountinggo-master-polish-plan-2026-07-17]]

## 📌 미해결

- 출시 전 플래그 false
- ko WIP 커밋 여부
