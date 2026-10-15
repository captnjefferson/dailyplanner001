# Ryan Brickwood — platform pass (public pages, logged out, 2026-10-15)

Method and limits: every page below was fetched logged out with curl and a desktop user agent (plus YouTube RSS, X's public oEmbed and embed endpoints, the Apple Podcasts lookup API, Bluesky's public API, WebSearch); no browser, no login, no form, no LinkedIn page opened; the lead's Maigret reports (`maigret/`, 2026-10-15) were used only as pointers and every hit flagged for triage was opened here. Limits found today: Instagram, Threads and Facebook return the identical logged-out shell for every handle, including known-existing controls (`instagram.com/instagram/`, `threads.com/@instagram`, `facebook.com/facebook`), so those three can only be recorded WALL, never NOT FOUND; X's embed endpoint (`syndication.twitter.com/srv/timeline-profile/…`) answered HTTP 429 on five spaced attempts, so X accounts could be tested for existence (oEmbed) but not read; Reddit answered 403; Medium profile pages answered 403 (Cloudflare) but Medium RSS feeds are readable; WebSearch declined name+social-platform queries for a private person and DuckDuckGo's HTML endpoint returned a bot challenge (202). Profile photos of candidate accounts were downloaded and compared by eye with the Rea bio photo (https://reaadvisory.com/wp-content/uploads/2023/01/Ryan-Brickwood-2023-500x500-1.png).

## Matrix

