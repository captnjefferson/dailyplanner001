Catalyst gate-scoring pass — the FEED for Jefferson's local `/briefing` (Hal9000 morning product). Approval happens in that briefing, not here; this command only scores and reports. (Named /gate to avoid colliding with Hal9000's local /brief ops command.)

1. Query the Catalyst Pipeline Notion database (MCP) for roles in Inbox/Sourced/Review not yet gate-scored.
2. Apply pre-filters from CLAUDE.md rule 5. Pre-filter hits: list under "Volume machine only" with the tripped filter.
3. Score survivors per reference/rubric.md: C1 (mandatory) / C2 / C3, graded /6, binary verdict.
4. Check background/network.md for known warm paths → auto-pass + priority flag where found.
5. Output table: `ORG — ROLE | Verdict | C1:x C2:x C3:x = n/6 | warm-path | one-line rationale`, sorted PASS → NEAR-MISS → FAIL.
6. End with the handoff line: "Approve in the morning briefing; execute each approval here: /run-role <url> (hm-outreach project)."

Output clean markdown only — the briefing module embeds it verbatim. READ-ONLY. Do not modify Notion. Do not launch research subagents from this command.
