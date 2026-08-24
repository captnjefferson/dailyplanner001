## DOSSIER: Posting Archaeology
## ROLE: Alera Group — Head of AI / "Head of Aritficial Intelligence (AI)" [sic]
## COLLECTED: 2026-08-24

### Findings

**1. CANONICAL REQ — FOUND AND LIVE**

- Canonical posting is **req/job ID 7564** on Alera's own careers site: https://careers.aleragroup.com/company/jobs/7564?lang=en-us — page `<title>` renders "Head of AI in United States | Alera Group"; sitemap-listed form is https://careers.aleragroup.com/jobs/7564?lang=en-us — **H** (EMPLOYER-SOURCED)
- Alera is **not on Workday**. Their ATS is a Jibe/iCIMS-style client-rendered career site whose working JSON endpoint is `GET https://careers.aleragroup.com/api/jobs?keywords=<q>&limit=<n>` (relevance-ranked, returns only ~4–8 records per call regardless of `limit`). Job pages are JS-rendered with no server-side JSON-LD, which is why direct page fetches look empty — https://careers.aleragroup.com/api/jobs?keywords=Head+of+AI — **H** (EMPLOYER-SOURCED)
- Full job inventory enumerable at https://careers.aleragroup.com/sitemap1.xml — 60 live job URLs, lastmod range 2026-06-25 → 2026-08-21. Job 7564 present; highest live ID is 7610 — **H** (EMPLOYER-SOURCED)

**2. STATE ELIGIBILITY — THE GATE'S OPEN QUESTION, RESOLVED**

- **No state-exclusion list exists.** The complete verbatim canonical description contains no state names, no "unable to hire in," no "not available in," and no pay-transparency state carve-outs. The only location language is: *"Work Arrangement — This position is Remote"* and *"Location Type: Remote."* Structured fields are `location_name: "Alera Group - Remote - United States"`, `country: "United States"`, `full_location: "United States"` — https://careers.aleragroup.com/api/jobs?keywords=Head+of+AI — **H** (EMPLOYER-SOURCED, full-text verbatim; independently re-verified by the parent agent at intake)
- The req's own LinkedIn tracking tags confirm nationwide scope: the description ends `#LI-BH1 ,#LI-Remote, #Nationwide`. The identical `#Nationwide` tag appears on Alera's other remote reqs (e.g. req 7538 ends `#LI-JP1 #Nationwide`), so it is Alera's standing convention for genuinely 50-state-eligible postings — https://careers.aleragroup.com/api/jobs?keywords=Implementation+Lead+Property+Casualty — **H** (EMPLOYER-SOURCED)

**3. POSTING METADATA — EXACT DATES**

- Canonical date fields: `posted_date 2026-08-20T18:54:00+0000`; `create_date 2026-08-20T18:55:27+0000`; `date_updated 2026-08-20T19:00:26Z`; `update_date`/`last_mod 2026-08-20T21:32:33+0000`; **`posting_expiry_date 2026-09-25T04:00:00+0000`** — **H** (EMPLOYER-SOURCED; expiry + posted date re-verified at intake)
- Actual first-posted date is **2026-08-20**, not LinkedIn's "3 days ago." There is a **hard posting expiry of 2026-09-25 04:00 UTC (= 2026-09-24 midnight ET)** that the LinkedIn view does not surface.
- The req was **edited the same day it went up** — created 18:55:27, last modified 21:32:33 (2h37m later). Content of the edit is not recoverable (no archive snapshot).
- LinkedIn shows **"Over 200 applicants"** as of 2026-08-24, i.e. ~4 days after posting. Single observation; no trajectory available — https://www.linkedin.com/jobs/view/4457053864 — **H** (observation)

**4. DISTRIBUTION — IN-HOUSE, NOT AGENCY-DISTRIBUTED**

