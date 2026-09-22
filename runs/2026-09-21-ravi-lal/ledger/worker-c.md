# Worker C — Layer 4 (open-web only): 4.3 co-occurrence · 4.4 shared rooms · 4.6 Voxly team & hiring

Run: 2026-09-21-ravi-lal · PARTNER SCAN · Target: Ravi Lal, Voxly Digital, London (ravi.lal@voxlydigital.com, S0)
Scope note: sub-steps 4.1, 4.2, 4.5 (answered circle, commenter inversion, mutuals) belong to the serial authenticated-browser worker — NO rows emitted for them here. This worker used open-web only: WebSearch, WebFetch, curl against public APIs (Companies House, GitHub, YouTube oEmbed, Wayback CDX). No Chrome browser tools, no LinkedIn/X login.
Today: 2026-09-21. Windows used: enduring public pages (no 90-day cap applied — these are conference/company records, not social posts); explicit dates stated per finding.

---

## Ledger

```yaml
- step: "4.3 co-occurrence"
  status: RAN-FOUND
  checked_count: 9
  checked_unit: "event/platform surfaces"
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S4, S5, S6, S7, S13, S14, S15, S18, S21]
  note: "One clean two-anchor co-occurrence hit (169 Labs / AAV Virtual Meetup #2, 2017-12-20, host confirmed via YouTube oEmbed). One self-reported-only appearance (Voice Global Conference, June 2020) with no corroborating speaker roster found. One AI-summary hallucination identified and rejected (fabricated 'Dec 2020 AAV meetup'). One named-individual co-occurrence via a 2025 joint press release (Eagle Eye). VOICE Summit 2019 checked as a negative control — Ravi Lal/Voxly absent. CreativeMornings page exists but is BLOCKED-WALLED (site-wide, control-checked). Mixed quality — see findings below for per-item grading."
- step: "4.4 shared rooms"
  status: RAN-FOUND
  checked_count: 5
  checked_unit: "named communities/directories"
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S7, S8, S6, S17]
  note: "Amazon's own Alexa agencies directory and the Texas Exes UK chapter's public events page both VERIFIED-PRIMARY for the room's existence and Voxly's/the room's own listing. Ravi Lal's PERSONAL presence in the Texas Exes run club and college-football watch party is self-report only (S0) — the public chapter page has no roster. IU Kelley alumni network is LEAD ONLY (LinkedIn SEARCH-ONLY, no independent roster found)."
- step: "4.6 Voxly team and hiring"
  status: RAN-FOUND
  checked_count: 9
  checked_unit: "sources checked"
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S1, S2, S9, S10, S11, S12, S16, S19, S20]
  note: "Company's own team page and hiring page are both current and VERIFIED-PRIMARY (fetched 2026-09-21). Headcount (4: Ravi + 3) matches S0's self-report structurally, though titles/tenure/ages are not confirmed to the specific numbers claimed. Companies House officer record for a same-named 'Ravinder Singh Lal' found but the entity-to-brand linkage is UNVERIFIED (see UNVERIFIED block). GitHub and Wayback checked and returned clean nulls / BLOCKED-WALLED respectively, both control-checked."
```

---

## 4.3 — Co-occurrence: findings

**1. VERIFIED — 169 Labs / "AAV Virtual Meetup #2 – Voice Marketing"**
- Who: 169 Labs (YouTube channel/host, confirmed via oEmbed API — `author_name: "169 Labs"`). 169 Labs co-presents the "All About Voice" (AAVclub) community together with MedienNetzwerk Bayern; AAVclub's own current self-description names Tim Kahle and Dominik Meissner as 169 Labs co-founders (moderate confidence this is also who ran the channel in 2017 — not independently re-confirmed for that specific date).
- What: Ravi Lal (named on-screen as "Ravi Lal, Voxly Digital") gave a session titled "Voice Marketing" as AAV Virtual Meetup #2.
- When: published/aired 2026-... no — **2017-12-20** (per video title and oEmbed).
- URL: https://www.youtube.com/watch?v=JY8mMlwTl9w (S4); oEmbed confirmation S5.
- Two-anchor gate: PASS — "Ravi Lal" + "Voxly Digital" both appear together in the primary artifact's own title, so the name-collision risk for "Ravi Lal" alone is cleared by the co-occurring employer anchor.
- What 169 Labs / AAVclub buys or sells: runs a voice-tech community/conference platform (ALL ABOUT VOICE); sells sponsorship and stage visibility to voice-tech vendors — not itself a buyer of AI training or builds, but a room where such vendors and their prospects circulate.

