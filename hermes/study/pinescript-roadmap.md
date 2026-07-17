# 파인스크립트 학습 로드맵 (Pine Script Roadmap)

> 튜터(tutor)가 관리. 곽경준님은 프로그래밍 입문자 — 모든 설명은 **"왜?" 중심**, 초등학생 비유 OK.
> 최종 목표: 파인스크립트를 배워 **MantisAlgo 공장(파인스크립트 생성 파이프라인)을 읽고, AI에게 지시할 수준**까지.

## 3트랙 개요
- **Track A — 파인스크립트 (척추)**: 지금 이 로드맵. 무조건 먼저.
- **Track B — 퀀트 기초 (병렬/선택)**: 캔들·OHLC, 타임프레임, 수수료·스프레드, 백테스트 함정.
- **Track C — 통계 (병렬/선택)**: 평균·분산·표준편차, 상관, 분포, 과적합.
- B·C는 A의 Stage 3~4를 넘어가면 자연스럽게 끼워 배웁니다. 따로 시간 잡지 말고 **"필요할 때"** 튜터에게 요청하세요.

## Track A 단계별 (순서가 중요)
각 스테이지 = **목표 / 핵심개념 / 직관비유 / 실습 / MantisAlgo 연결 / 통과기준**.
노트는 `[[study/note-template]]` 복사해서 `study/notes/` 에 한 장씩.

### Stage 0 — 환경 & 가장 큰 오해
- **목표**: TradingView Pine Editor 켜고 첫 빈 스크립트 돌리기. "인디케이터 ≠ 스트래티지" 감만 잡기.
- **핵심**: Pine의 가장 중요한 사고방식 — "코드는 위→아래 한 번 읽는 게 아니다. **매 봉(bar)마다 스크립트 전체가 다시 실행된다**."
- **비유**: 편의점 계산대. 영수증 프로그램은 손님(봉)이 들어올 때마다 처음부터 다시 돌림. 어제 손님 기록은 `close[1]` 로 꺼내 봄.
- **실습**: Pine Editor 열고 `//@version=6` 빈 인디케이터 저장 → 차트에 추가.
- **MantisAlgo**: `AGENTS.md` non-negotiable #2 "Indicator ≠ Strategy" 가 왜 있는지 감 잡기.
- **통과**: "왜 변수에 어제 값이 이미 들어있는지" 입으로 설명 가능.

### Stage 1 — 가장 작은 문법: 변수·타입·대입
- **목표**: `=` 와 `:=` 차이, 기본 타입 7개.
- **핵심**:
  - `=` : 처음 만들 때(한 번). `:=` : 이미 만든 걸 매 봉 갱신할 때.
  - 타입: int, float, bool, string, color, line, label.
- **비유**: `=` = "이름표 붙이기(최초 1회)". `:=` = "맞은 물건 갈아치우기(매일)".
- **실습**: `a = 1` 과 `a := a + 1` 차이 관찰(한쪽은 고정, 한쪽은 누적).
- **MantisAlgo**: 검증 게이트 규칙 #5 "신호 변수 `= false` 로 선언, AI존 안에서 `:=` 로 켜기, 이후 절대 리셋 안 함" — 이 규칙이 왜 있는지 지금 이해.
- **통과**: "왜 신호를 `= false` 로 시작해야 하는지" 설명.

### Stage 2 — 시리즈와 과거 참조 (시간 다루기)
- **목표**: `close[1]`, `close[2]`, `[]` 인덱싱, series 직관.
- **핵심**: Pine 변수는 "과거 값도 다 기억하는 줄"(series). `[n]` = n봉 전.
- **비유**: 사진 앨범. `close` = 맨 앞 사진(지금), `close[1]` = 바로 전 사진.
- **실습**: `prevClose = close[1]`, `isUp = close > prevClose` 플롯.
- **함정**: 0으로 나누기 → `math.max(denom, 1e-10)` 가드 패턴(MantisAlgo 표준).
- **통과**: "어제 종가 vs 오늘 종가 비교" 코드 손으로 쓸 수 있음.

