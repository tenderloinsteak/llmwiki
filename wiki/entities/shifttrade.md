---
tags: [project, shifttrade, quant, microstructure]
created: 2026-07-16
updated: 2026-07-16
sources: ["repo: Desktop/dev/ShiftTrade (DEVELOPMENT_MAP.md, docs/, hermes/)"]
---
# ShiftTrade (시프트트레이드)

> 가짜 시장에서 진짜처럼 트레이딩을 연습하는 웹 모의투자 앱. 핵심 경쟁력은 "시장이 얼마나 진짜 같은가"다.

## 🌱 쉽게

비행기 조종 시뮬레이터의 트레이딩 버전. 진짜 돈은 안 쓰지만 차트·호가창·체결 내역이 실제 거래소처럼 움직여야 연습이 된다. 그래서 가격을 대충 랜덤으로 만들지 않고, [[shifttrade-tick-engine|가격 엔진]]이 실제 시장의 통계적 특징([[stylized-facts]])을 재현하도록 만드는 게 이 프로젝트의 승부처다. 클라우드(Render)에서 엔진이 24시간 가격을 만들어 DB(Supabase)에 쌓고, 웹 화면(Next.js)이 그걸 받아 그린다.

## ⚙️ 정확히

- 위치: `Desktop/dev/ShiftTrade` — 진입 문서는 `DEVELOPMENT_MAP.md` (모듈식 개발 맵)
- 스택: Next.js(프론트) + Supabase(DB·Auth·Realtime) + Python(가격 엔진) + lightweight-charts
- 런타임 흐름: Render `scripts/cloud_engine.py` → `shiftflow_market_bars` 삽입 → `/api/prices`·RPC → `src/hooks/usePrice.ts` → `TradingChart.tsx`·`OrderBook.tsx`
- 호가창 단일 규칙: `src/lib/orderbook.ts` `buildOrderBookSnapshot` (메인/미니 공용)
- 유저 장부: `shiftflow_trades`가 원본 장부, portfolios/positions는 projection, snapshots는 분석 캐시 — `docs/user-data-and-rollup-plan.md`
- 로컬 데이터 시드: `scripts/generate_ticks.py` (`~/NemotronEngines/engine_4_good.py` 사용, 과거 6개월+미래 6개월 → `public/data/`)
- 작업 표준 정본: `hermes/microstructure-engineer.md`

## 🔗 연결

[[shifttrade-tick-engine]] · [[shifttrade-data-pipeline]] · 담당: [[microstructure-engineer]] · 개념: [[market-microstructure]] [[stylized-facts]] [[order-driven-simulation]]

## 📌 미해결

- 주문주도(order-driven) 시뮬레이션으로의 전환 여부 — FinancialPriceEngine 진화 vs 새 레이어 (표준 문서의 열린 질문)
- 시장 미시구조 참고문헌(교과서·논문) 미축적 — 리서치 대상
