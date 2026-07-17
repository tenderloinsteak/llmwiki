---
tags: [accounting-edu, accountinggo, i18n]
created: 2026-07-17
updated: 2026-07-17
sources:
  - "raw/accounting-terms-wikipedia-summaries-2026-07-17.json"
  - "raw/accounting-terminology-research-notes-2026-07-17.md"
  - "repo: Desktop/dev/AccountingGo/assets/content/en/glossary.json"
  - "repo: Desktop/dev/AccountingGo/docs/I18N.md"
---
# 회계 용어 다국어 매트릭스 (Accounting Terminology Matrix)

> AccountingGo 표시용 용어의 **국가·수험 관행 매칭 허브**. 사전식 대충 번역 금지. **수백 개 본체는 JSON 레지스트리**.

## 🌱 쉽게

앱은 영어로 문제를 먼저 쓰고([[accountinggo-i18n]]), 각 나라 화면에는 그 나라 **수험·교재에서 실제로 쓰는 말**을 붙인다. 표만으로는 계정과목까지 수백 개가 안 돌아가서, 실제 장부는 [[accounting-terminology-registry-index]] / `accounting-terminology-registry.json`(314 entries)이다. 이 페이지는 규칙·함정·샘플만 둔다.

## ⚙️ 정확히

### 정본 위치 (2026-07-17)

| 층 | 경로 | 내용 |
|---|---|---|
| 기계가독 SoT | `wiki/concepts/accounting-terminology-registry.json` | **314** = concept 143 + account 171 |
| 사람용 요약 | [[accounting-terminology-registry-index]] | 채움 통계·KO 검수 플래그 |
| 나라 앵커 | [[accounting-locale-registry]] | 수험·기준서 주소록 |
| 앱 SoT | `AccountingGo/assets/content/en/{glossary,accounts}.json` | authoring; ko 미러 있음 |

ko는 314칸 초안 완료(`kkj:?`). ja/zh/de/…는 **출처 확인된 소수만** 채움 — 나머지는 `PENDING`(직역 채우기 금지).

### 운영 규칙

| 규칙 | 내용 |
|---|---|
| Authoring SoT | 영어 termId (`glossary.json` / accounts) — 불변 |
| Display SoT | 이 매트릭스 → 이후 `assets/content/<locale>/glossary.json` 등으로 반영 |
| KO 게이트 | 한국어 셀은 곽경준 검수 후 `KKJ✓` |
| 금지 | 딕셔너리 직역만으로 셀 채우기; 출처 없는 `CAND`를 App Store 출시 로케일에 사용 |
| 상충 | 덮어쓰지 말고 `> ⚠️ 상충:` + DUAL 표기 |

### 출처 등급

- `W` — 이번 세션 Wikipedia extract (raw JSON에 저장)
- `STD` — 국가 GAAP / IFRS 채택 기준 문구 (PDF 인용 업그레이드 대상)
- `EXAM` — 수험 교재·검정 관행 (판본 인용 필요)
- `CAND` — 후보, 1차 출처 미확인
- `DUAL` — 병용 용어 (앱 기본값 + 병기)
- `KKJ✓` / `KKJ?` — 한국어 인간 검수 완료 / 대기

### 로케일 범위 (App Store 확장 우선)

허브 상세: [[accounting-locale-registry]]

Wave 1 표 컬럼: **en-US · en-UK · ko · ja · zh-CN · de · fr · es · pt-BR · hi**  
(후속 Wave: zh-TW · it · nl · vi · th · id)

---

### A. 샘플 — 개념 용어 (전체는 JSON 143개)

> 아래는 허브용 발췌. **전체·계정과목 포함은 레지스트리 JSON**을 연다.

| termId | en-US | en-UK | ko | ja | zh-CN | de | fr | es | pt-BR | hi | status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| accounting | Accounting | Accounting | 회계 | 会計 / 簿記※ | 会计 | Rechnungswesen / Buchführung※ | comptabilité | contabilidad | contabilidade | लेखांकन (lekhankan) | EXAM/CAND; ※JA·DE는 문맥 분기 |
| accounting_equation | Accounting equation | Accounting equation | 회계등식 | 会計等式 | 会计等式 / 会计恒等式 | Bilanzgleichung | équation comptable | ecuación contable | equação patrimonial | लेखांकन समीकरण | KO:`W` 회계등식; 타:`EXAM/CAND` |
| assets | Assets | Assets | 자산 | 資産 | 资产 | Vermögenswerte / Aktiva `DUAL` | actif | activo | ativo | संपत्ति / परिसंपत्ति | EXAM; DE `W` Bilanz 맥락 |
| liabilities | Liabilities | Liabilities | 부채 | 負債 | 负债 | Schulden / Verbindlichkeiten / Passiva `DUAL` | passif | pasivo | passivo | देयताएँ / दायित्व | EXAM |
| equity | Equity / Stockholders' equity | Equity / Shareholders' equity | 자본 | 純資産 `DUAL` (구: 資本) | 所有者权益 `DUAL` (股东权益) | Eigenkapital | capitaux propres | patrimonio neto | patrimônio líquido | इक्विटी / स्वामित्व | JA `W` 純資産; ZH `W` 所有者权益; DE `W` Eigenkapital; ES `W` patrimonio neto |
| double_entry | Double-entry bookkeeping | Double-entry bookkeeping | 복식부기 | 複式簿記 | 复式记账 / 复式簿记 | Doppelte Buchführung | partie double | partida doble | partidas dobradas | दोहरी प्रविष्टि लेखांकन | EN·KO·JA·ZH·ES `W` |
| debits_credits | Debits and credits | Debits and credits | 차변·대변 | 借方·貸方 | 借方·贷方 | Soll und Haben | débit et crédit | debe y haber | débito e crédito | डेबिट और क्रेडिट | KO `W` 대변차변; JA `W`; DE `W` |
| journal_entry | Journal entry | Journal entry / Journal | 분개 | 仕訳 | 会计分录 | Buchungssatz / Journalbuchung | écriture comptable | asiento contable | lançamento contábil | रोजनामचा प्रविष्टि | JA `W` 仕訳; KO `EXAM`/`KKJ?` |
| revenue | Revenue | Revenue / Turnover `DUAL` | 수익 | 収益 | 收入 | Erträge / Umsatzerlöse※ | produits / chiffre d'affaires※ | ingresos | receita | राजस्व | UK turnover `DUAL`; ※문맥 |
| expenses | Expenses | Expenses | 비용 | 費用 | 费用 | Aufwendungen | charges | gastos | despesa | व्यय | EXAM |
| balance_sheet | Balance sheet | Balance sheet / Statement of financial position | 재무상태표 `DUAL` 대차대조표 | 貸借対照表 | 资产负债表 `DUAL` 财务状况表 | Bilanz | bilan | balance de situación / balance general | balanço patrimonial | तुलन पत्र | KO·JA·ZH·DE·ES `W`; IFRS명 DUAL |
| net_income | Net income | Profit for the period / Net profit `DUAL` | 당기순이익 | 当期純利益 | 净利润 | Periodenergebnis / Jahresüberschuss※ | résultat net | resultado neto | lucro líquido | शुद्ध लाभ | EXAM |

