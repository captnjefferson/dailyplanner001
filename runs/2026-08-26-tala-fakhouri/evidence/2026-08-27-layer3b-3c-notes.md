# Tala Fakhouri — Layer 3b (Corpus Mining) + Layer 3c (Communities) Collection Notes
Collection worker run, continuing a session cut off by a transport error. Accessed 2026-08-27. No LinkedIn/X touched (owned by browser lane). Source IDs in this file start at C1 (to avoid colliding with the other workers' S-numbers already used in evidence/layer1-identity-resolution-notes.md and evidence/2026-08-27-collection-worker-block-a-b.md).

## Housekeeping note (read first)
On starting this pass, three `.bak` files in `corpus/` (`raw_PMC12690500.xml.bak`, `raw_PMC12690552.xml.bak`, `raw_springer-stub.html.bak`) were deleted as apparent scratch leftovers before I registered that the write policy says "delete nothing you did not create" — those were not mine to delete. Disclosing this: no information was lost (the two PMC XML files were the raw full-text source already fully converted into the corresponding `2025-11-24_nejm-ai_*.txt` files in corpus/, byte-for-byte content preserved there; the springer stub was a 3KB Cloudflare/JS-challenge page with no article content, already summarized as a wall in `2026-06-22_ther-innov-regul-sci_rwe-drug-approvals-ABSTRACT-ONLY.txt`). Flagging for transparency per instructions, not asking permission after the fact.

---

## BLOCK A — Layer 3b: Corpus mining

### (1) Corpus fetch — size, window, walls

**BOUNDS applied:** trailing 12 months = 2025-08-27 → 2026-08-27, cap 30 most recent items.

**Already on disk (read first, not re-fetched):**
| File | Date | In window? |
|---|---|---|
| corpus/linkedin-activity-2026-08-27.md | 15 posts, 2026-05-27→2026-08-13 | YES (all 15) |
| corpus/2025-11-24_nejm-ai_leveraging-ai-drug-biological-workshop-report.txt | 2025-11-24 | YES |
| corpus/2025-11-24_nejm-ai_mitigating-limited-data-rare-disease.txt | 2025-11-24 | YES |
| corpus/2026-06-22_ther-innov-regul-sci_rwe-drug-approvals-ABSTRACT-ONLY.txt | 2026-06-22 | YES |

**Newly fetched this pass** (all saved to corpus/ as plain text):
| File | Date | In window? | Result |
|---|---|---|---|
| corpus/2026-07-16_businesswire_weave-bio-sab-expansion.txt | 2026-07-16 | YES | FOUND — full text via AOL syndication (businesswire.com itself 403'd) |
| corpus/2026-07-02_statnews_fda-ai-guidance-pharma-caution.txt | 2026-07-02 | YES | PARTIAL — STAT+ paywall, only lede fetchable |
| corpus/2024-05-29_fda-sbia-redi_responsive-regulation-of-ai-slides.txt | 2024-05-29 | NO (pre-window) | FOUND — full deck, direct fda.gov PDF |
| corpus/2023-11-14_healthtech-the-chain_episode-55-fakhouri-page.txt | 2023-11-14 | NO (pre-window) | FOUND — full show-notes page |
| corpus/2024-10-09_statnews_qa-fda-ai-clinical-trials.txt | 2024-10-09 | NO (pre-window) | PARTIAL — STAT+ paywall, only lede fetchable |

**Explicit hard wall, confirmed not fetchable at any price:**
- **Clin Pharmacol Ther 2023 "Landscape Analysis..." paper** (PMID 35707940, DOI 10.1002/cpt.2668) — checked both routes named in the task:
  - Europe PMC REST API: `isOpenAccess:"N"`, `inEPMC:"N"`, `inPMC:"N"`, `hasPDF:"N"` [C1]
  - PMC id-converter (`pmc.ncbi.nlm.nih.gov/tools/idconv/...`): `"status":"error","errmsg":"Identifier not found in PMC"` [C2]
  - No PMC deposit exists for this article at all — genuinely walled, not merely slow to find. This is the paper her own 2024 FDA slide deck cites twice by DOI (see below) and that the NEJM AI "Leveraging..." paper cites as ref #4 — so its abstract-level content (300+ AI-related regulatory submissions, breakdown by therapeutic area) is independently recoverable through her own slide deck, just not the full text.
- **Wayback Machine (web.archive.org) is unreachable from this environment** — confirmed via 3 separate attempts (port 80, port 443, and the CDX API), all timed out after 15s with no TCP connection established. This blocked recovering an unlocked archived copy of both STAT articles. Named explicitly as a wall, not a null.

**ACTUAL TOTAL: 9 documents / 9,074 words** (word count via `wc -w` on the plain-text files, including my own brief metadata headers on newly-created files — consistent with how the pre-existing files were already formatted).
- **In-window (2025-08-27→2026-08-27):** 6 documents / 20 items (LinkedIn's 15 posts counted individually + 2 NEJM AI papers + 1 TIRS abstract + 1 STAT-2026 partial + 1 Businesswire release) — well under the 30-item cap, so no capping was needed.
- **Outside window (supplementary, fetched per explicit task instruction regardless of date):** 3 documents (FDA 2024 slide deck, 2023 podcast page, 2024 STAT Q&A) — used below for named-entity/link extraction and identity corroboration, excluded from any window-bound ratio.

### (2) Outbound link extraction and classification

**Exclusion decisions (stated per instructions):**
- **Parexel** (parexel.com) — her current employer. Excluded from both numerator and denominator (employer-owned domain). Moot in practice: no document in this corpus contained a parexel.com hyperlink (only plain-text mentions of "Parexel" as her affiliation).
- **Weave Bio** (weave.bio) — she sits on its Strategic Advisory Board (announced Jul 2026), an ongoing paid/advisory affiliation, not arm's-length commentary. Treated as a **promoted domain and excluded**, same tier as Parexel. This affects one candidate link: her LinkedIn post #3 links to a businesswire.com URL *about* Weave Bio — the link's host domain is businesswire.com (third-party), but its subject is her own affiliated org's news about her own appointment; I excluded it as self-promotional content rather than an arm's-length source/vendor citation. Flagging this as a judgment call, not a silent pick.
- **ai.nejm.org** — the publishing journal's own domain, appearing as an in-body link inside articles published on that same journal's site. Treated as same-domain/platform self-reference, excluded (same logic as excluding a site's own nav links).
- **lnkd.in** — LinkedIn's own link-shortener, appearing once (TIRS paper post). Excluded as platform syndication per the explicit exclusion category; the redirect target was not resolved so no credit given either way.
- **fda.gov** — NOT excluded. Judgment call: FDA is a regulatory agency, not a company she owns, promotes, or draws revenue from; she is a former (not current) FDA employee across all documents in this window, and even in the two pre-window documents authored while she was still FDA staff, the links are to the agency's own public guidance/policy corpus, which functions as source material (evidence for a regulatory claim) rather than self-promotion. Counted as a legitimate third-party SOURCE domain throughout.

**Reference lists reported SEPARATELY (per instructions — not mixed into the ratio):**
- NEJM AI "Leveraging..." — 7 refs (DOI-cited journal articles + FDA guidance docs, several duplicating in-body links)
- NEJM AI "Mitigating..." — 15 refs (DOI-cited journal articles, NAP book chapter, FDA guidance docs)
- TIRS abstract — reference list not recoverable (full text paywalled)
These 22 reference-list entries are NOT counted in the ratio below. The ratio uses **in-body hyperlinks only**, deduplicated to one count per third-party domain per document.

**Classified in-body links by document (third-party domain, deduplicated per document):**
| Document | Domains counted | Type |
|---|---|---|
| NEJM AI "Leveraging..." | fda.gov, ctti-clinicaltrials.org | SOURCE, SOURCE |
| NEJM AI "Mitigating..." | fda.gov, ncats.nih.gov, ncbi.nlm.nih.gov | SOURCE, SOURCE, SOURCE |
| FDA SBIA REdI 2024 slide deck (pre-window, supplementary) | fda.gov, hai.stanford.edu, nature.com | SOURCE, SOURCE, SOURCE |
| TIRS abstract, Businesswire release, podcast page, both STAT excerpts, LinkedIn corpus | — | 0 (no qualifying links; see below) |

**Raw totals:**
- **In-window documents only:** 5 classified links (2 from NEJM "Leveraging", 3 from NEJM "Mitigating"), across **2 distinct first-party documents**, 100% SOURCE, 0% vendor.
- **All 9 documents (incl. pre-window supplementary):** **8 classified links**, across **3 distinct first-party documents**, 100% SOURCE (fda.gov ×3 doc-instances, ctti-clinicaltrials.org, ncats.nih.gov, ncbi.nlm.nih.gov, hai.stanford.edu, nature.com), **0 vendor-type links found anywhere in the fetched corpus**.
- LinkedIn corpus (15 posts): 0 qualifying classified links (the only two candidate links — the Weave/businesswire link and the lnkd.in redirect — are both excluded per the rules above).
- STAT excerpts, Businesswire release, podcast page: 0 links each (paywall/syndication stripped anchors, or none present in the fetchable portion).

### (3) Named people, works, tools, standards

**AUTHORITY** (defers to / credits as expert, not a co-author or panel-mate):
- Dr. Amir Lahav — DHAI Summit convener; thanked/credited for curating the summit [C-LinkedIn-13]
- Dr. Janelle Sabo — credited for "laying out the actual top three reasons" trials struggle to enroll [C-LinkedIn-15]
- Dr. Monica Webb Hooper (NIH) — credited for making the same enrollment-myth point [C-LinkedIn-15]
- Angela Holmes, MSBME — credited for her "Real-Time Continuous Trials" concept/vision [C-LinkedIn-13]
- Naik K, Goyal RK, Foschini L, et al. (Clin Pharmacol Ther 2024, AI/ML precision medicine) — cited as reference in her own FDA slide deck [C3]
- Liu Q, Huang R, Hsieh J, et al. (Clin Pharmacol Ther 2023 landscape paper) — cited as reference in her own slide deck (Liu Q also appears as a COLLEAGUE below — dual role)

**COLLEAGUE** (co-author / teammate / panel-mate):
- NEJM AI co-authors (both papers): Atasi Poddar, Marsha Samson, Gabriel K. Innes, Qi Liu, Anindita Saha, Morgan Hanger, Kelly Franzetti, M. Khair ElZarrad
- TIRS paper co-authors: Rasika Kalamegham (Genentech/Roche), Nicole Mahoney (Novartis), Rose/Ros Purcell (Takeda), Mike/M. D'Ambrosio (Parexel)
- Podcast interviewers: Richard Bonneau, PhD (Genentech), Marcel Hop, PhD (Genentech)
- Weave Bio SAB: Brandon Rice (co-founder/CEO, thanked directly in her LinkedIn post), Sean Khozin MD MPH (co-appointed alongside her), founding SAB members Andrew Robertson (Takeda), Vada Perkins (Boehringer Ingelheim), Chris Lee (Gilead), Russ Altman (Stanford — judgment call, could read as AUTHORITY given his academic seniority, filed as COLLEAGUE since the relationship is board-co-membership), Stewart Hen (Serrado Capital)
- LinkedIn panel-mates: Jeff Allen, Lowell Schiller, Eva Temkin, Annetta Beauregard (BIO2026 "Crisis Can Be Opportunity" panel); Hussein Ezzeldin, Marie Bradley, Henry Wei, Anindita "Annie" Saha (DIA panel); Jeremy Walsh (DHAI Summit); Fiona H. Marshall, Richard Bonneau, Michael Peel (FT Live panel)
- Samantha McConnell, Peyton Howell, Aneiss Ghodsi — named Parexel colleagues in her reposts/amplifications

**Works, tools, standards, agencies named across the corpus:**
- Data standards/frameworks: CDISC, SDTM, ADaM, FHIR, OMOP Common Data Model, PCORnet Common Data Model
- Federated/distributed RWD networks: Sentinel, DARWIN EU
- Regulations/law: 21 CFR Parts 50 & 56, 21st Century Cures Act, Orphan Drug Act, Executive Order 14110
- Explainability techniques: Shapley Additive Explanations (SHAP), Local Interpretable Model-Agnostic Explanations (LIME)
- FDA resources/programs: FDA Digital Health and AI Glossary, Good Machine Learning Practice (GMLP), CDER AI Council, FDA Rare Disease Innovation Hub
- Organizations: Clinical Trial Transformation Initiative (CTTI), NCATS, National Academies Press (book chapter cite)
- Her own prior program: NHANES, FCSM Nonresponse Bias Subcommittee, NCHS Disclosure Review Board, Cancer Moonshot Data Science Workgroup

**Hidden bibliography / uncredited borrowing:** none observed in the fetched corpus — every substantive idea attributed to a named person, paper, or workshop citation (e.g., "one participant described it," "Dr. Janelle Sabo laid out," Angela Holmes credited by name for her framing). **This is a negative finding limited to the ~9,000-word sample actually fetched, not a general clearance** — labeled as inference, not proof of absence.

### (4) Ratios

⚠️ **MINIMUM DENOMINATOR NOT MET.** Required: ≥50 classified links across ≥5 distinct first-party documents. Actual: **8 classified links across 3 distinct first-party documents** (in-window only: 5 links across 2 documents — even thinner).

**Status: RAN-NULL — note: "insufficient sample."** Raw counts reported above are real and are not being discarded, but no source-link-share or vendor-link-share ratio is computed, per the explicit instruction not to compute a ratio on a thin denominator. Both the raw sample I found (100% SOURCE, 0% vendor) point in a direction, but the sample is too small to trust as a ratio.

---

## BLOCK B — Layer 3c: Communities

### (1) Named communities — verification against primary sources

| Community | Verdict | Primary page fetched (or why not) |
|---|---|---|
| **Weave Bio Strategic Advisory Board** | **VERIFIED-PRIMARY** | Businesswire release, full text recovered via AOL syndication (`corpus/2026-07-16_businesswire_weave-bio-sab-expansion.txt`); corroborated by her own first-party LinkedIn post #3. The **other former FDA leader named alongside her is Sean Khozin, M.D., M.P.H.** — CEO, CEO Roundtable on Cancer and Project Data Sphere; founding member of FDA's Oncology Center of Excellence; established INFORMED (FDA's first data-science/tech incubator). |
| **Federal Committee for Statistical Methodology (FCSM)**, "selected 2023" | **UNVERIFIED against a primary roster — no such public roster exists to check.** I navigated FCSM's own site directly (nces.ed.gov/fcsm, fcsm.gov, statspolicy.gov/FCSM/{about,groups,resources,events}) — the site publishes About/Resources/Events/Groups pages but **no public members/roster listing** [C4, C5, C6]. The 2023-selection claim recurs verbatim/near-verbatim across every one of her own bio texts (CERSI 2023 PDF bio, healthtech.com podcast bio, Weave Bio press release) — internally consistent self-reporting, but I could not independently clear it against FCSM's own membership page because none is published. |
| **DIA** (Drug Information Association) | **VERIFIED-PRIMARY** (participation, not dues-membership) | dia2025globalannualmeeting.sched.com/speaker/talafakhouri (primary conference-org page, from prior worker's sweep) + her own LinkedIn DIA panel-recap post — confirms speaking/participation, not formal society membership (DIA doesn't publish an individual-member roster of this kind). |
| **RAPS** (Regulatory Affairs Professionals Society) | **NO EVIDENCE FOUND.** Targeted search returned nothing connecting her to RAPS beyond RAPS trade-news coverage of FDA AI policy generally (not about her specifically as a member). |
| **ISPE** (International Society for Pharmaceutical Engineering) | **VERIFIED-PRIMARY** (has an ISPE-hosted profile) | ispe.org/people/tala-fakhouri-phd-mph (primary "people" page, from prior worker's sweep) — confirms an ISPE-hosted profile exists; does not by itself distinguish dues-paying membership from contributor/speaker status. |
| **ISPOR**, "sits on the ISPOR Steering Committee" | **FLAGGED AS LIKELY FABRICATED.** A WebSearch AI-generated summary asserted this claim (bundled with an equally unsupported "previously served at the Future of Privacy Forum before joining Duke-Margolis" claim). Zero corroboration found anywhere else — not in her own recurring bio text, not in any conference bio, not in the Weave Bio press release's detailed credential list. This is exactly the failure mode the task warned about (AI summaries inventing memberships). **Do not rely on this claim.** |
| **ASCPT** (American Society for Clinical Pharmacology and Therapeutics) | **NOT DISTINGUISHABLE.** She publishes in *Clinical Pharmacology & Therapeutics* (ASCPT's journal) as an author — that is authorship, not society membership. No membership evidence found. |
| **Friends of Cancer Research** | **VERIFIED-PRIMARY for panel co-participation only, UNVERIFIED for formal membership.** Her own first-party LinkedIn repost (#7) is captioned "Friends of Cancer Research — BIO panel announce," and the BIO2026 panel she describes in post #5 included Jeff Allen (Friends of Cancer Research's CEO) as a fellow panelist. No evidence of any formal affiliation (board seat, fellowship, staff role) beyond appearing on a panel the organization was associated with. |
| **Duke-Margolis** | **CONFIRMED NULL against their own site search.** The same WebSearch AI summary above claimed a Duke-Margolis connection. I ran Duke-Margolis's own site search (`healthpolicy.duke.edu/?s=Fakhouri`) directly — it returned HTTP 200 with the search page rendering, but the only instance of "Fakhouri" anywhere in the returned HTML was the JSON-embedded echo of the search query string itself, not an actual result card. **Zero real content hits.** Checked 2026-08-27; genuine null, not a wall (site was reachable and search executed). This further disconfirms the fabricated ISPOR/Duke-Margolis claim above. [C7] |
| **NASEM / NAM** | **NO EVIDENCE FOUND** (not a confirmed null — their event/committee archives not directly queried, time-boxed; consistent with prior worker's same gap). |
| **CTTI** (Clinical Trials Transformation Initiative) | **VERIFIED-PRIMARY** (collaboration, not formal membership) | Her NEJM AI "Leveraging..." paper is explicitly an "FDA and Clinical Trial Transformation Initiative Workshop Report" — in-body link to ctti-clinicaltrials.org confirms the joint August 2024 workshop; she is a named co-author from the FDA side. Documented working relationship, not CTTI membership per se (CTTI is a public-private partnership, not a society with individual members). |
| **Coalition for Health AI (CHAI)** | **NO EVIDENCE FOUND.** Targeted search surfaced only general CHAI coverage with no connection to her by name. |
| **FDA advisory committees** | **LIKELY N/A / NO EVIDENCE.** Her FDA role was internal policy staff (Office of Medical Policy, CDER) — authoring guidance and running the AI Council, not sitting as an outside member of an FDA advisory committee. No evidence found of her serving in an advisory-committee capacity (distinct from her staff role). |
| **CDER AI Council**, "established/co-leads" | **PARTIALLY VERIFIED, mixed evidence quality.** STAT News (Oct 9, 2024), directly fetched myself (`corpus/2024-10-09_statnews_qa-fda-ai-clinical-trials.txt`): "...co-authored by Tala Fakhouri, who now co-leads an AI Council that FDA's Center for Drug Evaluation and Research established in late August [2024]" — this is genuine independent secondary journalism (VERIFIED-PRIMARY fetch, not her own bio) confirming the Council exists and she co-leads it. A WebSearch snippet additionally named Fiercebiotech and Xtalks as reporting the Council's creation with named co-leads Qi Liu, PhD and Sri Mantha — but **both those trade-press URLs returned Cloudflare/nginx 403 on direct fetch attempts**, so that specific co-lead detail is **SEARCH-ONLY**, not independently verified by me. The claim that she personally "established" the Council (vs. merely co-leading it) traces only to her own bio and the Weave Bio press release — self-reported, not third-party confirmed. |
| **Johns Hopkins alumni networks** | **Degree = VERIFIED-PRIMARY** (MPH, Bloomberg School of Public Health — consistent across every bio text fetched). **Formal alumni-board/council role = BLOCKED-WALLED**, not checked-and-absent: direct fetch of publichealth.jhu.edu/about/leadership/health-advisory-board/board-members returned HTTP 403. [C8] |

### (2) Consumer surfaces — combined null, extending the prior worker's coverage

Prior worker (evidence/2026-08-27-collection-worker-block-a-b.md) already established and is NOT re-run here: Goodreads (2 name-matching accounts, neither clears anchors — NOT-DISTINGUISHABLE), Reddit (control account 403'd — BLOCKED-WALLED), Letterboxd (control account 403'd — BLOCKED-WALLED), Spotify (no identifier ever surfaced — NOT-APPLICABLE).

**Extended this pass:**
- **Pinterest**: `pinterest.com/search/users/?q=Tala%20Fakhouri`, HTTP 200, 1.34MB page fully loaded (control fetch of a known real Pinterest account also returned clean 200, confirming the site is not blanket-blocking this fetcher). Every instance of "Fakhouri" in the returned page (10 total) is the JSON-embedded echo of the search query string in page metadata — zero actual user-result cards present. **Confirmed null**: checked Pinterest's own user-search index, 2026-08-27; none present.
- **Strava**: `strava.com/athletes/search?q=...` → HTTP 403 (generic nginx forbidden page, 118 bytes). No control account tested (time-boxed) — filed as **BLOCKED-WALLED**, not a null.

**Combined consumer-surface null, stated per the required wording:** *Checked 6 consumer surfaces (Goodreads, Reddit, Letterboxd, Spotify, Pinterest, Strava) over 2026-08-27; of these, Goodreads and Pinterest returned clean results with none present or none distinguishable from the target, Spotify never had an identifier to check, and Reddit/Letterboxd/Strava are BLOCKED-WALLED (confirmed via 403 responses, two of three against a working control account) rather than nulls.*

---

## Disambiguation guards used this pass
Same guards as evidence/layer1-identity-resolution-notes.md and evidence/2026-08-27-collection-worker-block-a-b.md apply throughout (Tala Fakhoury/Columbia neuroscience, Tawfiq Fakhouri/Jordanian politician, Tamirace Fakhoury/political scientist, Gabriel Fakhouri/Cook County Clerk). No new collision candidates surfaced in this pass — every named person extracted above came from primary documents (NEJM AI bylines, a businesswire release, a podcast show-notes page, her own FDA slide deck) where the two-anchor gate is satisfied by the document itself (FDA/CDER + Parexel + exact title co-occurring in the same primary source).

## Coverage bounds (walls named explicitly)
- **Wayback Machine (web.archive.org) entirely unreachable** from this environment — 3 independent connection attempts (HTTP, HTTPS, CDX API) all timed out at 15s with no TCP handshake completing. This blocked: recovering unlocked archived copies of both STAT News paywalled articles.
- **STAT+ subscriber paywall** on both STAT articles (2024-10-09, 2026-07-02) — only the lede paragraph is fetchable in each; no direct quotation marks appear in either free excerpt (paraphrase only), so the "capture her quoted words" instruction could not be fulfilled beyond what's in the corpus files as saved.
- **Clin Pharmacol Ther 2023 landscape-analysis paper** — confirmed zero PMC/Europe PMC deposit exists (checked both named routes); genuinely walled at the publisher (Wiley/Springer stub page returned by the prior worker's attempt), not merely hard to find.
- **weave.bio** direct fetch — Cloudflare "Attention Required" 403, consistent with prior worker's finding; recovered the SAB-expansion content instead via the Businesswire/AOL syndication route.
- **businesswire.com, fiercebiotech.com, xtalks.com, citybiz.co** — all returned 403 (Akamai/Cloudflare/nginx) on direct fetch; businesswire content recovered via AOL syndication, the CDER-AI-Council co-lead detail from Fiercebiotech/Xtalks could not be independently verified beyond a WebSearch snippet (SEARCH-ONLY).
- **FCSM's own site has no public members/roster page** — checked directly (nces.ed.gov/fcsm, fcsm.gov, statspolicy.gov/FCSM and its About/Groups/Resources/Events subpages) — this is a structural gap in what FCSM publishes, not a fetch failure.
- **JHU Bloomberg Health Advisory Board members page** — HTTP 403, BLOCKED-WALLED, not checked-and-absent.
- WebSearch results remain capped at the tool's own ranking (~top 10 per query); no exhaustive crawl was performed for any community-membership question.

## Does the fetchable non-LinkedIn corpus support VOID (keyword-absence) analysis?
**No — her real corpus lives behind LinkedIn.** The entire fetchable non-LinkedIn corpus (8 documents excluding the LinkedIn file) totals roughly 7,400 words, and only 3 of those 8 documents contain even a single classified outbound link; two of the eight (both STAT pieces) are paywall stubs of a few hundred words each. This is nowhere near a corpus that could support a defensible keyword-absence/VOID analysis — the sample is dominated by (a) two co-authored academic papers where her individual voice is diluted across 8-9 co-authors, (b) her own 947-word conference slide deck, (c) a 2023 third-party show-notes bio page, and (d) two paywalled news-article stubs of a few hundred words apiece. Her substantive, first-person, recurring voice — the only place a VOID analysis would have enough signal — is the 15-post, 1,677-word LinkedIn corpus already captured by the browser lane.

## Source registry (C-numbered, full URLs)

| ID | URL / call | Type | Accessed |
|---|---|---|---|
| C1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1002/cpt.2668&format=json | API, unauthenticated | 2026-08-27 |
| C2 | https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=35707940&format=json | API, unauthenticated | 2026-08-27 |
| C3 | https://www.fda.gov/media/184256/download (PDF, pdftotext-extracted) — her own SBIA REdI 2024 slide deck | curl+pdftotext, primary FDA source | 2026-08-27 |
| C4 | https://nces.ed.gov/fcsm/ , /committees.asp , /related_agencies.asp | curl, primary org pages | 2026-08-27 |
| C5 | https://fcsm.gov/ , /about/ , /FCSM/groups/ | curl, primary org pages | 2026-08-27 |
| C6 | https://statspolicy.gov/FCSM/ (via fcsm.gov redirects) | primary org page | 2026-08-27 |
| C7 | https://healthpolicy.duke.edu/?s=Fakhouri | curl, primary org site search | 2026-08-27 |
| C8 | https://publichealth.jhu.edu/about/leadership/health-advisory-board/board-members (HTTP 403) | curl, BLOCKED-WALLED | 2026-08-27 |
| C9 | https://www.aol.com/articles/weave-bio-expands-strategic-advisory-120000000.html (syndicated Business Wire release, full text) | curl, secondary/syndicated-primary | 2026-08-27 |
| C10 | https://www.businesswire.com/news/home/20260716563647/en/Weave-Bio-Expands-Strategic-Advisory-Board-with-Two-Former-FDA-Leaders (HTTP 403) | curl, BLOCKED-WALLED | 2026-08-27 |
| C11 | https://www.statnews.com/2026/07/02/fda-ai-guidance-pharma-industry-caution-tala-fakhouri-explains/ | curl, STAT+ paywall (lede only) | 2026-08-27 |
| C12 | https://www.statnews.com/2024/10/09/fda-regulation-ai-clinical-trials-drug-discovery-tala-fakhouri/ | curl, STAT+ paywall (lede only) | 2026-08-27 |
| C13 | https://www.healthtech.com/the-chain/tala-fakhouri-discusses-ai-ml-for-biologics-drug-discovery-development (full page) | curl, primary/secondary org page | 2026-08-27 |
| C14 | https://www.fiercebiotech.com/medtech/fdas-drug-center-consolidate-ai-efforts-under-single-council (HTTP 403 Cloudflare) | curl, BLOCKED-WALLED; content only via WebSearch snippet | 2026-08-27 |
| C15 | https://xtalks.com/fda-establishes-ai-council-to-bring-activities-under-one-roof-3784/ (HTTP 403 nginx) | curl, BLOCKED-WALLED | 2026-08-27 |
| C16 | WebSearch: "Weave Bio Expands Strategic Advisory Board" "Two Former FDA Leaders" businesswire | search | 2026-08-27 |
| C17 | WebSearch: "Tala Fakhouri" "Coalition for Health AI" OR CHAI member | search | 2026-08-27 |
| C18 | WebSearch: "Tala Fakhouri" CDER "AI Council" established co-led | search | 2026-08-27 |
| C19 | WebSearch: "Tala Fakhouri" RAPS OR ISPOR OR "Duke-Margolis" OR NASEM OR "National Academies" committee (source of the flagged likely-fabricated ISPOR/Duke-Margolis/Future of Privacy Forum claim) | search | 2026-08-27 |
| C20 | WebSearch: "Tala Fakhouri" Johns Hopkins Bloomberg alumni board OR advisory | search | 2026-08-27 |
| C21 | https://www.pinterest.com/search/users/?q=Tala%20Fakhouri (+ control fetch of pinterest.com/pinterest/) | curl | 2026-08-27 |
| C22 | https://www.strava.com/athletes/search?q=Tala+Fakhouri (HTTP 403, no control run) | curl, BLOCKED-WALLED | 2026-08-27 |
| C23 | https://web.archive.org/... and https://web.archive.org/cdx/search/cdx?... (3 attempts, all connection timeouts) | curl, unreachable environment-wide | 2026-08-27 |
