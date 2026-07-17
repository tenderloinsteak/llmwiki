---
tags: [query, accountinggo, accounting-edu, ui-ux]
created: 2026-07-17
updated: 2026-07-17
sources: ["repo: Desktop/dev/AccountingGo/docs/MASTER_POLISH_PLAN.md", "repo: docs/CURRICULUM_V1.md"]
---
# AccountingGo Master Polish Plan 접수 (2026-07-17)

> 신규 문항 생성 없이 Duolingo급 완성도를 목표로 한 실행 계획. 레포 정본은 `docs/MASTER_POLISH_PLAN.md`.

## 🌱 쉽게

문제는 더 안 만들고, **앱이 문제를 잘 풀어주는 느낌**을 먼저 만든다. 그중에서도 T계정·시산표를 “진짜로 써보게” 만드는 게 열쇠다 — 이게 끝나야 커리큘럼 대량 생산이 열린다.

## ⚙️ 정확히

### 우선순위

| Phase | 내용 | 순서 |
|---|---|---|
| P0 | tAccount / trialBalance / theory grammar | 대량 생성 공식 게이트 — 최우선 |
| P1 | exercise → feedback → result → skill tree 루프 | 체감 퀄리티 |
| P2 | onboarding · 탭 · review · insights | 세션 바깥 흐름 |
| P3 | 테스트 · a11y · i18n · 에러 · 성능 | P0~P2와 병행 가능 |
| P4 | 모션 · SFX · 마스코트 · 마이크로카피 | 마지막 일괄 |

### P0 실측 (2026-07-17)

- `t_account_module.dart` — 216줄, 마감 잔액 입력형 (풀 포스팅 미구현)
- `trial_balance_module.dart` — 166줄, 차/대 배치 스텁
- `theory_scene_player.dart` — `lib/features/exercise/` 하위, 271줄, 레퍼런스 씬 1개
- 모듈 14개 등록 확인
- `AppFeatures.contentReviewUnlockAll` / `refillHeartsOnLaunch` = true (출시 전 false 필수, P3-6)

### 실행 규칙

- 태스크 하나 = Cursor 세션 하나 (권장 시작: **0-1 tAccount**)
- 공통 AC: `./tools/check.sh` 통과, 다크+텍스트 1.3x, 관련 docs 동기화
- 금지: 문항 신규 생성(P0 전), questionId 변경, NOT IMPLEMENTED 플래그 임의 ON
- 브랜치: `cursor/gamification-feedback-i18n-gate` (ko 번역 WIP와 P0 작업 혼선 주의)

### 게이트 출처

`docs/CURRICULUM_V1.md` — mass generation blocked until tAccount posting, trialBalance worksheet, theory grammar freeze (+ pilot templates + SME reviewer).

## 🔗 연결

[[accountinggo]] · [[accountinggo-content-pipeline]] · [[gamified-learning-loop]] · [[learning-ux-designer]] · [[quiz-writer]]

## 📌 미해결

- 다음 세션: **0-1** 착수 여부 확인
- 0-4 모듈 감사표는 플랜 문서 하단 빈 표 — 채운 뒤 커밋
