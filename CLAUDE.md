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

## Standing order — gate PASSes auto-run (Jefferson, 2026-07-08)

"Continue with the gates and such for whichever jobs qualify. I don't need to
approve any of that… Run it and pass whatever the results are on to Resumer."

- Gate PASSes no longer wait for per-role research approval. The Fixer runs
  `/run-role` directly on qualifying PASSes the same morning the feed lands.
- "Qualifying" = the gate's own caveats still get verified BEFORE running
  (e.g. 2026-07-08: Adobe verified internal-enablement not sales → ran;
  USAA verified 4-days-in-office TX/NC → killed, no run).
- Results (brief.md + note.md) are mailed to **Resumer** as they land.
- **Gate 2 is untouched:** Jefferson personally edits and sends every note.
  The system still never sends outreach.

## Standing priority — ADOBE (Jefferson, 2026-07-08, window ~through 2026-08-08)

"Adobe apps that I qualify for are high priority for the next month."

- Any Adobe role passing C1 (senior AI-transformation / enablement / adoption /
  change-management leadership) gets researched + built FIRST, ahead of other
  queue items. Adobe's enterprise-tech sector does NOT count against it during
  this window.
- "Qualify" still means the lane — PM/eng/data-science/sales seats stay FAILs.
- Full-board sweep 2026-07-08 found the qualifying set (see runs/ + Resumer
  mail): R164673 (staged), R164546 (bullseye, $165–306K), R168007 (remote-
  flexible), R169720, R169417, R168989.
- Workday CXS search trick: POST {"searchText": q} to
  adobe.wd5.myworkdayjobs.com/wday/cxs/adobe/external_experienced/jobs — clean
  JSON, no browser needed.

## Note doctrine v2 — APP-PAIRED (Jefferson, 2026-07-08 — SUPERSEDES the note-first framing everywhere)

His words: "The sequence is job app goes into the system, within about 24 hours I
follow up with one of these notes saying, 'Hey, I applied for that role, here's
why it resonated well enough for me to find your email and get into your
inbox.' What you've got right now sounds like a pitch — that's noise. I want to
give these people _signal_."

