---
tags: [system, mantisalgo, pine-script]
created: 2026-07-16
updated: 2026-07-17
sources: ["repo: Desktop/dev/MantisAlgo (AGENTS.md, hermes/development.md, hermes/factory-manager.md, context_prompting.py, pipeline.py)"]
---
# MantisAlgo 파이프라인 (Production Pipeline)

> `main.py`로 시작하는 자동 생산 라인. 아이디어 JSON을 넣으면 검증된 `.pine` 제품이 나온다.

## 🌱 쉽게

주문서(아이디어 JSON)를 넣으면 컨베이어벨트가 돌아간다: 규칙 주입 → 부품 조립 → 코드 생성 → 품질검사. 중요한 건 "사람이 손으로 코드를 고쳐서 통과시키기" 금지라는 것. 라인이 불량을 내면 라인 자체를 고쳐야지, 불량품을 손봐서 내보내면 공장이 약해진다.

## ⚙️ 정확히

- 실행: `python main.py --type strategy|indicator [--review|--from-idea FILE|-n N]`
- 흐름: `main.py` → `pipeline.py`(오케스트레이션) + `context_prompting.py`(시스템 규칙→레지스트리 제외→작업 페이로드) + `idea_registry.py`(중복 차단) → `factory_saver.py`(저장)
- **패키지 구조 (2026-07-17 리팩토링)**: 핵심 모듈 19개가 루트→`mantis/` 패키지로 이동 (루트 .py는 `main.py`만 남음). 모듈 간 flat import 유지, `mantis/__init__.py`가 sys.path 부트스트랩. 진입점(main.py·scripts·tests conftest·scratch·pinescript_generator)마다 `sys.path.insert(ROOT/"mantis")` 필요 — 새 스크립트 작성 시 주의
- 템플릿: `config/template_*.pinescript` — indicator/strategy × basic/enhanced/premium/platform, 5part
- 생성 원칙: 결정적 주입(deterministic injection) 우선, LLM 다듬기는 정적 검사 실패 시에만
- 테스트: `tests/` (pine_safe, tradingview_compile_fixes, sku_tv_safety, quality_rubric 등) — 파이프라인 변경 후 pytest 필수
- 저장 경로: `output/`(초안) → 게이트 통과 시 `pinescript_factory/1_Indicators|2_Strategies/<Mantis 30 카테고리>/` (2026-07-17)
- **인디케이터 리페인트 정책 (2026-07-17, 곽경준 명시적 지시로 변경 — strategy는 미변경)**: 인디케이터는 백테스트 대상이 아니므로 `context_prompting.py`의 `_INDICATOR_CONSTRAINTS`와 `pipeline.py`의 `INDICATOR_IDEA_SYSTEM`에서 "리페인트 금지" 요구를 제거하고 "차트·과거 시그널이 보기 좋아 보이면 리페인트/인트라바 값 허용"으로 교체. **전략(strategy) 프롬프트는 건드리지 않음** — `STRATEGY_IDEA_SYSTEM`과 자가검증 체크리스트(아래)의 "리페인트 확인"은 그대로 유지, 전략은 실제 백테스트 대상이라 리페인트가 결과를 왜곡하기 때문
- 이론 계약 (2026-07-16 신설, 인디케이터 한정): `indicators` 필드에 시장 메커니즘(왜 작동하는가)·정확한 수학·실패 모드 3가지를 명시하도록 프롬프트 강제. UI 계약(모든 input에 group+tooltip, bullColor/bearColor 색 문법, 기본값 절제)과 세트

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-verification-gate]] · [[mantisalgo-module-registry]] · 담당: [[factory-development]] [[factory-manager]] · 개념: [[5-part-anatomy]] [[pine-script]]

## 📌 미해결

- 파이프라인 우회 일회성 스크립트 발생 여부 모니터링 (안티패턴 1순위)
