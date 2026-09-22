# Worker B — Layer 2.7 (org channels), Layer 3b (corpus mining), Layer 3c.1–3c.2 (communities)

Run: 2026-09-21-ravi-lal · Target: Ravi Lal (Ravinder Singh Lal) / Voxly Digital, London
Worker role: COLLECTION only — no strategic claims. All output below is evidence + raw counts; interpretation belongs to the orchestrator.
Accessed_at for all sources below: 2026-09-21, ~12:55–13:20 UTC unless noted.

---

## Cross-cutting note for the orchestrator / Layer 1 worker (not my row — flagging only)

While extracting outbound links from Voxly's own blog (Layer 3b), two of Ravi Lal's own bylined posts contain **self-citing links to `linkedin.com/posts/lalravi_...`** (in `acamar-films-...-bingtime` and `scaling-the-human-touch-...-royal-navy`). This is VERIFIED-PRIMARY that the LinkedIn handle **`lalravi`** is Ravi Lal's own account (Voxly's own site, under his own schema.org byline, links to it as his). Two-anchor gate: (1) org = Voxly Digital, matches Layer 0 target org; (2) first-person self-link on his own bylined company content. Useful for Layer 1/Layer 7 if not already resolved. Source: B20 (raw HTML), specifically `corpus/raw/acamar-films-voxly-digital-grow-reach-of-preschool-hit-with-2022-webby-award-honoree-bingtime-skil.html` and `corpus/raw/scaling-the-human-touch-a-new-era-of-royal-navy-recruitment-via-conversationalai-and-digital-avatars.html`.

---

## Ledger rows

```yaml
- step: "2.7 organization channels (open web)"
  status: RAN-FOUND
  checked_count: 25
  checked_unit: pages/records
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18]
  note: >
    Website (8 pages incl. RSS), Companies House (9 records incl. 2 filed accounts),
    Wayback CDX (315-URL index + 1 snapshot fetch), Amazon Alexa partner directory
    (found), Google Assistant partner directory (checked, NOT found — contradicts a
    secondary-source claim). Full findings below.

- step: "3b.1 corpus fetch — size, window, walls"
  status: RAN-FOUND
  checked_count: 30
  checked_unit: documents
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [B19,B20]
  note: >
    Only 5 documents fall inside 2025-09-21→2026-09-21; extended to all-time per
    the thin-window rule. 30 most-recent fetched (RSS gave 20; +10 older pulled
    from the Wayback URL inventory to reach the 30 cap). No walls — Wix blog is
    fully fetchable, no auth/paywall. One fetch (a-year-of-voice-2021) returned
    0 bytes on retry-worthy transient failure; not re-fetched, immaterial to the
    ratio conclusion below.

- step: "3b.2 extract and classify outbound links"
  status: RAN-FOUND
  checked_count: 30
  checked_unit: documents
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [B20]
  note: >
    14 classified links total (12 source, 2 vendor/tool) across 5 of 30 documents;
    25 of 30 documents contain zero classified links. Raw breakdown below.

- step: "3b.3 named people, works cited, tools"
  status: RAN-FOUND
  checked_count: 30
  checked_unit: documents
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [B20,B21]
  note: >
    One named colleague (Rozzi Meredith), one named external community/podcast
    with two named hosts (VUX World — Kane Simms, Dustin Coates), zero named
    individual authorities cited as evidence-sources anywhere in 30 documents.
    Works/tools list below.

- step: "3b.4 diagnostic ratios"
  status: RAN-NULL
  checked_count: 14
  checked_unit: links
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [B20]
  note: "insufficient sample — 14 classified links across 5 documents; minimum is 50 links across ≥5 documents"

- step: "3c.1 communities named in corpus / org channels"
  status: RAN-FOUND
  checked_count: 30
  checked_unit: documents (corpus) + 8 (org channel pages)
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [B20,B25,B17]
  note: >
    One genuine community found: VUX World (voice-UX industry podcast). One
    professional directory found: Amazon Alexa "agencies and tools" partner
    listing. Two certification schemes (ISO 27001, Cyber Essentials) noted but
    NOT counted as communities (no participatory/forum element evidenced).

- step: "3c.2 consumer surfaces, checked explicitly"
  status: RAN-NULL
  checked_count: 3
  checked_unit: platforms (Reddit, general forum/Discord search, Facebook groups)
  evidence_quality: SEARCH-ONLY
  source_ids: [B22,B23]
  note: "Checked 3 consumer-surface categories via search; none present. Direct Reddit fetch BLOCKED-WALLED (403 on target query AND on a known-good control account — platform-wide wall, not evidence of absence)."
```

