---
tags: [ai-agents, query, llm-wiki]
created: 2026-07-17
updated: 2026-07-17
sources: ["disk audit 2026-07-17", "comparisons/karpathy-llm-wiki-vs-llmwiki.md"]
---
# LLM Wiki 취약점·개선점 (2026-07-17)

> 배선은 됐다. 불안한 건 **연료(raw)·강제력·합성 깊이** 쪽이다.

## 🌱 쉽게

공장 건물은 세워졌는데, 선반은 레지스트리 부품 미러로 가득하고, 밖에서 가져온 책(raw)은 거의 없다. 규칙은 “알아서 지켜라”(프롬프트)라서 도구·세션마다 빠질 수 있다. 모순 표시·아이디어 인박스는 거의 안 쓰였다.

## ⚙️ 정확히

### P0 — 구조적 취약

| # | 문제 | 왜 위험한가 | 완화 |
|---|---|---|---|
| 1 | **raw 극빈** (~4파일) vs md ~236 | Karpathy 패턴의 핵심은 “소스 컴파일 축적”. 지금 페이지 대다수는 레포/레지스트리 **미러** → 물어보면 답은 나오지만 *연구 위키처럼 깊이 합성*되진 않음 | 주 1회 이상 외부 소스 ingest (논문·LuxAlgo·microstructure) |
| 2 | **규율 = 프롬프트만** (hooks/cron 없음) | session-start·memory append·ingest를 기계가 강제하지 않음 → 도구/에이전트가 조용히 스킵 가능 | Cursor hook 또는 weekly `wiki-lint` cron; 최소한 lint를 습관화 |
| 3 | **자동 축적 ≠ 검증** | 잘못된 요약을 묻지 않고 파일링하면 **틀린 지식이 복리** | 중요 도메인만 ingest 후 2줄 사람 확인; lint의 stale/contradiction 패스 강화 |
| 4 | **이중 시계** `wiki/log.md` ↔ `hermes/memory.md` | 지식 타임라인 vs 세션 결정 — 혼동·한쪽만 갱신 | 역할 유지하되 세션 시작에 둘 다 읽기(이미 명시). “결정만 memory / 지식 이벤트만 log” 반복 |

### P1 — 콘텐츠·신호 품질

| # | 문제 | 상태 | 완화 |
|---|---|---|---|
| 5 | **모듈 미러가 그래프를 잠식** (modules 174 / curated ~39) | Obsidian graph·탐색이 “지식”보다 “부품 목록”처럼 보임 | modules를 별 vault 폴더/필터로; 또는 lint 시 curated-only 뷰 |
| 6 | **⚠️ 상충 거의 미사용** | 감지·기록이 안 돌고 있거나 충돌이 없는 척 | lint content pass에서 주장 대 주장 샘플 강제 |
| 7 | **ideas-inbox 표 비어 있음** | living page 규칙이 실전 미검증 | 다음 아이디어 발언부터 한 줄; 월 1회 비었으면 lint 경고 |
| 8 | **overview / evolving thesis 없음** | 연구형 합성의 앵커 부재 | 도메인별 `synthesis-*.md` 1장부터 |
| 9 | **comparisons 1장뿐** | 탐색이 채팅으로 증발하기 쉬움 | 비교 질문마다 파일링(규칙은 있음, 습관 필요) |

### P2 — 운영·규모

| # | 문제 | 완화 |
|---|---|---|
| 10 | SoT 삼중 복사 (SOUL ↔ vault souls ↔ wiki personas) | wiki는 요약만; sync 스크립트 주기 실행 |
| 11 | 주간 lint cron 미설정 | librarian cron 1줄 |
| 12 | qmd/검색 미도입 | ~100 curated 소스 넘을 때 |
| 13 | 이미지 로컬·Dataview·Marp 미도입 | 필요할 때 (선택) |
| 14 | pinestudy 분리 | 의도적 — 크로스링크만 유지, 병합 금지 |

### 상대적으로 괜찮은 점

- 3층 + ingest/query/lint 스킬 + 교차도구 경로 통일
- index/orphan 구조 lint 통과 이력
- git에 wiki 추적됨 (과거 “전부 untracked” 위험은 완화)
- 공유 `memory.md` 도구 공통 명시 완료 (2026-07-17)

## 🔗 연결

- [[karpathy-llm-wiki-vs-llmwiki]] · [[llm-wiki-pattern]] · [[structure-lint-2026-07-17]] · [[librarian]]

## 📌 미해결 (추천 순서)

1. raw 연료 채우기 (가장 ROI 큼)
2. weekly wiki-lint 자동화
3. curated vs modules 탐색 UX
4. synthesis 페이지 1장
5. ingest 중요건 human glance 정책 SCHEMA에 한 줄
