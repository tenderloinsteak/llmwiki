---
tags: [ai-agents, business, query]
created: 2026-07-16
updated: 2026-07-16
sources: ["disk audit: ~/.hermes/profiles, Desktop/dev/*/AGENTS.md, .cursor/rules, wiki/"]
---
# llmwiki 연동 상태 (2026-07-16)

> Hermes·Cursor·3개 레포가 `Desktop/dev/llmwiki/wiki`에 어떻게 물려 있는지 점검 결과.

## 🌱 쉽게

배선은 **거의 다 됨**. 위키 파일·Hermes `WIKI_PATH`·스킬·Cursor 규칙은 살아 있다. 아직 약한 건 **실제로 쌓이는 루프**(query/ingest 사용)와 **SKU 그래프 구멍**, **주간 lint 자동화**.

## ⚙️ 정확히

### 초록 (연결 OK)

| 층 | 상태 |
|---|---|
| 위키 코어 | `SCHEMA.md` / `index.md` / `log.md` / raw 트리 / living pages (`kkj-taste`, `ideas-inbox`) |
| 페이지 규모 | md 215개 — entities 25 · concepts 12 · modules 164 · SKU 8 · curated orphan 0 |
| Hermes | 11 프로필 `.env` 전부 `WIKI_PATH=/Users/kkj/Desktop/dev/llmwiki/wiki` · SOUL에 wiki 라인 · librarian `wiki-ingest/query/lint` + 전 프로필 bundled `llm-wiki` |
| Cursor | Mantis/ShiftTrade/AccountingGo에 `wiki-auto-accumulation.mdc` + `AGENTS.md` wiki 절 · CEO `~/.cursor/agents/ceo.md` 경로 OK · 워크스페이스 `Desktop/dev/MantisAlgo` |
| Vault | `Desktop/dev/llmwiki` (+ `.obsidian`) · `Desktop/dev/헤르메스` → `llmwiki/hermes` 심볼릭 |

### 구조 lint

- Index→disk 깨진 링크: 없음 (템플릿 예시 `[[link]]` / `[[위키링크]]`만 오탐)
- Curated orphan: 0
- queries/comparisons: 아직 비어 있었음 (본 페이지가 첫 filed query)

### 노랑 (콘텐츠·데이터)

1. **실사용 루프 미가동** — raw 인제스트 2건(Karpathy + pine-v6 idea)뿐; comparisons 0; ideas-inbox 표 비어 있음
2. **SKU 레지스트리 드리프트** — `registry.json` `product_skus`에 SKU-01..04, 08만 있음 → SKU-05/06/07은 위키 페이지는 있으나 모듈 그래프 미매핑 (`modules-map`에도 명시)
3. **taste/ideas 문구** — CEO SOUL에만 명시; 11 specialist SOUL에는 0 (Cursor rule로는 커버)
4. **주간 wiki-lint cron** — 미설정
5. **root Hermes `.env`** — `WIKI_PATH` 없음 (프로필별은 있음; CEO 기본 세션은 SOUL 경로에 의존)
6. **pinestudy** — SCHEMA에서 별도 위키로 분리 명시; `.cursor/rules` wiki 연동은 없음 (의도적일 수 있음)

## 🔗 연결

- [[llm-wiki-pattern]] · [[hermes-org]] · [[librarian]] · [[mantisalgo-module-registry]] · [[mantisalgo-sku-catalog]] · [[kkj-taste]] · [[ideas-inbox]] · [[modules-map]]

## 📌 미해결

- SKU-05/06/07 → `product_skus` 매핑 (module-developer)
- 주간 lint 스케줄
- specialist SOUL에 taste/ideas 한 줄 전파 여부
- 첫 실전 ingest (LuxAlgo 또는 microstructure survey)
