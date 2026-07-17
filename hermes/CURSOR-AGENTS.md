# Cursor ↔ Hermes sync

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

- [[personas/souls/ceo]] → `~/.cursor/agents/ceo.md`
- [[personas/souls/critic]] → `~/.cursor/agents/critic.md`
- [[personas/souls/factory-development]] → `~/.cursor/agents/factory-development.md`
- [[personas/souls/factory-idea]] → `~/.cursor/agents/factory-idea.md`
- [[personas/souls/factory-manager]] → `~/.cursor/agents/factory-manager.md`
- [[personas/souls/factory-module-developer]] → `~/.cursor/agents/factory-module-developer.md`
- [[personas/souls/factory-ui]] → `~/.cursor/agents/factory-ui.md`
- [[personas/souls/learning-ux-designer]] → `~/.cursor/agents/learning-ux-designer.md`
- [[personas/souls/librarian]] → `~/.cursor/agents/librarian.md`
- [[personas/souls/microstructure-engineer]] → `~/.cursor/agents/microstructure-engineer.md`
- [[personas/souls/quiz-writer]] → `~/.cursor/agents/quiz-writer.md`
- [[personas/souls/tutor]] → `~/.cursor/agents/tutor.md`

## Sync

```bash
python3 hermes/scripts/sync-cursor-agents.py
```

**Source of truth:** Hermes `SOUL.md` files under `~/.hermes/`.
**Obsidian** mirrors personas for reading/linking; **Cursor** agents are generated.
**Knowledge** stays in repo `hermes/` folders + this vault (`memory.md`, detailed personas).
**Wiki:** `${WIKI_PATH}/wiki/` (SCHEMA auto-accumulation; WIKI_PATH = llmwiki repo root).
