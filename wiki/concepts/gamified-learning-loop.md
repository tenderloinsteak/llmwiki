---
tags: [concept, learning-science, accountinggo]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/AccountingGo/hermes/learning-ux-designer.md"]
---
# 게임화 학습 루프 (Gamified Learning Loop)

> 듀오링고가 증명한 "공부를 계속하게 만드는 보상 회로". AccountingGo의 설계 기반.

## 🌱 쉽게

헬스장 앱이 "3일 연속 출석!"으로 나를 붙잡듯, 학습 루프는 심리 보상으로 학습을 붙잡는다. 공식: 짧은 세션(3~5분, 부담 제로) → 즉각 피드백(0.5초 내 정답/오답, 색·소리·진동) → 보상(XP·스트릭·레벨) → 눈에 보이는 진도(챕터 지도, "3문제 남음") → 내일 또 오게 하는 장치(스트릭). 핵심 반전: 벌은 역효과 — 하트 깎기식 벌점은 이탈을 부르니, 실수엔 벌 대신 복습([[spaced-repetition]])과 회복 장치(스트릭 프리즈)를 준다.

## ⚙️ 정확히

- AccountingGo 수치 기준: 세션 3~5분 / 레슨 8~12문제 / 피드백 0.5초 내 / 첫 실행 3분 내 첫 정답 경험
- 구성 요소: 스트릭, XP, 레벨, 챕터 완료, 진도 시각화, 스트릭 프리즈(회복)
- 명시적 배제: 하트 게이팅(체력 소진식 차단) — 이탈 유발로 판단, 무비판 복제 금지
- 원칙: 듀오링고는 기준선(baseline)이지 복사 대상이 아님 — 회계 도메인에 맞게 재해석
- 구현 연결: 축하 서비스·숙련도·분석·기능 플래그 등 기존 시스템 위에 구축 ([[accountinggo]])

## 🔗 연결

[[accountinggo]] · [[accountinggo-mastery-system]] · [[spaced-repetition]] · 담당: [[learning-ux-designer]]

## 📌 미해결

- 스트릭·XP 수치 밸런싱 근거 자료(듀오링고 연구·블로그) 인제스트 후보