---

## Findings — Layer 2.7: Organization channels (open web)

### What Voxly Digital is today (current site, 2026-09-21)
Tagline: *"Digital Transformation for Advertising, Commerce, and Customer Support for large multi-national brands."* Current product line is **Compliance AI** — "Voxly Vision," an AI co-pilot that scans ad creative against ASA/CAP Code, Portman Group (alcohol), FCA (financial promotions), TTB/DISCUS/BGC (US/gambling) rules — plus conversational-AI products for customer self-service, call centers, conversational marketing, and airports. Positioning line from the about-us page: *"advertising compliance has been the one part of marketing that generative AI hasn't touched."* Integrations: web, Slack, Microsoft Teams, API, **MCP** (Model Context Protocol — notable, an agency this size is already shipping MCP support), Chrome extension, DAM integration. Certifications claimed: ISO 27001, Cyber Essentials. Office: 8 Hermitage St, London W2 1BE (Paddington). Contact: freshthinking@voxlydigital.com. [Source: B1, B3]

**No mention anywhere on the current site of Amazon Alexa or Google Assistant** — the voice-agency identity has been fully retired from current marketing, even though it's the company's origin (see pivot timeline below). [B1]

### Company legal identity — the single most load-bearing finding in this layer
**"Voxly Digital" and "Voxly Vision" are trading names, not registered companies.** Companies House has no company named "Voxly Digital" or close variant. A search on "Voxly" returns only unrelated entities (VOXLY LTD 12027947 — a childcare/tuition company in Streatham, officers named Naveed, incorporated 2019, SIC codes for retail books / primary education / childcare — **confirmed false positive, not the target**; VOXLY CHILDCARE SERVICES LTD; VOXLY MARKETING SERVICES LTD; VOXLYN LTD; etc. — none connect to Ravi Lal or a digital/AI agency). [B7]

The actual registered vehicle is named on Voxly's own about-us page: *"Voxly is led by Ravi Lal and Elliot Brock... The company operates as a trading name of Dolphin Haley LTD."* [B3] That single sentence is what makes the rest of this section possible — Companies House has no "Voxly," but it has a very clean record for Dolphin Haley Limited.

### Companies House — Dolphin Haley Limited (company no. 08396885)

| Field | Value | Source |
|---|---|---|
| Registered name | DOLPHIN HALEY LIMITED | B8 |
| Company number | 08396885 | B8 |
| Incorporated | 11 February 2013 | B8 |
| Company status | Active | B8 |
| Company type | Private limited company | B8 |
| Registered office | Boundary House, Cricket Field Road, Uxbridge, Greater London, UB8 1QG (moved here 20 Mar 2026; previously Bentinck House, Bentinck Road, West Drayton, Middlesex UB7 7RQ) | B11 |
| SIC code on file | 47910 — Retail sale via mail order houses or via internet | B8 |
| Director | LAL, Ravinder Singh — appointed 11 Feb 2013 (sole active officer since incorporation), DOB Feb 1969, nationality **American**, residence England, identity-verification complete | B9 |
| PSC | Mr Ravinder Singh Lal, notified 11 Feb 2017, nature of control: "Has significant influence or control" (not an ownership-% band) | B10 |
| Confirmation statement | Last dated 11 Feb 2026 | B8 |
| Accounts basis | "Total exemption full accounts" (small-company exemption; no P&L disclosed, balance sheet only) | B12, B13 |

**Two-anchor identity confirmation:** (1) trading-name statement on voxlydigital.com/about-us naming Dolphin Haley Ltd as the operating entity for "Voxly," led by Ravi Lal; (2) director's stated nationality (American) and profile independently match Ravi's own AI Jam claim of being from Dallas, TX. Both anchors are distinctive and independent. CLEARED.

