# Chris Mangano — platform pass (public pages, logged out, 2026-10-15)

Method: curl with a desktop user agent (og: meta, embedded page JSON, public feeds and oEmbed endpoints), WebFetch, WebSearch, the iTunes Search API and YouTube's public feeds and search pages; no browser, no login, no wall crossed, no LinkedIn page opened. Limits: X's public timeline endpoint rate-limited every call (HTTP 429) for the whole pass, so X existence was confirmed through the publish.twitter.com oEmbed endpoint only (200 = account exists, 404 = none) and no X bio, photo or post was seen; Medium and Reddit are bot-walled; Facebook returns an error page to curl and only a page title to WebFetch; Instagram and Threads were readable through WebFetch but not curl; one WebSearch query (name + employer + home area) was refused by the search tool, so searches were name + platform only.

## Matrix

| Platform | Handle / URL | Status | Role | Last activity seen | Audience size seen | What was visible, logged out | Checked |
|---|---|---|---|---|---|---|---|
| LinkedIn | lead's lane, not opened | — | — | — | — | — | 2026-10-15 |
| X | https://twitter.com/chrisnmangano (handle identical to his LinkedIn slug) | LEAD (account exists; identity not confirmed on the page) | unknown | not visible (timeline endpoint 429) | not visible | oEmbed returns a timeline embed "Posts by chrisnmangano" (HTTP 200; non-existent handles return 404). No bio, photo, post or counts could be seen. Three other handles also exist on X and are identity-unknown: chrismangano ("Posts by ChrisMangano"), cmangano ("CMANGANO"), manganochris ("ManganoChris"). x.com profile pages return a JS shell with no og: meta. | 2026-10-15 |
| Instagram | instagram.com/chrisnmangano/, /manganochris/ | NOT FOUND (Instagram shell, no profile data) | — | — | — | Shell page only; no og: meta, no profile header, for either handle. | 2026-10-15 |
| Instagram | instagram.com/chrismangano/ | LEAD (empty) | unknown | none (no posts) | 0 followers / 0 following | Display name "Chris Mangano", no bio, no posts, no link. Nothing identifies the account holder. | 2026-10-15 |
| Instagram | instagram.com/chris.mangano/ | not him (collision) | — | — | 1,593 followers / 1,528 following | Private profile; bio "It's a classic rope-a-dope" + "Bucknell \| NYC". A Bucknell/NYC tag does not fit a Rider University graduate in Bucks County. | 2026-10-15 |
| Instagram | instagram.com/cmangano/ | not him (collision) | — | — | 0 / 1 | Display name "Carol". | 2026-10-15 |
| Facebook | no handle known; facebook.com/chrisnmangano, /chris.mangano, /chrismangano | NOT FOUND / WALL | — | — | — | curl: HTTP 400 "Sorry, something went wrong" error page for every facebook.com URL. WebFetch: title "Facebook" only (no profile) for all three. | 2026-10-15 |
| Facebook | facebook.com/manganochris | LEAD (identity unclear) | unknown | not visible | not visible | WebFetch title: "Mangano Chris (@mangano.chris) • Facebook" — a person profile exists under the reversed name; nothing else visible. | 2026-10-15 |
| TikTok | tiktok.com/@chrisnmangano, /@manganochris | NOT FOUND | — | — | — | "Couldn't find this account" in the page data. | 2026-10-15 |
| TikTok | tiktok.com/@chrismangano; /@chris.mangano | LEAD (empty) | unknown | none | 0 followers, 0 videos (both) | Nicknames "Chris" and "chris.mangano"; no bio, no videos. | 2026-10-15 |
| TikTok | tiktok.com/@cmangano | LEAD (identity unclear) | unknown | not visible | 14 followers, 18 videos | Default nickname "user6890608549951", no bio; video list not in the logged-out page data. | 2026-10-15 |
| Threads | threads.com/@chrisnmangano; threads.com/@chrismangano | WALL | — | — | — | Login page only ("Threads • Log in"). threads.net is not fetchable by WebFetch; threads.com was used. | 2026-10-15 |
| Threads | threads.com/@chris.mangano | not him (collision) | — | 2025-08-08 | 152 followers | Partially public: display name "Chris Mangano", latest post 08/08/25 "60 years of marriage, 3 children, 8 grandchildren, and they never had a fight". Same handle as the Bucknell/NYC Instagram account (Threads profiles are Instagram accounts). | 2026-10-15 |
| YouTube | youtube.com/@chrismangano (UCSTSsALcRovDSHSwB6rHJtQ) | not him (the fitness coach) | — | 2023-01-21 | 1.82K subscribers, 5 videos, 76,156 views | Joined 2013-11-12; uploads "Follow This To Burn Fat!", "TRUE BODY FAT PERCENTAGE EXAMPLES", "LEAN MUSCLE VS BULKY MUSCLE". | 2026-10-15 |
| YouTube | youtube.com/@cmangano (UCLA73U-SBxp3o7DvkHfqbHw) | not him (the fitness coach) | — | 2011-12-30 | 3 subscribers, 33 videos | Joined 2006-09-26; "ChrisManganoFitness.com Maria Training Montage", kettlebell and sled videos. | 2026-10-15 |
| YouTube | youtube.com/@chrisnmangano, /@manganochris | NOT FOUND | — | — | — | HTTP 404. No channel of his own found. | 2026-10-15 |
| Substack | https://substack.com/@chrismangano | LEAD (identity unclear) | C consumer at most | profile set up 2024-11-10; no posts | "See subscribers" (count hidden) | Public profile API: name "Chris Mangano", empty bio, no publication, 5 subscriptions (BOK & Anne on Ads, Love letters to literature, Lovely Thoughts, Sustainable AI, Written in Brooklyn). Nothing ties it to him. | 2026-10-15 |
| Substack | substack.com/@chrisnmangano, /@manganochris; /@cmangano | NOT FOUND; not him | — | — | — | First two resolve to a Substack search page (no profile). @cmangano is "Cassandra Mangano". | 2026-10-15 |
| Medium | medium.com/@chrisnmangano, /@chrismangano, /@cmangano, /@manganochris, /@chris.mangano | WALL | — | — | — | Cloudflare "Attention Required" (HTTP 403) on curl; HTTP 403 on WebFetch. | 2026-10-15 |
| Reddit | reddit.com/user/chrisnmangano/about.json, /user/chrismangano/about.json | WALL | — | — | — | HTTP 403 "blocked … network security". | 2026-10-15 |
| Pinterest | pinterest.com/chrismangano/ | LEAD (identity unclear; dormant if his) | D dormant | 2013-09-20 (last pin saved) | 0 followers, 1 pin, 1 board | Name "Chris Mangano", no bio, no website. | 2026-10-15 |
| Pinterest | pinterest.com/cmangano/, /manganochris/, /chrisnmangano/ | not him; not him; NOT FOUND | — | — | — | "Christina (cmangano)"; "Christine Buliano Mangano (manganochris)"; chrisnmangano has no profile (empty title). | 2026-10-15 |
| Personal site / blog | chrismangano.com; chrisnmangano.com; manganochris.com; chrismangano.net | NOT FOUND (not his) | — | — | — | chrismangano.com (HTTPS fails; HTTP) forwards to linkedin.com/in/chrismangano, a slug that is not his (his is chrisnmangano); LinkedIn answered the automatic redirect with HTTP 999 and no content was received. The other three domains have no DNS A record. The "Visit my website" link on his LinkedIn (seed) remains an unknown URL. | 2026-10-15 |
| Podcast (host / guest) | iTunes Search API, "Chris Mangano" and "Mangano Withum" | NOT FOUND | — | — | — | Hits are collisions: Fit Over 40 (fitness coach, 2020), Kentucky Call Sheet #10 (filmmaker, 2023-05-24, https://podcasts.apple.com/us/podcast/kentucky-call-sheet-10-max-neace-chris-mangano/id1649704105?i=1000614532021), Vin & Mike Ep. 11 (2022-03-29, a sports guest "Chris Mangano", Packers and NY Rangers; nothing ties it to him). Rainmakers Roundup exists as a podcast (https://podcasts.apple.com/us/podcast/rainmakers-roundup/id1719793302, 32 episodes 2023–2024, Spreaker feed): no Mangano episode; his appearances were on the TV/YouTube version. Withum's seven Apple-listed podcasts (Sounding Board, Civic Warriors, Cryptonomix, Take Me to the Cloud, The Capital Table, Founded in Tech, Taxing Topics): no episode with his name in the index. | 2026-10-15 |
| Newsletter | — | NOT FOUND | — | — | — | No newsletter of his own. Withum's "Cyber Matters: Edition 1" (https://www.withum.com/resources/cyber-matters-edition-1/, 2026-09-30) is a written digest by Edward Keck, Jr.; his name does not appear on it. | 2026-10-15 |
| TV / video produced by others | NJBIA "Minding Your Business – October 3, 2026", https://www.youtube.com/watch?v=Pces4eo4xeg (channel NJBIA, uploaded 2026-10-05); article https://njbia.org/withums-mangano-talks-new-cybersecurity-risks-through-ai-deep-fakes/ | VERIFIED | A participant | 2026-10-05 | NJBIA's channel (count not captured) | Title and channel confirmed by oEmbed and the watch page; his segment per the earlier read runs 14:16–29:40. | 2026-10-15 |
| TV / video produced by others | Rainmakers Roundup (RVN TV), on Mark Iorio's channel https://www.youtube.com/@markiorio5555: https://www.youtube.com/watch?v=QyEvu54AhpQ "Rainmakers Roundup Chris Mangano Mercadien Technologies" (uploaded 2019-06-21); https://www.youtube.com/watch?v=pddNJZ8kn3E "Rainmakers Roundup with Chris Mangano VP Sales/Marketing Ocellus Tech" (2020-09-11) | VERIFIED | A participant | 2020-09-11 | — | Titles name him; owner "Mark Iorio". The 2017 episode (o4cpdNO8cps) is unavailable (oEmbed and watch page return nothing). | 2026-10-15 |
| TV / video produced by others | Ocellus Tech channel https://www.youtube.com/@ocellustech6701: "Ocellus Tech on Rainmakers Roundup – Part 1" https://www.youtube.com/watch?v=RFatjFNVOWg and "– Part 2" https://www.youtube.com/watch?v=-CVaPVlAsmE (both 2020-09-15) | VERIFIED | A participant | 2020-09-15 | — | Cuts of the Sep 2020 episode, posted by his then employer. | 2026-10-15 |
| Company voice (Withum) | YouTube https://www.youtube.com/@WithumVids (listed in withum.com footer as /user/WithumVids) | VERIFIED company voice; he is NOT on it | — | — | 1.2K subscribers, 929 videos, 619,873 views, joined 2011-10-03 | Channel search "Mangano" returns 0 videos; YouTube-wide searches for "Chris Mangano" Withum / cybersecurity / Mercadien return only the NJBIA and Rainmakers videos above. | 2026-10-15 |
| Company voice (Withum) | X https://twitter.com/withumCPA; Facebook https://www.facebook.com/WithumSmithBrown; Instagram https://www.instagram.com/withumcpa (all from the withum.com footer) | LEAD (exist; not opened beyond existence) | — | — | — | X account exists per oEmbed ("Posts by WithumCPA"); Facebook and Instagram handles taken from the site footer, pages not opened. These are the firm's accounts, not his. | 2026-10-15 |

