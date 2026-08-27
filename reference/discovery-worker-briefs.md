# Discovery worker briefs — the dispatchable execution layer

> ## ⛔ SUPERSEDED 2026-08-26 — do not run from this file
>
> The canonical process is now **[Individual Discovery and Ambient Positioning](https://www.notion.so/3c8164c1810d804d8e9bd4de60c4ddca)** (v1.0), mirrored at `~/Sites/hm-outreach/reference/individual-discovery-process.md`. It is self-contained: each layer carries its own numbered sub-steps, output contract, and recipes, so the orchestrator dispatches a worker by handing it that layer's section verbatim. There is no separate dispatch layer any more.
>
> This file is kept for the model-split rationale below and for historical reference. **Everything operational in it is pre-v1.0 and may contradict the canonical doc** — notably the ledger schema, the Maigret command (which lacked `--no-recursion` and scattered reports into the repo), and the absence of an INCOMPLETE run state. Two documents that can drift is the exact failure this consolidation was built to end.

**Model policy (the honest split):**
- **Sonnet-ready workers (this file):** Layers 1, 2, 3a, 3b-mechanics, 3c, 4-enumeration, Phase-4 req verification, trace sweep. These are recipes + counting + structured extraction. Dispatch with `model: "sonnet"`.
- **Reserved for the Fable orchestrator (NOT worker briefs — see the last section):** Layer 0 frame, Layer 5b openings analysis, corpus match, touch-angle selection, and the final go/no-go on any disambiguation a worker flags. Judgment and taste, not recipes.
- **Adversarial verifier:** dispatch at Sonnet for mechanical claims, Fable for a load-bearing synthesis claim.

**Orchestration / concurrency (run-1 defect: parallel agents collided on the one logged-in browser):**
- **OPEN-WEB briefs (1, 4, 6, 7)** touch only public HTTP / APIs / Maigret — **parallelizable freely**, dispatch as many at once as there are targets.
- **BROWSER-LANE briefs (2, 3-LinkedIn/X parts, 5)** need Jefferson's logged-in Chrome (LinkedIn fully walled; X 402s every fetcher). **ONE browser worker, serial — never two on the same tab.** In practice the orchestrator either runs the browser lane itself or dispatches exactly one dedicated browser worker for all browser-lane layers of all targets in sequence.

**Universal rules — every brief below inherits these; do not restate, do not violate:**
1. **Per-claim provenance, inline.** Every fact in your output carries its source: the URL, or the exact API/tool call. Unsourced material is verified before writing or goes in a clearly-marked `UNVERIFIED` block. (Run-1 lesson: a bulk transfer with no provenance made one retraction cost an hour instead of ten minutes.)
2. **Disambiguation gate — 2+ biographical anchors before accepting ANY account as the target.** Anchor on: current employer, prior employer, city, school, exact title, a named collaborator. One anchor is a lead, not a match. Same-name collisions are the #1 failure mode (three near-misses on 8/26 alone). If you cannot clear the gate, report the candidate as `UNVERIFIED — needs orchestrator ruling`, never as fact.
3. **Nulls are findings, stated plainly.** "Zero across N checked" is a deliverable; "couldn't find any" is not. Run the explicit check and report the count.
4. **Coverage bounds, always.** End every output with what you read, what was walled/unreachable, what remains unverified.
5. **Your final message IS the deliverable** — return the OUTPUT CONTRACT as structured data, nothing else. No preamble, no meta-commentary.
6. **Browser-return guard:** the browser tool blocks returns containing 16+ char alphanumeric runs. Strip URLs and long tokens from anything you return from a browser call, or the call comes back blocked.
7. **Late ≠ dead, but claimed ≠ done.** Never claim a step ran that you cannot show output for.
8. **No silent skips — the RUN LEDGER is mandatory, WITH check-quality.** Every worker output ends with a `run_ledger`: one row per step/sub-layer, each marked `RAN-FOUND` / `RAN-NULL (count)` / `NOT-RUN (reason)` **AND a check-quality tag: `VERIFIED` (primary source / logged-in), `SEARCH-ONLY` (a search snippet, not the source itself), `DEFERRED` (punted to another lane), or `WALLED` (couldn't reach).** A `NOT-RUN` in a delivered result is unfinished work, not a finding. **A `SEARCH-ONLY` or `DEFERRED` null is SOFT — it may NEVER be reported to the human as a clean pass; either upgrade it to VERIFIED or name it as soft in the report.** This clause exists because on 2026-08-26 an X/Twitter check was deferred by one worker and search-only by another, then collapsed into a clean "✅ off-LinkedIn ~zero" in the summary — hiding that the reliable logged-in check (his following/likes) had never run. For login-walled platforms (X, LinkedIn) VERIFIED means the authenticated browser session, which is the only reliable route.

---

## ⛔ RUN LEDGER + COMPLETENESS GATE — model-independent enforcement (READ BEFORE DISPATCHING ANY RUN)

This section exists because the process kept getting run inconsistently — layers silently dropped, outputs buried — and the failure was always "the model didn't choose to be thorough." Thoroughness is now mechanical, not a disposition.

**1. Todos-first (orchestrator, before any dispatch).** Enumerate one tracked todo PER LAYER PER TARGET before work starts (composes with [[follow-the-steps]]). For each person: Layer 1, Layer 2, Layer 3a, Layer 3b, Layer 3c, Layer 4 (if active play), Layer 5/5b. No layer is optional at the "did it run" level — depth/judgment applies to how far you dig, NEVER to whether the layer runs. A run with an un-checked todo is not done.

**2. Every worker returns a `run_ledger`** (universal rule 8). The orchestrator reads it. A `NOT-RUN` row is not accepted as complete — either it re-runs, or it is escalated to the human as an explicit named gap ("Layer 3c not run because X — want it?"), never left silent.

**3. Completeness gate (orchestrator, before writing to Attio/card OR reporting done).** You may not declare a discovery run complete, write the synthesis, or tell the human it's done until: every enumerated todo is checked; every worker ledger shows RAN (found or null-with-count) for every layer; and the REPORT CONTRACT below is filled. If any layer is genuinely un-runnable (walled), it appears in the report as a NAMED gap, not an omission.

## 📤 REPORT CONTRACT — what the human receives, fixed sections, none optional

A discovery run is reported to Jefferson in THESE sections, in this order, every time. A section with nothing in it says so explicitly ("no individual voices followed — itself a finding") — it is never dropped. This is what stops the "I had to ask three times" failure: consumption is a headline, not a footnote buried in the dossier.

1. **Who + what they publish** — cadence, themes, and **REPLY BEHAVIOR (door / billboard)**.
2. **WHERE they read** — subscriptions/newsletters, communities, platforms. Explicit nulls (no Substack, etc.).
3. **WHO they read** — individual voices followed (or the finding that they follow none), plus who they engage/react to.
4. **Circle / inroads** — reachable people, mutuals (real vs brief), orbit direction.
5. **Openings (5b)** — OCCUPIED / PEER / OPEN / VOID + the corpus-match angles.
6. **Gaps + coverage bounds** — every NOT-RUN or walled layer named here, never omitted.

Sections 2 and 3 (consumption) are load-bearing and have been dropped before — they are as mandatory as section 1.

---

## WORKER BRIEF 1 — Identity resolution  (OPEN-WEB · Sonnet)

**ROLE:** Resolve one named person to their real home platforms. You are given a name and biographical anchors; return their verified accounts.

**INPUT:** `{name, current_org, prior_orgs[], city, school, title, known_urls[]}`

**TOOLS + EXACT RECIPES:**
- Email-first: work emails are guessable (org patterns) and often already published — conference bios, papers, WHOIS/Wayback. Self-owned addresses (personal domain) survive job changes and are higher-value than employer-pattern guesses (which stay UNVERIFIED — never assert an aggregator's guess as fact).
- Maigret (permanent install): `~/Sites/hm-outreach/tools/venv-maigret/bin/maigret <username> --json simple --no-progressbar`. Generate candidate handles first: `first.last`, `flast`, `firstlast`, `firstl`, + year variants; sweep all. Saturates on bot-protection at ~7% of sites — partial coverage by design; report it.
- Distinctive-phrase search: quote-search an odd verbatim line from their bio across the web — people paste the same bio everywhere.
- **Show-notes / speaker-bio bridge (HIGHEST-YIELD SINGLE STEP — run it even if identity is already resolved):** podcast + conference pages link everything a person owns. Podcast RSS carries `itunes:email` (their real address, often self-owned). Do this.
- Gravatar by email-hash: cheap, low yield (run-1: 34 addrs → 1 hit, a collision). Try, don't lean on it.
- Reverse image search: agents cannot upload — SKIP, mark manual.
- Second, work-only account: ALWAYS sweep for one (run-1 found a hidden work GitHub holding client demo repos). Creator and employer identities routinely split.

**METHOD:** candidate handles → Maigret sweep → distinctive-phrase → show-notes bridge → second-account sweep → clear each candidate through the 2-anchor gate.

**OUTPUT CONTRACT:**
```
{ target: name,
  accounts: [ {platform, handle, url, status: verified|UNVERIFIED, anchors_cleared: [...]} ],
  emails: [ {address, source, status} ],
  bio_drift: [ {platform, self_description, staleness_signal} ],   // a bio naming a former employer dates their pivot
  nulls: [ "platforms checked, not present" ],
  coverage_bounds: "..." }
```

**STOP-RULE:** once you have their 2–3 real home platforms, stop. You need where they live, not every account.
**SELF-CHECK before returning:** every account cleared the 2-anchor gate OR is marked UNVERIFIED · Maigret coverage % stated · second-account sweep run · show-notes bridge run.

---

## WORKER BRIEF 2 — Publishing map  (BROWSER-LANE · Sonnet, serial)

**ROLE:** Map where one person PUTS content and how it performs. Read their feeds in the logged-in browser.

**INPUT:** `{name, verified_accounts[] from Brief 1}`

**TOOLS + RECIPES:**
- LinkedIn: `/in/{slug}/` (profile-page feed is more reliable for text than `/recent-activity/all/`); scroll ~10 ticks before reading. `get_page_text`.
- X (if a verified account exists + logged in): profile + `/with_replies`.
- Cadence = real post counts over a real window (last ~30–60 days). Dead channels: record LAST-ACTIVITY DATE (the graveyard dates their pivot and tells you which surfaces to skip).
- Engagement gradient with NUMBERS AND A RULE: not "personal posts do well" but "personal/frontier takes run X–Y reactions; tutorials/recruiting sit at the Z floor." The rule sets the register to write in.
- **Reply behavior = THE most decision-relevant fact.** Open their last ~5–10 post threads: do they answer strangers, or only their own circle? A billboard (never replies) vs a door (replies by name) changes everything.
- Format effects (a "guide" format going nuclear vs the same person's article format dying).
- Org-level channels alongside the person's (an org newsletter can dwarf every individual — find the byline).
- "Nobody publishes" is valid → then find where the org's conversation happens (company page, trade press, stages, associations).

**OUTPUT CONTRACT:**
```
{ target, platforms_live: [{platform, cadence, last_active}], platforms_dead: [{platform, last_active}],
  themes: [{theme, dated_example, url}],   // 3-5
  engagement_gradient: "numeric rule",
  reply_behavior: {verdict: door|billboard|mixed, evidence: "N of last M posts had author replies to strangers", url},
  appearances: [{what, where, date, topic, register, url}],   // 2-4 sentences each — half the corpus-match work, free
  org_channels: [{channel, scale, byline}],
  coverage_bounds }
```
**STOP-RULE:** enough to characterize cadence + themes + reply behavior; don't transcribe the whole feed.
**SELF-CHECK:** reply behavior established from ACTUAL threads (not inferred) · engagement stated as numbers · dead channels dated.

---

## WORKER BRIEF 3 — Consumption + register  (BROWSER-LANE for LinkedIn/X · Substack part is OPEN-WEB · Sonnet)

**ROLE:** Find where one person READS. Run 3a FIRST (hard data), then 3b, then 3c.

**INPUT:** `{name, verified_accounts[]}`

**3a — platforms that leak subscriptions (do first):**
- **Substack public profile API (best consumption tool, INVISIBLE, no auth):** `GET https://substack.com/api/v1/user/{SLUG}/public_profile` — use the SLUG, the numeric-id form 404s. Returns their actual subscription list.
- **LinkedIn Interests tab (browser):** `/in/{slug}/details/interests/` — tabs for Top Voices / Companies / Groups / Newsletters / Schools. Extraction note: the li selectors break here; read `document.body.innerText` and slice from the tab labels.
- **X following + likes (browser, logged in):** the likes tab is literally a reading log.
- **GitHub stars/following (free API):** great for engineers, dead end for most (run-1: zero across all three). 30-second check, report the null.
- Also fast-check when they exist: Goodreads, Letterboxd, public Spotify, Reddit comment history.

**3b — citation mining (see Brief 4 — dispatch it separately for depth; here just note whether their corpus is worth mining).**

**3c — communities are often the real media:** enumerate every Discord / Subreddit / Slack / private community the target names anywhere in their corpus. Run-1's biggest surprise: all targets lived in communities, not newsletters. Being in the room beats being in the inbox.

**⚠️ The comment-proxy caveat:** inward-facing people barely comment on others (run-1: all three). If their comments are mostly on their OWN posts, that null is high-value — it inverts the orbit (Brief 5).

**OUTPUT CONTRACT:**
```
{ target,
  subscriptions: [{source: substack|interests|x_likes, item, url}],
  followed_voices: [...] | "NONE FOLLOWED — finding: no individual thought-leaders",   // REQUIRED: check the Interests → Top Voices tab explicitly; its ABSENCE is a finding (contrast McConnell's one, Braylyan's zero)
  followed_newsletters: [...],   // REQUIRED: Interests → Newsletters tab, read separately from Companies
  followed_companies: [...],
  communities: [{name, url, evidence}] | "NONE FOUND across corpus (checked)",   // REQUIRED: 3c — enumerate every Discord/subreddit/Slack/forum named anywhere in their corpus; a null is a null-WITH-the-check, never a skip
  github_consumption: {stars: N, follows: N} | "null — publishes, never browses",
  comment_proxy: {outward_facing: bool, evidence},
  register_in_the_wild: "how they talk in replies vs how they post",
  run_ledger: [{step: "3a-substack"|"3a-interests-topvoices"|"3a-interests-newsletters"|"3a-github"|"3c-communities"|..., status: "RAN-FOUND"|"RAN-NULL (n)"|"NOT-RUN (reason)"}],
  coverage_bounds }
```
**SELF-CHECK (all must be true before returning):** Substack tried with SLUG not id · Interests read as THREE separate tabs — Top Voices AND Newsletters AND Companies (Top-Voices absence stated as a finding) · 3c communities enumerated or explicit null · GitHub null reported if empty · comment-proxy verdict stated · **run_ledger present with a row for every sub-step, zero NOT-RUN rows** (a NOT-RUN = you are not done).

---

## WORKER BRIEF 4 — Citation mining  (OPEN-WEB · Sonnet computes, Fable interprets)

**ROLE:** Fetch a person's full published corpus and extract what they cite. You COMPUTE and REPORT raw aggregates + the diagnostic ratio; you do NOT interpret (that's synthesis).

**INPUT:** `{name, corpus_urls[] — articles, blog posts, published essays}`

**METHOD:** fetch each piece; extract and aggregate:
- Every OUTBOUND LINK → aggregate by domain, rank by frequency.
- Every NAMED PERSON → separate cited-as-authority from mentioned-as-colleague.
- Every PUBLICATION / PODCAST / BOOK / PAPER treated as a source.
- Every NAMED TOOL → used vs reviewed vs dismissed.
- **THE DIAGNOSTIC RATIO:** what share of outbound links go to an actual SOURCE (research, policy, journalism, an outside practitioner) vs a vendor / a tool / their own properties. (Run-1: Alex Lieberman scored 0% across 50 articles — that one number characterized him better than anything else.)
- Check for a HIDDEN BIBLIOGRAPHY (a reading list in a repo file, not on any profile — people who teach often keep one).
- Log what they BORROW WITHOUT CREDIT (shows what they've absorbed vs studied).
- Citation habits track the AUTHOR not the org — never characterize a company's reading from one byline.

**OUTPUT CONTRACT:**
```
{ target, pieces_read: [{title, url}], pieces_unreachable: [...],
  outbound_by_domain: [{domain, count}], 
  diagnostic_ratio: {source_pct: N, vendor_own_pct: N, denominator: total_links},
  named_authorities: [...], sources_treated_as: [...], tools: {used:[], reviewed:[], dismissed:[]},
  hidden_bibliography: {found: bool, url, domains:[...]},
  borrowed_uncredited: [...],
  coverage_bounds }
```
**SELF-CHECK:** ratio denominator stated · pieces_unreachable listed · no interpretation added (raw aggregates only).

---

## WORKER BRIEF 5 — Circles + inroads  (BROWSER-LANE · Sonnet enumerates · active plays only)

**ROLE:** Map who's around the target. Enumerate; the orchestrator ranks realness.

**INPUT:** `{name, verified_accounts[], comment_proxy verdict from Brief 3}`

**METHOD:**
- Comment-section mining: read last ~10 posts' threads — who recurs, and who does the target ANSWER (recurring answered names = the circle).
- **If Brief 3 said inward-facing → invert:** the circle is THEIR OWN COMMENTERS + their new hires. Mine commenters on the last ~10 posts, capture headlines (run-1 surfaced an in-lane AI strategist this way).
- Co-occurrence: co-speakers, co-authors, podcast co-guests, panel rosters (READ THE PAGE JSON not just the DOM — roles/moderator/affiliation often live only in the payload).
- Shared rooms: communities you're both in = strongest legitimate inroad.
- Mutuals: enumerate for THIS target specifically (run-1: one target's mutuals were dead, another's — never checked — were the deepest). Flag each as REAL vs BRIEF-INTERACTION; do NOT assert intro-worthiness (orchestrator's call — no presumed relationship capital).
- New-hire announcements: double-duty — scaling signal + second-order targets.

**OUTPUT CONTRACT:**
```
{ target, circle_answered: [{name, headline, url}], own_commenters: [{name, headline, url, same_lane: bool}],
  co_occurrence: [{name, context, url}], shared_rooms: [...],
  mutuals: [{name, url, relationship: REAL|BRIEF|UNKNOWN, evidence}],
  new_hires: [{name, role, url}],
  coverage_bounds }
```
**SELF-CHECK:** mutuals checked for THIS person (not inherited from another) · conference rosters read from JSON · no intro-worthiness asserted · headlines captured for own-commenters.

---

## WORKER BRIEF 6 — Req verification  (OPEN-WEB · Sonnet)

**ROLE:** Verify a job posting from the org's OWN ATS. Never trust an aggregator or another agent's JD summary.

**INPUT:** `{org, role_title, req_hint or url}`

**RECIPES:**
- Find the org's ATS: Workday CXS `POST /wday/cxs/<tenant>/<site>/jobs` with `{"searchText": q}` → clean JSON; job detail at `/wday/cxs/<tenant>/<site>/job/<path>`. Greenhouse `boards-api.greenhouse.io/v1/boards/{org}/jobs/{id}?questions=true` → JD + **every screening question with exact dropdown options**. Ashby `api.ashbyhq.com/posting-api/job-board/{org}?includeCompensation=true` + its GraphQL for form fields. Lever public JSON.
- Capture VERBATIM: location text, remote/hybrid/onsite policy, reporting line, travel, comp (or its absence), required years, req id, posting date, EVERY screening question + options.
- **Read the dropdowns** — the binding constraint often lives there, not in prose (run-1: an in-office question with no "hybrid" option was more decision-relevant than the whole JD).
- **Diff sibling reqs** — hash the JDs of a family; a "specialization" may exist only in the title. Same-day sibling postings = an org build-out signal.
- Repost history via aggregators (labeled as such) — quarterly repost = evergreen.
- 50%-rule count: list each required qual with a match/no-match call against the candidate profile provided.

**OUTPUT CONTRACT:**
```
{ org, req_id, title, ats, canonical_url, posted_date,
  location_verbatim, remote_policy_verbatim, reporting_line, travel, comp,
  required_quals: [{text, match: yes|no|partial}], qual_count: "N.N / M",
  screening_questions: [{q, options[]}] | "login-walled — unread",
  siblings: [{req_id, title, location, posted, note}],
  repost_history: "labeled aggregator finding",
  gate_claim_scorecard: [{claim, verdict: VERIFIED|FALSE|SUPPORTED}],
  coverage_bounds }
```
**SELF-CHECK:** read from the org's OWN ATS (not LinkedIn/Indeed) · dropdowns read or marked login-walled · siblings diffed · every load-bearing gate claim scored.

---

## WORKER BRIEF 7 — Trace sweep (everywhere-but-LinkedIn)  (OPEN-WEB · Sonnet)

**ROLE:** Find where a person exists (and provably doesn't) OFF LinkedIn.

**INPUT:** `{name, anchors, verified_accounts[]}`

**METHOD:** X/Twitter, Bluesky, Instagram, Threads, TikTok, Facebook, Substack, Medium, GitHub, personal site, podcasts (Listen Notes / Apple / Spotify web), YouTube/conference archives, webinar libraries, trade-press bylines. Anchor EVERY hit through the 2-anchor gate — same-name people are everywhere. Report absence per platform plainly. Note captcha/bot-walled surfaces as unverified, not absent.

**OUTPUT CONTRACT:**
```
{ target, surfaces_found: [{surface, what, date, url, status: verified|UNVERIFIED}],
  social_presence: {x, bluesky, instagram, threads, tiktok, facebook, github, medium, substack, site: found_url|"not found"|"not distinguishable"},
  upcoming_appearances: [...] | "none found",
  disambiguation_guards: ["same-name people to NOT attribute: ..."],
  the_read: "where they actually live, 3-5 lines",
  coverage_bounds }
```
**SELF-CHECK:** every "found" cleared 2 anchors · nulls stated per platform · same-name collisions listed as guards.

---

## ADVERSARIAL VERIFIER  (Sonnet for mechanical claims · Fable for a synthesis claim)

**ROLE:** Try to REFUTE a specific claim. Default to "refuted" if you cannot independently confirm it. You are not confirming the worker did its job — you are attacking the claim.

**INPUT:** `{claim, its_stated_source, target_context}`

**METHOD:** Open the stated source yourself. Does it actually say this? Is the account/person the right one (2-anchor re-check)? Is a null a real null or an unrun check? Is an inference dressed as a finding? For a synthesis claim (e.g. "his diagnostic ratio is the exploitable gap"), attack the reasoning, not just the datum.

**OUTPUT:** `{claim, verdict: CONFIRMED|REFUTED|UNCONFIRMABLE, what_i_checked, what_i_found}`. One claim per verifier; spawn N verifiers for N load-bearing claims.

---

## RESERVED FOR THE FABLE ORCHESTRATOR (not worker briefs — and why)

- **Layer 0 — Frame.** Who, which list, desired outcome, therefore depth. Sets everything downstream; cheap to get wrong, expensive when wrong.
- **Layer 5b — Openings analysis (OCCUPIED / PEER / OPEN / VOID).** The actual deliverable. Reading a corpus and landing "0% of his links go to a source, and THAT is the wedge" is synthesis a worker won't reliably reproduce. Workers hand up the raw aggregates (Brief 4); the orchestrator writes 5b. Includes the null-result regex for Jefferson's own terms, and hunting for their-own-words-making-his-argument.
- **Corpus match.** What Jefferson knows that they don't — requires holding his corpus (`reference/corpus-inventory-2026-08-26.md`) against theirs with judgment.
- **Touch-angle selection.** Which piece backs which comment, in what register. Taste. The prose is always Jefferson's; the angle is the orchestrator's.
- **Final ruling on any worker-flagged UNVERIFIED / disambiguation.** A worker escalates; the orchestrator decides.

**Dispatch pattern (proven shape):** orchestrator does Layer 0 → parallel Sonnet open-web workers (1, 4, 6, 7) + one serial Sonnet browser worker (2, 3, 5) → adversarial verifiers on load-bearing claims → orchestrator writes 5b + corpus match + touch angles → synthesis to Attio/card with per-claim provenance.
