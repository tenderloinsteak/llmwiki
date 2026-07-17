---
tags: [concept, quant, statistics]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/MantisAlgo/hermes/development.md", "Desktop/pinestudy/concepts/statistics.md"]
---
# 백테스트와 과적합 (Backtest & Overfitting)

> 과거 데이터로 전략을 시험하는 것(백테스트)과, 그 시험에만 최적화된 가짜 우등생(과적합)의 함정.

## 🌱 쉽게

기출문제만 달달 외운 학생은 기출에선 만점, 새 시험에선 낙제한다. 전략도 같다 — 파라미터를 과거 차트에 딱 맞게 조이면 백테스트 수익률은 화려하지만 실전에선 무너진다. 그래서 "검증 안 된 금융 숫자는 일단 의심"이 헤르메스 전체의 기질이다. 방어법: 시험 안 본 데이터로 재시험(아웃오브샘플), 파라미터를 조금 바꿔도 성적이 유지되는지(민감도), 수수료·슬리피지 포함, 충분한 표본 수.

## ⚙️ 정확히

- 필수 검증 4종 (MantisAlgo 전략 자가검증): 수수료·슬리피지 반영 / 표본 수 / 파라미터 민감도 / 아웃오브샘플(out-of-sample)
- 읽는 지표: 승률, Profit Factor, MDD(최대 낙폭) — [[tutor]] Phase 4
- 관련 함정: [[repainting]](백테스트 성적을 실전과 다르게 만드는 또 다른 주범), 짧은 역사·저유동성 구간 미검증
- 검사 주체: [[factory-development]](자가) → [[critic]](독립)
- 통계 배경: 평균·분산·상관·가설검정 직관 — `Desktop/pinestudy/concepts/statistics.md`

## 🔗 연결

[[mantisalgo-verification-gate]] · [[repainting]] · [[stylized-facts]](시뮬레이션 쪽의 검증 사고방식) · [[critic]] · [[tutor]]

## 📌 미해결

- 표본 수 최소 기준·민감도 허용 범위의 수치 기준 미정 — 사례 쌓이면 표준화
