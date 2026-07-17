---
tags: [concept, pine-script, mantisalgo]
created: 2026-07-18
updated: 2026-07-18
sources: ["~/.gemini/config/skills/pine_analyst_toolkit/SKILL.md"]
---
# Pine Script 해체 분석 프레임워크 (Pine Script Analysis Framework)
> 외부 Pine Script (v5/v6) 소스코드를 구조적, 수학적, 시각적으로 분석하여 MantisAlgo 모듈 후보를 도출하는 정본 분석 골격

## 🌱 쉽게
복잡한 외부 코드를 레고 블록 단위로 쪼개어 분석하는 설계 도면입니다. 이 코드가 수학적으로 어떤 공식을 쓰는지, 상태 머신이 있는지, 화면에 그림은 어떻게 그리는지 확인하여 MantisAlgo의 부품 상자에 넣을 새 부품(모듈)을 발굴합니다.

## ⚙️ 정확히

### 1. 분석 산출물 규격 (JSON Schema)
분석 시에는 항상 `example_analysis_REF-XXX.json` 파일에 아래 규격을 적용하여 작성합니다.

```json
{
  "schema_version": 1,
  "example_id": "REF-XXX",
  "source_label": "지표의 공식 명칭",
  "analyzed_at": "YYYY-MM-DDTHH:MM:SSZ",
  "script_type": "indicator | strategy",
  "architecture_hint": "signal-momentum-oscillator | quant-distribution-profile | price-structure-breaks | etc",
  "tier_estimate": "premium | basic",
  "repaint_policy_inferred": "bar_close | repaint | recalculate",
  "static_scan": {
    "line_count": 0,
    "inputs": 0,
    "alertconditions": 0,
    "strategy_entries": 0,
    "strategy_exits": 0,
    "table_new": 0,
    "line_new": 0,
    "label_new": 0,
    "box_new": 0,
    "polyline_new": 0,
    "security_calls": 0,
    "has_udt_method": false,
    "has_var_fsm": false,
    "section_headers": false,
    "ta_functions": []
  },
  "structural_blocks": [
    {
      "role": "블록의 역할 (예: online_1d_kmeans_clustering_engine)",
      "registry_match": "가장 인접한 기존 모듈 ID",
      "match_confidence": 0.00,
      "evidence": ["블록 판정 근거 코드 캡처 또는 설명"],
      "line_span_estimate": [시작라인, 끝라인]
    }
  ],
  "confirmed_existing_modules": ["매칭된 기존 모듈 ID 목록"],
  "candidate_modules": [
    {
      "proposed_id": "신규 모듈 ID 제안",
      "kind": "ui | logic | infra",
      "family": "sig | vol | liq | struct | qx | ui | exec | infra",
      "verdict": "novel",
      "best_match": "유사도가 높은 기존 모듈 ID",
      "similarity": 0.00,
      "recommendation": "핵심 알고리즘 요약 설명",
      "profile": {
        "when_to_use": ["해당 모듈을 채택해야 하는 구체적 조건/시장 상황"],
        "strengths": ["알고리즘적, 연산적 강점"],
        "weaknesses": ["성능 오버헤드 또는 한계점"],
        "complements": ["보완적인 타 모듈 ID"],
        "conflicts_with": ["충돌하거나 중복되는 모듈 ID"],
        "anti_patterns": ["이 모듈을 사용 시 피해야 하는 설계 형태"]
      },
      "match_confidence": 0.85,
      "status_recommendation": "planned"
    }
  ],
  "pipeline_gaps": ["지표 내에 보완되어야 할 문제점 (예: 렉 유발 가드 누락, alert 연동 결여)"],
  "do_not_copy": ["블록 구현 과정에서 직접 카피하면 안 되는 지표 고유의 하드코딩 수식"],
  "architecture_notes": {
    "profile_tier": "T1 (가벼움) | T2 (중간) | T3 (고부하)",
    "strengths": ["구조적 장점"],
    "weaknesses": ["버그 유발점 또는 자원 낭비점"],
    "beyond_examples": ["고도화를 위한 추가 설계 가드 제안"]
  },
  "summary_ko": "한국어로 간결하게 요약한 지표 해체 설명 (3줄 내외)",
  "needs_human_review": false,
  "review_reasons": []
}
```

### 2. 블록 분석 가이드 (Decomposition Checklist)
- **Mathematical Logic (양적 계산)**: 1차원 K-Means, Silverman 커널밀도(KDE), SSA eigenvalues decomposition, Catmull-Rom spline interpolation, IRLS quantile spline regression 등 기하/통계 수식 분석.
- **State Machine (FSM)**: `var` 또는 `varip`로 선언된 상태 변수가 상태 전이(regime, confirmation level)를 제어하는지 분석.
- **Visual Director (시각화)**: `polyline.new`, `box.new`, `table` 등 시각 개체 생성 및 동적 표현 분석.
- **Garbage Collection (GC)**: `box.delete()`, `line.delete()` 및 Array Shift/Pop 소거 루프 작동 분석.

### 3. 실행 파이프라인 규정
1. **정적 스캔(Static Scan)**: 내장 함수 및 객체 생성 개수 파악.
2. **구조적 블록(Structural Blocks)**: 라인 분할 및 `wiki/modules/modules-map.md`(174개 모듈 맵) 기준 유사도 비교.
3. **신규 후보(Candidate) 정의**: 1급 `kind` 분류(ui/logic/infra)를 매핑하여 `planned` 상태 부여.
4. **리페인팅(Repainting) 정책**: 
   - **인디케이터(Indicator)**: 비주얼 및 지표 성과 우선으로 리페인팅 허용.
   - **전략(Strategy)**: 백테스트 정합성 확보를 위해 리페인팅 절대 금지.

## 🔗 연결

[[pine-script]] · [[mantisalgo-module-registry]] · [[5-part-anatomy]] · [[repainting]]

## 📌 미해결
- 174개 모듈 맵과 비교하는 자동화 유사도 계산기 개발 여부