- The Head of AI req appears on exactly **two surfaces**: Alera's canonical careers site and LinkedIn. NOT found on Indeed, ZipRecruiter, Glassdoor, Jobright, SimplyHired, Talent.com, BeBee, Lensa, Remotive, TealHQ, Vaia, Dice, FlexJobs, or CareerBuilder — while *other* concurrent Alera reqs (Implementation Lead, Transformation Change Integration Leader, VP L&D, AI & Security Administrator) DO appear across those same aggregators — **M** (negative finding across searches; consistent with a 4-day-old in-house post scrapers have not yet picked up). Contrast case: https://bebee.com/us/jobs/transformation-change-integration-leader-alera-group-inc-us--t7xk-784184371
- **No third-party recruiter or retained search firm is fronting this req.** No search-firm-branded version exists on any surface. The `#LI-BH1` tag is Alera's internal recruiter-owner code (compare `#LI-JP1` on req 7538) — **M**. Alera runs in-house executive recruiting: William Zajac, Alera Group, talent acquisition / "executive search and recruiting" — https://www.linkedin.com/in/williamzajac/ — **M**

**5. COMP VERIFICATION**

- **$250,000 – $300,000 annually, "Bonus Eligible: Yes (Performance Based)"** — stated verbatim in the employer's own canonical description AND in the employer's structured `salary_range` field — https://careers.aleragroup.com/api/jobs?keywords=Head+of+AI — **H** (EMPLOYER-SOURCED; re-verified at intake)
- Same band shown on LinkedIn — https://www.linkedin.com/jobs/view/4457053864 — **H**. Note: LinkedIn and the careers site are both employer-published, so this is corroboration across two employer surfaces, **not** an independent second source.
- **No aggregator salary estimate for this req exists** anywhere — so there is no discrepancy to reconcile and nothing to discount as a scraped guess — **M** (negative finding)
- Internal band context, all EMPLOYER-SOURCED via the same API: VP Finance Operations (6946) $225–260K; VP Learning & Development $170–220K; Transformation Change Integration Leader $120–170K (aggregator-sourced); Implementation Leads (7537/7538) $100–150K. **The Head of AI band at $250–300K is the highest posted band in Alera's current requisition set** — **H**

**6. TITLE / DRAFTING ARTIFACT**

- The employer's own body copy misspells the title: the description opens `"OVERVIEW Head of Aritficial Intelligence (AI) Overview At Alera Group..."` while the structured `job_title` field is `"Head of AI"` — **H** (EMPLOYER-SOURCED; re-verified at intake). This typo is the origin of the two competing titles in circulation.
- Searching the typo string `"Head of Aritficial Intelligence"` returns **zero** mirrors carrying it — corroborating that no aggregator has scraped the canonical text yet — **M** (negative finding)

**7. REQUIREMENTS PRESENT ON CANONICAL BUT ABSENT FROM THE GATE'S SUMMARY**

- Canonical carries a **certification clause** the LinkedIn summary dropped: *"Licensure (if applicable): Relevant AI, technology, risk management, or business leadership certifications preferred"* — preferred, not required — **H**
- Canonical's required-experience industry list is **broader than the gate captured** and explicitly names brokerage: *"10-15 years of progressive leadership experience in enterprise strategy, business transformation, technology-enabled operations, consulting, financial services, insurance brokerage, or a related industry"* — **H**
- Canonical's required-degree list is **broader than "MBA/advanced degree"** and includes a non-technical path: *"MBA, Master's degree, or other advanced education in Business Administration, Technology Management, Data Science, Artificial Intelligence, Engineering, Organizational Development, or a related discipline"* — **H**
- Canonical names **seven** partner functions, not four: *"Partner with Executive Leadership across Finance, Operations, Technology, Legal, Compliance, Communications, and Learning & Development"* — **H** (re-verified at intake)
- Travel language is scoped to a specific program: *"Occasional travel may be required to support office implementations, training, and collaboration with project teams"* — **H** (re-verified at intake)

**8. BOILERPLATE DIFF ACROSS CONCURRENT ALERA REQS**

