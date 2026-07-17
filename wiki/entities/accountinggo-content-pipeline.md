---
tags: [system, accountinggo, accounting-edu]
created: 2026-07-16
updated: 2026-07-17
sources: ["repo: Desktop/dev/AccountingGo (docs/QUESTION_GENERATION.md, docs/CONTENT_SCHEMA.md, docs/CURRICULUM_V1.md, docs/MASTER_POLISH_PLAN.md, hermes/quiz-writer.md)"]
---
# AccountingGo 콘텐츠 파이프라인 (Content Pipeline)

> 문제를 만드는 공장. 철칙: 오프라인 생성 → 검증 → 번들. 앱은 절대 즉석에서 문제를 만들지 않는다.

## 🌱 쉽게

교과서 출판사와 같다. 문제는 미리 집필하고, 감수(검증기)를 통과한 것만 책(앱 번들)에 실린다. 수업 중에 즉석 출제하지 않는 이유는 품질을 보장할 수 없어서다. 문제마다 평생 바뀌지 않는 주민번호(questionId)가 있어서, 통계·복습 시스템이 그 번호로 학습자를 추적한다. 집필 언어는 영어이고 한국어는 같은 번호의 번역본이다([[accountinggo-i18n]]).

지금은 **공장 문을 아직 열면 안 된다**. T계정·시산표 인터랙션과 theory grammar가 먼저 완성되어야 한다([[queries/accountinggo-master-polish-plan-2026-07-17|Master Polish P0]]).

## ⚙️ 정확히

- 흐름: 템플릿 복사 → `status: "draft"` → `assets/content/en/bank/questions/<id>.json`(1문제 1파일) → 레슨 manifest에 id 추가 → `termIds ⊆ glossary.json`, `accountId ∈ accounts.json` 확인 → `dart run tools/validate_content.dart --strict` → 회계·편집 감수 → `approved` 승격 → 앱 스팟체크
- 품질 기준: 정답 정확히 1개(자가검증, 분개는 대차평형) / 오답은 실제 학습자 실수 기반 / 발문 ≤2문장 / 해설 = "왜 정답 + 왜 그 오답이 유혹적" 2줄 / 유형+난이도(1–5) 태그
- questionId 불변 — 재활용·개명 금지 (통계·SRS·향후 지표의 기반)
- 대량 생산 전 필독: `docs/QUESTION_GENERATION.md`, `CONTENT_SCHEMA.md`, `CURRICULUM_V1.md` + 유형·난이도 분포표 승인
- **P0 게이트** (`CURRICULUM_V1.md` + `MASTER_POLISH_PLAN.md` 0-1~0-3): tAccount 라인 포스팅, trialBalance 멀티행 워크시트, theory grammar 동결(레퍼런스 씬 2 + Reduce Motion). 게이트 해제 전 문항 신규 생성 금지
- 커리큘럼 트리: `curriculum.json`

## 🔗 연결

[[accountinggo]] · [[accountinggo-i18n]] · [[accountinggo-mastery-system]] · [[queries/accountinggo-master-polish-plan-2026-07-17]] · 담당: [[quiz-writer]] · 개념: [[double-entry-bookkeeping]]

## 📌 미해결

- P0 게이트 미해제 — 대량 생성 차단
- 현재 문제 뱅크 규모·유형 분포 집계 미기록 — 다음 배치 전 집계
