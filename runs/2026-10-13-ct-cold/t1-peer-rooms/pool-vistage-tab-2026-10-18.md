# T1 pool: Vistage chairs and one TAB facilitator, verification pass (2026-10-18)

**Status:** complete for the five. Identity checks that need LinkedIn are left to the lead's read.

**Scope.** Entries 16 to 20 of `t1-candidates.md`: Kirsten Yurich, Walter Paulsen, Dr. Veronica Anderson, Angelo Sisco (Vistage), Ed Riefenstahl (TAB). Garrido (15) is done and is not repeated here.

**Terms.**
- **Vistage** is a paid CEO peer-advisory network. Owners and CEOs pay to sit in a group of peers that meets monthly for a full day. A **Vistage chair** runs one or more groups, coaches each member one to one, and books the outside speaker for the monthly meeting. A **"CE" group** is Vistage's chief-executive group. **Chair Academy** is Vistage's training for new chairs.
- **TAB (The Alternative Board)** is a franchised peer-board network for small-business owners. A **TAB facilitator**, usually the local franchise owner or one of their coaches, runs boards of 6 to 8 owners that meet monthly, plus a monthly one-to-one coaching session.
- **Confessions of a Vistage Chair** is a podcast hosted by Ryan Hogan (CEO of Talent Harbor, a Vistage member) that interviews Vistage chairs. Its transcripts carry no speaker labels, so each quote below was attributed by reading the turns around it.

**Method.** curl with a desktop User-Agent and WebFetch on the people's own sites, the Vistage and TAB pages, podcast transcript pages and one press article; WebSearch where those ran out (7 searches). No logins, no LinkedIn pages opened, no contact.

**Grades** follow the plan's scale. A: a bureau-represented past speaker or an honorarium line. B: a sponsor-funded keynote or a named outside speaker. C: unknown. D: pay-to-play.

## What Vistage says in public about booking and paying speakers (applies to all four chairs)

- **Booking:** "Due to the volume of interest in speaking for Vistage, we are only onboarding speaker candidates who either have a meeting date arranged with a Chair or who are members of the Vistage community*." The asterisk: "A Vistage community member has an existing relationship with Vistage as a member, sponsor, or Chair." Source: https://vistage.com/membership/vistage-speakers/become-a-vistage-speaker/ (fetched 2026-10-18).
- **The intake form** asks for a "Committed Chair name" and "Committed meeting date", and says the date "will be verified with the Chair before processing your request." Source: https://vistage.com/membership/vistage-speakers/apply-to-be-a-speaker/ (fetched 2026-10-18).
- **Pay:** no fee, honorarium or travel language on either page, or on https://vistage.com/membership/vistage-speakers/. One search for public Vistage speaker-fee terms found none. **How Vistage pays speakers is not public; not found.** The only pay-adjacent public fact is that Vistage runs an "Impact Speaker Award" for speakers with "200 or more presentations" over five or more years, which shows a professional speaker roster exists (https://www.vistage.com/?p=12043, search result only, not fetched).
- **Chair directory:** vistage.com has no public per-chair page for any of the four. The URL patterns `vistage.com/vistage-chair/<name>/` all redirect to the chair-recruitment page. Vistage does host chair microsites at `app.vistage.com/sites/s/chairs/<id>/<name>`; one exists for Sisco (linked from a podcast page), but its content loads by script and was not readable with curl. The four names do not appear in Vistage's press-release sitemap (715 releases, grepped 2026-10-18).

## Summary