Binding rules:
1. **Notes PAIR with applications.** No application → no note. (A no-app
   exception is Jefferson's explicit per-role call, never the default.)
2. **Sequence: application SUBMITS → ~24h → note.** Never before the submit.
   The old conditional-truth rule ("say 'my application is in' only if true")
   is obsolete — the app-mention is now mandatory and the sequencing makes it
   always true.
3. **The note names the application up front** (role + req id) and says why it
   resonated — the one insight + the one proof point that made him apply. The
   note's job is to pull the reader toward an application already in their
   pipeline, not to open a conversation.
4. **No pitch-CTAs.** Kill meeting asks ("swap notes", "15 minutes",
   "compare notes"). The close points at the application — signal, not ask.
5. Humantic register still shapes tone/length/structure within these rules.
6. Draft notes with a "yesterday" placeholder + a tense-check verify item —
   the send date depends on when the app actually files.

### Doctrine clarification (Jefferson, 2026-07-08 — the Crone kill)
Dead req + no application possible = **KILL the note without asking** ("I don't
know why we're talking about something that's been dead for over a year...
this is an obvious call I can trust you to make"). The org-fit>liveness
calibration is NOT a blanket keep-alive for dead reqs — it fires only when
Jefferson has HIMSELF named the org as on-point (ButterflyMX precedent). Default
for zombie reqs: kill silently; he can always resurrect.

### Sending — permanent clarification (Jefferson, 2026-07-08)
There is NO send mechanism anywhere in this system, and none may ever be built.
The ⏱️ "SEND TRIGGER" callouts on note pages are timing guidance addressed to
JEFFERSON — he is always the final and only sender (his LinkedIn, his email,
his hands). No agent automates, schedules, or fires an outreach message under
any circumstances. Gate 2 is absolute.

### Doctrine v2.1 — the RESERVED FACT (Jefferson, 2026-07-08)
When a fresh, high-signal fact exists that is NOT in the filed application
(embargoed, too new, or negotiation-gated), the note LEADS with it: "I couldn't
include this in the application because [honest reason], but…" The note must
carry at least one thing the ATS doesn't have — that's what makes it signal
instead of a summary. Current reserved fact: the October keynote+workshop for
1,500 hospital leaders (see profile.md — notes only, never app materials,
until the contract signs and Jefferson lifts the embargo).

### Fit calibration — the 50% rule (Jefferson, 2026-07-08, GE Aerospace kill)
"Something like 3 out of six qualifications I don't match. One is one thing,
but 50% is too much." → If Jefferson doesn't substantively match at least half
of a posting's stated qualifications, it is NOT a fit — regardless of how well
the title or theme resonates. Gate + research runs must count the qualification
match explicitly, not just score theme alignment. (Gate had scored GE Aerospace
4/6 PASS; his gut said no — this is exactly the backtest signal the rubric is
tuned against.)

### Run behavior on failed caveats (Jefferson, 2026-07-09 — WWF precedent)
A failed gate-caveat (wrong seat shape, thin AI mandate, etc.) KILLS THE
APPLICATION FRAME, NOT THE RUN. Complete the org/person research anyway and
present the warm-lane alternative WITH the research done ("all the other stuff
should have run"). Only hard pre-filters (comp, eligibility, health-org rule)
stop a run cold.

### Morning job alerts — AUTO-ACTION standing order (Jefferson, 2026-07-09)
"When you find jobs in the morning, just start actioning." Alert-lane roles
(module 45) no longer wait for a 'pull jobs' ask: pull, read the real JDs,
verdict them (lane fit + 50% qualification rule), route qualifying ones into
Catalyst/Resumer, and report outcomes — not options — in the briefing.

### Superhuman Mail MCP — send capability exists, NEVER use it (2026-07-09)
The `superhuman-mail` MCP server (user-scope, `https://mcp.mail.superhuman.com/mcp`)
is installed as Jefferson's compose/read surface. Its toolset includes SENDING
email. Per the standing no-send doctrine above, agents may READ and STAGE DRAFTS
through it — but never call a send tool. Jefferson is the final and only sender,
always. Drafts staged via the Gmail MCP also appear inside Superhuman (same
underlying account), so either staging path is fine.

UPDATE 2026-07-09 (same day): Superhuman's MCP is ONE account per connection, so
three named instances now exist, all pointing at the same URL — `superhuman-mail`
= personal gmail (jefferson.stovall@gmail.com), `superhuman-mail-ct` =
jeffersons@captaintomorrow.io, `superhuman-mail-adv` = jeffersons@adaptiverseapp.com.
The no-send rule above covers ALL instances, present and future.

## Soften the Beach — the warm-up campaign (Overlord, 2026-07-13)

Named for Operation Overlord: soften the beach before the application lands.
Owned by the **Overlord** thread (2026-07-13 fork of The Fixer) — job-search
process, role evaluation/assignment, and this cadence. Seed: Jefferson's 7/12
brainstorm (claude.ai share 93ae9aff — "search the person everywhere except
LinkedIn").

**Per target** (each role Jefferson flags for campaign treatment):
1. **Map the room** — HM + 1–2 flanks (their boss, a team lead, the recruiter)
   via org announcements, case studies, people-search.
2. **Trace sweep, everywhere-but-LinkedIn** — podcasts (Listen Notes),
   YouTube/conference archives, webinars, vendor case studies, trade bylines,
   earnings calls/IR transcripts, association committee rosters, nonprofit
   boards/990s (ProPublica). Output: 2–3 ranked hooks per person — the
   surfaces almost nobody follows up on. (Extends the research subagents:
   person-finder + voice-corpus absorb the sweep.)
3. **Touch 1: one low-ask note** in his voice, Humantic register-tuned, built
   on the best hook — direction-ask (the Arti/Brown&Brown pattern) or
   trace-reference ("minute 34 of that panel"). Staged under the Catalyst
   card; Jefferson sends (gate 2, absolute).
4. **Timed follow-ons** — APP-PAIRED note ~24h post-submit (doctrine v2) →
   value-add artifact ~1 week later (Punchcard issue or a 2-page teardown,
   tier-1s only) → closed-loop on outcome. 7–10 day spacing; every touch
   logged on the card.

**The six lanes (Jefferson's taxonomy, 2026-07-19 — USE THESE NAMES):**
1. **Associations** — activation of his EXISTING association network
   (his correction, 2026-07-19: "I am deeply connected to a huge number of
   associations and haven't been taking advantage of that" — this lane is
   reconnection and activation, NOT cold committee-joining). Execution design
   in progress; anchors: ASAE Annual Aug 15–18 Indianapolis; Laura Brigandi
   (Public Affairs Council) as ecosystem super-node; Beekeeper-era
   association clients; DMAS 2024 keynote audience.
2. **In-Person Networking Events** — symposia/events in the target ecosystem
   (first two: Viva Creative symposium ~wk of 7/20; AI-in-the-arts symposium
   7/18 Hillyer Art Space DC via Josh — temple connection, immersive-
   experience shop leadership, Ford's Theatre background). Names he meets →
   Attio, same as any touch.
3. **Google** — page-one audit of his name; fill gaps via source requests
   (Qwoted / Help a B2B Writer). Once, then quarterly. Every HM notes get
   sent to will search him within a day.
4. **Speaking Engagements** — podcast/webinar/conference guesting AIMED at
   rooms his target orgs attend (Tim Villegas template; the Oct keynote +
   IHA breakouts already are this lane — the gap is aiming it).
5. **Single Shot Apps** — application to a live req, optionally paired with
   HM outreach (APP-PAIRED doctrine v2 above) or notes to several people at
   the org. Catalyst `Play` values: App only / App + HM note / App + org notes.
6. **Org Warm Ups** — multiple messages over time to people in an org with
   NO specific immediately-open role (the Brown & Brown / Arti pattern).
   Catalyst `Play` value: Org play. The multi-touch cadence applies here.

Operating rhythm across lanes: the **Monday warm-touch queue** — the briefing
surfaces touches due this week with drafts ready; Jefferson approves + sends
in one sitting. (Dormant until 3+ targets have touches in flight.)

Scope note: the one-follow-up rule (#7 at top) remains the default for
standard gate notes. This multi-touch cadence applies ONLY to targets
Jefferson explicitly flags for campaign treatment. All other doctrine binds
unchanged: no send mechanism ever, RESERVED-FACT keynote embargo, org-fit >
req liveness, zombie reqs killed silently.

### Tracking (Jefferson, 2026-07-15 — "1 only" + Attio)

- **Catalyst `Play` select** (one value per card, stamped at route/creation):
  `App only` / `App + HM note` / `App + org notes` / `Org play`. Board views
  group by it; gate/briefing modules read it. All open Jefferson-lane cards
  stamped 2026-07-15.
- **Person-side touch ledger = Attio** (his call: "Attio is available for
  tracking"). Every SENT touch → a note on the target's Attio person record
  (create the person if absent: name, title, company, LinkedIn URL). Closed-loop
  and intermediary touches log the same way, labeled in the note text. The
  Monday warm-touch queue reads Attio for last-touch recency.
- **Attio API access (verified 2026-07-15):** token in macOS keychain —
  `security find-generic-password -a jmos -s ATTIO_TOKEN -w` — then
  `POST https://api.attio.com/v2/objects/people/records/query` (and the
  records/notes write endpoints). JMOS `/api/meetings/*` remains the read
  path for call intelligence.
- Deliberately NOT built: a Touches DB or in-card comms-log convention —
  the select + Attio is the whole tracking system unless volume proves more.
