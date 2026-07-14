#!/usr/bin/env python3
"""Sync Hermes profiles → Cursor subagents (+ Obsidian persona mirrors).

Source of truth for character:
  ~/.hermes/SOUL.md              → ceo
  ~/.hermes/profiles/*/SOUL.md   → specialists

Knowledge wiki (not copied into agents as body):
  /Users/kkj/Desktop/obsidian/hermes/

Usage:
  python3 ~/Desktop/obsidian/hermes/scripts/sync-cursor-agents.py
"""

from __future__ import annotations

import re
from pathlib import Path

HOME = Path.home()
HERMES = HOME / ".hermes"
PROFILES = HERMES / "profiles"
CURSOR_AGENTS = HOME / ".cursor" / "agents"
OBSIDIAN = HOME / "Desktop" / "obsidian" / "hermes"
PERSONAS = OBSIDIAN / "personas"
SOUL_MIRRORS = PERSONAS / "souls"
# Knowledge-only wiki notes (do NOT overwrite with SOUL mirrors):
KNOWLEDGE_PERSONAS = {"tutor", "librarian"}

# Expand relative Desktop paths used in Hermes SOUL files
PATH_MAP = {
    "Desktop/헤르메스": str(OBSIDIAN),
    "Desktop/Mantis Algo": str(HOME / "Desktop" / "Mantis Algo"),
    "Desktop/ShiftTrade": str(HOME / "Desktop" / "ShiftTrade"),
    "Desktop/AccountingGo": str(HOME / "Desktop" / "AccountingGo"),
}

META = {
    "ceo": {
        "description": (
            "Hermes CEO / main orchestrator. Routes work to specialists and enforces "
            "quality gates only — no domain work. Use proactively for ambiguous requests, "
            "multi-role workflows, and any task that needs ownership confirmation."
        ),
        "extra": """
## Cursor hierarchy

You are the top router in Cursor. You do not implement domain work yourself.

### Direct reports (route here)
- `quiz-writer` — AccountingGo question authoring
- `learning-ux-designer` — AccountingGo UX / gamification
- `microstructure-engineer` — ShiftTrade market engine
- `factory-manager` — ALL MantisAlgo Pine/product production (do NOT route past the manager to factory staff)
- `critic` — independent audit of factory output
- `tutor` — study sessions
- `librarian` — wiki / index / memory compaction

### Factory subtree (owned by factory-manager — do not assign directly unless user names them)
- `factory-idea` → idea specs & sales copy
- `factory-development` → pipeline & verification gate
- `factory-module-developer` → module registry / parts
- `factory-ui` → chart visuals & input UX

When multi-role: run sequentially and state the active role each turn.
When handing off, say exactly which subagent should take over and why.
""",
    },
    "critic": {
        "description": (
            "MantisAlgo independent auditor (critic). Reviews freshness, marketability, "
            "and technical integrity; approve / conditional / reject. Use proactively after "
            "any indicator/strategy/module production before calling work done."
        ),
        "extra": """
## Org note
Independent of factory-manager. You audit; you never help produce.
Reports to CEO for routing, not to the factory.
""",
    },
    "factory-manager": {
        "description": (
            "MantisAlgo factory manager. Supervises the production pipeline and the four "
            "factory staff (idea, development, module-developer, ui). Use proactively for "
            "any Pine Script indicator/strategy/module production request."
        ),
        "extra": """
## Team (you supervise — assign stages, do not absorb their jobs)

| Staff subagent | Owns |
|---|---|
| `factory-idea` | Idea JSON specs, differentiators, sales copy |
| `factory-development` | Pipeline runs, verification gate, Pine assembly |
| `factory-module-developer` | Module registry, reusable parts, gap map |
| `factory-ui` | Visual standards, declutter, settings UX, marketing charts |

Production order default: idea → (module gaps) → development → ui → hand to `critic`.
Output is not done until `critic` approves.
When a stage is not yours, hand off to that staff subagent and state the active role.
""",
    },
    "factory-idea": {
        "description": (
            "MantisAlgo factory idea planner under factory-manager. Owns idea specs and "
            "sales copy. Use when drafting product ideas, differentiators, or pipeline-consumable idea JSON."
        ),
        "extra": """
## Reports to
`factory-manager`. Do not skip to critic or CEO for production decisions — escalate via manager.
""",
    },
    "factory-development": {
        "description": (
            "MantisAlgo factory development / pipeline engineer under factory-manager. "
            "Defends the verification gate and runs product generation. Use for pipeline "
            "runs, gate failures, and Pine assembly — not for idea specs or visual polish."
        ),
        "extra": """
## Reports to
`factory-manager`. Hand reusable parts to `factory-module-developer`. Hand visual work to `factory-ui`.
""",
    },
    "factory-module-developer": {
        "description": (
            "MantisAlgo factory module-developer under factory-manager. Owns module registry, "
            "generator parity, and reusable parts. Use when adding/fixing modules or checking registry gaps."
        ),
        "extra": """
## Reports to
`factory-manager`. Independent of product deadlines — parts quality over SKU rush.
""",
    },
    "factory-ui": {
        "description": (
            "MantisAlgo factory UI visual designer under factory-manager. Owns chart visuals, "
            "declutter, palette consistency, and settings UX. Use for visual review and marketing-grade defaults."
        ),
        "extra": """
## Reports to
`factory-manager`. Independent part — never a sub-task folded into development.
""",
    },
    "learning-ux-designer": {
        "description": (
            "AccountingGo learning UX designer. Storyboards, wireframes, gamification, "
            "explainer animations. Use proactively for AccountingGo UI/UX and learning-flow design."
        ),
        "extra": "",
    },
    "quiz-writer": {
        "description": (
            "AccountingGo quiz writer. Offline question authoring with accountant-grade "
            "accuracy across 13 types. Use proactively for question batches, types, and explanations."
        ),
        "extra": "",
    },
    "microstructure-engineer": {
        "description": (
            "ShiftTrade microstructure engineer. Order-event realism for price, book, and tape. "
            "Use proactively for engine, order book, trade strength, or tape work."
        ),
        "extra": "",
    },
    "librarian": {
        "description": (
            "Hermes librarian. Structure-only: indexes, links, orphan fixes, memory compaction. "
            "Use proactively for wiki maintenance and when notes/links drift."
        ),
        "extra": "",
    },
    "tutor": {
        "description": (
            "Hermes tutor. Applied teaching for Pine Script, quant basics, and statistics "
            "tied to real projects. Use proactively for study sessions."
        ),
        "extra": "",
    },
}

