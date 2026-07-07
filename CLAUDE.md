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
- `/gate` — gate-score new Catalyst roles (read Notion via MCP); outputs the scored table that FEEDS Jefferson's local `/briefing` (Hal9000 morning product — separate repo). The research thumbs-up (human gate #1) happens in that briefing, never here. Renamed from `/brief` 2026-07-05 to avoid colliding with Hal9000's local `/brief` ops command. Read-only; safe to run headless. Module stub for the briefing side: `reference/briefing-module.md`.
- `/run-role <posting-url-or-catalyst-page>` — full pipeline on one role approved in the briefing: spawn the four research subagents IN PARALLEL, intake, synthesize, draft. Output to `runs/YYYY-MM-DD-<org>/`.
- `/backtest` — score a role set against the gate without running research.

## Post-research note flow (CANONICAL — Jefferson, 2026-07-05: "if this works, this should become canonical")
After `/run-role` produces a draft, before anything reaches Jefferson's review table:
1. **Humantic profile** the target person: app.humantic.ai → Search For Anyone → paste the LinkedIn URL (or Name + Company) → click the result → Download PDF (lands in `~/Downloads/<Name> - Humantic AI Buyer Profile.pdf`). Jefferson's Chrome session is signed in. (The LinkedIn-page extension popup is the faster path when a human drives; it does not inject for automated sessions — use the app.) No person found (e.g. portal-only roles) → skip; the note ships as the application cover note.
2. **Adjust the note** for the profile's language/tone/structure guidance (salutation, length, bullets-or-not, ask style, superlative tolerance) — anti-slop rules and Jefferson's voice remain BINDING and win any conflict (e.g. Humantic "standard greeting line" loses to substance-first). Adjust register/structure, never mimic the person.
3. **Publish to Notion**: one child page per role under the role's Catalyst detail page, titled `HM outreach note — <Person> (<Org>) — YYYY-MM-DD`, containing recipient/channel callout, the adjusted note, the single follow-up, what-changed-for-the-profile, and verify-before-send flags.
4. **Hand off to the apply-side agent** (board name: **Job Apps**) via the Agent Messages board: all note URLs + instruction to include each URL in the review list/table Jefferson gets, one per matching application row. Notes remain Jefferson's to send personally (gate 2).
Conditional-truth rule: any note claiming "my application is in" ships only after that application actually files.

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
- Schema: `Name` (title), `Stage` (Inbox / Sourced / Building / Review / Ready / Applied / Interviewing / Closed), `Tier`, `Detail` (posting URL), `Amount` (comp), `Blocked`. `/gate` queries Stage ∈ {Inbox, Sourced, Review}.

## Jefferson calibrations (2026-07-07, from the ButterflyMX cycle — apply to all future runs)
- **HM inference at M confidence is sendable.** "Close enough is good enough" — address the best-inferred owner; don't spend a verification pass on HM identity. (Escalation alternates still get listed in the brief.)
- **Org-fit beats req liveness.** If the org/role type is on-point, outreach proceeds even if the posting looks closed/filled — the warm lane targets orgs and people, not postings. Only the parallel APPLICATION needs a live-status check before filing.
- **Comp bands that open below the $125K floor are workable when the max clears it** — he negotiates the top third. Keep flagging it in the table; don't treat it as a blocker.
- **network.md is a living list** — he can add names anytime; resolve (live LinkedIn pull) and append, then the next /gate run picks them up.
