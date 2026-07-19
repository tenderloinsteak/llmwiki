---
tags: [ai-agents, lint, query, llm-wiki]
created: 2026-07-18
updated: 2026-07-18
sources: ["disk audit: Desktop/dev/*, wiki/"]
---
# 지식 위키 및 형제 레포 전체 구조 감사 (2026-07-18)

> llmwiki 전체 구조 점검, 타 도구(Cursor 등)의 형제 레포 변경사항 반영 및 동기화, `wiki-lint` 결과 및 pending raw 파일 요점 정리.

## 🌱 쉽게

다른 코딩 도구들이 각 프로젝트(`MantisAlgo`, `ShiftTrade`, `AccountingGo`)를 대폭 수정한 내역을 확인하고, 이를 지식 위키에 연동시켰습니다. 새로 추가된 모듈(`sig_governor`)을 위키에 자동 반영하고, 누락된 회계 앱 관련 기록을 찾아내 인덱스에 넣었습니다. 위키의 모든 링크는 100% 정상 작동하며, 새로 들어온 3개의 참고 문서(Karpathy LLM Wiki, 옵시디언 정리 팁 등)의 인제스트 방향을 정리했습니다.

## ⚙️ 정확히

### 1. 형제 레포 변경사항 동기화 및 위키 반영

각 프로젝트 저장소의 `git status`를 확인하여 최근 변경사항을 감지하고 위키를 동기화했습니다.

- **MantisAlgo**: 
  - 신규 모듈 `sig_governor.py` (Signal Governor) 및 관련 테스트/캘리브레이터가 추가되었습니다.
  - `registry_to_wiki.py`를 실행하여 `wiki/modules/sig_governor.md`를 생성하고 `modules-map.md`를 업데이트했습니다 (총 모듈 수 **173 -> 174**로 증가).
  - 이에 맞춰 `wiki/index.md`의 모듈 카탈로그 설명을 174개로 갱신했습니다.
- **ShiftTrade**: 
  - `DEVELOPMENT_MAP.md` 및 `hermes/microstructure-engineer.md`가 수정되었습니다. (구조적 연결 확인 완료)
- **AccountingGo**: 
  - Master Polish Plan Phase 2–4가 마감되었습니다.
  - 이 과정에서 생성되었으나 `wiki/index.md`에서 누락되어 고아(orphan)로 남아있던 `queries/accountinggo-master-polish-phase2-4-2026-07-17.md`를 발견하여 `index.md`에 링크를 등록했습니다.

### 2. 구조 Lint 결과

`/Users/kkj/.gemini/antigravity/brain/e0270ea4-f1e6-4e63-84f9-496ba0d524d8/scratch/wiki_lint.py`를 작성하여 위키 전체를 검사했습니다.
- **총 마크다운 파일**: 244개
- **깨진 링크**: 0개 (SCHEMA나 인덱스의 템플릿 설명용 플레이스홀더 `[[위키링크]]` 등 외에 실제 지식 링크는 무결함)
- **고아/미도달 페이지**: 0개 (AccountingGo Phase 2-4 누락 해소 후 0 달성)
- **전체 정합성**: 이상 없음.

---

## 🔗 연결

- [[llm-wiki-pattern]] · [[structure-lint-2026-07-17]] · [[llmwiki-fragility-2026-07-17]] · [[accountinggo-master-polish-phase2-4-2026-07-17]] · [[modules-map]]

## 📌 미해결 (pending raw — 2026-07-18 폐기)

실험용 raw 3클립 + 공장 복제 pine 22개는 **인제스트 없이 삭제**함 (곽경준 승인).

| 폐기 | 이유 |
|---|---|
| hada.io LLM-Wiki 요약 · nashsu/llm_wiki commit diff · 칼퇴연구소 YouTube | Karpathy 원문·SCHEMA에 이미 반영 / 타 제품 노이즈 / 기준은 이미 Capture≠Ingest로 충분 |
| `raw/pine-*.pine` ×22 | SoT=`MantisAlgo/pinescript_factory/` + `wiki/pines/` — raw 복제는 중복 |

남긴 raw (이미 소화·출처 추적): `llm-wiki-karpathy.md` · accounting 노트/JSON · `pine-v6-learning-system-idea.md`
