# Tala Fakhouri — Layer 7 (Block A) + Layer 3a (Block B) Collection
Collection worker run. Accessed 2026-08-27 (all timestamps UTC unless noted). No LinkedIn/X touched (owned by another lane).

## Target identity anchors (confirmed via primary sources)
- Current: Chief AI & Regulatory Strategy Officer, Parexel (also seen as "VP Consulting: AI & Digital Policy, Real-World Research" — likely a title update in progress; both appear across Parexel-linked pages).
- Prior: Associate Director for Data Science and AI / Associate Director for Policy Analysis, Office of Medical Policy, CDER, US FDA, Silver Spring, MD.
- Prior: Senior Health Scientist / Chief Statistician, CDC NHANES.
- Education: MPH, Johns Hopkins Bloomberg School of Public Health; PhD Oncological Sciences, Huntsman Cancer Institute/U. Utah; postdoc Harvard; BSc Jordan University of Science and Technology.
- ORCID: 0000-0002-0523-3466 (verified via works list matching FDA/AI-drug-development topic exactly — S-ORCID-1, S-ORCID-2).

## Disambiguation guards used
1. "Fakhouri"/"Fakhoury" is a common Levantine surname. Every bare-name hit required two of: Parexel, FDA/CDER, Johns Hopkins, Bethesda MD, exact title, or a named collaborator (Richard Bonneau/Genentech, Brandon Rice/Weave, Lola Fashoyin-Aje/Parexel) before being credited to the target.
2. Confirmed distinct other people sharing the name/near-name during this run: "Tala Soubra" (Substack, Lebanese recipes), "Tala Fakhoury" PhD student at Columbia (LinkedIn, not touched), "Maria/Luis/Deena/Ala/Muhamad Fakhouri" (Bluesky), a Falls Church VA Goodreads user with 0 books, a Dubai Goodreads user with 43 books, an Instagram fitness coach @talafakhouri__ (8,320 followers, unrelated bio), a TikTok user @tala.fakhoury (119 followers, no bio) whose spelling and lack of any professional signal argue against a match, and a Facebook profile "tala.fakhoury.1" (spelling variant, unverified).
3. A GitHub account "talafakhouri" surfaced but its only content is a coding-bootcamp student portfolio ("Tala's Portfolio", HTML exercises) with zero bio/location — treated as unrelated/unverifiable, not credited.

---

## BLOCK A — 13 rows

