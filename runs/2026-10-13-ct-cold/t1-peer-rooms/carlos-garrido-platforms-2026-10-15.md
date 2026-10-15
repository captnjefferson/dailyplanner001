# Carlos Garrido — platform pass (public pages, logged out, 2026-10-15)

Method: curl with a desktop browser user agent (no login, no crawler spoofing, no browser pane), public API/embed endpoints where a platform offers one (YouTube feeds, Facebook page plugin, Bluesky public API, iTunes Search), WebSearch, and the Maigret reports already in `maigret/`. Limits: Instagram and Threads return JavaScript shells with no metadata logged out; Facebook returns HTTP 400 to curl (only the public page plugin renders); X's public syndication endpoint answered 429 (rate limit) on every attempt between 13:40 and 14:30; Reddit and Medium profile pages are behind Cloudflare. Every row was checked on 2026-10-15. "Dormant" is written only where the last activity is dated.

## Matrix

| Platform | Handle / URL | Status | Role | Last activity seen | Audience size seen | What was visible, logged out | Checked |
|---|---|---|---|---|---|---|---|
| LinkedIn | lead's lane, not opened | — | — | — | — | — | 2026-10-15 |
| X (personal) | none found | NOT FOUND | unknown | — | — | No personal handle surfaced in search or Maigret; `@carlosgarrido` is a Venezuelan lawyer (see triage). | 2026-10-15 |
| X (company voice) | https://twitter.com/sandler_miami | WALL | unknown | not seen | 1,447 followers (Maigret extraction, today) | Syndication endpoint 429 five times. Maigret (`maigret/sandler_miami.log`, run today) extracted: name "Sandler Miami", bio "We empower organizational growth through personal and professional development. #AimHighReachHigher NEW BOOK The 21st Century Ride-Along. Free Chapter", created 2013-05-18, 1,062 following, location "Miami, Florida.", link bit.ly/21stRideAlong. The 2022–23 Unscripted Selling show notes list "Twitter: @Sandler_Miami" (https://www.spreaker.com/show/5713715/episodes/feed). Last post date not seen. | 2026-10-15 |
| Instagram (personal) | none found | NOT FOUND | unknown | — | — | No personal handle in search, Maigret, or any of his sites. | 2026-10-15 |
| Instagram (company voice, current) | https://www.instagram.com/sandlertrainingmiami/ | WALL | unknown | not seen | not seen | JS shell, no og meta (page and /embed/). Exists per cross-links: the company YouTube channel's link block ("Instagram -> instagram.com/sandlertrainingmiami", https://www.youtube.com/channel/UC1a1iLv4cF1pTwgYtNJnW4Q/about) and https://linktr.ee/sandlermiami. | 2026-10-15 |
| Instagram (company voice, older) | https://www.instagram.com/sandler_miami/ | WALL | unknown | not seen | not seen | JS shell, no og meta. Listed as "Instagram: @Sandler_Miami" in the Unscripted Selling notes (2022–23) and in the Shoutout Miami interview (per the person read). | 2026-10-15 |
| Facebook (personal candidate) | https://www.facebook.com/carlosgarrido2024 | WALL (LEAD) | unknown | not seen | not seen | HTTP 400 to curl; the public page plugin renders blank, so it is a personal profile, not a Page. Maigret (`maigret/report_carlosgarrido2024_simple.json`, today) extracted name "Carlos Garrido", username `carlos.garrido.2024`, uid 61555751792891, with a profile photo. The handle matches the pattern of his LinkedIn slug `carlosgarrido2024`; nothing on the page itself was seen. | 2026-10-15 |
| Facebook (company voice) | https://www.facebook.com/AbsoluteSalesDevelopment | og-meta/plugin only | unknown | not seen | 1,117 followers | Page returns 400; the public plugin (https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FAbsoluteSalesDevelopment&tabs=timeline) shows "Sandler Training, Miami - Absolute Sales Development · 1,117 followers"; no posts rendered. Cross-linked from the YouTube channel and the Unscripted Selling notes. | 2026-10-15 |
| TikTok (company handle, his name on it) | https://www.tiktok.com/@sandlertrainingmia | VERIFIED | P (company voice) | not visible logged out | 797 followers · 94 following · 5,839 likes · 442 videos | Display name "Carlos Garrido"; bio "DM me “Grow” for info / Join the next live masterclass⬇️"; bio link linktr.ee/sandlermiami; account created 2025-05-20; not private, not verified. The page's own description meta reads "short videos created by Carlos Garrido". Linked as "TikTok -> tiktok.com/@sandlertrainingmia" from the company YouTube channel. 442 videos in about 17 months; individual video dates not rendered. | 2026-10-15 |
| TikTok (company voice, older) | https://www.tiktok.com/@sandlertrainingmiami | VERIFIED (company) | unknown | not visible | 137 followers · 19 videos | Display name "Absolute Sales Development"; bio "Sandler Training Miami" plus two staff mailboxes (Sofía Rodriguez, Hunter Furr); created 2021-10-20. Listed as "TikTok: @sandlertrainingmiami" in the Unscripted Selling notes. Appears superseded by @sandlertrainingmia; not marked dormant because no post date was visible. | 2026-10-15 |
| TikTok | https://www.tiktok.com/@sandler_miami | NOT FOUND | — | — | — | "Couldn't find this account" (statusCode 10221). | 2026-10-15 |
| Threads | https://www.threads.net/@sandler_miami · https://www.threads.net/@carlosgarrido | WALL | unknown | — | — | Both redirect to threads.com and return a JS shell with no og meta and no profile strings; existence unknown. | 2026-10-15 |
| YouTube (company voice) | https://www.youtube.com/channel/UC1a1iLv4cF1pTwgYtNJnW4Q (handle @sandlertrainingmiami) | VERIFIED | P (company voice) | 2026-10-14 ("Your Sales Team Is Either An Asset Or A Liability.") | 666 subscribers · 656 videos | Title "Sandler Miami - Absolute Sales Development"; channel created 2013-10-22; description "At Sandler Miami, we specialize in turning sales headaches into money-making opportunities…". Feed (https://www.youtube.com/feeds/videos.xml?channel_id=UC1a1iLv4cF1pTwgYtNJnW4Q): 15 uploads Sep 10–Oct 14, 2026, titles matching his LinkedIn themes ("The Hidden Factor Lowering Your Company's Value", "CEO acting like the seller", "Can You Predict Your Next Quarter? Buyers can tell when you can't", "Is Your CRM Creating Value Or Risk?"). Channel links: Facebook AbsoluteSalesDevelopment, Instagram sandlertrainingmiami, LinkedIn `carlosgarrido2024`, TikTok @sandlertrainingmia, linktr.ee/sandlermiami. Who is on camera was not verified (videos not watched). | 2026-10-15 |
| YouTube (personal candidate) | https://www.youtube.com/@carlosgarrido2022/about | LEAD | unknown | none (no uploads) | not shown | Channel "Carlos garrido" (UCgskOEZK3ccY7bXKojb9B-Q), created 2020-02-14, no videos, no description, no links. The handle matches his older LinkedIn slug; nothing on the page ties it to him. | 2026-10-15 |
| Substack | https://substack.com/@carlosgarrido | NOT FOUND (not him) | — | — | — | Redirects to https://substack.com/@garrido, "Dr. Carlos L. Garrido", philosophy professor and Midwestern Marx Institute director. Not him. No other Substack presence found. | 2026-10-15 |
| Medium | https://medium.com/@carlosgarrido | WALL (LEAD) | unknown | none | — | Profile page 403 (Cloudflare). Feed https://medium.com/feed/@carlosgarrido returns "Stories by Carlos Garrido on Medium" with 0 stories; identity unknown. | 2026-10-15 |
| Reddit | https://www.reddit.com/user/carlosgarrido/about.json | WALL | — | — | — | 403. No handle of his is known on Reddit. | 2026-10-15 |
| Pinterest | https://www.pinterest.com/carlosgarrido/ | LEAD (no tie) | unknown | not shown | 36 followers · 22 pins · 1 board | "Carlos A. Garrido", no bio, no location. Nothing ties it to him. | 2026-10-15 |
| Bluesky | https://bsky.app/profile/carlosgarrido.bsky.social | LEAD (empty) | unknown | none (0 posts) | 6 followers · 26 following | Public API: no display name, no bio, created 2023-07-31. | 2026-10-15 |
| Personal site / blog | https://305founders.com/ | VERIFIED | P | per the person read: essays dated through Oct 12–13, 2026 (sitemap) | — | 200. Only outbound social link on the homepage is https://www.linkedin.com/in/carlosgarrido2024. | 2026-10-15 |
| Personal site (directory) | https://bestsalesteamtraining.com/ | VERIFIED | P | — | — | 200. No social links in the HTML. | 2026-10-15 |
| Personal site (recruiting) | https://revenuebench.io/ | VERIFIED | P | — | — | 200. No social links in the HTML. | 2026-10-15 |
| Company site | https://go.sandler.com/absolute/ · https://absolute.sandler.com/ | WALL / connection failed | — | — | — | go.sandler.com: 403 Cloudflare "Just a moment". absolute.sandler.com: connection failed twice (DNS resolves to 199.46.34.162). | 2026-10-15 |
| Link hub (company voice) | https://linktr.ee/sandlermiami | VERIFIED (company) | — | — | — | Title "Sandler Miami Official: TikTok, Instagram, Facebook"; tagline "For Founders + Sales Leaders Building Scalable Revenue Teams."; links to instagram.com/sandlertrainingmiami, go.sandler.com/absolute and localoffers.sandler.com pages ("Enroll now: Mastering LinkedIn for Sellers Program", bootcamp, Budget Checklist, 30 Second Commercial Creator, Business Performance Assessment). | 2026-10-15 |
| Podcast (host) | "Unscripted Selling" — https://podcasts.apple.com/us/podcast/id1654064599 · feed https://www.spreaker.com/show/5713715/episodes/feed | VERIFIED | D (dormant since 2023-11-17) | 2023-11-17 (ep 51, "How to close deals: The key to sell anything") | 51 episodes | Show description: "We are Sofía Rodriguez and Carlos Garrido, coming at you straight from Miami and… well… figuring out how to do a podcast". Produced by Naranja Media Podcasts. Ran 2022-11-10 to 2023-11-17. Notes list TikTok @sandlertrainingmiami, Twitter @Sandler_Miami, Instagram @Sandler_Miami, Facebook @AbsoluteSalesDevelopment, LinkedIn `carlosgarrido2022`. | 2026-10-15 |
| Podcast (guest) | Apple Podcasts directory (iTunes Search API) | VERIFIED | A | 2026-07-07 | — | Episodes naming him in the notes: How to Succeed, "Asking for Referrals" (2019-10-14, https://podcasts.apple.com/us/podcast/id1097591566?i=1000453394498); Cyberside Chat (2020-03-20, https://podcasts.apple.com/us/podcast/id1503434117?i=1000469031490, "Carlos Garrido from absolute.sandler.com"); Growth Marketing for Martians (2020-12-14, https://podcasts.apple.com/us/podcast/id1533706484?i=1000502427463); Sales Tales ep 12 (2023-08-07, https://podcasts.apple.com/us/podcast/id1675110408?i=1000623716343, "founder and CEO of Miami Absolute Sales Development"); More Cheese Less Whiskers ep 255 (2023-11-05, https://podcasts.apple.com/us/podcast/id1135262567?i=1000633741371); Building Your Sales Engine with Mark McGraw (2025-05-15, https://podcasts.apple.com/us/podcast/id1779606270?i=1000708560872, "founder of Miami Absolute, who's nearly 100 pounds down"); How to Succeed, "Transforming Your Life" (2025-09-08, per the person read); The Exceptional Sales Leader ep 877 (2026-03-31, https://podcasts.apple.com/us/podcast/id1510188933?i=1000758343296); Confessions of a Vistage Chair E16 (2026-07-07, https://podcasts.apple.com/us/podcast/id1872757018?i=1000775768126). LEAD only: Confessions of a Sales Pro with Ian Selbie ep 267 "Carlos Garrido Pro-2-Pro" (2026-03-19, https://podcasts.apple.com/us/podcast/id1538032219?i=1000756121297) — the notes are sponsor text and do not say which Carlos Garrido. | 2026-10-15 |
| Newsletter (company voice) | "Limitless Selling" — https://localoffers.sandler.com/the-sandler-miami-sales-tribe-newsletter | VERIFIED (company) | P | — | — | Page title "The Limitless Sandler Newsletter"; sign-up page live. The biweekly cadence and "5K+ readers" claim were recorded in the person read and were not re-captured today. | 2026-10-15 |

## Maigret hits triaged

Reports present: `maigret/report_carlosgarrido_simple.json` (86 hits), `report_carlosgarrido2022_simple.json` (5), `report_carlosgarrido2024_simple.json` (5), and `sandler_miami.log` (4 hits; the log says a JSON report was saved but none is in the folder). fixya, joyreactor, Pling, Google Scholar and adult sites skipped as noise.

- `carlosgarrido2024` → https://www.facebook.com/carlosgarrido2024 — **WALL / LEAD.** HTTP 400; plugin blank (personal profile). Maigret's extraction (name "Carlos Garrido", username `carlos.garrido.2024`, uid 61555751792891, profile photo present) is the only evidence; the slug pattern matches his LinkedIn `carlosgarrido2024`.
- `carlosgarrido2022` → https://www.youtube.com/@carlosgarrido2022/about — **LEAD.** "Carlos garrido", created 2020-02-14, no videos, no description, no links.
- `sandler_miami` → https://twitter.com/sandler_miami — **company voice, VERIFIED by cross-link, content WALL.** Named in the Unscripted Selling notes and the Shoutout Miami interview; the syndication endpoint was rate-limited, so Maigret's extraction (above) stands in for the page.
- `carlosgarrido` (shared name), the five platforms the brief asked for:
  - Twitter https://twitter.com/carlosgarrido — **not-him.** Maigret bio: "Abogado; caraquista; playero… lucho a diario contra este régimen et je parle français", location Venezuela, 2,299 followers. Page itself not reachable (429).
  - Medium https://medium.com/@carlosgarrido — **WALL / LEAD.** 403 profile; feed has 0 stories.
  - TikTok https://www.tiktok.com/@carlosgarrido — **LEAD (empty).** Display name "carlosgarrido", 3 followers, 0 videos, no bio, created 2024-11-06.
  - YouTube https://www.youtube.com/@carlosgarrido/about — **not-him.** Spanish-language hair/grooming review channel ("reviews, unboxings, primeras impresiones de productos para el cabello"), 1.7K subscribers, 57 videos, joined Apr 18, 2017.
  - Bluesky https://bsky.app/profile/carlosgarrido.bsky.social — **LEAD (empty).** No name, no bio, 0 posts.
- Other `carlosgarrido` hits with extracted data, not opened (from the report): linktr.ee/carlosgarrido → links to carlosgarridoHQ accounts and portokabel.com — **not-him**; Calendly → "carlos eduardo garrido montoya", America/Santiago — **not-him**; SlideShare → a history teacher in Chile — **not-him**; Telegram → a TV repair technician — **not-him**; Chess.com → Portugal — **not-him**; PayPal → Daly City, CA — **not-him**; SoundCloud → Rio de Janeiro — **not-him**; Behance → "Carlos Garrido", Doral, FL, created 2014-12-19, 0 followers, 0 views — **LEAD (weak)**; Freelancer.com → employer account "Miami, United States", created 2004 — **LEAD (weak; predates his 2009 move)**; Snapchat, Disqus (1 comment, 2010), GitHub, GitLab, Duolingo, Imgur — name only, **LEAD (weak)**.

## Where a comment would be seen, where a post would land

In public, logged out, he produces on his own sites (305founders.com essays near-daily; the directory and Revenue Bench sites) and, under the company name, on YouTube (656 videos, the latest on Oct 14, 2026) and on the TikTok account that carries his name as its display name (442 videos since May 2025); LinkedIn is where his own words go, and that is the lead's lane. No personal X, Instagram, Facebook, Threads, Substack, Medium or Reddit account could be found, so nothing shows where he reads or comments outside LinkedIn. The podcast he co-hosted with Sofía Rodriguez, "Unscripted Selling", has been dormant since Nov 17, 2023; the older TikTok (19 videos) looks superseded but carries no visible dates. What could not be seen: both company Instagram accounts, the Facebook page's posts and the `carlosgarrido2024` profile, the company X timeline (rate-limited), Threads, Reddit and Medium.

## Every URL opened

- https://www.instagram.com/sandler_miami/ · 200, JS shell, no og meta · WALL
- https://www.instagram.com/sandler_miami/embed/ · 200, shell · WALL
- https://www.instagram.com/sandlertrainingmiami/ · 200, JS shell, no og meta · WALL
- https://www.instagram.com/sandlertrainingmiami/embed/ · 200, shell · WALL
- https://www.facebook.com/AbsoluteSalesDevelopment (and with trailing slash) · 400 "Error" · WALL
- https://m.facebook.com/AbsoluteSalesDevelopment/ · 301, no body
- https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FAbsoluteSalesDevelopment&tabs=timeline&width=500&height=600 · 200 · page name and 1,117 followers; no posts rendered
- https://www.facebook.com/carlosgarrido2024 (and with trailing slash) · 400 · WALL
- https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Fcarlosgarrido2024&tabs=timeline&width=500&height=600 · 200 · blank (not a Page)
- https://www.youtube.com/channel/UC1a1iLv4cF1pTwgYtNJnW4Q/about · 200 · title, description, 666 subscribers, 656 videos, link block
- https://www.youtube.com/feeds/videos.xml?channel_id=UC1a1iLv4cF1pTwgYtNJnW4Q · 200 · 15 entries, Sep 10–Oct 14, 2026
- https://www.youtube.com/@sandlertrainingmiami/videos · 200
- https://www.youtube.com/@carlosgarrido2022/about · 200 · empty channel
- https://www.youtube.com/feeds/videos.xml?channel_id=UCgskOEZK3ccY7bXKojb9B-Q · 200 · 0 entries, channel dated 2020-02-14
- https://www.youtube.com/@carlosgarrido/about · 200 · grooming channel (collision)
- https://www.threads.net/@sandler_miami · 200 (→ threads.com), JS shell · WALL
- https://www.threads.net/@carlosgarrido · 200, JS shell · WALL
- https://www.tiktok.com/@sandler_miami · 200 · "Couldn't find this account" · NOT FOUND
- https://www.tiktok.com/@sandlertrainingmia · 200 · profile data in page JSON
- https://www.tiktok.com/@sandlertrainingmiami · 200 · profile data in page JSON
- https://www.tiktok.com/@carlosgarrido · 200 · empty account
- https://syndication.twitter.com/srv/timeline-profile/screen-name/sandler_miami · 429 ×5 (13:40–14:30) · WALL
- https://syndication.twitter.com/srv/timeline-profile/screen-name/SandlerMiami · 429 ×2 · WALL
- https://publish.twitter.com/oembed?url=https://twitter.com/sandler_miami · empty body
- https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=sandler_miami · 200, empty
- https://medium.com/@carlosgarrido · 403 Cloudflare · WALL
- https://medium.com/feed/@carlosgarrido · 200 · 0 items
- https://substack.com/@carlosgarrido · 200 → redirected to https://substack.com/@garrido (Dr. Carlos L. Garrido) · not him
- https://www.reddit.com/user/carlosgarrido/about.json · 403 · WALL
- https://www.pinterest.com/carlosgarrido/ · 200 · "Carlos A. Garrido"
- https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=carlosgarrido.bsky.social · 200 · empty profile
- https://305founders.com/ · 200
- https://bestsalesteamtraining.com/ · 200
- https://revenuebench.io/ · 200
- https://go.sandler.com/absolute/ · 403 Cloudflare · WALL
- https://absolute.sandler.com/ · connection failed twice
- https://linktr.ee/sandlermiami · 200
- https://localoffers.sandler.com/the-sandler-miami-sales-tribe-newsletter · 200
- iTunes Search API: term "carlos garrido sandler", "carlos garrido" (episodes), "carlos garrido" (podcasts) · 200
- https://itunes.apple.com/lookup?id=1654064599 · 200 → https://www.spreaker.com/show/5713715/episodes/feed · 200, 51 items
- https://itunes.apple.com/lookup?id=1538032219 · 200 → https://rss.buzzsprout.com/1442926.rss · 200 (ep 267 notes are sponsor text only)
- WebSearch ×3 ("Carlos Garrido" + Sandler Miami + platforms; + Vistage Miami + Substack/Medium/Reddit/podcast; + 305Founders/Revenue Bench/Absolute Sales Development) · search-only; nothing new beyond go.sandler.com team page; one Miami New Times "305 Photo of the Day" credits "Carlos Garrido's Flickr" (https://www.miaminewtimes.com/news/305-photo-of-the-day-how-miamians-dress-for-the-cold-6564042/), not tied to him · LOW

## Open

- No personal account on X, Instagram, Facebook (beyond the `carlosgarrido2024` candidate), Threads, Substack, Medium or Reddit could be found; the name collides heavily and search engines returned nothing usable.
- Whether https://www.facebook.com/carlosgarrido2024 is his: the page is walled logged out; only Maigret's name/photo extraction exists.
- Last-post dates for the company X account, both Instagram accounts, the Facebook page and both TikTok accounts: not visible logged out.
- Who appears on camera in the company YouTube and TikTok videos: not verified (nothing was watched); the TikTok display name "Carlos Garrido" is the only signal.
- Confessions of a Sales Pro ep 267 (Mar 19, 2026): which Carlos Garrido was the guest is not stated in the notes.
- The Sandler site (go.sandler.com/absolute, absolute.sandler.com) could not be fetched, so its footer social links were not read today.
- 305founders.com was not checked for a newsletter sign-up form.
- The Flickr account credited by Miami New Times was not opened; no evidence it is his.
