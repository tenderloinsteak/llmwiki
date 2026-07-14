# Memory — Cross-session Log

Append after every work session. Old entries get compacted by [[personas/librarian]].

Format: `date | persona | decision/progress | next`

---

- 2026-07-15 | orchestrator | Created Hermes wiki (base 3 + 7 role personas + index). Writing-style profile not yet set — run "learn my writing style" in a future session | Fill user.md blanks; decide Obsidian vault location
- 2026-07-15 | factory-manager | Restructured factory into 4 role parts: idea & UI (top importance), module-developer, development | Confirm UI palette
- 2026-07-15 | orchestrator | Analyzed all three repos. Mantis Algo: working LLM factory (163 modules, 8 SKUs, verification gate). AccountingGo: Flutter MVP, 13 question types, English-first content pipeline. ShiftTrade: Next.js+Supabase, Python tick engine (NemotronEngines). Rewrote entire wiki in English with reason-in-English/answer-in-Korean rule; renamed all files to English | User pastes profiles into Hermes; fill remaining blanks (palette, pricing)
- 2026-07-15 | orchestrator | Split character vs knowledge: profiles now carry only persona character (profiles/1-8); working knowledge moved into each repo's hermes/ folder (Mantis Algo: 6 files, ShiftTrade: 1, AccountingGo: 2). Wiki keeps CLAUDE/soul/user/memory + tutor & librarian | Paste profiles/1-8 into Hermes profile soul.md fields
- 2026-07-15 | librarian | Dedup cleanup: deleted profiles/ (deployed to ~/.hermes as single source), .claude/agents, soul.md, user.md. Wiki now = CLAUDE.md (index) + memory.md (journal) + personas/tutor.md, librarian.md (knowledge). Project knowledge stays in each repo's hermes/ | —
