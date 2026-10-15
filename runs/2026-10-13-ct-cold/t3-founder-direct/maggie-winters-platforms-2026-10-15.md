# Maggie Winters — platform pass (public pages, logged out, 2026-10-15)

Method and limits: every page below was opened logged out with curl and a desktop Chrome user agent (no cookies, no login, no crawler spoofing), plus each platform's own public endpoints (Substack public_profile and archive APIs, Medium RSS, TikTok's page JSON, Bluesky's public API, iTunes Search), one public mirror of X profile fields (api.fxtwitter.com — x.com itself serves a JS shell logged out), WebFetch where curl got only a shell, and web search for snippets. Instagram, Facebook, Reddit, Product Hunt and Medium's profile tabs wall logged-out clients; X's public timeline endpoint answered 429 on every attempt and the Nitter mirrors are shut down, so no X post dates were read. LinkedIn was not opened.

## Matrix

| Platform | Handle / URL | Status (VERIFIED / LEAD / WALL / NOT FOUND) | Role (P producer / A participant / C consumer / D dormant / unknown) | Last activity seen | Audience size seen | What was visible, logged out | Checked |
|---|---|---|---|---|---|---|---|
| LinkedIn | linkedin.com/in/maggiewinters | lead's lane, not opened | — | — | — | — | — |
| X (current handle) | @maggiewinters_ · https://x.com/maggiewinters_ | VERIFIED — handle by her own cross-links (her Behance profile links twitter.com/maggiewinters_; her old handle's bio names it); profile fields read through the public mirror api.fxtwitter.com; x.com itself is a JS shell logged out | P (5,816 posts); cadence unknown | not visible: timeline endpoint 429 on three rounds, oEmbed empty, mirrors down | 989 followers · 1,169 following · 8,718 likes | Name "Maggie Winters"; bio "partner + creative director @itsthisjanuary. bad at jokes. she/her."; location Washington, DC; website maggie.is (dead, see below); joined 2011-01-12; not protected | 2026-10-15 |
| X (2015 handle) | @moonstompmaggie · https://x.com/moonstompmaggie | VERIFIED (mirror: name "Maggie Winters Gaudaen") | D — a placeholder | none: 0 posts | 4 followers · 0 following | Bio "The former internet home of @maggiewinters_"; joined 2020-10-12, i.e. re-registered as a pointer to the current handle; x.com returns 200 for this handle where dead handles return 404 | 2026-10-15 |
| X (agency) — company voice | @itsthisjanuary · https://x.com/itsthisjanuary | VERIFIED (mirror) | P (84 posts); cadence unknown | not visible | 392 followers · 591 following | "This January" — "An independent creative agency growing next year's brands. DTC, venture-backed startups and the occasional Fortune 500. Formerly known as January Third."; DC; thisjanuary.com; joined 2020-01-03. The older @thisjanuary handle no longer exists (x.com 404; mirror "User not found") | 2026-10-15 |
| Instagram | @maggiewinters_ · https://www.instagram.com/maggiewinters_/ | WALL — handle identity VERIFIED by cross-link (her site and her Substack profile both link it) | unknown | not visible | not visible | Logged-out shell only ("PolarisLoggedOut" page; no og:title / og:description); the public ?__a=1&__d=dis URL returns 201 with an empty body; public vs private cannot be told. Old handle @moonstompmaggie and agency @thisjanuary_ (company voice): same shell | 2026-10-15 |
| Facebook | facebook.com/lookitsmaggie (her own link on Behance) · https://www.facebook.com/lookitsmaggie | WALL — handle VERIFIED by cross-link, page unseen | unknown | not visible | not visible | HTTP 400 "Error" page to a logged-out client; same for /maggiewinters, /moonstompmaggie, /maggie.winters, /popwedco, /thisjanuary, /thisjanuary_, /januarythird | 2026-10-15 |
| TikTok | @maggiewinters_ · https://www.tiktok.com/@maggiewinters_ | VERIFIED | P (15 videos) and C (follows 588); last post not visible | not visible — the logged-out page JSON carries profile stats only; no video list rendered (curl and WebFetch) | 153 followers · 588 following · 9,588 likes · 22 friends | Display "maggie winters"; bio "cofounder @This January, obsessed with women's health, always hunting for a good noodle"; public (privateAccount false); account created 2021-05-31; region US; 15 videos | 2026-10-15 |
| TikTok (agency) — company voice | @thisjanuary · https://www.tiktok.com/@thisjanuary | VERIFIED | P (62 videos) | not visible | 1,024 followers · 37 following · 16.6K likes | "This January" — "an independent creative agency → building next year's brands / washington, d.c."; created 2023-01-31. @moonstompmaggie on TikTok: "Couldn't find this account" | 2026-10-15 |
| Threads | @maggiewinters_ · https://www.threads.com/@maggiewinters_ | VERIFIED | never posted (0 threads) | none: "No threads yet" | 290 followers | Display "Maggie Winters"; bio "🪂 being alive is weird ⚫️ building itsjanuarythird while we all figure it out" (still the pre-2023 agency name); "Log in to see more" beneath. Read via WebFetch; curl got a shell. @moonstompmaggie on Threads: login shell (WALL). Agency @thisjanuary_ (company voice): exists — page title "ᴛʜɪs ᴊᴀɴᴜᴀʀʏ (@thisjanuary_)" — bio, counts and posts not rendered | 2026-10-15 |
| YouTube | @moonstompmaggie · https://www.youtube.com/@moonstompmaggie | VERIFIED (an upload is titled "Final Flash Animation Maggie Winters") | D since 2011-02-08 | 2011-02-08 (both uploads) | 204 channel views; subscriber count not shown | 2 videos: "Final Flash Animation Maggie Winters" (16 views) and "Neutraface Animation.mov" (188 views), both uploaded 2011-02-08; no description, no links; joined 2011-02-08 | 2026-10-15 |
| YouTube (handle) | @maggiewinters_ · https://www.youtube.com/@maggiewinters_ | LEAD | unknown | none | none shown | Channel titled "Maggie Winters", joined 2020-06-18; no videos, no description, no links — nothing on the page ties it to her beyond the handle | 2026-10-15 |
| YouTube (agency) | @thisjanuary · https://www.youtube.com/@thisjanuary | NOT FOUND for the agency | — | — | — | The handle is held by an empty channel titled "N", joined 2006-02-26. The agency's September 2026 spots sit on the production company's channel "Unrivaled" (e.g. https://www.youtube.com/watch?v=ve3OWPEn7wE, 2026-09-16, "Comedy Director, Nathan Colby Directs, 'Everybody Knows' for CTIA") | 2026-10-15 |
| Substack | maggiewintersmaggiewinters · https://maggiewintersmaggiewinters.substack.com/ · https://substack.com/@maggiewintersmaggiewinters | VERIFIED | D (one post) + C (11 reads) — dormant since 2025-08-01 | 2025-08-01 "The Age of the Brand Mascot (Again)" — 0 comments, 0 hearts; the public activity feed holds only that post (no notes, no restacks) | 5 followers; subscriber count hidden ("See subscribers"); 0 recommendations | Bio "weird brain, many thoughts 🌞 cofounder, THIS JANUARY 👁️ i'm new here"; profile set up 2025-04-09; publication created 2025-07-30; payments disabled, pledges on; profile links LinkedIn and Instagram @maggiewinters_. Free subscriptions: Ctrl Alt Right Delete, The Existentialist Republic, Free Ideas, Lenny's Newsletter, METHOD®, On Substack, Product Fridays, A SHORT LIST, Slow Boring, The Substack Post, WelcomeStack | 2026-10-15 |
| Medium | @maggie-winters · https://maggie-winters.medium.com/ · feed https://medium.com/feed/@maggie-winters | VERIFIED (feed) / WALL (profile, /about, /responses, /lists and ?format=json all 403 Cloudflare, to curl and to WebFetch) | P; last 2026-05-22; participant status unknown | 2026-05-22 | not visible | 9 posts in the feed, all long-form (661–1,442 words), none a response: 2016-02-01 "Fucking Valentine's Day"; 2020-07-02 "The Fastest Competitive Analysis in the History of the World"; 2020-12-24 "An Ode to Christmas, Brought to You by Advertising"; 2021-12-27 "Do Businesses Get to Have Funerals? A Eulogy to My First Company."; 2022-06-03 "The Slide Deck That Changed My Life" (published in Entrepreneur's Handbook, ehandbook.com); 2022-08-10 "This isn't a breakup, it's business: a love letter to rejection"; 2024-01-03 "Girl freezes eggs. Girl tells internet."; 2024-01-03 "The best way to hire a creative agency…"; 2026-05-22 "Egg freezing stress, meet Claude: Building for women's health and fertility in the age of AI" (tags womens-health, claude-code, women-in-tech) | 2026-10-15 |
| Reddit | /user/maggiewinters · /moonstompmaggie · /maggiewinters_ · /maggiegaudaen | WALL | unknown | — | — | about.json → 403 for all four; stopped per rule | 2026-10-15 |
| Pinterest | maggiewinters · https://www.pinterest.com/maggiewinters/ | VERIFIED (website field maggie.is; about "human creative director") | C — an active curator; last save 2026-10-13 | 2026-10-13 21:21 UTC (last pin saved); boards modified 2026-10-13 (Cakes), 2026-10-03 (Nails), 2026-09-07 (Sparkles ✨), 2026-07-20 (Phones), 2026-06-27 (branding), 2026-04-25 (Food - Savory) | 553 followers · 222 following · 1,145 pins · 13 boards | Account created 2011-09-19. 9 of 13 boards rendered: branding (90 pins, created 2026-01-07), Cakes (62), Food - Savory (491, since 2014), Food: Lunch (1), Nails (59), Phones (87), Sparkles ✨ (66), My Posh Closet (0, created 2026-09-06), My Posh Picks (0, created 2026-09-06). A user object "Zach Goodwin" (ZBGoodwin_2020) sits in the page data. Other handles (moonstompmaggie, maggiewinters_, maggiegaudaen, thisjanuary): "User not found" | 2026-10-15 |
| Behance | maggiewinters · https://www.behance.net/maggiewinters | VERIFIED | D since 2019-01-19 | 2019-01-19 (the only project timestamp on the page) | 368 followers · 163 following · 1,391 appreciations · 46,734 project views | "Maggie Winters — Partner + ECD", This January, Washington, DC; "what's this page?: work from 2013-2019 at ISL 💖"; member since 2011-01-30; only project visible: "Uterus Invaders iOS Game"; profile links: maggie.is, januarythird.co, twitter.com/maggiewinters_, facebook.com/lookitsmaggie, dribbble.com/moonstompmaggie, linkedin.com/in/maggiewinters | 2026-10-15 |
| Dribbble | moonstompmaggie · https://dribbble.com/moonstompmaggie | VERIFIED ("Maggie Winters — building ➡️") | D since 2018-11-18 | 2018-11-18 "Uterus Invaders / Level Up" | counts not rendered | 15 shots: 2014-03-24 "Newspaper — The New Talk"; 2014-09-05 "Facebook Mentions Box Interface"; 2015-08-11 "Dot, a Period and Fertility Tracker"; 2015-08-13 "404 Page — ISL.co"; then eleven on 2018-11-11/12/18 (three Luden's pieces, two Meme Machine pieces, Pocket-Sized DIY Dental Dam, The It Kit Sex Ed Prototype, Capital One Elements, Fake News: The Game, Lyft Luck Slot Machine, Uterus Invaders) — ISL-era work. Individual shot pages answer 202 with an empty body | 2026-10-15 |
| Bluesky | maggiewinters.bsky.social · https://bsky.app/profile/maggiewinters.bsky.social | LEAD | unknown | none: 0 posts | 1 follower · 1 following | No display name, no bio, created 2024-11-15 (public API). moonstompmaggie.bsky.social, maggiewinters.com, thisjanuary.bsky.social, thisjanuary.com: not found | 2026-10-15 |
| Personal site / blog | https://maggiewinters.com/ (+ /about, /notebook) | VERIFIED | P — rebuilt September 2026; no feed | sitemap lastmod 2026-09-03 for all three pages; the notebook page source carries 2026-09-09 and 2026-09-10 | n/a | og:title "Maggie Winters — Co-Founder and Chief Creative Officer of This January"; outbound: Email, LinkedIn, Instagram @maggiewinters_, Medium; no RSS (/feed, /rss, /feed.xml, /rss.xml, /atom.xml → 404). Notebook, 8 items: "egg freezing companion app — an app mvp to help women through egg freezing"; stare-at-squares.pdf; "funeral for a tampon — a wacky stunt concept for a menstrual disc brand"; "the fitting room.pdf — the bridal try-on experience for everyday clothes"; "text club — an sms-based dating experiment"; "agencyland-game.jpg — agency suffering, now a board game!"; dcpools.netlify.app ("see what dc public pools are open right now"); thisjanuary.com. Three decks hosted on Dropbox (Tampon Funeral, squares deck, Fitting Room sponsor deck). About page: cofounded the agency with Zach Goodwin at 29, "grown it from five people to twenty", six consecutive years of growth, 2026 Inc. 5000; founded the NOOK Artist Residency in 2026; goal "to talk to 100 students a year… and organize events for at least 1,000 people every year"; wrote a book on planning a microwedding in the Pop Wed Co year | 2026-10-15 |
| Old portfolio domain | maggie.is | NOT FOUND (dead) | — | — | — | DNS A 54.194.41.141 on ISNIC forwarding nameservers; http → 301 to https://maggie.is/ → the TLS connection fails. Still the website on her X, Pinterest and Behance profiles | 2026-10-15 |
| Podcast (guest) | Apple Podcasts episode pages, listed at right | VERIFIED | guest only; no show of her own found; last 2024-10-02 | 2024-10-02 | n/a | Design Intercourse, "Wedding Design with Maggie & Steven", 2017-03-22 — description names POP Wed Co. and "Maggie and Stephen Gaudaen" — https://podcasts.apple.com/us/podcast/wedding-design-with-maggie-steven/id1050697945?i=1000382995630 · storyOS, "Maggie Gaudaen on Telling Stories in the Commercial Space", 2018-07-12 — https://podcasts.apple.com/us/podcast/maggie-gaudaen-on-telling-stories-in-the-commercial-space/id1144237944?i=100041570 (feed https://feeds.transistor.fm/story-podcast) · Reel II Real With Coach Herb & B, "Episode 9: Pop We'd Co.", 2020-08-12, "its co owner Maggie Gaudaen" — https://podcasts.apple.com/us/podcast/episode-9-pop-wed-co/id1521671655?i=1000487526766 (video "Episode 8: PopWedCo", 2020-08-15, https://www.youtube.com/watch?v=MV9dx0EfHMc) · Brands & Campaigns, "23: Behind 'Agencyland': A Board Game From This January", 2024-10-02, with Zach Goodwin — https://podcasts.apple.com/us/podcast/behind-agencyland-a-board-game-from-this-january/id1714654583?i=1000671547447 (episode 24, 2024-10-16, discusses it without her). Collisions, not her: the show "Literally Life Changing with Maggie Winters" (Apple id1846195822, from October 2025) and the "Maggie Winters" guest spots on Not Aspirational (2020-12-18), Good at Parties (2021-09-17), The Ladylike Podcast (2023-04-10), Brooke and Connor Make A Podcast (2025-02-06), So True (2025-11-20), The Comment Section (2026-01-28) and The Tangle (2026-08-25) all describe the Chicago comedian, @saggiesplinters | 2026-10-15 |
| Newsletter (personal) | her Substack, above | VERIFIED | D | 2025-08-01 | 5 followers; subscribers hidden | One issue, 2025-08-01 | 2026-10-15 |
| Newsletter (agency) — company voice | Mailchimp archive https://us17.campaign-archive.com/home/?u=51d9f2bade0fed8148878b2c8&id=4529ad252e | VERIFIED | P, every two to five months | 2026-09-10 "Odds and ends of summer at This January 🌞" | n/a | Previous issues: 2026-03-27 "The Spring Lineup: Art. Drinks. Sun ☀️"; 2026-01-15 "We're coming for you, 2026 ✨" | 2026-10-15 |
| Vimeo (agency) — company voice | https://vimeo.com/thisjanuary | VERIFIED exists | unknown | not visible | not visible | "THIS JANUARY is a member of Vimeo"; location US; video list and counts not rendered logged out (also /videos) | 2026-10-15 |
| Linktree (agency) — company voice | https://linktr.ee/thisjanuary | VERIFIED exists | — | — | — | "This January Official: Instagram — Linktree"; "An independent agency building next year's brands"; one real link ("THIS JANUARY Email Forms"); the other items are Linktree's own ad placements | 2026-10-15 |

