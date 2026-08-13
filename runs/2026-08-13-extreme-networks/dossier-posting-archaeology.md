# DOSSIER: Posting Archaeology
## ROLE: Extreme Networks — Director, Marketing AI Transformation
## COLLECTED: 2026-08-13

### Findings

**Canonical posting & liveness**
- Canonical posting is on Extreme Networks' Lever ATS and is live as of 2026-08-13 — the Lever public API returns the full posting (HTTP 200), title "Director, Marketing AI Transformation," department Marketing / team Corporate Marketing, workplaceType remote, location category "South Carolina, United States," reports to CMO — https://api.lever.co/v0/postings/extremenetworks/c440e869-eede-474e-a395-24741d49b673 — H
- Extreme's own careers page routes to this Lever instance (jobs.lever.co/extremenetworks), confirming Lever as the ATS of record — https://www.extremenetworks.com/about-extreme-networks/career — H
- Lever API `createdAt` = 1785944287653 ms → 2026-08-05 (~15:38 UTC); posting is ~8 days old at collection — H (decode by collector)
- Liveness contrast check: two Extreme marketing reqs Google still indexes now 404 on the Lever API ("Director of Marketing - Integrated Campaigns" https://api.lever.co/v0/postings/extremenetworks/dbec4315-5c74-417c-a7be-0a28174d2cae and "Senior MarTech Solution and Innovation Manager" https://api.lever.co/v0/postings/extremenetworks/9ab76726-748b-41c3-b0ce-b367e9da5c97) — confirms the API-200 on the target req is a meaningful live signal — H

**Repost / history**
- No archive.org snapshot of the posting URL exists (Wayback availability API returns empty `archived_snapshots`), so no pre-2026-08-05 version can be documented — https://archive.org/wayback/available?url=jobs.lever.co/extremenetworks/c440e869-eede-474e-a395-24741d49b673 — H
- No prior Extreme Networks posting found under any of the JD's four alternate titles in web search; the only hit for those strings is the target req itself — M (absence-of-evidence)
- The req is part of an early-August marketing batch: "CXO Program Manager" createdAt 2026-08-05 (same day), "Business Development Representative" (CA) 2026-08-04, and marketing-team **"AI Agent Implementations Specialist"** 2026-08-07 (Thornhill, Canada, remote) — https://api.lever.co/v0/postings/extremenetworks?mode=json&department=Marketing and https://jobs.lever.co/extremenetworks/ebb38b50-7d0e-46ef-b166-2a3d2d41d5d6 — H
- A sibling senior marketing req, "Sr. Director of North America Field Marketing" (Texas, remote), createdAt 2026-06-11, also carries no compensation range — https://api.lever.co/v0/postings/extremenetworks/3f225be1-aef6-4caa-b109-d86280c5ffee — H

**Comp verification**
- Canonical posting contains NO salary range (confirmed against raw API JSON) — https://api.lever.co/v0/postings/extremenetworks/c440e869-eede-474e-a395-24741d49b673 — H
- Extreme DOES publish ranges on reqs tagged to disclosure states: BDR tagged "California" states "80-100K OTE" verbatim — https://jobs.lever.co/extremenetworks/955c857a-8e34-47f4-b4cc-729ddc788d83 — H; Sr. SLED Account Executive VA/MD/DC shows $200,000–$275,000 OTE per search snippet — https://jobs.lever.co/extremenetworks/bfda4b5c-966c-4a02-ba5c-32fb6846aa0c — M
- Comp proxies (aggregates, not this req): Levels.fyi Extreme Marketing median TC $136,950, headline "$137K–$195K+" — https://www.levels.fyi/companies/extreme-networks/salaries/marketing — M; Indeed Extreme Director avg ~$177,907 — https://www.indeed.com/cmp/Extreme-Networks/salaries/Director — L; Salary.com Extreme director range to ~$297K — https://www.salary.com/research/company/extreme-networks-inc-salary — L
- $125K-floor read: director-level comp at Extreme is reported well above $125K on every proxy source — M

**Language signals / diffs**
- The JD names a PRE-EXISTING corporate governance body verbatim: "Represent marketing's best interest on the corporate IT-led AI Council and share best practices and learnings across the organization" — H. No public source describing this council was found — internal-only fact — M
- Diff: posting is generic about tooling ("Familiarity with AI tools like generative AI platforms, marketing automation systems, and data analytics tools") while Extreme's public strategy is highly specific: "We have AI at the center of everything" (Carla Guzzetti, Chief Product Officer, Extreme AI Summit recap blog, 2025-12-04) — https://www.extremenetworks.com/resources/blogs/shaping-tomorrow-bold-insights-from-extreme-ai-summit — H; and the Agent ONE agentic-AI launch at Extreme Connect 26 — https://www.computerweekly.com/news/366642566/Extreme-Connect-26-Agent-ONE-takes-forward-network-AI — H. The JD never names Extreme Platform ONE or Agent ONE.
- Internal-adoption ethos quote: "Move fast, keep moving, and aim to be first" (Nabil Bukhari, President of AI Platforms and CTO, on Extreme's internal AI messaging) — https://www.extremenetworks.com/resources/blogs/shaping-tomorrow-bold-insights-from-extreme-ai-summit — H
- The JD carries an explicit "Alternate Titles:" list of five titles inside the posting body — unusual for a published req; reads as a role-design document published as-is — H
- Reporting line: "Reports to: Chief Marketing Officer (CMO)"; the CMO is Monica Kumar, EVP & CMO (announced 2023-12-20) — https://investor.extremenetworks.com/news-releases/news-release-details/extreme-networks-appoints-monica-kumar-chief-marketing-officer/ and https://www.businesswire.com/news/home/20231220035893/en/ — H
- South Carolina tag context: Extreme's US state-level location tags on remote reqs vary per posting (CA on the BDR, TX on the Field Marketing Sr. Dir., SC on this one); US operational HQ is Morrisville, NC per ZoomInfo — https://www.zoominfo.com/c/extreme-networks/32214307 — M. No Extreme marketing leader based in South Carolina was located to explain the tag.

**Eligibility facts**
- Remote, full-time, US posting; no application deadline stated; no work-authorization/sponsorship language; no clearance; Bachelor's required (MBA preferred); standard EEO language only — H

### Not Found (mandatory)
- Salary range for THIS req on any aggregator scrape — searched Built In, ZipRecruiter, Indeed, Jobright, Adzuna, Levels.fyi, Glassdoor; the req is not syndicated anywhere yet (only the Lever URL surfaces)
- LinkedIn copy of the posting / applicant count — no LinkedIn job URL found for this req, so no competition signal available
- Any earlier posting of this role under its own title or the four alternate titles
- Wayback snapshot of the posting URL
- Public documentation of the "corporate IT-led AI Council" named in the JD
- Any Extreme Networks marketing/leadership employee based in South Carolina
- Application deadline or changes
- Named internal candidate signals (no one on LinkedIn holds this or an alternate title at Extreme)

### Collector Notes (facts only)
- Timestamp decodes are collector arithmetic from raw `createdAt` ms values; one WebFetch sub-response misdecoded a date — trust the raw values quoted here.
- Lever's API shows the ambiguity directly: categories.location = "South Carolina, United States" while the JD body says "Location: Remote." The state tag's purpose is unresolved.
- The JD references two DIFFERENT councils: the Marketing AI Council (to be established/chaired by this hire) and the corporate IT-led AI Council (pre-existing). Only the first is publicly described anywhere, and only inside this JD.
- Levels.fyi/Indeed/Salary.com figures conflict with each other — usable only as floor-clearance signal, not as the role's band.
- Age caveat: "first seen" = Lever createdAt (2026-08-05). No board syndication found yet, consistent with a very fresh req.
