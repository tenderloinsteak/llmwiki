---
tags: [concept, pine-script]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/pinestudy/concepts/", "Desktop/dev/llmwiki/hermes/personas/tutor.md"]
---
# 시리즈 (Series) vs 배열 (Array)

> Pine의 핵심 개념. 값이 "봉마다 하나씩 자동으로 생기는 줄"이며, 일반 언어의 배열과 다르다.

## 🌱 쉽게

사탕 기계 비유: 봉(캔들)이 하나 지나갈 때마다 기계가 사탕(값)을 하나씩 뱉는다. `close`는 "매 봉의 종가"라는 사탕 줄 전체를 뜻하고, `close[1]`은 "한 봉 전 사탕"이다. 내가 반복문을 돌리지 않아도 차트의 모든 봉에 대해 코드가 자동으로 다시 실행된다. 이걸 이해하면 "왜 Pine에선 for문을 잘 안 쓰는지", "왜 `var`로 선언한 변수만 누적되는지"가 풀린다.

## ⚙️ 정확히

- 실행 모델: bar-by-bar — 스크립트 전체가 각 봉에서 1회 실행 (실시간 봉에서는 틱마다 재실행 → [[repainting]] 원인)
- 과거 참조: `[n]` 히스토리 연산자 (`close[1]` = 직전 봉 종가)
- `var` 선언 = 초기화 1회 후 봉 간 유지, 일반 선언 = 봉마다 재초기화
- simple vs series 타입 구분: 입력 시점에 고정되는 값 vs 봉마다 변하는 값 — 함수 인자 제약의 원인
- Pine의 `array.*`는 별도 자료구조(한 봉 안에서 쓰는 진짜 배열, 55개 함수)로 시리즈와 다름

## 🔗 연결

[[pine-script]] · [[repainting]] · 학습: [[tutor]] (Phase 1, 가장 중요 단계)

## 📌 미해결

- `request.security()`와 시리즈의 상호작용 — 리페인팅 학습 시 함께 정리
