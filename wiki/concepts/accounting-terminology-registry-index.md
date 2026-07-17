---
tags: [accounting-edu, accountinggo, i18n]
created: 2026-07-17
updated: 2026-07-17
sources:
  - "concepts/accounting-terminology-registry.json"
  - "raw/accounting-terms-wikipedia-summaries-2026-07-17.json"
  - "raw/accounting-terminology-research-notes-2026-07-17.md"
  - "repo: Desktop/dev/AccountingGo/assets/content/en|ko/glossary.json"
  - "repo: Desktop/dev/AccountingGo/assets/content/en|ko/accounts.json"
---
# 회계 용어·계정과목 레지스트리 인덱스

> 기계가독 정본: [[accounting-terminology-registry.json]] — **314 entries** (concept 143 + account 171).

## 🌱 쉽게

개념 용어(glossary)와 계정과목(accounts)을 한데 모은 **큰 장부**다. 마크다운 표만으로는 수백 개가 안 돌아가서 JSON이 본체다. 영어·한국어는 314칸이 찼고, 일본·중국·유럽 등은 출처 확인된 칸만 소수 채워 두었다 — 빈칸을 번역기로 채우지 않는다.

## ⚙️ 정확히

### 규모 (2026-07-17)

| 구분 | 수 |
|---|---:|
| total | **314** |
| concepts (`glossary.json` v1) | 143 |
| accounts in-app (`accounts.json` v1) | 43 |
| accounts expanded (수험 COA 골격, 앱 미편입) | 128 |

### 로케일별 term 채움

| locale | filled | pending | 비고 |
|---|---:|---:|---|
| en-US | 314 | 0 | 앱 authoring SoT |
| en-UK | 314 | 0 | 지금은 en-US 복제+`CAND` — synonym pass 필요 |
| ko | 314 | 0 | 전부 `kkj:?` 검수 대기 |
| ja | 10 | 304 | `W`만 |
| zh-CN | 4 | 310 | `W`만 |
| de | 4 | 310 | `W`만 |
| fr | 1 | 313 | `W`만 |
| es | 3 | 311 | `W`만 |
| pt-BR | 0 | 314 | 미착수 |
| hi | 0 | 314 | 미착수 (CA는 영어 본문 多) |

### 한국어 검수 우선 플래그

| id | 이슈 |
|---|---|
| `supplies` | 레포 accounts=`비품` vs 수험 기본안=`소모품` (비품≈furniture/fixtures) |
| `equipment` | 레포=`비품·설비` vs 수험=`비품` |
| `accounts_receivable` / `accounts_payable` | 매출채권·매입채무 ↔ 외상매출금·외상매입금 `DUAL` |
| `balance_sheet` | 재무상태표 ↔ 대차대조표 `DUAL` |

### 채움 규칙 (강제)

1. `PENDING` 셀을 사전/LLM 직역으로 채우지 않는다.
2. 채울 때 `status` + `note`(출처) 필수. 가능하면 raw/에 1차 자료 저장.
3. ko는 곽경준 검수 후 `kkj: "✓"`.
4. expanded account를 앱에 넣으려면 먼저 `accounts.json`에 id 추가.

스키마 요약: 각 entry = `{id, kind: concept|account, labels: {locale: {term, alts, status, note, kkj?}}}`.

상세 매칭·운영: [[accounting-terminology-matrix]] · 나라별 앵커: [[accounting-locale-registry]]

## 🔗 연결

[[accounting-terminology-matrix]] · [[accounting-locale-registry]] · [[accountinggo-i18n]] · [[accountinggo]] · [[queries/accounting-multilingual-terms-wave1-2026-07-17]]

## 📌 미해결

1. 곽경준: ko 314칸 검수 (우선 위 플래그 4건)
2. ja: 日商簿記 계정과목표 기준으로 171 accounts 채우기
3. zh-CN: 初级会计 会计科目表 기준 채우기
4. de/fr/es/pt-BR: Kontenrahmen / PCG / PGC / CPC 기준 채우기
5. en-UK synonym pass (stock, debtors, creditors, turnover, …)
6. expanded 128개를 앱 `accounts.json` 편입 여부 결정
