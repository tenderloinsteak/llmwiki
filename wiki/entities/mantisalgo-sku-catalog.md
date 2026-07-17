---
tags: [system, mantisalgo, business]
created: 2026-07-16
updated: 2026-07-17
sources: ["repo: Desktop/dev/MantisAlgo (config/product_skus/, config/ideas/, hermes/idea.md)"]
---
# MantisAlgo 제품 카탈로그 (SKU Catalog, SKU-01..08)

> 완성되어 판매 가능한 제품 8개의 목록. 새 아이디어의 "이미 있는 것과 겹치나?" 판정 기준이기도 하다.

## 🌱 쉽게

가게 진열대다. 지금 8개 상품이 올라가 있고, 새 상품을 만들려면 "진열대에 이미 비슷한 게 있지 않나"부터 확인해야 한다. 기존 상품의 변형만으로는 신상품이 아니다 — 반드시 외부 소스(시장 불만, 커뮤니티 요구, 새로 배운 개념)와 결합해야 한다. 각 상품에는 판매문구가 붙는데, 3가지 차별점이 그대로 들어가고 한계도 숨기지 않는다(환불과 평판이 더 비싸다).

## ⚙️ 정확히

- 정본: `config/product_skus/SKU-01.json` ~ `SKU-08.json` — 모듈 조합 매핑 포함
- **판매 카테고리 (2026-07-17, LuxAlgo식 30종 도입)**: PAC Lite/Pro·Full Platform→Price_Action, Signals Overlay→Signals, Session Engine→Time_Based, Order Flow→Volume, Trade Engine→Money_Management, Quant Forecast→Forecasting. 부가 분류는 아이디어 JSON `category_tags`(예: PAC Lite = +Support_Resistance, FVG, Liquidity) → `.pine` 헤더 `// Tags:`
- 품질 스냅샷 (2026-07-17 감사 후): 완성품 22개 A14/B8/C0 (구세대 3개 폐기: MA_Cross·Generated_Pine_Strategy·Donchian_Squeeze), static fail 0, SKU 8종 UI 커버리지 group/tooltip 100%. 전 SKU에 input.color 커스터마이징·패널 위치/크기 옵션·동적 alert() 반영
- 신규 등록 조건: [[mantisalgo-verification-gate]] 통과 + [[critic]] 승인 + 판매문구 확정
- 판매문구 구조: 한 줄 훅 → 무엇을 보여주나 → 3단계 사용법 → 설정 → 솔직한 한계
- 아이디어 스펙 필수 항목: 타깃 유저·상황 / 벤치마크 스크립트 1~2개(이름 명시) / 차별점 3개(구체) / 한 줄 셀링포인트 / 필요 모듈(기존/신규)
- 분기 감사: 중복·노후·저품질 SKU 제거 제안 ([[critic]] 담당)

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-module-registry]] · 담당: [[factory-idea]](등록·문구) [[critic]](감사)

## 📌 미해결

- SKU 8개 각각의 벤치마크·차별점 요약을 위키에 실을지 — 판매 전략 다룰 때 결정
- 가격 정책 미확정 (memory.md 2026-07-15)