| Name | Organization | Role | Grade | Own words (short), with URL | Identity | Keep / kill | Deep-read candidate? |
|---|---|---|---|---|---|---|---|
| Kirsten Yurich | Vistage, Harrisburg PA area; also her own coaching practice | Chair of one referral-only CE group; also runs "The Circle," a women leaders' peer group | C | "There's a lot of people who wanna use it and sort of take the, 'I've got the hammer, where are the nails?' approach." (2026-06-23) https://confessions.fm/podcast/s/confessions_of_a_vistage_chair/e15_the_group_is_the_prize_with_kirsten_yurich_on_building_a_vistage_culture_worth_protecting | VERIFIED-PRIMARY | Keep | **Yes** |
| Walter Paulsen | Vistage, Palo Alto CA; also his own CEO coaching and an AI strategy service | Chair of "the Palo Alto group" since 2022 | B | "I think a, a smart human working with AI creates a much better moat for… most companies" (2026-06-09) https://confessions.fm/podcast/s/confessions_of_a_vistage_chair/e14_who_owns_strategy_and_what_happens_when_no_one_really_does_with_walter_paulsen | VERIFIED-PRIMARY | Keep, with a flag (he sells AI strategy work to the same owners) | No |
| Dr. Veronica Anderson | Vistage, Philadelphia (per one event page) | "Vistage Chair and Chief Executive Advisor" (event page wording) | C | None found in her own words | UNVERIFIED | Kill unless the lead's LinkedIn read confirms her | No |
| Angelo Sisco | Vistage, Chicago area; also Sisco Advisors | Chair of one CE group, "The Lighthouse," 10 members, launched Dec 2025 | C | "And now I run a wonderful CE group with 10 amazing people." (2026-05-26) https://confessions.fm/podcast/s/confessions_of_a_vistage_chair/e13_fear_identity_and_finding_freedom_with_angelo_sisco | VERIFIED-PRIMARY | Keep, low priority (no AI record) | No |
| Ed Riefenstahl | TAB Fort Worth & West (TX, NM) | "Founder & Facilitator"; one of four facilitators | C | No dated words of his own found; the franchise page's copy is undated marketing | VERIFIED-PRIMARY (one anchor) | Kill | No |

**Counts:** 3 keep (Yurich, Paulsen, Sisco), 2 kill (Anderson, Riefenstahl). **Deep-read candidate:** Kirsten Yurich.

## Per person

### 16. Kirsten Yurich

