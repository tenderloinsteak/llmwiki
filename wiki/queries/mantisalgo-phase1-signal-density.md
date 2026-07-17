---
tags: [mantisalgo, signal-density, pine-script]
created: 2026-07-17
updated: 2026-07-17
sources: ["repo: MantisAlgo/docs/IMPROVEMENT_PLAN_2026-07-17.md"]
---
# MantisAlgo Phase 1 — 신호 밀도 엔진

> 확정 신호를 심볼×TF 매트릭스에서 측정·캘리브레이션·게이트화.

## 🌱 쉽게
차트가 너무 자주 울리면 환불 위험이 크다. 그래서 "100봉당 몇 번 쏘는지"를 재고, 목표 구간 안으로 파라미터를 맞춘 뒤, 안 맞으면 출고를 막는다.

## ⚙️ 정확히
- `mantis/signal_mirror.py` — BOS/FVG/EQH·sweep/OB/RSI/MACD/EMA/ST/ORB 미러
- `mantis/signal_calibrator.py` — grid search → `extra.calibration`
- `config/signal_density_targets.json` — profile bands (swing/intraday/scalp)
- `generators/.../sig_governor.py` — cooldown + one-per-leg + ★ (INFRA_ALWAYS)
- 데이터: `data/ohlcv/` 3심볼×3TF (`scripts/fetch_ohlcv.py`)
- 게이트: `scripts/factory_gate.py` dens FAIL if missing/out-of-band
- 상태 (2026-07-17): 8/8 SKU in-band, registry 174 live

## 🔗 연결
- [[entities/mantisalgo]]
- [[entities/mantisalgo-verification-gate]]
- [[entities/mantisalgo-sku-catalog]]

## 📌 미해결
- Phase 2 비주얼 v2
- 실데이터 yfinance 교체 (`--source yfinance`)
- confirm 모듈이 governor 훅을 더 깊게 통과하도록 추가 리팩터
