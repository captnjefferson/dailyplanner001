# INCOMPLETE — Ethan Mollick / AMBIENT / 2026-08-26

**Failing acceptance rows and their unblocks**
- `load_bearing_claims_verified: FAIL` — single-agent run. Per the process doc, `SINGLE-AGENT-DEGRADED` is not convertible to PASS. Unblock: re-run under an orchestrator with 3–8 independent verifiers.
- `applicable_layers_terminal: FAIL` — Layer 2 (X + LinkedIn post/reply behavior), Layer 3a.3 (X following/likes), Layer 3c, Layer 4, and most of Layer 7 were NOT-RUN under the 20-call time-box imposed by the caller, not by a wall.
All conclusions below are provisional.

## 1. Who and what they publish
Publication *One Useful Thing* (www.oneusefulthing.org), 18 posts in the 12-month window 2025-08-26 → 2026-08-26 (~1.5/mo, 35,450 words). All `audience: everyone` — no paywall. Median 984 reactions, range 411–2,186; median 89 restacks. Substack followers 572,857. Reply behavior: **UNKNOWN** — threads not opened (time-box, not a wall). [S1,S2,S6]

## 2. Where they read
Substack personal reader profile (handle `oneusefulthing`, id 846835 — obtained from the publication post byline, per A3, not guessed): **21 visible subscriptions, `subscriptionsTruncated: false`** — a complete list, not a sample. 7 paid, 14 free. [S2]
Bluesky @emollick.bsky.social — 147 follows, 36,293 followers, 3,011 posts; 100 of 147 follows read (cursor present). [S4]
LinkedIn Interests: tabs rendered are **Companies / Groups / Newsletters / Schools** — no Top Voices tab. Companies tab captured (8 entries). Groups/Newsletters/Schools NOT-RUN. [S5]
GitHub `emollick`: 36 repos, 135 followers, **no name/bio/company/location — zero anchors, NOT-DISTINGUISHABLE**, not counted as the target. [S3]
Reddit + Letterboxd: **BLOCKED-WALLED** — control accounts (reddit/user/spez, letterboxd/dave) both returned 403. Not absence. [S7]

## 3. Who they read
Paid: Core Memory (Ashlee Vance), Derek Thompson, Ettingermentum, Latent.Space (swyx), The Learning Dispatch (Carl Hendrick), Rhystic Studies, Scott's Mixtape (Scott Cunningham), Sources.
Free: Age of Invention, AI as Normal Technology (Narayanan/Kapoor), Astral Codex Ten, CTAS Higher Ed Business, Education Disrupted (Bauschard), The Future of Higher Education (Stricker), Ghosts of Electricity, Numb at the Lodge, Rami's Readings, The Third Place (Max Gladstone), Transformer, Wild World of Work (Matt Beane). [S2]
Bluesky follows skew economists + AI journalists + AI practitioners: Erik Brynjolfsson, Daniel Rock, Kevin A. Bryan, Kristina McElheran, Basil Halperin, Simon Willison, Chris Albon, Kevin Roose, Casey Newton, Christopher Mims, Eric Topol, Anil Dash, Max Roser, Anna Mills. [S4]

## 4. Circle and inroads
NOT-RUN (Layer 4 not reached; auto-promotion could not be evaluated because reply behavior is UNKNOWN).

## 5. Openings — territory match, 18 documents, 67 regexes, 9 territories
Noisy (⚠️) terms counted only on same-territory co-occurrence, per the terms file.

| terr | standing | docs/18 | class |
|---|---|---|---|
| T3 founder-led AI / building without engineers | STRONG | 12 (67%) | OCCUPIED |
| T1 AI adoption & enablement | STRONG | 7 (39%) | OCCUPIED-or-OPEN — **doc gives no tie-break** |
| T2 org change & leadership fear | STRONG-in-practice / THIN-in-print | 3 (17%) | OPEN (at the ≥3-doc floor) |
| T5 ed-tech & special education | STRONG | 2 (11%) | **UNCLASSIFIABLE** |
| T6 cost & architecture | STRONG | 2 (11%) | **UNCLASSIFIABLE** |
| T7 associations / healthcare-adjacent | STRONG | 2 (11%) | **UNCLASSIFIABLE** |
| T4 AI risk & model governance | STRONG | 1 (6%) | **UNCLASSIFIABLE** |
| T8 sales & GTM enablement | MEDIUM | 0 | VOID (INFERRED-FROM-FETCHABLE) — barred from top three |
| T9 building/leading a tech team | MEDIUM | 0 | VOID (INFERRED-FROM-FETCHABLE) — barred from top three |