## Where a comment would be seen, where a post would land

She produces long-form on Medium (nine essays since 2016, the latest 2026-05-22, all articles and no responses in the feed) and on her own site, rebuilt in September 2026 with a notebook of side projects but no feed; X (@maggiewinters_, 5,816 posts, 989 followers) and TikTok (@maggiewinters_, 15 videos, 153 followers) are also hers and public, but neither page showed post dates logged out, so their cadence is unknown. The one place she was demonstrably active this week is Pinterest: 1,145 pins across 13 boards, the last saved 2026-10-13, with boards touched in June, July, September and October 2026 — consumption and curation, not publishing. Substack is a one-post shell (2025-08-01, no comments, no notes) that she uses to read eleven letters; Threads has 290 followers and has never carried a post; Behance (last 2019-01-19), Dribbble (last 2018-11-18) and YouTube (two uploads, 2011-02-08) are portfolio archives. Instagram @maggiewinters_ (linked from her site and her Substack), Facebook (lookitsmaggie) and Reddit could not be seen logged out, and Medium's profile tabs are bot-walled, so whether she comments or claps on Medium is unknown. LinkedIn is the lead's lane.

## Every URL opened

Instagram
- https://www.instagram.com/maggiewinters_/ · 200, WALL · logged-out shell ("PolarisLoggedOut"), no og meta
- https://www.instagram.com/moonstompmaggie/ · 200, WALL · same shell
- https://www.instagram.com/thisjanuary_/ · 200, WALL · same shell
- https://www.instagram.com/maggiewinters/ · 200, WALL · same shell (collision handle)
- https://www.instagram.com/{maggiewinters_,moonstompmaggie,thisjanuary_}/?__a=1&__d=dis · 201 · empty body

