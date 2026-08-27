# Layer 1 — Identity Resolution: Tala Fakhouri — Collection Notes
Run date: 2026-08-27. Collection worker output (no strategic claims).

## Target confirmation anchors (from assignment, treated as given/pre-verified by LinkedIn lane)
- Parexel, Chief AI & Regulatory Strategy Officer
- Prior: US FDA
- Location: Bethesda, MD
- Education: Johns Hopkins (MPH)
- LinkedIn: https://www.linkedin.com/in/talafakhouri/ (VERIFIED-AUTHENTICATED, out of my scope)

## Step 1 — Published/self-owned email
- No self-owned personal email, personal site, or ORCID-listed email found.
- ORCID record (0000-0002-0523-3466) fetched directly via public API (pub.orcid.org): name only, all other fields (bio, email, researcher URLs, external IDs) empty/not public. [S7]
- FDA guidance documents (primary, PDF text-extracted directly, not search snippets) list her as point of contact with PHONE only: "For questions regarding this draft document, contact (CDER) Tala Fakhouri, 301-837-7407" — confirmed verbatim in three separate FDA PDFs. No email address appears in any of the three PDF bodies. [S1, S2, S3]
- Third-party scraper sites (ZoomInfo, SignalHire) report Tala.Fakhouri@fda.hhs.gov — this is the standard federal firstname.lastname@fda.hhs.gov pattern, NOT found printed in any primary FDA document I could locate. Per evidence contract this is an EMPLOYER-PATTERN GUESS and stays UNVERIFIED. [S4, S5]
- No Parexel employer-pattern email found or guessed (out of scope — guesses aren't asserted).
- Podcast RSS (see Step 4) itunes:owner block has no itunes:email tag, only itunes:name = "Cambridge Healthtech Institute" (the publisher, not the guest). [S12]

## Step 2 — Bounded Maigret handle sweep
Variants generated: tala.fakhouri, tfakhouri, talafakhouri, talaf, talahfakhouri (5th variant uses middle initial "H" — confirmed real, from "Tala H. Fakhouri" byline used consistently in Parexel/FDA bios).
Command run verbatim per variant (max 6, 5 used):
`~/Sites/hm-outreach/tools/venv-maigret/bin/maigret <handle> --json simple --no-progressbar --no-recursion --no-extracting --top-sites 500 --timeout 15 --folderoutput .../maigret/`

Results (raw JSON saved in maigret/ dir):
| variant | sites attempted | accounts found | extended info extracted | bot-protection errors |
|---|---|---|---|---|
| tala.fakhouri | ~509 | 18 | 0 | 6.09% |
| tfakhouri | ~509 | 17 | 0 | 6.88% |
| talafakhouri | ~509 | 29 | 0 | 6.29% |
| talaf | ~509 | 81 | 0 | 6.88% |
| talahfakhouri | ~509 | 6 | 0 | 6.68% |

Total: 151 raw hits across ~2,545 site-checks (coverage ≈ 5 × ~509 sites, hit rate ≈ 5.9%). Extended-info (bio-text) extraction was disabled per the required command flags (`--no-extracting`), so **zero** hits carry any scraped bio text — none can be checked against the two-anchor gate from maigret data alone. All hits landed on generic username-squatting platforms unrelated to pharma/regulatory work (Genius, Vivino, fixya, Championat, Pling, joyreactor.cc, Duolingo, Venmo, PayPal.me, xHamster, GitHub Gist, Twitter [talahfakhouri only], etc.) — classic common-username coincidence, especially "talaf" (81 hits, effectively an unbounded generic 5-letter string). **None of the 151 hits clear the two-anchor gate; all are filed as unconfirmed noise, not accounts belonging to the target.**
Notable: `talahfakhouri` returned a Twitter/X hit (https://twitter.com/talahfakhouri) — NOT pursued per scope (X is walled to me, owned by the LinkedIn/X lane). Flagging as an unverified lead for that lane only.

## Step 3 — Quoted distinctive-bio search
Searched distinctive phrases unique to her bio ("established the CDER AI Council", "Senior Health Scientist and Chief Statistician" + NHANES). Returns were consistent: the same bio text (or close paraphrases of it) recurs verbatim/near-verbatim across Parexel, ISPE, ADAPT conference, CERSI/UMD workshop bios, and press coverage — confirming a single stable canonical bio text she (or her employers) reuse. No new identity/account surfaced from this search that wasn't already found via name search. No personal blog or non-professional site turned up.

## Step 4 — Show-notes / speaker-bio bridge (podcast RSS + iTunes API)
- iTunes Search API lookup (`itunes.apple.com/lookup?id=1477483749`) resolved "The Chain: Protein Engineering Podcast" (Cambridge Healthtech Institute), feed URL `rss.buzzsprout.com/468796.rss`. [S11]
- Fetched raw RSS XML directly (not through a summarizer) and grepped the `<itunes:owner>` block: only `<itunes:name>Cambridge Healthtech Institute</itunes:name>` — no owner email tag anywhere in the feed. [S12]
- Located Episode 55 item: title "Episode: 55 - Tala Fakhouri Discusses AI/ML for Biologics Drug Discovery & Development", `pubDate: Tue, 14 Nov 2023`. Named collaborators/interviewers: Richard Bonneau, PhD, and Marcel Hop, PhD, of Genentech. Guest described as "Tala Fakhouri, PhD, of the FDA" — this is a bio-drift anchor (still FDA as of Nov 2023). [S12]
- No personal contact info for the guest anywhere in the feed or episode metadata — this is a genuine null, not a wall (RSS is unauthenticated, fully fetchable, fully read).
- Also surfaced (not deep-dived, redundant with Step 3): AllAmericanSpeakers booking-agency bio page, Sched.com DIA2025 speaker page (handle "talafakhouri" used as her Sched username — consistent with the handle variants tested in Step 2, but Sched is a conference-registration site, not evidence of an independent social account).

## Step 5 — Separate work-only account sweep
- **ORCID**: 0000-0002-0523-3466 — name-only record, no works/affiliations populated in the public API response (surprising for someone with 30+ publications; the record appears to be a claimed-but-unpopulated stub). [S7]
- **ResearchGate**: profile page https://www.researchgate.net/profile/Tala-Fakhouri exists per search snippet (lists her as "Senior Fellow, CDC, Atlanta | DHANES"), but direct fetch returned HTTP 403 (bot wall). Not re-tried against a control account since this is a single incidental data point, not a claimed null — filed as BLOCKED-WALLED, not absence. [S8]
- **Google Scholar**: search snippet surfaced a Scholar page but it resolved to a DIFFERENT Tala Fakhoury (Columbia neuroscience PhD student, `scholar.google.com/citations?user=DK7hkTYAAAAJ`) — see disambiguation below. No confirmed Scholar page for the target was independently verified (would need direct fetch, which I did not do given time-box; flagging as a gap).
- **PubMed**: not directly queried by name in this pass (time-boxed); her FDA/NIH-affiliated publications are referenced secondhand via NEJM AI workshop-report co-authorship (ai.nejm.org/doi/full/10.1056/AIpc2500801 and AIp2500802) — primary journal, two anchors clear (FDA + AI/regulatory topic + her name as listed author). [S9, S10]
- **FDA staff pages / Wayback**: attempted a Wayback CDX API query for fda.gov pages mentioning "fakhouri" in the URL — zero results (she was never the subject of a dedicated fda.gov staff bio page; she only appears as a named contact inside PDF guidance documents, confirmed in Step 1). This is a genuine, tool-verified null (CDX API is unauthenticated, fully queryable, returned a clean empty JSON list, not a wall).
- **CERSI/UMD workshop bio (Feb 2023)** — found and PDF-extracted directly, a primary conference-organizer document: "Tala Fakhouri, B.Sc., Ph.D., M.P.H. — Associate Director for Policy Analysis, OMP | CDER | FDA" — this is an earlier/different title than later bios ("Associate Director for Data Science and Artificial Intelligence"), see Step 6. [S6]

## Step 6 — Bio-drift comparison (dates)
Chronological bio/title sightings, oldest to newest, each independently sourced:
1. **Feb 2023** — CERSI/UMD workshop bio (PDF, primary): "Associate Director for Policy Analysis, OMP | CDER | FDA." States she joined FDA "in October of 2020" from CDC/NHANES. [S6]
2. **Dec 3, 2023** — Eventscribe/ASHP Midyear 2023 presenter page: "Associate Director for Policy Analysis" at FDA/CDER — same title as #1, ~10 months later. [S13]
3. **Nov 14, 2023** — Podcast Episode 55 (The Chain, Buzzsprout RSS pubDate): described simply as "of the FDA," no specific title given. [S12]
4. **2023** (undated within year) — selected to Federal Committee for Statistical Methodology — recurs in all later bios as a fixed credential. [multiple, e.g. S6, S14]
5. **Jul 1, 2025** — Parexel/GlobeNewswire press release (via Manila Times syndication, dated 2025-07-01): "Parexel announces appointments of two FDA luminaries" — Tala Fakhouri, Ph.D., MPH, joins as "Vice President Consulting, AI & Digital Policy, Real-World Research." This is the FDA→Parexel pivot point. Her FDA title is given there as "Associate Director for Data Science and Artificial Intelligence in the Office of Medical Policy" — a title upgrade from the 2023 "Policy Analysis" title, implying an internal FDA promotion/retitling sometime between Dec 2023 and mid-2025 (exact date not found). [S14, S15]
5b. STAT News (Jul 2, 2026) independently corroborates with looser language: "after leaving the FDA last summer" (i.e., summer 2025) — consistent with the Jul 1, 2025 press release. [S16]
6. **May 18, 2026** — Parexel launches "ParexelAI™" product; multiple press outlets (GlobeNewswire, HITConsultant, HealthTechnologyNet) cover it, by which point she is established in the Parexel AI leadership role. [S17, S18, S19]
7. **Jul 2, 2026** — STAT News feature quotes her under the title "chief AI and regulatory strategy officer at Parexel" — a further title change/promotion from the Jul 2025 "VP Consulting" title. [S16]
8. **2026 (current)** — BIO International Convention 2026 speaker page STILL lists her as "Vice President Consulting: AI & Digital Policy, Real-World Research" — i.e., that conference-organizer bio has NOT been updated to reflect the "Chief AI & Regulatory Strategy Officer" title used by STAT News and her own Parexel expert page / LinkedIn. This is a live, current bio-drift discrepancy as of this run (2026-08-27) — two different titles for the same current employer circulating simultaneously in reputable sources. [S20 vs S16/S21]

**Net read: a bio still saying "Associate Director... FDA" or "Associate Director for Policy Analysis" (rather than Parexel) dates that snapshot to on/before ~mid-2025 (the Jul 1, 2025 pivot).**

## Disambiguation guards (name-collision contamination controls)
Distinct OTHER people who surfaced under "Fakhouri" / near-spellings and must NOT be merged with the target:
1. **Tala Fakhoury** (note: -oury, not -ouri) — PhD student, Center for Theoretical Neuroscience, Columbia University; studies reasoning/planning/working memory via Neuropixels electrophysiology. Has her own LinkedIn (linkedin.com/in/talafakhoury22/) and Google Scholar (scholar.google.com/citations?user=DK7hkTYAAAAJ). Zero anchor overlap with target (no Parexel/FDA/Hopkins/Bethesda/AI-regulatory-policy). A BIO International Convention 2026 speaker page existed at the URL slug `/speakers/tala-fakhoury` but returned 404 on fetch — likely never populated or since removed; the correctly-spelled `/speakers/tala-fakhouri` is live and matches the target. [S22, S23]
2. **Tawfiq Fakhouri** — male, Jordanian politician/businessman (Wikipedia). Surname-only collision, no other overlap.
3. **Tamirace Fakhoury** — Lebanese-American political scientist (Wikipedia). Different first name and spelling, surname-only collision.
4. **Nikta Fakhri** — different surname entirely (Fakhri, not Fakhouri); appeared only as search noise.
5. **Bachir Bash Fakhouri, laila.fakhouri, Diala Fakhouri** — unrelated individuals surfaced via generic Instagram/social search; zero anchors, filed as noise.
6. **github.com/fakhouri** (bare surname handle) — never queried by full given-name match; not investigated (out of bounded scope — assignment forbids running the sweep on a bare surname or given name).
7. All 151 Maigret hits (Step 2) are presumptively OTHER people or unrelated squatted accounts, not the target, absent any anchor confirmation.

## Nulls (confirmed absence, with counts/windows)
- FDA Wayback/CDX query for any fda.gov URL containing "fakhouri": 0 results returned by the CDX API (query run 2026-08-27; API responded cleanly, not a wall) — confirmed null: no dedicated FDA staff bio page for her was ever archived.
- Podcast RSS feed (91 episodes total in feed, includes hers): 0 personal contact fields (itunes:email) present anywhere in the feed-level or item-level XML — confirmed null, checked 2026-08-27, full feed fetched and grepped directly (not summarized).
- No personal website/domain in her name found via search (checked via 6 distinct WebSearch queries spanning email, ORCID, Johns Hopkins, Bethesda, Scholar/PubMed/ResearchGate, podcast/speaker-bio terms, run 2026-08-27) — confirmed null within the bound of what general web search surfaces; not an exhaustive domain-registration check.

## Walls (not nulls)
- ResearchGate profile page: HTTP 403 on direct fetch (2026-08-27). Not re-tested against a control account (single incidental hit, not a claimed absence) — filed as BLOCKED-WALLED.
- Parexel newsroom press release page: HTTP 403 on direct curl fetch (2026-08-27) — bot-walled; content instead recovered via search-engine snippet and a syndicated re-publication (Manila Times). Filed as BLOCKED-WALLED for the primary, SEARCH-ONLY for the syndicated copy.
- LinkedIn and X: explicitly out of scope for this lane per assignment — not attempted, owned by browser lane (already VERIFIED-AUTHENTICATED for LinkedIn).

## Named manual gap
Reverse-image search on her profile photo was not performed — I have no image-upload capability. Flagging as an open manual step for a human or an image-capable lane.

## Coverage bounds
- WebSearch: 12 distinct queries run (email, FDA contact, ORCID, podcast/bio, Johns Hopkins, Bethesda, quoted-bio phrases x2, social handles, Google Scholar/PubMed/ResearchGate, BIO convention disambiguation, Parexel press-release date). Standard web-search result caps apply (approx. top 10 results per query) — not an exhaustive crawl of every indexed page mentioning her name.
- Maigret: exactly 5 handle variants (of 6 allowed), ~509 sites each per the `--top-sites 500` bound, `--no-extracting` per required command (so no bio-text confirmation was structurally possible from this tool in this run).
- Direct document fetches: 3 FDA guidance PDFs (fully OCR'd/text-extracted), 1 CERSI/UMD conference-bio PDF (fully extracted), 1 full podcast RSS feed (fully fetched, 91 items), 1 ORCID public-API JSON record (fully fetched).
- Not attempted: PubMed direct name search, Google Scholar direct profile fetch for the target (only found via search snippet, misattributed in one instance to the Columbia namesake), full ResearchGate publication list, LinkedIn, X.
