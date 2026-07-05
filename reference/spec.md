# HM-Direct Outreach System v2 — "Surgical Strike"

**Lineage:** Rebuilt July 2026 from the Nov 2024 pain-point outreach prompt (originally job-search, evolved into investor outreach with dossier-based personalization). v2 inverts the 2024 economics: research is now nearly free via agentic deep research, so the scarce resource is *roles worth the treatment* and *human judgment on the send*.

**Core thesis:** In 2026, AI-personalized outreach is table stakes and often reads as spam. The differentiator is (1) verifiable specificity that could not have been templated, (2) brevity, (3) Jefferson's authentic voice. One or two surgical strikes per week beat four decent notes.

**Operating cadence:** Every role that passes the Phase 0 gate gets the full treatment — the gate is the limiter, not a count. If a week produces five qualified roles with warm paths clustering, execute all five. Time budget: agent does the research; Jefferson spends ≤20 min per role on judgment, editing, and sending.

**Morning briefing integration:** Nightly Catalyst sourcing feeds a gate-scoring pass (cheap model, rubric below). The morning briefing surfaces: roles that passed, their gate scores, and any warm-path flags. Jefferson's thumbs-up per role is what triggers Tier 1 research — the system never self-initiates a deep-research run or a send.

> **PARKED — await "go" from Jefferson:** Backtest the Phase 0 gate against the current Catalyst role set. Hypothesis: the gate as written is too strict and is filtering out roles worth the treatment. Do not run this test until explicitly told "go."

---

## Phase 0 — Qualification Gate

**Pre-filters first (any hit = volume machine, no scoring):** comp range max below $125K; equity-in-lieu-of-cash comp; eligibility not easily confirmable; travel >50%. Details in the rubric (companion artifacts file).

Run the gate on survivors. Three criteria — **C1 is mandatory**; pass = C1 YES plus at least one of C2/C3 YES:

1. **C1 — Target-spec fit (mandatory):** Senior AI-transformation leadership at a target-sector org. Gut-level "I'd take this call tomorrow."
2. **C2 — Findable decision-maker:** A plausible hiring manager (not just HR) can likely be identified from public information.
3. **C3 — Real-problem visibility:** The org has public exhaust (strategy docs, 990s, talks, news) rich enough to infer the actual problem behind the posting.

**Warm-path accelerator (not a gate criterion):** If a warm path is *already known* at briefing time (Beekeeper-era, ASAE, cohort, Punchcard, Temple network), the role auto-passes with C1 YES and gets priority-flagged. Warm-path *discovery* for everything else happens in Phase 1C, after the gate — requiring stack knowledge before research has looked for it was an order-of-operations error, fixed 2026-07-04.

If it fails the gate, it goes in the volume machine and nothing more.

---

## Phase 1 — Deep Research (agent-executed)

Run as a deep-research task. Every finding must carry a source link. Output feeds Phase 2.

### 1A. Organization layer
- Strategic plan, annual report, board priorities, recent leadership communications.
- **Form 990 (associations/nonprofits):** revenue trend, staff size, program vs. admin spend, exec compensation, technology line items. This is public, rarely mined, and tells you budget reality — the thing the posting never says.
- Recent news, press releases, leadership changes, funding events.
- **Job-posting cluster analysis:** every other role currently open at the org. Three simultaneous data/AI postings = a transformation initiative; one lonely posting = an experiment or a backfill. The cluster reveals the initiative.
- Conference/webinar footprint: what the org chose to present on in the last 18 months = what leadership believes matters.

### 1B. Posting archaeology
- How long has the role been open? Reposted? Re-leveled? (Wayback Machine, LinkedIn posting dates, Google cache of job boards.)
- Diff the posting language against the org's public strategy. Where the posting is vague but the strategy is specific, the gap is usually the real problem.
- Salary band vs. 990 comp data: is this role scoped realistically? (Informs negotiation later, too.)
- Output: a one-sentence **Real Problem Hypothesis** — falsifiable, source-grounded. *"This role exists because [org] committed to X in its strategic plan, has no one on staff who has shipped X, and the board is asking about it."* If the research can't support a hypothesis this specific, the role fails out of the process here.

