# HM-Direct Outreach System v2 — Claude Code Operating Rules

This project runs Jefferson Stovall's hiring-manager-direct outreach pipeline. Full spec in `reference/spec.md`; rubric and templates in `reference/`.

## Non-negotiable rules
1. **Two human gates, always.** Jefferson authorizes research (per role) and Jefferson sends outreach (personally). NEVER send, submit, or post anything. All notes are drafts written to `runs/`.
2. **Source discipline.** Every factual claim in a dossier carries a working URL. No URL → delete at intake, don't soften. A wrong specific is fatal; a missing one is not.
3. **Anti-slop guardrails on all drafts:** 100–130 words; no flattery openers ("I was impressed by", "I've been following"); substance-first; ONE proof point; soft question CTA; Jefferson's voice (direct, a little dry, builder's vocabulary). Register-match the target's altitude — NEVER mimic their style.
4. **Inference visibility.** Every load-bearing claim in a synthesis brief is tagged [sourced], [inferred — from X], or [speculation].
5. **Pre-filters before scoring:** comp range max < $125K fails; equity-in-lieu-of-cash fails (standard RSUs atop clearing cash are fine); unconfirmable eligibility fails; travel >50% fails.
6. **The gate** (survivors only): C1 target-spec fit is MANDATORY; pass = C1 YES + at least one of C2 (findable decision-maker) / C3 (real-problem visibility) YES. Known warm path + C1 YES = auto-pass + priority flag. Health-focused orgs at senior level = C1 fail (domain mismatch).
7. **Follow-up policy:** exactly one, 6–8 business days, value-add only. Then closed.
8. **No new tooling** until 8–10 roles have flowed through and friction points are known.

## Workflow
- `/brief` — gate-score new Catalyst roles (read Notion via MCP), output briefing table. Read-only; safe to run headless.
- `/run-role <posting-url-or-catalyst-page>` — full pipeline on one authorized role: spawn the four research subagents IN PARALLEL, intake, synthesize, draft. Output to `runs/YYYY-MM-DD-<org>/`.
- `/backtest` — score a role set against the gate without running research.

## Research subagents (each returns ONLY the dossier template in reference/dossier-template.md)
- `org-researcher` — Phase 1A: strategy, news, 990s if nonprofit, job-cluster analysis
- `posting-archaeologist` — Phase 1B: repost history, language diffs, comp verification
- `person-finder` — Phase 1C: HM triangulation + warm-path check against background/network.md
- `voice-corpus` — Phase 1D: target's public writing/talks; priorities and register only

## Context files
- `background/profile.md` — Jefferson's background and proof points
- `background/network.md` — ten-names list and warm-network context (feeds person-finder)
- `runs/2026-07-04-blue-acorn-ici/` — golden example of a complete run

## Catalyst Pipeline (Notion) — verified 2026-07-05
- Database: https://app.notion.com/p/38f164c1810d817dafddd42ea3cb4157 (data source `collection://38f164c1-810d-8121-9f38-000b5a53dbaf`, inside "Catalyst — Job Application Pipeline")
- Schema: `Name` (title), `Stage` (Inbox / Sourced / Building / Review / Ready / Applied / Interviewing / Closed), `Tier`, `Detail` (posting URL), `Amount` (comp), `Blocked`. `/brief` queries Stage ∈ {Inbox, Sourced, Review}.
