---
tags: [concept, quant, microstructure, simulation]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/ShiftTrade/hermes/microstructure-engineer.md"]
---
# 주문주도 시뮬레이션 (Order-Driven Simulation)

> 가격을 직접 만들지 않고, 주문 이벤트를 만들어 가격·호가·체결이 "저절로" 나오게 하는 시장 생성 방식.

## 🌱 쉽게

인형극(가격을 손으로 움직이고 배경을 그려 넣기) 대신 개미 농장(개미들을 풀어놓으면 길이 저절로 생김)을 만드는 것. 가상의 시장 참여자들 — 급한 사람(시장가), 기다리는 사람(지정가), 추세 쫓는 사람(모멘텀) — 이 주문을 내게 하면, 그 주문들이 부딪히면서 가격·호가창·체결 테이프가 동시에, 서로 모순 없이 태어난다. ShiftTrade의 "가격 먼저 만들고 호가 꾸미기 금지" 철칙의 해법이 이것이다.

## ⚙️ 정확히

- 반대 개념: 가격 프로세스 우선 방식(랜덤워크/GBM으로 가격 생성 → 호가는 장식) — 테이프·깊이 불일치 유발
- 구성: 에이전트 유형 믹스(유동성 테이커 / 지정가 공급자 / 모멘텀 추종) 비율로 리얼리즘 튜닝
- 기대 효과: [[stylized-facts]]가 규칙으로 주입되지 않고 창발(emerge)
- ShiftTrade 적용 상태: 방향은 확정, `FinancialPriceEngine`을 진화시킬지 위에 레이어를 얹을지 미결
- 비용: 이벤트 루프 성능 — 스캘핑급 리플레이가 요구사항이므로 성능 예산 필수

## 🔗 연결

[[market-microstructure]] · [[stylized-facts]] · [[shifttrade-tick-engine]] · [[microstructure-engineer]]

## 📌 미해결

- 아키텍처 결정(진화 vs 레이어) — 결정 시 이 페이지 갱신
- ABM(agent-based model) 참고 구현 사례 리서치