### 1C. Person layer — find the actual human
Triangulate the hiring manager (not the recruiter, not HR):
- LinkedIn org-structure mapping: who leads the function this role reports into; who at the org posted, reshared, or commented on the job.
- Who has spoken publicly about the initiative (webinars, ASAE sessions, podcasts, bylines, committee work)?
- Recent hires into adjacent roles — who did they say they report to?
- **Warm-path check (mandatory):** mutual LinkedIn connections, Beekeeper-era overlap, shared association memberships, cohort/Punchcard network. If a warm path exists, the warm intro *replaces or precedes* the cold note — never skip this check.

### 1D. Voice-and-priorities corpus
- Gather the target's own writing/talks: LinkedIn posts, articles, conference sessions, podcast appearances.
- Extract: what they say the problem is (in their words), their register (formal/casual, data-driven/story-driven), their stated frustrations.
- **2026 change from v1:** this corpus calibrates *register and priorities only*. Do NOT mimic their style — style-mimicry by AI is now detectable and repellent. The note is written in Jefferson's voice at the target's preferred altitude and length.

---

## Phase 2 — Synthesis (agent drafts, Jefferson verifies)

Produce a one-page brief:
1. **Real Problem Hypothesis** (one sentence, sourced).
2. **The One Insight:** the single most specific, non-obvious, verifiable thing the research surfaced that connects the org's problem to Jefferson's proof points. Must pass the test: *could this sentence appear in anyone else's outreach?* If yes, dig deeper or kill.
3. **Matched proof point:** ONE item from Jefferson's record (Captain Tomorrow cohort outcomes, Adaptiverse 0-to-1 build, Beekeeper-era association work, agentic-systems work) that most directly answers the hypothesis. One. Not three.
4. **Warm-path recommendation:** intro-first, note-first, or note-plus-parallel-intro.
5. **Channel recommendation:** email (preferred at senior level; find via org domain patterns + verification) vs. LinkedIn.
6. **Source ledger:** every factual claim mapped to a URL. Unverifiable claims are deleted, not softened. A wrong specific is fatal; a missing one is not.
7. **Gaps & Inference Register (brief):** what the research *couldn't* find, and which conclusions rest on inference rather than sources. Tag each load-bearing claim in the Hypothesis and the One Insight as **[sourced]**, **[inferred — from X]**, or **[speculation]**. Inference is the point of this phase; the register just makes visible which levers are being pulled, so Jefferson can judge whether the load-bearing inference is one he'd stand behind in a reply.

---

## Phase 3 — The Note

