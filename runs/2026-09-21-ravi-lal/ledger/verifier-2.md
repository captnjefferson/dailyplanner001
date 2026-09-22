# Adversarial verification — Voxly Digital claim (verifier-2)

Method note: no Chrome browser tools used. Independent verification via direct `curl` fetches of voxlydigital.com pages, Wayback Machine CDX API (archive.org), and WebSearch/curl against third-party domains (wpp.com, decisionmarketing.co.uk, greatstate.co, marketingdive.com, digiday.com). This deliberately avoids the collector's LinkedIn-authenticated source set (S-L7/S-L8/S-L9), which is walled to me, and instead tests the claim against agency/publisher sources the collector did not cite.

---

claim: "Voxly Digital today is a four-to-five-person company (Ravi Lal; Elliot Brock as CTO/Head of Technology, there since the start; two junior engineers Mini/Minhaz Karim and Alex/Alexandre Vander Elst; possibly Nimesh Patel as a technical program manager), it is currently advertising two open roles — Enterprise Sales (Junior/Mid) and Full Stack AI Software Engineer (Junior/Mid) — and its flagship offer is 'Voxly Vision', an agentic AI ad-compliance product, with Diageo (Don Julio, Baileys, Seedlip), the UK Royal Navy (the 'Atlas' avatar via WPP/Wavemaker) and Bristol Airport as named clients."

verdict: UNCONFIRMABLE (compound claim — sub-claims diverge; see split below. Two clients and the team roster confirm independently; Diageo and "Voxly Vision" as a validated product do not clear an independent bar and default to REFUTED per instructions.)

checked:
- Live re-fetch (curl, 2026-09-21) of https://voxlydigital.com/team, /hiring, /about-us — full text extracted and quoted below
- Wayback Machine CDX for voxlydigital.com/hiring, /team, /about-us — snapshot history and content-length diffs
- Text diff of /hiring across 5 Wayback snapshots (2025-04-22 through 2026-06-08)
- wpp.com/en/case-studies/wpp-royal-navys-atlas — fetched, Voxly named 4×
- decisionmarketing.co.uk/news/royal-navy-dives-into-ai-recruitment-with-wavemaker — fetched, Voxly named 1×
- greatstate.co/work/casestudy/powering-smarter-travel-with-ai/ — fetched, Voxly named 1×
- greatstate.co/work/casestudy/bristol-airport-customer-chatbot/ — 404, dead link (search-indexed URL no longer resolves)
- marketingdive.com/news/how-ai-helping-diageo-target-audiences-navigate-regulatory-waters — fetched in full (295KB), zero mentions of "Voxly"
- creativebrief.com/bite/interview/brand-leader/how-diageo-is-embracing-the-ai-opportunity — 403 Forbidden, could not verify
- seedlipai-diageoai.diageoplatform.com — 200 but returns an unrendered JS-app shell (1166 bytes raw HTML), zero mentions of "Voxly" — inconclusive (client-side rendered, not a refutation)
- WebSearch passes for: Diageo Marketing Code + Voxly trade press; Ravi Lal + Diageo press interview; "Voxly Vision" on Product Hunt/G2/Capterra

