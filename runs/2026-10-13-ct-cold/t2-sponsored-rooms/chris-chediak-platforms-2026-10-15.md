# Chris Chediak — platform pass (public pages, logged out, 2026-10-15)

Method and limits: every page below was fetched logged out with curl and a desktop user agent (plus YouTube RSS, X's public oEmbed and embed endpoints, the Apple Podcasts lookup API, the DailyMotion and Bluesky public APIs, WebSearch); no browser, no login, no form, no LinkedIn page opened; the lead's Maigret reports (`maigret/`, 2026-10-15) were used only as pointers and every hit flagged for triage was opened here. Limits found today: Instagram, Threads and Facebook return the identical logged-out shell for every handle, including known-existing controls (`instagram.com/instagram/`, `threads.com/@instagram`, `facebook.com/facebook`), so those three can only be recorded WALL, never NOT FOUND; X's embed endpoint answered HTTP 429 on five spaced attempts, so X accounts could be tested for existence and for whether a timeline exists, but no name, bio or post could be read; Reddit answered 403; Medium profile pages answered 403 (Cloudflare) but Medium RSS feeds are readable; WebSearch declined name+social-platform queries for a private person and DuckDuckGo's HTML endpoint returned a bot challenge (202). Candidate avatars were compared by eye with the firm bio photo (https://www.weintraub.com/wp-content/uploads/storage/images/fit-800x900-noupscale-95-Chediak_Chris_800x900_v2.png). "Chediak" is a widely shared family name (Brazil, Argentina, Uruguay, U.S.), so the bare handle `chediak` belongs to other people on every platform where it could be read. Janet Z. Chediak (Trusts & Estates, same firm): no page opened on this pass was hers.

## Matrix

| Platform | Handle / URL | Status (VERIFIED / LEAD / WALL / NOT FOUND) | Role (P producer / A participant / C consumer / D dormant / unknown) | Last activity seen | Audience size seen | What was visible, logged out | Checked |
|---|---|---|---|---|---|---|---|
| LinkedIn | linkedin.com/in/christopher-chediak-95526 (the link is on his firm bio page; seen as a link only) | lead's lane, not opened | — | — | — | — | 2026-10-15 |
| X | @chrischediak, @christopherchediak, @chris_chediak → embed endpoint returns no profile header → no account. @chediak → exists (embed header "chediak"; oEmbed 200), 0 posts visible. @CChediak → exists (embed header "CChediak"; oEmbed 200), 0 posts visible | NOT FOUND for him. @chediak and @CChediak are other people (Maigret's extractor read them as "Alex Chediak — Christ-follower, Husband, Dad, Professor, Author…", 1,396 followers, created 2009, and "Carlos Chediak", 0 followers, created 2010-10-21; see triage) | — | — | — | x.com/<handle> is a JS shell with no og meta | 2026-10-15 |
| Instagram | instagram.com/chediak/, /cchediak/, /chrischediak/, /christopherchediak/, /chris.chediak/ | WALL (HTTP 200 generic shell, no og meta; the control @instagram returns the same shell) | unknown | — | — | title "Instagram"; login/challenge shell | 2026-10-15 |
| Facebook | facebook.com/chediak, /chris.chediak, /chrischediak, /christopher.chediak, m.facebook.com/chris.chediak, facebook.com/public/Chris-Chediak | WALL (HTTP 400 "Error" for all; control facebook.com/facebook also 400). Maigret's extractor read facebook.com/chediak as "Alex Chediak" — not him | unknown | — | — | nothing | 2026-10-15 |
| TikTok | tiktok.com/@chrischediak → status 10221 (no such user). tiktok.com/@chediak → exists: nickname "Chediak", empty bio, 0 videos, 2 followers, 5 following, created 2016-04-26, region US | NOT FOUND for @chrischediak; LEAD for @chediak (nothing Sacramento, lawyer or Shriners on it; a shared family-name handle) | unknown | none (0 videos) | 2 followers | — | 2026-10-15 |
| Threads | threads.com/@chrischediak, /@chediak, /@cchediak | WALL (generic "Threads" shell; control @instagram same). Maigret's extractor read @chediak as "Carolina Chediak", 123 followers — not him | unknown | — | — | — | 2026-10-15 |
| YouTube — own channel | search `"Chediak" Weintraub OR "Chris Chediak" OR "Christopher Chediak"` | NOT FOUND (no channel of his) | — | — | — | — | 2026-10-15 |
| YouTube — appearance | "Chris Chediak -- SEA Graduate Testimonial", SEA ARCHIVE channel (UCPlhBMevNNh9QBRwZdcYBIg), https://www.youtube.com/watch?v=rlIb7BubUGU | VERIFIED as a participant — name in the title; description: "Chris Chediak says the Sacramento Entrepreneurship Academy is the best at giving real-world business training." (his firm bio lists him as that academy's past president) | A | 2013-06-07 (published) | 69 views; 1:41 | — | 2026-10-15 |
| Substack | substack.com/@chediak = "Mattheus Chediak \| Substack" (not him); substack.com/@chrischediak → redirects to search, no profile | NOT FOUND | — | — | — | — | 2026-10-15 |
| Medium | medium.com/@chediak profile 403 (WALL); its feed = "Stories by the bitter boy on Medium" (not him); feeds for @chrischediak, @cchediak, @christopherchediak → 404 | NOT FOUND | — | — | — | — | 2026-10-15 |
| Reddit | reddit.com/user/chediak, /cchediak, /chrischediak (about.json) | WALL (HTTP 403) | unknown | — | — | — | 2026-10-15 |
| Pinterest | pinterest.com/chrischediak/ (uid 560557622277752751) | VERIFIED — full name "Chris Chediak", country US; the first board on the grid is "L&R Wedding Ideas", a collaborative board (313 pins) owned by Lynsey Chediak (Pinterest `lynnelouz`, 155–162 followers), his daughter by his own words on the firm's Shriners announcement thread (`chris-chediak-person.md` §5) | C (consumer; D — dormant since 2024-01-21) | 2024-01-21 (last pin save) | 2 followers / 15 following / 15 pins / 7 boards | created 2015-02-26; default avatar (no photo); no bio, location or website; public boards "Books to Read" (1 pin), "Food" (3), "Health, Fitness and Workouts" (2), "Places to Visit" (6), "Watches" (1), created 2015-11-28 | 2026-10-15 |
| Personal site / blog | chrischediak.com, christopherchediak.com, chediaklaw.com: no DNS; chediak.com: DNS record, no HTTP response | NOT FOUND | — | — | — | — | 2026-10-15 |
| Podcast — host or guest | Apple Podcasts episode search "Chediak": 9 episodes, none his ("#1 – Lynsey Chediak: Never give up", Rarebase Remarks, 2022-01-24, is his daughter's). Firm show *The Briefing by Weintraub Tobin* (Apple id1561403962, 281 episodes; feed https://thebriefing.blubrry.net/feed/podcast/, 295 items): "Chediak" appears only in the copyright line "Weintraub Tobin Chediak Coleman Grodin" | NOT FOUND | — | — | — | — | 2026-10-15 |
| Newsletter | California Lawyers Association, Business Law Section e-Bulletins and committee posts: https://calawyers.org/business-law/pllc-proposes-changes-to-california-llc-law/ (200), https://calawyers.org/business-law/recent-developments-affecting-partnerships-llcs-and-lps/ (200); May 2026 FIPVCC piece reposted on the firm site https://www.weintraub.com/2026/05/dfpi-suspends-implementation-of-the-fipvcc-pending-rulemaking/ (200; page meta "Written by Aravind Mahajan" is the site poster); Mondaq author page https://www.mondaq.com/author/3481580/weintraub-tobin-chediak-coleman-grodin-law-corporation-christopher-chediak (200) lists two articles under his name: "What DFPI's Suspension Of FIPVCC Implementation Means For Businesses" (17 Mar 2026) and "ICE's Updated I-9 Audit Guidelines: What Employers Need To Know" (28 May 2026, filed under Immigration — attribution as Mondaq shows it) | VERIFIED | P (occasional bar-bulletin author) | 2026-05-28 (Mondaq listing) | not shown | — | 2026-10-15 |
| Print | *Comstock's* magazine: "Here's What a Mergers & Acquisitions Deal Looks Like in Sacramento" (2025-10-14) https://www.comstocksmag.com/longreads/heres-what-mergers-acquisitions-deal-looks-sacramento (200, quotes him) and "Computing Litigation" (2011-05-01) https://www.comstocksmag.com/longread/computing-litigation (200, quotes him); CEB treatise chapters (*Forming and Operating LLCs in California*, *Advising California Partnerships*) listed on his firm bio https://www.weintraub.com/people/christopher-chediak-corporate-finance/ (200) | VERIFIED | A (quoted source) / P (treatise chapters) | 2025-10-14 | — | — | 2026-10-15 |
| Other — Snapchat | snapchat.com/@chrischediak (from /add/chrischediak) | LEAD — public page "Chris Chediak is on Snapchat!", bitmoji avatar only, no bio or stories visible; identity unclear. snapchat.com/add/cchediak → 404 | unknown | not shown | not shown | — | 2026-10-15 |
| Other — DailyMotion | dailymotion.com/chediak (API: screenname "Chris Chediak", username chediak, country US, created 2024-07-20) | LEAD — name match only; 0 videos, 0 followers, no description, default avatar | unknown | none | 0 | — | 2026-10-15 |
| Other — Bluesky | chediak.bsky.social "Chediak" (no bio, 0 posts, 11 followers, created 2024-09-02) → LEAD, unclear; mchediak.bsky.social = Mark Chediak, Bloomberg journalist → not him | LEAD / NOT FOUND | unknown | none | 11 | — | 2026-10-15 |
| Other — Tumblr | tumblr.com/cchediak = "Que seja doce.." (Portuguese) | not him | — | — | — | — | 2026-10-15 |
| Firm voice — Weintraub Tobin X | @weintraub_law (linked from weintraub.com; `twitter:creator` meta on firm posts; oEmbed 200) | exists; timeline WALL (embed endpoint 429) | — | not seen | not seen | — | 2026-10-15 |
| Firm voice — Weintraub Tobin Facebook | facebook.com/weintraubtobin (site footer) | WALL (400) | — | — | — | — | 2026-10-15 |
| Firm voice — Weintraub Tobin Instagram / Threads | instagram.com/weintraubtobin/ (site footer); threads.com/@weintraubtobin | WALL (shell) | — | — | — | — | 2026-10-15 |
| Firm voice — Weintraub Tobin TikTok | tiktok.com/@weintraublaw | VERIFIED firm account — "Weintraub Tobin", bio "Sophisticated legal services to businesses…", 42 videos, 37 followers, created 2026-01-29; no mention of him on the page | — | 2026 (recent uploads) | 37 followers | — | 2026-10-15 |
| Firm voice — Weintraub Tobin YouTube | youtube.com/@weintraubtobin (UCmqMbM5rgBEH08MVERmWYGQ) | VERIFIED firm channel; *The Briefing* and *California Employment News*; no video naming him in search; the one T&E-adjacent hit, "Navigating Business Interests as a Fiduciary in California" https://www.youtube.com/watch?v=6_LmvBixzTI (2025-05-29, 60 views), was presented by Kelly E. Dankbar, Lily M. Harris and Josiah M. Prendergast — neither Chediak | — | 2026-10-13 (last upload) | 459 subscribers; 356 videos; 50,858 views | joined 2022-12-27 | 2026-10-15 |
| Firm voice — Weintraub Tobin LinkedIn | linkedin.com/company/weintraub-tobin (site footer) | lead's lane, not opened | — | — | — | — | 2026-10-15 |
| Firm voice — firm pages about him | bio https://www.weintraub.com/people/christopher-chediak-corporate-finance/ (200; links only the firm's socials plus his LinkedIn); Shriners post https://www.weintraub.com/2026/09/chris-chediak-elected-chair-of-shriners-childrens-northern-california-board-of-governors/ (200; page meta "Written by Jason Bobadilla") | VERIFIED | A (subject) | 2026-09 (Shriners post) | — | — | 2026-10-15 |
| Shriners Children's Northern California (third party) | WebSearch twice for "Chediak" + Shriners Children's Northern California / Board of Governors / chair elect | NOT FOUND — no Shriners page, roster or release naming him surfaced; the firm's own post is the only source seen | — | — | — | — | 2026-10-15 |

## Where a comment would be seen, where a post would land

He produces on no social platform found on this pass. His one verified personal account, Pinterest, is a private-interest consumer account (watches, places, books, his daughter's wedding board) with two followers, dormant since January 2024. His public words live in firm and bar channels: the firm bio and firm posts, California Lawyers Association e-Bulletins (republished on weintraub.com and Mondaq), two *Comstock's* interviews, and one 2013 Sacramento Entrepreneurship Academy testimonial video with 69 views. LinkedIn, not opened here, is where the person file records his only social activity. On X no account of his exists; @chediak and @CChediak are other Chediaks. Instagram, Facebook, Threads and Reddit cannot be seen logged out, so whether he consumes there is unknown. A public comment on the SEA video or on a firm video would sit in rooms of double-digit views; nothing found here is a place where he posts.

## Every URL opened

- https://www.instagram.com/chediak/ · 200, WALL shell · title "Instagram", no og meta
- https://www.instagram.com/cchediak/ · 200, WALL shell · same
- https://www.instagram.com/chrischediak/ · 200, WALL shell · same
- https://www.instagram.com/christopherchediak/ · 200, WALL shell · same
- https://www.instagram.com/chris.chediak/ · 200, WALL shell · same
- https://www.instagram.com/instagram/ (control) · 200, same shell
- https://www.facebook.com/chediak · 400 · "Error"
- https://www.facebook.com/chris.chediak · 400 · "Error"
- https://www.facebook.com/chrischediak · 400 · "Error"
- https://www.facebook.com/christopher.chediak · 400 · "Error"
- https://m.facebook.com/chris.chediak · 400 (redirects to www …?_rdr) · "Error"
- https://www.facebook.com/public/Chris-Chediak · 400 · "Error"
- https://www.facebook.com/facebook (control) · 400
- https://www.threads.net/@chrischediak → threads.com · 200, WALL shell
- https://www.threads.com/@chediak · 200, WALL shell
- https://www.threads.com/@cchediak · 200, WALL shell
- https://www.threads.com/@instagram (control) · 200, same shell
- https://syndication.twitter.com/srv/timeline-profile/screen-name/chediak · 200 · profile header present (screenName "chediak"), 0 timeline entries
- https://syndication.twitter.com/srv/timeline-profile/screen-name/cchediak · 200 · profile header present (screenName "CChediak"), 0 entries
- https://syndication.twitter.com/srv/timeline-profile/screen-name/chrischediak · 200 · no profile header (no account)
- https://syndication.twitter.com/srv/timeline-profile/screen-name/christopherchediak · 200 · no profile header
- https://syndication.twitter.com/srv/timeline-profile/screen-name/chris_chediak · 200 · no profile header
- https://syndication.twitter.com/srv/timeline-profile/screen-name/weintraub_law · 429 (three attempts) · "Rate limit exceeded"
- https://publish.twitter.com/oembed?url=https://twitter.com/CChediak (→ publish.x.com) · 200 · "Posts by CChediak"
- https://publish.twitter.com/oembed?url=https://twitter.com/chediak · 200 · "Posts by chediak"
- https://publish.twitter.com/oembed?url=https://twitter.com/weintraub_law · 200 · "Posts by weintraub_law"
- https://x.com/CChediak · 200 · JS shell, 67 KB, no og meta
- https://x.com/chediak · 200 · JS shell, 161 KB, no og meta
- https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=… · 200, empty body · endpoint dead
- https://www.tiktok.com/@chrischediak · 200 · embedded state statusCode 10221 (user not found)
- https://www.tiktok.com/@chediak · 200 · "Chediak", 0 videos, 2 followers, created 2016-04-26, US, no bio
- https://www.tiktok.com/@weintraublaw · 200 · "Weintraub Tobin", 42 videos, 37 followers, created 2026-01-29
- https://www.tiktok.com/@tiktok (control) · 200 · state present
- https://medium.com/@chediak · 403 · Cloudflare (WALL)
- https://medium.com/feed/@chediak · 200 · "Stories by the bitter boy on Medium"
- https://medium.com/feed/@chrischediak · 404 · "Not Found – Medium"
- https://medium.com/feed/@cchediak · 404
- https://medium.com/feed/@christopherchediak · 404
- https://substack.com/@chediak · 200 · "Mattheus Chediak | Substack"
- https://substack.com/@chrischediak · 200 → redirect to https://substack.com/search/chrischediak?searching=profile · no profile
- https://www.reddit.com/user/chediak/about.json · 403 · WALL
- https://www.reddit.com/user/cchediak/about.json · 403 · WALL
- https://www.reddit.com/user/chrischediak/about.json · 403 · WALL
- https://www.pinterest.com/chrischediak/ · 200 · og:title "Chris Chediak (chrischediak) - Profile | Pinterest"; page JSON: 2 followers, 15 following, 15 pins, 7 boards, created 2015-02-26, last pin save 2024-01-21; first board "L&R Wedding Ideas" owned by Lynsey Chediak (`lynnelouz`), collaborative, 313 pins
- https://www.pinterest.com/chediak/ · 200 · "Chediak Diego (chediak)", bio "¡¡¡¡¡QUE NO DECAIGA!!!!!!1", og:url ar.pinterest.com
- https://www.pinterest.com/cchediak/ · 200 · "claudia chediak (cchediak)"
- https://www.tumblr.com/cchediak (also cchediak.tumblr.com) · 200 · "Que seja doce.. (@cchediak) on Tumblr"
- https://www.snapchat.com/add/chrischediak → /@chrischediak · 200 · "Chris Chediak is on Snapchat!", bitmoji only
- https://www.snapchat.com/add/cchediak · 404
- https://www.dailymotion.com/chediak · 200 · JS shell, title "Dailymotion"
- https://api.dailymotion.com/user/chediak?fields=… · 200 · screenname "Chris Chediak", US, created 2024-07-20, 0 videos, 0 followers, default avatar (https://s2.dmcdn.net/d/5000002HraHpp/720x720 opened: placeholder)
- https://public.api.bsky.app/xrpc/app.bsky.actor.searchActors?q=Chediak&limit=25 · 200 · 3 actors (Mark Chediak; "Chediak"; one unrelated)
- https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=chediak.bsky.social · 200 · "Chediak", no description, 0 posts, 11 followers, created 2024-09-02
- https://www.youtube.com/results?search_query=%22Chediak%22+Weintraub+OR+%22Chris+Chediak%22+OR+%22Christopher+Chediak%22 · 200 · one video naming him (SEA testimonial); the rest are firm videos not naming him
- https://www.youtube.com/watch?v=rlIb7BubUGU · 200 · SEA ARCHIVE, published 2013-06-07, 101 s, 69 views, description quoted above
- https://www.youtube.com/results?search_query=SEA+ARCHIVE+Chediak · 200 · only the same video
- https://www.youtube.com/watch?v=6_LmvBixzTI · 200 · Weintraub Tobin, 2025-05-29, 60 views; presenters Kelly E. Dankbar, Lily M. Harris, Josiah M. Prendergast; 0 mentions of Chediak
- https://www.youtube.com/@weintraubtobin/about · 200 · 459 subscribers, 356 videos, 50,858 views, joined 2022-12-27
- https://www.youtube.com/feeds/videos.xml?channel_id=UCmqMbM5rgBEH08MVERmWYGQ · 200 · last 15 uploads (2026-08-07 … 2026-10-13), none naming him
- https://itunes.apple.com/search?term=Chediak&entity=podcastEpisode · 200 · 9 episodes, none his
- https://itunes.apple.com/search?term=Weintraub+Tobin&entity=podcast · 200 · *The Briefing by Weintraub Tobin*, id1561403962, 281 episodes
- https://itunes.apple.com/lookup?id=1561403962 · 200 · feed URL
- https://thebriefing.blubrry.net/feed/podcast/ · 200 · 295 items; "Chediak" only in the copyright line
- https://www.weintraub.com/ · 200 · footer links: twitter.com/weintraub_law, facebook.com/weintraubtobin, instagram.com/weintraubtobin, linkedin.com/company/weintraub-tobin, tiktok.com/@weintraublaw, youtube.com/@weintraubtobin
- https://www.weintraub.com/people/christopher-chediak-corporate-finance/ · 200 · bio; links the firm's socials and linkedin.com/in/christopher-chediak-95526 (not opened); photo URL above
- https://www.weintraub.com/2026/09/chris-chediak-elected-chair-of-shriners-childrens-northern-california-board-of-governors/ · 200 · "Weintraub Tobin shareholder Chris Chediak has been elected Chair of the Board of Governors for Shriners Children's Northern California."
- https://www.weintraub.com/2026/05/dfpi-suspends-implementation-of-the-fipvcc-pending-rulemaking/ · 200 · FIPVCC piece
- https://www.mondaq.com/author/3481580/weintraub-tobin-chediak-coleman-grodin-law-corporation-christopher-chediak · 200 · 2 articles (17 Mar 2026; 28 May 2026); topics Corporate/Commercial Law, Immigration
- https://www.comstocksmag.com/longreads/heres-what-mergers-acquisitions-deal-looks-sacramento · 200 · quotes him
- https://www.comstocksmag.com/longread/computing-litigation · 200 · quotes him
- https://calawyers.org/business-law/pllc-proposes-changes-to-california-llc-law/ · 200 · names him
- https://calawyers.org/business-law/recent-developments-affecting-partnerships-llcs-and-lps/ · 200 · names him
- https://www.facebook.com/weintraubtobin · 400 · WALL
- https://www.instagram.com/weintraubtobin/ · 200, WALL shell
- https://www.threads.com/@weintraubtobin · 200, WALL shell
- https://html.duckduckgo.com/html/?q=%22Chris+Chediak%22 (and two variants) · 202 · bot challenge, WALL
- chrischediak.com, christopherchediak.com, chediaklaw.com · no DNS; chediak.com · DNS only, no HTTP
- WebSearch: `"Chris Chediak" OR "Christopher Chediak" Sacramento` (no hit on him); `"Chediak" Sacramento (instagram OR facebook OR …)` (no hit); `"Chris Chediak" Weintraub Tobin` (hits: https://www.weintraub.com/?p=2491 his bio, https://www.weintraub.com/?p=2492 Janet Z. Chediak's bio, firm posts); `"Chediak" Shriners Children's Northern California Board of Governors` (no hit); `Shriners Children's Northern California "Chediak" chair elect 2027` (no hit)

## Maigret hits triaged

Each hit from the lead's Maigret run opened logged out; fixya and adult sites skipped as noise.

- cchediak → https://twitter.com/cchediak: **not-him** — the account exists (embed header "CChediak", oEmbed 200) with 0 visible posts; Maigret's extractor read the profile as "Carlos Chediak", created 2010-10-21, 0 followers, default avatar. (Its PayPal hit under the same handle also reads "Carlos Chediak".)
- cchediak → https://www.tumblr.com/cchediak: **not-him** — blog title "Que seja doce.." (Portuguese).
- cchediak → https://www.pinterest.com/cchediak/: **not-him** — "claudia chediak (cchediak)".
- chrischediak → https://www.snapchat.com/add/chrischediak: **LEAD** — "Chris Chediak is on Snapchat!", bitmoji only, no bio or content.
- chrischediak → https://www.pinterest.com/chrischediak/: **VERIFIED-his** — name "Chris Chediak", US; the grid leads with the collaborative board "L&R Wedding Ideas" owned by Lynsey Chediak, his daughter; 7 boards, 15 pins, 2 followers; last save 2024-01-21.
- chediak → https://twitter.com/chediak: **not-him** — exists, 0 visible posts; Maigret's extractor read the bio "Christ-follower, Husband, Dad, Professor, Author (Beating the College Debt Trap, Thriving at College, Preparing Your Teens for College)…", name "Alex Chediak", 1,396 followers, created 2009-02-08.
- chediak → https://medium.com/@chediak: **not-him** — feed title "Stories by the bitter boy on Medium"; the profile page itself is a Cloudflare WALL.
- chediak → https://substack.com/@chediak: **not-him** — "Mattheus Chediak | Substack".
- chediak → https://www.facebook.com/chediak: **WALL** (400); Maigret's extractor read it as "Alex Chediak" → not-him on that evidence.
- chediak → https://www.threads.com/@chediak: **WALL** (shell); Maigret's extractor read it as "Carolina Chediak", 123 followers → not-him on that evidence.
- chediak → https://www.tiktok.com/@chediak: **LEAD** — "Chediak", empty bio, 0 videos, 2 followers, created 2016-04-26, US; nothing Sacramento, lawyer or Shriners.
- chediak, other hits in the same report, not requested but name-relevant: https://www.dailymotion.com/chediak **LEAD** (screenname "Chris Chediak", US, created 2024-07-20, empty); https://bsky.app/profile/chediak.bsky.social **LEAD** (no bio, 0 posts); GitHub, GitLab, Chess.com, BuyMeACoffee = Mattheus Chediak (**not-him**); SoundCloud/MixCloud = a São Paulo musician (**not-him**); Telegram "pedro chediak", PayPal "University of Miami Miller School of Medicine", Pinterest "Chediak Diego" (**not-him**).
- Janet Z. Chediak: none of the pages opened was hers; her firm bio (https://www.weintraub.com/?p=2492) surfaced only as a search hit.

## Open

- Snapchat @chrischediak and DailyMotion "Chris Chediak": name matches only; no bio, photo or cross-link to confirm or exclude him.
- X: no account under his name variants; whether he holds one under another handle is unknown, and the embed endpoint was rate-limited all session, so @chediak / @CChediak were excluded on Maigret's extracted bios rather than on a page I could read.
- Instagram, Facebook, Threads: existence unknown; all three wall logged-out curl even for known accounts. Reddit: 403.
- Shriners Children's Northern California: no page of theirs naming him was found by search; the Sacramento Business Journal is not reachable by these tools.
- Mondaq lists an immigration article (I-9 audits, 28 May 2026) under his author page; whether that attribution is Mondaq's error was not checked against weintraub.com.
- Search coverage: WebSearch declines name+platform queries for a private person; DuckDuckGo's HTML endpoint blocks curl; so no search-snippet evidence (including any LinkedIn snippet) was gathered on this pass.
