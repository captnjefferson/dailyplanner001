Catalyst gate-scoring pass — the FEED for Jefferson's local `/briefing` (Hal9000 morning product). Approval happens in that briefing, not here; this command only scores and reports. (Named /gate to avoid colliding with Hal9000's local /brief ops command.)

1. Query the Catalyst Pipeline Notion database (MCP) for roles in Stage Inbox/Sourced/Review.
2. Skip roles already in `runs/gate-ledger.md` (the scored-role watermark). Everything remaining is "new."
3. Apply pre-filters from CLAUDE.md rule 5. Pre-filter hits: list under "Volume machine only" with the tripped filter.
4. Score survivors per reference/rubric.md: C1 (mandatory) / C2 / C3, graded /6, binary verdict.
5. Check background/network.md for known warm paths → auto-pass + priority flag where found.
6. Append every newly scored role to `runs/gate-ledger.md` as `date | org — role | url | verdict`. If the ledger can't be written (headless permissions), say so in the output rather than failing silently.
7. Output — ALWAYS begins with the headline, even on empty days (no silent failures):
   `Catalyst gate — YYYY-MM-DD: N new · P PASS · M NEAR-MISS · F FAIL · X pre-filtered`
   - N = 0 → exactly one more line: "Nothing new in Inbox/Sourced/Review since the last run." Stop.
   - N > 0 → the scored table `ORG — ROLE | Verdict | C1:x C2:x C3:x = n/6 | warm-path | one-line rationale`, sorted PASS → NEAR-MISS → FAIL.
   - P = 0 and M = 0 → keep the table and add: "Nothing passed the gate today."
8. When at least one PASS or NEAR-MISS exists, end with the handoff line: "Approve in the morning briefing; execute each approval here: /run-role <url> (hm-outreach project)."

Output clean markdown only — the briefing module embeds it verbatim. READ-ONLY against Notion (never modify it); the only local write is the ledger append. Do not launch research subagents from this command.
