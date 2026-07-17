---
tags: [ai-agents, comparison, llm-wiki]
created: 2026-07-17
updated: 2026-07-17
sources: ["raw/llm-wiki-karpathy.md", "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"]
---
# Karpathy LLM Wiki vs llmwiki 구현

> gist 패턴을 **아키텍처·3대 연산까지는 충실히 구현**했고, 팁·출력형식·인제스트 스타일은 의도적으로 다르게 / 아직 안 쓴 부분이 있다. gist 본문도 “추상 패턴, 구현은 도메인에 맞게”라고 명시.

## 🌱 쉽게

맞는 위키다 — RAG처럼 매번 다시 찾는 게 아니라, raw를 읽고 위키에 **컴파일해서 쌓는** 그 패턴이다. 다만 Karpathy가 “선택”이라고 한 것들(이미지 로컬 저장, Marp, qmd, Dataview)은 아직 거의 안 켰고, 우리는 Hermes 저널 분리·한국어 템플릿·자동 축적처럼 **우리 도메인용 확장**을 얹었다. 원문 raw는 gist와 동일(공백 차이만).

## ⚙️ 정확히

### ✅ 충실히 반영된 핵심 (필수 패턴)

| Karpathy | 우리 |
|---|---|
| raw 불변 / wiki LLM 소유 / schema 규율 | `raw/` · `entities|concepts|…` · `SCHEMA.md` + vault `CLAUDE.md`/`AGENTS.md` |
| Ingest / Query / Lint | librarian `wiki-ingest` · `wiki-query` · `wiki-lint` (+ `llm-wiki` ×11) |
| index.md 카탈로그, query 시 먼저 읽기 | `wiki/index.md` |
| log.md append-only, `## [날짜] …` grep | `wiki/log.md` |
| 좋은 답은 위키에 파일링 | `queries/` · `comparisons/` + SCHEMA auto-file |
| 모순은 덮어쓰지 않고 표시 | `> ⚠️ 상충:` |
| Obsidian = IDE, LLM = 프로그래머 | `.obsidian` vault + 에이전트 편집 |
| git으로 버전 | `llmwiki` git repo |
| Memex 정신 (연결이 문서만큼 중요) | `[[wikilinks]]` + graph 전제 |

### 🔀 의도적 차이 (패턴 위반 아님 — 도메인 확장)

| 항목 | Karpathy | 우리 |
|---|---|---|
| 스키마 위치 | CLAUDE.md / AGENTS.md 예시 | `wiki/SCHEMA.md`가 계약 + 루트 AGENTS/CLAUDE가 교차도구로 강제 |
| 인제스트 톤 | “읽고 **당신과 논의**한 뒤” 선호 | **2026-07-17 정렬:** Capture(raw)만 자동 · Ingest는 요점 논의 후 (알아서/배치 예외) |
| 페이지 포맷 | 미지정 | 🌱/⚙️/🔗/📌 + 한국어 본문 |
| 지식 vs 업무 | 한 위키에 섞일 수 있음 | `wiki/`(지식) ↔ `hermes/`(**도구 공통** 세션 일지) **역할 분리** — Hermes 전용 아님 |
| 자동 생성 층 | 없음 | `modules/`·`skus/` = `registry_to_wiki.py` (공장 레지스트리 미러) |
| living pages | 없음 | `kkj-taste` · `ideas-inbox` |
| 학습 위키 | 단일 위키 가정 가능 | `Desktop/pinestudy/` **별도** (SCHEMA에 분리 명시) |
| 멀티에이전트 | 단일 에이전트 전제 | Hermes 11 페르소나 + Cursor rules ×3 repos |

### ⚠️ 약하거나 아직 안 탄 부분 (gist 대비 실천 갭)

1. **raw 축적 얇음** — 패턴의 연료인데 articles 2건 수준. 페이지 229개는 상당 부분이 레포/레지스트리 미러·허브이지 “외부 소스 컴파일”이 아님.
2. **overview / evolving synthesis 페이지** — gist가 wiki 예로 든 “overview, synthesis” 전용 허브는 없음 (프로젝트 허브·쿼리 페이지가 부분 대체).
3. **비교(`comparisons/`) 비어 있음** — 디렉터리만 있고 파일 0.
4. **선택 팁 미도입** — 이미지 로컬 다운로드 핫키, Marp 슬라이드, Dataview 대시보드, qmd 검색 (📌에만 적혀 있음).
5. **Query 산출물 형식** — 스킬에 Marp/matplotlib/canvas 언급은 있으나 실사용은 markdown 파일링 위주.
6. **인제스트 시 human-in-the-loop 논의** — Karpathy 선호와 반대 방향(자동). 품질은 높일 수 있으나 “강조점 가이드”는 약함.

### gist Note가 말하는 기준

> “Everything mentioned above is optional and modular… The document's only job is to communicate the pattern.”

→ **패턴 인스턴스로서는 맞다.** “gist의 모든 팁까지 켠 레퍼런스 구현”은 아니다.

## 🔗 연결

- [[llm-wiki-pattern]] · [[librarian]] · [[hermes-org]] · 원문 `raw/llm-wiki-karpathy.md`
- [[structure-lint-2026-07-17]]

## 📌 미해결

- raw 실전 ingest 루프를 키울지 (LuxAlgo / microstructure survey 등)
- overview/synthesis 페이지를 둘지
- qmd / Dataview / 이미지 로컬 저장을 켤 시점
- 인제스트 때 “자동 vs 한 줄 논의 후” 기본값을 SCHEMA에 명시할지