| Platform | Handle / URL | Status (VERIFIED / LEAD / WALL / NOT FOUND) | Role (P producer / A participant / C consumer / D dormant / unknown) | Last activity seen | Audience size seen | What was visible, logged out | Checked |
|---|---|---|---|---|---|---|---|
| LinkedIn | linkedin.com/in/ryan-brickwood (slug from the person file) | lead's lane, not opened | — | — | — | — | 2026-10-15 |
| X | @ryanbrickwood, @RyanBrickwood, @ryan_brickwood → oEmbed 404 (no account). @brickwoodryan → oEmbed 200 (an account exists). @rbrickwood → oEmbed 200, display "RBRICKWOOD" | NOT FOUND for the three name handles; LEAD for @brickwoodryan (exists; name, bio and posts unread: embed endpoint HTTP 429 on every try); @rbrickwood is not him (see Maigret triage) | unknown | not seen | not seen | oEmbed returns only "Posts by brickwoodryan"; x.com/<handle> is a JS shell with no og meta | 2026-10-15 |
| Instagram | instagram.com/ryanbrickwood/, /ryan.brickwood/, /rbrickwood/, /brickwoodryan/ | WALL (HTTP 200 generic shell, no og meta; the control @instagram returns the same shell) | unknown | — | — | title "Instagram"; login/challenge shell | 2026-10-15 |
| Facebook | facebook.com/ryanbrickwood, /ryan.brickwood, m.facebook.com/ryanbrickwood, facebook.com/public/Ryan-Brickwood | WALL (HTTP 400 "Error" for all; control facebook.com/facebook also 400) | unknown | — | — | nothing | 2026-10-15 |
| TikTok | tiktok.com/@ryanbrickwood (id 7621310077156705301) | LEAD (page exists; identity unclear — no bio, no face; avatar is a photo of a white supercar) | unknown (if his, C: no videos) | none — 0 videos; account created 2026-03-25 (createTime 1774474557) | 0 followers / 0 following / 0 likes | nickname "ryanbrickwood", empty bio, region US, public, not verified | 2026-10-15 |
| Threads | threads.com/@ryanbrickwood, /@ryan.brickwood | WALL (generic "Threads" shell, no og meta; control @instagram same) | unknown | — | — | — | 2026-10-15 |
| YouTube | youtube.com/@RyanBrickwood (channel UCe1fWgyZMsPw-av1DkQ9LgQ) | VERIFIED — channel name "Ryan Brickwood"; its three videos are a youth player surnamed Brickwood at U.S. Soccer national ID camps in Lebanon OH, Carmel IN and Columbus OH, which fits the Wooster residence and "Coaching and watching my kids sports" on the Rea bio (https://reaadvisory.com/biography/ryan-brickwood/) | P (personal, minimal) / D — dormant since 2024-05-01 | 2024-05-01 (last upload, per RSS) | 3 subscribers; 3 videos; 199 total views (36 / 74 / 89) | joined 2024-01-03; no description; default letter avatar, no photo; uploads 2024-01-03, 2024-02-01, 2024-05-01 | 2026-10-15 |
| Substack | substack.com/@ryanbrickwood → redirects to substack.com/search/ryanbrickwood?searching=profile; that page lists no Brickwood profile | NOT FOUND | — | — | — | — | 2026-10-15 |
| Medium | medium.com/@ryanbrickwood (profile page 403 Cloudflare = WALL); medium.com/feed/@ryanbrickwood = "Stories by Ryan Brickwood on Medium", 0 items | LEAD (an account named Ryan Brickwood exists, no stories; identity unclear — feed avatar shows a young man with a young woman at an outdoor festival, does not resemble the Rea photo) | unknown (C at most) | none (empty feed; lastBuildDate is just the fetch time) | not seen | feed title and avatar only | 2026-10-15 |
| Reddit | reddit.com/user/ryanbrickwood/about.json, /user/rbrickwood/about.json | WALL (HTTP 403) | unknown | — | — | — | 2026-10-15 |
| Pinterest | pinterest.com/ryanbrickwood/ (uid 592082819669516062) | LEAD — name "Ryan Brickwood", country US, no bio, no location, no website; avatar is a photo of an England rugby player in kit (not a personal photo); boards "Animals", "Futuristic Motorcycle", "Mythical Creatures", "Projects to Try", "Stuff" — nothing tying it to Wooster, Rea, manufacturing or finance; og:url resolves to nz.pinterest.com | unknown (if his, C; last save 2021-06-28) | 2021-06-28 (last_pin_save_time) | 3 followers / 14 following / 60 pins / 5 boards | created 2020-04-08 | 2026-10-15 |
| Personal site / blog | ryanbrickwood.com, ryanbrickwood.net: no DNS. brickwood.com: a domain-sales page | NOT FOUND | — | — | — | — | 2026-10-15 |
| Podcast — guest | *Taking Stock with Koble* (Koble Systems), Ep. 005 "Using cost discipline to bless customers & improve profitability, with Ryan Brickwood", 2025-07-08 · Apple Podcasts https://podcasts.apple.com/us/podcast/using-cost-discipline-to-bless-customers-improve-profitability/id1812943368?i=1000716315069 · YouTube https://www.youtube.com/watch?v=4JLspkJWNHc (Koble Systems channel) · feed https://fast.wistia.com/channels/2e1d863w6h/rss | VERIFIED (episode title names him) | A (guest, once) | 2025-07-08 | 46 views on YouTube (48 min); the show has 12 episodes, last 2025-11-04 | — | 2026-10-15 |
| Podcast — host | none. Apple Podcasts episode search "Brickwood" returns 10 episodes, none his (other Brickwoods) | NOT FOUND | — | — | — | — | 2026-10-15 |
| Newsletter | *Plain & Simple*, Rea's quarterly print newsletter for Plain-community business owners; he signs the cover letter. Newest issue Aug–Oct 2026: Rea highlights page https://reaadvisory.com/insight/plain-simple-august-october-2026/ (200, names him); Joomag viewer https://viewer.joomag.com/plain-simple-august-october-2026/0325361001789412993 (200; JavaScript viewer, text not in the HTML) | VERIFIED | P (signer; firm-produced) | 2026-09-15 (issue post date on reaadvisory.com) | print circulation not public | — | 2026-10-15 |
| Print / bylines | *Plain & Simple* (print, above) and the Rea author archive https://reaadvisory.com/author/ryan-brickwood/ (200; 18 bylines Dec 2023 – Sep 2026 per the ledger in `ryan-brickwood-person.md` §2G) | VERIFIED | P | 2026-09-15 | — | — | 2026-10-15 |
| Other — Snapchat | snapchat.com/@ryanbrickwood (from /add/ryanbrickwood) | LEAD — public page "Ryan Brickwood is on Snapchat!", bitmoji avatar only, no bio, no stories visible; identity unclear | unknown | not shown | not shown | — | 2026-10-15 |
| Other — SoundCloud | soundcloud.com/ryan-brickwood | LEAD, probably not him — profile city "Silver Spring", US; 0 tracks, 0 followers, 0 following; last modified 2018-03-24 | — | 2018-03-24 | 0 | — | 2026-10-15 |
| Other — Bluesky | public search "Brickwood": 7 actors (Nolan Brickwood, Jonathan Brickwood, others), no Ryan | NOT FOUND | — | — | — | — | 2026-10-15 |
| Firm voice — Rea YouTube | youtube.com/@Rea-Advisory (UC_eV4nJToshDK5yNISpZH1w) | VERIFIED firm channel; he appears in "Spotlight Award 2023 \| Tim McDaniel Award for Innovation \| Ryan Brickwood" https://www.youtube.com/watch?v=Y7WE21f-VgQ (published 2025-02-13, 4:31, 5 views) and the channel carries "Rea Manufacturing Day \| Wooster, OH" https://www.youtube.com/watch?v=90WgNXdk94M (2025-10-31, 41 views) | A (subject of firm videos) | 2026-09-14 (channel's last upload) | 433 subscribers; 39 videos; 3,797 total views | joined 2011-09-26 | 2026-10-15 |
| Firm voice — Rea X | @ReaCPA (the `twitter:site` meta on reaadvisory.com pages; oEmbed 200) and @ReaAdvisory (oEmbed 200) | exists; timeline WALL (embed endpoint 429) | — | not seen | not seen | — | 2026-10-15 |
| Firm voice — Rea Facebook | facebook.com/reaadvisory and facebook.com/reacpa (both linked from the reaadvisory.com footer) | WALL (400) | — | — | — | — | 2026-10-15 |
| Firm voice — Rea Instagram / Threads | instagram.com/lifeatrea/ (footer link); threads.com/@lifeatrea | WALL (shell) | — | — | — | — | 2026-10-15 |
| Firm voice — Rea LinkedIn | linkedin.com/company/reaadvisory (footer link) | lead's lane, not opened | — | — | — | — | 2026-10-15 |
| Firm voice — Rea podcast | *unsuitable on Rea Radio*, Apple Podcasts id1032387000 (213 episodes, last 2021-11-01); feed https://feeds.captivate.fm/unsuitable/ (200; 0 mentions of Brickwood) | firm show, dormant since 2021-11-01; no episode with him | — | 2021-11-01 | — | — | 2026-10-15 |
| Firm voice — Rea bio page | https://reaadvisory.com/biography/ryan-brickwood/ | VERIFIED (200) | — | — | — | the page links only the firm's Facebook, Instagram and LinkedIn; no personal handle of his anywhere on it | 2026-10-15 |

## Where a comment would be seen, where a post would land

He produces nothing in public outside firm channels: the one personal account that is certainly his, the YouTube channel, holds three family soccer-camp videos, has 3 subscribers and has been dormant since May 2024. His visible output is firm-made or firm-hosted — the Rea bylines, the signed *Plain & Simple* letters, the Rea award video (5 views), one Koble podcast episode (46 views on YouTube) — and, per the person file, LinkedIn is the only place he posts and reacts in his own name (not opened here). The accounts that carry his name on TikTok (created March 2026, empty), Medium, Pinterest and Snapchat show nothing that confirms they are his, and the Pinterest and Medium avatars belong to other people. On X there is no @ryanbrickwood; @brickwoodryan exists but could not be read today. Instagram, Facebook, Threads and Reddit could not be seen logged out, so whether he consumes there is unknown. A public comment on any video that features him would be seen in rooms of single- to double-digit views; nothing found on this pass is a place where he posts.

## Every URL opened

- https://www.instagram.com/ryanbrickwood/ · 200, WALL shell · title "Instagram", no og meta
- https://www.instagram.com/ryan.brickwood/ · 200, WALL shell · same
- https://www.instagram.com/rbrickwood/ · 200, WALL shell · same
- https://www.instagram.com/brickwoodryan/ · 200, WALL shell · same
- https://www.instagram.com/instagram/ (control) · 200, same shell · proves the shell is not a "not found" signal
- https://www.facebook.com/ryanbrickwood · 400 · "Error"
- https://www.facebook.com/ryan.brickwood · 400 · "Error"
- https://m.facebook.com/ryanbrickwood · 400 (redirects to www.facebook.com/ryanbrickwood?_rdr) · "Error"
- https://www.facebook.com/public/Ryan-Brickwood · 400 · "Error"
- https://www.facebook.com/facebook (control) · 400 · proves 400 is the wall, not absence
- https://www.threads.net/@ryanbrickwood → https://www.threads.com/@ryanbrickwood · 200, WALL shell · title "Threads", no og meta
- https://www.threads.net/@ryan.brickwood → threads.com · 200, WALL shell
- https://www.threads.com/@instagram (control) · 200, same shell
- https://syndication.twitter.com/srv/timeline-profile/screen-name/ryanbrickwood · 429 on four spaced attempts · "Rate limit exceeded"
- https://syndication.twitter.com/srv/timeline-profile/screen-name/ryan_brickwood · 429 · same
- https://syndication.twitter.com/srv/timeline-profile/screen-name/brickwoodryan · 429 (three attempts) · same
- https://syndication.twitter.com/srv/timeline-profile/screen-name/rbrickwood · 429 · same
- https://syndication.twitter.com/srv/timeline-profile/screen-name/ReaCPA · 429 · same
- https://syndication.twitter.com/srv/timeline-profile/screen-name/reaadvisory · 429 · same
- https://publish.twitter.com/oembed?url=https://twitter.com/ryanbrickwood (→ publish.x.com) · 404 · no account
- https://publish.twitter.com/oembed?url=https://twitter.com/RyanBrickwood · 404 · no account
- https://publish.twitter.com/oembed?url=https://twitter.com/ryan_brickwood · 404 · no account
- https://publish.twitter.com/oembed?url=https://twitter.com/brickwoodryan · 200 · "Posts by brickwoodryan" (exists; nothing else)
- https://publish.twitter.com/oembed?url=https://twitter.com/rbrickwood · 200 · "Posts by RBRICKWOOD"
- https://publish.twitter.com/oembed?url=https://twitter.com/ReaCPA · 200 · "Posts by ReaCPA"
- https://publish.twitter.com/oembed?url=https://twitter.com/reaadvisory · 200 · "Posts by ReaAdvisory"
- https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=… · 200, empty body · endpoint is dead
- https://www.tiktok.com/@ryanbrickwood · 200 · embedded state: uniqueId ryanbrickwood, 0/0/0, created 2026-03-25, region US; avatar = supercar photo
- https://www.tiktok.com/@tiktok (control) · 200 · state present, so TikTok pages are readable logged out
- https://www.pinterest.com/ryanbrickwood/ · 200 · og:title "Ryan Brickwood (ryanbrickwood) - Profile | Pinterest"; 3 followers, 14 following, 60 pins, 5 boards, created 2020-04-08, last save 2021-06-28
- https://i.pinimg.com/280x280_RS/bc/2c/48/bc2c48cd736a19dac058a57a2cd4cdca.jpg · 200 · Pinterest avatar: an England rugby player in kit
- https://medium.com/@ryanbrickwood · 403 · Cloudflare "Attention Required" (WALL)
- https://medium.com/feed/@ryanbrickwood · 200 · "Stories by Ryan Brickwood on Medium", 0 items
- https://cdn-images-1.medium.com/fit/c/150/150/0*cdLu6OG0QV8ZbIdD. · 200 · Medium avatar: young man and young woman at an outdoor festival
- https://substack.com/@ryanbrickwood · 200 → redirect to https://substack.com/search/ryanbrickwood?searching=profile · no Brickwood profile listed
- https://www.reddit.com/user/ryanbrickwood/about.json · 403 · WALL
- https://www.reddit.com/user/rbrickwood/about.json · 403 · WALL
- https://soundcloud.com/ryan-brickwood · 200 · "Ryan Brickwood", city Silver Spring, US, 0 tracks, last modified 2018-03-24
- https://www.snapchat.com/add/ryanbrickwood → https://www.snapchat.com/@ryanbrickwood · 200 · "Ryan Brickwood is on Snapchat!", bitmoji only
- https://www.snapchat.com/add/rbrickwood → /@rbrickwood · 200 · display name "rileyyy"
- https://www.youtube.com/feeds/videos.xml?channel_id=UCe1fWgyZMsPw-av1DkQ9LgQ · 200 · author "Ryan Brickwood"; 3 entries dated 2024-01-03, 2024-02-01, 2024-05-01
- https://www.youtube.com/@RyanBrickwood/about · 200 · "Ryan Brickwood", 3 subscribers, 3 videos, 199 views, joined 2024-01-03, no description
- https://yt3.googleusercontent.com/ytc/AIdro_nhoOi8Lhcr7w0l0Ur6N0ern1n6gqe49p8sDZDsXjKezsAllwS3frRAi1p45L_qVDrCfQ=s240-c-k-c0x00ffffff-no-rj · 200 · YouTube avatar: default letter "R", no photo
- https://www.youtube.com/@rbrickwood/about · 200 · "Roger Brickwood" (UCoj61pvzrGIz0hhGNxIW3ag)
- https://www.youtube.com/results?search_query=%22Ryan+Brickwood%22 · 200 · five videos: the Koble episode, the Rea award video, and his three camp videos; nothing else
- https://www.youtube.com/watch?v=4JLspkJWNHc · 200 · Koble Systems channel, published 2025-07-08, 2,879 s, 46 views
- https://www.youtube.com/watch?v=Y7WE21f-VgQ · 200 · Rea channel, published 2025-02-13, 271 s, 5 views
- https://www.youtube.com/@Rea-Advisory/about · 200 · "Rea", 433 subscribers, 39 videos, 3,797 views, joined 2011-09-26
- https://www.youtube.com/feeds/videos.xml?channel_id=UC_eV4nJToshDK5yNISpZH1w · 200 · last 15 uploads (2025-04-10 … 2026-09-14), incl. "Rea Manufacturing Day | Wooster, OH" 2025-10-31
- https://itunes.apple.com/search?term=Taking+Stock+with+Koble&entity=podcast · 200 · one show, id1812943368, 12 episodes
- https://itunes.apple.com/lookup?id=1812943368&entity=podcastEpisode · 200 · Ep. 005 with him, 2025-07-08; feed URL
- https://podcasts.apple.com/us/podcast/using-cost-discipline-to-bless-customers-improve-profitability/id1812943368?i=1000716315069 · 200 · episode page
- https://itunes.apple.com/search?term=Brickwood&entity=podcastEpisode · 200 · 10 episodes, none his
- https://itunes.apple.com/search?term=unsuitable+Rea+Radio&entity=podcast · 200 · id1032387000, 213 episodes, last 2021-11-01
- https://itunes.apple.com/lookup?id=1032387000 · 200 · feed URL
- https://feeds.captivate.fm/unsuitable/ · 200 · 7 items in the live feed, 0 "Brickwood"
- https://reaadvisory.com/ · 200 · footer links: facebook.com/reaadvisory, facebook.com/reacpa, instagram.com/lifeatrea, linkedin.com/company/reaadvisory, youtube.com/@Rea-Advisory; no X link
- https://reaadvisory.com/biography/ryan-brickwood/ · 200 · bio; `twitter:site` meta @ReaCPA; no personal handles; photo URL above
- https://reaadvisory.com/author/ryan-brickwood/ · 200 · "Ryan Brickwood, Author at Rea Business Advisors"
- https://reaadvisory.com/insight/plain-simple-august-october-2026/ · 200 · names him
- https://viewer.joomag.com/plain-simple-august-october-2026/0325361001789412993 · 200 · JS viewer, text not in HTML
- https://reaadvisory.com/insight/manufacturing-days-2026/ · 200 · names him
- https://www.acg.org/columbus/events/acg-columbus-2026-aerospace-defense-dealmaking-investment-summit · 200 · names him once
- https://www.facebook.com/reaadvisory · 400 · WALL
- https://www.facebook.com/reacpa · 400 · WALL
- https://www.instagram.com/lifeatrea/ · 200, WALL shell
- https://www.threads.com/@lifeatrea · 200, WALL shell
- https://public.api.bsky.app/xrpc/app.bsky.actor.searchActors?q=Brickwood&limit=25 · 200 · 7 actors, no Ryan
- https://html.duckduckgo.com/html/?q=%22Ryan+Brickwood%22 (and two variants) · 202 · bot challenge, WALL
- https://brickwood.com/ · 200 · domain-sales page, unrelated
- ryanbrickwood.com, ryanbrickwood.net · no DNS record
- WebSearch: `"Ryan Brickwood" Wooster Ohio` (no hit on him); `"Ryan Brickwood" (instagram OR facebook OR twitter OR x.com OR tiktok OR threads)` (no hit); `"Ryan Brickwood" Rea` (no hit); `"Ryan Brickwood" twitter OR facebook OR instagram` (the tool declined the query); `"Brickwood" "Rea & Associates" OR "Rea Business Advisors" OR reaadvisory manufacturing` (hits: https://reaadvisory.com/?p=156578 and https://www.reacpa.com/biography/ryan-brickwood — his firm bio only; no social profile in any snippet)

## Maigret hits triaged

Each hit from the lead's Maigret run opened logged out; fixya/joyreactor/pling skipped as noise.

- ryanbrickwood → https://www.tiktok.com/@RyanBrickwood (serves @ryanbrickwood): **LEAD** — exists, empty (0 videos, 0 followers), created 2026-03-25, no bio; avatar is a supercar photo, no face.
- ryanbrickwood → https://medium.com/@RyanBrickwood: profile page **WALL** (Cloudflare 403); the RSS feed shows an account "Ryan Brickwood" with 0 stories → **LEAD**; the feed avatar (young man at a festival) does not resemble the Rea bio photo.
- ryanbrickwood → YouTube @RyanBrickwood: already known; **VERIFIED-his** (matrix).
- ryanbrickwood → https://www.pinterest.com/ryanbrickwood/ (Maigret extra): **LEAD** — name match only; England-rugby-player avatar; boards on animals, motorcycles, mythical creatures; last save 2021-06-28.
- ryanbrickwood → https://www.snapchat.com/add/ryanbrickwood (Maigret extra): **LEAD** — "Ryan Brickwood is on Snapchat!", bitmoji only.
- rbrickwood → https://twitter.com/rbrickwood: **not-him** — oEmbed shows display "RBRICKWOOD"; Maigret's extractor read the profile name as "ROGER BRICKWOOD" (created 2009-03-27, 1 follower, default avatar); timeline unreadable today (429).
- rbrickwood → https://www.youtube.com/@rbrickwood/about: **not-him** — channel "Roger Brickwood".
- rbrickwood → https://www.snapchat.com/add/rbrickwood: **not-him** — display name "rileyyy".
- ryan-brickwood → https://soundcloud.com/ryan-brickwood: **LEAD, probably not him** — city Silver Spring, US; 0 tracks; last modified 2018-03-24 (he was in Ohio then, per the Rea bio and the person file).

## Open

- X @brickwoodryan: exists (oEmbed 200) but its name, bio and posts could not be read; X's embed endpoint was rate-limited for the whole session.
- Instagram, Facebook, Threads: whether any account of his exists is unknown; all three wall logged-out curl, even for known accounts.
- Reddit: 403 to the about.json endpoint; no finding either way.
- TikTok, Medium, Pinterest, Snapchat "Ryan Brickwood": no bio, caption or photo ties them to him; the Pinterest and Medium avatars point to other people; the TikTok account (created March 2026, empty) could be anyone.
- *Plain & Simple* print circulation: not public.
- Search coverage: WebSearch declines name+platform queries for a private person; DuckDuckGo's HTML endpoint blocks curl; so no search-snippet evidence (including any LinkedIn snippet) was gathered on this pass.
