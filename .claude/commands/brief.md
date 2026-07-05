Morning briefing: gate-score new roles from the Catalyst Pipeline.

1. Query the Catalyst Pipeline Notion database (MCP) for roles in Inbox/Sourced/Review not yet gate-scored.
2. Apply pre-filters from CLAUDE.md rule 5. Pre-filter hits: list under "Volume machine only" with the tripped filter.
3. Score survivors per reference/rubric.md: C1 (mandatory) / C2 / C3, graded /6, binary verdict.
4. Check background/network.md for known warm paths → auto-pass + priority flag where found.
5. Output table: `ORG — ROLE | Verdict | C1:x C2:x C3:x = n/6 | warm-path | one-line rationale`, sorted PASS → NEAR-MISS → FAIL.
6. End with: "Reply /run-role <url> to authorize research on any PASS."

READ-ONLY. Do not modify Notion. Do not launch research subagents from this command.
