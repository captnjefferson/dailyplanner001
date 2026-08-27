# The Org Awareness Play

**What it is.** A repeatable research-and-action sequence for any organization that (a) looks like it's scaling and (b) has, or plausibly will have, a role Jefferson wants. It ends in a short action list he can execute from, plus a set of watches that keep the play running without anyone re-deciding anything.

**Jefferson's framing (2026-08-20, when he ratified it):** *"We're doing this to get a job. This is a play we'll run any org like Tenex — where it looks like they're scaling up and might have a good role."* This is a job-getting motion. Not networking, not brand-building. Designed on the Tenex run, 2026-08-19/20.

**Where it sits:** this is lane 6 of the six-lane taxonomy in `../CLAUDE.md` ("Org Warm Ups") made concrete, and it composes with lane 5 (Single Shot Apps) when a live req exists.

**Why it works — his own data.** His highest-reach post ever was a reply *into someone else's live conversation* (3,286 impressions), versus 277 for his own follow-up five days later. His published originals otherwise run 130–970 impressions. His own results tracking already concluded **reach, not content quality, is the bottleneck** — and a paid speaking engagement (IHA) arrived inbound off published writing. Joining an existing thread is his single highest-leverage move by roughly an order of magnitude. The play is built on that fact.

---

## THE PRIME DIRECTIVE: verify from primary sources

The Tenex run produced **three retractions** — claims relayed from an agent's summary that turned out to be unsupported, one of which became the centerpiece of a plan for several hours. Jefferson caught all three by asking "what's the source?"

**Rules, non-negotiable:**

1. **An agent's summary is a lead, not a fact.** Before any claim becomes load-bearing — before it shapes a plan, a timeline, or a recommendation — open the primary source and read it.
2. **A web-search result summary is not a primary source.** It is a paraphrase of a paraphrase. Two claims died on this in one day.
3. **Never dress an inference as a finding.** "They're hiring creators" → "they're starving for material" is an inference. Label it or drop it.
4. **State coverage bounds unprompted** — what was read, what couldn't be reached, what remains unverified. Every deliverable, every time.
5. **When a source can't be read, say so.** X/Twitter returns HTTP 402 to fetchers and every mirror is CAPTCHA-walled; LinkedIn is login-walled to agents without Chrome. Those are reportable gaps, not things to route around with inference.
6. **A retraction is a good outcome.** Say it plainly, early, and without cushioning. Then say what's true instead.

---

## PHASE 0 — Run every phase. A gate narrows what you DO, never what you LOOK AT.

