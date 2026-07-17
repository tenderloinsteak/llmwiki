# Extracting the full Pine v6 reference identifier list

Goal: get an exhaustive, typo-free list of every function/variable/constant/keyword/operator from the official TradingView Pine Script v6 reference, to build a complete learning checklist.

## Key fact: it is an SPA
- `curl` (even with a UA) on `https://kr.tradingview.com/pine-script-reference/v6/` returns ~120 KB of app skeleton. **No function names are in the static HTML.** The list is rendered client-side from JS.
- Therefore: do NOT try to grep/parse the curl'd HTML for functions. You will get nothing useful (only `ta.` matches that are JS var names like `ta.theme`).

## Working method (browser_console DOM scrape)
1. `browser_navigate` to the v6 URL. Wait for render.
2. `browser_console` with a JS expression that:
   - collects `[...document.querySelectorAll('a')]`, takes `textContent.trim()`
   - filters out Korean UI menu words, any string containing a non-ASCII char, any containing `→` or whitespace, any containing `...`
   - de-duplicates
   - classifies into TYPE / VAR / CONST / FUNC (has `(` → strip to base name + `()`) / KEYWORD / OPERATOR / ANNOTATION (starts with `@`)
   - groups FUNC by namespace prefix
   - marks a hand-picked `core` set with 🔴 (daily/essential) vs ⚪
   - returns the assembled markdown string
3. To get the markdown out of the browser: build a `Blob`, make an `<a download>` and `.click()`. It lands in `~/Downloads/`. Then `mv` it into the project (e.g. `Desktop/pinestudy/`).
   - Do NOT try to paste 950 lines through the chat — transcription errors. The blob download is the reliable path.

## Result of the 2026-07-15 run
- Extracted **952 identifiers**: 20 types, 193 built-in vars, 216 constants, **479 functions**, 14 keywords, 20 operators, 10 annotations.
- Functions grouped by namespace: ta 59, strategy 49, array 55, matrix 49, box 29, label 21, line 22, table 22, math 24, input 14, map 11, request 11, str 18, color 7, chart 5, linefill 5, polyline 2, footprint 9, volume_row 8, ticker 9, timeframe 3, syminfo 2, runtime 1, top-level 41.
- Saved to `Desktop/pinestudy/pine_v6_checklist.md`.

## Pitfalls
- Korean-page (`kr.`) link text is clean ASCII identifiers (the menu words are the only Korean). The English page is the same structure. Either works; filter on non-ASCII to drop menu noise.
- `array.new<type>()` and `map.new<type,type>()` and `matrix.new<type>()` appear with `<type>` — keep them as literal template entries, don't try to expand.
- Function overloads with return-type signatures (e.g. `math.abs(number) → series float`) are rendered as separate `<a>` text in the page body but the sidebar/anchor list uses the bare `math.abs()` form. Scrape the anchor list (clean, no `→`), not the body, to avoid duplicates.