**Hard constraints:**
- 100–130 words. (Down from 200–300 in v1. Brevity is now a credibility signal.)
- Structure: [Specific observation from research, stated plainly] → [Why it's hard / what it implies — the insight] → [One proof point, one sentence, with a number if honest] → [Soft, specific CTA].
- CTA is a low-friction question, not a meeting request: *"Is [inferred problem] actually the hard part of this role, or am I misreading it?"* Curiosity invites reply; asks invite deletion.

**Anti-slop guardrails (absolute):**
- No flattery openers. Never "I was impressed by," "I've been following," "I came across."
- No "I'm reaching out because." Start with the substance.
- No adjective stacking, no "passionate," no "leverage," no "synergy."
- Every specific claim traces to the source ledger.
- Jefferson's voice: direct, a little dry, builder's vocabulary. Reads like it took ten minutes of thought, not ten seconds of generation — because it did.
- The disclosure paragraph (Adaptiverse side-build) does NOT go in the first note. It's for process conversations, not cold outreach.

**Human gate:** Jefferson edits and sends personally. The agent never sends. Minimum one full read-aloud pass — if any sentence sounds like AI wrote it, rewrite or cut.

---

## Phase 4 — Cadence & Logging

- **Follow-up:** exactly one, 6–8 business days later, and only if it adds new value (a relevant article, a Punchcard-style two-paragraph analysis of their problem, a genuine update). Never "just bumping this." After one follow-up, the thread is closed — the role stays in the volume pipeline regardless.
- **Stacking:** where the association lane touches the same org, sequence deliberately — warm intro or ASAE-opener conversation first, HM note second, application on file throughout.
- **Logging:** one row in the tracker table (name, org, channel, last touch, next action, date). No new views, no dashboard.
- **Review:** after 8–10 sends, look at reply rate before changing anything. No redesigning the system mid-flight.

---

## Pipeline Architecture — Two Tiers, One Handoff

**INTERIM MODE (current):** All tiers run in Fable/Claude for the first 8–10 roles. Research executes as parallel subagent tasks inside one session; each subagent returns the same rigid dossier template, and synthesis happens in the main thread. The template is the internal interface — when/if collection later splits to cheaper platforms, only the collector changes; Phase 2 onward is untouched. Split decision deferred until real reply-rate data exists.

**Tier 1 — Collection (interim: Fable subagents; later, possibly GPT deep research, Manus, etc.):** Runs Phase 1 (a)–(d) per role. Output must conform to a rigid dossier template: every finding as `[finding] — [URL] — [collector's confidence: high/med/low]`. No synthesis, no recommendations — collection only. One research run per role (or two: org+posting, person+voice) with the template embedded in the prompt.

**Boundary rule (where quality is enforced):** Any Tier 1 finding without a working URL is discarded at intake, not carried forward. Cheap-tier hallucination risk lives here, so the source ledger is enforced at the handoff, before synthesis ever sees the material.

**Tier 2 — Synthesis (Fable/Claude):** Takes the structured dossier(s), spot-checks 2–3 load-bearing citations, then runs Phases 2–3: hypothesis, One Insight, Gaps & Inference Register, note draft. One clear output per role.

**Anti-complexity rules:**
- The interface between tiers is a markdown template, not an integration. Manual paste is the orchestration layer until volume proves otherwise.
- No new tooling until 8–10 roles have flowed through by hand and the friction points are known.
- The morning briefing's thumbs-up is the only trigger for Tier 1; Jefferson's send is the only trigger for outreach. Two human gates, everything else automated between them.

---

## Runnable Prompt (paste into a deep-research-capable Claude session or Project)

> You are running Phase 1–3 of my HM-Direct Outreach System v2. Inputs: [JOB POSTING URL/TEXT] and my background summary [attach resume/profile].
>
> **Phase 1 — Research (use web search extensively; cite every finding):**
> (a) Org layer: strategic plan, annual report, recent news, leadership priorities. If a nonprofit/association, pull the most recent Form 990 (ProPublica Nonprofit Explorer) and summarize revenue trend, staff size, and any technology-relevant spend. List ALL other currently open roles at the org and infer what initiative the cluster implies.
> (b) Posting archaeology: how long open, any reposts or re-leveling, and where the posting's vague language diverges from the org's specific public strategy.
> (c) Person layer: identify the most likely hiring manager with evidence (org structure, who posted/commented on the job, who speaks publicly about this initiative). Check for warm paths against my network context.
> (d) Voice corpus: find the likely HM's recent writing/talks; summarize their stated priorities and register. Do not plan to mimic their style.
>
> **Phase 2 — Synthesis:** Produce the one-page brief: Real Problem Hypothesis (one falsifiable sentence), The One Insight (must fail the "could anyone else have written this?" test), one matched proof point from my background, warm-path and channel recommendations, a source ledger mapping every claim to a URL, and a brief Gaps & Inference Register — what you couldn't find, plus each load-bearing claim tagged [sourced], [inferred — from X], or [speculation]. Flag anything you could not verify.
>
> **Phase 3 — Draft:** Write the note at 100–130 words following the structure and anti-slop guardrails: no flattery openers, substance-first, one proof point, soft question CTA, my voice. Then write the one permitted follow-up (value-add version). Mark any sentence whose factual content isn't in the source ledger.
>
> Do not send anything. End by listing the top 2 uncertainties a human should verify before sending.

---

## What changed from v1 (Nov 2024), for the record

| | v1 (2024) | v2 (2026) |
|---|---|---|
| Research | Manual dossier assembly | Agentic deep research; human verifies |
| Volume | Template for many | Qualification-gated, no count cap |
| Personalization | Style-mimicry from writing samples | Register-matching only; Jefferson's voice |
| Length | 200–300 words | 100–130 words |
| Edge | Personalization | Verifiable specificity + brevity + judgment |
| New veins | — | Form 990s, posting archaeology, job-cluster analysis, warm-path-first check |
| Follow-up | 2–3 follow-ups | Exactly one, value-add only |