- Head of AI (2026-08-20): *"Alera Group has grown to become the **12th largest** broker of U.S. business... Employee Benefits, Property & Casualty Insurance, and Financial Services"* — **H** (EMPLOYER-SOURCED)
- Implementation Lead – P&C req 7538 (2026-08-12) instead: *"one of the nation's leading independent insurance and financial services firms... Employee Benefits, Property & Casualty, Retirement Plan Services, Wealth Services, and **Human Capital Solutions**"* — **H** (EMPLOYER-SOURCED)
- Transformation Change Integration Leader (~2026-08-03): *"**14th largest** broker of U.S. business"* — https://bebee.com/us/jobs/transformation-change-integration-leader-alera-group-inc-us--t7xk-784184371 — **M** (AGGREGATOR-SOURCED scrape)
- Net: three concurrent Alera reqs carry three different company boilerplates, and the Head of AI's version omits Retirement Plan Services, Wealth Services, and Human Capital Solutions from Alera's practice list — **M**

**9. LANGUAGE DIFF — POSTING VAGUE vs. ORG STRATEGY SPECIFIC**

- **Gap A (governance).** Posting: *"Champion Responsible AI Practices by establishing governance models that ensure the ethical, secure, compliant, and transparent use of AI while effectively managing organizational risk."* Alera's own published position (2026-04-01) is far more specific and liability-first: *"If AI touches your professional services in any way — drafting, analysis, recommendations, decision support — you should assume it increases your exposure, rather than reducing it"* and *"Mandating human review of AI outputs helps reduce professional risk and makes you a more attractive client for the insurance company"* — https://aleragroup.com/insights/ai-isnt-liable-mistake-you-are — **H** (both EMPLOYER-SOURCED)
- **Gap B (the actual transformation program) — THE LOAD-BEARING DIFF.** Posting: *"defining and executing the organization's AI vision, strategy, governance framework, and investment roadmap to accelerate business transformation"* — names no system, no program, no unit. Alera's concurrent sibling req names all three: *"Join Alera Group's **Transformation Office** and lead the successful migration of our Property & Casualty offices to a **standardized enterprise platform centered on Applied Epic**"*, preferred quals naming *"Applied Epic or other Agency Management Systems (BenefitPoint, TAM, Zywave/BKB, Dynamics, Gen4, etc.)"* — https://careers.aleragroup.com/api/jobs?keywords=Implementation+Lead+Property+Casualty — **H** (both EMPLOYER-SOURCED; re-verified at intake). **The Head of AI posting never mentions the platform consolidation that its own "occasional travel… to support office implementations" phrase points at.**
- Sibling req detail confirmed at intake: the Implementation Lead leads a *"cross-functional implementation pod including Data Migration, Training, Hypercare, and local office Change Champions"* and partners *"to ensure successful office readiness and adoption"* — same URL — **H** (EMPLOYER-SOURCED)
- **Gap C (where Alera has actually shipped AI).** Posting frames AI as internal-only: *"helping transform how work gets done, how decisions are made, and how value is created across the enterprise."* Alera's only announced production AI deployment is client-facing and in a practice the req doesn't list — TIFIN @Work in Retirement Plan Services — https://www.prnewswire.com/news-releases/alera-group-deploys-tifin-works-ai-powered-platform-302315209.html — **H**
- **Gap D (regulatory specificity).** Posting: *"Stay Ahead of What's Next by monitoring emerging technologies, industry trends, and evolving regulations."* Alera already publishes concrete regulatory guidance: *"Plan sponsors should take measures to ensure that AI-driven systems are rigorously tested and continuously monitored"* (2024-12-02) — https://aleragroup.com/insights/what-dols-ai-guidance-means-plan-sponsors — **H**
- **Gap E (client-facing AI agenda absent from the req).** Alera has a client webinar scheduled 2026-11-17 covering *"Where AI is already being used within employee benefits to support administration, communications, and decision-making"* and *"Considerations for adopting AI responsibly within benefits programs, including oversight and controls"* — https://aleragroup.com/events/ai-advantage-benefits-practical-use-cases-support-hr-and-employees — **H**. The req's scope language is enterprise-internal and does not mention client-facing or practice-level AI.

