# Verifier-3 — Adversarial check on the "thin public surface" null

## Method note
Tools used: WebSearch, WebFetch, curl (iTunes Search API, YouTube oEmbed, Google Books API,
Filmot, Medium, VUX World site search), no browser. LinkedIn and X/Twitter are walled to me —
every hit that traced back to LinkedIn (several did, via WebSearch AI-overview summaries) was
excluded from consideration per the claim's own scope ("off LinkedIn and his own company
website") and is flagged below, not counted as evidence either way. AI search-overview prose was
never taken at face value — every candidate URL was opened directly (WebFetch/curl) or cross-
checked with a second query before being counted.

Different strategy than the collector: instead of Voicebot.ai tag pages, I queried the iTunes/
Apple Podcasts Search API directly (`itunes.apple.com/search`, entity=podcastEpisode) for "Ravi
Lal Voxly" and "Voxly Digital" — this indexes Apple's full podcast-episode corpus, not just one
site's tag page. Instead of fetching The Drum/Campaign/Marketing Week directly, I searched a
wider ring of trade press plus regulator/industry-body sites, event platforms, YouTube (scrape +
oEmbed title/author verification per video ID, not just title-string search), Filmot, Google
Books, Medium, Crunchbase, and PitchBook.

## claim
"Off LinkedIn and his own company website, Ravi Lal (Founder & CEO, Voxly Digital, London) has a
thin public surface: no podcast appearance since Voicebot.ai Ep 128 (2019-12-23), no conference
or webinar appearance since the 2017 AAV Virtual Meetup, no bylined trade-press article, no
personal website or newsletter, and no public statement that he or Voxly is 'looking for a
mission' or a new direction — the public material still presents Compliance AI / Voxly Vision as
the settled category."

## verdict: CONFIRMED

## checked (surfaces/sources, ~43 total)
- Podcasts: iTunes/Apple Podcasts Search API (2 queries: "Ravi Lal Voxly", "Voxly Digital"),
  Listen Notes (blocked 403; supplemented via WebSearch), Spotify (WebSearch)
- Video/captions: YouTube search scrape + oEmbed verification of 4 distinct video IDs, Filmot
  (blocked — inconclusive, not counted as clean)
- Long-form/authored: Google Books API (quota-exceeded — inconclusive), Amazon (WebSearch),
  Medium direct search (403 — inconclusive) + WebSearch, Substack (WebSearch), Beehiiv (WebSearch)
- Events: Eventbrite/Luma/Meetup (WebSearch), MAD//Fest lineup page + WebSearch, Advertising Week
  Europe, Cannes Lions, DMEXCO, Voice Summit/Modev, Alexa Live, Tech London Advocates,
  MassChallenge UK, Texas Exes UK (all WebSearch)
- Trade press beyond the collector's three: PRWeek, Creative Review, LBBonline, Adweek, Digiday,
  AdExchanger, ExchangeWire, MarTech, VUX World (site search attempted directly, redirected;
  supplemented via WebSearch)
- Regulators/bodies: Portman Group, ASA, ISBA, IPA, DMA (incl. site:dma.org.uk)
- Corporate/partner pages: Diageo, WPP, Wavemaker, Great State, Tavus, Eagle Eye (blog fetched
  directly), Solace Women's Aid (404 on the specific URL — inconclusive)
- Company intelligence: Crunchbase (403 direct fetch; WebSearch overview only), PitchBook
  (WebSearch — no funding/news hits)
- Misc profiles: CreativeMornings (personal attendee profile, not a talk record), General
  Assembly instructor page (fetched directly — current instructor listing, no dated live session
  found), IMDb (unrelated actor namesake)

## finding
No qualifying appearance, byline, or "new direction" statement after 2019 surfaced under this
different methodology. Specifics:

