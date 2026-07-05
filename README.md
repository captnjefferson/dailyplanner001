# HM-Direct Outreach — Setup

## 1. Install & open
Install Claude Code (desktop app or `npm install -g @anthropic-ai/claude-code`), then open this folder as the project.

## 2. Connect Notion (Catalyst pipeline access)
The Notion MCP server is pre-configured in `.mcp.json` — approve it on first launch and authenticate when prompted. (Manual fallback: `claude mcp add --transport http notion https://mcp.notion.com/mcp`.) Claude Code web/remote sessions with the Notion connector enabled already have access. The `/brief` command reads the Catalyst Pipeline database; its coordinates are pinned in `CLAUDE.md`.

## 3. Fill in the blanks
- `background/profile.md` — replace TODOs (attach real resume content, proof-point numbers)
- `background/network.md` — the ten-names list. Everything downstream is better with this filled in.

## 4. Daily use
- Morning: run `/brief`. Thumbs-up roles = run `/run-role <url>` for each.
- Review the draft in `runs/`, edit in your voice, read-aloud pass, send it yourself.
- Log one row in the tracker. That's the whole motion.

## 5. Optional: automated morning briefing
Headless run on a schedule (launchd/cron on macOS):
    claude -p "/brief" > ~/briefings/$(date +%F)-brief.md
Safe because /brief is read-only. Research and sending stay behind your two gates.

## Migration provenance
Built 2026-07-04 from the chat-based v2 spec. The Blue Acorn iCi run in runs/ is the golden example — single-threaded simulation; this repo runs the same pipeline with real parallel subagents.
