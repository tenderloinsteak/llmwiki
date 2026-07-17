---
tags: [meta, setup]
created: 2026-07-17
updated: 2026-07-17
sources: []
---
# Obsidian Web Clipper 설정 (llmwiki)

> 브라우저 확장 설정에 그대로 복사. vault Templates 플러그인 파일 불필요.

## 한 줄 결론

- **저장 위치:** 보관소 `llmwiki` · 노트 경로 `wiki/raw`
- **프로젝트 체크:** 클리핑 직전에 Clipper 팝업에서 체크 (아래 속성)
- **내 생각:** 필수는 아님. 한 줄 `why`만 적어도 충분. 자세한 건 ingest 때 말로.

## 확장 설정값

| 항목 | 값 |
|---|---|
| 템플릿 이름 | `llmwiki-raw` |
| 템플릿 트리거 | (비움) |
| 보관소 | `llmwiki` |
| 노트 (폴더) | `wiki/raw` |
| 노트 이름 형식 | `{{title}}` |

## 템플릿 속성 (권장)

Clipper UI에서 속성 타입을 맞출 것.

| 속성 이름 | 타입 | 기본값 / 값 | 설명 |
|---|---|---|---|
| clipped | text | `{{date}}` | 클립 시각 |
| source | text | `{{url}}` | 원문 URL |
| site | text | `{{site}}` | 사이트 |
| author | text | `{{author}}` | 저자 |
| mantisalgo | **checkbox** | off | MantisAlgo 관련이면 체크 |
| shifttrade | **checkbox** | off | ShiftTrade 관련이면 체크 |
| accountinggo | **checkbox** | off | AccountingGo 관련이면 체크 |
| wiki-meta | **checkbox** | off | 위키/에이전트/도구 자체 (llmwiki) |
| why | text | (비움) | 선택 — “왜 긁었는지” 한 줄 |

여러 프로젝트에 걸치면 **체크를 여러 개** 하면 됨.

체크박스 UI가 애매하면 대신 하나의 **리스트** 속성:

| 속성 | 타입 | 예 |
|---|---|---|
| projects | list / multi | `mantisalgo`, `shifttrade`, `accountinggo`, `wiki-meta` |

## 노트 내용

```markdown
# {{title}}

> source: {{url}}
> clipped: {{date}}

## 내 메모 (선택)
{{why}}

{{content}}
```

`{{why}}`가 확장에서 안 먹으면, 메모 칸을 비워 두고 클립 직전 본문에 손으로 한 줄 적어도 됨.

## 옵시디언 앱

- 첨부 파일 경로: `wiki/raw/assets` (이미지 쓸 때만)

## 흐름 (Capture ≠ Ingest)

1. 클립 (+ 프로젝트 체크, why는 선택) → `wiki/raw/`
2. “ingest / 소화해줘” → 에이전트가 요점 보여주고 강조점 물음
3. 확정 후 위키 페이지에 `tags`·`sources`·프로젝트 연결 반영

## 기존 llmwiki 페이지는?

- **전용 `projects:` / 체크박스 필드는 없었음.**
- 프로젝트 허브는 `tags: [project, mantisalgo|shifttrade|accountinggo]` + `[[wikilinks]]`로 묶여 있음.
- 개념 페이지는 도메인 태그(`pine-script`, `quant`…) 위주라, “ShiftTrade 전용”처럼 **항상 명시되진 않음.**
- raw 클립은 지금까지 `clippings`만 있고 프로젝트 체크 없음 → **앞으로 템플릿으로 보완.**