finding: |
  Sub-claim (a) TEAM SIZE/NAMES — CONFIRMED for 4 of the claimed 4–5; UNCONFIRMABLE for the 5th.
  Live /team page (re-fetched independently, matches S1) names exactly four people, verbatim:
  "Founder Ravi Lal... Head of Technology Elliot Brock — It would be hard to overstate Elliot's
  impact at Voxly Digital. One of the OGs, he's been here since day one... Full Stack AI Engineer
  Mini Karim... Full Stack AI Engineer Alex Vander Elst [Imperial College, Applied Computational
  Science and Engineering MSc]." This confirms Ravi Lal, Elliot Brock ("Head of Technology" —
  note the site itself never says "CTO," only the claim's own hedge covers that), Mini Karim, and
  Alex Vander Elst, including "since day one" for Brock. Nimesh Patel appears NOWHERE on the
  company's own team page — he is not independently confirmable from any non-LinkedIn source I
  could reach (LinkedIn People tab S-L9 is walled to me; RocketReach/Crunchbase aggregators only
  mirror LinkedIn/company-site data and did not surface him either). The claim already hedges this
  ("possibly"), so it is not refuted, but the primary source the collector cited for team
  composition (S1) does not itself support a 5-person count — only 4 people are the company's own
  public claim.

  Sub-claim (b) TWO LIVE POSTINGS — CONFIRMED as literally true, but STALE / low-signal.
  Live /hiring page (re-fetched, matches S2) lists exactly, verbatim: "Job Opening Enterprise
  Sales (Junior / Mid Level)" and "Job Opening Full Stack AI Software Engineer (Junior / Mid
  Level)" — nothing else. However, Wayback CDX + snapshot diffs show this exact pairing,
  byte-for-byte identical posting text, present continuously from at least 2025-10-13 through
  2026-01-19, 2026-03-14, and 2026-06-08 (11+ months unchanged); the Full Stack AI Software
  Engineer posting alone traces back unchanged to the 2025-04-22 snapshot (17 months). This is
  strong evidence these are evergreen/vestigial listings rather than fresh, actively-worked reqs —
  "currently advertising" is technically true today but should not be read as a signal of an
  imminent hire or recent headcount need.

  Sub-claim (c) VOXLY VISION AS A VALIDATED PRODUCT — UNCONFIRMABLE, effectively REFUTED as an
  independently-evidenced product. All descriptions of "Voxly Vision" (agentic AI co-pilot,
  scans creative against brand rules, "near-instant reporting," "100% compliance") trace only to
  Voxly's own site (about-us/complianceai pages). I found zero Product Hunt listing, zero
  G2/Capterra listing or reviews, no pricing page, no demo page, and no independent trade-press
  piece (Marketing Dive, Digiday, Marketing Week, Adweek, Campaign, Creativebrief) that names
  "Voxly" or "Voxly Vision" in connection with any deployment. The only two deployments with real
  third-party (non-Voxly, non-LinkedIn) confirmation — Royal Navy Atlas and Bristol Airport — are
  both from a *different* Voxly product line (conversational avatar / customer-service chatbot),
  not the "Voxly Vision" ad-compliance line the claim names as flagship. So the flagship product
  itself is a website-only assertion.

  Sub-claim (d) NAMED CLIENTS — split verdicts:
  - UK Royal Navy / "Atlas" avatar via WPP/Wavemaker: CONFIRMED independently, from two sources
    neither Voxly-owned nor LinkedIn. wpp.com/en/case-studies/wpp-royal-navys-atlas: "In a
    groundbreaking partnership, the Royal Navy, WPP's Wavemaker, and Wavemaker's partner Voxly
    Digital, have developed Atlas..." decisionmarketing.co.uk: "Voxly Digital developed the front
    and back end of the solution, supported by the Royal Navy's digital agency, Great State."
    Presented as a current/ongoing engagement (WPP piece dated ~Nov 2025, Atlas shortlisted for
    2026 Campaign Media Awards per search snippets) — no evidence it's a lapsed/former client.
  - Bristol Airport: CONFIRMED independently. greatstate.co (Bristol Airport's own lead agency,
    per the page) states in its own case study: "As Bristol Airport's lead strategic agency, we
    partnered with specialists Voxly Digital to develop and deploy the always-on, AI-powered
    chatbot." Non-Voxly, non-LinkedIn, and Great State has no incentive to over-credit a
    subcontractor. Current tense, no indication of a past/ended relationship. Note: the specific
    greatstate.co URL surfaced by search (/casestudy/bristol-airport-customer-chatbot/) 404s —
    the live case study now lives at a different slug (/casestudy/powering-smarter-travel-with-ai/).
  - Diageo (Don Julio, Baileys, Seedlip): NOT independently confirmed. Every mention of Voxly +
    Diageo I could find traces back to voxlydigital.com's own case-study pages or to aggregators
    (RocketReach, Crunchbase) that mirror company/LinkedIn self-description. A full fetch of the
    one plausible independent trade-press candidate (Marketing Dive's Diageo AI/regulatory piece,
    295KB of body text) contains zero occurrences of "Voxly." A Diageo-owned subdomain
    (seedlipai-diageoai.diageoplatform.com) returned only an empty JS shell — inconclusive, not
    a refutation, but not corroboration either. creativebrief.com's Diageo AI interview returned
    403 and could not be checked. Given the instruction to default to REFUTED absent independent
    confirmation, I am marking this REFUTED-for-verification-purposes: the underlying business
    relationship may well be real (Voxly's own site is detailed and internally consistent, and
    "Seedlip" specifically is not even named on the about-us page I re-fetched — only "Don Julio,
    Baileys, etc." — so the claim's inclusion of "Seedlip" appears to come from a different Voxly
    blog post, not S1–S3), but it does not clear an independent evidentiary bar the way Royal Navy
    and Bristol Airport do.

source_ids: [S1, S2, S3, S16 (weak — mirrors company/LinkedIn self-description, not independent)]