- **Identity: VERIFIED-PRIMARY.**
  - Her own site, https://kirstenyurich.com: "Kirsten is a licensed behavior analyst, speaker, author, and retired CEO who partners with business leaders"; services include "Peer Groups for CEOs and Executives." The site does not mention Vistage by name.
  - In her own voice on Confessions of a Vistage Chair, E15, aired 2026-06-23 (URL in the table): "I have one CE group. We are referral only" and "we do span a million to a billion in this group."
  - Central Penn Business Journal, 2022-07-15, "Kirsten Yurich launches executive coaching group for CEOs, business owners" (https://www.cpbj.com/kirsten-yurich-launches-executive-coaching-group-for-ceos-business-owners, read through WebFetch; curl returned 403): she is a Vistage chair whose chief-executive group started in spring 2022 in the Harrisburg area and meets monthly, rotating among members' businesses. The same article says she was most recently CEO of Vista Autism Services, a nonprofit serving over 300 people with autism, has worked in the Harrisburg area for more than 25 years in health care and special education, and is an adjunct professor of education at Felician University.
  - **Correction to `t1-candidates.md`:** that file says the episode shows she "previously led Hunt a Killer." It does not. Hunt A Killer is the host's company (Ryan Hogan), and the "nine years in Vistage… Ed Robinson was my first chair" passage at 1:07 is also the host speaking about himself. Her prior CEO role was Vista Autism Services (CPBJ).
- **Role current and city:** chair of one CE group as of 2026-06-23, in her own words. City: Harrisburg, PA area (CPBJ 2022; her site's testimonials name Mechanicsburg PA, the Whitaker Center and Central Penn Youth Ballet, both in Harrisburg). That the group still meets in Harrisburg in 2026 is an inference from those two signals.
- **The room:**
  - One referral-only Vistage CE group, member companies from about $1M to $1B in revenue. Member count: not found.
  - Speakers: "We had a speaker, um, last week for my group. It was the third time he came… He remembered people's names." (E15, 30:46). The speaker is not named, so grade stays C.
  - Pay: Vistage policy only (see the top section); nothing of her own.
  - **Second room:** "The Circle," her own peer group, "Close intimate group of up to 8 female non-profit leaders," "Monthly 4 hour in-person sessions curated and facilitated by Kirsten," "$750/mo," with a wait list. Source: https://www.kirstenyurich.com/the-circle (fetched 2026-10-18).
- **AI on record:** no AI session run or written about. On E15 (2026-06-23, about 43:25 to 47:42) the host asks how she sees AI implementation and she answers at length:
  - "There's a lot of people who wanna use it and sort of take the, 'I've got the hammer, where are the nails?' approach… I'm concerned that approach may, uh, do more damage. You may have more holes than you have, uh… actual solved problems." (43:58 to 44:18)
  - "The approach I've seen be a little more effective is… who are your people willing to sit in a room with, um, some donuts and some ideas and a computer and be like, 'Hey, um, where could we, um, 10X ourselves?'" (44:29)
  - "It is the ultimate squirrel syndrome, and you want people to be excited, and you want the guardrails so that… if you're government regulated or you've got… PHI or PII… you need to be a little more, uh, careful." (47:29)
  - "My, my husband's a CISO. I hear about it all the time." (46:44). Attribution to her rests on the turn order (the host had just been speaking about his own team); the transcript has no speaker labels.
  - Her blog's 2026 posts (1/5, 4/29, 10/2) are not about AI.
- **Own words, one line:** "My motto is the group is the prize." (E15, 53:54, 2026-06-23)
- **On-record context:** "Speaker, Author, retired CEO, mother of 4 and recovering work-aholic" (https://kirstenyurich.com/podcast). On E15 she says she "always wanted to work with animals" and "got adopted into the field of autism" with "no personal connection."
- **Public footprint:** her site with a blog (posts dated 1/5/26, 4/29/26 and 10/2/26 this year, much more often in 2025; RSS at https://www.kirstenyurich.com/blog?format=rss), her podcast "Executive Hustle" (local executives; https://kirstenyurich.com/podcast), The Circle, the CPBJ article, E15, and a Calendly link (https://calendly.com/kirstenyurich/30min). Handles: not checked beyond the site.
- **Keep, because** she controls the monthly speaker slot for a CE group, runs a second paid room of her own, publishes, and has thought out loud about how owners should and should not adopt AI.
- **Deep-read candidate: yes.** Same slot control as the other chairs, plus a second room, a podcast and blog of her own, and the most considered AI passage of the five.

### 17. Walter Paulsen

- **Identity: VERIFIED-PRIMARY.**
  - His own site, https://walterpaulsen.com (title "Walter Paulsen — CEO Coach for Bay Area Founders," © 2026): "Vistage CEO Peer Groups (Palo Alto)… I chair the Palo Alto group." "In 2020 I started coaching full-time. In 2022 I took on a Vistage Chair role in Palo Alto." Contact: walter.paulsen@vistagechair.com, 650.465.7929.
  - In his own voice on E14, aired 2026-06-09 (URL in the table): "So, uh, I'm a, a CEO and executive coach based in, uh, Palo Alto. Uh, and I typically work with company CEOs that have, you know, five to 50 million in revenue." (57:32)
  - Midlife Fulfilled podcast, episode 158, published 2024-02-19: "Walter Paulsen, a Vistage Chair," same Vistage email. https://fulfilledatworkacademy.com/podcast/lessons-from-a-silicon-valley-vistage-chair-for-high-achieving-ceos/
- **Role current and city:** Vistage chair, Palo Alto, CA (own site, 2026).
- **The room:**
  - One group as far as public sources say ("I chair the Palo Alto group"). Member count: not found.
  - Speakers: "Gosh, who's the guy who wrote, uh, 'Culture by, uh, Design'? He was a speaker at my, um, Vistage, uh, group. David Friedman wrote a book called… 'Culture by Design.'" (E14, 43:14). Date not given. **Grade B** on that named outside speaker. Whether Friedman is bureau-represented was not checked.
  - Pay: Vistage policy only.
- **AI on record:**
  - E14 (2026-06-09): "I think a, a smart human working with AI creates a much better moat for moat- most companies than for the $10 million CEO to say, 'Okay, I'm gonna go to Claude and I'm gonna be my own marketing VP. I don't need any additional help.'" (21:12) and "the LLMs are, uh, and AI are really much more powerful when they are joined with some domain expertise" (21:29).
  - E14: "I'm doing work with an AI strategic planning platform that, um, you know, targets middle market companies." (17:15)
  - His site sells "Strategic Advisory (GO GROW AI): Top-tier strategic rigor for middle-market companies, at a fraction of big-firm cost," and one-to-one coaching on the "Outgrow Method."
  - No AI session run for his group found.
- **Own words, one line:** "Most CEO coaches have never been a CEO. I've built and sold four companies, including a unicorn." (https://walterpaulsen.com, 2026)
- **Public footprint:** his site, E14, Midlife Fulfilled (2024), an appearance on "Ilana's podcast," which he calls "primarily the sales podcast" (E14, 0:45; not identified further). His book on balance for technology CEOs was "upcoming" in Feb 2024; publication not found. Background on his site: Blackhawk Network founding team, CardFact president, Redbox Gift Card Exchange VP and GM, co-founder and CEO of Alula Hydronutrients.
- **Keep, with a flag.** He controls his group's speaker slot, has a named outside speaker on record, and talks about AI for $5M to $50M owners. The flag: he sells an AI-assisted strategy service (GO GROW AI) to the same kind of owner, so an outside AI session in his room overlaps his own offer. That is a fact for Jefferson to weigh, not a rule.
- **Deep-read candidate:** no. His record is thinner than Yurich's and his own AI offer complicates the room.

### 18. Dr. Veronica Anderson

- **Identity: UNVERIFIED.**
  - The only source is the Luma event page for the "2026 Philadelphia CEO Summit," Sep 24, 2026: "Hosted by Dr. Veronica Anderson, Vistage Chair and Chief Executive Advisor," under the heading "Sponsor & Host." https://luma.com/CEO-Summit-Philadelphia (fetched 2026-10-18).
  - The event is "Presented by CXO & Co / Rosewater Falls" and listed on the organizer calendar https://luma.com/cxoandco-vistage, which shows no other events now. The organizer is an events company, not her.
  - Two searches ("Veronica Anderson" Vistage chair Philadelphia; "Dr. Veronica Anderson" CEO advisor coach Pennsylvania) found nothing that names her. No own site, no Vistage page, no press release.
- **Role current and city:** Philadelphia, as of Sep 2026, on that one page only.
- **The room:**
  - Her Vistage group: not found.
  - The summit: a free, invite-only morning for "Philadelphia's top 50 CEOs ($5m-$500m revenue)," with a panel of three CEOs (Steve Graham of Graham Partners, Mike Fiebach of Mainfactor, Drew Morrisroe of CTN) and a "CEO Hot Seat," themed on "planning for growth in a world of uncertainty and AI." The panel is of CEOs, not paid speakers. Her role is "Sponsor & Host." Reading this as a member-recruiting event paid for by the chair is an inference from the "Sponsor & Host" wording and the free attendance; not sourced.
  - Grade C.
- **AI on record:** she hosted the summit above (2026-09-24, past) whose theme names AI. No words of her own about AI found.
- **Own words:** not found.
- **Public footprint:** the one event page.
- **Kill, unless** the lead's LinkedIn read confirms who she is and that she chairs a group. If it does, she becomes interesting because she runs an outside-facing summit as well as a group.
- **Deep-read candidate:** no.

### 19. Angelo Sisco

- **Identity: VERIFIED-PRIMARY.**
  - His own site, https://siscoadvisors.com ("Sisco Advisors," © 2025): "Angelo Sisco: Helping founders and CEOs implement a Business Operating System (BOS)"; "I help $2-50M companies create structure, build strong teams and implement systems." The site does not mention Vistage or AI. Its blog page is empty; its newsletter is "GrowthOS."
  - In his own voice on E13, aired 2026-05-26 (URL in the table): "I signed up for Chair Academy September 2025, went there, and then I launched my group in December of '25… And now I run a wonderful CE group with 10 amazing people… the name of our group is The Lighthouse." (35:56 to 36:18)
  - The Ambitious Coach Lab, episode 25, 2026-05-21: "Angelo Sisco is a Vistage Chair, business coach, and leadership facilitator." The page links his Vistage chair microsite (https://app.vistage.com/sites/s/chairs/0032E00003Nv9ObQAJ/angelo-sisco; loads by script, content not read) and siscoadvisors.com. https://ambitiouscoachlab.buzzsprout.com/2567603/episodes/19206159-the-inner-work-behind-elite-coaches-with-angelo-sisco
- **Role current and city:** Vistage chair since Dec 2025. Chicago area: on E13 he says his family moved to San Clemente, CA, then "we came back in '22, and when I came back in June of '22…" (32:50), and earlier stories place his gyms in Chicago. A search-only result says he opened O'Hare CrossFit (2010) and CrossFit Harwood Heights (2015) (https://storyengine.libsyn.com/website/the-art-of-investing-in-yourself-with-angelo-sisco, search result only). The current city is an inference from those two signals.
- **The room:**
  - One CE group, 10 members, launched Dec 2025.
  - Speakers: none named. Grade C.
  - How he built it: "I set a date for it, and I started a meeting October. I had five people show up." (56:06)
- **AI on record:** none found, on E13, his site, or the Ambitious Coach Lab notes.
- **Own words, one line:** "my why is to help people feel seen. That's it." (E13, 0:10, 2026-05-26)
- **On-record context:** "what else did God give us this place for?" (E13, 23:15); "sometimes I think God has better plans than your goals anyway" (51:40); his father was absent for 11 years in his childhood (1:15); he has a son who was nine months old when the family moved to California (31:03).
- **Public footprint:** his site, E13, The Ambitious Coach Lab (May 2026), and older podcast appearances from his CrossFit and "Alpha Hippie" years (search results only: https://toddnief.com/angelo-sisco-interview/, https://hustleandflowchart.libsyn.com/angelo-sisco-the-4-pillars-of-a-bulletproof-business-mindset).
- **Keep, low priority.** He controls the speaker slot of a new group whose calendar is still being built, but there is nothing on AI in his record and his own site is silent on Vistage.
- **Deep-read candidate:** no.

### 20. Ed Riefenstahl

- **Identity: VERIFIED-PRIMARY, one anchor.**
  - The TAB franchise page, https://www.thealternativeboard.com/fort-worth (title "Ed Riefenstahl Founder & Facilitator | TAB Fort Worth," fetched 2026-10-18), with his phone 817-480-2516 and email eriefenstahl@tabfortworth.com. His own domain, tabfortworth.com, redirects to this page, so it is the same anchor, not a second one.
  - One search on his name returned only pages about Leni Riefenstahl. No second source found.
- **Role current and city:** "Founder & Facilitator," TAB Fort Worth & West, covering Fort Worth and Tarrant County, Weatherford, West Texas (Abilene, San Angelo, Midland, Odessa), the Panhandle (Lubbock, Amarillo), El Paso and Albuquerque. Facilitators: "Ed Riefenstahl, Val Riefenstahl, Cathy Trinh, and Dale Jackson."
- **The room:**
  - "Each TAB Fort Worth & West board includes 6–8 experienced business leaders who meet monthly," plus monthly one-to-one coaching. Members are "typically business owners growing typically $500K toward $30M in revenue."
  - No outside speaker slot is described on the page; the format is peer discussion led by the facilitator. TAB's national conferences do book outside speakers (see `t1-candidates.md`, TAB note), but those are TAB's, not his. Grade C.
- **AI on record:** the page's table of owner fears includes "AI disruption & being left behind: Competitors using AI to move faster while you stand still. TAB gives members a place to compare AI experiments and vendors, and to tie AI decisions to strategy, cash, and people." Undated marketing copy, not his own signed words.
- **Own words:** none dated found.
- **Public footprint:** the franchise page only. No blog, podcast or articles found.
- **Kill, because** the board format has no outside-speaker slot on record and no dated words of his own turned up.
- **Deep-read candidate:** no.

## Sources

- https://vistage.com/membership/vistage-speakers/
- https://vistage.com/membership/vistage-speakers/become-a-vistage-speaker/
- https://vistage.com/membership/vistage-speakers/apply-to-be-a-speaker/
- https://www.vistage.com/sitemap_index.xml and https://vistage.com/press_release-sitemap.xml (grepped for the four names)
- https://www.vistage.com/?p=12043 (search result only)
- https://confessions.fm/podcast/s/confessions_of_a_vistage_chair/e15_the_group_is_the_prize_with_kirsten_yurich_on_building_a_vistage_culture_worth_protecting
- https://confessions.fm/podcast/s/confessions_of_a_vistage_chair/e14_who_owns_strategy_and_what_happens_when_no_one_really_does_with_walter_paulsen
- https://confessions.fm/podcast/s/confessions_of_a_vistage_chair/e13_fear_identity_and_finding_freedom_with_angelo_sisco
- https://kirstenyurich.com, https://www.kirstenyurich.com/why-kirsten, https://www.kirstenyurich.com/the-circle, https://kirstenyurich.com/podcast, https://www.kirstenyurich.com/blog?format=rss
- https://www.cpbj.com/kirsten-yurich-launches-executive-coaching-group-for-ceos-business-owners
- https://walterpaulsen.com
- https://fulfilledatworkacademy.com/podcast/lessons-from-a-silicon-valley-vistage-chair-for-high-achieving-ceos/
- https://luma.com/CEO-Summit-Philadelphia, https://luma.com/cxoandco-vistage
- https://siscoadvisors.com, https://siscoadvisors.com/llms.txt, https://siscoadvisors.com/blog/
- https://ambitiouscoachlab.buzzsprout.com/2567603/episodes/19206159-the-inner-work-behind-elite-coaches-with-angelo-sisco
- https://app.vistage.com/sites/s/chairs/0032E00003Nv9ObQAJ/angelo-sisco (exists; content loads by script, not read)
- https://storyengine.libsyn.com/website/the-art-of-investing-in-yourself-with-angelo-sisco, https://toddnief.com/angelo-sisco-interview/, https://hustleandflowchart.libsyn.com/angelo-sisco-the-4-pillars-of-a-bulletproof-business-mindset (search results only)
- https://www.thealternativeboard.com/fort-worth, https://tabfortworth.com (redirects to it), https://www.thealternativeboard.com/global-events
