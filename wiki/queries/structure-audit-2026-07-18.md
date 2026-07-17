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

## 📌 미해결 (사용자 인제스트 대기 소스 요약)

`wiki/raw/`에 새로 수집(Capture)되어 대기 중인 3개의 문서를 분석했습니다. 인제스트(Ingest) 여부와 강조할 중심점에 대해 논의가 필요합니다.

### 1. `raw/LLM-Wiki - LLM을 활용하여 개인 지식저장소 구축 하기.md`
- **핵심 요약**:
  - **compounding artifact**: 검색할 때마다 관련 본문을 임베딩으로 찾아 쓰는 RAG와 달리, 매 인제스트마다 LLM이 기존 위키 페이지(10~15개)를 점진적으로 업데이트 및 교차 연결하는 영속적 지식베이스 구축.
  - **비용의 제로화**: 위키 관리의 최대 난제인 '유지보수(bookkeeping)' 비용을 LLM이 대폭 낮춤으로써 개인의 Zettelkasten 관리가 현실화됨.
  - **사용자 검토 의견**: 
    - *모델 붕괴(collpase)*: AI가 글을 반복 요약하다 보면 정보가 얇아지거나 2차 오류가 복리로 쌓일 수 있으므로 검수(편집국 구조)가 중요함.
    - *Zettelkasten의 진의*: 직접 글을 쓰면서 뇌에서 생각이 정리되는 것인데, AI가 다 써주면 생각하는 능력을 잃거나 기술 부채가 될 수 있음.
- **인제스트 제안**: [[concepts/llm-wiki-pattern]] 페이지에 'RAG와의 차이점', '모델 붕괴 및 지식 부채 우려와 극복 방안' 문단으로 나누어 보강.

### 2. `raw/docs update feature overview.md`
- **핵심 요약**:
  - **다중 포맷**: PDF, Office 외에도 ePub/Mobi 문서, 웹 클립 등을 통틀어 파싱 지원.
  - **로컬 보안**: 복잡한 레이아웃을 처리하는 MinerU 파싱을 클라우드뿐 아니라 로컬 API/파이프라인 모드로 지원하여 기밀 보장.
  - **유지보수 도구**: 전체 위키의 ZIP 백업 및 기존 마크다운 파일들로부터 `wiki/index.md`를 결정론적으로 다시 재구축(rebuild)하는 기능 포함.
- **인제스트 제안**: [[entities/llm-wiki-pattern]] 또는 [[entities/hermes-org]]의 도구/인프라 섹션에 최신 LLM-Wiki의 발전(로컬 파싱, ePub 지원, 인덱스 재구축) 내용으로 요약 추가.

### 3. `raw/옵시디언 LLM Wiki, 아무 자료나 넣으면 안 됩니다  LLM Wiki 만들기 전에 꼭 정해야 하는 2가지.md`
- **핵심 요약**:
  - **수집 필터 (3가지 중 2개 만족 시 보관)**: 1) 다시 사용할 가능성이 높은가 2) 의사 결정에 영향을 주는가 3) 내 프로젝트/업무와 연결되는가. 5분 이상 정리가 필요하다면 보류.
  - **단일 볼트(Vault) 원칙**: 부서별로 볼트를 나누면 링크와 검색이 끊김. 또한 현실의 자료는 부서 경계에 걸쳐 있으므로 폴더가 아닌 속성(Attributes/YAML)으로 다중 지정할 것.
  - **볼트 분리 예외**: 기밀/보안상 AI 컨텍스트 차단 필요, 목적의 완전한 불일치(개인 학습 vs 업무), 템플릿/흐름의 이질성.
- **인제스트 제안**: [[wiki/SCHEMA.md]] 자체의 캡처/인제스트 세부 행동 강령을 보완하거나, [[concepts/llm-wiki-pattern]]에 '옵시디언 볼트 설계와 수집 기준' 개념 페이지로 신설.