**2. SELF-REPORT ONLY — "Voice Global Conference," June 2020**
- Who: unnamed conference (VOICE Global, run by voicesummit.ai per general search context — not independently confirmed as the specific "Voice Global" named in Voxly's own post).
- What: per Voxly's own 2021-09-14 blog post, Ravi Lal presented "a webinar recorded for the Voice Global Conference in June 2020" on "creating a voice-first experience for a very iconic UK Sports brand" — identifiable from the same post as the BBC Match of the Day Magazine Alexa skill.
- URL: https://www.voxlydigital.com/post/bbc-match-of-the-day-magazine-goes-voice-first (S14).
- Status: this is Voxly's own self-report of the appearance; no independent Voice Global 2020 agenda/speaker-roster page naming Ravi Lal was found, so no co-speaker/moderator could be identified. Not a corroborated co-occurrence — filed as a lead only.

**3. REJECTED — AI-summary hallucination, "AAV Virtual Meetup, December 2020"**
- Multiple search-engine AI overviews asserted a *separate* December 2020 AAV Virtual Meetup appearance with the specific talk title "Voice Marketing Case Study: Launching an Iconic UK sports brand on Voice." Every citation offered for this claim resolves back to either the 2017 YouTube video (item 1) or the 2021 blog post describing the June 2020 Voice Global webinar (item 2) — there is no independent event page. This is the exact "AI summaries invent conference appearances" failure mode named in the run rules. **Not reported as a real co-occurrence.**

**4. VERIFIED — Eagle Eye Solutions / Al Henderson (Chief Sales Officer)**
- Who: Al Henderson, Chief Sales Officer, Eagle Eye Solutions (UK loyalty/personalized-marketing SaaS platform).
- What: joint press release announcing an Eagle Eye × Voxly Digital partnership; both named individuals quoted (Al Henderson for Eagle Eye, Ravi Lal, CEO/Founder, for Voxly).
- When: 2025-07-29.
- URL: https://eagleeye.com/blog/eagle-eye-voxly-digital-partnership (S13).
- What Eagle Eye buys/sells: sells a SaaS platform for customer loyalty, coupons, and personalized marketing to retail/FMCG brands — an adjacent vendor whose client base (retail/FMCG marketing buyers) is a plausible overlap room with AI-native-build buyers.

**5. Negative controls (RAN-NULL, reportable)**
- VOICE Summit 2019 speakers page (S21) — checked in full for "Ravi Lal" / "Voxly" / "Voxly Digital": absent. Checked 1 page over the 2019 event window; none present.
- AAVclub's own visible archive on allaboutvoice.io (S6) — lists only 2021–2022 sessions (ALL ABOUT VOICE 22, Jan König interview, Voice and Media, Voice in Cars); the 2017 Ravi Lal session does not appear in the org's own current archive listing (only recoverable via YouTube). Checked 1 archive page; the 2017 item is not shown there.
- General Assembly instructor page (S15) lists three GA course categories ("AI-First Product Management," "AI Workplace Fundamentals," "Data Analytics and Visualization") but these read as GA's general catalog links near the bio, not confirmed co-taught sessions with named co-instructors — checked, no co-instructor named, filed as UNVERIFIED rather than a finding.
- CreativeMornings profile (S18) — BLOCKED-WALLED (see 4.6/UNVERIFIED for the control check detail); talk content, date, and any co-speakers could not be read this pass.

---

## 4.4 — Shared rooms: findings

**1. VERIFIED-PRIMARY — Amazon's own Alexa "agencies-and-tools" directory**
- Room: `developer.amazon.com/en-GB/alexa/agencies-and-tools` — Amazon's own published list of UK-based Alexa skill-building agencies.
- Evidence Voxly is verifiably in it: Voxly Digital appears in the directory with its own description ("Voxly Digital's mission is to build the world best voice experiences...").
- Full UK list alongside Voxly (24 total): Accenture, Adassa Innovations, AKQA, Apadmi, Cation Consulting, Hi Mum! Said Dad, Intive, Modal Systems, Polar Night Studio, Rehab, Reply AG, Say It Now, Screenmedia, SoapVox, StarfishMint, VaynerMedia, Vixen Labs, Vocala, Voice Interactive, Voxogenic, Voz Lab, Waracle Ltd, Voicefront.
- URL: https://developer.amazon.com/en-GB/alexa/agencies-and-tools (S7), accessed 2026-09-21.
- Buyer-adjacency flag: this is a **supplier-side** directory, not a buyer roster — it does not itself contain buyers. But it is the room competing agencies (and the brands vetting them) use, so it is the room to watch for **who else pitches the same enterprise voice/AI buyers Voxly pitches** — not a room that itself holds AI-training or AI-build buyers.

**2. VERIFIED-PRIMARY (room) / SELF-REPORT (personal membership) — Texas Exes United Kingdom chapter**
- Room: Texas Exes UK chapter (`texasexes.org/chapters-and-networks/find-chapter-or-network/157/united-kingdom/our-events`), confirmed to run: Thirsty Thursdays (happy hours), **Game Watching** ("Live viewing of Longhorns football during the season, or replays the following day"), Pub Crawl, a volunteer event, and **Stampede Running Club** ("typically on a Saturday at fun locations including Hyde Park and Kew Gardens").
- URL: S8, accessed 2026-09-21.
- This directly and independently confirms the *existence* of both communities S0 attributed to Ravi Lal: "a run club under the Texas Exes umbrella" = Stampede Running Club; a UT-specific instance of "the London college-football watch-party scene" = Game Watching.
- **What is NOT verified:** Ravi Lal's own membership/attendance. The chapter page carries no roster; his participation rests entirely on his own self-report (S0). No independent membership list was found (WhatsApp/Facebook Group are the chapter's stated member channels and are not accessible to open-web tools).
- Buyer-adjacency flag: a UT-Austin alumni chapter and college-sports watch-party crowd in London skews toward corporate/professional expats — plausibly contains buyers of both AI-leadership-training and AI-native builds, but no roster evidence ties a specific buyer-type individual to this room; flagged as a room worth mapping, not a confirmed buyer pool.