Threads
- https://www.threads.net/@maggiewinters_ → https://www.threads.com/@maggiewinters_ · 200 · curl: shell; WebFetch: "Maggie Winters", bio, 290 followers, "No threads yet"
- https://www.threads.net/@moonstompmaggie → threads.com · 200, WALL · login shell ("Threads • Log in", "Scan to get the app")
- https://www.threads.net/@thisjanuary_ → threads.com · 200 · title "ᴛʜɪs ᴊᴀɴᴜᴀʀʏ (@thisjanuary_) • Threads" only

TikTok
- https://www.tiktok.com/@maggiewinters_ · 200 · profile JSON: bio, counts, created 2021-05-31; no video list (curl and WebFetch)
- https://www.tiktok.com/@thisjanuary · 200 · profile JSON: agency bio, counts, created 2023-01-31
- https://www.tiktok.com/@moonstompmaggie · 200 (404-equivalent) · "Couldn't find this account", statusCode 10221
- https://www.tiktok.com/@maggiewinters · 200 · "Maggie Winters", empty bio, 4 followers, 0 videos

X
- https://syndication.twitter.com/srv/timeline-profile/screen-name/{moonstompmaggie,maggiewinters,thisjanuary,maggiewinters_,maggiegaudaen} · 429 on every attempt (three rounds with backoff; WebFetch returned an empty page)
- https://x.com/maggiewinters_ · 200 · JS shell
- https://x.com/moonstompmaggie · 200 · JS shell
- https://x.com/itsthisjanuary · 200 · JS shell
- https://x.com/maggiewinters · 404
- https://x.com/thisjanuary · 404
- https://twitter.com/moonstompmaggie · 200 → x.com shell
- https://publish.twitter.com/oembed?url=https://twitter.com/{moonstompmaggie,thisjanuary,maggiewinters} · empty body
- https://cdn.syndication.twimg.com/widgets/timelines/profile?screen_name=moonstompmaggie · 200 · empty
- https://api.fxtwitter.com/maggiewinters_ · 200 · profile fields (public mirror)
- https://api.fxtwitter.com/moonstompmaggie · 200 · profile fields (public mirror)
- https://api.fxtwitter.com/itsthisjanuary · 200 · profile fields (public mirror)
- https://api.fxtwitter.com/thisjanuary · 404 · "User not found"
- https://xcancel.com/maggiewinters_ · 451 · "XCancel service is suspended"
- https://nitter.net/maggiewinters_ · 200 · notice only: the project stopped after X Corp cease-and-desist letters of 2026-08-24 and 2026-09-08; no timeline
- https://nitter.privacydev.net/maggiewinters_ · connection failed

