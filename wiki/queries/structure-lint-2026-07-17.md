---
tags: [ai-agents, lint, query]
created: 2026-07-17
updated: 2026-07-17
sources: ["disk audit: Desktop/dev/*, ~/.hermes/profiles, wiki/"]
---
# 구조·연관관계 린트 (2026-07-17)

> llmwiki 전체 구조 + 형제 폴더 연동 + wiki-lint 결과.

## 🌱 쉽게

지식 위키·운영 저널·3개 제품 레포·학습용 pinestudy가 **역할별로 나뉘어 잘 물려 있다**. 링크/색인은 깨끗. 남은 건 경로 표기 잔재 몇 곳과 실사용 루프(비교·인제스트)다.

## ⚙️ 정확히

### 폴더 지도

```
Desktop/
├── pinestudy/          ← Pine 식별자 학습 위키 (별도, SCHEMA에 분리 명시) ✅ 존재
└── dev/
    ├── llmwiki/        ← 공유 지식 위키 + Hermes 운영 저널
    │   ├── wiki/       ← 지식 (SCHEMA/index/log/raw/…)
    │   └── hermes/     ← 업무 기록 (memory.md, study/, souls mirror)
    ├── 헤르메스 → llmwiki/hermes
    ├── MantisAlgo/     ← 공장 (hermes/ + AGENTS + .cursor/rules → llmwiki)
    ├── ShiftTrade/     ← 모의투자 (동일 연동)
    └── AccountingGo/   ← 회계앱 (동일 연동)

~/.hermes/profiles/×11
  .env WIKI_PATH=…/llmwiki/wiki
  librarian: wiki-ingest / wiki-query / wiki-lint (+ hermes-wiki-maintenance)
  all 11: research/llm-wiki (bundled)
```

### 구조 lint

| 항목 | 결과 |
|---|---|
| 페이지 | md 229 (entities 25 · concepts 12 · modules 173 · skus 8 · queries 4 · ideas 1 · raw 3) |
| 깨진 링크 | 0 (SCHEMA 템플릿 `[[wikilinks]]` 오탐만) |
| Index drift / orphan | 0 |
| Frontmatter (curated) | 0 누락 |
| SKU 레지스트리 매핑 | 미매핑 없음 (이전에 해소됨) |
| comparisons/ | 비어 있음 |

### 이번 세션 기계 수정

- `registry_to_wiki.py` sources · modules/skus 182p · `kkj-taste` · vault `.cursor/rules` · `CURSOR-AGENTS.md` 경로: `Mantis Algo` → `MantisAlgo` / `obsidian` → `llmwiki`
- wiki `factory-module-developer` 한줄 정의 163→173; vault soul mirror도 173으로

### 스킬 보유 확인

| 스킬 | 위치 | 상태 |
|---|---|---|
| `wiki-ingest` | `~/.hermes/profiles/librarian/skills/hermes/` | ✅ |
| `wiki-query` | 동상 | ✅ |
| `wiki-lint` | 동상 | ✅ |
| `hermes-wiki-maintenance` | 동상 (ops journal용) | ✅ |
| `llm-wiki` | 11 프로필 전부 `skills/research/` | ✅ |

## 🔗 연결

- [[llm-wiki-pattern]] · [[hermes-org]] · [[librarian]] · [[mantisalgo-module-registry]] · [[modules-map]] · [[llmwiki-integration-status-2026-07-16]]

## 📌 미해결

1. ~~3개 제품 레포 `.cursor/rules` `Mantis Algo` 표기~~ → 2026-07-17 수정 완료 (`MantisAlgo/...`)
2. ~~SOUL `(163 modules)`~~ → 2026-07-17 수정 완료 (173)
3. comparisons 0 · 실전 raw ingest 여전히 얇음
4. 주간 wiki-lint cron 미설정
5. tutor Stage 0 미시작
