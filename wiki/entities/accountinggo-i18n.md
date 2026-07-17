---
tags: [system, accountinggo]
created: 2026-07-16
updated: 2026-07-17
sources: ["repo: Desktop/dev/AccountingGo (docs/I18N.md, README.md)"]
---
# AccountingGo 다국어 체계 (I18N — English First)

> 영어가 원본, 한국어는 같은 ID의 번역본. 순서를 뒤집으면 파이프라인이 깨진다.

## 🌱 쉽게

원서와 번역서의 관계다. 문제의 원본은 항상 영어로 먼저 쓰고, 한국어판은 같은 문제번호(questionId)를 달고 번역만 바뀐다. 이렇게 하면 통계 시스템 입장에서 "영어로 풀든 한국어로 풀든 같은 문제"로 집계되고, 나중에 다른 언어를 추가할 때도 원본 하나에 번역만 붙이면 된다. 한국 앱인데 왜 영어 먼저냐고 묻는다면: 구조의 문제다. 원본이 하나여야 번역이 늘어나도 관리가 된다.

## ⚙️ 정확히

- 정본 문서: `docs/I18N.md` (새 관리자 필독 1순위)
- 규칙: authoring locale = English (`assets/content/en/`), 한국어는 동일 ID·경로 구조의 번역
- questionId·경로는 언어 간 공유 — 분석·SRS·숙련도가 언어 불문 동일 키로 동작
- 위반 시나리오(금지): 한국어로 먼저 집필 → 영어 번역 — ID 정합성과 검증 순서가 깨짐
- 로케일 추가 방법: `docs/MODULE_GUIDE.md`

## 🔗 연결

[[accountinggo]] · [[accountinggo-content-pipeline]] · [[accounting-terminology-matrix]] · [[accounting-terminology-registry-index]] · 담당: [[quiz-writer]]

## 📌 미해결

- 다국어 표시 용어 SoT: [[accounting-terminology-registry-index]] (314). ko 검수·타언어 PENDING 채움
- 한국어 번역 커버리지 현황 집계 미기록