Substack
- https://substack.com/api/v1/user/maggiewintersmaggiewinters/public_profile · 200 · bio, links, 11 reads, 5 followers, dates
- https://maggiewintersmaggiewinters.substack.com/archive · 200
- https://maggiewintersmaggiewinters.substack.com/feed · 200 · one item, 2025-08-01
- https://maggiewintersmaggiewinters.substack.com/api/v1/archive?sort=new&search=&offset=0&limit=50 · 200 · 1 post, 0 comments, 0 reactions
- https://substack.com/@maggiewintersmaggiewinters · 200
- https://substack.com/api/v1/reader/feed/profile/10976040 · 200 · 1 item (the post)
- https://substack.com/@maggiewinters · 200 · a different, empty profile (see Maigret section)
- https://substack.com/api/v1/user/maggiewinters/public_profile · 200 · empty bio, 10 followers, set up 2023-08-01, no links

Medium
- https://medium.com/feed/@maggie-winters · 200 · 9 items with full text
- https://medium.com/@maggie-winters · 403 (curl and WebFetch)
- https://medium.com/@maggie-winters/about · 403
- https://medium.com/@maggie-winters/responses · 403 (curl and WebFetch)
- https://medium.com/@maggie-winters/lists · 403
- https://medium.com/@maggie-winters?format=json · 403
- https://maggie-winters.medium.com/ , /about , /responses , /lists · 403
- https://medium.com/@thisjanuary · 403 Cloudflare
- https://medium.com/@maggiewinters · 403 Cloudflare

