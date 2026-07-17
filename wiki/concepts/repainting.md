---
tags: [concept, pine-script, quant, quality]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/MantisAlgo/hermes/development.md", "Desktop/dev/MantisAlgo/hermes/critic.md"]
---
# 리페인팅 (Repainting)

> 지표가 과거를 몰래 고쳐 그리는 현상. 백테스트에선 천재, 실전에선 사기꾼이 되는 주범.

## 🌱 쉽게

시험이 끝난 뒤 답안지를 고쳐 쓰는 것과 같다. 실시간 봉에서는 값이 확정 전까지 계속 바뀌는데, 이때 신호를 내면 "과거 차트에선 완벽했던 신호"가 실제 매매에선 재현되지 않는다. 상습범은 `request.security()`의 lookahead(미래 데이터 훔쳐보기)와 미확정 봉 신호. 그래서 MantisAlgo에선 확정 봉에서만 신호를 내고, 모든 모듈에 리페인팅 여부를 라벨로 선언하며, 크리틱이 독립적으로 재검사한다.

## ⚙️ 정확히

- 원인 1: 실시간 봉 재실행 — 봉 확정 전 값 변동. 대응: 확정 봉 신호(`barstate.isconfirmed` 등)
- 원인 2: `request.security()` lookahead — 상위 타임프레임의 미확정/미래 값 참조. 대응: lookahead 처리 규칙 준수
- MantisAlgo 규칙: 생성 코드 리페인팅 금지(코드 표준), 모듈 메타데이터에 리페인팅 동작 선언 의무, 자가검증 항목 "realtime vs confirmed bars" 비교
- 검사 주체: [[factory-development]](자가) → [[critic]](독립 재검증, 기계 결과 불신)

## 🔗 연결

[[pine-script]] · [[series-vs-array]] · [[mantisalgo-verification-gate]] · [[mantisalgo-module-registry]] · [[backtest-and-overfitting]]

## 📌 미해결

- 리페인팅 검사 자동화 수준(현재 테스트가 어디까지 잡는지) 확인 필요
