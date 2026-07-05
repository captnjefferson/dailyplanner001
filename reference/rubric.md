# HM-Direct Outreach v2 — Operational Artifacts

Companion to `hm-direct-outreach-v2.md`. Three artifacts: the gate-scoring rubric (briefing-ready), the Tier 1 dossier template, and the master orchestration prompt. Plus the backtest protocol for the current Catalyst batch.

---

## Artifact 1 — Gate-Scoring Rubric (briefing-ready)

**Pre-filters (checked before any scoring — a hit here = straight to volume machine):**
- **Comp floor:** $125K. Fails only if the range *maximum* is below $125K. No mission-org exceptions in the rules — Jefferson's gut drives trade-off decisions at review, not the gate. (Calibrated 2026-07-04.)
- **Equity-in-lieu-of-cash:** equity-heavy comp structures fail. Rationale: already holding substantial Adaptiverse equity; this exercise buys cash runway. (Standard RSUs atop cash that independently clears the floor do NOT trigger this.)
- **Eligibility:** if location/remote eligibility can't be easily confirmed, fail. Too many likely subsequent flags.
- **Travel:** >50% fails. ≤50% passes through.

Each surviving role gets a **binary verdict** (C1 YES mandatory + at least one of C2/C3 YES) *and* a **graded score** (0–6). A warm path already known at briefing time = auto-PASS with C1 YES + priority flag; warm-path discovery for everything else happens in Phase 1C, post-gate.

**C1 — Target-spec fit (MANDATORY — a 0 here is an automatic FAIL)**
- 2: Senior AI/digital-transformation leadership at a target-sector org (association, public-sector-adjacent, mission-driven, or agency/communications world). "I'd take this call tomorrow."
- 1: Adjacent — right seniority in a nearby sector, or right sector scoped slightly junior/broader.
- 0: Wrong level (IC/manager where AI is a facet), wrong role, or **health-focused org at senior level** (domain-knowledge mismatch — calibrated 2026-07-04). (Binary: YES = 1 or 2.)

**C2 — Findable decision-maker**
- 2: HM identifiable now, or org small enough (<~200 staff) that the function leader is trivially findable.
- 1: Plausible with real digging (mid-size org, some public structure).
- 0: Opaque — large anonymous enterprise, agency/RPO posting, confidential search. (Binary: YES = 1 or 2.)

**C3 — Real-problem visibility**
- 2: Rich public exhaust — strategic plan, 990s, leadership talks/writing, news coverage.
- 1: Some exhaust; hypothesis possible but will lean on inference.
- 0: Thin — private co with no public strategy footprint. (Binary: YES = 1 or 2.)

**Verdicts:**
- **PASS** — C1 YES + ≥1 of C2/C3 YES (or known warm path + C1 YES).
- **NEAR-MISS** — exactly one criterion short of passing. Surfaced during calibration.
- **FAIL** — everything else. Volume machine only.

**Briefing line format:**
`[ORG] — [ROLE] | Verdict | C1:x C2:x C3:x = n/6 | warm-path flag | one-line rationale`

---

## Artifact 2 — Tier 1 Dossier Template (subagent return format)

Every research subagent returns exactly this structure. No synthesis, no recommendations, no prose conclusions — collection only.

```
## DOSSIER: [section — Org Layer | Posting Archaeology | Person Layer | Voice Corpus]
## ROLE: [org — title]

### Findings
- [finding, one sentence, specific] — [URL] — [confidence: H/M/L]
- ...

### Not Found (mandatory — list what was searched for and not located)
- [item] — [where searched]

### Collector Notes (facts only — ambiguities, conflicting sources)
- ...
```

Intake rule: any finding without a working URL is deleted before synthesis. "Not Found" entries feed the Gaps & Inference Register.

---

## Artifact 3 — Master Orchestration Prompt

Paste into a research-capable Claude session (or set as Project instructions). Inputs per role: posting URL/text + Jefferson's background summary + network context (ten-names list when available).

> Run my HM-Direct Outreach System v2 for this role: [POSTING]. My background: [ATTACHED]. Network context: [ATTACHED/none].
>
> **Stage 1 — Parallel research.** Spawn four research tasks; each must return ONLY the Tier 1 Dossier Template:
> 1. **Org Layer:** strategic plan, annual report, leadership priorities, recent news. If nonprofit/association: most recent Form 990 via ProPublica Nonprofit Explorer (revenue trend, staff size, exec comp, tech-relevant spend). All other currently open roles at the org.
> 2. **Posting Archaeology:** days open, reposts/re-leveling (Wayback, posting dates), salary band vs. comp data, divergence between posting language and org's public strategy.
> 3. **Person Layer:** most likely hiring manager with evidence; who posted/commented/spoke about this initiative; warm paths against my network context.
> 4. **Voice Corpus:** the likely HM's recent writing/talks; their stated priorities and register. (Calibration only — never style mimicry.)
>
> **Stage 2 — Intake.** Delete any finding lacking a working URL. Spot-check 2–3 load-bearing citations by fetching them. Carry "Not Found" items forward.
>
> **Stage 3 — Synthesis brief:** Real Problem Hypothesis (one falsifiable sentence); the One Insight (must fail "could anyone else have written this?"); one matched proof point from my background; warm-path recommendation (intro-first / note-first / parallel); channel recommendation; source ledger; **Gaps & Inference Register** — each load-bearing claim tagged [sourced] / [inferred — from X] / [speculation].
>
> **Stage 4 — Draft:** the note (100–130 words; substance-first, no flattery openers, one proof point, soft question CTA, my voice) and the single value-add follow-up. Flag any sentence not backed by the ledger. End with the top 2 uncertainties a human must verify. Do not send anything.

---

## Backtest Protocol — Current Catalyst Batch

**Purpose:** Test Jefferson's hypothesis that the Phase 0 gate is too strict, using real roles. Gate runs AS WRITTEN — no mid-test adjustments.

1. **Input:** the current role set (org, title, posting URL; days-open and source if handy).
2. **Scoring pass (Claude):** every role scored per Artifact 1; output one table sorted PASS → NEAR-MISS → FAIL, with per-criterion scores and one-line rationales. C3 scored heuristically where network context is missing (flagged as such).
3. **Gut calibration (Jefferson, ~15 min):** for every PASS and NEAR-MISS — and any FAIL that jumps out — mark "would take the call" YES/NO. No justification needed.
4. **Comparison:** false negatives (gut-YES, gate-FAIL/NEAR-MISS) are the too-strict evidence; false positives (gate-PASS, gut-NO) are the too-loose evidence. Identify WHICH criterion causes the misses.
5. **Adjustment decision:** options include lowering the binary threshold, making C1 mandatory + any 1 other, or moving to graded ≥5. Chosen only after the data, not before.

**Success criterion:** the gate agrees with Jefferson's gut on ≥80% of roles, and every disagreement is explainable by a single identifiable criterion.
