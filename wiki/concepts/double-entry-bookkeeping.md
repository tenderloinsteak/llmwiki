---
tags: [concept, accounting-edu]
created: 2026-07-16
updated: 2026-07-16
sources: ["Desktop/dev/AccountingGo/hermes/quiz-writer.md", "Desktop/dev/AccountingGo/hermes/learning-ux-designer.md"]
---
# 복식부기 (Double-Entry Bookkeeping)

> 모든 거래를 두 쪽(차변/대변)에 동시에 기록하는 회계의 대원칙. AccountingGo가 가르치는 내용의 심장.

## 🌱 쉽게

저울 비유(AccountingGo 공식 메타포): 거래 하나 = 저울 양쪽에 똑같은 무게의 추를 하나씩 올리는 것. 현금 100만원으로 기계를 사면, 왼쪽(차변)에 "기계 +100"과 오른쪽(대변)에 "현금 −100"이 동시에 실려 저울은 항상 수평이다. 이 "항상 수평"(대차평형)이 강력한 이유: 한쪽만 기록하는 실수를 구조적으로 잡아낸다. 회계 문제의 정답 검산법이 "분개가 저울처럼 맞는가"인 이유다.

## ⚙️ 정확히

- 핵심 등식: 자산 = 부채 + 자본 (모든 분개 후에도 성립)
- 분개(journal entry): 거래를 차변(debit)/대변(credit) 계정과 금액으로 기록 — 차변 합 = 대변 합
- AccountingGo 적용: 문제 자가검증 기준("분개는 반드시 균형"), 애니메이션 메타포(저울+추), 계정 정본 `accounts.json`, 용어 정본 `glossary.json`
- 범위: 회계원리(principles) 수준까지만 — 중급 이상 배제 (quiz-writer 표준)

## 🔗 연결

[[accountinggo]] · [[accountinggo-content-pipeline]] · 담당: [[quiz-writer]] [[learning-ux-designer]]

## 📌 미해결

- 개념 페이지 확장 후보: 계정과목 분류, 재무제표 3종 — 문제 뱅크 확장에 맞춰 추가
