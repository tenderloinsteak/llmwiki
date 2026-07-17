---
tags: [concept, pine-script, mantisalgo]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/MantisAlgo/AGENTS.md", "Desktop/dev/MantisAlgo/hermes/development.md"]
---
# 5-Part Anatomy (5부 해부 구조)

> MantisAlgo의 모든 Pine 코드가 따르는 표준 골격: Inputs → Filter Engine → Custom Logic → Execution → Risk Mgmt.

## 🌱 쉽게

집을 지을 때 방 배치가 정해진 표준 설계도다. ①Inputs(설정 — 사용자가 만지는 손잡이) ②Filter Engine(장세 필터 — 지금 신호를 낼 환경인가) ③Custom Logic(핵심 계산 — 이 제품만의 두뇌) ④Execution(신호/주문 실행) ⑤Risk Mgmt(손절·익절). 모두가 같은 골격을 쓰면 코드를 처음 봐도 어디에 뭐가 있는지 알고, 모듈이 어느 방에 들어갈 부품인지 분류할 수 있다.

## ⚙️ 정확히

- 지위: `.hermesrules.txt`에서 의무 사항, 생성 코드 표준
- 모듈 분류: 레지스트리의 각 모듈은 5개 슬롯 중 하나에 배정 ([[mantisalgo-module-registry]])
- 검토 용법: 생성된 `.pine`을 5부로 나눠 읽기 — [[tutor]] Phase 6 (지휘자 훈련)의 핵심 도구
- 시그널 변수 규율(관련 규칙): AI 존 앞 `= false` 선언, 존 안 `:=` 대입, 존 뒤 리셋 금지

## 🔗 연결

[[pine-script]] · [[mantisalgo-pipeline]] · [[mantisalgo-module-registry]] · [[mantisalgo]]

## 📌 미해결

— (안정된 표준; 변경 시 repo가 정본)