### 1. Bluesky
- Action: `app.bsky.actor.searchActors?q=fakhouri` (platform's own index) + 4 direct handle probes (talafakhouri.bsky.social, tfakhouri.bsky.social, tala-fakhouri.bsky.social, talafakhouri.com as custom-domain handle).
- Result: search returned 6 accounts with "fakhouri" in handle/display name (mariafakhouri, luisfakhouri, deenafakhouri1988, fakhouri, alafakhouri, muhamad-fakhouri.bsky.social) — none is Tala Fakhouri. All 4 direct handle probes returned `{"error":"InvalidRequest","message":"Profile not found"}` (HTTP 400).
- Verdict: **VERIFIED-NOT-FOUND**. Checked 6 name-matching accounts in the platform's own search index + 4 handle guesses on 2026-08-27; none present.
- Source: S1 (curl to public.api.bsky.app, 2026-08-27T11:44Z–11:52Z)

### 2. Instagram
- Action: web search → found `instagram.com/talafakhouri/`; WebFetch of that URL.
- Result: account exists, 1,361 followers / 1,845 following, **private** — bio and posts not visible without login. A lookalike `@talafakhouri__` was also fetched and is confirmed a DIFFERENT person (fitness coach, 8,320 followers, unrelated bio) — ruled out.
- Verdict: **WALLED** (main candidate is private/auth-walled; cannot clear the two-anchor gate without logging in).
- Source: S2 (WebFetch instagram.com/talafakhouri/, 2026-08-27), S3 (WebFetch instagram.com/talafakhouri__/ — ruled out as different person)

### 3. Threads
- Action: curl `threads.net/@talafakhouri` (public og:meta tags render without login).
- Result: page resolves — title "tala fakhouri (@talafakhouri) • Threads, Say more", "35 Followers • 1 Thread". No bio text or post content beyond meta description was retrievable; identical handle to the private Instagram account (Threads identity is tied to Instagram) but no professional anchors visible.
- Verdict: **NOT-DISTINGUISHABLE** (fetched; account exists but zero anchors surfaced — could be the target's dormant/linked Threads or a coincidental same-handle claim).
- Source: S4 (curl threads.net/@talafakhouri, 2026-08-27T~12:05Z)

### 4. TikTok
- Action: curl `tiktok.com/@tala.fakhoury` with browser UA (SSR JSON embedded in page).
- Result: `"desc":"@tala.fakhoury 119 Followers, 186 Following, 119 Likes"`, `"signature":""` (empty bio), `"followerCount":119`.
- Verdict: **NOT-DISTINGUISHABLE** (fetched; different spelling "Fakhoury", zero bio, low follower count with no professional content — likely a different, unrelated person, but cannot fully rule out without more anchors).
- Source: S5 (curl tiktok.com/@tala.fakhoury, 2026-08-27)

### 5. Facebook
- Action: web search for personal profile; curl `mbasic.facebook.com/public/Tala%20Fakhouri` (lightweight search endpoint).
- Result: web search surfaced only (a) Parexel's own FB page hosting a video ABOUT her ("Patients First Friday"), (b) Financial Times Live's FB page hosting a video of her conference remarks, (c) a spelling-variant profile "tala.fakhoury.1" (unverified, likely unrelated). mbasic search returned an "Error" page (HTTP 200 but Facebook error/block page, 3.7KB) — Facebook's search blocks unauthenticated/bot requests.
- Verdict: **WALLED** (Facebook's own search is bot-blocked; no personal profile confirmed via any accessible route).
- Source: S6 (curl mbasic.facebook.com, 2026-08-27), S7 (WebSearch results)

### 6. Substack
- Action: WebSearch `"Tala Fakhouri" Substack` and `site:substack.com "Tala Fakhouri"`.
- Result: only unrelated hits — "Tala's Newsletter" (talasoubra.substack.com, by "Tala Soubra," Lebanese recipes), "self-portrait | tala", "Taabeer Tala", "Tala Talks NICU", "Tala Samman" — none is the target.
- Verdict: **VERIFIED-NOT-FOUND**. Checked Substack's own indexed content via 2 targeted searches on 2026-08-27; none present.
- Source: S8, S9 (WebSearch, 2026-08-27)

### 7. Medium
- Action: WebSearch `"Tala Fakhouri" Medium.com`; curl `medium.com/search/users?q=Tala Fakhouri`.
- Result: WebSearch returned no Medium content. Direct API call blocked — Cloudflare "Attention Required" interstitial, HTTP 403.
- Verdict: **WALLED** (Medium's own search/API is bot-blocked; cannot confirm a real null against the platform's own index).
- Source: S10 (curl medium.com/search/users, 2026-08-27, HTTP 403)

### 8. GitHub
- Action: `api.github.com/users/talafakhouri`, `/tfakhouri`, `/TalaFakhouri`, `/tala-fakhouri`; `api.github.com/search/users?q=fakhouri` (platform's own index, 60 total results).
- Result: `talafakhouri` (id 90216458, created 2021) and `tfakhouri` (id 9449758, created 2014) both exist but have **no bio, no name, no location, no company** set. `talafakhouri`'s 6 repos are a coding-bootcamp student portfolio ("final-website-project — Tala's Portfolio", "image-excercise", "talas-site-exercise1", etc.) — content inconsistent with a PhD regulatory scientist. `tala-fakhouri` returns 404.
- Verdict: **NOT-DISTINGUISHABLE** (fetched; two name-matching accounts exist but zero anchors clear, and repo content suggests a different, likely much younger, person).
- Source: S11–S14 (curl api.github.com/users/*, 2026-08-27)

### 9. Personal site
- Action: curl `https://talafakhouri.com` and `https://www.talafakhouri.com`; cross-checked all fetched bio pages (Parexel, ISPE, ADAPT, BIO Convention, DIA, Weave Bio) for any personal-site link.
- Result: both domain probes returned `HTTP:000` (no DNS/connection — domain does not resolve or host is down). No official bio page links to a personal site.
- Verdict: **VERIFIED-NOT-FOUND**. Checked the 2 obvious domain guesses (both fail to resolve) plus 6 official bio pages for a linked personal site on 2026-08-27; none present.
- Source: S15, S16 (curl, 2026-08-27); S17–S22 (bio pages, see Block A #12 sources)

### 10. Podcasts
- Action: WebSearch + WebFetch of `healthtech.com/the-chain/tala-fakhouri-discusses-ai-ml-for-biologics-drug-discovery-development` and `buzzsprout.com/468796/episodes/13947341-...`.
- Result: **FOUND** — "The Chain: Protein Engineering Podcast" (Genentech), Episode 55, "Tala Fakhouri Discusses AI/ML for Biologics Drug Discovery & Development." Guest bio: Associate Director for Policy Analysis, FDA CDER; prior CDC NHANES Chief Statistician; PhD Utah, MPH Johns Hopkins, Harvard postdoc. Hosts named: Richard Bonneau (Genentech) and Marcel Hop (Genentech).
- Anchors cleared: (1) FDA CDER title, (2) CDC NHANES Chief Statistician + Johns Hopkins MPH bio detail — both distinctive and matching the target's known profile.
- Source: S23 (healthtech.com), S24 (buzzsprout.com), 2026-08-27

### 11. YouTube
- Action: WebSearch for video titles; cross-verified against the FDA-hosted PDF of the same talk (see #12).
- Result: **FOUND** — "Tala Fakhouri - Responsive Regulation of AI in Drug Development" (youtube.com/watch?v=Jc9axucreyc, published ~Nov 25, 2024) and "REdI 2024 | D1S06 - Responsive Regulation of Artificial Intelligence in Drug Development" (youtube.com/watch?v=kueGYjRCn8c). Title and topic match exactly the FDA's own title-slide PDF (fda.gov/media/184256/download): "Tala H Fakhouri, Associate Director for Policy Analysis, Office of Medical Policy, CDER | US FDA, REdI – May 29th, 2024." A separate, differently-spelled "Tala Fakhoury" YouTube channel (UCeaWDyVew2Fpn6oogJ1YMsQ) also surfaced and is unrelated (ruled out — no topical match).
- Anchors cleared: (1) FDA/CDER affiliation, (2) exact talk title + event name (SBIA REdI Conference 2024) matching the primary FDA PDF verbatim.
- Note: WebFetch could not render full YouTube page content (JS-heavy); verdict rests on WebSearch title/date match plus the independently-fetched primary FDA PDF, not on directly viewing the YouTube page body.
- Source: S25 (WebSearch), S26 (fda.gov/media/184256/download, fetched directly via curl, confirmed PDF metadata below)

### 12. Conference and webinar archives
- Action: Direct WebFetch of primary event/org pages; direct curl+pdftotext of an FDA-hosted PDF.
- **FOUND**, verified against primary pages:
  - **FDA SBIA REdI Conference 2024** (primary, fda.gov/media/184256/download — fetched and text-extracted directly): title slide reads "Responsive Regulation of Artificial Intelligence in Drug Development / Tala H Fakhouri / Associate Director for Policy Analysis / Office of Medical Policy / CDER | US FDA / REdI – May 29th, 2024." This is the single strongest anchor in the whole run (hosted directly on fda.gov, names her by full title).
  - **DIA 2025 Global Annual Meeting** (primary, dia2025globalannualmeeting.sched.com/speaker/talafakhouri): title "Associate Director for Data Science and Artificial Intelligence, CDER," FDA. Five named sessions June 17–19, 2025 (#203, #225, #328, #405 EMA-FDA Question Time, #408 FDA Town Hall).
  - **BIO International Convention 2026** (primary, convention.bio.org/speakers/tala-fakhouri): "VP Consulting, AI & Digital Policy, Real-World Research," Parexel + FDA bio. Two named sessions June 23–24, 2026.
  - **ADAPT conference** (primary, adapt-conference.com/speaker/tala-h-fakhouri-phd-mph/): Parexel + FDA + full education detail (Johns Hopkins MPH, Utah PhD, Harvard postdoc).
  - **ISPE** (primary, ispe.org/people/tala-fakhouri-phd-mph): Parexel + FDA + CDC + Johns Hopkins.
  - **Weave Bio webinar host page** (primary, weave.bio/webinar-host/tala-fakhouri-parexel/): co-presenter with Brandon Rice (Weave CEO), "Beyond Submission Assembly" webinar, Parexel + "former FDA AI policy lead."
  - **Kisaco Research** speaker page: thin (FDA title only, no second anchor) — filed as supporting context, not a standalone two-anchor FOUND.
- **UNVERIFIED / flagged per task instruction**: an AI search-summary claimed a "Bio-IT World Conference & Expo (April 2025) keynote." I could not find this on any Bio-IT World primary page (conference site, agenda archive) — a follow-up targeted search returned no corroborating primary source. Per the task's warning that AI summaries invent conference appearances, **this claim is NOT verified and should not be relied on** until a primary Bio-IT World agenda page is found.
- Anchors cleared (per FOUND item): FDA/CDER affiliation + exact title/session names, all on the organizations' own domains.
- Source: S26 (fda.gov PDF), S27 (DIA sched.org), S28 (BIO convention.bio.org), S29 (adapt-conference.com), S30 (ispe.org), S31 (weave.bio), S32 (kisacoresearch.com — thin), S33 (WebSearch — Bio-IT World claim, unverified)

### 13. Trade-press bylines
- Action: ORCID public API (works list) + WebSearch/WebFetch of individual journal/trade pages.
- **FOUND** (peer-reviewed academic bylines, which the task explicitly directs to check): via ORCID 0000-0002-0523-3466 works list (3 groups):
  1. "Leveraging Artificial Intelligence in Drug and Biological Product Development: An FDA and Clinical Trial Transformation Initiative Workshop Report," NEJM AI, Nov 26 2025.
  2. "Mitigating Limited Data Challenges to Improve Artificial Intelligence Integration in Rare Disease Drug Development," NEJM AI, Nov 26 2025.
  3. "Landscape Analysis of the Application of Artificial Intelligence and Machine Learning in Regulatory Submissions for Drug Development From 2016 to 2021," Clinical Pharmacology & Therapeutics, April 2023.
  Search-returned author metadata confirms affiliation "Office of Medical Policy, Center for Drug Evaluation and Research, Food and Drug Administration, Silver Spring, MD" on the NEJM AI byline — matches target exactly.
- **Distinguished from bylines** (these are trade press covering/quoting her, NOT authored by her): STAT News Q&A "How the FDA is approaching AI in clinical trials" (Oct 9, 2024, byline not hers) and STAT explainer "A former AI regulator... says biopharma is reading FDA's guidance wrong" (July 2, 2026, byline: Brittany Trang); multiple RAPS Regulatory Focus news articles about FDA AI policy that quote/reference her (not her own byline).
- No confirmed op-ed/bylined piece found under her name in Endpoints, Pink Sheet, or Fierce Biotech/Pharma.
- Direct fetch of ai.nejm.org and ascpt.onlinelibrary.wiley.com (Wiley) both returned HTTP 403 (paywall) — authorship confirmed via ORCID (her own record, self-asserted/Crossref-linked) and WebSearch snippet metadata instead of the publisher page itself.
- Anchors cleared: (1) FDA/CDER Office of Medical Policy affiliation on the NEJM AI byline, (2) topical match (AI/ML in drug regulation, her named specialty) across all 3 works — both distinctive.
- Source: S34, S35 (pub.orcid.org/v3.0/.../works, .../person — curl, 2026-08-27), S36 (WebSearch NEJM AI author confirmation), S37 (statnews.com Oct 2024 — WebSearch), S38 (statnews.com Jul 2026 — WebFetch)

---

## BLOCK B — 4 rows

### Sub-step 1: Substack subscriptions (what she reads)
- Requirement: identifier must come from her own bio link, a Substack byline handle, or handle reuse — never a bare-name guess.
- Action: exhausted all authorized-source routes first — checked her Parexel bio, ISPE, ADAPT, BIO Convention, DIA, Weave Bio pages (Block A #12) for any Substack link; none found. Checked whether she has ever appeared as a `publishedBylines[0].handle` on any Substack post (Block A #6 — no Substack presence at all under her name). No authorized candidate slug surfaced.
- One unauthorized guess was tried for completeness only (NOT counted as the verification method): `talafakhouri.substack.com/api/v1/user/talafakhouri/public_profile` → HTTP 404 (45 bytes) — but per the task's rule this doesn't count as a confirmed null since it wasn't sourced from an authorized reference.
- Verdict: **NOT-APPLICABLE** — no authorized slug ever surfaced.
- Source: S39 (curl, unauthorized guess, logged for completeness only)

### Sub-step 4: Bluesky follows
- Requirement: apply two-anchor gate to her own account first, then read follows.
- Action: see Block A #1 — `app.bsky.actor.searchActors?q=fakhouri` (platform's own index, 6 results) plus 4 direct handle probes. No account attributable to the target exists.
- Verdict: **RAN-NULL** at the account-existence gate — cannot proceed to `getFollows` because no verified account exists to query.
- Checked: 6 name-matching accounts (platform index) + 4 handle guesses, 2026-08-27; none present.
- Source: S1 (same as Block A #1)

### Sub-step 5: GitHub stars and following
- Action: for both name-matching candidates from Block A #8 (`talafakhouri`, `tfakhouri`), ran `/starred?per_page=100` and `/following?per_page=100`.
- Result: **both empty** — `talafakhouri`: starred=[] (0), following=[] (0). `tfakhouri`: starred=[] (0), following=[] (0).
- ⚠️ Per the task's explicit warning, neither account clears the two-anchor gate (see Block A #8 — no bio/name/location, and `talafakhouri`'s repos indicate a coding-bootcamp student, likely a different, unrelated person). The null counts (0 starred, 0 following) are reported below but are **NOT attributable to the target** — they describe two unconfirmed same-name accounts only.
- Verdict: **RAN-NULL** (on unconfirmed accounts only; not credited to target).
- Checked: 2 candidate accounts, 0 starred / 0 following each, 2026-08-27.
- Source: S12, S13, plus S40/S41 (curl .../starred, .../following for both logins)

### Sub-step 6: Fast checks (Goodreads / Reddit / Letterboxd / Spotify)
- **Goodreads**: `goodreads.com/search?q=Tala+Fakhouri&search_type=people` → HTTP 200, "showing 1-2 of 2 people." Result 1: user 62298377, "Falls Church, VA," 0 books, 74 friends. Result 2: user 186642770, "Dubai, UAE," 43 books, 2 friends. Neither profile mentions Parexel/FDA/Johns Hopkins/Bethesda or any professional anchor — Falls Church VA is DC-adjacent but not Bethesda and carries no second anchor.
  - Verdict: **NOT-DISTINGUISHABLE** (fetched; 2 name-matching accounts, zero anchors clear on either).
- **Reddit**: control check first per task rule — `reddit.com/user/spez/about.json` → HTTP 403 (Blocked page, 1,522 bytes). Control failed, confirming Reddit is bot-walled to plain fetchers.
  - Verdict: **BLOCKED-WALLED** (never attempted against her name, per rule — control failure is sufficient).
- **Letterboxd**: control check — `letterboxd.com/dave/` → HTTP 403 (5,420 bytes). Control failed.
  - Verdict: **BLOCKED-WALLED** (never attempted against her name, per rule).
- **Spotify**: no identifier ever surfaced (no bio link, no handle reuse) — per task instruction, this category is skipped entirely when no identifier surfaces.
  - Verdict: **NOT-APPLICABLE**.
- Source: S42 (goodreads.com/search, 2026-08-27), S43 (reddit.com control, 2026-08-27, HTTP 403), S44 (letterboxd.com control, 2026-08-27, HTTP 403)

---

## Source registry (full URLs)

| ID | URL / call | Type | Accessed |
|----|------------|------|----------|
| S1 | https://public.api.bsky.app/xrpc/app.bsky.actor.searchActors?q=fakhouri (+4 getProfile probes) | API, unauthenticated | 2026-08-27 |
| S2 | https://www.instagram.com/talafakhouri/ | WebFetch | 2026-08-27 |
| S3 | https://www.instagram.com/talafakhouri__/ | WebFetch | 2026-08-27 |
| S4 | https://www.threads.net/@talafakhouri (curl) | curl | 2026-08-27 |
| S5 | https://www.tiktok.com/@tala.fakhoury (curl) | curl | 2026-08-27 |
| S6 | https://mbasic.facebook.com/public/Tala%20Fakhouri | curl | 2026-08-27 |
| S7 | WebSearch: "Tala Fakhouri" Facebook profile | search | 2026-08-27 |
| S8 | WebSearch: "Tala Fakhouri" Substack | search | 2026-08-27 |
| S9 | WebSearch: "Tala Fakhouri" site:substack.com | search | 2026-08-27 |
| S10 | https://medium.com/search/users?q=Tala Fakhouri | curl | 2026-08-27 |
| S11 | https://api.github.com/users/talafakhouri | API | 2026-08-27 |
| S12 | https://api.github.com/users/tfakhouri | API | 2026-08-27 |
| S13 | https://api.github.com/users/talafakhouri/repos | API | 2026-08-27 |
| S14 | https://api.github.com/search/users?q=fakhouri | API | 2026-08-27 |
| S15 | https://talafakhouri.com | curl | 2026-08-27 |
| S16 | https://www.talafakhouri.com | curl | 2026-08-27 |
| S17 | https://www.parexel.com/about-us/experts/tala-h-fakhouri-phd-mph | WebFetch | 2026-08-27 |
| S23 | https://www.healthtech.com/the-chain/tala-fakhouri-discusses-ai-ml-for-biologics-drug-discovery-development | WebFetch | 2026-08-27 |
| S24 | https://www.buzzsprout.com/468796/episodes/13947341-episode-55-tala-fakhouri-discusses-ai-ml-for-biologics-drug-discovery-development | search | 2026-08-27 |
| S25 | WebSearch: "Responsive Regulation of AI in Drug Development" Fakhouri youtube channel | search | 2026-08-27 |
| S26 | https://www.fda.gov/media/184256/download (PDF, pdftotext-extracted) | curl+pdftotext, primary FDA source | 2026-08-27 |
| S27 | https://dia2025globalannualmeeting.sched.com/speaker/talafakhouri | WebFetch | 2026-08-27 |
| S28 | https://convention.bio.org/speakers/tala-fakhouri | WebFetch | 2026-08-27 |
| S29 | https://adapt-conference.com/speaker/tala-h-fakhouri-phd-mph/ | WebFetch | 2026-08-27 |
| S30 | https://ispe.org/people/tala-fakhouri-phd-mph | WebFetch | 2026-08-27 |
| S31 | https://www.weave.bio/webinar-host/tala-fakhouri-parexel/ | WebFetch | 2026-08-27 |
| S32 | https://www.kisacoresearch.com/content/tala-fakhouri | WebFetch | 2026-08-27 |
| S33 | WebSearch: "Tala Fakhouri" "Bio-IT World" 2025 keynote (unverified claim) | search | 2026-08-27 |
| S34 | https://pub.orcid.org/v3.0/0000-0002-0523-3466/works | API | 2026-08-27 |
| S35 | https://pub.orcid.org/v3.0/0000-0002-0523-3466/person, /employments | API | 2026-08-27 |
| S36 | WebSearch: "Tala H. Fakhouri" author NEJM AI Clinical Pharmacology Therapeutics | search | 2026-08-27 |
| S37 | https://www.statnews.com/2024/10/09/fda-regulation-ai-clinical-trials-drug-discovery-tala-fakhouri/ | search snippet | 2026-08-27 |
| S38 | https://www.statnews.com/2026/07/02/fda-ai-guidance-pharma-industry-caution-tala-fakhouri-explains/ | WebFetch | 2026-08-27 |
| S39 | https://substack.com/api/v1/user/talafakhouri/public_profile (unauthorized guess, not credited) | curl | 2026-08-27 |
| S40 | https://api.github.com/users/talafakhouri/starred, /following | API | 2026-08-27 |
| S41 | https://api.github.com/users/tfakhouri/starred, /following | API | 2026-08-27 |
| S42 | https://www.goodreads.com/search?q=Tala+Fakhouri&search_type=people | curl | 2026-08-27 |
| S43 | https://www.reddit.com/user/spez/about.json (control) | curl | 2026-08-27 |
| S44 | https://letterboxd.com/dave/ (control) | curl | 2026-08-27 |

## Coverage bounds
- Web search results are capped by the search tool's ranking; deeper pages of results were not paged through for any query.
- YouTube, Instagram, TikTok, Threads, Facebook pages are JS-rendered SPAs — WebFetch/curl retrieved only server-rendered meta tags and embedded JSON, not full authenticated views (post grids, comments, follower lists beyond profile-header counts).
- No Google Scholar, Federal Register, or FDA advisory-committee-roster direct queries were run (time-boxed); ORCID + NEJM AI + CPT + FDA PDF were treated as sufficient primary confirmation for rows 12–13. This is a gap if a fuller academic/regulatory-docket sweep is wanted later.
- Duke-Margolis, NASEM: only one generic WebSearch run; no hits, but this is NOT a verified null (their own event archives were not directly queried) — treat as uncovered, not confirmed-absent.
- GitHub API calls were unauthenticated (rate limit ~10/min for search, 60/hr for REST) — no rate-limit errors were hit during this run, but a broader sweep (e.g., checking `talafakhouri`'s starred repos' topics) was not exhaustive.
