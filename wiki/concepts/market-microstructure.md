---
tags: [concept, quant, microstructure]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/ShiftTrade/hermes/microstructure-engineer.md"]
---
# 시장 미시구조 (Market Microstructure)

> 가격이 "어떻게" 만들어지는지를 다루는 분야 — 주문, 호가창, 체결의 미세한 역학.

## 🌱 쉽게

경제 뉴스가 "왜 올랐나"를 다룬다면, 미시구조는 "오르는 순간에 정확히 무슨 일이 있었나"를 본다. 시장은 경매장이다: 사려는 사람들이 가격표를 들고 줄 서 있고(호가창의 매수 호가), 팔려는 사람들도 줄 서 있다(매도 호가). 누군가 "지금 당장 살게요"(시장가 주문) 하면 줄 맨 앞의 매도 가격표와 체결되고, 그 순간이 테이프(체결 내역)에 찍히며 가격이 움직인다. ShiftTrade가 진짜 같으려면 이 경매장 역학을 재현해야 한다.

## ⚙️ 정확히

- 핵심 요소: 지정가 주문(호가 공급) vs 시장가 주문(유동성 소비), 스프레드, 호가 깊이(depth), 체결강도(매수 체결량 vs 매도 체결량), 테이프
- 경험 법칙: 깊이는 최우선호가 근처에 집중 / 스프레드는 변동성과 함께 벌어지고 좁아짐 / 대량 체결 후 깊이 회복
- 일관성 원칙: 호가창·테이프·차트는 같은 사건의 세 단면 — 하나라도 모순되면 미완성
- 적용: [[shifttrade-tick-engine]]의 설계 기준, [[order-driven-simulation]]의 이론 배경

## 🔗 연결

[[stylized-facts]] · [[order-driven-simulation]] · [[shifttrade]] · 담당: [[microstructure-engineer]] · 학습: [[tutor]] C트랙 연계

## 📌 미해결

- 입문 교과서/서베이 논문 선정해 raw/로 인제스트 — 리서치 1순위