**10. SIBLING AND PREDECESSOR REQS**

- **Predecessor AI-titled req, now CLOSED:** "AI and Security Administrator in Indianapolis, Indiana" = job **7344**. Canonical URL now returns **HTTP 404**; the LinkedIn version redirects to a generic search page; the Vaia mirror returns **HTTP 410 Gone**; the BeBee/Lensa mirror returns **404**. Google still indexes the canonical title — https://careers.aleragroup.com/company/jobs/7344?lang=en-us / https://www.linkedin.com/jobs/view/ai-and-security-administrator-at-alera-group-inc-4423311522 — **H** (existed and is now closed)
- That predecessor was **practitioner-level, hybrid Indianapolis, Microsoft 365 / Copilot / AI-agent design in a HIPAA-regulated environment, 5+ years experience** — i.e. Alera's prior AI hiring was an administrator seat, not an executive one — **M** (AGGREGATOR/search-snippet-sourced description)
- **This is a NEW seat, not a backfill.** No person with an AI-titled leadership role at Alera Group was found across LinkedIn, TheOrg, Crunchbase, Zippia, or Alera's own leadership pages — https://theorg.com/org/alera-group/teams/leadership-team — **M** (negative finding)
- **Concurrent live tech/transformation reqs** (all EMPLOYER-SOURCED via https://careers.aleragroup.com/api/jobs?keywords=transformation): Implementation Lead – Employee Benefits (7537, Remote, 2026-08-12, $100–150K); Implementation Lead – P&C (7538, Remote, 2026-08-12, $100–150K); Data Migration Specialist – Employee Benefits (7534, Remote, 2026-08-10, $80–120K); P&C Content Designer (7543, Remote, 2026-08-10, $60–75/hr, *"training materials… for Applied Epic and other P&C platforms"*); VP Finance Operations (6946, Remote, 2026-06-30, $225–260K); Risk Analyst (7563, Deerfield IL w/ remote option, 2026-08-21); Senior Recruiting Operations Coordinator (7464, Remote, 2026-08-21, $80–85K) — **H**
- **Concurrent transformation reqs visible only via aggregators:** Transformation Change Integration Leader (Remote, Corporate Services, $120–170K, *"supporting a One Alera Group transformation approach"*) — https://bebee.com/us/jobs/transformation-change-integration-leader-alera-group-inc-us--t7xk-784184371 — **M**; Transformation Change Manager (Front Office) — https://dailyremote.com/remote-job/transformation-change-manager-front-office-5076922 (fetch 403; title/employer from search index only) — **L**
- **Adjacent leadership req that CLOSED before this one opened:** VP, Learning & Development (Remote, $170–220K, 10+ yrs L&D incl. 5+ senior leadership) — Jobright reports it posted ~6 months prior and marks it *"This position has closed and is no longer accepting applications"* — https://jobright.ai/jobs/info/697be7cd0b88cc7d6422cbe6 — **M** (AGGREGATOR-SOURCED). Relevant because the Head of AI req names "Learning & Development" as a partner function and assigns it *"Drive Workforce Transformation by fostering AI readiness, advancing digital skills, leading change management efforts."*
- **Other recently-closed adjacent reqs** (Google-indexed canonical titles, URLs now HTTP 404): Manager, Integration Operations & Partnerships (7239) — https://careers.aleragroup.com/company/jobs/7239?lang=en-us — **H**; also indexed but unverified for liveness: Growth Leader (7221), Senior Analytics Consultant (6329) — **L**

**11. STRUCTURAL READ — REPORTING LINE**

- **The canonical req states no reporting line.** Full verbatim text contains no "reports to," no manager title, no department field beyond the corporate-functions framing: *"At Alera Group, our corporate teams play a critical role… From Human Resources and Finance to Technology, Legal, Marketing, and Operations."* The only relational language is the seven-function partner list — **H** (EMPLOYER-SOURCED; absence verified against complete text, twice)
- Nearest sourced structural facts: **John Mollica, Chief Information and Innovation Officer**, published scope *"the vision, strategy and operations for the firm's technology across the United States"*; promoted to CIIO effective 2022-06-06 from **Vice President of Business Intelligence and Transformation**, the release citing intent to *"leverage our technology and data capabilities to accelerate innovation"* — https://aleragroup.com/profile/john-mollica and https://aleragroup.com/news/alera-group-promotes-john-mollica-chief-information-and-innovation-officer — **H** (title/scope) — but **no source connects this req to him.**
- A named org unit exists that could house the seat: **"Alera Group's Transformation Office"** (employer-sourced, req 7538) — **H** that the unit exists; **no source ties the Head of AI to it.**
- Also sourced: **Matthew Mudry, Chief Information Security Officer** — https://www.linkedin.com/in/matthewmudry/ — **M**

**12. ELIGIBILITY FACTS (canonical, verbatim-verified)**

- Location/remote scope: **Remote, United States, nationwide, no state exclusions** (see §2) — **H**
- Travel: **"Occasional travel may be required to support office implementations, training, and collaboration with project teams"** — **H**
- Employment type: `FULL_TIME` — **H**
- Certifications: **preferred, not required** — **H**
- Degree: **advanced degree listed as a required qualification**, broad discipline list including Organizational Development — **H**
- Clearance: none mentioned; not applicable — **H**
- EEO boilerplate present; no state-specific pay-transparency addendum — **H**

---

### Not Found (mandatory)

- **Sponsorship / work-authorization / visa language** — searched the complete verbatim canonical description and the LinkedIn posting. **No statement either way.** Neither "will sponsor" nor "must be authorized without sponsorship" appears. (Moot for Jefferson — he is authorized — but flagged for completeness.)
- **Reporting line for the Head of AI seat** — searched: complete canonical req text; LinkedIn posting; aleragroup.com/profile/john-mollica; the Mollica promotion release; theorg.com; Crunchbase; Zippia; RocketReach; Equilar ExecAtlas; Alera news index. **No stated reporting line anywhere. Do not infer CIIO as fact.**
- **Repost history / any earlier version of this req** — searched: Alera ATS API with keywords `AI`, `artificial intelligence`, `Head of AI`, `technology`, `data`, `transformation`, `change`, `integration leader`, `Applied Epic`; the full 60-URL sitemap; Google/Bing `site:careers.aleragroup.com`; Jobright, BeBee, Lensa, Vaia, Remotive, TealHQ, ZipRecruiter, Glassdoor, Indeed, SimplyHired, Talent.com, Dice, FlexJobs, CareerBuilder, Simplify, DailyRemote; and a fingerprint search on the employer's own typo. **Result: exactly one Head of AI record has ever been observable. No prior posting under Head of AI, VP of AI, Chief AI Officer, Director of AI, Head of Data & AI, or AI Strategy.** Confidence this is a first posting: **M** (absence of evidence — Alera's ATS does not expose closed reqs and no archive exists).
- **Wayback Machine history** — queried `archive.org/wayback/available` for `careers.aleragroup.com/jobs/7564`, `careers.aleragroup.com/company/jobs/7564?lang=en-us`, and `linkedin.com/jobs/view/4457053864`. **All three return `"archived_snapshots": {}` — zero snapshots.** The `web.archive.org/cdx` API is blocked to this tool. **No archival diff of the 2026-08-20 21:32 edit is recoverable.**
- **Workday CXS endpoint** — the parent brief's premise that Alera has a 500ing Workday host did not hold up. Searched `aleragroup.*.myworkdayjobs.com` (wd1/wd5); POSTed/GET `https://aleragroup.wd1.myworkdayjobs.com/wday/cxs/aleragroup/External/jobs` → **HTTP 400**, no tenant. **Alera Group does not run Workday recruiting.** Surfaces are `careers.aleragroup.com` (corporate) and `agency-aleragroup.icims.com` (iCIMS, for the separate Alera Group General Agency entity).
- **Aggregator mirror of the Head of AI req** — none found on any of the 14 boards listed. Consequently **no cross-board comp discrepancy and no aggregator salary estimate exists to flag.**
- **Third-party recruiter or retained search firm fronting the req** — none found.
- **Applicant-count trajectory** — only one observation ("Over 200 applicants," 2026-08-24). No historical snapshots exist to build a curve.
- **Named hiring manager or recruiter on the req** — only the internal owner code `#LI-BH1`. No name published; the initials do not match the one Alera TA person located by name (William Zajac).
- **Canonical req IDs for "Transformation Change Integration Leader" and "Transformation Change Manager (Front Office)"** — not on careers.aleragroup.com; neither returned by the ATS API across five keyword queries; neither in sitemap1.xml. Both are aggregator-only sightings.
- **A formal Alera announcement of the Applied Epic / BenefitPoint platform consolidation** — searched Alera's news and insights indexes plus general web. **The program is documented only in Alera's own job postings, not in any press release.**

