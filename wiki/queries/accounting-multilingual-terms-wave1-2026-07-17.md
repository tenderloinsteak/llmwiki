---
tags: [query, accountinggo, accounting-edu, i18n]
created: 2026-07-17
updated: 2026-07-17
sources:
  - "raw/accounting-terms-wikipedia-summaries-2026-07-17.json"
  - "raw/accounting-terminology-research-notes-2026-07-17.md"
  - "concepts/accounting-terminology-matrix.md"
---
# Query: AccountingGo 다국어 회계용어 — Wave 1 (2026-07-17)

> 질문: 대충 번역이 아니라 국가별 수험·교재 용어로 매칭표를 llmwiki에 쌓자. 한국·미국뿐 아니라 유럽·일본·중국 등 앱스토어 확장 가능 범위로.

## 결론

1. **기계가독 레지스트리** `concepts/accounting-terminology-registry.json` = **314 entries** (concept 143 + account 171). 요약: [[accounting-terminology-registry-index]].
2. 허브: [[accounting-terminology-matrix]] · 나라 앵커: [[accounting-locale-registry]].
3. en-US·ko는 314칸 채움(ko 전부 `kkj:?`). ja/zh/de/…는 Wikipedia로 확인된 **소수만** — 나머지는 `PENDING`(직역 금지).
4. 「모든 나라 × 모든 용어」는 셀 단위 출처 승격으로 계속 쌓는다.

## 한 일

| 산출물 | 경로 |
|---|---|
| 매칭 허브 | `wiki/concepts/accounting-terminology-matrix.md` |
| 로케일 레지스트리 | `wiki/concepts/accounting-locale-registry.md` |
| raw extracts | `wiki/raw/accounting-terms-wikipedia-summaries-2026-07-17.json` |
| 방법론 노트 | `wiki/raw/accounting-terminology-research-notes-2026-07-17.md` |

### 레퍼런스로 확인된 핵심 (발췌)

- **KO**: 재무상태표 = statement of financial position, 동의어 대차대조표; 차변/대변; 복식부기; 회계등식 (`W`)
- **JA**: 貸借対照表, 借方/貸方, 仕訳, 純資産, 試算表, 総勘定元帳, 売掛金 (`W`)
- **ZH**: 资产负债表/财务状况表, 复式记账, 所有者权益, 利润表 (`W`)
- **DE**: Bilanz, Eigenkapital, Soll und Haben, Doppelte Buchführung (`W`)
- **ES**: balance de situación, patrimonio neto, partida doble (`W`)
- **EN**: Assets = Liabilities + Equity; debit left / credit right (`W` double-entry)

### 의도적 DUAL (뭉개지 않음)

- KO 재무상태표↔대차대조표, 매출채권↔외상매출금
- JA 純資産↔資本
- EN-UK stock/debtors/creditors/turnover/P&L
- IFRS statement of financial position ↔ balance sheet

## 다음 (우선순위)

1. 곽경준: KO 열 검수 → `KKJ✓` (특히 재무상태표 기본값·외상 vs 채권 채무 기본값)
2. 에이전트: 429로 비어 있는 EN/KO/pt extract 재수집; KASB·日商·财政部·PCG·PGC·HGB·CPC 1차 문서 raw 인제스트
3. Wave 2: de/fr/es/pt-BR 계정과목표 기준 계정명 채우기
4. 레포 반영: 검수된 셀만 `assets/content/<locale>/glossary.json`으로 승격

## 🔗 연결

[[accounting-terminology-matrix]] · [[accounting-locale-registry]] · [[accountinggo-i18n]] · [[accountinggo]]