**SIC-code mismatch, worth flagging plainly:** the company's registered business classification is "retail sale via mail order or internet," not any advertising/software/AI code. Small UK companies frequently leave stale SIC codes from an earlier incorporation purpose and never update them — this alone is not a red flag on its own, but it means Companies House's own categorization of this business is administratively stale, which the actioning map should not lean on for classification.

### Financial headline figures — last three filed year-ends (from the iXBRL of the two most recent AA filings, which carry the prior year as a comparative column)

| | FYE 31 Mar 2024 | FYE 31 Mar 2025 | FYE 31 Mar 2026 |
|---|---|---|---|
| Filed | (comparative in B13) | 3 Jul 2025 (B13) | 19 Jun 2026 (B12) |
| Shareholders' funds / Net assets | £632,280 | £848,101 | £859,648 |
| Cash at bank and in hand | £524,881 | £1,011,643 | £784,576 |
| Debtors | £320,480 | £9,252 | £141,343 |
| Creditors due within 1 year | £(213,081) | £(172,794) | £(66,271) |
| Average employees (incl. directors) | 5 | 5 | 5 |
| Called-up share capital | £1 | £1 | £1 |

Evidence quality: **VERIFIED-PRIMARY** (filed statutory accounts, iXBRL, B12/B13). No fixed-assets line appears in either filing — this is a balance sheet with no owned property/equipment, consistent with a small services agency renting office space (hot desks, per Ravi's own AI Jam account) rather than owning infrastructure.

**Read (raw, not spun):** net assets grew every year (£632K → £848K → £860K) and the company has been solvent and self-funded (no share capital beyond £1 nominal, no loan notes visible) across all three years on file. Cash dipped from £1.01M to £785K over the FYE-March-2026 year — but that year-end (31 Mar 2026) predates the Diageo revenue loss Ravi described in the AI Jam transcript (~3 months before 2026-09-18, i.e., roughly June 2026), so this filed balance sheet does **not yet reflect** whatever the Diageo loss did to cash; the next filing (due ~Dec 2027 for FYE Mar 2027) will be the one that shows it. Headcount held flat at 5 (including directors) across all three years, consistent with Ravi's own "him + 3 coders" framing from the AI Jam call.

### Wayback Machine — dating the pivots (315-URL CDX index, 2018-08-09 → 2026-05-20; a handful of representative snapshots fetched)

| Era | Evidence |
|---|---|
| **2018–2021: Voice agency (Alexa/Google Assistant)** | Site live from at least 2018-08-09. July 2019 snapshot has dedicated sector pages: `/automotive`, `/beauty-fashion`, `/health-fitness-wellbeing`, `/smart-home`, `/enterprise`, `/financial-services`, `/content-publishing-digital`, `/voicecommerce`. 2020 has COVID-era Alexa content (`/alexa-covid-19-infographics`, `/alexa-family-usage-infographics`) and case studies for BBC Match of the Day, Joe Wicks, RSPCA, Public Health England ("Breast-Feeding Friend"), Aquafresh. Team page (2019, live-site current version) lists Ravi Lal (Founder) + Elliot Brock (Head of Tech) + 2 engineers — a 4-person shop even then. |
| **2021–2022: Peak Alexa/Google Assistant client work** | Cadbury Hide & Find (2021–22), Diageo "The Bar" Alexa skill (Webby Award 2019), Unilever All Things Hair chatbot/voice strategy (2023 write-ups of earlier work), Solace Women's Aid webchat, Rogers/NHL voice quiz. |
| **2022–2024: Pivot to conversational AI / LLM chatbots** | Diageo "conversational AI strategy" (2022–23), Diageo Seedlip generative-AI concierge "Elli" (launched Nov 2023, quote from Miguel Orlarte, Diageo Breakthrough Innovation — B6), Bristol Airport generative-AI chatbot (2024, "first major UK airport to launch AI chatbot for customer services"), UK Royal Navy generative-AI recruitment chatbot ("70% reduction in live chat support," 2024). |
| **2024–2026: Full pivot to "Compliance AI" / Voxly Vision** | Product pages for `/vxd-products/ai-for-compliance-media`, `/vxd-products/ai-for-call-centers`, `/vxd-products/ai-for-conversational-marketing`, `/vxd-products/ai-for-customer-self-service`; blog posts in 2026 are compliance-AI market-education pieces (see corpus below), not case studies. Royal Navy "digital avatar" work continued into 2026 (Feb 2026 post). |

Source: B15 (CDX index), B16 (2019 snapshot fetch test — confirms the era is fetchable), B1/B3/B5/B19/B20 (current site + blog corpus for the later eras).

### Client / case-study roster (source-cited)

| Client | What was built | Source |
|---|---|---|
| Diageo (Seedlip, Baileys, Don Julio, "The Bar") | Alexa skill (2019 Webby winner); conversational-AI strategy (2022–23); generative-AI concierge "Elli" (Nov 2023); "first Diageo Marketing AI Agent" (compliance, 2026) | B5, B6, B19 |
| UK Royal Navy | Generative-AI recruitment chatbot ("70% reduction in live chat support," 2024); digital-avatar recruitment tool (2026) | B5, B19 |
| Bristol Airport | Generative-AI customer-service chatbot (2024) — "first major UK airport" claim | B5, B19 |
| Unilever (All Things Hair) | Haircare chatbot + voice strategy (2023 write-ups) | B19 |
| Cadbury | "Hide & Find" Alexa/Google Assistant game (2021–22) | B19 |
| Acamar Films (Bing / BingTime) | Alexa skill, 2022 Webby Award Honoree | B19 |
| Solace Women's Aid (UK domestic-abuse charity) | Webchat (2023) | B19 |
| Joe Wicks (The Body Coach), BBC Match of the Day Magazine, RSPCA, Public Health England (Start4Life), Rogers Communications/NHL, Aquafresh | Alexa/Google Assistant skills, 2019–2021 era | B15 (Wayback inventory) |
| Eagle Eye | Named technology **partnership** (not a client case study) — "Eagle Eye and Voxly Digital Partner to Drive Customer Engagement" | B25 (secondary source, not independently fetched — UNVERIFIED, listed for completeness) |

Named client-side quote found (org channel, live case-studies page, NOT part of the blog corpus counted under 3b): *"Working with Voxly has been a game-changer for Diageo... The speed at which they delivered a sophisticated, market-ready AI concierge like Elli was truly impressive."* — **Miguel Orlarte, Breakthrough Innovation, Diageo**. [B6]

### Directories / trade press

- **Amazon Alexa "agencies and tools" partner directory** (developer.amazon.com/en-GB/alexa/agencies-and-tools): **CONFIRMED PRESENT** — Voxly's own logo and a live link to voxlydigital.com appear in the page's HTML. VERIFIED-PRIMARY. [B17]
- **Google Assistant "agencies" partner directory** (developers.google.com/assistant/agencies): **CHECKED, NOT FOUND.** Voxly does not appear anywhere in this page's current HTML. This directly contradicts a secondary AI-search-summary claim that Voxly is "Amazon & Google Recommended" — per the evidence rules, that claim is flagged **UNVERIFIED / CONTRADICTED-BY-PRIMARY-SOURCE**, not reported as fact. [B18]
- Clutch, The Drum, Campaign: **searched, no listing found.** "Nobody publishes there" is the honest finding — where Voxly's public conversation actually happens is (a) its own blog under Ravi's byline, and (b) the Amazon partner directory above, not agency-review sites.
- EU-Startups directory, Crunchbase, Tracxn, ZoomInfo, ContactOut, Facebook page, LinkedIn company page: **exist** per search snippets but are aggregators/social platforms outside my remit (aggregators are non-primary per the process's own dead-ends list; LinkedIn is SEARCH-ONLY for me) — listed as leads only, **UNVERIFIED**, not fetched or relied on for any claim above. [B25]

---

## Findings — Layer 3b: Corpus mining

### 3b.1 — Size, window, walls
Fetchable first-party corpus = Voxly's own blog at voxlydigital.com/blog, **entirely bylined to "Ravi Lal"** (confirmed via schema.org JSON-LD `"author":{"@type":"Person","name":"Ravi Lal"}` on every one of the 30 posts fetched, plus matching Open Graph `article:author` meta tag) [B20]. No Medium, Substack (checked — no personal or publication slug surfaced from any authorized source; NOT-APPLICABLE per the process's own rule, not a null), or podcast-transcript corpus found for him personally.

- **In-window (2025-09-21 → 2026-09-21): only 5 documents** — thin, well under any usable sample.
- **Extended to all-time** per the thin-window rule: fetched the 30 most recent posts via the blog's own RSS feed (`/blog-feed.xml`, returned 20 items) plus 10 older posts pulled from the Wayback URL inventory to reach the 30-item cap. Actual corpus spans 2021-09-25 → 2026-07-13.
- **Walls: none.** Wix blog pages are fully fetchable by plain curl, no auth/paywall/captcha. One of the 30 fetches (`a-year-of-voice-2021`) returned 0 bytes (transient), not re-fetched — immaterial given the conclusion below.
- **Publishing cadence gap worth flagging on its face:** zero posts between 2025-03-24 and 2026-01-14 (nearly 10 months of silence), then a resumption in Jan–Jul 2026. Raw fact, no interpretation offered.

### 3b.2 — Outbound link extraction and classification
Extracted every `href="http..."` per document, excluded voxlydigital.com/voxlyvision.com (own domains) and Wix platform infrastructure (parastorage.com, wixstatic.com, iubenda.com, a Scytale trust-center subdomain that is Dolphin Haley's own compliance-cert page). Counted **once per document** per the process's own rule.

**Result: 14 classified links total, across 5 of the 30 documents.** The other 25 documents (mostly client case studies) contain zero non-own outbound links — their only hrefs are to the client's own site (e.g., bristolairport.co.uk, seedlipdrinks.com, royalnavy.mod.uk, solacewomensaid.org, thebar.com, hideandfind.cadbury.co.uk) or embedded YouTube demo videos, which are neither "evidence for a claim" nor "someone else's commercial product" — they're the case study's own subject matter, so not counted either way.

| Document (date) | Domain | Classification |
|---|---|---|
| 5-best-compliance-ai-solutions-for-advertising-in-2026 (2026-03-02) | mckinsey.com | source |
| " | techradar.com | source |
| " | filestage.io | source |
| " | intelligencebank.com | source |
| " | asa.org.uk | source |
| " | persado.com | vendor/tool |
| how-compliance-ai-is-rewiring... (2026-01-14) | mckinsey.com | source |
| " | uk.surveymonkey.com | source |
| " | techradar.com | source |
| scaling-the-human-touch... (2026-02-04) | wpp.com | source |
| acamar-films...bingtime (2023-11-30) | ukscreenalliance.co.uk | source |
| " | aboutamazon.co.uk | source |
| " | amazon.co.uk (product listing) | vendor/tool |
| cadbury-hide-find-2022 (2022-11-30) | edinburghlive.co.uk | source |

(One nonsense/broken link — `http://time.It` inside the 5-best-compliance post, evidently an auto-linked typo in running prose — excluded as non-substantive, not a real citation.)

### 3b.3 — Named people, works cited, tools
- **Named individuals found in the corpus body text: two, both in one document** (`how-has-2020-changed-voice-habits`, 2021-10-01): **Rozzi Meredith**, described as "our Head of Innovation and Strategy" — a **colleague** (Voxly's own staff, not an external authority); and the two hosts of a podcast Voxly appeared on — **Kane Simms** and **Dustin Coates** (see communities, below) — classified as **authority/external** (industry hosts, not colleagues).
- **Zero other named individuals** appear anywhere across the other 29 documents — no analysts, no academics, no "as X said" quotes. (The Miguel Orlarte client quote noted above is from a case-studies *page*, not the blog RSS corpus, and is reported under 2.7 to keep the two evidence trails distinct.)
- **Works/data cited as evidence:** McKinsey QuantumBlack "State of AI" (cited twice, in two different 2026 posts); ASA Pulse Report on alcohol advertising; TechRadar creator-AI-tools article (cited twice); SurveyMonkey "AI marketing statistics" learn page; WPP's own published case study of Royal Navy work ("Atlas").
- **Tools named:** Voxly Vision (own product); competitors reviewed by name in the "5 Best" post — GetGen.AI, Red Marker, Persado Governance, Warrant; IntelligenceBank (DAM); Filestage (creative review/approval).
- **No hidden bibliography, no repo/reading-list, no observable uncredited borrowing detected.**

### 3b.4 — Diagnostic ratios
**RAN-NULL — insufficient sample.** 14 classified links across 5 distinct documents; the process's floor is **50 classified links across ≥5 documents**. Reporting raw, not forcing a ratio: of the 14 classified links found, 12 are source-type and 2 are vendor/tool-type — but this is far too small a base to support any source-vs-vendor read. The honest finding is about the *shape* of the corpus, not a ratio: Voxly's blog is overwhelmingly **client case-study content** (25 of 30 posts have no outbound citations at all — they're announcements, not arguments), with a **small recent cluster of analytical/opinion posts** (all 5 in-window posts, Jan–Jul 2026) that do cite outside sources, coinciding exactly with the pivot to Compliance-AI positioning and the post-Diageo-loss period Ravi described. That shift itself (case-study blog → cited-argument blog, starting ~Jan 2026) is a real, dateable, raw observation — offered here as fact, not spin.

---

## Findings — Layer 3c.1–3c.2: Communities

### 3c.1 — Named communities (from corpus + org channels)
**One genuine community found, in the corpus:** **VUX World** — an industry podcast/community for voice-UX practitioners (self-described "the practical voice podcast"; vux.world). Voxly's own 2021-10-01 blog post states Voxly's then Head of Innovation & Strategy, **Rozzi Meredith**, appeared as a guest, hosted by **Kane Simms and Dustin Coates**. [B20 (primary: Voxly's own post text), B26 (independent corroboration: Voicebot.ai's own profile of Kane Simms as VUX World co-founder, and vux.world's own site — confirms the community is real and the hosts named match, satisfying the "verify AI summaries against the actual page" rule with two independent primary sources)]. This is a company-level (Voxly-staff) appearance, not confirmed as Ravi Lal personally — flagged accordingly; do not conflate with a Ravi Lal personal appearance without further verification (that check belongs to Layer 1/browser-worker territory, outside my lane).

**One professional directory found, in org channels:** Amazon Alexa's "agencies and tools" partner directory (see 2.7 above) — a curated partner list, not a participatory community, but the closest thing to an industry "membership" Voxly has that is independently verifiable.

**Not counted as communities (noted for completeness, distinct from the above):** ISO 27001 and Cyber Essentials certification schemes — these are compliance/audit frameworks Voxly holds certifications under, not forums, boards, or associations with member participation. Including them as "communities" would overstate what was found.

**Not found despite checking:** no LinkedIn Group, Slack, Discord, subreddit, alumni group, or conference-circuit affiliation appears anywhere in the 30-document blog corpus or the org channel pages checked. (Texas Exes London and an Indiana University MBA affiliation are already on record in Layer 0 — but those came from the AI Jam transcript (S0), a different source than "the corpus" I mined; I have not independently re-discovered or verified them and am not re-classifying them as a 3c.1 corpus finding. That verification, if wanted, belongs to whichever worker owns S0 corroboration.)

### 3c.2 — Consumer surfaces, checked explicitly
Checked three consumer-surface categories:
1. **Reddit** — searched (`site:reddit.com "Voxly Digital"` / `"Ravi Lal" voice assistant`): **zero hits**. Direct platform fetch attempted and **BLOCKED-WALLED**: `reddit.com/user/spez/about.json` (known-good control account) returned HTTP 403, and `reddit.com/search.json?q=Voxly+Digital` also returned HTTP 403 — the wall is platform-wide, confirmed against a control per the process's own rule, so this is **not** reported as a confirmed absence.
2. **General forum/Discord search** — searched broadly for Voxly/Ravi Lal + "Discord," "forum," "community": zero hits.
3. **Facebook** — a Voxly Digital **brand page** exists (facebook.com/voxlydigital, per search snippet only, not fetched) — this is a company page, not a consumer community/group, and is listed under org channels (2.7), not counted here.

**Stated null:** Checked 3 consumer-surface categories over an unbounded (all-time) search window; none present as a genuine consumer community. Reddit specifically is BLOCKED-WALLED for direct verification, not a confirmed absence — flagged per the evidence contract.

---

## Source registry (worker B)

| ID | Source | Type | Accessed |
|---|---|---|---|
| B1 | voxlydigital.com (homepage, current) | primary | 2026-09-21 |
| B2 | voxlydigital.com/team (current) | primary | 2026-09-21 |
| B3 | voxlydigital.com/about-us (current) | primary | 2026-09-21 |
| B4 | voxlydigital.com/hiring (current) | primary | 2026-09-21 |
| B5 | voxlydigital.com/clients-industry-ai (current) | primary | 2026-09-21 |
| B6 | voxlydigital.com/voxly-case-studies/diageo-ai-innovation- (current) | primary | 2026-09-21 |
| B7 | find-and-update.company-information.service.gov.uk/search/companies?q=Voxly / q=Voxly+Digital | primary (Companies House) | 2026-09-21 |
| B8 | find-and-update.company-information.service.gov.uk/company/08396885 (overview) | primary | 2026-09-21 |
| B9 | .../company/08396885/officers | primary | 2026-09-21 |
| B10 | .../company/08396885/persons-with-significant-control | primary | 2026-09-21 |
| B11 | .../company/08396885/filing-history | primary | 2026-09-21 |
| B12 | .../company/08396885/filing-history/.../document?format=xhtml (AA, FYE 31 Mar 2026, filed 19 Jun 2026) | primary (statutory filing) | 2026-09-21 |
| B13 | .../company/08396885/filing-history/.../document?format=xhtml (AA, FYE 31 Mar 2025, filed 3 Jul 2025) | primary (statutory filing) | 2026-09-21 |
| B14 | find-and-update.company-information.service.gov.uk/search/officers?q=Ravi+Lal + 6 individual appointment pages | primary | 2026-09-21 |
| B15 | web.archive.org/cdx/search/cdx?url=voxlydigital.com* (315-row index) | primary (archive) | 2026-09-21 |
| B16 | web.archive.org/web/20190720082412/voxlydigital.com/google-stats-news (fetch test) | primary (archive) | 2026-09-21 |
| B17 | developer.amazon.com/en-GB/alexa/agencies-and-tools | primary | 2026-09-21 |
| B18 | developers.google.com/assistant/agencies | primary | 2026-09-21 |
| B19 | voxlydigital.com/blog-feed.xml | primary (RSS) | 2026-09-21 |
| B20 | 30 individual voxlydigital.com/post/... pages, raw HTML saved to `corpus/raw/` | primary | 2026-09-21 |
| B21 | WebSearch: "Voxly Digital" Ravi Lal Alexa agency | search-snippet (AI summary) | 2026-09-21 |
| B22 | WebSearch: site:reddit.com Voxly Digital / Ravi Lal | search-snippet | 2026-09-21 |
| B23 | curl control checks: reddit.com/user/spez/about.json, reddit.com/search.json, letterboxd.com/dave/ (all 403) | primary (negative/wall test) | 2026-09-21 |
| B25 | WebSearch: "Voxly Digital" Clutch/Drum/Campaign; Eagle Eye partnership; EU-Startups directory | search-snippet | 2026-09-21 |
| B26 | WebSearch: VUX World podcast Kane Dustin (corroboration) | search-snippet, cross-checked against vux.world and voicebot.ai | 2026-09-21 |

---

## UNVERIFIED block

- "Voxly Digital is Amazon & Google Recommended" / "official Google Assistant partner agency" — **CONTRADICTED BY PRIMARY SOURCE.** Amazon side confirmed (B17); Google side checked directly on Google's own current directory page and Voxly is absent (B18). Do not carry the Google claim forward as fact.
- Eagle Eye technology partnership — mentioned only in a search-result title (B25), not independently fetched or read in full. Lead only.
- EU-Startups, Crunchbase, Tracxn, ZoomInfo, ContactOut, Facebook page, LinkedIn company page listings — exist per search snippets, not fetched by me (aggregators / out-of-lane platforms). Leads only.
- Texas Exes London / Indiana University MBA affiliation — already on record in Layer 0 from the AI Jam transcript (S0), not independently re-verified by me as a corpus (3c.1) finding. Do not attribute this discovery to Layer 3b/3c without separate corroboration.
- VUX World appearance is attributed to Voxly staff (Rozzi Meredith) in a 2021 post — NOT verified as a Ravi Lal personal appearance. Do not upgrade to "Ravi Lal was on VUX World" without further check.
- The "amazon.co.uk" and "filestage.io"/"intelligencebank.com" link classifications above (vendor vs. source) are judgment calls at the margin, flagged as such in-line; raw links are given so the orchestrator can reclassify if it disagrees.
