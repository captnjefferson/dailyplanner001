# Novanta posting archaeology (dossier, 2026-07-13)

## Canonical posting (URL, req id, comp, remote policy as EMPLOYER states it)

- **Canonical apply URL:** https://novanta.wd5.myworkdayjobs.com/en-US/Novanta-Careers/job/Remote---US/AI-Strategy-Director_R009436 [sourced — Workday CXS API returns this as `externalUrl`; careers entry point https://novanta.com/careers/ links to the `novanta.wd5.myworkdayjobs.com/Novanta-Careers` tenant]
- **Req ID:** R009436. Workday internal posting id `AI-Strategy-Director_R009436`, posted date (`startDate`) **2026-07-10**, "Posted 3 Days Ago", Full time. [sourced — raw JSON: https://novanta.wd5.myworkdayjobs.com/wday/cxs/novanta/Novanta-Careers/job/Remote---US/AI-Strategy-Director_R009436]
- **Comp (employer-stated):** "$160,400 to $256,600 annually based on full-time employment" — **exact match to the LinkedIn band** — plus "Certain roles may be eligible for performance-based incentive compensation and/or long-term incentives." [sourced — same CXS JSON, Benefits section]
- **Remote policy (employer-stated):** Workday location field is literally **"Remote - US"** (country: United States of America); description header "AI Strategy Director – Remote (US)" and body says "You'll join a global team, work remotely." **No Bedford-residency or travel requirement appears anywhere in the live req text.** [sourced — CXS JSON]. LinkedIn-geo-localization concern moot here: employer and LinkedIn agree on Remote-US.
- **Reports to:** CIO per the posting [sourced]. Novanta's CIO & CISO is **Sarah Betadam, D.Eng.** (since Jan 2021) [sourced — https://theorg.com/org/novanta/org-chart/sarah-betadam, https://www.linkedin.com/in/betadam/] — i.e., she is almost certainly the hiring manager [inferred].

## Age + repost history

**This seat has been on the market ~7.5 months across two reqs and a title change.** Timeline:

1. **~Nov 2025 — posted as "AI Architect", req R008735.** Workday URL slug `AI-Architect_R008735` (slugs freeze at req creation) [sourced — Google-indexed URL https://novanta.wd5.myworkdayjobs.com/en-US/Novanta-Careers/job/AI-Architect_R008735]. A LinkedIn posting "AI Architect at Novanta Inc." existed at https://www.linkedin.com/jobs/view/ai-architect-at-novanta-inc-4321971112 — now 404 (closed); search-engine dating places it ~Nov 10–24, 2025 [sourced but exact day uncertain — date came from search-result metadata, not a live page]. Built In also carried an "AI Architect" Novanta listing with the same lead-enterprise-AI-strategy description [sourced — https://builtin.com/company/novanta/jobs summary].
2. **By 1/31/2026 — same req retitled "AI Strategy Director".** Simplify's record (title "AI Strategy Director") contains req **R008735** in its page source with `updated_date: 2026-01-31T13:42:40` and "Posted on 1/31/2026" [sourced — https://simplify.jobs/p/df42964b-5364-4ff2-a91b-7be5d086f3ed/AI-Strategy-Director]. Google's index of the R008735 Workday URL also shows title "AI Strategy Director" [sourced]. Search-engine snippets of that old posting carried "preferred in Bedford, MA but open to remote (U.S.-based) with ability to travel to the Bedford, MA head office" [sourced but secondhand — page no longer fetchable; treat as probable-but-unverified old-req language].
3. **R008735 closed** — its CXS API now returns 403 "permission denied" (the closed-Workday-job signature; the HTML shell still 200s but loads no data). No Wayback snapshots exist of either req URL (CDX empty). [sourced — direct API check 2026-07-13]
4. **2026-07-10 — fresh req R009436 posted** with the same title, near-identical description, same comp band, and location loosened to plain "Remote - US" (Bedford language gone). LinkedIn copy = job id 4438358760, "3 days ago", **170 applicants in ~3 days** [sourced — https://www.linkedin.com/jobs/view/4438358760].

Interpretation: not a simple repost-bump — they closed one req and cut a new one, which resets LinkedIn's posted-date and applicant counter [inferred]. Whether the 5-month Nov→Jul stretch was continuous posting or had a gap between R008735's close and R009436's open is not determinable from available snapshots [speculation either way].

## Seat novelty (new seat vs backfill, evidence)

**First-of-kind seat, never filled — moderate-to-high confidence.**

- No person with "AI Strategy Director," "Head of AI," "Director of AI," or "VP AI" at Novanta surfaces in LinkedIn people searches or general web/news searches [sourced — multiple null searches 2026-07-13].
- The org chart shows no AI role under CIO Sarah Betadam (theorg lists her with no direct reports at all — sparse data, weak signal) [sourced — https://theorg.com/org/novanta/org-chart/sarah-betadam].
- The req's own evolution (AI Architect → AI Strategy Director on the same req, then a fresh req) is the behavior of an org still defining a net-new seat, not backfilling a departed incumbent [inferred].
- Adjacent-but-different roles exist: Robert Little is "Chief of Robotics Strategy" (BU-level, robotics domain — not this seat) and Randell Kilmer (Novanta) posts about AI/data governance, likely a colleague/interviewer [sourced — https://www.linkedin.com/in/robert-little-707791a/, https://www.linkedin.com/in/randykilmer/; role adjacency is [inferred]].

## Application mechanics

- **ATS:** Workday, tenant `novanta` on wd5, site `Novanta-Careers`. `canApply: true`, `includeResumeParsing: true` (resume-autofill flow), and the req carries a primary + secondary questionnaire ID (secondary is typically the voluntary EEO/self-ID block) [sourced — CXS JSON; the EEO characterization is [inferred] from standard Workday config].
- **Account:** standard Workday external-candidate flow — creating a candidate account on `novanta.wd5.myworkdayjobs.com` is required to submit [inferred — universal Workday behavior; not independently verified for this tenant].
- **LinkedIn apply** hands off to the Workday posting (no Easy Apply observed on the guest page) [inferred].
- **Process per employer:** Apply → recruiter phone screen → hiring-manager interview → panel/onsite → decision [sourced — https://novanta.com/careers/].
- **Notable for the apply-side agent:** Novanta's careers page **explicitly supports "ethical, transparent use of AI tools during your application process"** and references candidate-conduct guidance on AI usage [sourced — https://novanta.com/careers/]. Disability accommodation line: +1 781-266-5700 [sourced — job description].

## Flags (anything that changes the outreach or application calculus)

1. **7.5-month unfilled, twice-rescoped seat = the outreach angle.** Title inflation (Architect → Strategy Director) and location loosening (Bedford-preferred → fully Remote-US) suggest they struggled to land the profile and widened the aperture. The HM (Betadam) plausibly has real pain and a story about what the first pass missed — good discovery question territory [inferred].
2. **Front door is crowded:** 170 LinkedIn applicants in ~3 days [sourced]. HM-direct outreach is strongly differentiated; a Workday application alone will sit in a large pile.
3. **Fresh req = clean slate:** anyone who applied to R008735 can apply anew to R009436; applicant/date counters reset [inferred].
4. **Comp band held flat since at least January** ($160,400–$256,600 on both reqs) despite the rescope — band likely HR-fixed at the Director grade; negotiate within it plus incentive/LTI eligibility rather than expecting band movement [sourced band; negotiation read is [speculation]].
5. **Timely hooks for outreach:** Novanta joined the NVIDIA Halos AI Systems Inspection Lab (March 2026) [sourced — https://www.businesswire.com/news/home/20260316901538/en/Novanta-Joins-NVIDIA-Halos-AI-Systems-Inspection-Lab], and Q1 2026 earnings leaned hard on an AI narrative — ~15% of revenue tied to AI-infrastructure demand, +20% YoY [sourced — https://www.fool.com/earnings/call-transcripts/2026/05/12/novanta-novt-q1-2026-earnings-transcript/]. Note the earnings AI story is *product-demand* AI; this role is *enterprise/internal* AI under the CIO — don't conflate them in outreach [inferred].
6. **Employer explicitly OK with AI-assisted applications** (transparent use) — lowers risk for the apply-side agent's drafting workflow, but keep it disclosure-clean [sourced, calculus [inferred]].
