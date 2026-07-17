---
tags: [hermes, knowledge]
owner: tutor
---

# Tutor 페르소나 — 곽경준 전용 학습 로그 & 커리큘럼

> Character lives in Hermes `~/.hermes/profiles/tutor/SOUL.md` (mirrored at [[souls/tutor]]).
> This file is the **curriculum + learning log** only.

> 목표 지향(2026-07-15 확정): **균형 트랙**
> - 중간 목표: 기본 문법으로 간단한 지표/전략을 스스로 짤 수 있을 것
> - 궁극 목표(지휘자): MantisAlgo 파이프라인이 생성하는 Pine 코드를 읽고·지시하고·검토할 것
> - 원칙: 못 짜면 남의 코드도 못 읽으니 문법과 도메인 양쪽 다. 매 세션 = 1개념 → 미니 예제 → 실제 프로젝트 적용.

---

## 1. 3트랙 커리큘럼

- **A. Pine 문법/구조** — 코드 자체를 다룸 (version, 블록, 변수, 시리즈, 제어문, 함수, 지표/전략 분리)
- **B. 퀀트 기초** — 지표/전략이 무슨 뜻인지 도메인 지식 (OHLCV, 캔들, 타임프레임, 지표 카테고리, 백테스트 지표)
- **C. 통계** — 숫자를 믿을 수 있는지 판단력 (평균/편차, 정규분포, 상관관계, 과적합)

> 3트랙은 따로 가는 게 아니라 **매 세션에서 적절히 섞어서** 감. 비즈니스 필요 순서(문법→도메인→통계)를 따름.

---

## 2. 단계별 로드맵 (Phase 0 → 6)

### Phase 0 — 환경 & 첫 1줄 (≈30분)
- TradingView 파인 에디터 열기, `//@version=6`
- Pine의 5개 기본 블록: `version` / `indicator()`(or `strategy()`) / 변수 / `plot()` / 실행
- 미니 예제: `plot(close)` — 캔들 위에 종가 선 하나 긋기
- **적용:** MantisAlgo `output/` 폴더의 `.pine` 파일을 "그냥 열어보기"만 (겁먹지 말 것)

### Phase 1 — 시리즈(series) 개념 — Pine의 핵심 (가장 중요)
- 왜 Pine는 "배열이 아니라 시리즈"인가 (사탕 비유: 매 봉마다 하나씩 자동 계산)
- `close`, `close[1]`, `close[2]` — 과거 봉 참조
- `var` vs 일반 대입 (누적 변수의 차이)
- 미니 예제: 전일 종가 대비 변화량 `close - close[1]`
- **B트랙 연결:** OHLCV, 캔들, 타임프레임

### Phase 2 — 기본 지표 직접 만들기 (도메인 입문)
- 이동평균 SMA/EMA 수식 이해 + 직접 코딩
- RSI 개념(모멘텀) + 간단 버전 코딩
- 미니 예제: SMA(20)과 가격 크로스 표시
- **B트랙:** 추세/모멘텀/볼륨/변동성 지표 카테고리
- **적용:** ShiftTrade의 `TradingViewWidget`이 띄우는 지표가 실제로 뭔지 연결
- **C트랙 연결:** 평균이 뜻하는 것, 단순이동평균의 가중치 직관

### Phase 3 — 제어문 & 함수 (구조화)
- `if` / `for` (Pine에선 제한 있음 — 왜? 시리즈 때문)
- 사용자 함수 정의, 라이브러리 `@library`
- 미니 예제: 조건에 따라 색깔 바꾸는 `plot`