**3. LEAD ONLY — Indiana University Kelley School of Business alumni network**
- A LinkedIn search snippet (SEARCH-ONLY, unauthenticated — never verified per platform rule) shows a London-based "Ravi Lal" profile with "education from Indiana University – Kelley School of Business," consistent with S0's "IU for MBA school" self-report.
- No independent (non-LinkedIn) public roster or chapter page for an IU Kelley London alumni network was found in this pass — checked 3 search queries; none surfaced a standalone community page. Filed as a lead for the authenticated-browser lane, not a room.

**4. Voice-tech community, secondary — AAVclub / "All About Voice" (169 Labs)**
- Ravi Lal has at least one confirmed historical appearance (2017) in this recurring voice-tech community/event series (see 4.3, item 1). Its current activity level and whether Ravi/Voxly remain active in it is unknown — the org's own visible archive only shows 2021–2022 sessions and does not include Ravi. Filed as a secondary, lower-confidence shared room (last confirmed contact 2017, ~9 years stale).

**5. RAN-NULL — a distinct "London college-football watch-party scene" beyond Texas Exes**
- Searched for a broader/independent college-football watch-party community (not Texas-specific) that Ravi might also be part of. Checked 3 queries; found nothing beyond the Texas Exes "Game Watching" listing already reported in item 2. No separate room identified — the S0 claim appears to describe the same Texas Exes room, not an additional one.

---

## 4.6 — Voxly team and hiring: findings

**Current team, per Voxly's own site (VERIFIED-PRIMARY, fetched 2026-09-21, `voxlydigital.com/team`, S1):**