**Podcasts** — The Apple Podcasts Search API (independent of any single site's tag pages) returns
exactly one episode matching "Ravi Lal Voxly": *The Voicebot Podcast* Ep 128, "2019 Year in
Review with Jargon, Voxly and Voicebot," released 2019-12-22 (Apple's `releaseDate` field; the
claim's 2019-12-23 is the publish-page date, same episode). A second query for "Voxly Digital"
alone returns unrelated episodes (e.g., a 2019 VUX World panel featuring *Rozzi Meredith* of
Voxly — a different named individual, not Ravi Lal). No Ravi Lal podcast appearance after 2019
exists in Apple's index.

**Conferences/webinars** — No hit for MAD//Fest, Advertising Week Europe, Cannes Lions, DMEXCO,
Voice Summit/Modev, Alexa Live, or Tech London Advocates. His MassChallenge UK "mentor" listing
and CreativeMornings "individual" profile are standing/attendee-type profiles with no associated
talk or date — not conference appearances. His General Assembly instructor page (fetched live,
2026 copyright footer) lists him teaching "AI-First Product Management," "AI Workplace
Fundamentals," and "Data Analytics and Visualization," but the page is a generic instructor bio
with no scheduled/dated session I could confirm — worth flagging as a soft signal of ongoing
teaching activity, but it does not meet "conference or webinar appearance" and is unconfirmable as
to date. YouTube search for "Ravi Lal Voxly" returns only 4 videos total, verified by oEmbed
title/channel: the known 2017 AAV Virtual Meetup clip, a second clip from the *same* 2017 AAV
event (different speaker, Sam Warnaars), a VUX World panel (different Voxly person, Rozzi
Meredith), and a "Maybelline Tutorial" on Voxly Digital's own channel (product demo, not a Ravi
Lal appearance). Nothing post-2017.

**Bylined trade press** — Zero hits across PRWeek, Creative Review, LBBonline, Adweek, Digiday,
AdExchanger, ExchangeWire, MarTech, or VUX World's own site.

**Regulators/industry bodies** — No independent hit on Portman Group, ASA, ISBA, or IPA. A "DMA
judge" claim surfaced in two separate WebSearch AI-overviews, but both explicitly trace it to his
LinkedIn profile ("According to his LinkedIn profile...") with zero corroboration on dma.org.uk
itself (site: search returned nothing) — this is LinkedIn content, out of scope for this claim and
unverifiable to me regardless.

**Personal site/newsletter** — No Substack, Beehiiv, or Medium presence found.

**"Looking for a mission" / new-direction statement** — None found off LinkedIn/company site. One
WebSearch AI-overview mentioned Ravi "scored eight Shopify brands for AI commerce readiness" in
May and "shut down" that product in June — but the overview itself states this comes from "his
LinkedIn profile," and I could not independently locate the underlying post on any non-LinkedIn
surface. Excluded from consideration per the claim's own scope; not a refutation.

