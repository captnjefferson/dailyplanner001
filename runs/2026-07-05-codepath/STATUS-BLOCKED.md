# RUN BLOCKED — CodePath

- **Role:** https://job-boards.greenhouse.io/codepath/jobs/5175813007
- **Attempted:** 2026-07-05
- **Outcome:** Could not run. No dossiers, no brief, no draft produced.

## Why
Web access is permission-denied in this session. `WebSearch`, `WebFetch`, and
outbound `curl` all returned "you haven't granted it yet" on every attempt —
at BOTH the orchestrator level and inside all three research subagents
(org-researcher, posting-archaeologist, person-finder). Local file ops work;
network egress does not. Pattern matches a headless/non-interactive invocation
(see gate-ledger history re: headless auth walls).

## What this blocks
- Fetching the posting → cannot confirm the gate, read the title, or verify the
  comp pre-filter (comp max < $125K = fail; unknowable without the fetch).
- All four research phases (org / posting / person / voice) — all web-dependent.
- Source discipline (CLAUDE.md rule 2) forbids writing any dossier claim without
  a working URL, so nothing was drafted. No fabrication.

## Prior general knowledge (NOT recorded as findings — must be independently sourced)
- CodePath is a US 501(c)(3) tech-education nonprofit (student CS-career pipeline).
- Co-founders commonly associated: Michael Ellison, Tim Lee, Nathan Esquenazi.
- None of this is URL-backed this session and must not be used until sourced.

## To unblock
1. Re-run `/run-role https://job-boards.greenhouse.io/codepath/jobs/5175813007`
   in an INTERACTIVE session where WebSearch/WebFetch can be approved, OR
2. Grant WebSearch + WebFetch for this session and the subagents, then re-run.

Subagents left standing (resumable via SendMessage): org a5944b8ae75fea0a3,
posting ad0656a15a49b2aaa, person a18d907b14365614e.
