---
tags: [hermes, ai-agents, org]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/llmwiki/hermes/CLAUDE.md", "~/.hermes/profiles/"]
---
# Hermes 조직 (Hermes Agent Organization)

> 곽경준의 AI 에이전트 회사. CEO(오케스트레이터) 아래 11명의 전문 직원(페르소나)이 프로젝트 3개를 분업으로 운영한다.

## 🌱 쉽게

혼자서 회사 세 개를 굴릴 수 없으니 AI 직원을 고용한 셈이다. 각 직원은 성격과 판단 기준(SOUL.md)을 갖고 자기 분야만 담당한다. CEO는 지식이 없고 오직 "이 일은 누구 담당인가"만 정한다(라우팅). 일이 끝나면 모두가 팀 일지([[hermes-org|memory.md]])에 결정을 기록해서, 다음에 누가 이어받아도 맥락이 남는다.

## ⚙️ 정확히

- 조직도: CEO 아래 [[quiz-writer]] [[learning-ux-designer]] [[microstructure-engineer]] [[critic]] [[tutor]] [[librarian]] [[factory-manager]], 공장장 아래 [[factory-idea]] [[factory-development]] [[factory-module-developer]] [[factory-ui]]
- 페르소나 정본: `~/.hermes/profiles/<이름>/SOUL.md` (11개) — 위키는 요약만
- 라우팅·수칙 정본: `Desktop/dev/llmwiki/hermes/CLAUDE.md`
- 팀 일지: `Desktop/dev/llmwiki/hermes/memory.md` — 형식 `date | persona | decision | next`
- 품질 게이트: factory→critic 승인 필수 / 새 노트는 librarian 색인 규칙 준수 / tutor의 개념은 표준화 시 repo hermes/로 전파
- 언어 규칙: 추론은 영어, 곽경준에게는 한국어(결론 우선)
- 프로젝트별 작업 표준: 각 repo의 `hermes/` 폴더 (코드와 함께 산다)

## 🔗 연결

프로젝트: [[mantisalgo]] [[shifttrade]] [[accountinggo]] · 이 위키의 원리: [[llm-wiki-pattern]]

## 📌 미해결

- 위키(지식)와 운영 저널(hermes/)의 분리·크로스링크 원칙이 실제로 유지되는지 — librarian 점검 항목