Reddit
- https://www.reddit.com/user/{maggiewinters,moonstompmaggie,maggiewinters_,maggiegaudaen}/about.json · 403, WALL

Pinterest
- https://www.pinterest.com/maggiewinters/ · 200 · profile JSON: counts, 9 boards, last pin 2026-10-13
- https://www.pinterest.com/{moonstompmaggie,maggiewinters_,maggiegaudaen,thisjanuary}/ · 200 · "User not found"
- https://www.pinterest.com/popwedco/ · 200 · not parsed (defunct company handle)

Behance / Dribbble
- https://www.behance.net/maggiewinters · 200 · stats, links, one project (curl and WebFetch)
- https://dribbble.com/moonstompmaggie · 200 · 15 shots with dates
- https://dribbble.com/shots/5566060-Uterus-Invaders-Level-Up · 202 · empty body
- https://dribbble.com/shots/2194706-404-Page-ISL-co · 202 · empty body

YouTube
- https://www.youtube.com/@maggiewinters · 404
- https://www.youtube.com/@moonstompmaggie (+ /about, /videos) · 200 · 2 videos, joined 2011-02-08, 204 views
- https://www.youtube.com/@maggiewinters_ (+ /about, /videos) · 200 · empty channel "Maggie Winters", joined 2020-06-18
- https://www.youtube.com/@thisjanuary (+ /about, /videos) · 200 · empty channel "N", joined 2006-02-26
- https://www.youtube.com/@maggiegaudaen · 404
- https://www.youtube.com/@popwedco · 404
- https://www.youtube.com/watch?v=0DOISLsBTbo · 200 · "Final Flash Animation Maggie Winters", 2011-02-08, 16 views
- https://www.youtube.com/watch?v=l5STeTQTj30 · 200 · "Neutraface Animation.mov", 2011-02-08, 188 views
- https://www.youtube.com/watch?v=MV9dx0EfHMc · 200 · "Episode 8: PopWedCo", channel "Reel II Real with Coach Herb & B", 2020-08-15
- https://www.youtube.com/watch?v=ve3OWPEn7wE · 200 · channel "Unrivaled", 2026-09-16

