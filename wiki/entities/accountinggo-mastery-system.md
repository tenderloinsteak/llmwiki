---
tags: [system, accountinggo, learning-science]
created: 2026-07-16
updated: 2026-07-16
sources: ["repo: Desktop/dev/AccountingGo (docs/MASTERY.md, docs/QUESTION_ANALYTICS.md)"]
---
# AccountingGo 숙련도 시스템 (Mastery System)

> 학습자가 각 회계 개념을 "지금" 얼마나 알고 있는지 점수화하고, 잊혀질 때쯤 복습을 밀어주는 시스템.

## 🌱 쉽게

근육과 같다 — 안 쓰면 빠진다. 이 시스템은 개념(용어)마다 최근 10번의 정답 여부를 기억하고, 마지막으로 푼 지 오래될수록 점수를 깎는다(7일 지나면 절반). 점수가 70 아래로 떨어지면 "복습 대상"이 되어 다시 나온다. 벌점이 아니라 리마인더다 — 틀렸다고 혼내는 게 아니라 잊기 전에 다시 보여주는 것([[spaced-repetition]]).

## ⚙️ 정확히

- 코드: `lib/domain/services/mastery_service.dart` (MasteryService)
- 모델: 용어별 최근 10회 결과 비트스트링 → 정답률% × 0.5^(경과일/7) 반올림 = 유효 점수
- 임계: 유효 점수 < 70 → Review "Concept refresh" 노출
- 반감기 7일 = 단순화한 망각곡선 (Ebbinghaus 원표 아님)
- 레거시 행은 lifetime correct/wrong으로 부트스트랩
- 폐기된 설계: 불투명 델타(+5/−8) — 설명 불가능해서 정답률 기반으로 교체
- 연계: 오답 → SRS 큐 (하트 차감식 벌점 구조는 의도적으로 배제), 분석·AI 코치는 `docs/QUESTION_ANALYTICS.md`, `AI_COACH_OPERATIONS.md`

## 🔗 연결

[[accountinggo]] · [[accountinggo-content-pipeline]](questionId가 추적 키) · 담당: [[learning-ux-designer]](UX 연동) [[quiz-writer]](콘텐츠 태그) · 개념: [[spaced-repetition]] [[gamified-learning-loop]]

## 📌 미해결

- 반감기 7일이 회계 도메인에 적절한지 — 실사용 데이터 쌓이면 검증
