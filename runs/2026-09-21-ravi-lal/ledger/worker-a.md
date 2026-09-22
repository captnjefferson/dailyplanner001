# Worker A — Layer 1 (Identity Resolution) + Layer 7 (Trace Sweep)

Run: 2026-09-21-ravi-lal (PARTNER SCAN, see layer0-frame.md for deviation). Target: Ravi Lal, Voxly Digital, London.
Worker role: COLLECTION ONLY. No strategic claims. All touches: read-only fetches / public API calls. No send, post, comment, connect, subscribe, follow, apply, or join. No contact with the target or anyone else. No authenticated LinkedIn/X session used or attempted — those platforms are SEARCH-ONLY at best per hard rules; browser tools not used (separate serial browser worker owns that lane).
Today: 2026-09-21. All fetches below performed 2026-09-21 (UTC timestamps noted where captured; local capture window 08:57–13:10 EDT).

---

## IDENTITY RESULT UP FRONT

Two-anchor gate **CLEARED**. Legal identity: **Ravinder Singh LAL**, DOB February 1969, nationality American, country of residence England — sole director of **Dolphin Haley Limited** (Companies House #08396885, incorporated 11 Feb 2013), which Voxly's own About Us page states is the legal entity trading as "Voxly." Two independent, distinctive anchors:
1. **Employer** — Voxly Digital, tied to Ravi Lal by name via the company's own site, and tied to the legal person "Ravinder Singh Lal" via Companies House officer records for Dolphin Haley Ltd (the confirmed legal owner of the "Voxly" trading name). [S10, S12, S13]
2. **Origin/nationality** — "from Texas" per Voxly's own team-page bio, independently corroborated by Companies House's own nationality field ("American") on the same officer record. Two independent sources (company's own site + UK government filing) agree. [S3, S12]

This clears the gate; Layer 1–7 collection below proceeds on that identity. Run does NOT end IDENTITY-UNRESOLVED.

---

## LAYER 1 — IDENTITY RESOLUTION (6 rows)

### 1.1 Published or self-owned email search
```yaml
- step: "1.1 email search"
  status: RAN-FOUND
  checked_count: 2
  checked_unit: emails
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S0, S37]
  note: >
    ravi.lal@voxlydigital.com already established VERIFIED-PRIMARY per Layer 0 frame
    (S0: Google Calendar invite for "AI Jam," organizer patrick@patchbaymedia.com,
    Ravi as invitee — self-owned employer-domain address). Voxly's own Contact Us
    page (S37, fetched directly) additionally publishes freshthinking@voxlydigital.com,
    a general company inbox, not a personal address — confirms domain but adds no
    new personal-email evidence. No personal (non-employer) self-owned email or
    domain found anywhere in this run (see 10. personal site, below — none).
```

### 1.2 Bounded Maigret handle sweep
Variants generated (exactly the 6 specified, no bare given-name run): `ravilal`, `ravi.lal`, `rlal`, `ravil`, `lalravi`, `ravi_lal`. Command run per Ops §A2, one invocation, all 6 usernames, `--no-recursion --no-extracting --top-sites 500 --timeout 15 --folderoutput <run_dir>/maigret/`.

Raw claimed-account counts per variant (NOT identity-verified — raw hits only):
| variant | claimed accounts | bot-protection error rate |
|---|---|---|
| ravilal | 70 | 6.88% |
| ravi.lal | 18 | 6.48% (+ 10.22% "unsupported username format" — periods break many site regexes) |
| rlal | 85 | 6.68% |
| ravil | 204 | 6.68% |
| lalravi | 21 | 6.68% |
| ravi_lal | 14 | 6.88% |

Coverage: ~93–94% of attempted checks per variant returned a clean found/not-found signal; the remainder hit bot protection (Cloudflare-class walls), consistent across all 6 variants — this is a platform-side saturation floor, not a run defect. Countries/interest tags returned span dozens of unrelated verticals (gaming, dating, crypto, Russian-language forums), confirming most raw hits are noise from short/common substrings (`ravil` is a common Russian given name; `rlal`/`ravi_lal` are generic 4–7 character strings).

Single highest-value signal: **`lalravi` claimed on LinkedIn** (`linkedin.com/in/lalravi`) — matches the actual "Ravi Lal – Voxly Digital" LinkedIn profile independently found via web search (S1), confirming his real handle pattern is surname+firstname concatenation. Per hard rules this remains SEARCH-ONLY (no authenticated session), but the handle-pattern match is useful for downstream browser-worker verification.

Every platform-specific hit that could be cheaply checked (GitHub, Bluesky, Substack, Medium, Instagram, Facebook, TikTok, Threads) was individually run through the two-anchor gate — see Layer 7 rows 1–9 below; nearly all resolved to **other people** or unconfirmable empty shells.

```yaml
- step: "1.2 Maigret handle sweep"
  status: RAN-FOUND
  checked_count: 6
  checked_unit: handles
  evidence_quality: SEARCH-ONLY
  source_ids: [S47]
  note: >
    6 variants, ~500-site cap each, 70/18/85/204/21/14 raw claims respectively;
    bot-protection saturation 6.48-6.88% uniformly (plus a 10.22% "unsupported
    username format" spike on ravi.lal from the period character). Zero accounts
    carried extractable bio/identity data (--no-extracting by design); every
    claim required manual anchor-checking, done in Layer 7. Only "lalravi" on
    LinkedIn corroborates a real, independently-found profile (still SEARCH-ONLY
    per the LinkedIn/X precedence rule).
```

### 1.3 Quoted distinctive-bio search
Searched his standing origin-story phrases verbatim/near-verbatim: "led the London expansion of Impossible Labs," "created Better Than One," "Head of Operations at Tech City," and the newer "from Texas... long career in Big Telco." Also searched named prior employers (Opearlo, France Telecom, Telefónica/O2).

Finding: the Impossible Labs / Better Than One / Tech City trio recurs **only** within his own controlled/self-published surfaces (General Assembly instructor bio, Crunchbase-style aggregator summaries that appear to mirror it) — it did **not** turn up pasted verbatim on a third-party site the way the process expects for a widely-reused bio line. That absence is itself informative: he is not syndicating one canonical bio blurb across guest posts/press. The current company bio ("from Texas... Big Telco") is a completely different, shorter self-description that appears only on voxlydigital.com/team — see 1.6 for the drift analysis.

```yaml
- step: "1.3 quoted distinctive-bio search"
  status: RAN-FOUND
  checked_count: 10
  checked_unit: queries
  evidence_quality: SEARCH-ONLY
  source_ids: [S1, S2, S3, S10, S21, S22, S23, S24]
  note: >
    No independent third-party reuse of his bio phrasing found outside his own
    controlled platforms (GA, CreativeMornings, Voxly's own site) and aggregator
    mirrors of the same. Treated as a confirmed narrow-reuse finding, not a gap.
```

### 1.4 Show-notes and speaker-bio bridge
```yaml
- step: "1.4 show-notes/speaker-bio bridge"
  status: RAN-FOUND
  checked_count: 3
  checked_unit: appearances
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S26, S20, S27]
  note: >
    CONFIRMED via direct fetch: Voicebot.ai Podcast Ep 128, "2019 Voice Year in
    Review with Jargon, Voxly, and Voicebot" (2019-12-23) — Ravi Lal named guest,
    "CEO of Voxly Digital," alongside Milkana Brace (CEO, Jargon) and Eric
    Schwartz (Voicebot.ai), hosted by Bret Kinsella [S26]. CONFIRMED via YouTube
    title fetch: "Ravi Lal, Voxly Digital - AAV Virtual Meetup #2 - Voice
    Marketing" (2017-12-20) [S20]. No podcast RSS feed found under his own name
    (he appears as guest, not host) so no itunes:email contact field to mine.
    REJECTED: a UC Expo London appearance ("The Hidden UX of Voice...") surfaced
    ONLY via an AI-generated search summary with zero corroborating primary
    source (no UC Expo agenda/speaker page found under his name) [S27] — flagged
    per the standing warning that AI search summaries invent conference
    appearances; moved to the UNVERIFIED block, not counted as a finding.
```

### 1.5 Separate work-only account sweep
```yaml
- step: "1.5 work-only account sweep"
  status: RAN-FOUND
  checked_count: 5
  checked_unit: platforms
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S3, S10, S37, S42, S17]
  note: >
    Work identity fully mapped to Voxly's own branded channels: Instagram
    @voxlydigital (confirmed real via direct fetch, 145 followers/41
    following/57 posts) [S42], the company blog (voxlydigital.com/post/*, e.g.
    the Diageo/Seedlip "Elli" generative-AI concierge launch post), the Contact
    Us page [S37], and the team/about pages [S3, S10]. No separate personal
    creator identity confirmed: the one Substack candidate under his handle
    pattern ("ravilal") is a gardening-topic reader profile with no anchors
    tying it to Voxly/London/AI [S17] — does not qualify as a confirmed
    separate creator account (see Layer 7.7).
```

### 1.6 Bio-drift comparison
```yaml
- step: "1.6 bio-drift comparison"
  status: RAN-FOUND
  checked_count: 3
  checked_unit: bios
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S2, S3, S10, S48]
  note: >
    Clean, confirmed drift. (a) General Assembly instructor bio [S2, undated,
    but scoped to pre-2019 roles]: "Ravi Lal is the founder and CEO of Voxly
    Digital. Our mission is to build the worlds best voice experiences. We
    offer Voice Design, get your content Voice-ready, and are experts in Voice
    Analytics. Prior to that, he led the London expansion of Impossible Labs,
    created Better Than One, and was Head of Operations at Tech City." (b)
    Current Voxly team-page bio [S3, fetched live 2026-09-21]: "Ravi is from
    Texas and founded the company after a long career in Big Telco" — zero
    mention of Alexa, voice, Impossible Labs, Better Than One, or Tech City.
    (c) Current About Us page [S10, fetched live]: repositions the whole
    company as "Agentic AI systems... Compliance AI," again with zero voice/
    Alexa framing despite that being the entire product line as recently as
    the 2019 podcast and a 2024 Drum Award for a Royal Navy conversational-AI
    chatbot. Wayback CDX [S48] confirms voxlydigital.com/team was re-published
    at least 8 times between 2019-07-20 and 2026-03-14 — an actively evolving
    self-presentation. GAP: attempted to pull literal text from an intermediate
    (2019/2020/2022) Wayback snapshot to pinpoint the drift date; the archived
    page is a JS-rendered Wix site and a plain-text fetch returned no visible
    bio content [S49] — the drift is dated only to the bound "sometime between
    2019-07-20 and 2026-09-21," not pinpointed.
```

**Layer 1 output summary:** Identity resolved (see box above). Emails: 1 verified-primary personal-pattern address (S0) + 1 general company inbox (S37). Bio drift: confirmed, voice/Alexa-agency framing → Big-Telco/Agentic-AI-compliance framing, exact pivot date not pinpointed. No IDENTITY-UNRESOLVED condition.

---

## LAYER 7 — TRACE SWEEP (14 surfaces, 1 row each)

```yaml
- step: "7.1 X"
  status: SOFT-NOT-FOUND
  checked_count: 1
  checked_unit: handles
  evidence_quality: SEARCH-ONLY
  source_ids: [S28]
  note: >
    Only candidate found, @raviglal ("Ravi Lal" per X's server-rendered title
    tag), is a CONFIRMED NAME COLLISION, not the target: a secondary source
    (Frances Arnold's own tweet, quoted in search results) identifies
    @raviglal as a protein/enzyme engineer collaborating with her Caltech lab
    on directed-evolution research — contradicts every target anchor (field,
    employer, geography). No other X candidate surfaced. X requires
    authenticated verification per hard rules regardless; capped SOFT-NOT-FOUND.
    Do not use @raviglal as a touch surface under any circumstance.
```

```yaml
- step: "7.2 Bluesky"
  status: RAN-NULL
  checked_count: 7
  checked_unit: handles
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S15, S16]
  note: >
    "Checked 7 Bluesky handle variants (ravil, rlal, ravilal, ravi-lal,
    ravinderlal, voxlydigital, voxly) via the public unauthenticated API on
    2026-09-21; none present under a distinguishable account for this target."
    ravil.bsky.social = a different "Ravil" (7 follows, 2 posts, no bio).
    rlal.bsky.social = anonymous (no display name/bio, 23 followers/64
    follows/0 posts) — unconfirmable either way. voxlydigital/voxly/
    ravilal/ravi-lal/ravinderlal = profile not found / invalid identifier.
```

```yaml
- step: "7.3 Instagram"
  status: FOUND
  checked_count: 2
  checked_unit: accounts
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S42, S43]
  note: >
    Org account @voxlydigital CONFIRMED via direct fetch (title tag "Voxly
    Digital (@voxlydigital)"; 145 followers/41 following/57 posts) [S42] — this
    is a real, active organizational presence. Candidate personal account
    @ravishlal: title tag confirms display name "Ravi Lal" (134 followers/110
    following/372 posts) [S43], but Instagram's public meta tags expose no
    bio/location/employer text to an unauthenticated fetch, so the second
    anchor cannot be cleared — filed UNVERIFIED lead, NOT accepted as the
    target's personal account (see UNVERIFIED block).
```

```yaml
- step: "7.4 Threads"
  status: BLOCKED-WALLED
  checked_count: 2
  checked_unit: handles
  evidence_quality: UNVERIFIED
  source_ids: [S32]
  note: >
    Both @voxlydigital and @ravilal redirect identically to threads.com/login
    — a full login wall applied uniformly to org and candidate-personal handles
    alike (control-equivalent: the wall does not distinguish real accounts from
    nonexistent ones). Named wall: Threads login gate.
```

```yaml
- step: "7.5 TikTok"
  status: BLOCKED-WALLED
  checked_count: 6
  checked_unit: handles
  evidence_quality: UNVERIFIED
  source_ids: [S45, S46]
  note: >
    @ravilal, @ravi.lal, @ravi_lal, @rlal, @voxlydigital all fetched but
    returned an identical un-rendered generic shell ("TikTok - Make Your Day")
    — the SAME shell returned by the control fetch of the verified-real
    official @tiktok account [S46]. TikTok's HTML requires JS execution to
    render distinguishing content; plain fetch cannot tell a real profile from
    a nonexistent one here. Maigret's "Claimed" status for these handles is an
    HTTP-status-only check and does not confirm identity — not corroborated.
```

```yaml
- step: "7.6 Facebook"
  status: NOT-DISTINGUISHABLE
  checked_count: 2
  checked_unit: pages
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S30, S1]
  note: >
    facebook.com/lalravi redirects to facebook.com/lal.ravi, titled "Tunahan
    Sezer (@lal.ravi)" — CONFIRMED WRONG PERSON (unrelated Turkish name; total
    anchor contradiction) [S30]. facebook.com/voxlydigital exists per search
    results (org page, London-located) [S1] but was not independently
    content-fetched (Facebook walls non-friend content beyond the title shell)
    — filed SEARCH-ONLY, not independently verified. No confirmed personal
    Facebook account for the target.
```

```yaml
- step: "7.7 Substack"
  status: NOT-DISTINGUISHABLE
  checked_count: 6
  checked_unit: handles
  evidence_quality: UNVERIFIED
  source_ids: [S17, S18]
  note: >
    Per Ops §A3, none of these candidates originate from an authorized source
    (no bio-link or handle-reuse pointing to a Substack account) — strictly
    this step is NOT-APPLICABLE with zero authorized candidates; run anyway as
    a bounded check against the Maigret-derived handle list, reported as leads
    only. "ravilal": real name match ("Ravi Lal," id 26703879, profile since
    2023-03-30) but bio empty and both visible subscriptions are UK gardening
    newsletters (Mike the Gardener; Wild Way habitat gardening) — thematically
    inconsistent with a London voice/AI agency founder; one weak anchor (name)
    only, does not clear the gate. "rlal" = Austin Daniels (finance content,
    different person). "ravil" = Ravil Suleymanov (different person). "ravi.lal",
    "lalravi", "ravi_lal" = profile not found.
```

```yaml
- step: "7.8 Medium"
  status: BLOCKED-WALLED
  checked_count: 6
  checked_unit: handles
  evidence_quality: UNVERIFIED
  source_ids: [S36]
  note: >
    @ravilal, @ravi.lal, @ravil, @rlal all returned HTTP 403. Control check
    against known-good accounts (@medium, @ev) ALSO returned HTTP 403 —
    confirms Medium is platform-wide bot-blocked to plain fetchers, per the
    fast-check rule this is BLOCKED-WALLED, never a null.
```

```yaml
- step: "7.9 GitHub"
  status: RAN-NULL
  checked_count: 6
  checked_unit: handles
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S14]
  note: >
    "Checked 6 GitHub handle variants via the public API on 2026-09-21; none
    present under a distinguishable account for this target." ravilal = empty
    shell (0 repos, 0 followers, created 2015-04-01). rlal = near-empty (2
    repos, 0 followers, created 2016-05-24). ravil = Ravil Gatin, location
    "Leningrad, USSR" — different person. lalravi = empty shell (created
    2018-04-15). ravi.lal / ravi_lal = do not exist. No bio/company/location
    field on any account matches Voxly/London/Texas.
```

```yaml
- step: "7.10 personal site"
  status: RAN-NULL
  checked_count: 13
  checked_unit: subdomains/domains
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S35, S50]
  note: >
    "Checked ravilal.com domain search plus certificate-transparency records
    for all voxlydigital.com subdomains on 2026-09-21; none present." No
    personal domain indexed under his name [S50]. crt.sh certificate-
    transparency sweep of *.voxlydigital.com returned only standard cPanel/
    shared-hosting subdomains (mail, webmail, cpanel, cpcontacts, cpcalendars,
    webdisk, autodiscover, status, accounts.status, clerk.status) — no
    separate personal or dev/blog subdomain [S35].
```

```yaml
- step: "7.11 podcasts"
  status: FOUND
  checked_count: 1
  checked_unit: appearances
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S26]
  note: >
    Voicebot.ai Podcast Ep 128, "2019 Voice Year in Review with Jargon, Voxly,
    and Voicebot" (2019-12-23) — Ravi Lal named guest as "CEO of Voxly
    Digital," confirmed via direct fetch of the show-notes article, verbatim
    quote captured. No podcast appearances found in the 2020-2026 window
    despite targeted search; he appears to guest rarely and not recently.
```

```yaml
- step: "7.12 YouTube"
  status: FOUND
  checked_count: 4
  checked_unit: channels/videos
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S20, S33, S34]
  note: >
    FOUND: "Ravi Lal, Voxly Digital - AAV Virtual Meetup #2 - Voice Marketing"
    (2017-12-20), hosted on a third-party channel, title-confirmed via direct
    fetch [S20]. RAN-NULL for a dedicated channel: youtube.com/@voxly is NOT
    Voxly Digital — direct fetch confirms it is "voxly.pl," a Polish channel
    ("Oficjalny kanał voxly.pl") [S33]; youtube.com/@voxlydigital returns 404;
    a general channel search for "voxly digital" surfaced no dedicated org or
    personal channel among results [S34]. Corrects a wrong-org inference an AI
    search summary had suggested.
```

```yaml
- step: "7.13 conference and webinar archives"
  status: FOUND
  checked_count: 2
  checked_unit: appearances
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S20, S27]
  note: >
    The 2017 AAV Virtual Meetup talk (also counted under 7.12) is itself an
    archived webinar recording — counts here too. One additional candidate,
    "UC Expo London — The Hidden UX of Voice," was checked and REJECTED: it
    surfaced only via an AI-generated search summary; no UC Expo agenda,
    speaker page, or any primary source confirms it under his name [S27].
    Per the standing warning that AI search summaries invent conference
    appearances, this is excluded from findings entirely (see UNVERIFIED
    block) rather than filed even as a soft lead.
```

```yaml
- step: "7.14 trade-press bylines"
  status: RAN-NULL
  checked_count: 4
  checked_unit: articles/outlets
  evidence_quality: VERIFIED-PRIMARY
  source_ids: [S38, S25, S40]
  note: >
    Checked The Drum, Campaign Live, Marketing Week, Voicebot.ai, and
    ExchangeWire. The Drum (2024): Voxly Digital credited (not Ravi Lal
    personally) as Bronze winner, Drum Awards for Media 2024, for the Royal
    Navy campaign [S40, search-snippet, not independently fetched in full].
    Campaign Live (2019): quotes Nimesh Patel, "programme manager" at Voxly
    Digital, on voice commerce — NOT Ravi Lal [S40]. Voicebot.ai's own
    "Voxly Digital" tag archive has exactly 2 articles, neither with a direct
    Ravi Lal quote or byline [S25, direct fetch]. ExchangeWire's April 2026
    "Agentic AI... Ad Tech" piece — directly on-topic for Voxly's current
    positioning — was fetched directly and CONFIRMED to contain zero mention
    of Ravi Lal or Voxly Digital [S38, direct fetch, genuine verified null].
    No standalone bylined article authored by Ravi Lal found on any trade
    outlet in this sweep.
```

**Layer 7 output summary:** FOUND on 4/14 surfaces (Instagram [org], podcasts, YouTube, conference/webinar archives). RAN-NULL on 4/14 (Bluesky, GitHub, personal site, trade-press bylines). BLOCKED-WALLED on 3/14 (Threads, TikTok, Medium — all confirmed via control-test symmetry, not target-specific absence). NOT-DISTINGUISHABLE on 2/14 (Facebook, Substack — best candidates are either a confirmed wrong person or a single weak anchor). SOFT-NOT-FOUND on 1/14 (X — capped by the authenticated-only rule; the one candidate found is a confirmed wrong person). Zero NOT-RUN rows.

---

## SOURCE REGISTRY

```yaml
sources:
  S0: {url_or_tool_call: "Google Calendar invite 'AI Jam', ~/Downloads/20260918_aijam.rtf (Riverside transcript)", type: primary, accessed_at: "2026-09-18 (pre-existing, cited by orchestrator)", target_anchors: ["email", "employer", "self-reported bio"]}
  S1: {url_or_tool_call: "WebSearch: \"Ravi Lal\" \"Voxly Digital\"", type: search-snippet, accessed_at: "2026-09-21T13:01Z", target_anchors: ["employer", "city"]}
  S2: {url_or_tool_call: "WebFetch https://www.generalassemb.ly/instructors/ravi-lal/20294", type: secondary, accessed_at: "2026-09-21T13:02Z", target_anchors: ["employer", "prior employer", "title", "city"]}
  S3: {url_or_tool_call: "WebFetch https://www.voxlydigital.com/team", type: primary, accessed_at: "2026-09-21T13:02Z", target_anchors: ["employer", "city origin"]}
  S4: {url_or_tool_call: "WebFetch https://find-and-update.company-information.service.gov.uk/officers/0ufaLvA30m-ctt0_fK0LJFDSSN8/appointments", type: primary, accessed_at: "2026-09-21T13:03Z", target_anchors: ["name-collision check only — DOB Aug 1978, DIFFERENT person from confirmed target"]}
  S5: {url_or_tool_call: "WebFetch Companies House company search q=voxly+digital", type: primary, accessed_at: "2026-09-21T13:03Z", target_anchors: []}
  S6: {url_or_tool_call: "WebFetch Companies House officer search q=Ravi+Lal", type: primary, accessed_at: "2026-09-21T13:03Z", target_anchors: ["name-collision landscape — 6 distinct Ravi Lals found"]}
  S7: {url_or_tool_call: "curl https://creativemornings.com/individuals/ravilal", type: primary, accessed_at: "2026-09-21T13:05Z", target_anchors: ["city (London chapter)"]}
  S8: {url_or_tool_call: "WebFetch Companies House VOXLY LTD (12027947) officers", type: primary, accessed_at: "2026-09-21T13:07Z", target_anchors: ["ruled out — wrong company (childcare/education SIC, different officers)"]}
  S9: {url_or_tool_call: "WebFetch Companies House VOXLY LTD (12027947) profile", type: primary, accessed_at: "2026-09-21T13:07Z", target_anchors: []}
  S10: {url_or_tool_call: "WebFetch https://www.voxlydigital.com/about-us", type: primary, accessed_at: "2026-09-21T13:07Z", target_anchors: ["employer (legal trading-name owner: Dolphin Haley LTD)", "city"]}
  S11: {url_or_tool_call: "WebFetch Companies House company search q=dolphin+haley", type: primary, accessed_at: "2026-09-21T13:08Z", target_anchors: []}
  S12: {url_or_tool_call: "WebFetch https://find-and-update.company-information.service.gov.uk/company/08396885/officers", type: primary, accessed_at: "2026-09-21T13:09Z", target_anchors: ["employer", "nationality/origin", "legal name", "DOB"]}
  S13: {url_or_tool_call: "WebFetch https://find-and-update.company-information.service.gov.uk/company/08396885", type: primary, accessed_at: "2026-09-21T13:09Z", target_anchors: []}
  S14: {url_or_tool_call: "curl https://api.github.com/users/{ravilal,ravi.lal,rlal,ravil,lalravi,ravi_lal}", type: primary, accessed_at: "2026-09-21T13:12Z", target_anchors: []}
  S15: {url_or_tool_call: "curl https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=ravil.bsky.social", type: primary, accessed_at: "2026-09-21T13:12Z", target_anchors: []}
  S16: {url_or_tool_call: "curl https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=rlal.bsky.social", type: primary, accessed_at: "2026-09-21T13:12Z", target_anchors: []}
  S17: {url_or_tool_call: "curl https://substack.com/api/v1/user/ravilal/public_profile", type: primary, accessed_at: "2026-09-21T13:13Z", target_anchors: ["name only — one weak anchor"]}
  S18: {url_or_tool_call: "curl https://substack.com/api/v1/user/{ravi.lal,rlal,ravil,lalravi,ravi_lal}/public_profile", type: primary, accessed_at: "2026-09-21T13:13Z", target_anchors: []}
  S19: {url_or_tool_call: "WebFetch Companies House officer search q=Ravinder+Singh+Lal", type: primary, accessed_at: "2026-09-21T13:14Z", target_anchors: ["confirms single unique match, 1 appointment total"]}
  S20: {url_or_tool_call: "WebFetch https://www.youtube.com/watch?v=JY8mMlwTl9w", type: secondary, accessed_at: "2026-09-21T13:15Z", target_anchors: ["employer", "topic/title"]}
  S21: {url_or_tool_call: "WebSearch: \"Ravi Lal\" \"Opearlo\"", type: search-snippet, accessed_at: "2026-09-21T13:16Z", target_anchors: ["prior employer (self-reported)"]}
  S22: {url_or_tool_call: "WebSearch: \"Ravi Lal\" \"Impossible Labs\"", type: search-snippet, accessed_at: "2026-09-21T13:16Z", target_anchors: ["prior employer (self-reported)"]}
  S23: {url_or_tool_call: "WebSearch: \"Ravi Lal\" \"Tech City\" OR \"Tech Nation\"", type: search-snippet, accessed_at: "2026-09-21T13:16Z", target_anchors: ["prior employer (self-reported)"]}
  S24: {url_or_tool_call: "WebSearch: \"Ravi Lal\" Telefonica", type: search-snippet, accessed_at: "2026-09-21T13:00Z", target_anchors: ["prior employer (AI-summarized, UNVERIFIED)"]}
  S25: {url_or_tool_call: "WebFetch https://voicebot.ai/tag/voxly-digital/", type: secondary, accessed_at: "2026-09-21T13:20Z", target_anchors: []}
  S26: {url_or_tool_call: "WebFetch https://voicebot.ai/2019/12/23/2019-voice-year-in-review-with-jargon-voxly-and-voicebot-voicebot-podcast-ep-128/", type: secondary, accessed_at: "2026-09-21T13:24Z", target_anchors: ["employer", "exact title"]}
  S27: {url_or_tool_call: "WebSearch: \"UC Expo\" \"Ravi Lal\" OR \"Voxly\" speaker agenda", type: search-snippet, accessed_at: "2026-09-21T13:18Z", target_anchors: ["UNCONFIRMABLE — no primary source found, rejected"]}
  S28: {url_or_tool_call: "curl https://x.com/raviglal ; WebSearch \"@raviglal\"", type: search-snippet, accessed_at: "2026-09-21T13:27Z", target_anchors: ["REFUTED — confirmed different person (Caltech protein engineer)"]}
  S29: {url_or_tool_call: "curl https://x.com/jack (control test)", type: primary, accessed_at: "2026-09-21T13:27Z", target_anchors: []}
  S30: {url_or_tool_call: "curl -L https://www.facebook.com/lalravi", type: primary, accessed_at: "2026-09-21T13:28Z", target_anchors: ["REFUTED — confirmed different person (Tunahan Sezer)"]}
  S31: {url_or_tool_call: "curl -L https://www.facebook.com/zuck (control test)", type: primary, accessed_at: "2026-09-21T13:28Z", target_anchors: []}
  S32: {url_or_tool_call: "curl -L https://www.threads.com/@voxlydigital ; https://www.threads.net/@ravilal", type: primary, accessed_at: "2026-09-21T13:28Z", target_anchors: []}
  S33: {url_or_tool_call: "curl https://www.youtube.com/@voxly/about", type: primary, accessed_at: "2026-09-21T13:29Z", target_anchors: ["ruled out — different org (voxly.pl)"]}
  S34: {url_or_tool_call: "curl https://www.youtube.com/results?search_query=voxly+digital", type: primary, accessed_at: "2026-09-21T13:29Z", target_anchors: []}
  S35: {url_or_tool_call: "curl https://crt.sh/?q=%25.voxlydigital.com&output=json", type: primary, accessed_at: "2026-09-21T13:19Z", target_anchors: []}
  S36: {url_or_tool_call: "curl https://medium.com/@{ravilal,ravi.lal,ravil,rlal} + control @medium, @ev", type: primary, accessed_at: "2026-09-21T13:19Z", target_anchors: []}
  S37: {url_or_tool_call: "curl https://www.voxlydigital.com/contactus", type: primary, accessed_at: "2026-09-21T13:06Z", target_anchors: ["employer (general inbox)"]}
  S38: {url_or_tool_call: "WebFetch https://www.exchangewire.com/blog/2026/04/02/agentic-ai-quality-and-courtroom-battles-whats-rewriting-the-rules-of-ad-tech-in-2026/", type: secondary, accessed_at: "2026-09-21T13:23Z", target_anchors: []}
  S39: {url_or_tool_call: "WebSearch: \"Ravi Lal\" Voxly Diageo interview OR quoted", type: search-snippet, accessed_at: "2026-09-21T13:25Z", target_anchors: []}
  S40: {url_or_tool_call: "WebSearch: \"Voxly Digital\" site:thedrum.com OR site:marketingweek.com OR site:campaignlive.co.uk OR site:voicebot.ai", type: search-snippet, accessed_at: "2026-09-21T13:17Z", target_anchors: []}
  S41: {url_or_tool_call: "WebSearch: \"Ravi Lal\" London run club OR running \"Texas Exes\"", type: search-snippet, accessed_at: "2026-09-21T13:09Z", target_anchors: ["self-reported claim, uncorroborated"]}
  S42: {url_or_tool_call: "curl https://www.instagram.com/voxlydigital/", type: primary, accessed_at: "2026-09-21T13:31Z", target_anchors: ["employer (org account)"]}
  S43: {url_or_tool_call: "curl https://www.instagram.com/ravishlal/", type: primary, accessed_at: "2026-09-21T13:31Z", target_anchors: ["name only — one weak anchor"]}
  S44: {url_or_tool_call: "curl https://www.instagram.com/instagram/ (control test)", type: primary, accessed_at: "2026-09-21T13:31Z", target_anchors: []}
  S45: {url_or_tool_call: "curl https://www.tiktok.com/@{ravilal,voxlydigital}", type: primary, accessed_at: "2026-09-21T13:32Z", target_anchors: []}
  S46: {url_or_tool_call: "curl https://www.tiktok.com/@tiktok (control test)", type: primary, accessed_at: "2026-09-21T13:32Z", target_anchors: []}
  S47: {url_or_tool_call: "~/Sites/hm-outreach/tools/venv-maigret/bin/maigret ravilal ravi.lal rlal ravil lalravi ravi_lal --json simple --no-progressbar --no-recursion --no-extracting --top-sites 500 --timeout 15 --folderoutput <run_dir>/maigret/", type: primary, accessed_at: "2026-09-21T08:57-09:00 EDT", target_anchors: []}
  S48: {url_or_tool_call: "curl http://web.archive.org/cdx/search/cdx?url=voxlydigital.com/team&output=json", type: primary, accessed_at: "2026-09-21T13:35Z", target_anchors: []}
  S49: {url_or_tool_call: "curl https://web.archive.org/web/20190720082419if_/https://www.voxlydigital.com/team", type: primary, accessed_at: "2026-09-21T13:36Z", target_anchors: ["attempted, inconclusive — JS-rendered page, no text extracted"]}
  S50: {url_or_tool_call: "WebSearch: \"Ravi Lal\" personal website OR blog ravilal.com", type: search-snippet, accessed_at: "2026-09-21T13:30Z", target_anchors: []}
  S51: {url_or_tool_call: "WebSearch: \"by Ravi Lal\" Voxly OR voice OR agentic article contributor", type: search-snippet, accessed_at: "2026-09-21T13:37Z", target_anchors: []}
```

---

## UNVERIFIED BLOCK

Everything below did **not** clear the two-anchor gate, or is a claim resting only on an AI-generated search summary without primary confirmation. None of this may support an opening, a touch, or an Attio fact.

1. **@raviglal (X)** — REFUTED as the target. Display name matches ("Ravi Lal") but independent corroboration (a Frances Arnold tweet, via search) identifies this account as a protein/enzyme engineer collaborating on directed-evolution research at Caltech — contradicts employer, field, and geography. [S28]
2. **facebook.com/lal.ravi** — REFUTED as the target. Confirmed via direct title fetch to belong to "Tunahan Sezer," an unrelated person. [S30]
3. **Substack "ravilal"** (substack.com/@ravilal) — UNVERIFIED lead. Exact name match ("Ravi Lal") but empty bio and both visible subscriptions are UK gardening newsletters — thematically inconsistent with the target's known profile. One weak anchor (name) only. [S17]
4. **Instagram @ravishlal** — UNVERIFIED lead. Display name "Ravi Lal" confirmed via title tag, but no bio/employer/location text retrievable from an unauthenticated fetch. One weak anchor (name) only. [S43]
5. **GitHub ravilal / lalravi** — UNVERIFIED. Accounts exist (created 2015 and 2018 respectively) but are empty shells with zero bio/company/location content — cannot be attributed to the target or ruled out. [S14]
6. **Bluesky rlal.bsky.social** — UNVERIFIED. Anonymous account (no display name, no bio); cannot be confirmed or ruled out. [S16]
7. **Ravi LAL, DOB Aug 1978, RA GLOBAL LTD (Companies House)** — REFUTED as the target. Different DOB than the confirmed Ravinder Singh Lal (Feb 1969); a name-collision candidate that surfaced accidentally in an unrelated search and should not be used. [S4]
8. **Prior-employer detail: "Head of Messaging Services and Operations at O2 (Telefónica UK), 2009"** — UNVERIFIED. Surfaced only via an AI-generated WebSearch summary paragraph, not traced to any specific primary or self-published document. The frame's own S0-sourced prior-employer list ("France Telecom, Telefónica") is his own spoken claim in the AI Jam transcript and stands on that basis alone; this more specific O2/2009 detail is an independent, uncorroborated elaboration and should be treated with extra caution. [S24]
9. **Prior employers Opearlo / Impossible Labs / Better Than One / Tech City (Tech Nation)** — self-reported only (his own General Assembly instructor bio, a self-published but third-party-hosted source), not independently corroborated by any unrelated document; Companies House shows him with exactly one UK directorship ever (Dolphin Haley Ltd), so none of these were companies he formally directed — consistent with employee-level roles, which would not appear in Companies House regardless of whether the claim is true. Filed as sourced-to-him, not independently verified. [S2, S12, S19]
10. **UC Expo London appearance ("The Hidden UX of Voice")** — REJECTED, not even filed as a lead. Surfaced only via an AI-generated search summary; no UC Expo agenda, speaker roster, or any other primary source names him. Per the standing rule that AI search summaries invent conference appearances, this claim is excluded from the report entirely rather than softened. [S27]
11. **Texas Exes / London run club membership** — self-reported only (his own statement in the AI Jam transcript, S0); targeted search for independent corroboration returned nothing connecting him by name to the UK Texas Exes chapter or its Stampede Running Club. RAN-NULL on the corroboration search, not a confirmed membership beyond his own claim. [S41]
12. **UT Austin affiliation** — per the run frame, already flagged LEAD ONLY (member of Texas Exes London is not itself proof of a UT Austin degree; Indiana University is the confirmed MBA anchor per his GA bio and Voxly's own descriptions). This worker found no additional evidence either way and did not upgrade or downgrade this flag.
13. **facebook.com/voxlydigital (org page)** — existence only, via search snippet; not independently content-fetched. SEARCH-ONLY, not VERIFIED. [S1]
14. **Drum Awards 2024 / Campaign Live 2019 Voxly mentions** — existence of the articles confirmed only via search snippet, not independently fetched in full; treat citations as SEARCH-ONLY pending a direct fetch. [S40]

---

## Coverage bounds and gaps (for the orchestrator's Gaps section)

- LinkedIn and X: no authenticated session used or available to this worker (by design — separate serial browser worker owns that lane); every LinkedIn/X data point above is SEARCH-ONLY at best, per hard rules.
- Threads, TikTok, Medium: platform-level walls confirmed via control-account testing (not target-specific).
- Facebook, Instagram (personal): confirmed WALLED beyond title-tag/meta-description level; cannot retrieve bio/anchor text without authentication.
- Wayback: attempted to pin the exact bio-drift transition date via an intermediate snapshot; the archived page is JS-rendered and yielded no extractable text via plain fetch — the drift is bounded (2019-07-20 to 2026-09-21) but not dated precisely.
- Substack, GitHub, Bluesky checks in this worker's scope were run against Maigret-derived handle guesses rather than an authorized bio-link/handle-reuse source per Ops §A3's strict reading — flagged inline at each relevant row; results are reported as leads/nulls, not elevated beyond what the evidence supports.
- No podcast RSS feed under the target's own name was found (he guests, does not host), so the itunes:email contact-field technique in the process doc had no feed to apply to.
