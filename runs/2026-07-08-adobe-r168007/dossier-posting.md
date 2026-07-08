## DOSSIER: Posting Archaeology
## ROLE: Adobe — Senior Manager, Enterprise AI Strategy (R168007)
## COLLECTED: 2026-07-08

### Findings

**Canonical / liveness**
- Canonical posting is the Adobe Workday tenant; the authoritative cxs JSON returns `canApply: true`, `posted: true`, confirming the req is LIVE and accepting applications as of 2026-07-08 — https://adobe.wd5.myworkdayjobs.com/wday/cxs/adobe/external_experienced/job/New-York/Senior-Manager--Enterprise-AI-Strategy_R168007 — H
- DISCREPANCY: the public front-end careers page for the same req ID shows "the job you are trying to apply for has been filled," while the Workday tenant still accepts applications — treat the tenant JSON as authoritative but flag the front-end says filled — https://careers.adobe.com/us/en/job/R168007/Senior-Manager-Enterprise-AI-Strategy — M
- Careers front-end classifies the role's department as "Marketing and Strategy" (not Sales), consistent with the JSON's non-sales comp framing — https://careers.adobe.com/us/en/job/R168007/Senior-Manager-Enterprise-AI-Strategy — H

**Age / history**
- `startDate` = 2026-05-20 and `postedOn` = "Posted 30+ Days Ago"; May 20 is ~49 days before the 2026-07-08 collection date, so the two are consistent — the req has been open ~7 weeks with no evidence of repost/re-leveling — runs/2026-07-08-adobe-r168007/posting-raw.json — H
- The "May 20 2026" date appears in the JD only inside the Colorado Application Window Notice; Colorado is NOT in the location list, so no CO window governs this posting and it "may close at any time based on hiring needs" — runs/2026-07-08-adobe-r168007/posting-raw.json — H

**Comp verification**
- Authoritative U.S. band on the Workday JSON: $125,500–$226,700; NY & CA $156,500–$226,700; IL & MA $136,300–$197,350 — base salary only (non-sales = base + Annual Incentive Plan; "certain roles may be eligible for" new-hire equity) — runs/2026-07-08-adobe-r168007/posting-raw.json — H
- The stated $226,700 max is BASE only; Adobe "Senior Manager" total-comp comparables run materially higher (6figr: avg base ~$294K, total ~$400K, range ~$250K–$538K), so the JD band undersells total package once AIP + equity are layered — https://6figr.com/us/salary/adobe--senior-manager — M
- Band clears the pipeline $125K floor at the top in every geo; NY/CA base floor ($156.5K) already clears it — runs/2026-07-08-adobe-r168007/posting-raw.json — H

**Level / altitude tension (sibling role)**
- A higher-level sibling exists on the SAME initiative: "Director, Enterprise AI Strategy" (New York), whose JD builds "a field AI-ambassador network" and transforms "Adobe's global field organization into an AI-first operation" — the same AI-Ambassador Program / AI-for-Sales program R168007 supports — indicating a team build-out (Director + Senior Manager on one initiative), not a lone backfill — https://jobright.ai/jobs/info/69262bfb27bf2f41a2c43fb3 — M
- Director sibling comp/floor: US $182,500–$389,650 (NY $250,600–$389,650), 10+ years required — vs R168007's $156.5K–$226.7K NY / "5+ years"; the Director sits one clear rung above — https://jobright.ai/jobs/info/69262bfb27bf2f41a2c43fb3 — M
- ALTITUDE MISMATCH: R168007's JD reads Director-grade — "partners with Adobe's top leaders globally," owns "end-to-end AI for Sales vision," and "own[s] executive storytelling for All Hands, QBRs, and CRO forums" — yet is leveled Senior Manager with only a "More than 5 years" floor and a sub-Director band; the scope language outruns the stated seniority floor — runs/2026-07-08-adobe-r168007/posting-raw.json — M
- Build-out / new-role signal (vs backfill): JD includes "Welcome and assist new members joining the AI for Sales group," "Expand the AI for Sales program," and pilot-to-scale framing ("lead the transition from pilot phases to a balanced AI operating model") — language of a forming team — runs/2026-07-08-adobe-r168007/posting-raw.json — M

**Location / remote eligibility (candidate is DC-based)**
- Primary location New York; additional locations: Remote Illinois, San Francisco, San Jose, Remote New Jersey, Remote Texas, Remote Massachusetts, Remote Georgia (US) — runs/2026-07-08-adobe-r168007/posting-raw.json — H
- No remote-eligibility listed for DC, Virginia, or Maryland; nearest East-Coast remote-eligible geos are Remote New Jersey and Remote Massachusetts (plus Remote Georgia) — a DC-based candidate is NOT in a listed remote geo, so eligibility for a DC-based hire is unconfirmed on the posting — runs/2026-07-08-adobe-r168007/posting-raw.json — H
- Travel expectation ~20–25%; full-time — runs/2026-07-08-adobe-r168007/posting-raw.json — H

**Eligibility facts**
- Education: Bachelor's required; MBA or equivalent "strongly preferred." No security clearance, no certification, and no sponsorship statement appear anywhere in the posting — runs/2026-07-08-adobe-r168007/posting-raw.json — H

### Not Found (mandatory)
- Wayback Machine snapshot of R168007 (canonical or cxs URL) — archive.org availability API returned no snapshot; web.archive.org CDX blocked — no first-seen date or language diff obtainable.
- Any aggregator MIRROR of the Senior Manager R168007 posting (LinkedIn Jobs, Indeed, Dice, Built In, Teal, ZipRecruiter) — none index R168007 (only the Director sibling is mirrored).
- Exact Adobe management-track level (M-band) and manager-of-managers vs senior-IC designation for this "Senior Manager" — not published.
- Director sibling's exact Workday req ID — slug points to "R162748" but cxs JSON / ZipRecruiter returned 403; unverified (comp/experience taken from jobright.ai mirror).
- Any comp discrepancy ACROSS boards for R168007 — none, because no other board carries R168007; comp verified on canonical source only.

### Collector Notes (facts only)
- Hardest conflict: canonical Workday tenant says LIVE/`canApply: true`; the Adobe-branded careers front-end for the identical req ID says "filled." Same title and NY location on both. Tenant JSON treated as authoritative for liveness.
- The Director "Enterprise AI Strategy" role posted ~6 months ago predates R168007's 2026-05-20 open; sequence (Director first, Senior Manager later) supports a staged team build-out.
- JD text is visibly AI-paraphrased in places (e.g., "Competitive intelligence involves monitoring the external AI landscape.") — no bearing on facts, noted only for register.
- 6figr Adobe "Senior Manager" comp sample likely skews toward engineering/product Senior Managers; directional altitude context, not a direct comp.
