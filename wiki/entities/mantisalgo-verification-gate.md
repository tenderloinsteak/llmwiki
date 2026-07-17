---
tags: [system, mantisalgo, quality]
created: 2026-07-16
updated: 2026-07-17
sources: ["repo: Desktop/dev/MantisAlgo (hermes/development.md, hermes/critic.md, tests/, mantis/ui_audit.py, mantis/verify_v2.py, mantis/quality_rubric.py, scripts/module_lint.py)", "repo: Desktop/dev/MantisAlgo/docs/AUDIT_REPORT_2026-07-17.md"]
---
# MantisAlgo 검증 게이트 (Verification Gate)

> "검사 불합격 = 저장 금지, 예외 없음." 공장의 품질을 지키는 마지막 관문. 기계 검사(코드) 위에 사람격 판단([[critic]])이 한 층 더 있다.

## 🌱 쉽게

공항 보안검색대와 같다. 아무리 급해도, 아무리 아까워도 검색대를 통과 못 하면 탑승 불가다. "이번만 손으로 고쳐서 통과시키자"가 누적되면 검색대가 장식이 되고 공장 전체가 무너진다. 그래서 이 규칙만은 협상 불가(non-negotiable #4)다. 게이트는 2층 구조: 1층은 자동 검사(컴파일·안전성·품질 루브릭), 2층은 크리틱의 독립 감사(신선도·시장성·기술 무결성).

## ⚙️ 정확히

- 1층 기계 검사: `mantis/pine_safe.py`, `mantis/quality_rubric.py`, `tests/`(tradingview_compile_fixes, sku_tv_safety, quality_rubric_platform, advisor_quality), `--review` 플래그
- **UI 감사 레이어** (2026-07-16 신설, 인디케이터는 top priority): `mantis/ui_audit.py` — 모든 SKU 조립 결과(`factory_gate.py`)와 모듈 카탈로그 자체(`scripts/module_lint.py`)에서 툴팁/그룹 커버리지 90%+, 기본값 declutter(배경 음영 3개 이하), 시그니처 팔레트 규율을 기계 판정. `quality_rubric.py`의 인디케이터 점수에도 25점 반영
- **정적 검사 강화 3종 (2026-07-17, TradingView 상용급 감사 결과)**: `mantis/verify_v2.py`에 ①콤마 체인 대입 차단(`a = x, b = y` — Pine v6 문법 위반, 괄호 깊이 추적으로 다중행 호출 오탐 방지) ②환각 bare 함수 차단(`strpos()`류 — 빌트인·사용자 정의 함수 화이트리스트 대조) ③`lookahead_on` 사용 시 `// Repaint policy:` 헤더 없으면 차단. 배경: 기존 게이트가 컴파일 불가 파일 2개를 통과시키고 있었음
- **상용 폴리시 루브릭 (2026-07-17)**: `quality_rubric.py`에 Mantis 표준 체크 5종 추가 — input.color 색상 커스터마이징(5점)·패널 위치 옵션(3)·글자 크기 옵션(3)·동적 alert()/그라디언트(3)·리페인트 정책 준수(5). tier 통과선 상향: premium 65→70%, platform 60→70%. 교훈: 관대한 루브릭은 플래그십 100점 착시를 만든다
- **TV 컴파일 오류 구조 방지 2종 (2026-07-17, 곽경준 실컴파일 피드백)**: ①CE10272 일반화 검사 — 전역 식별자를 선언 전에 사용하면 차단 (SKU-02·08의 chochPlusUp·impulseUp·liqSweepHigh 잠복 버그 적발). 근본 원인은 레지스트리 depends_on 누락으로 인한 모듈 순서 — *_alert 계열 7개에 생산자 의존성 추가. ②CW10002 — and/or/삼항 뒤 ta.* 호출 차단 + 조립 단계에서 `pine_safe.hoist_conditional_ta_calls`가 자동 호이스팅 (아이디어 JSON에 뭘 쓰든 공장이 교정)
- **차트 과밀 방지 (2026-07-17, 스크린샷 피드백)**: 게이트 없는 plotshape/plotchar 43개 발견 → 전부 티어 게이트 적용, SH/SL 스윙 라벨·X마커류 17개 모듈 Tier3(Full 전용) 강등, ui_audit에 ungated_marker_count 차단 검사 신설. Standard 프로필 기본 마커 시리즈 8개 수준으로 절제
- 리페인트 정책과의 관계: 인디케이터 리페인트는 허용([[mantisalgo-pipeline]] 2026-07-17 정책)이지만 **문서화가 조건** — `lookahead_on`을 쓰려면 헤더에 Repaint policy를 명시해야 게이트 통과. 금지가 아니라 투명성 강제
- 규칙: 게이트 실패 시 `output/` 초안이 `pinescript_factory/`로 승격되지 않음. 수동 구제 금지
- 2층 크리틱 감사: 3축(신선도·시장성·기술 무결성), 기계 통과는 승인 근거가 아님 — [[critic]] 참조
- 자가검증(개발이 크리틱 전에): 리페인트 확인, 극단 장세, 수수료·슬리피지, 표본 수, 파라미터 민감도, 아웃오브샘플
- 기각 시: 기각 사례집(`hermes/development.md` 표)에 원인+예방규칙 기록 — 같은 이유로 두 번 기각되지 않기

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-pipeline]] · 담당: [[factory-development]](방어) [[critic]](2층) · 개념: [[repainting]] [[backtest-and-overfitting]]

## 📌 미해결

- 기각 사례집 아직 비어 있음 — 첫 기각부터 축적 시작
