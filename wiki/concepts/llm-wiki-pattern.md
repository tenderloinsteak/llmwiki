---
tags: [concept, ai-agents, wiki]
created: 2026-07-16
updated: 2026-07-17
sources: ["raw/llm-wiki-karpathy.md"]
---
# LLM 위키 패턴 (Karpathy's LLM Wiki Pattern)

> 이 위키 자체가 작동하는 원리. LLM이 자료를 읽을 때마다 지식을 위키로 "컴파일"해 축적하는 방식 — 매번 다시 찾는 RAG의 반대.

## 🌱 쉽게

RAG(업로드한 파일에서 그때그때 검색)는 매번 처음부터 다시 찾는 사서다. LLM 위키는 다르다: 자료가 들어올 때마다 사서가 요약하고, 관련 페이지에 반영하고, 모순을 표시해서 서가 자체를 점점 좋게 만든다. 지식이 쌓인다(compound). 역할 분담이 핵심 — 사람은 자료를 고르고 질문하고, LLM이 요약·연결·색인·장부 정리라는 귀찮은 일을 전부 한다. "옵시디언은 IDE, LLM은 프로그래머, 위키는 코드베이스." 사람이 위키를 포기하는 이유는 유지보수 부담인데, LLM은 지루해하지 않으므로 유지비가 0에 가깝다. 사상적 뿌리는 Vannevar Bush의 Memex(1945).

## ⚙️ 정확히

- 3층 구조: raw/(불변 원본) → 위키 페이지(LLM 소유) → 스키마(SCHEMA.md — 규율 문서, 함께 진화)
- 단계 분리: **Capture**(raw 자동) ≠ **Ingest**(요점 논의 후 컴파일 — Karpathy 협업)
- 3대 작업: **Ingest**(소스 1건이 페이지 10~15개를 갱신 가능) / **Query**(index 먼저 → 페이지 → 인용 답변, 좋은 답은 다시 파일링) / **Lint**(모순·낡음·고아·누락 링크·데이터 갭 점검)
- 특수 파일: index.md(내용 색인, 매 인제스트 갱신) / log.md(연대기, `## [날짜] 작업 | 제목` 접두사로 grep 가능)
- 규모: 색인 파일만으로 ~100소스·수백 페이지까지 동작, 그 이상은 검색 도구(qmd 등) 고려
- 우리 구현: `Desktop/dev/llmwiki/wiki/` + librarian 스킬 3종(wiki-ingest/query/lint) + 전 프로필 `.env`의 `WIKI_PATH` — 도구를 바꿔도(Claude Code, Cursor, Hermes) 같은 파일을 읽으므로 컨텍스트 연속성 유지
- 팁: Obsidian Web Clipper로 소스 수집, 그래프 뷰로 구조 확인, git으로 버전 관리

## 🔗 연결

[[hermes-org]](운영 주체) · 담당: [[librarian]] · 원문: `raw/llm-wiki-karpathy.md`

## 📌 미해결

- 위키가 커지면 검색 도구(qmd) 도입 검토 (~100소스 넘어갈 때)
- Dataview 플러그인으로 frontmatter 대시보드 만들지 검토