CURSOR_PREAMBLE = """
## Cursor operating rules

When invoked:
1. Read the Working Knowledge files listed below (absolute paths) before acting.
2. Stay in your lane; if the task belongs to another role, say so and stop (or hand off).
3. Think in English; speak to 곽경준 in Korean — concise, conclusion first, no filler, no flattery.
4. End the job by appending a short decision note to `{memory}` (decision + why).
5. Prefer verifying over guessing. Push back when the user is wrong.

This agent was generated from Hermes SOUL.md. Re-run `obsidian/hermes/scripts/sync-cursor-agents.py` after editing profiles.
""".strip()


def expand_paths(text: str) -> str:
    out = text
    # Longest keys first; replace each key only once so
    # "/Users/kkj/Desktop/..." is not re-matched on "Desktop/..."
    for old, new in sorted(PATH_MAP.items(), key=lambda kv: -len(kv[0])):
        out = out.replace(old, new)
    out = out.replace(str(HOME / "Desktop" / "헤르메스"), str(OBSIDIAN))
    return out


def strip_title(soul: str) -> str:
    # Keep body; drop leading "# Hermes Profile — ..." title for cleaner agent body
    lines = soul.strip().splitlines()
    if lines and lines[0].startswith("# Hermes Profile"):
        lines = lines[1:]
        while lines and lines[0].strip() in ("", "---"):
            lines = lines[1:]
    return "\n".join(lines).strip() + "\n"


