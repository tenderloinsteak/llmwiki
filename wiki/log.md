# Log — Chronological Record

Append-only. Entry format: `## [YYYY-MM-DD] ingest|query|lint | title`

---

## [2026-07-16] init | Wiki created
Structure initialized per Karpathy LLM Wiki pattern: SCHEMA.md, index.md, log.md, raw/{articles,papers,transcripts,assets}, entities/, concepts/, comparisons/, queries/. Operated via librarian-profile skills wiki-ingest / wiki-query / wiki-lint; `WIKI_PATH` set in all 11 Hermes profiles. First suggested sources: external marketplace scripts to dissect (tutor track), TradingView market research (factory-idea track).

## [2026-07-16] init | Vault reorganized under Desktop/dev
Desktop repos (Mantis Algo, ShiftTrade, AccountingGo, pinestudy) and the obsidian vault moved into `Desktop/dev/`. All path references updated (11 SOUL.md, 14 skills, .env WIKI_PATH, wiki + repo hermes files). Vault-root IDEA.md filed as raw/articles/pine-v6-learning-system-idea.md (not yet ingested).

## [2026-07-16] ingest | Initial build: 36 pages from 3 repos + Hermes org
Analyzed Mantis Algo / ShiftTrade / AccountingGo repos and Hermes org. Built: 4 project/org hubs, 9 system pages, 11 persona pages, 12 concept pages — all on the 🌱/⚙️/🔗/📌 template. Karpathy gist fetched → raw/articles/llm-wiki-karpathy.md → concepts/llm-wiki-pattern. Repo entry points (AGENTS.md, DEVELOPMENT_MAP.md, README.md) now point here for cross-tool context. Lint: 0 broken links, 0 orphans.

## [2026-07-16] lint | Auto-accumulation enabled
SCHEMA gained auto-accumulation rules (fetch→raw without asking, auto-file syntheses, external-code analysis flow via raw/code/). Vault root CLAUDE.md + AGENTS.md created so Claude Code/Codex/Cursor load the same discipline. wiki-query now files automatically; wiki-ingest triggers on any self-fetched source.

## [2026-07-16] ingest | Full-tool coverage + module graph + taste/ideas capture
Cursor rules (.cursor/rules/wiki-auto-accumulation.mdc) in vault + 3 repos; AGENTS.md created for ShiftTrade & AccountingGo; all 11 SOUL.md gained the wiki line. registry_to_wiki.py generates modules/ (163) + skus/ (8) + modules-map hub — found drift: SKU-05/06/07 missing from registry product_skus mapping (flagged ⚠️ on their pages). New living pages: entities/kkj-taste.md (preference ledger, esp. UI/UX) + ideas/ideas-inbox.md — agents append without asking (SCHEMA rules 4-5).

## [2026-07-16] lint | Vault renamed: dev/obsidian → dev/llmwiki
User-created empty llmwiki vault merged in (its .obsidian config kept). All references rewritten (profiles, skills, .env WIKI_PATH, repo docs, cursor rules, registry_to_wiki.py). Symlink dev/헤르메스 → llmwiki/hermes. Links re-verified clean.

## [2026-07-16] lint | Full dev-tree audit after user reorg
User renames handled: "Mantis Algo"→"MantisAlgo", pinestudy moved back to Desktop/pinestudy — all references updated (profiles, skills, .env, wiki, repo docs, cursor rules, sync & registry scripts). Stale Desktop/obsidian fragment (02:01 sync output to old path) merged into llmwiki/hermes and removed. Symlink OK, wiki links/index CLEAN, no absolute paths in repo code, git intact ×4. Note: Cursor session auto-filed its first query page (integration status) — auto-accumulation confirmed working.

