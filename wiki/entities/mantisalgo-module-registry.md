---
tags: [system, mantisalgo, pine-script]
created: 2026-07-16
updated: 2026-07-17
sources: ["repo: Desktop/dev/MantisAlgo (config/module_registry/, hermes/module-developer.md, ui_audit.py, scripts/module_lint.py)"]
---
# MantisAlgo 모듈 레지스트리 (Module Registry, 173개)

> 제품을 조립하는 부품 창고이자 장부. 어떤 부품이 있고, 어느 제품에 쓰였는지의 단일 진실.

## 🌱 쉽게

레고 부품함이다. RSI 계산기, 추세 필터, 대시보드 같은 부품 173개가 등록돼 있고, 새 제품은 이 부품들을 조합해 만든다. 부품함 장부가 정확해야 "이 조합은 이미 만든 제품이랑 겹친다"(신선도 검사)를 판단할 수 있다. 부품은 "등록 + 테스트 통과" 둘 다 되어야 완성이고, 하나만 되면 미완성이다. 2026-07-17부터 부품함 자체가 두 서랍으로 나뉜다: **UI 서랍**(화면에 보이는 것 — 대시보드·범례·컬러링, 26개)과 **로직 서랍**(안 보이는 계산·시그널 — 구조·모멘텀·볼륨 등, 134개), 그리고 조립을 지탱하는 **인프라 서랍**(13개).

## ⚙️ 정확히

- 정본: `config/module_registry/registry.json` — 173개 (live/planned, 레거시 별칭, SKU 매핑)
- **1급 분류 `kind`** (2026-07-17 도입): `ui`(차트 표현층 — 판매 첫인상 담당) · `logic`(공장 분석/시그널 — 인디케이터·전략 공용) · `infra`(조립 기반). `module_registry.modules_by_kind()`로 조회
- 계획: `config/module_registry/MASTER_PLAN.md` (갭맵 포함, 2026-07-16 kind 분리 + 신규 10모듈 항목 기록됨)
- 조립 코드: `premium_modules.py` · `premium_assembler.py` · `architecture_catalog.py`
- **UI 감사 게이트** (2026-07-16 신설): `ui_audit.py` — 툴팁/그룹 커버리지, 기본값 declutter(배경 음영 상한), 시그니처 팔레트(bull=teal/bear=orange/neutral=gray) 규율을 기계 판정. `factory_gate.py`(SKU 조립 결과 게이트)와 `scripts/module_lint.py`(모듈 카탈로그 자체 게이트) 양쪽에서 사용
- 완성 조건: 레지스트리 등재 AND `tests/test_module_registry.py` + `tests/test_registry_generator_parity.py` + `scripts/module_lint.py --kind all` (findings=0) 통과
- 품질 기준: 단일 책임 / 명시적 인터페이스(입력 시리즈·반환 타입) / [[repainting]] 동작 메타데이터 선언(단, 2026-07-17부로 리페인트 자체는 금지 사항 아님 — [[mantisalgo-pipeline]] 참조) / [[5-part-anatomy]] 슬롯 분류
- 안티스테일: 분기별 카테고리 집계로 약한 분야를 생산 우선순위화, 미출시 planned 감사
- 자동 위키 반영: `hermes/scripts/registry_to_wiki.py` 실행 시 `wiki/modules/*.md`(모듈당 1페이지, kind 태그 포함) + `wiki/skus/*.md` + `wiki/modules/modules-map.md`(kind·family 허브)를 registry.json에서 재생성 — **수동 실행 스크립트이며 자동 트리거 없음** (git hook·cron 없음). 아래 📌 참조

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-pipeline]] · [[mantisalgo-sku-catalog]] · [[mantisalgo-verification-gate]] · 담당: [[factory-module-developer]] [[factory-ui]](UI kind) · 신선도 판정에 사용: [[critic]]

## 📌 미해결

- 현재 카테고리 스큐(어느 분야에 몰려있는지) 최신 집계 필요 — 다음 갭맵 때 기록
- ~~SKU-05/06/07 `product_skus` 미매핑~~ → **해소 (2026-07-17)**: registry.json에 SKU-01..08 전부 등재, modules-map `미매핑: 없음`
- `registry_to_wiki.py`가 수동 스크립트라 registry.json 변경 후 재실행을 잊으면 위키가 드리프트됨 — MantisAlgo `.cursor/commands/*-module-update.md` 마지막 단계에서 호출하도록 연결됨 (2026-07-17)