### Phase 4 — 지표 vs 전략 (MantisAlgo 핵심 분리)
- `indicator()` vs `strategy()` 차이 (MantisAlgo non-negotiable #2)
- `strategy.entry` / `strategy.close` / `strategy.exit` (익절/손절)
- 백테스트 결과 읽기: 승률, Profit Factor, MDD
- 미니 예제: SMA 크로스 전략 백테스트
- **적용:** `pinescript_factory/` 안 `.pine`를 "전략/지표"로 분류해 보기

### Phase 5 — 실전 오픈소스 리딩 (지휘자 훈련 시작)
- Monte Carlo Engine 참고 스크립트 같은 실제 코드 읽기
- 전체 구조 파악: 어디가 설정 / 계산 / 그리기인지
- "왜 이 상수를 썼을까" 물어보기 연습
- **C트랙 연결:** 과적합(overfitting)이 뭔지, 샘플 수의 중요성

### Phase 6 — MantisAlgo 파이프라인 검토 (지휘자 완성)
- `main.py` → `pipeline.py` 흐름 훑기 (코드 짜지 않고 흐름만)
- 생성된 `.pine`를 5-part anatomy로 검토
- 요구사항을 정확히 지시하는 연습 (프롬프트 짜기)
- **C트랙:** 생성 결과의 통계적 타당성 점검

---

## 2.1 함수 레벨 세부 체크리스트 (공식 레퍼런스 기반)
- `Desktop/pinestudy/pine_v6_checklist.md` — **공식 레퍼런스 실제 추출**(추측 없음).
- 2026-07-15 브라우저 DOM 파싱으로 식별자 **총 952개** 추출:
  - 타입 20 · 빌트인 변수 193 · 콘스탄트 216 · **함수 479** · 키워드 14 · 오퍼레이터 20 · 어노테이션 10
  - 함수는 네임스페이스별 그룹(ta 59, strategy 49, array 55, matrix 49, box 29, label 21, line 22, table 22, math 24, input 14, map 11, request 11, str 18, color 7, chart 5, linefill 5, polyline 2, footprint 9, volume_row 8, ticker 9, timeframe 3, syminfo 2, runtime 1, top 41)
- 함수 하나씩 `[ ]` → `[x]` 체크. 🔴 매일/필수(핵심 ~30개) · ⚪ 그 외 상황별.
- 출처: https://kr.tradingview.com/pine-script-reference/v6/ (v6 한국어판). 추후 버전업 시 재추출 필요.

## 2.2 학습 방식 원칙 (골격 vs 살)
- **골격(Phase 0→6, §2)**: 제가 잡은 나침반. 가볍게 훑기만. 무조건 순서대로 갈 필요 없음.
- **살(세부)**: **실전 코드를 주시거나, 제가 던진 코드를 같이 뜯어보며** 하나하나 위키 문서(`Desktop/pinestudy/wiki/`)로 익힘.
- 즉 "커리큘럼 = 골격 나침반, 위키 = 실전에서 채워지는 살". 남의 코드(특히 외부 참고 스크립트 등)를 뜯다 보면 자연히 필요한 걸 먼저 배움.
- 매 학습: 함수/개념 1개 → `wiki/` 문서(용어해부+분류뜻+비유+인자+미니예제) → **"이해했다" 말씀 후에만** 체크리스트 `[x]` + `update_progress.py`.
- 배경 지식은 `concepts/`(분류기초/통계) · `glossary.md`(도메인용어)에서 병행.

## 3. 학습 로그 (매 세션 뒤 업데이트)

| 날짜 | Phase | 한 일 | 이해도(1-5) | 다음 단계 |
|------|-------|-------|-------------|-----------|
|      |       |       |             |           |

---

## 4. 참고 — 기존 학습 자산
- `Desktop/pinestudy/pine_v6_checklist.md` — 952개 식별자 체크리스트 (§2.1)
- `Desktop/pinestudy/wiki/` — 식별자별 위키 문서 (템플릿 `wiki/_template.md`)
- `Desktop/pinestudy/concepts/` — 분류 기초(`00_classifications.md`) · 통계(`statistics.md`)
- `Desktop/pinestudy/glossary.md` — 도메인 용어집 / `progress.md` — 대시보드 (`update_progress.py`로 재생성)
- `Desktop/pinestudy/idea.md` — 학습 시스템 기획 / `Pine_Script_Master.md` — 세부 진도표
- `../MantisAlgo/` — 실전 파이프라인 (검토 대상) / `../ShiftTrade/` — TradingView 위젯 연결 대상
- (구 스캐폴드) [[study/pinescript-roadmap]] Stage 0~9 · [[study/note-template]] · [[study/notes/index]] — Phase 로드맵으로 대체됨, 참고용