## [2026-07-17] ingest | MantisAlgo module kind split + 10 new modules + UI audit gate
registry.json modules gained a first-class `kind` field (ui/logic/infra) to separate the chart display layer from factory analysis logic. 10 new modules added (163→173): 5 logic (volatility squeeze, TD-style exhaustion count, engulfing/pinbar patterns, auto-fibonacci, OBV divergence) + 5 UI (signal legend, live perf-accuracy panel, alert log, top info bar, gradient bar coloring). New `ui_audit.py` + `scripts/module_lint.py` mechanically enforce tooltip/group coverage, default-off declutter, and the signature palette (bull=teal/bear=orange/neutral=gray) — closing a gap where the `hermes/factory-ui.md` "zero findings" pass bar had no machine backing (0% tooltip coverage before this). Indicator repaint-ban prompt requirement removed per explicit user direction (indicators aren't backtested — visual persuasiveness now outranks strict signal timing); strategy prompts unchanged. `registry_to_wiki.py` extended to carry `kind` and re-run (173 module pages + modules-map kind section). Updated: entities/mantisalgo-module-registry, mantisalgo-verification-gate, mantisalgo-pipeline.

## [2026-07-17] lint | git hygiene gap found in llmwiki itself
`wiki/`, `.cursor/`, root `AGENTS.md`/`CLAUDE.md`, `hermes/scripts/registry_to_wiki.py` are entirely untracked in this repo's git — 200+ wiki pages exist only on disk, no commit history. 11 persona souls + memory.md + hermes/CLAUDE.md + sync-cursor-agents.py are tracked but have uncommitted changes (pre-existing, not from this session). Not committed here to avoid mixing unrelated changes — flagged for 곽경준 to review and commit.

## [2026-07-17] ingest | MantisAlgo TradingView 상용급 감사·개선 + 카테고리 택소노미 + mantis/ 패키지화
- 품질 감사 결과 filed: [[queries/mantisalgo-quality-audit-2026-07-17]] (컴파일 불가 2건 발견→수리, verify 차단 3종·루브릭 상용 체크 5종 신설, A13/B12/C0)
- 터치한 페이지: mantisalgo(허브 — mantis/ 구조·30 카테고리·자산 현황), mantisalgo-verification-gate(검사 강화 상세 + 리페인트 정책과의 관계 명시), mantisalgo-sku-catalog(Mantis 카테고리 재배치 + 품질 스냅샷), mantisalgo-pipeline(mantis/ 패키지 구조 + 저장 경로)
- 상충 없음 — 인디케이터 리페인트 허용 정책(07-17)과 lookahead 게이트는 "금지 아닌 문서화 강제"로 양립

## [2026-07-17] lint | MantisAlgo 구세대 산출물 3개 폐기 (곽경준 지시)
- MA_Cross_Volume_Indicator·Generated_Pine_Strategy·Donchian_ATR_Squeeze_Pulse 삭제 (툴팁 0%·데모 수준). 제품 22개, A13/B9/C0. 아이디어 레지스트리 항목은 중복 방지용으로 유지.

## [2026-07-17] ingest | TV 실컴파일 피드백 → CE10272/CW10002 구조 근절 + 차트 declutter
- SKU-02 신고 오류 4건 수정 + 동종 잠복 버그(SKU-08 3건, 독립 파일 9개) 일괄 해소. verify 차단 2종·자동 호이스터·registry deps 7건·마커 게이트 39곳. 제품 22개 A14/B8. 터치: mantisalgo-verification-gate

## [2026-07-17] lint | structure-review follow-ups closed
- AlertHub tv_safety 정책 정합(86 pytest pass). Cursor rule·SKU-01..08 product_skus·modules-map 미매핑 해소. wiki/ 최초 커밋 진행. → [[queries/mantisalgo-structure-review-2026-07-17]]

## [2026-07-17] query | AccountingGo Master Polish Plan

- Filed [[queries/accountinggo-master-polish-plan-2026-07-17]]; updated [[entities/accountinggo]] + [[entities/accountinggo-content-pipeline]].
- Repo SoT: `docs/MASTER_POLISH_PLAN.md` (path fix: theory player under `lib/features/exercise/`).
- Next recommended task: **0-1 tAccount** full posting interaction.

## [2026-07-17] lint | structure + cross-folder + skills inventory

- Skills confirmed: librarian `wiki-ingest`/`wiki-query`/`wiki-lint`/`hermes-wiki-maintenance` + `llm-wiki` ×11 profiles; WIKI_PATH ×11 OK.
- Structural: 229 md, 0 broken/orphan/index-drift; SKU unmapped=0; modules=173.
- Fixed in-vault: MantisAlgo path remnants (registry_to_wiki + 182 module/sku sources + kkj-taste + CURSOR-AGENTS + vault cursor rule); factory-module-developer 163→173.
- Pending (sibling/outside): 3 repo `.cursor/rules` still say `Mantis Algo/`; Hermes SOUL module-developer still `(163 modules)`.
- Filed [[queries/structure-lint-2026-07-17]].

## [2026-07-17] lint | follow-up: sibling rules + SOUL count
- Fixed `Mantis Algo/` → `MantisAlgo/` in MantisAlgo/ShiftTrade/AccountingGo `.cursor/rules/wiki-auto-accumulation.mdc`
- Fixed `~/.hermes/profiles/factory-module-developer/SOUL.md` (163→173 modules)
- Closed 📌 items 1–2 on [[queries/structure-lint-2026-07-17]]

## [2026-07-17] query | Karpathy LLM Wiki vs our implementation
Filed [[comparisons/karpathy-llm-wiki-vs-llmwiki]]. Verdict: core pattern (3 layers + ingest/query/lint + index/log) faithfully instantiated; intentional extensions (Hermes split, Korean template, auto-accumulation, registry mirror); practice gaps (thin raw/, empty comparisons until now, optional tips unused).

## [2026-07-17] lint | clarify shared ops journal (not Hermes-only)
- CLAUDE/AGENTS/SCHEMA + vault&3repo cursor rules: `hermes/memory.md` = shared journal for Cursor/Claude/Codex/Hermes; session start now includes `tail -20 memory.md`.

## [2026-07-17] query | AccountingGo Master Polish Phase2-4 complete

Phase 0–4 실행 트랙 마감. P0 인터랙션 게이트 해제, CI/릴리스 체크리스트/피드백 prefs/마스코트 v1 반영. 상세: [[entities/accountinggo]] · 레포 `docs/MASTER_POLISH_PLAN.md`.

## [2026-07-17] query | LLM wiki fragility assessment
Filed [[queries/llmwiki-fragility-2026-07-17]]. Top risks: thin raw fuel, prompt-only discipline, silent wrong-compounding, module-mirror drowning curated graph, unused contradiction/ideas loops.

## [2026-07-17] ingest | MantisAlgo Phase 1 signal density engine

## [2026-07-17] ingest | Accounting multilingual terminology registry Wave1

- Raw: `raw/articles/accounting-terms-wikipedia-summaries-2026-07-17.json`, `accounting-terminology-research-notes-2026-07-17.md`
- Living: [[accounting-terminology-registry-index]] + `concepts/accounting-terminology-registry.json` (**314** = 143 concepts + 171 accounts)
- Hubs: [[accounting-terminology-matrix]] · [[accounting-locale-registry]]
- Filed: [[queries/accounting-multilingual-terms-wave1-2026-07-17]]
- ko 314 filled (`kkj:?`); ja/zh/de/… mostly PENDING (no mass MT)


## [2026-07-17] lint | raw/articles → raw/clips (catch-all inbox)
- Renamed folder; Web Clipper + agent fetches default to `wiki/raw/clips/` for everything (blog/wiki/YouTube/code). Specialized papers/code/transcripts optional only.

## [2026-07-17] lint | flatten raw/ to single inbox
- Removed clips/papers/code/transcripts subfolders. All sources live flat in `wiki/raw/`; only `raw/assets/` kept for images. Web Clipper inbox = `wiki/raw/`.

## [2026-07-17] lint | Capture≠Ingest (Karpathy collaboration)
- SCHEMA/CLAUDE/AGENTS/Cursor rules + librarian wiki-ingest: raw capture stays auto; wiki compile requires takeaway discussion (or 알아서/배치). Removed accidental `wiki/queries 1/` duplicate.
- Pending collaborative ingest: `raw/LLM-Wiki - LLM을 활용하여 개인 지식저장소 구축 하기.md`, `raw/docs update feature overview.md`

## [2026-07-18] query | 지식 위키 및 형제 레포 전체 구조 감사
- MantisAlgo 신규 모듈 `sig_governor` 감지 및 `registry_to_wiki.py` 실행을 통한 위키 반영 (모듈 173 -> 174).
- `index.md` 모듈 지도 개수 업데이트 및 누락 고아 파일 `queries/accountinggo-master-polish-phase2-4-2026-07-17` 인덱스 등록 완료.
- `wiki_lint.py` 검사로 broken link / orphan 0개 확인. 3개 pending raw 파일 요약 및 인제스트 방향 정리.
- 사서(librarian), 개발, 기획, UI, 공장장 등 11개 프로필에서 사용하던 모든 프로젝트 커스텀 스킬 총 18종을 Gemini/Antigravity 환경(~/.gemini/config/skills/)으로 이식 및 등록 완료.

## [2026-07-18] ingest | Pine 분석 및 한 줄 해설서 프레임워크 뼈대 구축 및 스킬 동기화
- `llmwiki` 내에 두 스킬의 정본(Source of Truth) 개념 문서인 [[concepts/pine-script-analysis-framework]] 및 [[concepts/pine-explainer-generation-framework]]를 작성하여 지식 자산으로 수록.
- **중복 스킬 간소화 및 통합**: 별개로 존재하던 `pine-analyst-toolkit` 및 `pine-explainer-generator` 스킬 디렉토리를 전면 폐기하고, 그 기능을 각각 기존 스킬인 `mantisalgo-module-registry` 및 `tutoring-session`에 통합함으로써 에이전트 스킬 엔트로피를 최적화하고 지식 위키를 정본으로 정렬함.



## [2026-07-18] query | Pine 평탄 저장 + 다대다 카테고리 연결 구조
폴더=단일부모 한계 → factory 평탄 + `// Tags:` SoT + wiki `pines/scripts`↔`pines/categories` wikilink 다대다 제안. 결정 대기.
