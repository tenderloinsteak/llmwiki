# Wiki Schema — 곽경준's Knowledge Base

> **한눈에:** 이 폴더는 LLM이 대신 관리하는 지식 위키다(Karpathy LLM Wiki 패턴).
> **캡처(raw)는 자동**, **인제스트(위키 컴파일)는 협업** — 곽경준이 강조점을 넣은 뒤에야 “내 위키”가 된다.
> 옆 트리 `../hermes/`는 **도구 공통 운영 저널**(Cursor·Claude Code·Codex·Hermes 모두 같은 `memory.md`). 폴더 이름은 역사적 — Hermes 전용 아님.

## Domain

Personal knowledge base. Initial focus: quant/trading study (Pine Script, market microstructure, statistics) and business research (TradingView indicator market, learning apps). New domains may be added — extend the tag taxonomy when they appear.

Related but separate: `${PINESTUDY_PATH}/wiki/` is the per-identifier Pine v6 study wiki with its own template; do not merge it into this wiki. Cross-link instead. (`PINESTUDY_PATH` = llmwiki 조상 옆 `pinestudy`, 예: `${WIKI_PATH}/../../pinestudy`; env 우선)

## Three Layers

1. **`raw/`** — immutable sources. LLM reads, never edits.
   - **전부 `wiki/raw/`에 평탄하게 둔다** (블로그·위키·뉴스·유튜브 링크·논문·코드·Web Clipper). 하위 분류 폴더 없음.
   - `raw/assets/`만 예외 — 이미지 첨부용(옵시디언 Attachment folder로 지정 가능).
2. **Wiki pages** — `entities/`, `concepts/`, `comparisons/`, `queries/`, plus auto hubs `modules/`, `skus/`, `pines/`. LLM-owned. 곽경준 reads, LLM writes.
   - `pines/` — factory `.pine` 그래프 (scripts ↔ categories 다대다). SoT는 레포 `pinescript_factory/` + `// Tags:`; 페이지는 `pine_factory_to_wiki.py`가 생성.
3. **This file** — structure contract. Co-evolves as we learn what works.

## Page Template (all pages follow this)

```markdown
# 페이지명 (English Name)
> 한 줄 정의

## 🌱 쉽게      ← 곽경준용: 비유 중심, 코딩초보 기준
## ⚙️ 정확히    ← 에이전트용: 경로·명령어·수치·규칙, 출처 명시
## 🔗 연결      ← [[위키링크]]
## 📌 미해결    ← 다음에 알아볼 것 (리서치 방향)
```

정본(source of truth) 규칙: 페르소나는 `~/.hermes/profiles/*/SOUL.md`, 작업 표준은 각 repo `hermes/*.md`가 정본 — 위키 페이지는 요약+링크만 담는다 (드리프트 방지).

## Conventions

- File names: lowercase, hyphens, no spaces (e.g., `volatility-clustering.md`).
- Internal links: Obsidian `[[wikilinks]]`. Every page must be reachable from `index.md`.
- Every page starts with YAML frontmatter: `tags`, `created`, `updated`, `sources` (list of raw/ files it draws from).
- Language: body in Korean (곽경준 reads this), technical terms with English original on first mention — e.g., 변동성 군집(volatility clustering).
- Contradictions: never silently overwrite. Add a `> ⚠️ 상충:` callout naming both sources and dates.
- One concept = one page. Same concept in two pages → merge, leave a redirect link.

## Capture vs Ingest (Karpathy 정렬 — 도구 공통)

두 단계를 **절대 섞지 않는다.**

| 단계 | 무엇을 | 자동? |
|---|---|---|
| **Capture** | 자료를 `wiki/raw/`에 떨어뜨림 (Clipper·에이전트 fetch·붙여넣기) | **예 — 묻지 않음** |
| **Ingest** | raw를 읽고 위키 페이지로 컴파일 (요약·엔티티/컨셉 갱신·교차링크·index/log) | **아니오 — 협업이 기본** |

### Ingest 기본 절차 (모든 도구)

1. raw 파일을 읽는다 (수정 금지).
2. 곽경준에게 **핵심 요점 3–5개**를 한국어로 제시하고, **무엇에 무게를 둘지** 묻는다.
3. 강조점이 확정되면(또는 “알아서” / “배치로” 지시가 있으면) 그때 위키에 기록한다.
4. **한 번에 소스 1개**가 기본. 여러 개면 하나씩, 또는 배치 전에 “이번엔 논의 생략?”을 한 번만 묻는다.

### 여전히 자동인 것 (인제스트가 아님)

- `raw/` 캡처
- 질답 중 **비교·분석·발견된 연결** → `queries/`·`comparisons/` 파일링 (탐색 복리; 1회성 팩트체크는 제외)
- `owner-taste` / `ideas-inbox` 한 줄 기록
- 세션 결정 → `memory.md`

### 에이전트가 웹을 직접 fetch한 경우

- `raw/` 저장까지는 자동.
- 위키 컴파일(ingest)은 **하지 않고** “raw에 저장함 — ingest 할까?”로 한 줄 제안. 예외: 사용자가 이미 “알아서 ingest / 배치 ingest”라고 한 세션.

## Auto-Accumulation Rules (세부)

1. **Capture:** 외부 자료 → `wiki/raw/` (종류 가리지 않음). Web Clipper inbox = `wiki/raw/`.
2. **Ingest:** 위 협업 절차. “넣어줘/소화해줘/ingest” 또는 강조점 확정 후에만 컴파일.
3. **Query 파일링:** 비교·분석·연결은 묻지 않고 `queries/`/`comparisons/` + index/log. 잡담·1회성 사실확인은 제외.
4. **Pine 코드:** 공장 산출은 `MantisAlgo/pinescript_factory/{1_Indicators,2_Strategies}/`에 **평탄** 저장 (`// Title`/`// Kind`/`// Tags` 헤더) — **SoT는 공장**. 위키는 `pines/` 그래프만 동기화(`pine_factory_to_wiki.py`). 공장 전체를 raw에 복제하지 않음. 외부/분석 대상 1개는 그때 `raw/pine-*.pine` 캡처 후 요점 논의 → ingest.
5. **취향·아이디어:** 자동 한 줄 (`owner-taste` / `ideas-inbox`).
6. **지식 갱신 vs 세션 일지:** 위키 사실이 바뀌면 페이지+⚠️; 세션 결정만 `../memory.md` (절대경로 `${WIKI_PATH}/memory.md`). 도구별 다른 일지 금지.

## Special Files

- `index.md` — content catalog by category, one line per page. Updated on **every** ingest/filed query. Read this first when answering questions.
- `log.md` — append-only timeline. Entry prefix format: `## [YYYY-MM-DD] ingest|query|lint | title` (grep-parseable: `grep "^## \[" log.md | tail -5`).

## Workflows

Defined as Hermes skills (librarian profile): `wiki-ingest`, `wiki-query`, `wiki-lint`. The generic bundled `llm-wiki` skill also resolves here via `WIKI_PATH` in each profile's `.env`.

## Tag Taxonomy (extend as needed)

`pine-script`, `quant`, `statistics`, `microstructure`, `trading-psychology`, `market-research`, `accounting-edu`, `ai-agents`, `business`

프로젝트 소속(클리핑·페이지): `mantisalgo` · `shifttrade` · `accountinggo` · `wiki-meta`(llmwiki/에이전트 자체). raw 클립은 Web Clipper 체크박스/`projects` 리스트로 남기고, ingest 때 위키 `tags`와 `[[entity]]` 링크로 승격.
