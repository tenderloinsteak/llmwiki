---
tags: [project, accountinggo, accounting-edu]
created: 2026-07-16
updated: 2026-07-17
sources: ["repo: Desktop/dev/AccountingGo (README.md, docs/, hermes/)", "repo: docs/MASTER_POLISH_PLAN.md"]
---
# AccountingGo (어카운팅고)

> "회계원리의 듀오링고" — 회계를 3~5분짜리 게임 같은 세션으로 배우는 Flutter 모바일 앱. 현재 Phase 1 MVP(오프라인, 서버 없음).

## 🌱 쉽게

듀오링고가 외국어를 가르치듯 회계를 가르친다. 짧은 세션, 즉각 피드백, 스트릭·XP 같은 보상 고리([[gamified-learning-loop]])로 꾸준히 하게 만들고, 틀린 문제는 [[spaced-repetition|간격 반복]] 큐로 다시 나온다. 문제는 앱이 즉석에서 만들지 않는다 — 공장([[accountinggo-content-pipeline|콘텐츠 파이프라인]])에서 미리 만들어 검증한 것만 앱에 실린다. 의도적으로 안 만든 기능(서버, 광고, 결제)이 문서화되어 있어서, 디자인·개발 전에 반드시 확인해야 한다.

2026-07-17부터 **Master Polish Plan**으로 신규 문항 생성 없이 앱 완성도를 끌어올리는 실행 트랙이 열렸다. 대량 콘텐츠 생산은 P0 게이트(tAccount·trialBalance·theory grammar)가 풀리기 전까지 금지.

## ⚙️ 정확히

- 위치: `Desktop/dev/AccountingGo` — 진입 문서는 `README.md` → docs/ 순서: I18N → OPERATIONS → QUESTION_ANALYTICS → AI_COACH_OPERATIONS → NOT_IMPLEMENTED
- 스택: Flutter, 로컬 SQLite 진행도, JSON 레슨, dev 로그인(아무 이메일+6자 비번)
- 실행: `flutter pub get` → `./tools/check.sh`(검증+분석+테스트) → `flutter run`
- 기능 플래그 정본: `lib/core/config/app_features.dart` (앱 내 Settings → System status로 확인)
- 문제 유형: 앱 모듈 14종 등록 / 템플릿 `tools/content/templates/*.json` — 그중 `tAccount`(잔액만 입력, 216줄), `trialBalance`(배치 스텁, 166줄)가 P0 스텁
- Theory player: `lib/features/exercise/theory_scene_player.dart` (271줄), 레퍼런스 씬 `s1_u2_equation_flyin` 1개
- 콘텐츠: `assets/content/en/` 편집 → `dart run tools/validate_content.dart` → 리빌드
- 숙련도 모델: 최근 10회 정답률 × 반감기 7일 지수감쇠, 70 미만이면 복습 대상 (`docs/MASTERY.md`)
- 작업 표준 정본: `hermes/quiz-writer.md`, `hermes/learning-ux-designer.md`
- **폴리시 실행 정본**: `docs/MASTER_POLISH_PLAN.md` (P0→P1→P2 순차, P3 병행, P4 마지막). 태스크 1개 = Cursor 세션 1개
- 활성 브랜치(2026-07-17): `cursor/gamification-feedback-i18n-gate` — ko 번역 대량 uncommitted + 개발 플래그 `contentReviewUnlockAll`/`refillHeartsOnLaunch` = true

## 🔗 연결

[[accountinggo-content-pipeline]] · [[accountinggo-mastery-system]] · [[accountinggo-i18n]] · [[queries/accountinggo-master-polish-plan-2026-07-17]] · 담당: [[quiz-writer]] [[learning-ux-designer]] · 개념: [[gamified-learning-loop]] [[spaced-repetition]] [[double-entry-bookkeeping]]

## 📌 미해결

- P0 게이트 미해제: tAccount 풀 포스팅, trialBalance 워크시트, theory grammar 동결 — 대량 생성 차단 중 (`CURRICULUM_V1.md`)
- Phase 2(서버·계정 동기화) 시점 미정 — NOT_IMPLEMENTED 목록이 현재 경계
- 듀오링고 외 학습앱 벤치마크 리서치 미축적 — 리서치 대상