Facebook
- https://www.facebook.com/{lookitsmaggie,maggiewinters,moonstompmaggie,maggie.winters,popwedco,thisjanuary,thisjanuary_,januarythird} · 400, WALL · "Error" page

Bluesky
- https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=maggiewinters.bsky.social · 200 · empty profile, 0 posts, created 2024-11-15
- same endpoint for moonstompmaggie.bsky.social, maggiewinters.com, thisjanuary.bsky.social, thisjanuary.com · 400 · "Profile not found"
- https://bsky.app/profile/maggiewinters.bsky.social · 200 · og:title is the handle only

Personal site and old domain
- https://maggiewinters.com/ · 200 · bio, "Recent Writing", links
- https://maggiewinters.com/about · 200 · bio text, Recognition
- https://maggiewinters.com/notebook · 200 · 8 notebook items
- https://maggiewinters.com/sitemap.xml · 200 · lastmod 2026-09-03 for /, /about, /notebook
- https://maggiewinters.com/{feed.xml,rss.xml,feed,rss,notebook/feed,atom.xml} · 404
- http://maggie.is/ · 301 → https://maggie.is/ · TLS connection fails; DNS on ISNIC forwarding

Podcasts and newsletters
- https://itunes.apple.com/search?media=podcast&entity=podcastEpisode&term=… for "Maggie Gaudaen", "Maggie Winters Gaudaen", "Maggie Winters This January", "This January agency", "Maggie Winters Pop Wed", "Reel II Real Maggie", plus description lookups for the ambiguous episodes · 200
- https://feeds.transistor.fm/story-podcast · 200 · 2018-07-12 episode
- https://feeds.megaphone.fm/CELCE8824969288 · 200 · episodes 23 (2024-10-02) and 24 (2024-10-16)
- https://podcasts.apple.com/us/podcast/wedding-design-with-maggie-steven/id1050697945?i=1000382995630 · 200 (WebFetch) · POP Wed Co., "Maggie and Stephen Gaudaen"
- https://us17.campaign-archive.com/feed?u=51d9f2bade0fed8148878b2c8&id=4529ad252e · 200 · last three issues dated

