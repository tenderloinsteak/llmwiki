---
tags: [system, shifttrade, quant, microstructure]
created: 2026-07-16
updated: 2026-07-16
sources: ["repo: Desktop/dev/ShiftTrade (hermes/microstructure-engineer.md, scripts/)", "~/NemotronEngines/engine_4_good.py"]
---
# ShiftTrade 가격 엔진 (Tick Engine)

> 가짜 시장의 심장. 가격·호가·체결을 만들어내며, "진짜 같음"의 통계적 기준([[stylized-facts]])을 만족해야 한다.

## 🌱 쉽게

날씨 시뮬레이터가 "그럴듯한 비"를 만들려면 실제 기상 통계를 따라야 하듯, 가격 엔진도 실제 시장의 통계 지문을 따라야 한다. 지켜야 할 철칙: 가격을 먼저 만들고 호가창을 나중에 꾸미면 안 된다. 주문 이벤트를 만들면 가격·호가·체결이 함께 자연스럽게 나오게 해야([[order-driven-simulation]]) 셋이 서로 모순되지 않는다. "눈으로 보기에 그럴듯함"은 완성 기준이 아니다 — 통계 테스트 코드가 통과해야 완성이다.

## ⚙️ 정확히

- 엔진 정본: `~/NemotronEngines/engine_4_good.py` (`FinancialPriceEngine`) — repo 밖 홈 폴더
- 소비자: `scripts/generate_ticks.py` (과거 6개월+미래 6개월 시드 → `public/data/`), Render 상시 실행 `scripts/cloud_engine.py`
- 미리보기: `scripts/preview_engine.py`, `preview_market_dynamics.py`
- 완성 정의: ①stylized facts 통계 재현(검증 코드 포함) ②호가·체결·차트 무모순 ③시나리오 주입 지원(급등·투매·횡보·상하한) ④스캘핑급 리플레이 속도
- 호가 규칙: 최우선호가 근처 깊이 집중, 스프레드는 변동성 연동, 대량 체결 후 깊이 회복
- 체결강도 = 매수 체결량 vs 매도 체결량, 테이프와 호가 변화 일관성 유지

## 🔗 연결

[[shifttrade]] · [[shifttrade-data-pipeline]] · 담당: [[microstructure-engineer]] · 개념: [[order-driven-simulation]] [[stylized-facts]] [[market-microstructure]]

## 📌 미해결

- FinancialPriceEngine을 주문주도형으로 진화시킬지, 위에 레이어를 얹을지 — 아키텍처 결정 대기
- 에이전트 유형 믹스(지정가 공급자·시장가 테이커·모멘텀 추종) 튜닝 자료 미축적