※ 표의 `EXAM/CAND` 셀은 **다음 세션에서 판본·기준서 페이지를 raw에 붙이며 `STD`/`EXAM`로 승격**한다. 한국어는 곽경준 검수 전 `KKJ?`.

---

### B. 재무제표·장부 프로세스 (커리큘럼 확장 Wave 1)

| termId | en-US | en-UK | ko | ja | zh-CN | de | fr | es | pt-BR | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| income_statement | Income statement | Profit and loss account `DUAL` | 손익계산서 | 損益計算書 | 利润表 `DUAL` 损益表 | Gewinn- und Verlustrechnung (GuV) | compte de résultat | cuenta de pérdidas y ganancias | demonstração do resultado (DRE) | JA·ZH·FR `W`/partial |
| trial_balance | Trial balance | Trial balance | 시산표 | 試算表 | 试算平衡表 / 试算表 | Rohbilanz / Saldenbilanz | balance de vérification | balance de comprobación | balancete de verificação | JA `W` 試算表 |
| general_ledger | General ledger | Nominal ledger `DUAL` | 총계정원장 | 総勘定元帳 | 总账 / 总分类账 | Hauptbuch | grand livre | libro mayor | razão geral | JA `W`; UK nominal ledger |
| t_account | T-account | T-account | T계정 | T勘定 | T型账户 | T-Konto | compte en T | cuenta T | conta T | EXAM |
| posting | Posting | Posting | 전기 | 転記 | 过账 | Übertragungung | report | pase | lançamento no razão | EXAM |
| chart_of_accounts | Chart of accounts | Chart of accounts | 계정과목일람 / 계정체계 | 勘定科目一覧 | 会计科目表 | Kontenrahmen / Kontenplan | plan comptable | plan de cuentas | plano de contas | FR→PCG; DE→SKR |
| financial_statements | Financial statements | Financial statements | 재무제표 | 財務諸表 | 财务报表 | Abschluss / Finanzberichte | états financiers | estados financieros | demonstrações financeiras | EXAM |

---

### C. 계정과목 — 레지스트리에 171개

- 앱 편입 43개: `assets/content/*/accounts.json`과 동기
- 확장 128개: 수험 COA 골격(토지·상품·부가세·매입·인출금·충당부채 등). en-US+ko 채움, 타 언어 `PENDING`
- 검수 플래그·통계: [[accounting-terminology-registry-index]]

유럽·일본·중국 계정명은 각국 **표준계정과목표 / 수험 勘定科目**을 raw에 넣은 뒤 셀 단위로 승격한다.

---

### D. 앱 기본값 제안 (검수 전)

한국어 표시 기본안 (곽경준 `KKJ?` 대기):

1. 재무제표명: **재무상태표** (K-IFRS/기준서) — 이론 레슨에서 「대차대조표=동의어」 1회 명시
2. 채권·채무: **매출채권 / 매입채무** — 초급 부기 레슨에서 외상매출금·외상매입금 병기
3. 자본 요소: **자본** (equity) / **자본금** (capital stock)
4. 성과: **수익·비용·당기순이익** / 표 이름 **손익계산서**

영어 표시: authoring = **en-US**. en-UK는 별 로케일 또는 glossary variant로 `stock/debtors/creditors/turnover/P&L` 전환.

## 🔗 연결

[[accounting-locale-registry]] · [[accountinggo-i18n]] · [[accountinggo]] · [[double-entry-bookkeeping]] · [[queries/accounting-multilingual-terms-wave1-2026-07-17]] · 담당 [[quiz-writer]]

## 📌 미해결

1. 곽경준: 레지스트리 ko 314칸 검수 → `kkj: ✓` (우선 supplies/equipment/채권채무/재무상태표)
2. ja 171 accounts — 日商簿記 勘定科目으로 채우기
3. zh-CN — 初级会计 会计科目表
4. de/fr/es/pt-BR — SKR/PCG/PGC/CPC
5. en-UK synonym pass
6. 1차 출처 PDF raw 인제스트 + cite 필드
7. expanded 128 → 앱 `accounts.json` 편입 여부
8. Wave 3 로케일: zh-TW · it · nl · vi · th · id
