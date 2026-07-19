---
tags: [system, mantisalgo, pine-script]
created: 2026-07-16
updated: 2026-07-20
sources: ["repo: Desktop/dev/MantisAlgo (config/module_registry/, hermes/module-developer.md, ui_audit.py, scripts/module_lint.py)"]
---
# MantisAlgo 모듈 레지스트리 (Module Registry, 194개)

> 제품을 조립하는 부품 창고이자 장부. 어떤 부품이 있고, 어느 제품에 쓰였는지의 단일 진실.

## 🌱 쉽게

레고 부품함이다. RSI 계산기, 추세 필터, 대시보드 같은 부품 194개가 등록돼 있고, 새 제품은 이 부품들을 조합해 만든다. 부품함 장부가 정확해야 "이 조합은 이미 만든 제품이랑 겹친다"(신선도 검사)를 판단할 수 있다. 부품은 "등록 + 테스트 통과" 둘 다 되어야 완성이고, 하나만 되면 미완성이다. 부품함은 세 서랍이다: **UI 서랍**(화면에 보이는 것 — 대시보드·범례·네온·오버레이, 45개)과 **로직 서랍**(안 보이는 계산·시그널 — 구조·모멘텀·볼륨 등, 135개), 그리고 조립을 지탱하는 **인프라 서랍**(14개). 그중 13개는 `sku_ship:false`(smoke-test only)라 SKU-08 `features:"all"`에 자동으로 안 실린다.

## ⚙️ 정확히

- 정본: `config/module_registry/registry.json` — **194 live / 0 planned** (레거시 별칭, SKU 매핑)
- 카운트 (2026-07-20): kind **ui 45 / logic 135 / infra 14**; `sku_ship:false` smoke **13** · SKU 자동탑재 가능 **181**
- **1급 분류 `kind`**: `ui` · `logic` · `infra`. `module_registry.modules_by_kind()`로 조회
- **`sku_ship`**: `false`면 live이지만 SKU-08 `features:"all"`에서 제외 (네온·패널 실험 모듈)
- 계획: `config/module_registry/MASTER_PLAN.md` + `docs/plan_ui_modules_batch3.md` / `batch4.md` (2026-07-20 실행 완료)
- 조립 코드: `premium_modules.py` · `premium_assembler.py` · `architecture_catalog.py`
- **UI 감사 게이트**: `ui_audit.py` — 툴팁/그룹, declutter, 시그니처 팔레트, 패널 코너 중복 advisory. `factory_gate.py` + `scripts/module_lint.py`
- 완성 조건: 레지스트리 등재 AND `tests/test_module_registry.py` + `tests/test_registry_generator_parity.py` + `scripts/module_lint.py --kind all` (findings=0)
- 자동 위키 반영: `hermes/scripts/registry_to_wiki.py` → `wiki/modules/*.md` + `wiki/skus/*.md` + `wiki/modules/modules-map.md`

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-pipeline]] · [[mantisalgo-sku-catalog]] · [[mantisalgo-verification-gate]] · 담당: [[factory-module-developer]] [[factory-ui]](UI kind) · 신선도 판정에 사용: [[critic]]

## 📌 미해결

- smoke-only 13종(네온·카운트다운·버블·배지·고스트 등) SKU 탑재 우선순위 미정 — 판매 주력 SKU 스크린샷용으로 E-2 배지 후보
- 현재 카테고리 스큐 최신 집계는 다음 갭맵 때
