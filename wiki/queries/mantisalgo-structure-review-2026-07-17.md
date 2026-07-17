---
tags: [ai-agents, pine-script, query]
created: 2026-07-17
updated: 2026-07-17
sources: ["disk audit: Desktop/dev/MantisAlgo (main.py, mantis/, tests/, scripts/, .cursor/rules)", "factory_gate + pytest + score_factory run 2026-07-17", "wiki entities + registry_to_wiki parity"]
---
# MantisAlgo 구조·흐름 검토 (2026-07-17)

> Claude로 대량 변경 직후, 파일 수정 없이 구조·파이프라인·llmwiki 연동만 감사한 결과.

## 🌱 쉽게

공장은 **실제로 잘 돌아간다**. SKU 8개 조립 게이트 전부 통과, 완성품 22개는 A14/B8·정적실패 0. 다만 **에이전트용 나침반(Cursor rule)이 구식**이고, **테스트 6개가 깨져 있으며**, **위키는 배선은 됐는데 git에 안 올라가 있고 숫자 한 줄이 163으로 남아** 있다. “망가진 공장”이 아니라 “문서·동기화가 코드보다 뒤처진 공장”에 가깝다.

## ⚙️ 정확히

### 현재 구조 (실측)

| 층 | 상태 |
|---|---|
| 진입점 | 루트 `main.py`만. 코어는 `mantis/` (flat import + `sys.path` 부트스트랩) |
| 모듈 | registry 173 = generators/families 173, kind ui26/logic134/infra13, 14 family |
| SKU | `config/product_skus/` 01–08 전부 있음. `registry.json`의 `product_skus`에는 **01–04, 08만** (05–07 미매핑 — `SKU_BASE_FEATURES`·아이디어 JSON으로는 조립 가능) |
| 팩토리 | `.pine` **22개** (Ind 11 / Str 11), LuxAlgo식 카테고리 폴더. 구 Trend/Momentum/Breakout만의 구조는 폐기됨 |
| 게이트 | `factory_gate.py` → **ALL PASSED** (SKU-01..08 verify+UI audit) |
| 품질 | `score_factory` A14 / B8 / static fail 0 |
| 테스트 | 86 collect, **80 pass / 6 fail** (`test_all_sku_tv_safety`: `if useAlertHub` 잔존 — SKU 01,02,03,05,07,08) |
| 위키 모듈 그래프 | registry↔wiki/modules **173=173 완전 일치** (+ modules-map). `registry_to_wiki.py`는 수동 |

### 파이프라인 흐름 (의도 vs 실체)

의도된 축은 그대로다:

`idea JSON` → `enrich/assemble(결정적)` → `verify_v2` (+ ui_audit/quality) → `factory_saver` → `pinescript_factory/`

병렬로 모듈 공장: `generators/families/*` ↔ `registry.json` ↔ (수동) `registry_to_wiki.py` → `wiki/modules/`.

`pinescript_generator/`는 여전히 통합 파이프라인 위임 진입점으로 살아 있고 path 부트스트랩도 맞춰져 있다. scripts/tests/conftest도 동일 패턴.

### 초록 (건강한 것)

1. **패키지화 방향 맞음** — 루트 오염 제거, `mantis/__init__.py` + 진입점 path insert로 동작.
2. **SKU 자동 게이트·UI audit 100%** — 상용 라인의 기계 검사는 살아 있음.
3. **모듈↔위키 페이지 패리티 완벽** (173).
4. **커맨드 스킬 ↔ wiki sync 연결** — `.cursor/commands/*-module-update.md`가 `registry_to_wiki.py` 호출을 명시.
5. **지식 페이지 본체** (`entities/mantisalgo*.md`)는 2026-07-17 패키지화·kind·리페인트 정책까지 대체로 최신.

### 노랑 (드리프트·위생 — 당장 안 터지지만 에이전트를 헷갈리게 함)

1. **`.cursor/rules/mantis-algo-context.mdc` 심각 구식**
   - 파일 표를 루트 `pipeline.py` 등으로 기술 (실제는 `mantis/`)
   - Factory State: “13 `.pine` / Trend·Momentum·Breakout” → 실제 22 + 30카테고리
2. **`wiki/index.md` 한 줄**이 아직 “부품 163개” — 본문 페이지는 173.
3. **`entities/mantisalgo.md` 🌱 비유 문장**에 “163개” 잔존 (⚙️는 173).
4. **감사 리포트 수치 스냅샷** (`docs/AUDIT_REPORT_2026-07-17.md`): .pine 25·테스트 63 — 현재 22·86과 불일치 (시점 스냅샷일 수 있음).
5. **flat import 계약** — `python -c "from module_registry import …"`는 실패. 새 스크립트에 path insert 빠지면 즉시 깨짐 (wiki pipeline 페이지가 이미 경고).
6. **llmwiki git** — `wiki/` 전체가 여전히 `??` untracked. 유실 위험(이전 librarian 지적 미해소).
7. **SKU-05/06/07** `registry.json` `product_skus` 미매핑 — modules-map에도 명시. 조립은 idea/SKU_BASE로 되지만 위키 그래프·신선도 장부가 구멍.

### 빨강 (실질 회귀)

1. **`tests/test_all_sku_tv_safety.py` 6실패** — 조립 결과에 `if useAlertHub`가 들어감. `factory_gate`/`verify_v2`는 통과하므로 **게이트가 이 TV 안전 규칙을 안 막음**. `test_tradingview_compile_fixes`의 alert hub 테스트와 정책이 어긋났을 가능성.

### 권장 우선순위 (수정은 이번 세션에서 하지 않음)

1. AlertHub `if` 래핑 회귀 수정 → tv_safety 6개 녹색
2. Cursor rule을 `mantis/` + 22 pine + 30카테고리로 갱신 (에이전트 토큰 절약 정본)
3. `registry.json`에 SKU-05/06/07 `product_skus` 매핑 채우기 → wiki 재생성
4. llmwiki `wiki/` 최초 커밋 (유실 방지)
5. index/🌱 문장의 163 → 173 정리

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-pipeline]] · [[mantisalgo-module-registry]] · [[mantisalgo-verification-gate]] · [[mantisalgo-sku-catalog]] · [[queries/llmwiki-integration-status-2026-07-16]] · [[queries/mantisalgo-quality-audit-2026-07-17]]

## 📌 미해결

- ~~AlertHub 조건부 래핑~~ → **해소**: `if useAlertHub`+동적 `alert()` 허용, alertcondition 전역 유지. pytest 86 pass (2026-07-17)
- ~~Cursor rule 구식~~ → **해소**: mantis/·22pine·30카테고리로 갱신됨
- ~~SKU-05/06/07 product_skus~~ → **해소**: registry 8개 전부, modules-map `미매핑: 없음`
- ~~llmwiki wiki/ untracked~~ → 본 세션에서 최초 커밋 진행
- `registry_to_wiki`를 factory_gate 후에도 돌릴지 (선택)
