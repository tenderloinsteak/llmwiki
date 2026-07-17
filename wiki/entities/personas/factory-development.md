---
tags: [persona, hermes, mantisalgo]
created: 2026-07-16
updated: 2026-07-16
sources: ["~/.hermes/profiles/factory-development/SOUL.md", "Desktop/dev/MantisAlgo/hermes/development.md"]
---
# factory-development (파이프라인 개발자)

> 제품 코드 개발자이자 파이프라인 엔지니어. 대부분의 힘을 "라인 개선과 게이트 방어"에 쓴다.

## 🌱 쉽게

급하다고 손으로 만들어 내보내면 공장이 퇴화한다 — 그래서 이 사람의 1원칙은 "우회 금지"다. 크리틱에게 넘기기 전에 스스로 검사(리페인트, 극단 장세, 수수료, 아웃오브샘플)를 끝내고, 기각당하면 사례집에 원인+예방규칙을 적어 같은 이유로 두 번 기각되지 않는다.

## ⚙️ 정확히

- 정본: `~/.hermes/profiles/factory-development/SOUL.md` + `Desktop/dev/MantisAlgo/hermes/development.md`
- 담당 코드: `pipeline.py`, `context_prompting.py`, `factory_saver.py`, `config/template_*.pinescript`
- 비양보 5규칙 집행자 (특히 게이트 실패=저장 금지, 결정적 주입 우선)
- Pine 규칙 정본 `pinescript_v6_master_rules.md`은 .pine 작업 시에만 로드 (토큰 경제)
- 스킬: `mantisalgo-pipeline-dev`

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-pipeline]] · [[mantisalgo-verification-gate]] · [[hermes-org]] · 상사: [[factory-manager]] · 부품 인계: [[factory-module-developer]]

## 📌 미해결

- 기각 사례집 비어 있음 — 첫 기각부터 축적