def write_agent(name: str, soul_body: str, meta: dict) -> Path:
    memory = OBSIDIAN / "memory.md"
    preamble = CURSOR_PREAMBLE.format(memory=memory)
    body = expand_paths(soul_body)
    extra = meta.get("extra") or ""
    content = (
        f"---\n"
        f"name: {name}\n"
        f"description: {meta['description']}\n"
        f"---\n\n"
        f"{body}\n"
        f"{extra.rstrip()}\n\n"
        f"{preamble}\n"
    )
    # Collapse excessive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)
    path = CURSOR_AGENTS / f"{name}.md"
    path.write_text(content, encoding="utf-8")
    return path


def mirror_persona(name: str, soul: str) -> Path | None:
    """Mirror SOUL into personas/souls/ — never overwrite knowledge notes in personas/."""
    SOUL_MIRRORS.mkdir(parents=True, exist_ok=True)
    path = SOUL_MIRRORS / f"{name}.md"
    header = (
        f"---\n"
        f"tags: [hermes, persona, soul-mirror]\n"
        f"source: ~/.hermes/{'SOUL.md' if name == 'ceo' else f'profiles/{name}/SOUL.md'}\n"
        f"cursor_agent: ~/.cursor/agents/{name}.md\n"
        f"---\n\n"
        f"> Character mirror only. Edit Hermes SOUL.md, then re-run sync.\n"
        f"> Knowledge for tutor/librarian lives in `personas/tutor.md` / `personas/librarian.md` (not here).\n\n"
    )
    path.write_text(header + soul.strip() + "\n", encoding="utf-8")
    return path


def main() -> None:
    CURSOR_AGENTS.mkdir(parents=True, exist_ok=True)
    written = []

    # CEO from ~/.hermes/SOUL.md
    ceo_soul = (HERMES / "SOUL.md").read_text(encoding="utf-8")
    written.append(write_agent("ceo", strip_title(ceo_soul), META["ceo"]))
    written.append(mirror_persona("ceo", ceo_soul))

    for profile_dir in sorted(PROFILES.iterdir()):
        if not profile_dir.is_dir():
            continue
        name = profile_dir.name
        soul_path = profile_dir / "SOUL.md"
        if not soul_path.exists():
            print(f"skip {name}: no SOUL.md")
            continue
        if name not in META:
            print(f"warn {name}: no META description — using generic")
            meta = {
                "description": f"Hermes profile `{name}`. Use when this specialist owns the task.",
                "extra": "",
            }
        else:
            meta = META[name]
        soul = soul_path.read_text(encoding="utf-8")
        written.append(write_agent(name, strip_title(soul), meta))
        written.append(mirror_persona(name, soul))

    # Index note for Obsidian
    index = OBSIDIAN / "CURSOR-AGENTS.md"
    names = ["ceo"] + sorted(p.name for p in PROFILES.iterdir() if p.is_dir())
    bullets = "\n".join(f"- [[personas/souls/{n}]] → `~/.cursor/agents/{n}.md`" for n in names)
    index.write_text(
        f"""# Cursor ↔ Hermes sync

## Hierarchy

```
CEO (ceo)
├── quiz-writer
├── learning-ux-designer
├── microstructure-engineer
├── critic          ← audits factory; independent
├── tutor
├── librarian
└── factory-manager
    ├── factory-idea
    ├── factory-development
    ├── factory-module-developer
    └── factory-ui
```

## Agents

{bullets}

## Sync

```bash
python3 ~/Desktop/obsidian/hermes/scripts/sync-cursor-agents.py
```

**Source of truth:** Hermes `SOUL.md` files under `~/.hermes/`.
**Obsidian** mirrors personas for reading/linking; **Cursor** agents are generated.
**Knowledge** stays in repo `hermes/` folders + this vault (`memory.md`, detailed personas).
""",
        encoding="utf-8",
    )

    print(f"Wrote {len([p for p in written if p.parent == CURSOR_AGENTS])} Cursor agents → {CURSOR_AGENTS}")
    print(f"Mirrored personas → {PERSONAS}")
    print(f"Index → {index}")
    for p in sorted(CURSOR_AGENTS.glob("*.md")):
        print(f"  {p.name}")


if __name__ == "__main__":
    main()