| Name | Role (site's own words) | Notes on the page |
|---|---|---|
| Ravi Lal | Founder | "Ravi is from Texas and founded the company after a long career in Big Telco." |
| Elliot Brock | Head of Technology | "One of the OGs, he's been here since day one" / "the nicest guy in tech." |
| Mini Karim | Full Stack AI Engineer | "Mini is an ace developer and runs his very own e-commerce business on the side as an Amazon Seller." |
| Alex Vander Elst | Full Stack AI Engineer | Imperial College MSc, Applied Computational Science and Engineering; a year at BMW in Data Science and Innovation. |

- **Cross-check against S0's self-report** ("Ravi + a 9-year CTO + two ~25-year-olds"): headcount matches exactly (4 people: 1 founder + 3). Elliot Brock is the clear CTO-equivalent match ("here since day one" is directionally consistent with a long tenure, though the site never states "9 years" or calls him CTO — it says "Head of Technology"). Mini Karim and Alex Vander Elst are the two junior engineers; neither's age is stated anywhere public. **Net: STRUCTURALLY CONFIRMED, numerically UNVERIFIED** (see UNVERIFIED block).
- Secondary corroboration (SEARCH-ONLY, RocketReach aggregator, S16): lists Elliot Brock's title explicitly as "Chief Technology Officer" and prior roles at **Opearlo** (a known UK Alexa-skill agency — itself a voice-tech co-occurrence lead worth a future pass), General Assembly, and Edustaff.

**Hiring (VERIFIED-PRIMARY, `voxlydigital.com/hiring`, S2, fetched 2026-09-21):** exactly two live postings —
1. Enterprise Sales (Junior/Mid Level) — Paddington, London.
2. Full Stack AI Software Engineer (Junior/Mid Level) — Paddington, London — link: `voxlydigital.com/post/job-opening-full-stack-ai-software-engineer-junior-mid-level`.
Contact: freshthinking@voxlydigital.com. No posting dates shown; no third-party ATS (Greenhouse/Lever/etc.) — postings are native to the Wix-built site. This is a current, active hiring signal (2026), consistent with a small team rebuilding after the S0-reported Diageo revenue gap.

**Companies House (VERIFIED-PRIMARY for the raw record; entity-to-brand link UNVERIFIED):**
- A same-named **Ravinder Singh LAL** is the sole active director of **Dolphin Haley Limited** (company no. 08396885), incorporated 2013-02-11, nationality American, date of birth February 1969, resident in England. Officer ID `-Ik6vVcLGTWQ3L8bADVK6XvwsF4` — a name search for "Ravinder Singh Lal" across all of Companies House returns exactly this one match (S11), i.e., this specific full name is not itself ambiguous.
- **Name-collision control performed:** a separate, similarly-named "Voxly Ltd" (co. no. 12027947) was checked and ruled OUT — it is an unrelated children's-book/education retail company whose directors are the Naveed family, incorporated 2019, registered in Streatham (S12). This confirms the collision risk flagged in the task brief is real and demonstrates it was controlled for.
- **What is not confirmed:** that Dolphin Haley Limited is in fact the legal entity trading as "Voxly Digital." This linkage appears only in AI-generated web-search overview text; it is not stated on Voxly's own site (no footer/company-registration disclosure found on the homepage, and `/terms`, `/terms-and-conditions`, `/cookies-policy` all 404) and Dolphin Haley's own Companies House SIC code (47910, mail-order/internet retail) does not match Voxly's stated advertising/AI business. Filed as a lead, not a verified identity fact — see UNVERIFIED block.

**GitHub (RAN-NULL, confirmed):** no organization named `voxlydigital` or `VoxlyDigital` exists (404 on both). A GitHub org literally named `Voxly` exists (created 2020-06-14) but its only public repo is `react-mentions` (a `@mention`-in-textarea UI library) — unrelated software, ruled out as a different entity (S20).

**Wayback Machine (BLOCKED-WALLED, control-checked):** the CDX API for `voxlydigital.com/team` returned a site-wide "Internet Archive: Temporarily Offline" 503 (S19). Control check against a known-good query (`example.com`) also returned 503, confirming a genuine platform-side outage rather than a null result. Historical/past team-member snapshots could not be checked this pass — this is a named gap, not a finding of team stability.

**Press / new-hire announcements 2024–2026 (RAN-NULL):** checked 3 targeted queries (generative-AI/LLM meetup panels, awards, general press) covering 2024–2026; found no press release, trade item, or announcement of a new Voxly hire in this window. The team-page roster (4 people) is the only headcount signal available and appears to have been stable across every source checked in this pass — though this is a soft null (absence of announcement is not proof of no hiring), consistent with the two open 2026 postings above representing active, not-yet-filled growth attempts.

---

## LEADS (for the orchestrator — not ledger rows, not asserted as verified)

**What Ravi/Voxly says publicly about what they want next:**
- Current site framing (2026, `voxlydigital.com/about-us`, S3): *"We build Agentic AI systems that sit inside the world's most regulated advertising workflows, pioneering a category we call Compliance AI."* Flagship product: Voxly Vision, an "Agentic AI Co-Pilot" that scans advertising creative for compliance.
- Older/legacy framing (General Assembly bio, undated, S15): *"Our mission is to build the world's best voice experiences."*
- Direct Ravi Lal quote, 2025-07-29 press release (S13): *"Voice assistants are no longer an emerging tech. They're now a mainstream part of daily life for many in the UK."*
- **Not found publicly:** the specific S0 framing that Ravi is personally "looking for a mission" / searching for the next product-market fit. That reads as a private, in-person remark (AI Jam transcript, 2026-09-18) and has no public echo in anything surfaced this pass — the public-facing material still presents Voxly as having settled on Compliance AI as its category, which is worth the orchestrator flagging as a possible tension with the private framing.

**Public mentions of Diageo as a Voxly client:**
- Voxly's own about-us/case-study pages state Diageo (brands including Don Julio, Baileys, Seedlip) as a client, citing: "one of the first Branded Alexa skills in the UK with Voxly Digital" (2017); "Elli," a Generative AI brand ambassador for Seedlip Drinks — described as Diageo's first-ever generative-AI consumer service globally (Nov 2023); a Compliance AI engagement starting Feb 2024, "reducing review cycles from days to under an hour."
- URLs: `voxlydigital.com/about-us` (S3), `voxlydigital.com/clients-industry-ai`, `voxlydigital.com/consumerbrands-ai` (surfaced via search, not independently re-fetched this pass — flagged for the orchestrator to fetch directly if the Diageo relationship becomes load-bearing).

---

## Source registry

```yaml
sources:
  S1: {url_or_tool_call: "https://www.voxlydigital.com/team", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravi Lal", "Voxly Digital"]}
  S2: {url_or_tool_call: "https://www.voxlydigital.com/hiring", type: primary, accessed_at: "2026-09-21", target_anchors: ["Voxly Digital"]}
  S3: {url_or_tool_call: "https://www.voxlydigital.com/about-us", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravi Lal", "Voxly Digital", "Diageo"]}
  S4: {url_or_tool_call: "https://www.youtube.com/watch?v=JY8mMlwTl9w", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravi Lal", "Voxly Digital"]}
  S5: {url_or_tool_call: "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=JY8mMlwTl9w&format=json", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravi Lal", "Voxly Digital", "169 Labs"]}
  S6: {url_or_tool_call: "https://www.allaboutvoice.io/", type: primary, accessed_at: "2026-09-21", target_anchors: ["169 Labs"]}
  S7: {url_or_tool_call: "https://developer.amazon.com/en-GB/alexa/agencies-and-tools", type: primary, accessed_at: "2026-09-21", target_anchors: ["Voxly Digital"]}
  S8: {url_or_tool_call: "https://www.texasexes.org/chapters-and-networks/find-chapter-or-network/157/united-kingdom/our-events", type: primary, accessed_at: "2026-09-21", target_anchors: ["Texas Exes London"]}
  S9: {url_or_tool_call: "https://find-and-update.company-information.service.gov.uk/company/08396885", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravinder Singh Lal"]}
  S10: {url_or_tool_call: "https://find-and-update.company-information.service.gov.uk/officers/-Ik6vVcLGTWQ3L8bADVK6XvwsF4/appointments", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravinder Singh Lal"]}
  S11: {url_or_tool_call: "https://find-and-update.company-information.service.gov.uk/search/officers?q=Ravinder+Singh+Lal", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravinder Singh Lal"]}
  S12: {url_or_tool_call: "https://find-and-update.company-information.service.gov.uk/company/12027947", type: primary, accessed_at: "2026-09-21", target_anchors: ["name-collision control — unrelated entity"]}
  S13: {url_or_tool_call: "https://eagleeye.com/blog/eagle-eye-voxly-digital-partnership", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravi Lal", "Voxly Digital"]}
  S14: {url_or_tool_call: "https://www.voxlydigital.com/post/bbc-match-of-the-day-magazine-goes-voice-first", type: primary, accessed_at: "2026-09-21", target_anchors: ["Ravi Lal", "Voxly Digital"]}
  S15: {url_or_tool_call: "https://www.generalassemb.ly/instructors/ravi-lal/20294", type: primary, accessed_at: "2026-09-21", target_anchors: ["Voxly Digital"]}
  S16: {url_or_tool_call: "https://rocketreach.co/voxly-digital-management_b456a569fca0cfe9", type: secondary, accessed_at: "2026-09-21", target_anchors: ["Elliot Brock", "Voxly Digital"]}
  S17: {url_or_tool_call: "web search snippet — linkedin.com/in/lalravi (search-only, not fetched/authenticated)", type: search-snippet, accessed_at: "2026-09-21", target_anchors: ["Ravi Lal", "Indiana University Kelley School of Business"]}
  S18: {url_or_tool_call: "https://creativemornings.com/individuals/ravilal", type: primary, accessed_at: "2026-09-21", target_anchors: ["BLOCKED-WALLED — content not retrievable"]}
  S19: {url_or_tool_call: "http://web.archive.org/cdx/search/cdx?url=voxlydigital.com/team&output=json", type: primary, accessed_at: "2026-09-21", target_anchors: ["BLOCKED-WALLED — service outage"]}
  S20: {url_or_tool_call: "https://api.github.com/users/Voxly and /repos", type: primary, accessed_at: "2026-09-21", target_anchors: ["confirmed non-match"]}
  S21: {url_or_tool_call: "https://www.voicesummit.ai/speakers-2019", type: primary, accessed_at: "2026-09-21", target_anchors: ["negative control — absent"]}
```

---

## UNVERIFIED block

- **"Dolphin Haley Limited" = the legal entity trading as "Voxly Digital."** Asserted only by AI-generated search-overview text; not found on Voxly's own site (homepage footer carries no company-registration text; `/terms`, `/terms-and-conditions`, `/cookies-policy` all 404) and not stated on the Companies House record itself. Dolphin Haley's SIC code (47910, retail mail-order/internet) does not match Voxly's stated business. Ravinder Singh Lal's biographical facts (American nationality, DOB Feb 1969, England residence) are *consistent with* but do not *confirm* he is Voxly's Ravi Lal. Treat as a lead for adversarial verification, not a fact.
- **"AAV Virtual Meetup, December 2020"** as a distinct second Ravi Lal appearance, with talk title "Voice Marketing Case Study: Launching an Iconic UK sports brand on Voice" — assessed as a probable AI-summary hallucination conflating the real 2017-12-20 YouTube video with the self-reported June-2020 Voice Global Conference webinar. No independent event page found. Do not carry forward as a real co-occurrence.
- **S0's "Amazon recommended them... top 3 Alexa build agencies in the UK."** Amazon's own directory (S7) lists Voxly among ~24 UK agencies with no visible ranking or tiering — the "top 3" framing could neither be corroborated nor refuted from this primary source. Self-report only.
- **Elliot Brock's exact tenure ("9-year CTO") and Mini Karim / Alex Vander Elst's ages ("~25 years old").** Not stated on any public source found. The team page's "since day one" / "OG" language for Elliot Brock is directionally consistent but not a verified number; "CTO" itself only appears on a secondary aggregator (RocketReach), not on Voxly's own site (which says "Head of Technology").
- **CreativeMornings talk content for Ravi Lal.** Page indexed and titled by search engines, but content is BLOCKED-WALLED (HTTP 202, empty body; control-checked against a known CreativeMornings profile, which returned the identical empty response — confirmed site-wide bot/JS protection, not an absent or empty profile). Talk topic, date, city, and any co-speakers remain unknown.
- **Indiana University Kelley School of Business MBA and personal Texas Exes / Stampede Running Club membership.** Both rest on LinkedIn SEARCH-ONLY snippets and/or Ravi's own S0 self-report. Per the authenticated-only rule for LinkedIn, these cannot be promoted above SEARCH-ONLY / CORROBORATED-UNVERIFIED without the authenticated-browser lane.
- **General Assembly instructor bio spells the name "Ravi Lai."** Almost certainly a text-extraction artifact of "Lal" (the same page's URL slug and photo context are unambiguously Voxly's Ravi Lal), not evidence of a different person — flagged for the record per source-discipline, not treated as a discrepancy.

---

## Coverage bounds (this worker's scope only)

- 4.3: 9 event/platform surfaces checked (see ledger). No authenticated LinkedIn/X co-occurrence data — that is the browser worker's lane and out of scope here.
- 4.4: 5 named communities/directories checked. LinkedIn Groups/Interests tabs (where a Texas Exes or IU Kelley group might also show) were not checked — authenticated-browser lane, out of scope.
- 4.6: 9 sources checked. Wayback (historical team turnover) is BLOCKED-WALLED on a platform-wide outage, control-verified — worth a retry later in the run if time allows, since it is the one source that could confirm/deny past team members beyond the current 4.