Role codes: P producer, A participant, C consumer, D dormant.

## Where a comment would be seen, where a post would land

On the public web he does not produce anywhere outside LinkedIn (lead's lane) and withum.com bylines: no YouTube channel, no podcast, no newsletter, no personal site, no Substack or Medium writing, and no Instagram, TikTok, Threads or Pinterest account that can be tied to him. The one strong lead is X: the handle chrisnmangano, identical to his LinkedIn slug, exists, but its bio and timeline could not be seen this pass, so whether it is active, dormant or empty is unknown. Where he does appear is on video produced by others, as a guest: NJBIA's Minding Your Business (uploaded 2026-10-05) and the Rainmakers Roundup episodes on Mark Iorio's and Ocellus Tech's channels (2019–2020); comments under those videos land on other people's channels. Instagram and Threads turned up only empty or collision accounts (a Bucknell/NYC Chris Mangano, a fitness coach on YouTube, a Carol and a Cassandra on cmangano). Medium and Reddit were bot-walled and Facebook unreadable, so a presence there can be neither confirmed nor ruled out.

## Maigret hits triaged

- chrisnmangano → https://twitter.com/chrisnmangano · **LEAD** · account exists (oEmbed 200, "Posts by chrisnmangano"); handle matches his LinkedIn slug; bio/photo/posts not viewable (timeline endpoint HTTP 429 on every attempt). The strongest lead of the pass.
- chris.mangano → https://medium.com/@chris.mangano · **WALL** · Cloudflare 403 (curl and WebFetch).
- chris.mangano → https://www.tiktok.com/@chris.mangano · **LEAD (empty)** · nickname "chris.mangano", 0 followers, 0 videos, no bio.
- chris.mangano → https://www.threads.com/@chris.mangano · **not-him** · 152 followers, last post 2025-08-08 (a family anniversary post); same handle as the private Instagram account whose bio reads "Bucknell | NYC".
- manganochris → https://twitter.com/manganochris · **LEAD** · exists ("Posts by ManganoChris"); nothing else visible.
- manganochris → https://www.facebook.com/manganochris · **LEAD** · WebFetch title "Mangano Chris (@mangano.chris) • Facebook"; a person profile under the reversed name; no visible text.
- manganochris → https://www.pinterest.com/manganochris/ · **not-him** · profile "Christine Buliano Mangano (manganochris)".
- chrismangano → https://substack.com/@chrismangano · **LEAD** · "Chris Mangano", no bio, no publication, set up 2024-11-10, five unrelated subscriptions (ads, literature, Brooklyn, "Sustainable AI").
- chrismangano → https://twitter.com/chrismangano · **LEAD** · exists ("Posts by ChrisMangano"); nothing else visible.
- chrismangano → https://www.youtube.com/@chrismangano/about · **not-him (the fitness coach)** · 1.82K subscribers, 5 fat-loss/body-fat videos, last upload 2023-01-21.
- chrismangano → https://www.tiktok.com/@chrismangano · **LEAD (empty)** · nickname "Chris", 0 followers, 0 videos.
- cmangano → https://twitter.com/cmangano · **LEAD** · exists ("Posts by CMANGANO"); nothing else visible.
- cmangano → https://substack.com/@cmangano · **not-him** · "Cassandra Mangano".
- cmangano → https://www.youtube.com/@cmangano/about · **not-him (the fitness coach)** · "CMangano", 33 videos from 2011 including "ChrisManganoFitness.com Maria Training Montage".
- cmangano → https://www.tiktok.com/@cmangano · **LEAD (identity unclear)** · default nickname "user6890608549951", 14 followers, 18 videos, no bio; WebFetch sees only the TikTok title.
- cmangano → https://linktr.ee/cmangano · **not-him** · page title "Carol Mangano", bio "Creative mind on a journey".
- cmangano → https://bsky.app/profile/cmangano.bsky.social (also in the Maigret list) · **LEAD (empty)** · exists, no display name, no bio, 18 followers, 0 posts, created 2025-04-09.
- Not checked: joyreactor, Pling, Calendly, Codepen, Pbase, Snapchat, Google Scholar, Vivino, picturepush, Chatujme, Tistory, Lobsters, Salon24, Upwork, Giphy, Disqus, Myspace, WordPress.org, PayPal, Chess, Duolingo, Untappd, Letterboxd, Wattpad, Freesound, Picsart, Clubhouse, Periscope, Smule, Academia, GitHub, Weebly, SoundCloud, MixCloud, Bandcamp, Genius, TripAdvisor, Twitch, GOG, LibraryThing, Lichess, MyMiniFactory, VSCO, Venmo, Memrise, Revolut, Gist — outside the platform matrix; Maigret's "exists" on these is usually a shared-handle false positive.

## Every URL opened

- https://www.instagram.com/chrisnmangano/ · curl 200, shell only (no og: meta) · WebFetch: "Instagram" and two images, no profile data.
- https://www.instagram.com/chrismangano/ · curl shell · WebFetch 200 · "Chris Mangano", 0/0, no posts.
- https://www.instagram.com/cmangano/ · WebFetch 200 · "Carol", 0/1.
- https://www.instagram.com/chris.mangano/ · WebFetch 200 (private) · "Chris Mangano", "It's a classic rope-a-dope", "Bucknell | NYC", 1,593/1,528.
- https://www.instagram.com/manganochris/ · curl shell · WebFetch: no profile data.
- https://syndication.twitter.com/srv/timeline-profile/screen-name/{chrisnmangano,chrismangano,cmangano,manganochris,chris_mangano} · HTTP 429 "Rate limit exceeded" on every attempt (first batch, a 10-call slow retry over ~5 minutes, and a final attempt).
- https://publish.twitter.com/oembed?url=https://twitter.com/{chrisnmangano,chrismangano,cmangano,manganochris,withumCPA} · 301 → publish.x.com · 200 JSON, "Posts by …" (accounts exist).
- https://x.com/chrisnmangano · 200 · JS shell, no title or og: meta.
- https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=… · 200, empty body (endpoint dead).
- https://www.facebook.com/{chrisnmangano,chris.mangano,chrismangano,cmangano} · curl HTTP 400 error page ("Sorry, something went wrong") · WebFetch title "Facebook" only (first three).
- https://www.facebook.com/manganochris · WebFetch title "Mangano Chris (@mangano.chris) • Facebook, Connect with friends".
- https://www.tiktok.com/@{chrisnmangano,chrismangano,cmangano,manganochris,chris.mangano} · 200 · embedded JSON as recorded in the matrix.
- https://www.threads.net/@{chrisnmangano,chrismangano,cmangano} · curl 200 → threads.com shell, no og: meta · WebFetch cannot fetch threads.net.
- https://www.threads.com/@chrismangano · WebFetch: login page.
- https://www.threads.com/@chris.mangano · WebFetch: partial profile, 152 followers, post of 08/08/25.
- https://www.youtube.com/@chrismangano and /about · 200 · fitness channel; feed https://www.youtube.com/feeds/videos.xml?channel_id=UCSTSsALcRovDSHSwB6rHJtQ · last upload 2023-01-21.
- https://www.youtube.com/@cmangano and /about · 200 · ChrisManganoFitness; feed …channel_id=UCLA73U-SBxp3o7DvkHfqbHw · last upload 2011-12-30.
- https://www.youtube.com/@chrisnmangano · 404 · https://www.youtube.com/@manganochris · 404.
- https://www.youtube.com/results?search_query= "Chris Mangano" Withum / "Chris Mangano" cybersecurity / "Mangano" Rainmakers Roundup / "Chris Mangano" Mercadien · 200 · only Pces4eo4xeg, QyEvu54AhpQ, pddNJZ8kn3E, RFatjFNVOWg, -CVaPVlAsmE (plus two unrelated Manganos).
- https://www.youtube.com/oembed?url=…{Pces4eo4xeg,QyEvu54AhpQ,pddNJZ8kn3E,RFatjFNVOWg,-CVaPVlAsmE} · 200 · titles and channels as in the matrix · o4cpdNO8cps · oEmbed unavailable.
- https://www.youtube.com/watch?v={Pces4eo4xeg,QyEvu54AhpQ,pddNJZ8kn3E,RFatjFNVOWg,-CVaPVlAsmE,o4cpdNO8cps} · 200 · publishDate/ownerChannelName as in the matrix (o4cpdNO8cps: none).
- https://www.youtube.com/user/WithumVids/about and https://www.youtube.com/@WithumVids/about · 200 · "Withum – YouTube", 1.2K subscribers, 929 videos.
- https://www.youtube.com/user/WithumVids/search?query=Mangano · 200 · 0 results.
- https://www.youtube.com/@WithumCPA/about · 404.
- https://www.withum.com/ · 200 · footer social links (Facebook /WithumSmithBrown, Instagram /withumcpa, LinkedIn company, YouTube /user/WithumVids, X /withumCPA).
- https://www.withum.com/resources/cyber-matters-edition-1/ · WebFetch 200 · Edition 1, 2026-09-30, by Edward Keck, Jr.; no Mangano.
- https://substack.com/@chrisnmangano · 200 → Substack search page (no profile) · https://substack.com/@manganochris · same · https://substack.com/@chrismangano · 200 profile · https://substack.com/@cmangano · 200 "Cassandra Mangano".
- https://substack.com/api/v1/user/chrismangano/public_profile · 200 JSON (id 183558122; set up 2024-11-10; 5 subscriptions).
- https://medium.com/@{chrisnmangano,chrismangano,cmangano,manganochris} · 403 Cloudflare · https://medium.com/@chris.mangano · WebFetch 403.
- https://www.reddit.com/user/{chrisnmangano,chrismangano}/about.json · 403 "blocked".
- https://www.pinterest.com/{chrisnmangano,chrismangano,cmangano,manganochris}/ · 200 · as in the matrix.
- https://linktr.ee/cmangano · 200 · "Carol Mangano".
- https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor={chrisnmangano,chrismangano,manganochris}.bsky.social · "Profile not found" · …actor=cmangano.bsky.social · exists, empty.
- https://chrismangano.com/ · HTTPS: connection failed (000) · http://chrismangano.com/ · 301 → https://www.linkedin.com/in/chrismangano · HTTP 999 (LinkedIn's bot wall; the redirect was followed automatically by curl -L; no page content was received; the slug is not his).
- DNS A lookups: chrisnmangano.com, manganochris.com, chrismangano.net · no record.
- https://itunes.apple.com/search?term=Chris+Mangano&media=podcast&entity=podcastEpisode · 200 · 25 collision episodes · term=Mangano+Withum · 0 · term=Rainmakers+Roundup&entity=podcast · 1 (id1719793302) · term=Withum+podcast · 8 shows · term=Vin+and+Mike+Episode+11 · description read (sports guest).
- https://itunes.apple.com/lookup?id=1719793302 · 200 · feed https://www.spreaker.com/show/6017378/episodes/feed · 200 · 32 items, 0 "Mangano".
- WebSearch: "Chris Mangano" Withum instagram OR facebook OR twitter · no relevant hit · "Chris Mangano" Withum cybersecurity twitter OR x.com · no hit · "Chris Mangano" site:x.com OR site:twitter.com · no hit · "Chris Mangano" site:instagram.com OR site:facebook.com OR site:threads.net Withum OR Mercadien OR cybersecurity · no social hit (bio pages only) · "Chris Mangano" Withum video OR webinar OR "Cyber Matters" OR NJCPA OR JKJ youtube · no hit · "Chris Mangano" Withum facebook OR instagram Langhorne OR Bucks County · refused by the search tool.

## Open

- **X @chrisnmangano:** exists, but no bio, photo, follower count or post could be seen (timeline endpoint rate-limited all pass; x.com serves a JS shell). Whether it is his, and whether it is active or dormant, is undetermined. A later retry of https://syndication.twitter.com/srv/timeline-profile/screen-name/chrisnmangano from a different network would settle it.
- **Facebook:** no handle known; the platform is unreadable from curl (400) and WebFetch (title only). The "Mangano Chris (@mangano.chris)" profile is a name match only.
- **"Visit my website" on his LinkedIn (seed):** URL not known; no personal domain found under his name.
- **Substack @chrismangano and Pinterest chrismangano:** name matches with no identifying content; cannot be assigned or ruled out.
- **Medium and Reddit:** bot-walled; presence unknown.
- **Whether he appears on Withum's own social accounts** (X @withumCPA, Facebook, Instagram): not opened beyond existence; the YouTube channel has nothing under his name.
- **Method note:** http://chrismangano.com/ redirected to a linkedin.com URL that curl followed automatically before the response (HTTP 999) could be inspected; no LinkedIn content was received.

Drafted with Claude — directed, edited, and approved by Jefferson.
