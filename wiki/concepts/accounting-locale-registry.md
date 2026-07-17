---
tags: [accounting-edu, accountinggo, i18n]
created: 2026-07-17
updated: 2026-07-17
sources:
  - "raw/articles/accounting-terminology-research-notes-2026-07-17.md"
  - "repo: Desktop/dev/AccountingGo/assets/config/locales.json"
---
# 회계 로케일·수험 레지스트리 (Accounting Locale Registry)

> 나라마다 **어떤 시험·기준의 용어를 정본으로 삼을지** 적어 둔 레지스트리. 번역 사전 목록이 아니다.

## 🌱 쉽게

한국이면 세무사·공인회계사·전산세무 교재 말투, 일본이면 일상호기, 중국이면 초급회계사 교재, 독일이면 Bilanzbuchhalter/HGB. 앱스토어에 언어를 열 때마다 「그 나라 수험생이 어색하지 않은 단어」를 고르기 위한 주소록이다.

## ⚙️ 정확히

### AccountingGo locales.json 대비

레포 `assets/config/locales.json` 현재: `en`(complete), `ko/ja/zh/hi`(planned).  
이 레지스트리는 **그보다 넓은 후보 집합**을 미리 고정해, 용어 매트릭스([[accounting-terminology-matrix]])가 앞서 쌓이게 한다.

### 로케일 카드

#### ko — 한국어 / 한국
- **정본 앵커**: K-IFRS·일반기업회계기준(한국회계기준원); 수험 = KICPA·세무사·전산세무회계·대학 회계원리
- **표기 함정**: 재무상태표↔대차대조표; 매출채권↔외상매출금; 매입채무↔외상매입금
- **검수**: 곽경준 도메인 검수 가능 → 모든 ko 셀 `KKJ` 게이트
- **상태**: Wave 1 초안 등록 / `KKJ?`

#### en-US — English (US)
- **정본 앵커**: CPA Exam blueprints 용어; US GAAP 교재(Kieso 등); AICPA
- **앱 역할**: AccountingGo **authoring locale** ([[accountinggo-i18n]])
- **상태**: glossary 12 term SoT 존재

#### en-UK — English (UK / ACCA)
- **정본 앵커**: ACCA FA/FR; FRS; Companies Act 관행
- **표기 함정**: stock, debtors, creditors, turnover, profit and loss account, nominal ledger
- **상태**: 매트릭스 DUAL로 분리 시작; 별 로케일 코드 미도입

#### ja — 日本語 / 日本
- **정본 앵커**: 日商簿記検定(商工会議所); 公認会計士; 企業会計基準
- **표기 함정**: 純資産(재무제표) vs 資本(구·계정); 仕訳(仕分 오용 주의 — W)
- **상태**: Wave 1 핵심 `W` 다수

#### zh-CN — 简体中文 / 中国大陆
- **정본 앵커**: 初级·中级会计职称; 企业会计准则; 注会(CPA China)
- **표기 함정**: 所有者权益↔股东权益; 利润表↔损益表; 六大会计要素(资产·负债·所有者权益·收入·费用·利润)
- **상태**: Wave 1 핵심 `W` 일부

#### zh-TW — 繁體中文 / 台灣
- **정본 앵커**: 會計師; 企業會計準則
- **상태**: Wave 3 (스크립트 분기만으로 zh-CN 복붙 금지)

#### de — Deutsch / Deutschland (+AT/CH 주의)
- **정본 앵커**: Bilanzbuchhalter; Steuerberater; HGB; SKR03/SKR04 Kontenrahmen
- **표기**: Soll/Haben, Bilanz, GuV, Eigenkapital, Aktiva/Passiva
- **상태**: Wave 1 개념어 `W`; 계정 Wave 2

#### fr — Français / France (+BE/CH 주의)
- **정본 앵커**: DCG/DSCG; Plan Comptable Général (PCG)
- **표기**: débit/crédit, bilan, compte de résultat, grand livre
- **상태**: Wave 1 일부; PCG 계정표 Wave 2

#### es — Español / España (+LATAM 분기 예정)
- **정본 앵커**: Plan General Contable (PGC); ROAC
- **표기**: debe/haber, balance de situación, patrimonio neto, partida doble (`W`)
- **상태**: Wave 1 개념; LATAM(MX/AR/CL)은 별 카드로 쪼갤 것

#### pt-BR — Português (Brasil)
- **정본 앵커**: CFC; CPC pronunciamentos
- **표기**: ativo/passivo/patrimônio líquido, débito/crédito, balanço, DRE
- **상태**: Wave 1 후보; Wikipedia 429로 extract 재수집 필요

#### hi — हिन्दी / India
- **정본 앵커**: ICAI CA Foundation — **시험 본문은 영어가 주**인 경우 多
- **전략**: UI 힌디어 글로스 + 학습 본문은 en-IN(영국/인도 교재 용어) 검토
- **상태**: CAND; 무리한 직역 금지

#### it / nl / vi / th / id
- **상태**: Wave 3 예약. 이탈리아 partita doppia, 네덜란드 IFRS-EU, 베트남 VAS, 태국 TFRS, 인도네시아 SAK.

### 추가 프로토콜 (새 나라)

1. 위 카드 한 장 작성 (시험 이름 + 기준서 + 함정)
2. [[accounting-terminology-matrix]]에 컬럼 추가
3. 공식/수험 1차 자료를 `wiki/raw/`에 저장 후 등급 `STD`/`EXAM`로 승격
4. `locales.json` status를 planned→draft→complete

## 🔗 연결

[[accounting-terminology-matrix]] · [[accountinggo-i18n]] · [[accountinggo]] · [[queries/accounting-multilingual-terms-wave1-2026-07-17]]

## 📌 미해결

- pt-BR·en Wikipedia extract 재수집
- 각국 공식 용어집 URL/PDF 목록을 raw에 고정
- es-LATAM / fr-CA / de-CH 분기 정책 결정
