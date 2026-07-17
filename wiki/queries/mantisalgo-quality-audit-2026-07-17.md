---
tags: [query, mantisalgo, quality, pine-script]
created: 2026-07-17
updated: 2026-07-17
sources: ["repo: Desktop/dev/MantisAlgo/docs/AUDIT_REPORT_2026-07-17.md"]
---
# MantisAlgo 품질 감사 + LuxAlgo급 개선 (2026-07-17)

> "게이트 전부 통과"였지만 외부 기준으로 보니 컴파일 불가 파일 2개와 상용 기능 공백이 숨어 있었다. 감사→개선 11건→재검증까지 하루에 완료.

## 🌱 쉽게

공장 자체 검사표로는 전 제품 합격이었는데, 남의 눈(LuxAlgo 기준)으로 다시 보니 시동도 안 걸리는 차 2대와 "색상도 못 바꾸는 옵션 제로" 문제가 나왔다. 검사표 자체가 관대했던 것. 검사표를 갈아엎고, 부품(생성기)을 업그레이드해서 전 제품에 자동 반영했다.

## ⚙️ 정확히

- 감사 전: A13/B10/C2, 플래그십 루브릭 100점(착시). 결함: ①콤마 체인 대입(Harmonic — 컴파일 불가) ②환각 함수 strpos/strtonumber(Liquidity Engine — 컴파일 불가) ③lookahead_on 미문서(경고만) ④input.color 0/9 SKU, 패널 위치/크기 옵션 0/9, 동적 alert() 2/25
- 개선 11건: verify_v2 차단 검사 3종 신설, 루브릭 상용 체크 5종+통과선 상향(premium/platform 70%), gen_theme(input.color×3+투명도)·플랫폼/프리미엄 대시보드(위치 5방향·크기 3단)·alert hub(동적 alert()) 업그레이드, 결함 파일 4개 직접 수리
- 감사 후: A13/B12/C0, static fail 0, 테스트 63개 회귀 0, SKU 재생성 후 전 게이트 통과
- 남은 권고: TV 실컴파일 스모크 테스트 절차화(정적 검사는 Pine 컴파일러 100% 대체 불가), backtesting.py 미설치, invite-only 라이선스 모듈 부재, 구세대 산출물 4개 재생성/폐기
- 상세 수치: 레포 `docs/AUDIT_REPORT_2026-07-17.md`

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-verification-gate]](검사 강화 상세) · [[mantisalgo-sku-catalog]](카테고리 재배치) · [[mantisalgo-pipeline]](mantis/ 패키지화) · 개념: [[repainting]]

## 📌 미해결

- TV 에디터 실컴파일 스모크 테스트를 릴리스 체크리스트에 명문화
- 판매 인프라(라이선스 체크 모듈) 설계
