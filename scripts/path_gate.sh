#!/usr/bin/env bash
# path_gate.sh — fail if hard-coded machine paths remain in portable docs.
# History under wiki/ and memory.md journal lines are excluded.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEV="$(cd "$ROOT/.." && pwd)"

PATTERN='/Users/kkj|~/Desktop/dev|Desktop/dev/llmwiki'

echo "== path_gate: scanning portable docs =="

fail=0

scan() {
  local label="$1"; shift
  local hits
  hits="$(grep -rn -I --exclude-dir=.git --exclude-dir=node_modules \
    --exclude-dir=build --exclude-dir=.next --exclude-dir=wiki \
    -E "$PATTERN" --include='*.md' --include='*.mdc' "$@" 2>/dev/null \
    | grep -v 'memory\.md:' || true)"
  if [[ -n "$hits" ]]; then
    echo "FAIL [$label]:"
    echo "$hits"
    fail=1
  else
    echo "OK   [$label]"
  fi
}

scan "llmwiki skills/docs" \
  "$ROOT/skills" "$ROOT/CLAUDE.md" "$ROOT/AGENTS.md" \
  "$ROOT/hermes/personas" "$ROOT/hermes/profiles" "$ROOT/hermes/CLAUDE.md"

# Empty-substitution check
empty="$(grep -rn -E '(^|[^A-Za-z0-9_}~.])/memory\.md|~//' --include='*.md' \
  "$ROOT/skills" "$ROOT/hermes" 2>/dev/null | grep -v '\${WIKI_PATH}' || true)"
if [[ -n "$empty" ]]; then
  echo "FAIL [empty \${WIKI_PATH} substitution]:"
  echo "$empty"
  fail=1
else
  echo "OK   [empty substitution]"
fi

for repo in MantisAlgo ShiftTrade AccountingGo; do
  if [[ -d "$DEV/$repo" ]]; then
    scan "$repo" "$DEV/$repo"
  else
    echo "SKIP [$repo] (not found next to llmwiki)"
  fi
done

# .env must not be tracked
tracked_env="$(cd "$ROOT" && git ls-files | grep -E '(^|/)\.env$' || true)"
if [[ -n "$tracked_env" ]]; then
  echo "FAIL [.env tracked in git]:"
  echo "$tracked_env"
  fail=1
else
  echo "OK   [no tracked .env]"
fi

if [[ "$fail" -ne 0 ]]; then
  echo "== path_gate FAILED =="
  exit 1
fi
echo "== path_gate PASSED =="
