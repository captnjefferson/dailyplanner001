# HM-Direct Outreach — Setup

## 1. Install & open
Install Claude Code (desktop app or `npm install -g @anthropic-ai/claude-code`), then open this folder as the project.

## 2. Connect Notion (Catalyst pipeline access)
The Notion MCP server is pre-configured in `.mcp.json` — approve it on first launch and authenticate when prompted. (Manual fallback: `claude mcp add --transport http notion https://mcp.notion.com/mcp`.) Claude Code web/remote sessions with the Notion connector enabled already have access. The `/gate` command reads the Catalyst Pipeline database; its coordinates are pinned in `CLAUDE.md`.

## 3. Fill in the blanks
- `background/profile.md` — replace TODOs (attach real resume content, proof-point numbers)
- `background/network.md` — the ten-names list. Everything downstream is better with this filled in.

## 4. Daily use
- Overnight/early: the gate feed runs headless (see 5) and lands in `~/briefings/`.
- Morning: your local `/briefing` (Hal9000) surfaces the scored table — approve roles there.
- Execute each approval here: `/run-role <url>`. Review the draft in `runs/`, edit in your voice, read-aloud pass, send it yourself.
- Log one row in the tracker. That's the whole motion.

## 5. Briefing integration (the intended wiring)
Headless run on a schedule (launchd/cron on macOS), before your usual `/briefing` time:
    claude -p "/gate" --permission-mode acceptEdits > ~/briefings/$(date +%F)-gate.md
(acceptEdits lets the run append `runs/gate-ledger.md`, the already-scored watermark; the feed always opens with a dated headline line — counts or "nothing new" — so a missing/empty file means the cron broke, never a quiet day)
Then point a Hal9000 `skills/briefing/` module at that file — a paste-ready stub is in `reference/briefing-module.md`. Safe because /gate is read-only. Research approval (in the briefing) and sending stay your two gates.

Note: this repo's gate command is `/gate`, not `/brief` — Hal9000 already owns `/brief` (Daily Ops Brief) and `/briefing` (morning product) locally.

## Migration provenance
Built 2026-07-04 from the chat-based v2 spec. The Blue Acorn iCi run in runs/ is the golden example — single-threaded simulation; this repo runs the same pipeline with real parallel subagents.
