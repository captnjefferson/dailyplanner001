# Briefing Module Stub — Catalyst Gate

Paste-ready module for Hal9000 `skills/briefing/` (adapt header/registration to the manifest format there). This is the bridge between this repo's `/gate` feed and the local `/briefing` where Jefferson approves roles for research.

## Module: catalyst-gate
Purpose: surface the overnight Catalyst gate feed; collect Jefferson's research approvals (human gate #1).

Steps:
1. Read today's feed file: `~/briefings/<YYYY-MM-DD>-gate.md` (today's date). If missing, emit exactly one line — "Catalyst gate: no feed today (cron may not have run)" — and stop.
2. Always render the feed's headline line first — quiet days surface one line ("Nothing new in Inbox/Sourced/Review since the last run." / "Nothing passed the gate today."), so cadence stays visible and a missing headline means a broken cron, not a quiet day. Then render PASS and NEAR-MISS rows verbatim when present. The table arrives pre-scored and pre-formatted: do NOT rescore, re-rank, or editorialize. Keep warm-path flags prominent.
3. When PASS/NEAR-MISS rows exist, end with the approval affordance: "Approve research per role by replying with its `/run-role <url>` line — execute in the hm-outreach project."

Contract notes:
- The feed is produced by `/gate` in the hm-outreach repo (read-only against Notion; the rubric lives there — this module never rescores).
- Approval in the briefing is gate #1 (research authorization). Gate #2 (the send) stays with Jefferson at the end of the pipeline, per the two-gate rule.
- FAIL rows are omitted from the briefing by design; they remain in the dated feed file if ever needed.
