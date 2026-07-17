---
tags: [concept, learning-science, accountinggo]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/AccountingGo/docs/MASTERY.md", "Desktop/dev/AccountingGo/hermes/learning-ux-designer.md"]
---
# 간격 반복 (Spaced Repetition, SRS)

> 잊어버릴 때쯤 다시 보여주면 기억이 오래 간다는 원리. 틀린 문제를 "벌"이 아니라 "예약 복습"으로 처리하는 근거.

## 🌱 쉽게

벼락치기로 외운 건 시험 끝나면 증발하지만, 며칠 간격으로 세 번 본 건 오래 남는다. 뇌는 "다시 만난 정보"를 중요하다고 판단하기 때문이다. 그래서 AccountingGo는 틀린 문제를 감점하고 끝내는 게 아니라 복습 대기열에 넣고, 잊혀질 타이밍(숙련도 점수가 70 아래로 떨어질 때)에 다시 내민다. SRS = **S**paced **R**epetition **S**ystem(간격 반복 시스템).

## ⚙️ 정확히

- AccountingGo 구현: [[accountinggo-mastery-system]] — 최근 10회 정답률 × 7일 반감기 감쇠, 유효점수 <70 → "Concept refresh"
- 오답 처리 원칙: 페널티 박스가 아니라 SRS 큐 (learning-ux 표준)
- 추적 키: questionId·용어(termId) — 불변 ID 덕에 언어·세션을 넘어 이력 유지
- 이론 배경: 망각곡선(단순화 적용, Ebbinghaus 원표 아님)

## 🔗 연결

[[accountinggo-mastery-system]] · [[gamified-learning-loop]] · [[accountinggo]] · 담당: [[learning-ux-designer]] [[quiz-writer]]

## 📌 미해결

- 회계 학습에 최적인 복습 간격 — 실데이터로 반감기 검증 (mastery 페이지와 공유)