---

### Collector Notes (facts only — ambiguities, conflicting sources)

- **Title conflict is internal to the employer, not a board artifact.** Structured `job_title` = "Head of AI"; the description's own first line = "Head of Aritficial Intelligence (AI)," misspelled. Both are req 7564.
- **The careers site's `/api/jobs` endpoint is relevance-ranked and caps output.** `limit=100` and `limit=60` both returned only ~4 records. **Absence of a job from an API keyword query is therefore NOT evidence the job is closed.** The reliable liveness test is a direct fetch of `/company/jobs/<id>?lang=en-us`: live reqs return `<title>` "<Job Title> in <Location> | Alera Group"; closed reqs return HTTP 404 (verified: 7239 → 404, 7344 → 404, 7564 → live title).
- **Job pages are JS-rendered with no server-side JSON-LD.** A naive fetch returns generic careers-portal chrome and looks like a dead link — almost certainly why the gate could not reach the canonical req. The `/api/jobs` endpoint and the page `<title>` are the two working extraction paths. **This is a reusable tooling finding: add it to reference/research-tooling.md.**
- **Job IDs are sequential by creation.** 7564 sits below 7569, 7592, and 7610 (all live), so at least three reqs were created after the Head of AI. This does not indicate any repost.
- **CEO title conflict in third-party sources:** Zippia lists Alan J. Levitz as CEO; Crunchbase lists him as Executive Chairman. Both third-party. First-party leadership page says Jim Blue is CEO. Not load-bearing.
- **Boilerplate rank conflict unresolved:** "12th largest" (Head of AI, employer-sourced) vs "14th largest" (Transformation Change Integration Leader, aggregator-scraped; and LinkedIn company-page copy). Cannot determine whether this is a ranking update, a template fork, or a scraper serving stale text.
- **The two strongest actionable archaeology signals** are both employer-sourced and both invisible from LinkedIn: (a) the **hard 2026-09-25 posting expiry**, and (b) the fact that the req's travel clause — *"to support office implementations, training"* — points at a transformation program the req never names, which Alera's sibling reqs describe explicitly as the **Transformation Office's Applied Epic / BenefitPoint migration waves**, complete with implementation pods containing Training and local office Change Champions.
- The parent brief's "occasional travel" and comp figures all check out verbatim against the canonical. The one item the canonical contradicts by omission is the requirements framing: canonical explicitly includes "insurance brokerage" and "Organizational Development" as acceptable backgrounds, which **widens** the qualification surface relative to the gate's summary.
