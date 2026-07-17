# Index — Content Catalog

> One line per page: `[[link]] — one-line summary`. Updated on every ingest and filed query.
> Read this file FIRST when answering questions against the wiki.

## Entities — 프로젝트

- [[entities/mantisalgo]] — Pine 지표·전략을 파는 자동화 공장 (허브)
- [[entities/shifttrade]] — 진짜 같은 가짜 시장의 모의투자 앱 (허브)
- [[entities/accountinggo]] — 회계원리 듀오링고, Flutter MVP (허브)
- [[entities/hermes-org]] — AI 에이전트 조직: CEO + 11 페르소나, 라우팅·게이트

## Entities — 시스템

- [[entities/mantisalgo-pipeline]] — main.py 생산 라인, 결정적 주입 우선
- [[entities/mantisalgo-module-registry]] — 부품 173개 장부 (ui/logic/infra), 등재+패리티 테스트
- [[entities/mantisalgo-verification-gate]] — 실패=저장금지 2층 관문(기계+크리틱)
- [[entities/mantisalgo-sku-catalog]] — 판매 제품 SKU-01..08, 신선도 기준선
- [[entities/shifttrade-tick-engine]] — 가격 엔진, stylized facts가 합격 기준
- [[entities/shifttrade-data-pipeline]] — Render→Supabase→화면 물길 + 유저 원장
- [[entities/accountinggo-content-pipeline]] — 오프라인 생성→검증→번들, ID 불변
- [[entities/accountinggo-mastery-system]] — 최근10회×7일반감기 숙련도, <70 복습
- [[entities/accountinggo-i18n]] — 영어 원본, 한국어는 같은 ID의 번역

## Entities — 페르소나 (정본: ~/.hermes/profiles + repo hermes/)

- [[entities/personas/factory-manager]] — 공장장: 라인을 돌리고 고침, 손제작 금지
- [[entities/personas/factory-idea]] — 기획: 아이디어 JSON과 판매문구의 주인
- [[entities/personas/factory-ui]] — 비주얼: 팔레트·절제·마케팅 에셋
- [[entities/personas/factory-module-developer]] — 부품: 레지스트리와 갭맵
- [[entities/personas/factory-development]] — 파이프라인 개발: 게이트 방어자
- [[entities/personas/critic]] — 독립 감사: 3축 심사, 의심되면 기각
- [[entities/personas/quiz-writer]] — 출제: 개념을 시험, 오답은 실수 기반
- [[entities/personas/learning-ux-designer]] — 학습 UX: 듀오링고 재해석
- [[entities/personas/microstructure-engineer]] — 시장 리얼리즘: 통계로 검증
- [[entities/personas/tutor]] — 전담 교사: 지휘자 양성, 온디맨드
- [[entities/personas/librarian]] — 사서: 구조만 지킴, 이 위키의 관리자

## Concepts

- [[concepts/pine-script]] — TradingView 전용 언어, v6, 식별자 952개
- [[concepts/series-vs-array]] — 봉마다 자동 실행되는 값의 줄 (Pine의 핵심)
- [[concepts/repainting]] — 과거를 고쳐 그리는 지표 사기, 검증 1순위
- [[concepts/5-part-anatomy]] — Pine 코드 표준 골격 5부
- [[concepts/backtest-and-overfitting]] — 기출만 잘 푸는 전략 걸러내기
- [[concepts/market-microstructure]] — 가격이 만들어지는 경매장 역학
- [[concepts/stylized-facts]] — 시장의 통계 지문 4종, 시뮬레이션 합격선
- [[concepts/order-driven-simulation]] — 주문을 만들면 가격이 창발하는 방식
- [[concepts/gamified-learning-loop]] — 짧은 세션+즉각 피드백+보상, 벌 금지
- [[concepts/spaced-repetition]] — 잊을 때쯤 복습, 오답은 벌 아닌 예약
- [[concepts/double-entry-bookkeeping]] — 저울처럼 항상 수평인 복식부기
- [[concepts/llm-wiki-pattern]] — 이 위키 자체의 원리 (Karpathy)
- [[concepts/accounting-terminology-matrix]] — 회계용어 다국어 매칭 허브 (규칙·함정·샘플)
- [[concepts/accounting-terminology-registry-index]] — 용어·계정과목 레지스트리 314 entries 요약
- [[concepts/accounting-locale-registry]] — 국가별 수험·기준서 앵커 (ko/ja/zh/de/fr/es/…)

- [[queries/mantisalgo-phase1-signal-density]] — Phase 1 신호 밀도 캘리브레이션·거버너

## Living Pages (자동 축적)

- [[entities/kkj-taste]] — 곽경준 취향·피드백 원장 (특히 UI/UX) — 에이전트가 자동 기록
- [[ideas/ideas-inbox]] — 툭 던진 아이디어 인박스 — 에이전트가 자동 기록

## Modules & SKUs (auto-generated — `registry_to_wiki.py`)

- [[modules/modules-map]] — 모듈 173개 지도 (kind: ui/logic/infra별 + family별) + SKU 연결 허브
- SKU 상세: [[skus/SKU-01]] [[skus/SKU-02]] [[skus/SKU-03]] [[skus/SKU-04]] [[skus/SKU-05]] [[skus/SKU-06]] [[skus/SKU-07]] [[skus/SKU-08]] — 각 페이지에서 사용 모듈이 그래프로 연결됨

## Comparisons

- [[comparisons/karpathy-llm-wiki-vs-llmwiki]] — Karpathy gist 패턴 vs 우리 구현: 핵심 충실 / 의도적 확장 / 실천 갭 (2026-07-17)

## Queries (filed answers)

- [[queries/accounting-multilingual-terms-wave1-2026-07-17]] — 다국어 회계용어 Wave1: 레지스트리 314 + KO 전수 초안
- [[queries/llmwiki-integration-status-2026-07-16]] — Hermes·Cursor·레포 ↔ llmwiki 연동 점검 (2026-07-16)
- [[queries/mantisalgo-quality-audit-2026-07-17]] — TradingView 상용급 품질 감사: 결함 발견→개선 11건→C0 달성 (2026-07-17)
- [[queries/mantisalgo-structure-review-2026-07-17]] — Claude 대량변경 후 구조·흐름·wiki 연동 검토 (게이트 OK / tv_safety 6실패 / Cursor rule 구식)
- [[queries/accountinggo-master-polish-plan-2026-07-17]] — AccountingGo Master Polish Plan 접수·P0 게이트 실측 (2026-07-17)
- [[queries/structure-lint-2026-07-17]] — 전체 구조·형제폴더 연동·스킬 보유 확인 + lint (2026-07-17)
- [[queries/llmwiki-fragility-2026-07-17]] — LLM 위키로서 취약점·부족점·개선 우선순위 (2026-07-17)

## Sources (raw/)

- [[raw/articles/llm-wiki-karpathy]] — Karpathy LLM Wiki 원문 (2026-07-16 인제스트 → [[concepts/llm-wiki-pattern]])
- [[raw/articles/pine-v6-learning-system-idea]] — Pine v6 학습 시스템 기획서 (구 IDEA.md). 미소화 — pinestudy로 대부분 실현됨, 필요시 인제스트
- [[raw/articles/accounting-terms-wikipedia-summaries-2026-07-17]] — 다국어 회계용어 Wikipedia extract JSON
- [[raw/articles/accounting-terminology-research-notes-2026-07-17]] — 용어 리서치 방법·로케일 앵커 노트
