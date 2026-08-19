## DOSSIER: Posting Archaeology — REFRESH (re-approach run)
## ROLE: ButterflyMX — Director, AI Strategy & Transformation (public req 3834c6df)
## COLLECTED: 2026-08-19 · Prior run: runs/2026-07-07-butterflymx/ (reused, not redone)

### Canonical facts — new req (all from the official Ashby posting API, verified by me 2026-08-19)
Source: https://api.ashbyhq.com/posting-api/job-board/butterflymx (job id 3834c6df-0292-4c85-b035-c16fb1f22541) · page: https://jobs.ashbyhq.com/butterflymx/3834c6df-0292-4c85-b035-c16fb1f22541

- Title: **Director, AI Strategy & Transformation** (single title — the July req's Head-of/Director dual-titling is gone) — H
- Published **2026-07-21**, `isListed: true` (PUBLIC board — the July req 3839e6f9 was unlisted/direct-link-only) — H
- Department **Engineering**, team **"Software Engineering"** (confirmed twice: posting API + Ashby GraphQL `teamNames: ["Engineering","Software Engineering"]`) — H
- Location: US Remote, `isRemote: true`, FullTime — H
- **COMP, FIRST-PARTY: "The expected base salary range for this position is $200,000 - $300,000"** — stated verbatim in the JD body (`descriptionPlain`, COMPENSATION section) on the canonical Ashby source. The API's *structured* compensation fields are empty (`compensationTiers: []`, `shouldDisplayCompensationOnJobPostings: false`) — which is why the briefing gate's API check saw "no comp data." The figure is no longer third-party: it is in the employer's own posting text. — H
- No hiring-team block: neither the posting API nor GraphQL exposes any hiring-team/recruiter/reports-to data for this req. Reporting line remains unpublished. — H

### Diff: July "Head of" req (3839e6f9, died ~7/7) → this Director req (3834c6df)
- **Comp re-priced ~2x**: $120,300–$148,400 (aggregator-sourced, July) → **$200,000–$300,000 base (first-party)**. Floor alone now clears Jefferson's $125K pre-filter outright — the July straddle caveat is dead.
- **Unlisted → public.** July's req was deliberately hidden (quiet/referral sourcing); this one is on the open board.
- **Title settled down a notch (Head → Director) while comp went up** — the seat was re-leveled as a Director inside Engineering but priced like a serious hire.
- **Explicit org placement appears for the first time**: Engineering / Software Engineering. The July run had NO public reporting signal and inferred Jeffrey Kok (CInO) at M. This placement is the first structural data point and it points toward the engineering line (CTO Benjamin Trent) rather than Innovation — though Ashby department metadata is admin taxonomy, not an org chart (the Director of IT req also sits under "Engineering").
- **Mandate language ~identical** to the July composite JD: same de-scope line ("You will not be expected to build models or write production code"), same budget/governance/headcount/intake/evangelist scope. Additions in this version: "Ensure decisions are driven by data with clear KPIs"; "Deep curiosity and a hands-on mindset with emerging technology"; "Identify AI tools and services that should be adopted by our company"; "Balance risk management with speed and usability"; "Help define guardrails that enable innovation."
- **Copy-paste artifact**: the JD boilerplate still contains "ButterflyMX is looking for a Senior Full Stack Engineer to join our stellar team…" — the posting was cloned from an engineering-req template. Corroborates that whoever drafted it works from Engineering's templates.
- **Culture boilerplate now says "ai-forward"**: "…more intelligent, passionate, collaborative, ai-forward, and down-to-earth individuals…" — company-wide language, present across current postings.

### The three-req archaeology (full arc, prior run + this refresh)
1. **AI Solutions Lead** — hands-on technical IC (LangChain/RAG/agents), pulled 2025-09-26 — https://www.builtinnyc.com/job/ai-solutions-lead/6408669 [spot-checked in July run]
2. **Head of AI Strategy & Transformation** — unlisted, $120.3–148.4K (aggregators), non-coding transformation leader; died ~2026-07-07 (filled or closed — which one was never determined)
3. **Director, AI Strategy & Transformation** — public, $200–300K base, same mandate, Engineering department, published 2026-07-21 — live as of today (verified on board API 2026-08-19)

Read: across 11 months the company kept the same non-coding adoption/governance mandate and **re-priced it upward ~2x** while moving it from a quiet unlisted search to the open board. Whatever happened to req #2 (a failed search, a fell-through hire, or a re-scope), the org's answer was to raise the price and widen the funnel — the seat got MORE important, not less.

### Adjacent-req cluster (same board pull, 2026-08-19)
- **Director of Information Technology** — Engineering, published 2026-07-17
- **Vice President of Data** — Engineering, published 2026-07-23
- **Principal AI-Native Software Engineer** — Engineering, published 2026-08-17
Three senior tech-leadership seats posted within a week of the AI Director (7/17–7/23) plus an AI-native principal engineer a month later. Combined with the JD's "Manage headcount planning and hiring strategy for AI teams," this reads as a deliberate AI/data leadership build-out under Engineering — the Director seat will have peers and a team, not a lone-evangelist perch. — H (all ids on the board API)

### Not Found
- Reports-to line / hiring team for the Director req — not exposed on any Ashby surface.
- Fate of the July Head-of req (filled vs closed) — still undetermined.
- Any repost/refresh cycle on the new req since 7/21 — none observed.

### Pre-filter & 50%-rule check (this req)
- Comp: floor $200K > $125K — PASS outright. Cash base, standard bonus/equity language — PASS.
- Remote US, FullTime, no travel requirement stated — PASS.
- Qualification match (8 stated requirements): cross-functional change leadership ✓ (CT cohort; Beekeeper); deep AI understanding ✓; org budget management ✓ (Beekeeper SVP; Adaptiverse CEO); exec stakeholder influence ✓; governance frameworks ✓ (verification systems; lobbying-firm data-security/disclosure protocol); technical↔non-technical translation ✓ (PromptLab, DMAS keynote); curiosity/hands-on with emerging tech ✓ (builds with Claude Code); preferred strategy/ops/tech-leadership/consulting background ✓. **8/8 — clears the 50% rule with room.**