**This rule exists because the procedure was violated on its first use.** On the One Call run, the domain gate came back "healthcare — C1 fail for outreach." That conclusion was allowed to cascade: since the outreach lane was closed, the whole non-comment surfaces bucket (Phase 5's "now, ~20 minutes" actions — communities, events, subscriptions) was silently dropped as if it were part of the same question. It wasn't. The gate blocks *drafted outreach and relationship asks*; it says nothing about attending a public webinar or subscribing to a newsletter. An entire phase went unrun and the output shipped anyway.

**The rule:**

> **Run every phase to completion and report what it found. Gates and judgment apply to the OUTPUT — what to recommend, what to skip, how far to keep digging — never to whether the phase runs at all.**

Jefferson's words, ruling on it (2026-08-20): *"You are to follow the instructions. The judgement gets applied in the outputs and the decisions around how far to keep digging."*

**The failure shape to watch for:** reaching a conclusion and then stopping the gathering. It is the same mechanism behind the three retractions on the Tenex run — an early conclusion ("they're starving for material," "there's no awareness lane here") became the thing the plan was built on, in place of what was actually there. **A conclusion is a reason to keep checking, not a reason to stop.**

Phase 0 itself: check the domain gate against `rubric.md` up front — a health-focused org at senior level is a C1 fail for **outreach only**, and **the application is unaffected**. Record the gate result and carry it to the output stage. Then run Phases 1–6 regardless.

## PHASE 1 — Who publishes, and what

Goal: know who to aim at, and where they actually live.

- Start from the org's LinkedIn People tab and its leadership page. Identify everyone who plausibly touches the target role: the function's leaders, the likely hiring manager, any named recruiter, and anyone whose title matches the candidate's own lane.
- **For each, read their actual feed** — via Jefferson's logged-in Chrome, read-only. `linkedin.com/in/<slug>/` and scroll ~10 ticks before reading; the profile page is more reliable than `/recent-activity/all/` for text extraction.
- Capture per person: observed cadence, 3–5 recurring themes with a dated example each, register, engagement gradient (what lands vs. what dies), and **whether they reply to strangers**.
- **The reply behavior is the most decision-relevant fact you will collect.** Someone who posts constantly but never answers a comment is a visibility surface. Someone with modest reach who answers everyone by name is a door. On the Tenex run, the founder with 217K followers replied to nobody; the enablement manager with 10K replied to almost everyone. The second person was worth ten of the first.
- **"Nobody publishes" is a valid finding**, not a failed search. Say it, then find where the org's conversation actually happens instead — company page, trade press, conference stages, industry associations, podcasts.

### ⚠️ Phase 1's person research IS the Individual Discovery process — read it before running (wired 2026-08-26)

**Canonical doc (v1.0, rebuilt 2026-08-26 after a full red team):** [Individual Discovery and Ambient Positioning](https://www.notion.so/3c8164c1810d804d8e9bd4de60c4ddca) — Notion page id `3c8164c1-810d-804d-8e9b-d4de60c4ddca`. Version-controlled mirror: `~/Sites/hm-outreach/reference/individual-discovery-process.md` (edit there, push to Notion). It is **self-contained** — every recipe it needs is in its own Ops appendix; it needs no companion files.

⚠️ The old page `3c7164c1-810d-8118-ab1f-cf3cd5c9e38d` is DEPRECATED and kept only for run history. Do not run from it — its layer definitions are pre-v1.0.

Its two inputs live on disk and are named in its run-input block: `reference/corpus-inventory-2026-08-26.md` (Jefferson's themes and backing pieces) and `reference/territory-terms.md` (the Layer 5b search list). Memory pointer: `reference_individual_discovery_process.md`.

Designed with Jefferson 2026-08-25, proven end-to-end on Tenex the same day. The bullets above are the SUBSET that fit this file; the canonical doc is the process. Per person on an org play: **Layers 1–3 for everyone on the roster** (identity resolution → publishing map → consumption + register), **Layer 4 (circles/orbit) once promoted to an active play**, **Layer 5/5b synthesis to Attio incl. the openings analysis (OCCUPIED / PEER / OPEN / VOID) — the actual deliverable.** Its tooling reference (Substack profile API, Interests-tab extraction, citation mining + the diagnostic ratio, Maigret — permanent install at `tools/venv-maigret/`), ethics/detectability ladder, reach-per-follower rule, and touch catalogue all bind here.

Origin of this wiring: the 2026-08-26 Parexel run executed this file's Phase 1 WITHOUT the discovery process — even though that doc's own to-do had named Parexel as run 2, Layer-0-first, on hold until settled. Two docs, no cross-reference, work lost to the seam. Never again: **a run that hasn't fetched the discovery doc hasn't run Phase 1.**

Operational rules from run 1 that bind every run: **one browser tab per agent lane** (a parallel agent navigated the logged-in LinkedIn session away mid-run and got stranded); **per-claim provenance inline** on everything written to the research record; **an application-gated workshop/community that shares its roster with a second target org is the highest-value touch available — look for these deliberately.**

**Never infer cadence or themes from a job title.**

## PHASE 2 — Match to his existing corpus

He has a large body of written work, much of it unpublished but fully drafted. The play uses what exists rather than commissioning new writing.

- Inventory sources: Notion **Content Pipeline** DB `37c164c1810d819b8859dc67fc6b5601` (the live editorial funnel), the **Thought Leadership hub** `37c164c1810d81949147e9adaa17f2e5`, his LinkedIn Articles archive and activity feed, local markdown under `~/Sites` (`Content_Creation/`, `punchcard/`, `docent/gtm/`, root-level strategy docs), and the memory files `resume-positioning-facts.md` and `project_thought_leadership_pipeline.md`. **The Atomic Notes DB is operational only — no essay content. Skip it.**
- Group by theme, not by source. Mark each piece PUBLISHED (where/when) or DRAFT.
- **A fully-sourced draft answers "I wrote about exactly this" as well as a published piece does** — for a comment, it's the argument that matters, not the URL.
- Then match: their recurring themes × his pieces. A real match is one where **he knows something the author doesn't**, not one where the topics merely overlap.

**The move that works (his highest-reach post, and the pattern to repeat): take an argument they've made at the individual level and move it to the organizational altitude.** He has the receipts; they usually have the assertion.

## PHASE 3 — Measure cadence

Observed post counts over a real window, per person. This sets the whole timeline.

- **High-cadence group** (someone posting daily, several posting weekly): plenty of surface, so the *req* sets the clock, not them.
- **Low-cadence group**: surfaces are scarce; compress the awareness window and lean on non-comment actions (events, communities, newsletters).

## PHASE 4 — Verify the req from primary source

**Never build a timeline on a job aggregator or on another agent's summary of a JD.**

- Find the org's own ATS and read the posting there. Ashby exposes a clean public API (`api.ashbyhq.com/posting-api/job-board/<org>?includeCompensation=true`) plus a public GraphQL endpoint that returns **the application form's field definitions** — read those; the screening questions are where the real gates live. Workday's CXS search endpoint takes a POST with `{"searchText": q}`. Greenhouse and Lever have public JSON boards.
- Capture verbatim: location text, remote/hybrid/onsite policy, reporting line, travel, comp (or its absence), required years, and **every screening question with its exact answer options**.
- **Read the dropdowns.** On the Tenex run the binding constraint wasn't in the JD prose — it was that the in-office question offered exactly three options and none of them was "hybrid." That single field was more decision-relevant than the entire job description.
- **Diff the JDs across a family of similar reqs.** Ten Tenex strategist postings turned out to be byte-identical except one line; the "Enablement" specialization existed only in the title. Hashing them killed a "purest match ever" claim in one step.
- Check repost history on aggregators. A req that reposts quarterly is evergreen and behaves differently from a fresh one.

## PHASE 5 — The output

Two surfaces, and the split matters:

**The org's Catalyst card = the research record.** Everything goes here — dossier, people map, corpus match, req analysis, corrections, coverage bounds. Append; never delete. Corrections go in as new, clearly-labeled blocks that name what was wrong, so the reasoning stays auditable. Put a **START HERE index** at the top of the card so it stays navigable as it grows.

**The weekly note = his action surface.** Only what he does, with minimal but sufficient context per item: the action, the link, and *why*. No research, no reasoning chains, no background. He works from the weekly note; the card is what he opens when he wants the detail.

The action list itself is always the same four sections:

1. **Now, ~20 minutes** — the low-friction, high-value actions: apply to a community, RSVP an event, subscribe to their newsletter. These vary the most by org and are usually the best return per minute.
2. **This week — comments, which HE writes.** Fixer supplies the *angle* plus which of his own pieces backs it. Never the prose.
3. **Fixer's lane** — application essays, drafted for his edit.
4. **The dates** — awareness window, submit date, maintain period, kill trigger.

## PHASE 6 — Post-research actions (the part that makes it ongoing)

Research without these is a document, not a play. Execute every one before declaring the play running.

1. **Add the targets to the LinkedIn people-watch** — `Context_Engineering/skills/briefing/state/linkedin-watch.txt`, one per line as `Name | https://www.linkedin.com/in/slug/`. Group them under a `#` comment naming the org and the date added, and **write the review date into that comment** so the kill decision has a home. Module `55-linkedin-posts` surfaces new posts daily in the morning briefing.
2. **Put every dated commitment on the deferred list** — `Context_Engineering/skills/briefing/state/deferred.txt`, format `YYYY-MM-DD | item | context`. Module `27-decisions-waiting` renders dated items as "⏰ Back today" on the day and collapses everything else to a single count line, so nothing nags. At minimum: the day-7 review, the submit date, and any event date.
3. **Update the Catalyst card** — Stage, `Next Touch`, and a provenance note in `Amount` recording who created the play and why.
4. **Set the kill rule explicitly, with a date.** ~4 comments with zero engagement from anyone means the room isn't reading: change surface or park. Write the review date down; a kill rule with no date never fires.
5. **Confirm the watch actually fires.** Module 55 needs Chrome connected and skips loudly when it isn't. A watch nobody verified is not a watch.

**Measure both** profile views (which names the person) **and** comment engagement. Profile views are the truer awareness signal; replies are the relationship signal.

---

## The timing model (his rules, verbatim in substance)

- **Frequent posters + a fresh posting** → roughly 2–3 weeks of room. Watch ~7 business days, post 3–4 comments, then submit and message a couple of them — especially anyone who replied.
- **An old posting and/or infrequent posters** → 24–48 hours after the comments, then submit.
- **Interest level turns the cadence dial down, never to zero.** *"We don't stop."*
- **Spread comments across 2–3 people, about one per person per week.** Four comments on one person in a week reads wrong.

**RTO mandates do not gate the play.** His ruling: *"I don't care. RTO mandates are their problem, not mine."* A five-day in-office requirement is not a reason to skip an application. The geography kill line is real distance — NYC works (he'll take the train), San Francisco does not.

**Domain gate, from the rubric:** a health-focused org at senior level is a C1 fail for **outreach** (domain mismatch) — but **the application is unaffected**. On a healthcare-adjacent org, run the application lane and check the outreach lane against `rubric.md` before drafting anything.

---

## Division of labor (fixed)

| Work | Owner |
|---|---|
| Research, verification, coverage bounds | Fixer |
| Comment **angles** + which of his pieces backs each | Fixer |
| Comment **prose** | **Jefferson** — never drafted for him |
| Application essays | Fixer drafts, Jefferson edits |
| Every send: comments, messages, applications, RSVPs | **Jefferson, always** |

**On the comment→message escalation:** he is explicit that it's fine for the play to be visible. *"It is! If they see what my play is, more respect to them."* And he will message people who never replied — *"more often than not, they've read my comments."* Do not hedge this step, do not make it coy, do not add a gate that he didn't ask for.

---

## How to report to him (binding)

- **Chat is the receipt. The detail lives on the page.** Never paste a research dump into chat.
- **Bullets, skimmable, short.** He has asked for this repeatedly and it is a real preference, not a mood.
- **His language, not invented vocabulary.** No coined terms, no jargon, no shorthand he'd have to decode. If a phrase would make him ask "what do you mean by that?" — like "unlocks JJ Englert" did — it was the wrong phrase.
- **Only the most relevant.** Not everything found; what changes what he does next.
- **Lead with what changed.** If a prior claim was wrong, that goes first, plainly.
- **Never assert a checkable negative** — go read the data.
- Deep dives happen when he asks for one, and only then.

---

## Worked example — Tenex, 2026-08-19/20 (the reference implementation)

Use this as the template for what "done" looks like.

**Artifacts produced**
- Research record: the Tenex org-play Catalyst card, with a START HERE index + auto table of contents at the top and every phase appended below in order, corrections included as labeled blocks.
- Action surface: a `🎯 Tenex — your actions` section on that week's prep note — today / this week / next week / submit / after, each item a checkbox carrying the link and one line of *why*.
- Watches: three people added to `linkedin-watch.txt` under a dated comment block that names the **9/10 kill-review date**.
- Deferred entries: the 8/28 event, the ~9/1 submit, the 9/10 kill review.
- Catalyst card properties: `Next Touch` set to the next real action, `Play` = Org play, and a bracketed provenance note in `Amount` recording what was set up and when.

**What the research actually changed**
- The starting dossier said "zero warm paths." His logged-in LinkedIn showed five 2nd-degree routes. **Guest-view research systematically understates the warm graph — always re-check logged in.**
- The dossier called one req "his purest JD match ever." Hashing all ten sibling JDs showed they were byte-identical except a years-of-experience line; the specialization existed only in the title.
- The binding constraint turned out to live in an application-form dropdown, not in any job description.
- The best target was not either founder. It was the manager two levels down whose title matched his lane and who answers strangers.

**Three retractions, and what caused each**
1. "The newsletter is scaling 1x→3x/week" — relayed from a web-search summary, never confirmed primary. Their own site says weekly; the archive confirms weekly.
2. "They're publicly starving for material" — an inference from "they're hiring creators," presented as their statement. No such solicitation exists anywhere.
3. "There's an open application for a new show" — relayed from an agent without checking; the named page is a plain newsletter signup with no form, and the post wasn't in the founder's visible feed.

All three were caught by Jefferson asking for the source. **Assume he will ask. Have the source before he does.**

---

## Second worked example — One Call, 2026-08-20 (the fast variant)

Run the same six phases and you can land somewhere completely different. One Call produced the **opposite** timeline from Tenex, and the reason generalizes.

**What Phase 1/4 turned up:**
- The req's "Silver Spring, MD" location was **LinkedIn showing Jefferson his own city.** Their ATS said Remote/United States; the logged-out LinkedIn view agreed. **Always check the location against the org's own ATS — LinkedIn geo-personalizes the display.**
- The org is healthcare by its own self-description, which under `rubric.md` is a **C1 fail for outreach** at senior level.

**⚠️ CORRECTED — this section originally taught the wrong lesson.** The first draft concluded that a closed outreach lane plus a fresh req plus heavy applicant volume meant "submit immediately, speed is the only lever." It also argued awareness should come *after* the application at One Call, on the theory that a parser screens the first pass and the people who publish aren't the screeners.

**Jefferson overruled both, and the ruling is the doctrine:**

> *"I want people to become aware of me before the app submits. Even if it's not people on the hiring team, people on the adjacent AI team hearing about me is immensely positive."*

**Awareness precedes the application. Always. There is no org-shaped exception.** The value of being known is not limited to the people who read the résumé — an adjacent team knowing the name is worth having on its own, and it compounds at the interview stage. Do not re-derive the inversion; it has been ruled on.

**What the domain gate actually does:** it blocks drafted outreach and relationship asks — nothing more. It does not close the awareness play, it does not license skipping Phase 5's non-comment surfaces, and it does not move the submit date earlier. Cadence sets the window; the gate only shapes which *kinds* of awareness are permitted.

**What cadence does here:** where the individuals post infrequently, a long window buys no new surface — comment on what is already up, then submit 24–48 hours later. Days, not weeks. That is compression driven by cadence, which is his rule, not compression driven by a gate, which is not.

**Other reusable technique from this run:**
- **Diff sibling reqs posted the same day.** Two Senior Director seats posted on one date, same salary band, same VP, revealed a funded org build-out — context no single JD carried.
- **Search the org's coined phrases.** "AI-for-Operators" returned zero hits anywhere on the indexed web, which is how the run established the req was genuinely new rather than an evergreen repost.
- **Name the unnamed.** When the hiring manager can't be found in any public source, report "not found" — never a plausible guess. Data-broker results (RocketReach / ZoomInfo / LeadIQ class) are not sources; on this run one broker-supplied name directly contradicted a press-release-verified one.
- **When no recruiter is named and volume is high**, first-pass screening is parser-driven. The résumé has to carry the JD's own vocabulary. That's a concrete action item, not a caveat.

---

## Tooling

**→ `research-tooling.md`** — the complete pass over `jivoi/awesome-osint` (74 sections, ~1,450 entries, maintenance verified on 101 repos), organized by need and scored on a **detectability** rubric: can the target or company tell he used this, and by what mechanism.

**Jefferson's standing instruction (2026-08-20):** *"Add to your rubric: is there any way to tell how I get the information? Then give me everything and I'll make the ethical calls."* **Do not pre-filter tooling on ethics.** Report what exists, classify how detectable it is and why, and let him decide. The first pass at this was pre-filtered and also missed the single most relevant section in the file (Web Monitoring, including Google Alerts) — being judgmental cost coverage.

Two counterintuitive results worth carrying: **the least detectable category is the most damaging** (breach brokers are invisible to the target, but the provenance can never be explained), and **hosted tools beat self-hosted on detectability** (a vendor's IP does the polling instead of his residential one, where a fixed interval becomes a signature).
