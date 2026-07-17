---
tags: [mantisalgo, pine-script, wiki-meta, structure]
created: 2026-07-18
updated: 2026-07-18
sources: ["MantisAlgo/mantis/factory_saver.py", "MantisAlgo/pinescript_factory/"]
---

# Pine 평탄 저장 + 다대다 카테고리 연결 구조
> 폴더=단일부모 한계를 버리고, 파일은 평탄·분류는 wikilink/태그로 다대다.

## 🌱 쉽게

지금 `1_Indicators/Price_Action/`처럼 **폴더가 카테고리**면, 한 지표는 한 서랍에만 들어간다. 그런데 PAC Lite는 Price Action이면서 FVG·Liquidity·Support/Resistance에도 해당한다 — 이미 `// Tags:`에 적혀 있다.

원하는 그림: **서랍은 하나(Indicators)** 이고, 각 파일에 **여러 라벨을 붙인다.** 위키에서는 라벨 페이지 ↔ 스크립트 페이지가 서로 `[[링크]]`로 이어진다.

## ⚙️ 정확히

### 현재 상태 (이미 반쯤 있음)

| 층 | 위치 | 역할 |
|---|---|---|
| 주 카테고리 | `idea.category` → `// Category:` → **폴더명** | 단일 부모 (한계) |
| 부가 태그 | `idea.category_tags` → `// Tags:` | 이미 다대다 |
| 택소노미 | `factory_saver.CATEGORIES` 30종 | 정본 후보 |

실측: Indicators 11 `.pine` / Strategies 11 `.pine` / 빈 카테고리 폴더 다수.

### 제안 A — 레포(공장) 평탄화

```
pinescript_factory/
  1_Indicators/
    PAC_Lite_SKU01.pine          ← 평탄, 제목 통일
    Order_Flow_SKU05.pine
  2_Strategies/
    Trade_Engine_SKU06.pine
```

- **폴더로 분류 금지.** macro만 유지 (`indicator` vs `strategy`).
- 헤더 통일:
  ```
  //@version=6
  // Title: PAC Lite SKU-01
  // Kind: indicator
  // Tags: Price_Action, Support_Resistance, FVG, Liquidity
  ```
- `// Category:`(단일) 폐기 → **`// Tags:`만** (또는 Category를 Tags의 첫 항목으로 흡수).
- 파일명: `Pascal_Or_Snake` 통일 규칙 1개 (예: `{Name}_SKU{nn}.pine` / 비상용은 `{Descriptive_Name}.pine`).
- `factory_saver.save_to_factory`: micro 폴더 생성·라우팅 제거, Tags 헤더만 보장.

### 제안 B — llmwiki 쪽 (다대다 그래프)

모듈 지도와 같은 패턴:

```
wiki/
  pines/
    pines-map.md                 ← 허브 (자동생성 가능)
    scripts/
      pac-lite-sku01.md          ← 스크립트 1개 = 페이지 1개
      order-flow-sku05.md
    categories/
      price-action.md            ← 카테고리 1개 = 페이지 1개
      fvg.md
      liquidity.md
      …
  raw/
    pine-pac-lite-sku01.pine     ← 원본 캡처 (immutable)
```

**스크립트 페이지 frontmatter 예시:**

```yaml
tags: [pine-script, mantisalgo, indicator]
kind: indicator
mantis_tags: [Price_Action, Support_Resistance, FVG, Liquidity]
sku: SKU-01
source_repo: MantisAlgo/pinescript_factory/1_Indicators/PAC_Lite_SKU01.pine
sources: [raw/pine-pac-lite-sku01.pine]
```

**연결 (다대다):**

- 스크립트 → `## 🔗 연결`에 `[[categories/price-action]] · [[categories/fvg]] · …`
- 카테고리 → 해당 태그 가진 스크립트 목록 (pines-map 또는 카테고리 페이지에 backlink)
- Obsidian 그래프가 자동으로 다대다 반영

**캡처 ≠ 인제스트 유지:** `.pine`은 먼저 `raw/`에만. 분석 페이지(`pines/scripts/…`)는 요점 논의 후 또는 “알아서/배치” 시.

### 제안 C — 동기화 스크립트 (선택)

`modules`의 `registry_to_wiki.py`처럼:

`pine_factory_to_wiki.py`

1. `pinescript_factory/**/*.pine` 스캔
2. `// Tags:` 파싱
3. `wiki/pines/scripts/*.md` + `wiki/pines/categories/*.md` + `pines-map.md` 재생성
4. `index.md` 섹션 갱신

### 하지 말 것

- raw/ 아래에 카테고리 폴더 만들기 (SCHEMA: raw는 평탄)
- pinestudy와 병합 (식별자 학습 위키는 별도, 크로스링크만)
- 폴더와 태그 **둘 다** 권위 갖기 (드리프트) — 태그만 SoT

## 🔗 연결

[[mantisalgo]] · [[mantisalgo-sku-catalog]] · [[modules/modules-map]] · [[concepts/pine-script]] · [[concepts/llm-wiki-pattern]]

## 📌 미해결

- [x] 공장 평탄화 + Tags SoT (2026-07-18)
- [x] 헤더 Title/Kind/Tags 통일 + TV 제목=파일 stem
- [x] wiki/pines/ 그래프 + raw 캡처
- [ ] 외부(비공장) Pine도 같은 `pines/`에 넣을지 — 추천: origin 필드로 수용
- [ ] score_factory 경로 표기 갱신(output/factory_quality.md는 다음 스코어 시 자동)