Maigret extras
- https://500px.com/p/moonstompmaggie and https://500px.com/moonstompmaggie · 200 · 3 KB JS shell, no profile fields, no "not found" text
- https://www.producthunt.com/@moonstompmaggie · 403, WALL · Cloudflare "Just a moment..."
- https://giphy.com/channel/maggiegaudaen · 200 · generic GIPHY page carrying 404 markers; no channel content; https://giphy.com/api/v4/channels/maggiegaudaen · 400
- https://vimeo.com/thisjanuary and /videos · 200 · member page; list not rendered
- https://linktr.ee/thisjanuary · 200 · agency Linktree

Web searches (search-only, LOW): "maggiewinters_" instagram · "moonstompmaggie" · "Maggie Winters" "This January" / "Pop Wed" / "January Third" with facebook/pinterest/youtube/threads/tiktok · "maggiewinters_" tiktok · "Maggie Winters" "This January" podcast 2025/2026 · "lookitsmaggie" / "human creative director" · "maggiewinters_" x.com. None returned a page for her handles; every query surfaced the Chicago comedian (Wikipedia: known online as @saggiesplinters).

## Open

- X: last post date and content for @maggiewinters_ (5,816 posts) and @itsthisjanuary (84). The public timeline endpoint answered 429 on every attempt, oEmbed came back empty, XCancel is suspended and Nitter has shut down; the mirror returns profile fields only. Whether her X bio ("partner + creative director") is simply stale is not stated anywhere on the page.
- Instagram @maggiewinters_: public or private, counts, last post — logged-out shell; search snippets returned nothing for the handle.
- Facebook lookitsmaggie: everything — HTTP 400 to a logged-out client.
- TikTok @maggiewinters_ and @thisjanuary: last video date — no video list renders logged out.
- Medium: follower count and whether she responds or claps on others' stories — profile tabs 403; the feed (long-form only, no responses among nine items) is the only read.
- Reddit: whether any of the four handles is hers — 403.
- Threads: whether @moonstompmaggie exists (login shell); bio and counts for @thisjanuary_.
- Pinterest: 4 of 13 boards did not render; INFERENCE, not seen on the page: "My Posh Closet" and "My Posh Picks" (both empty, created 2026-09-06) are the board names Poshmark's share-to-Pinterest feature creates.
- Dribbble follower and like counts; Behance projects beyond the one visible.
- YouTube @maggiewinters_ (empty, 2020) and Bluesky maggiewinters.bsky.social (empty, 2024): whether either is hers.
- Substack @maggiewinters (2023, empty bio, 10 followers): whether it is an earlier account of hers — her verified 2025 profile says "i'm new here".
- 500px moonstompmaggie (JS shell) and Product Hunt moonstompmaggie (Cloudflare wall): undetermined.

