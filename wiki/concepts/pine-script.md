---
tags: [concept, pine-script]
created: 2026-07-16
updated: 2026-07-16
sources: ["https://kr.tradingview.com/pine-script-reference/v6/", "Desktop/pinestudy/"]
---
# Pine Script (파인 스크립트)

> TradingView 차트 위에서 도는 전용 프로그래밍 언어. MantisAlgo가 만들어 파는 제품이 이 언어로 쓰인다.

## 🌱 쉽게

엑셀 수식이 엑셀 안에서만 돌 듯, Pine Script는 TradingView 차트 안에서만 돈다. 용도는 딱 두 가지: 지표(indicator — 차트에 선·신호를 그림)와 전략(strategy — 매수·매도 규칙을 정해 백테스트). 일반 언어와 가장 다른 점은 코드가 "봉(캔들)마다 한 번씩" 자동으로 다시 실행된다는 것 — 이게 [[series-vs-array|시리즈]] 개념이고, Pine 이해의 절반이다.

## ⚙️ 정확히

- 현행 버전: v6 (`//@version=6` 필수)
- 공식 레퍼런스: https://kr.tradingview.com/pine-script-reference/v6/ — 식별자 총 952개(타입 20·변수 193·상수 216·함수 479·키워드 14·연산자 20·어노테이션 10)
- 학습 정본: `Desktop/pinestudy/` (체크리스트·식별자별 위키·용어집) — 이 위키와 별도 운영
- MantisAlgo 생산 규칙 정본: `Desktop/dev/MantisAlgo/pinescript_v6_master_rules.md`
- indicator ≠ strategy: 템플릿·검증 분리 (비양보 규칙 #2)

## 🔗 연결

[[series-vs-array]] · [[repainting]] · [[5-part-anatomy]] · 쓰이는 곳: [[mantisalgo]] · 배우는 사람: [[tutor]]

## 📌 미해결

- v6 → v7 변경 시 체크리스트 재추출 필요 (레퍼런스 SPA 스크레이핑 방법 문서화되어 있음)