### Stage 3 — 이동평균 가족 (내장 함수 직관)
- **목표**: `ta.sma` / `ta.ema` / `ta.wma` / `ta.rma` 차이와 "왜 가중치가 다른지".
- **비유**: 급식 줄 서기. SMA=다 똑같이, EMA=최근 애가 앞(가중), WMA=거리순, RMA=부드럽게.
- **실습**: 4개 다 그려서 곡선 모양 비교.
- **MantisAlgo**: 모듈 레지스트리에 평균 관련 모듈 많음 — 나중에 어떤 걸 쓰는지 매핑.
- **통과**: "최근 추세에 민감한 건 어떤 평균?" 대답 가능.

### Stage 4 — 조건과 신호 (bool의 세계)
- **목표**: 비교·`and`/`or`, `ta.crossover`, 신호 변수 패턴.
- **실습**: 골든크로스 = `ta.crossover(fast, slow)`.
- **패턴**: `bool buy = false` → 크로스 안에서 `buy := true`.
- **리페인팅 직관**: `barstate.isconfirmed` (실시간 봉은 계속 바뀜, 확정 봉은 굳음).
- **MantisAlgo**: 검증 게이트 "signals on confirmed bars" = 이거.
- **통과**: 골든크로스 화살표 그리기.

### Stage 5 — 그리기 (plot / shape / bgcolor)
- **목표**: `plot`, `plotshape`, `bgcolor`, `plotchar`.
- **실습**: Stage 4 신호를 `plotshape` 로 화살표 찍기.
- **통과**: 신호가 차트에 보임.

### Stage 6 — 입력과 파라미터 (`input.*`)
- **목표**: `input.int/float/bool/string`, 왜 파라미터화하나.
- **비유**: 세탁기 버튼. 코드 안 바꾸고 설정만으로 동작 바꿈.
- **MantisAlgo**: 템플릿의 Inputs 파트 = 이거.
- **통과**: 길이를 input으로 받는 평균 인디케이터.

### Stage 7 — 인디케이터 vs 스트래티지 실전
- **목표**: `strategy()` 진입/청산, ATR SL/TP, 백테스트 읽기.
- **핵심**: `strategy.entry / close / exit`, `strategy.position_size`.
- **ATR**: `ta.atr(14)` 로 변동성 재서 SL/TP 거리 잡기(MantisAlgo 표준).
- **실습**: 골든크로스 진입 + ATR 청산 백테스트.
- **통과**: "인디케이터는 알림, 스트래티지는 자동매매" 설명.

### Stage 8 — 모듈화 & v6 문법
- **목표**: `//@version=6`, 함수 `f_x() =>`, 라이브러리 `import`, short-circuit eval, 음수 인덱싱.
- **MantisAlgo**: `pinescript_v6_master_rules.md` 읽기. 모듈 163개 구조 훑기.
- **통과**: 함수 하나 만들어 재사용.

### Stage 9 — MantisAlgo 공장 지도 읽기
- **목표**: 파이프라인·템플릿·아이디어 레지스트리 이해, 오픈소스 해체.
- **실습**: Monte Carlo Engine 참고 스크립트 같은 걸 읽고 "5-Part Anatomy(Inputs→Filter→Logic→Execution→Risk)가 어디인가" 찾기.
- **통과**: "다음 아이디어는 이 모듈 재활용해서 만들면 된다" 제안 가능.

## 노트 쌓는 법
1. 개념 하나 = `study/notes/` 에 노트 한 장 (`[[study/note-template]]` 복사).
2. 세션 끝마다 `[[study/learning-log]]` 에 한 줄.
3. 이해 확인 = **"적용 과제" 풀기** (설명 회상은 인정 안 함).

## 관련
- [[study/learning-log]] · [[study/note-template]] · [[study/notes/index]] · [[personas/tutor]]
