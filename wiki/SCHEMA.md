# Wiki Schema — 곽경준's Knowledge Base

> **한눈에:** 이 폴더는 LLM이 대신 관리하는 지식 위키다(Karpathy LLM Wiki 패턴).
> 나는 소스를 던지고 질문만 한다. 요약·연결·정리·모순 체크는 전부 LLM 몫.
> 옆 트리 `../hermes/`는 **도구 공통 운영 저널**(Cursor·Claude Code·Codex·Hermes 모두 같은 `memory.md`에 기록). 폴더 이름은 역사적 — Hermes 전용이 아니다. 여기는 **지식**, 저기는 **세션 결정**.

## Domain

Personal knowledge base. Initial focus: quant/trading study (Pine Script, market microstructure, statistics) and business research (TradingView indicator market, learning apps). New domains may be added — extend the tag taxonomy when they appear.

Related but separate: `Desktop/pinestudy/wiki/` is the per-identifier Pine v6 study wiki with its own template; do not merge it into this wiki. Cross-link instead.

## Three Layers

1. **`raw/`** — immutable sources (articles, papers, transcripts, assets). LLM reads, never edits. Obsidian Web Clipper drops go here.
2. **Wiki pages** — `entities/`, `concepts/`, `comparisons/`, `queries/`. LLM-owned. 곽경준 reads, LLM writes.
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

## Auto-Accumulation Rules (모든 에이전트 공통 — 묻지 말고 저장)

1. **외부 자료를 가져왔으면 무조건 raw/에 저장한다.** 웹 페이지·논문·코드 등 에이전트가 fetch한 것은 사용자에게 묻지 않고 `raw/articles|papers|code/`에 떨어뜨린 뒤 인제스트한다. 사용자가 손으로 넣는 경우는 브라우저 클리핑뿐이다.
2. **의미 있는 답변은 자동 파일링한다.** 질답 중 만들어진 비교·분석·발견된 연결은 "저장할까요?" 묻지 않고 `queries/` 또는 `comparisons/`에 저장하고 index/log를 갱신한다. 1회성 사실 확인·잡담은 저장하지 않는다.
3. **외부 Pine 코드 분석 플로:** 코드 → `raw/code/<이름>.pine(.md)` 저장 → 분석 페이지(무슨 기법·구조·핵심 아이디어) 생성 → MantisAlgo 레지스트리(`config/module_registry/registry.json`)와 대조해 없는 부품 목록 → 모듈 등록 후보를 분석 페이지 📌에 기록.
4. **취향·피드백 자동 기록.** 곽경준이 칭찬·불만·선호를 표현하면(특히 UI/UX) `entities/kkj-taste.md`에 즉시 한 줄 추가한다. 묻지 않는다.
5. **아이디어 자동 기록.** 곽경준이 아이디어를 툭 던지면(다듬어지지 않아도) `ideas/ideas-inbox.md` 표에 추가하거나 개별 페이지로 만든다. MantisAlgo 제품감이면 factory-idea 스펙으로 승격 제안.
6. **작업 후 지식 반영.** 어떤 도구(Hermes/Claude Code/Codex/Cursor)로 작업했든, 새로 알게 된 사실이 기존 페이지와 다르면 페이지를 갱신하고(상충은 ⚠️), 세션의 결정은 **공유** 운영 저널(`../hermes/memory.md`, 절대경로 `~/Desktop/dev/llmwiki/hermes/memory.md`)에 적는다. 도구마다 다른 일지를 쓰지 않는다.

## Special Files

- `index.md` — content catalog by category, one line per page. Updated on **every** ingest/filed query. Read this first when answering questions.
- `log.md` — append-only timeline. Entry prefix format: `## [YYYY-MM-DD] ingest|query|lint | title` (grep-parseable: `grep "^## \[" log.md | tail -5`).

## Workflows

Defined as Hermes skills (librarian profile): `wiki-ingest`, `wiki-query`, `wiki-lint`. The generic bundled `llm-wiki` skill also resolves here via `WIKI_PATH` in each profile's `.env`.

## Tag Taxonomy (extend as needed)

`pine-script`, `quant`, `statistics`, `microstructure`, `trading-psychology`, `market-research`, `accounting-edu`, `ai-agents`, `business`