**Settled-category framing holds, with one adjacent 2025 data point** — I found one genuine
third-party (non-LinkedIn, non-Voxly-owned) public statement by Ravi Lal: a quote on Eagle Eye's
own blog (eagleeye.com), dated 2025-07-29, announcing an Eagle Eye/Voxly partnership: "Voice
assistants are no longer an emerging tech. They're now a mainstream part of daily life for many in
the UK." This is neither a podcast, conference/webinar, bylined article, nor newsletter, and it
does not gesture at a new direction — it reinforces the voice-technology framing (adjacent to, not
"Compliance AI/Voxly Vision" specifically, but consistent with "the public material still presents
[the] settled category"). It does not refute the claim; I flag it only because it is the single
closest thing to a qualifying item found anywhere in this pass, and it still falls short on every
count. Crunchbase's own summary (via WebSearch, direct fetch blocked 403) independently states
"there is no recent news or activity for this profile" — corroborating, not refuting.

**Count of surfaces checked, absolute window 2020-01-01 → 2026-09-21**: ~43 distinct
platforms/sites/APIs queried (enumerated above); 0 qualifying podcast appearances, 0 qualifying
conference/webinar appearances, 0 bylined trade-press articles, 0 personal site/newsletter
properties, 0 "new direction" statements found for Ravi Lal in that window outside LinkedIn/
Voxly's own site.

**Caveats on completeness**: Filmot, Google Books API, Medium's own search, and Crunchbase's full
profile all returned blocks (redirect/quota/403) rather than clean negatives; I supplemented each
with a WebSearch pass into the same domain, which also returned nothing, but I cannot claim the
same exhaustiveness for those four as for the iTunes Search API (which is a clean, complete,
directly-queried negative). LinkedIn and X are walled to me entirely, consistent with the claim's
own framing of excluding them.

## source_ids
- S1: https://itunes.apple.com/search?term=Ravi+Lal+Voxly&media=podcast&entity=podcastEpisode — accessed 2026-09-21 — iTunes Search API returns exactly 1 result, Voicebot Podcast Ep 128, releaseDate 2019-12-22T16:51:11Z, description names "Ravi Lal, CEO of Voxly Digital."
- S2: https://itunes.apple.com/search?term=Voxly+Digital&media=podcast&entity=podcastEpisode — accessed 2026-09-21 — 6 results; only other Voxly-related hit is a 2019-12-13 VUX World episode about Rozzi Meredith of Voxly, not Ravi Lal.
- S3: https://www.youtube.com/results?search_query=%22Ravi+Lal%22+Voxly — accessed 2026-09-21 — 4 videoIds returned; verified via oEmbed (S4-S6 below), all pre-2018 or unrelated.
- S4: https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=46iIQRf5Pws — accessed 2026-09-21 — "Live from Mobile UX London: Designing for voice panel," VUX World channel (not Ravi Lal).
- S5: https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ihVGLiCk3Bg — accessed 2026-09-21 — "Sam Warnaars, Open Voice – AAV VIRTUAL MEETUP #2 - Voice Marketing (20/12/17)" — same 2017 event as the known Ravi Lal clip, different speaker.
- S6: https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=M6oK41HePEY — accessed 2026-09-21 — "Maybelline Tutorial," Voxly Digital's own channel (product demo, not a Ravi Lal appearance, and is company-owned content).
- S7: https://www.generalassemb.ly/instructors/ravi-lal/20294 — accessed 2026-09-21 — live instructor bio page (2026 copyright footer), lists "AI-First Product Management," "AI Workplace Fundamentals," "Data Analytics and Visualization" as courses taught; no dated/scheduled session found on the page.
- S8: https://eagleeye.com/blog/eagle-eye-voxly-digital-partnership — accessed 2026-09-21 — third-party (Eagle Eye's own site, not Voxly's, not LinkedIn) blog post dated 2025-07-29, quotes Ravi Lal: "Voice assistants are no longer an emerging tech. They're now a mainstream part of daily life for many in the UK."
- S9: https://www.solacewomensaid.org/news/wavemaker-and-voxly-digital-support-vawg-charity-solace-web-based-chatbot-enables-those-need — accessed 2026-09-21 — 404, could not verify (inconclusive, not counted).
- S10: https://creativemornings.com/individuals/ravilal — accessed 2026-09-21 (direct fetch blank/blocked; content via WebSearch cache) — personal attendee/member profile bio ("Coffee man... Conversational AI"), no talk record found.
- S11: WebSearch "site:dma.org.uk Voxly" — accessed 2026-09-21 — zero relevant results; DMA-judge claim found only via LinkedIn-sourced AI-overview text in other queries, not corroborated on dma.org.uk itself.
- S12: WebSearch queries covering PRWeek, Creative Review, LBBonline, Adweek, Digiday, AdExchanger, ExchangeWire, MarTech, VUX World, Portman Group, ASA, ISBA, IPA, MAD//Fest, Advertising Week Europe, Cannes Lions, DMEXCO, Voice Summit/Modev, Alexa Live, Tech London Advocates, MassChallenge, Texas Exes, Eventbrite/Luma/Meetup, Substack/Beehiiv/Medium, Google Books/Amazon, Crunchbase, PitchBook — accessed 2026-09-21 — no qualifying hits in any.
- S13: https://www.crunchbase.com/person/ravi-lal — accessed 2026-09-21 — direct fetch/curl both returned HTTP 403; WebSearch AI-overview of this page states "there is no recent news or activity for this profile" (corroborates thin surface, not independently verified by me beyond the overview).