Walls that could hide a VOID: X corpus, LinkedIn corpus, academic papers, *Co-Intelligence* (book), pre-2025-08-26 Substack (73+ further posts exist).
No ranked opening list is issued: four STRONG territories have no class, and both true VOIDs are on MEDIUM territories the terms file bars from the top three.

## 6. Recommended action list
Not issued. An INCOMPLETE report may not feed a touch. (Doc: "An INCOMPLETE report may not feed a touch or an Attio write.")

## 7. Gaps and coverage bounds
Corpus bound: trailing 12 months (18 docs) chosen over 30 items, because 18 < 30. Full archive is 100+ posts back to 2023-04-09; 82%+ of the lifetime corpus was NOT fetched.
Bluesky follows: 100 of 147 read. LinkedIn Interests: 1 of 4 tabs read. X: not read. Layers 2, 3c, 4, 7: NOT-RUN.
Detectability disclosed: LinkedIn profile + Interests reads from Jefferson's account are ATTRIBUTABLE-BY-BYPRODUCT — Mollick may see a profile view from Jefferson dated 2026-08-26.

## 8. Run ledger
Abbreviated — this run did not meet the per-sub-step row count. L0 RAN-FOUND (both input paths readable, both ACTIVE). L1 partial: identity VERIFIED via Substack byline + first-party bio links (Wharton employer + oneusefulthing.org + x.com/emollick + mgmt.wharton.upenn.edu) = ≥2 distinctive anchors. Maigret NOT-RUN. L3a: 6/6 surfaces touched, 2 walled, 1 not-distinguishable. L3b: corpus fetched; diagnostic ratio NOT COMPUTED. L5b: RAN-FOUND, classification incomplete.

## 9. Source registry
S1 https://www.oneusefulthing.org/api/v1/archive?sort=new&limit=50 (primary, 2026-08-26)
S2 https://substack.com/api/v1/user/oneusefulthing/public_profile (primary, 2026-08-26)
S3 https://api.github.com/users/emollick (primary, 2026-08-26)
S4 https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile + graph.getFollows?actor=emollick.bsky.social (primary, 2026-08-26)
S5 https://www.linkedin.com/in/emollick/details/interests/?detailScreenTabIndex=0 (authenticated-platform, 2026-08-26)
S6 https://www.oneusefulthing.org/api/v1/posts/<slug> ×18 (primary, 2026-08-26) — **endpoint not in the process doc; inferred**
S7 reddit.com/user/spez/about.json 403; letterboxd.com/dave/ 403 (control test, 2026-08-26)

## 10. Attio
NOT REQUESTED (write_attio: false). No preview issued — an INCOMPLETE run may not feed an Attio write.

```yaml
acceptance:
  applicable_layers_terminal:        FAIL
  no_not_run_steps:                  FAIL
  handoffs_have_receiving_rows:      PASS
  identities_clear_two_anchor_gate:  PASS
  factual_claims_have_sources:       PASS
  soft_nulls_labeled:                PASS
  corpus_loaded_from_named_path:     PASS
  load_bearing_claims_verified:      FAIL   # SINGLE-AGENT-DEGRADED
  coverage_bounds_stated:            PASS
  writes_confined_to_run_dir:        PASS
  attio_action_authorized:           PASS
run_state: INCOMPLETE
coverage_achieved: "Layer 3a 6/6 surfaces; Layer 3b corpus 18/100+ lifetime docs; Layers 2, 3c, 4, 7 not run"
verification: SINGLE-AGENT-DEGRADED
```
