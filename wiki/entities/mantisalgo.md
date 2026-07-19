---
tags: [project, mantisalgo, pine-script]
created: 2026-07-16
updated: 2026-07-18
sources: ["repo: Desktop/dev/MantisAlgo (AGENTS.md, hermes/, config/)", "repo: Desktop/dev/MantisAlgo/docs/AUDIT_REPORT_2026-07-17.md"]
---
# MantisAlgo (맨티스알고)

> TradingView용 Pine Script 지표·전략을 만들어 파는 "소프트웨어 공장". 사람이 한 땀씩 코딩하는 게 아니라 파이썬 파이프라인이 제품을 생산한다.

## 🌱 쉽게

자동차 공장을 떠올리면 된다. 기획팀이 "이런 차를 만들자"고 설계도([[factory-idea|아이디어 JSON]])를 내면, 부품창고([[mantisalgo-module-registry|모듈 레지스트리 194개]])에서 부품을 꺼내 조립 라인([[mantisalgo-pipeline|파이프라인]])이 차를 만들고, 품질검사([[mantisalgo-verification-gate|검증 게이트]])를 통과해야만 출고된다. 마지막으로 외부 감사관([[critic]])이 승인해야 판매 목록([[mantisalgo-sku-catalog|SKU 카탈로그]])에 오른다. 파는 물건은 트레이딩 차트 위에 그려지는 지표(indicator)와 자동매매 규칙(strategy)이다.

## ⚙️ 정확히

- 위치: `Desktop/dev/MantisAlgo` — 진입 문서는 `AGENTS.md` (전체 재스캔 금지)
- 실행: `python main.py --type strategy|indicator [--review|--from-idea FILE|-n N]`
- Phase 1 (2026-07-17): `signal_mirror`/`signal_calibrator`/`sig_governor` — 신호 밀도 밴드 게이트
- 핵심 코드 (2026-07-17 패키지화): `main.py`(루트 유일 진입점) → `mantis/` 패키지 (`pipeline.py` + `context_prompting.py` + `idea_registry.py` 등 19개 모듈, flat import + `__init__.py` sys.path 부트스트랩)
- 산출: `output/`(초안) → 검증 통과 시 `pinescript_factory/1_Indicators|2_Strategies/` **평탄 저장**. 분류는 `// Tags:` 다대다 (아이디어 JSON `category`+`category_tags`). 헤더 통일: Title / Kind / Tags. 위키 그래프: [[pines/pines-map]] (`hermes/scripts/pine_factory_to_wiki.py`)
- 자산 현황: 모듈 194개(`config/module_registry/registry.json`, smoke-only 13·SKU ship 181), 제품 SKU-01..09(`config/product_skus/`), 완성 .pine은 `pinescript_factory/`
- 5대 비양보 규칙: ①아이디어 유니크 ②indicator≠strategy ③결정적 주입 우선, LLM은 실패 시만 ④게이트 실패=저장 금지 ⑤시그널 변수 규율
- Pine 규칙 정본: `docs/pinescript_v6_master_rules.md` (.pine 작업 시에만 읽기; 2026-07-17 docs/로 이동)
- 작업 표준 정본: `hermes/` 폴더 (factory-manager, idea, ui, module-developer, development, critic)

## 🔗 연결

[[mantisalgo-pipeline]] · [[mantisalgo-module-registry]] · [[mantisalgo-verification-gate]] · [[mantisalgo-sku-catalog]] · [[pines/pines-map]] · 담당: [[factory-manager]] [[factory-idea]] [[factory-ui]] [[factory-module-developer]] [[factory-development]] [[critic]] · 개념: [[pine-script]] [[5-part-anatomy]] [[repainting]]

## 📌 미해결

- UI 시그니처 팔레트 미확정 (memory.md 2026-07-15)
- TradingView 시장 리서치(경쟁 스크립트 gap 분석) 소스 미축적 — 리서치 대상
