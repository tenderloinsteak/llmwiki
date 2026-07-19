# Memory — Cross-session Log

Append after every work session. Old entries get compacted by [[personas/librarian]].

Format: `date | persona | decision/progress | next`

---

- 2026-07-15 | orchestrator | Created Hermes wiki (base 3 + 7 role personas + index). Writing-style profile not yet set — run "learn my writing style" in a future session | Fill user.md blanks; decide Obsidian vault location
- 2026-07-15 | factory-manager | Restructured factory into 4 role parts: idea & UI (top importance), module-developer, development | Confirm UI palette
- 2026-07-15 | orchestrator | Analyzed all three repos. Mantis Algo: working LLM factory (163 modules, 8 SKUs, verification gate). AccountingGo: Flutter MVP, 13 question types, English-first content pipeline. ShiftTrade: Next.js+Supabase, Python tick engine (NemotronEngines). Rewrote entire wiki in English with reason-in-English/answer-in-Korean rule; renamed all files to English | User pastes profiles into Hermes; fill remaining blanks (palette, pricing)
- 2026-07-15 | orchestrator | Split character vs knowledge: profiles now carry only persona character (profiles/1-8); working knowledge moved into each repo's hermes/ folder (Mantis Algo: 6 files, ShiftTrade: 1, AccountingGo: 2). Wiki keeps CLAUDE/soul/user/memory + tutor & librarian | Paste profiles/1-8 into Hermes profile soul.md fields
- 2026-07-15 | tutor | Created `study/` substructure in wiki: `pinescript-roadmap.md` (Track A Spine, Stages 0–9, each w/ goal·concept·analogy·practice·MantisAlgo-link·pass-criteria), `learning-log.md`, `note-template.md`, `notes/index.md`. Linked from `personas/tutor.md` + `CLAUDE.md`. Wiki real path = `Desktop/dev/llmwiki/hermes/` (not `Desktop/dev/헤르메스/`). | Start Stage 0 (TradingView Pine Editor setup) next session
- 2026-07-16 | orchestrator | Created per-profile workflow skills (skills/hermes/, 1 per profile ×11: production-run, idea-spec, visual-review, module-registry, pipeline-dev, audit, question-authoring, learning-ux, market-realism, tutoring-session, wiki-maintenance) + 3 knowledge-wiki ops skills in librarian (wiki-ingest/query/lint). Consolidated wiki: Desktop/dev/헤르메스 merged into Desktop/dev/llmwiki/hermes (newer tutor.md kept; symlink 헤르메스→obsidian/hermes); all SOUL.md paths fixed. Initialized knowledge wiki at Desktop/dev/llmwiki/wiki (SCHEMA/index/log/raw+4 page dirs); WIKI_PATH set in all 11 profile .env | First ingest into obsidian/wiki; confirm skills load in fresh Hermes sessions
- 2026-07-16 | orchestrator | Desktop reorganized: Mantis Algo, ShiftTrade, AccountingGo, pinestudy, obsidian vault (+헤르메스 symlink) moved into Desktop/dev/. All references rewritten to dev/ paths across 11 SOUL.md, 14 skills, 11 .env (WIKI_PATH), wiki files, repo hermes/*.md. Vault IDEA.md → wiki/raw/articles/pine-v6-learning-system-idea.md | Re-open Obsidian vault at Desktop/dev/llmwiki; first wiki ingest
- 2026-07-18 | tutor | 5교시 완료 (코드 비교 학습: A=MantisAlgo SKU-09 / B=LunqFX Plasma Flow). 체크 17/952 확정. 신규 구조: user_profile.md / code_quality_prefs.md / learning_analytics.md, study/ 비교교재. 인터넷 끊김 후 유실 우려 → 점검: 파일 전부 실재·정합성 OK. GitHub 인증 없었음 → gh auth login (tenderloinsteak) → private repo `tenderloinsteak/pinestudy` 신규 생성 + 로컬 커밋 b21ca41 + push 완료 (origin/main 동기화). .gitignore 추가(.obsidian/.DS_Store 제외) | 6교시: B 신호부 전체 조망. 미해결: .obsidian 추적해제(git rm --cached -r .obsidian)는 보류 — 학습내용 무관
- 2026-07-16 | librarian | Knowledge wiki initial build complete: 36 pages (projects 3 + hermes-org + systems 9 + personas 11 + concepts 12), Karpathy source ingested, repo entry points linked, lint clean. Wiki = dev/llmwiki/wiki, journal stays here | First real ingest (market microstructure survey or external-script dissection); revisit SKU-level pages when sales strategy work starts
- 2026-07-16 | librarian | Auto-accumulation enabled: SCHEMA rules (fetch→raw, auto-file answers, code-analysis flow), vault root CLAUDE.md/AGENTS.md for cross-tool discipline, wiki-query/ingest skills updated, raw/code/ created | Optional next: registry→wiki sync script (module graph), weekly auto-lint schedule
- 2026-07-16 | librarian | Cross-tool auto-accumulation완성: Cursor rules ×4, AGENTS.md (ShiftTrade·AccountingGo 신규), SOUL ×11 위키 라인, registry_to_wiki.py(모듈163+SKU8 그래프, 드리프트 발견: SKU-05/06/07 레지스트리 미매핑→module-developer 확인 필요), kkj-taste·ideas-inbox 자동 기록 페이지 | 주간 lint 스케줄; SKU 매핑 드리프트 해소

- 2026-07-16 | cursor | New session prep: synced Cursor agents from Hermes SOUL, confirmed ceo.md wiki path, enabling auto-accumulation rules (raw/ filing, kkj-taste, ideas-inbox) for this session | Apply wiki auto-accumulation going forward
- 2026-07-16 | cursor | Session-prep smoke + structure audit: ceo.md already has Desktop/dev/llmwiki; SCHEMA/index/rules/AGENTS/SOUL wiring intact on disk. Gap: this Cursor window still rooted at Desktop/Mantis Algo (gone) not Desktop/dev/MantisAlgo — project alwaysApply wiki rules not loaded here; auto-accumulation is prompt-only (no mechanical gate); taste/ideas explicit only in CEO SOUL; queries/ideas-inbox never exercised | Re-open Cursor at Desktop/dev/*; optional harden specialist SOULs with taste/ideas lines

- 2026-07-16 | cursor | Progress check: infra wiring mostly done (wiki~215p, Hermes WIKI_PATH×11, Cursor rules×3repos). Open: SKU-05/06/07 registry drift; real ingest loop thin; weekly lint unset; tutor Stage0 not started; pinestudy path missing under Desktop/dev. Repo WIP: Mantis/ShiftTrade uncommitted wiki hooks; AccountingGo on gamification-feedback-i18n-gate with large KO content diffs. This Cursor workspace = Desktop/dev/llmwiki (path gap from earlier session closed) | Pick next: (1) Stage0 study (2) SKU drift fix (3) AccountingGo branch ship (4) first external-script/microstructure ingest
- 2026-07-16 | librarian | dev 전수 점검: 사용자 리네임(MantisAlgo, pinestudy→Desktop) 참조 전면 수정, Desktop/obsidian 잔해(구경로 sync 출력) llmwiki로 병합 후 제거, 링크·색인 CLEAN, repo 코드 절대경로 0, git 4개 정상. Cursor 자동 파일링 첫 사례 확인(queries/llmwiki-integration-status) | 홈·AI_AGENT_LEARN 빈 폴더 용도 결정; sync 스크립트 재실행으로 ~/.cursor 미러 갱신
- 2026-07-17 | factory-module-developer (Cowork) | **MantisAlgo 모듈에 1급 `kind` 분류 도입**: ui(26)/logic(134)/infra(13), `modules_by_kind()` API. 갭 분석 후 신규 10모듈 추가(163→173): 로직 5(mt_squeeze_detector, mt_exhaustion_count, pat_engulfing_pinbar, struct_fib_auto, vol_obv_divergence) + UI 5(ui_signal_legend, ui_perf_stats_panel, ui_alert_log_panel, ui_top_info_bar, ui_gradient_bar_coloring). `ui_audit.py`(신설) + `scripts/module_lint.py`(신설, 모듈 카탈로그 단위 린트)로 툴팁/그룹 100%·declutter·팔레트 기계 검증, factory_gate 전체 통과. 인디케이터 리페인트 금지 조항 제거(전략은 유지) — 곽경준 명시 지시, "성과·비주얼이 이론보다 우선, 백테스트 대상 아님". `registry_to_wiki.py`를 kind 태그 포함하도록 확장 후 재실행(173페이지+modules-map). 지식 페이지 갱신: mantisalgo-module-registry, mantisalgo-verification-gate, mantisalgo-pipeline | 스킬 4종 완료·3환경 배포됨: (1) Cowork .skill 4개 전달 (2) Cursor: MantisAlgo/.cursor/commands/ 4개 + mantis-algo-context.mdc에 자연어→커맨드 라우팅 표 추가 (3) Hermes: factory-ui 프로필에 mantis-ui-module-{update,lint}, factory-module-developer 프로필에 mantis-strategy-module-{update,lint} 설치 (skills/hermes/). 주의: factory-module-developer의 기존 mantisalgo-module-registry 스킬과 트리거 일부 겹침(등록/감사 계열 발화) — 신규 스킬이 더 구체적이라 우선 매칭될 것으로 예상, 혼선 시 기존 스킬 description 좁히기
- 2026-07-17 | librarian (Cowork) | **git 위생 점검**: llmwiki 저장소에 `wiki/`, `.cursor/`, 루트 `AGENTS.md`/`CLAUDE.md`, `hermes/scripts/registry_to_wiki.py` 전체가 미추적(untracked) 상태 — 위키 콘텐츠 200+ 페이지가 git 이력 없이 디스크에만 존재. 추가로 persona souls 11개·`hermes/memory.md`·`hermes/CLAUDE.md`·`sync-cursor-agents.py`가 추적되지만 미커밋 상태로 남아있음(이전 Cursor/Hermes 세션 산출물로 추정, 이번 세션에서 만든 것 아님). 이번 세션은 무관한 변경을 섞지 않기 위해 커밋을 하지 않음 | 곽경준 확인 후 `git add -A && git commit`으로 wiki 전체를 최초 커밋 권장 (현재 유실 위험 있음)
- 2026-07-17 | cursor | structure-review follow-ups 전부 처리: AlertHub 테스트 정합(86 pass), Cursor rule 현행화 확인, registry product_skus SKU-01..08, registry_to_wiki 재동기화, llmwiki wiki/ 최초 커밋 | 일상: 모듈 변경 시 registry_to_wiki 습관화

- 2026-07-17 | cursor (AccountingGo) | Master Polish Plan 접수·위키 반영. 레포 `docs/MASTER_POLISH_PLAN.md` SoT. 실측: tAccount 216줄(잔액만)/trialBalance 166줄(스텁)/theory 271줄(exercise/). P0 게이트 미해제. 브랜치 `cursor/gamification-feedback-i18n-gate`에 ko WIP 공존 | 다음: **0-1 tAccount** 착수 확인 후 세션 시작

- 2026-07-17 | librarian | Structure lint: wiring OK (llmwiki↔3repos↔pinestudy↔Hermes×11). Skills YES (wiki-ingest/query/lint + llm-wiki×11). Fixed vault path remnants MantisAlgo. Pending: sibling cursor rules + SOUL 163→173 | Optional: approve sibling rule fix; weekly lint cron; first comparison page

- 2026-07-17 | librarian | Closed lint follow-ups: 3 repo cursor rules MantisAlgo path + factory-module-developer SOUL 163→173 | Remaining: comparisons/ingest depth, weekly lint cron, tutor Stage0

- 2026-07-17 | cursor (AccountingGo) | Master Polish Phase 0 완료(0-1 tAccount/0-2 trialBalance/0-3 theory grammar v1 동결/0-4 모듈감사+F1–F4 수정). Phase 1 부분: exercise 상단바·이탈시트·콤보≥3·피드백 SRS 카피·하트소진→복습. 테스트 40통과. 잔여: 1-3 result 카운트업, 1-4 skill tree, Phase 2–4 | 다음 세션 Phase 1 잔여부터 계속

- 2026-07-17 | cursor (AccountingGo) | Phase1 잔여+Phase2 일부: result 카운트업·스킬노드5상태(mastered)·섹션진행률·온보딩 배치/첫레슨·복습하트보상·ag_motion 토큰. 테스트40통과 | 다음: Phase2 잔여(홈 약한개념 티저 강화)·Phase3 테스트망/CI·Phase4 폴리시
- 2026-07-17 | cursor | 외부 벤더 브랜드명 scrub: MantisAlgo+llmwiki+canvas를 Mantis 택소노미/TradingView 상용 어휘로 치환. Cursor rule에 긍정 Wording 절 추가 | 에이전트는 금지 목록 대신 대체어만 사용

- 2026-07-17 | librarian | Compared Karpathy gist vs llmwiki: pattern YES; optional tips mostly unused; raw thin. Filed comparisons/karpathy-llm-wiki-vs-llmwiki | Optional: thicken raw ingest; decide human-in-loop ingest default

- 2026-07-17 | cursor | Clarified hermes/ is shared ops journal for all tools (not Hermes-only); session-start now reads memory.md; synced cursor rules ×3 repos | Keep appending one line per session from every tool

- 2026-07-17 | cursor (AccountingGo) | Master Polish Phase2–4 마감: Home Continue-first+약한개념·result 리텐션·SFX/햅틱 설정·코인마스코트·Semantics·CI·RELEASE_CHECKLIST·grader 골든·journal listEquals 버그픽스. 테스트 통과 | 출시 전 contentReviewUnlockAll/refillHeartsOnLaunch=false; ko WIP 커밋 여부 확인

- 2026-07-17 | cursor | Filed llmwiki fragility assessment (P0: raw thin, prompt-only gates, auto-file without verify) | Next if wanted: weekly lint cron + first real external ingest

- 2026-07-17 | cursor (MantisAlgo) | **Phase 1 신호 밀도 엔진 완료**: `signal_mirror`/`signal_calibrator`/`sig_governor`(INFRA_ALWAYS)·`signal_density_targets.json`·idea `signal_profile`+`extra.calibration`·factory_gate 밀도 게이트. 8/8 SKU 3×3 밴드 내. pytest 98 pass. 다음: Phase 2 비주얼 v2

- 2026-07-17 | cursor (AccountingGo) | 다국어 회계용어 레지스트리 Wave1: `wiki/concepts/accounting-terminology-registry.json` 314 entries (glossary 143 + accounts 43 in-app + COA 확장 128). en-US·ko 전셀 채움(ko=`kkj:?`). ja/zh/de/fr/es는 Wikipedia 검증분만. supplies 레포'비품' vs 수험'소모품' 플래그. | 다음: 곽경준 ko 검수 → ja 日商勘定科目 → zh 初级科目表

- 2026-07-17 | cursor | raw inbox = wiki/raw/clips/ catch-all (articles renamed); Clipper should point there | Set Obsidian Web Clipper folder to wiki/raw/clips

- 2026-07-17 | cursor | Flattened raw/ to one inbox (kept assets/ for images only); Clipper → wiki/raw/ | Point Obsidian Web Clipper at wiki/raw

- 2026-07-17 | cursor | Aligned to Karpathy: capture auto / ingest collaborative (SCHEMA+vault Cursor+AGENTS+Hermes wiki-ingest). Sibling repo rule sync still pending approval | Discuss 2 new raw clips before filing

- 2026-07-18 | antigravity | 전체 구조 감사 및 동기화: MantisAlgo 신규 모듈(sig_governor) 동기화, 고아 쿼리 페이지 인덱스 수리, 3개 raw 파일 요점 분석 완료. 사서(librarian) 및 개발/기획/UI/공장장/Tutor/Audit 등 11개 프로필의 모든 커스텀 워크플로우 스킬 총 18종을 현재 Gemini/Antigravity 도구 환경(~/.gemini/config/skills/)에 이식 및 일괄 등록 완료 | 3개 pending raw 파일 인제스트 승인 대기
- 2026-07-18 | antigravity | 중복 스킬 정리 및 llmwiki 정본 동기화: pine-analyst-toolkit 및 pine-explainer-generator 스킬을 폐기하고, 그 기능을 각각 기존 스킬인 mantisalgo-module-registry 및 tutoring-session에 완벽히 통합/미러링 완료 | 3개 pending raw 파일 인제스트 승인 대기 또는 다음 지시 대기




- 2026-07-18 | cursor | Pine 구조: 카테고리 폴더 폐기·평탄 저장 + Tags/wikilink 다대다 제안 파일링 (`queries/pine-flat-multitag-structure-2026-07-18`) | 곽경준 강조점 확인 후 factory flatten / wiki pines/ 착수

- 2026-07-18 | cursor | portability remediation (빈치환 25건 복구, 형제레포 치환, .env 분리, WIKI_PATH=레포루트 주입, SOUL.md 복구) | rehearsal on second machine

- 2026-07-18 | cursor | Pine 공장 평탄+제목통일+wiki pines/ 다대다 완료 (22 scripts, Tags SoT, factory_gate PASS) | 이후 신규 .pine은 평탄 저장; 동기화는 `pine_factory_to_wiki.py`

- 2026-07-18 | cursor | llmwiki GitHub 연동: private repo tenderloinsteak/llmwiki 생성, origin(SSH) + main push 완료 | 이후 git push로 동기화

- 2026-07-18 | cursor | raw 실험소스 폐기: clip 3 + pine복제 22 삭제; 공장 SoT만 유지; pine_factory_to_wiki raw복사 제거 | pending ingest 없음

- 2026-07-18 | cursor | wiki lint: path_gate OK, orphan/index drift 0; JSON wikilink+pine-flat stale raw note 수정 | pending ingest 없음

- 2026-07-18 | cursor | portability remediation (ShiftTrade 스크립트 상대경로, sync-cursor-agents 스크립트기준 resolve, PINESTUDY_PATH 도입, path_gate 강화) | 새 기기: clone → setup_env.py --init-env --force; 형제레포 커밋/푸시 권장

- 2026-07-18 | cursor | SKU-09 VWAP Regime Quality 조립: 기존 모듈 28종(VWAP밴드·레짐·스퀴즈·합류·거버너·UI패널)로 시중 레짐퀄리티 축 재현, static PASS / rubric A / density in-band 0.55 | 패널 밀도는 Phase2 UI 모듈 업그레이드 여지

- 2026-07-18 | cursor | username hardcodes scrub: kkj-taste→owner-taste, registry kkj→owner_review, ShiftTrade NEMOTRON_ENGINE_PATH, path_gate /Users/* | re-run sync-cursor-agents on new machine

- 2026-07-18 | cursor | SKU-09 TV 컴파일 수정: CE10123(plotshape series text→const ★티어) + CW10004(ta.atr 삼항 호이스트); verify_v2에 CE10123/CW10004 게이트+테스트 추가

- 2026-07-18 | cursor | UI 차별화: platform dashboard를 모듈적응형으로(VWAP+레짐→FLOW 3열 패널), vol_vwap_bands fill/그라디언트 승격 — SKU-09가 PAC 클론이 아니게

- 2026-07-18 | cursor | pinescript_generator 루트 복구(실수 flatten 이동) + wiki sync: SKU-09/pine 페이지 등록(indicator·MantisAlgo·Tags) · 카탈로그 01..09 | GitHub는 fix/portability-remediation 평탄 레이아웃; main은 아직 30카테고리 폴더

- 2026-07-18 | cursor | 공장 save_to_factory 후 wiki pines 자동 동기화 (mantis/wiki_sync.py); SKU regenerate는 pines+registry 일괄; WIKI_SYNC_ON_FACTORY=0으로 비활성

- 2026-07-20 | cursor | UI 세션1: est_lines 드리프트 4건 갱신 + 팔레트 위반 5모듈 teal/orange 정리; lint advisories 16→7, factory_gate ALL PASSED, SKU 재생성+wiki sync

- 2026-07-20 | cursor | UI 세션2+PartC: confluence 위치input(하단중앙)·ui_audit 코너중복 advisory·countdown/day_range smoke(sku_ship:false)·gate PASS

- 2026-07-20 | cursor | B-3 infra_common_series: 공용 ATR14/EMA50·100/RSI14/VolSMA20 모듈 추가, UI 7종 depends_on 전환, zone=PLATFORM_HELPERS, factory_gate ALL PASSED | neon/Part C 미착수

- 2026-07-20 | factory-ui | Part A 네온 UI 4종(flow/key_levels/beacon/sr_zones) smoke-only 추가, master_dim 보류, registry 183→187, lint0/gate PASS, SKU-08 미탑재

- 2026-07-20 | cursor | UI 계획 잔여 완료: B-3 infra_common_series·B-4/6/7 테마·compact·패널상수·네온4종 smoke(sku_ship:false)·레지스트리 187·gate PASS. A-5 master_dim·volume팔레트는 보류

- 2026-07-20 | factory-ui | Part D/E/F + A-5 UI 7종 추가(sparkline/sess_timeline/vol_bubble/outcome_badges/htf_ghost/led_strip/neon_dim), sku_ship:false, registry 187→194, lint0/gate ALL PASSED | SKU 미탑재

- 2026-07-20 | cursor | UI 잔여 계획 완료: vol팔레트·코너위치input·PartD/E/F 6종+A-5 master_dim(전부 sku_ship:false)·레지스트리 194·gate PASS

- 2026-07-20 | cursor | batch3/4 확정 실행: vol_bubble+outcome_badges(f_push_label·infra_label_manager dep)·htf_ghost+led_strip 스펙정렬·계획서 완료표시·registry/wiki 194 sync
