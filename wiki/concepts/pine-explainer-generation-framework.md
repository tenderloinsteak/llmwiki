---
tags: [concept, pine-script, tutor]
created: 2026-07-18
updated: 2026-07-18
sources: ["~/.gemini/config/skills/pine_explainer_generator/SKILL.md"]
---
# Pine 한 줄 해설서 생성 프레임워크 (Pine Explainer Generation Framework)
> Pine Script (v5/v6) 소스코드를 초보자가 쉽게 이해할 수 있도록 구조화된 다크모드 HTML 해설서로 자동 생성하는 정본 지침 및 템플릿

## 🌱 쉽게
코드를 모르는 비전공자나 초보자도 "이 코드가 왜 여기에 있고 차트에서 어떻게 움직이는지" 직관적으로 알 수 있게 해주는 한 줄 해설서 표준 템플릿입니다. Mantis Algo 시그니처 색상을 기본으로 사용하며, 5부 구조와 매수/매도 흐름을 보여줍니다.

## ⚙️ 정확히

### 1. HTML 문서 구조 및 스타일 규격 (템플릿)
출력되는 HTML 파일은 반드시 아래의 CSS 구조와 태그 배치를 따라야 합니다. (Mantis Algo의 시그니처 톤인 Teal, Orange, Gray 반영)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[지표 이름] — 한 줄 한 줄 풀이 (초보용)</title>
<style>
  :root{
    --bg:#0d0d0d; --panel:#161616; --panel2:#1d1d1d; --border:#2E2E2E;
    --txt:#DBDBDB; --head:#808080; --teal:#00b4d8; --orange:#ff9f1c; --green:#089981; --red:#f23645;
    --yellow:#ffd166; --aqua:#26c6da; --purple:#b388ff;
  }
  *{box-sizing:border-box;}
  body{margin:0;background:var(--bg);color:var(--txt);
    font-family:"Pretendard","Apple SD Gothic Neo",-apple-system,"Segoe UI",Roboto,sans-serif;
    line-height:1.7;font-size:15px;}
  header{background:linear-gradient(135deg,#161616,#0d0d0d);border-bottom:1px solid var(--border);
    padding:40px 24px 28px;text-align:center;}
  header h1{margin:0 0 8px;font-size:26px;color:#fff;letter-spacing:-.5px;}
  header p{margin:0;color:var(--head);font-size:14px;}
  .wrap{display:flex;max-width:1300px;margin:0 auto;align-items:flex-start;}
  nav{position:sticky;top:0;align-self:flex-start;width:250px;flex:none;
    padding:20px 14px;height:100vh;overflow:auto;border-right:1px solid var(--border);
    background:#101010;}
  nav a{display:block;color:var(--head);text-decoration:none;padding:6px 10px;border-radius:6px;
    font-size:13px;margin-bottom:2px;}
  nav a:hover{background:var(--panel2);color:var(--txt);}
  nav .grp{color:var(--teal);font-weight:700;font-size:12px;margin:14px 0 4px;text-transform:uppercase;letter-spacing:.5px;}
  main{flex:1;padding:24px 30px 120px;min-width:0;}
  section{margin-bottom:54px;scroll-margin-top:20px;}
  h2{font-size:22px;color:#fff;border-left:4px solid var(--teal);padding-left:12px;margin:0 0 6px;}
  h3{font-size:17px;color:var(--yellow);margin:30px 0 8px;}
  h4{font-size:14px;color:var(--head);margin:18px 0 6px;text-transform:uppercase;letter-spacing:.5px;}
  p{margin:10px 0;}
  code{background:#202020;color:#ffd479;padding:2px 6px;border-radius:4px;font-family:"JetBrains Mono",monospace;font-size:13px;}
  .codecard{background:var(--panel);border:1px solid var(--border);border-radius:10px;
    margin:14px 0;overflow:hidden;}
  .codecard .ln{background:#0a0a0a;color:#6a6a6a;padding:8px 12px;font-family:monospace;
     font-size:13px;white-space:pre;border-bottom:1px solid var(--border);}
  .codecard .body{padding:12px 16px;}
  .tok{display:inline-block;background:#232323;border:1px solid #333;border-radius:5px;
    padding:1px 6px;margin:2px 3px 2px 0;font-family:monospace;font-size:12.5px;color:#9ad;}
  .note{background:var(--panel2);border-left:3px solid var(--green);padding:10px 14px;border-radius:0 8px 8px 0;margin:8px 0;}
  .warn{background:var(--panel2);border-left:3px solid var(--red);padding:10px 14px;border-radius:0 8px 8px 0;margin:8px 0;}
  .why{background:#14181f;border-left:3px solid var(--teal);padding:10px 14px;border-radius:0 8px 8px 0;margin:8px 0;}
  table{width:100%;border-collapse:collapse;margin:12px 0;font-size:13.5px;}
  th,td{border:1px solid var(--border);padding:7px 10px;text-align:left;}
  th{background:var(--panel2);color:var(--head);}
  .swatch{display:inline-block;width:14px;height:14px;border-radius:3px;vertical-align:middle;margin-right:6px;border:1px solid #000;}
  .diagram{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:22px;margin:18px 0;}
  .flex{display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:center;}
  .box{background:var(--panel2);border:1px solid var(--border);border-radius:10px;padding:12px 16px;
    min-width:120px;text-align:center;font-size:13px;}
  .box.bsl{border-color:var(--red);}
  .box.ssl{border-color:var(--green);}
  .arrow{color:var(--head);font-size:22px;}
  .layer{height:34px;border-radius:4px;margin:3px 0;display:flex;align-items:center;
    padding:0 10px;font-size:12px;color:#000;font-weight:600;}
  .pill{display:inline-block;background:var(--panel2);border:1px solid var(--border);border-radius:20px;
    padding:3px 12px;font-size:12px;margin:3px 4px 3px 0;}
  .sig{display:inline-block;padding:3px 10px;border-radius:6px;font-weight:700;font-size:13px;color:#fff;}
  .sig.abs{background:var(--red);} .sig.exh{background:#e08e0b;} .sig.div{background:#7c4dff;} .sig.rej{background:var(--green);}
  .kbd{background:var(--panel2);border:1px solid var(--border);border-radius:6px;padding:2px 8px;font-family:monospace;font-size:12px;}
  .muted{color:var(--head);}
  .gloss{display:grid;grid-template-columns:1fr 2fr;gap:6px 16px;font-size:13.5px;}
  .gloss dt{color:var(--yellow);font-weight:700;}
  .gloss dd{margin:0;color:var(--txt);}
  details{background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:8px 14px;margin:10px 0;}
  summary{cursor:pointer;color:var(--teal);font-weight:600;}
  .flowrow{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:8px 0;}
</style>
</head>
<body>
...
</body>
</html>
```

### 2. 세부 콘텐츠 생성 지침

*   **0. Pine Script란 무엇인가? (`#basics`)**: Pine Script의 봉별 동작 메커니즘을 설명하고 해당 지표의 핵심 목표 한 줄 요약을 작성합니다. 이때 `llmwiki`(`concepts/series-vs-array.md`, `concepts/repainting.md` 등) 및 `pinestudy/`와 교차 링크를 생성합니다.
*   **1. 이 지표가 하는 일 (`#bigpic`)**: 흐름 다이어그램으로 입력-연산-출력을 도식화하고, 해당 코드가 **5-Part Anatomy** 골격을 어떻게 충족하는지 또는 예외적인 구조인지를 기술합니다.
*   **2. 시각 해부도 (`#visuals`)**: 화면에 그려지는 박스, 라인 등의 구조와 설정의 의미를 시각화하여 초보자에게 해설합니다.
*   **3. 코드 한 줄 풀이 (`#header` ~ `#logic`)**: 소스코드를 블록별로 쪼개어 `.codecard`로 포장하고 아래 내용을 기재합니다.
    - **5-Part Anatomy 매핑**: 해당 코드 블록이 5부 중 어디에 해당하는지 명시 (예: `[Custom Logic]`, `[Risk Mgmt]`).
    - **한 줄 뜻**: 직관적인 번역.
    - **💡 왜 있는가? (`.why`)**: 기획적, 수학적 설계 의도를 설명.
    - **경고/팁 (`.warn` 또는 `.note`)**: 리페인팅이나 메모리 한도 등 기술적 유의점을 기술.
*   **4. 코드가 어떻게 연결되나 (`#connect`)**: 함수 호출 체인과 변수 참조 흐름을 도식화합니다.
*   **5. 용어 사전 (`#gloss`)**: Technical Term을 가나다/알파벳 순으로 정리하되, `pinestudy`의 952개 식별자 사전 정의에 일치하도록 정렬합니다.

## 🔗 연결

[[pine-script]] · [[5-part-anatomy]] · [[repainting]] · [[tutor]]

## 📌 미해결
- 5-part anatomy 코드가 아닌 기존 오픈소스 Pine 코드를 해설할 때의 Anatomy 예외 판정 가이드 보강