## Maigret hits triaged

maggiewinters_
- https://twitter.com/maggiewinters_ → VERIFIED-hers — mirror fields: "Maggie Winters", "partner + creative director @itsthisjanuary", Washington, DC, website maggie.is; her Behance links this handle. x.com itself: JS shell.
- https://www.threads.com/@maggiewinters_ → VERIFIED-hers — bio "building itsjanuarythird while we all figure it out"; 290 followers; 0 threads.
- https://www.tiktok.com/@maggiewinters_ → VERIFIED-hers — bio "cofounder @This January, obsessed with women's health…"; 15 videos, 153 followers.
- https://www.youtube.com/@maggiewinters_/about → LEAD — channel "Maggie Winters", joined 2020-06-18, no videos, no description, no links.

moonstompmaggie
- https://twitter.com/moonstompmaggie → VERIFIED-hers — mirror: "Maggie Winters Gaudaen", bio "The former internet home of @maggiewinters_", 0 posts.
- https://www.youtube.com/@moonstompmaggie/about → VERIFIED-hers — upload "Final Flash Animation Maggie Winters" (2011-02-08); 2 videos, 204 views.
- https://dribbble.com/moonstompmaggie → VERIFIED-hers — "Maggie Winters — building ➡️"; ISL-era shots 2014–2018; her Behance links it.
- https://500px.com/p/moonstompmaggie → WALL (undetermined) — 200 but a 3 KB JS shell with no profile fields and no "not found" text.
- https://www.producthunt.com/@moonstompmaggie → WALL — 403 Cloudflare "Just a moment...".

maggiegaudaen
- https://giphy.com/channel/maggiegaudaen → 404 — generic GIPHY page with 404 markers, no channel content; the channels API rejects the slug.

thisjanuary (agency)
- https://www.facebook.com/thisjanuary → WALL — HTTP 400 "Error".
- https://www.tiktok.com/@thisjanuary → VERIFIED-agency — "This January", "an independent creative agency → building next year's brands / washington, d.c.", 1,024 followers, 62 videos.
- https://www.youtube.com/@thisjanuary/about → not-the-agency — empty channel titled "N", joined 2006-02-26.
- https://medium.com/@thisjanuary → WALL — 403 Cloudflare.
- https://vimeo.com/thisjanuary → VERIFIED-agency — "THIS JANUARY is a member of Vimeo"; videos not rendered.
- https://linktr.ee/thisjanuary → VERIFIED-agency — "This January Official", "An independent agency building next year's brands".

maggiewinters (shared with the comedian)
- https://substack.com/@maggiewinters → LEAD — name "Maggie Winters", empty bio, no links, 10 followers, set up 2023-08-01; her own profile is @maggiewintersmaggiewinters.
- https://medium.com/@maggiewinters → WALL — 403; her Medium is @maggie-winters.
- https://www.tiktok.com/@maggiewinters → LEAD — "Maggie Winters", empty bio, 4 followers, 0 videos; her TikTok is @maggiewinters_. (Not the comedian either: she posts as @saggiesplinters.)
- https://www.behance.net/maggiewinters → VERIFIED-hers — "Partner + ECD", This January, Washington, DC; links maggie.is and dribbble.com/moonstompmaggie.
- https://bsky.app/profile/maggiewinters.bsky.social → LEAD — no name, no bio, 0 posts, created 2024-11-15.
- https://www.pinterest.com/maggiewinters/ → VERIFIED-hers — website maggie.is, "human creative director"; last pin saved 2026-10-13.
