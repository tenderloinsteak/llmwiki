---
tags: [system, shifttrade]
created: 2026-07-16
updated: 2026-07-16
sources: ["repo: Desktop/dev/ShiftTrade (DEVELOPMENT_MAP.md, docs/user-data-and-rollup-plan.md, scripts/)"]
---
# ShiftTrade 데이터 파이프라인 (tick → 집계 → Supabase → 화면)

> 엔진이 만든 가격이 화면까지 가는 물길, 그리고 유저 거래 기록이 저장되는 장부 체계.

## 🌱 쉽게

강물이 흐르듯: 클라우드(Render)의 엔진이 쉬지 않고 가격 방울(tick)을 만들어 저수지(Supabase DB)에 붓고, 웹 화면은 저수지에서 물을 끌어다 차트를 그린다. 유저의 거래는 은행 원장처럼 관리된다 — 체결 기록(trades)이 원본이고, 잔고나 수익률 화면은 원본에서 계산해 보여주는 사본이다. 사본이 꼬여도 원본에서 언제든 다시 계산할 수 있어야 한다.

## ⚙️ 정확히

- 시세 흐름: Render `scripts/cloud_engine.py` → `public.shiftflow_market_bars` → `/api/prices`(주) + RPC `get_aggregated_bars`(예비, 3.5초 레이스) → `src/hooks/usePrice.ts` → 차트·호가창. 이후 Realtime INSERT + REST 폴링
- 유저 장부: `shiftflow_trades`(원본) → 같은 트랜잭션에서 `shiftflow_portfolios`·`shiftflow_positions`·`shiftflow_orders` 갱신 (projection)
- 분석 캐시: `shiftflow_portfolio_snapshots` — 5분봉 30~90일 / 1시간봉 1~3년 / 1일봉 영구
- 보조 스크립트: `build_aggregates.py`, `run_market_rollup.py`, `archive_ticks.py`, `upload_archive_to_supabase.py`
- 전역 설정: `shiftflow_app_settings` (공지·수수료·티커·초기자금, 어드민 관리)
- 제약: 엔진 변경은 이 파이프라인 호환을 깨면 안 됨

## 🔗 연결

[[shifttrade]] · [[shifttrade-tick-engine]] · 담당: [[microstructure-engineer]]

## 📌 미해결

- 로그인 이후 단계별 구현(rollup 운영안) 진행 상태 추적 필요
