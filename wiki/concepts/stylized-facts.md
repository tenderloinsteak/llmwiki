---
tags: [concept, quant, statistics, microstructure]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/ShiftTrade/hermes/microstructure-engineer.md"]
---
# Stylized Facts (스타일라이즈드 팩트, 시장의 통계적 지문)

> 어느 시장 데이터에서나 반복적으로 관찰되는 통계 패턴. "가짜 시장이 진짜 같은가"의 합격 기준.

## 🌱 쉽게

사람 손글씨엔 지문 같은 버릇이 있어서, 위조 서명은 기계 분석에 걸린다. 시장 가격에도 그런 지문이 있다: ①큰 폭락·폭등이 정규분포 예상보다 훨씬 자주 온다(두꺼운 꼬리) ②변동성은 몰려다닌다(폭풍우는 며칠씩 이어짐) ③어제 올랐다고 오늘 오르진 않지만, "어제 크게 움직였으면 오늘도 크게 움직인다"는 오래 지속 ④거래량과 변동성은 같이 커진다. 단순 랜덤워크는 이 지문이 없어서 가짜 티가 난다 — ShiftTrade 엔진은 이 4가지를 통계 테스트로 통과해야 한다.

## ⚙️ 정확히

- ShiftTrade 합격 기준 4종: fat-tailed returns(비정규) / volatility clustering / 수익률 자기상관 없음 + 절대수익률 장기기억 / 거래량–변동성 양의 상관
- 판정 방식: 시각 확인이 아니라 **테스트 코드** — 생성 데이터에 대해 통계 검정 실행
- 함의: 순수 랜덤워크+노이즈로는 불합격 → GBM+점프 또는 [[order-driven-simulation]] 필요
- 학습 연결: [[tutor]] C트랙(통계)의 자연스러운 실습장 — 자기상관·분포 검정을 실제 틱 데이터로

## 🔗 연결

[[shifttrade-tick-engine]] · [[market-microstructure]] · [[order-driven-simulation]] · [[backtest-and-overfitting]](같은 "숫자로 검증" 정신) · [[microstructure-engineer]]

## 📌 미해결

- Cont(2001) 등 고전 서베이 원문 인제스트 — 기준 목록을 문헌 기반으로 보강
