# Accounting terminology multilingual research notes (2026-07-17)

Session capture for AccountingGo i18n terminology registry.
Companion machine extracts: `accounting-terms-wikipedia-summaries-2026-07-17.json`

## Method (mandatory)

1. Prefer **exam / standards terminology** over dictionary translation.
2. Every locale cell must carry a **status**:
   - `W` = Wikipedia extract saved this session
   - `STD` = national GAAP / IFRS local adoption wording (needs PDF cite upgrade)
   - `EXAM` = national exam textbook convention (needs edition cite)
   - `CAND` = candidate pending primary cite / human review
   - `DUAL` = two accepted terms coexist (document both; pick app default)
3. Korean cells: 곽경준 final review gate (`KKJ`).
4. English authoring locale remains AccountingGo SoT (`docs/I18N.md`); this registry is the **display-term** map.

## Locale → primary exam / standards anchors

| Locale | Country/region | Exam / standard anchors |
|---|---|---|
| ko | Korea | 한국공인회계사(KICPA), 세무사, 전산세무회계; K-IFRS / 일반기업회계기준 (한국회계기준원) |
| en-US | United States | CPA Exam (AICPA/NASBA); US GAAP textbooks (e.g. Kieso Intermediate Accounting) |
| en-UK | United Kingdom | ACCA FA/FR; UK Companies Act / FRS; (legacy: stock/debtors/creditors/turnover) |
| ja | Japan | 日商簿記検定 (商工会議所); 公認会計士; 企業会計基準 |
| zh-CN | China (Simplified) | 初级/中级会计职称; 中国企业会计准则; CPA China |
| zh-TW | Taiwan | 會計師; 企業會計準則 (traditional script) |
| de | Germany | Bilanzbuchhalter; Steuerberater; HGB Kontenrahmen |
| fr | France | DCG/DSCG; Plan Comptable Général (PCG) |
| es | Spain | Plan General Contable (PGC); ROAC |
| pt-BR | Brazil | CFC; CPC (Comitê de Pronunciamentos Contábeis) |
| hi | India | CA Foundation (ICAI) — exam language often English; Hindi glosses for UI |
| it | Italy | partita doppia; OIC / commercialista track |
| nl | Netherlands | MBA/AA tracks; Dutch GAAP / IFRS-EU |
| vi | Vietnam | kế toán viên / VAS |
| th | Thailand | FAP / TFRS |
| id | Indonesia | IAI / SAK |

## Dual-term traps (do not collapse)

- KO: 재무상태표 (K-IFRS) ↔ 대차대조표 (부기/수험 전통)
- KO: 매출채권 ↔ 외상매출금; 매입채무 ↔ 외상매입금
- JA: 純資産 (FS) ↔ 資本 (older textbook / capital account)
- ZH: 所有者权益 ↔ 股东权益; 利润表 ↔ 损益表
- EN-UK vs EN-US: inventory/stock; receivables/debtors; payables/creditors; revenue/turnover; income statement / P&L account
- DE: Vermögenswerte/Aktiva; Schulden/Verbindlichkeiten/Passiva; Eigenkapital
- IFRS: statement of financial position preferred over balance sheet in standards text

## Sources fetched this session

- Wikipedia REST summaries JSON (multi-lang)
- en.wikipedia Double-entry bookkeeping (WebFetch)
- ko.wikipedia 재무상태표 / 복식부기 / 대변차변 / 회계등식
- ja.wikipedia 貸借対照表 / 複式簿記 / 借方 / 貸方 / 仕訳 / 純資産 / 試算表 / 総勘定元帳 / 売掛金
- zh.wikipedia 资产负债表 / 复式记账 / 所有者权益 / 利润表
- de.wikipedia Bilanz / Eigenkapital / Doppelte Buchführung / Soll und Haben
- es.wikipedia Balance de situación / Patrimonio neto / Partida doble
- fr.wikipedia Compte de résultat (Bilan summary empty on fetch)

## Explicit non-claims

- This file is **not** a complete chart of accounts for every country.
- Cells marked EXAM/CAND must be upgraded with edition-level cites before shipping that locale in App Store.
