# Person-read brief, v2 (replaces v1 on 2026-10-13 evening; v1 retired after Jefferson's "hard no": its output was a recitation of facts)

Read-only. Never contact anyone, never log in, never visit LinkedIn, Facebook, Instagram or X profile pages (the lead does LinkedIn and Humantic in its own tab). WebSearch, WebFetch, curl only. Every claim carries a source URL or says "not found". Every inference is labeled INFERENCE with the two or more signals it rests on; one signal is a lead, not an inference. Never invent.

**Order matters: the person first, the room last.** "My shit's secondary. Their shit is primary." Nothing about Captain Tomorrow belongs in this file.

**Target:** {name} · {org} · {role} · thread {T1|T2|T3} · seeds: {candidate file section; prior v1 scan file; linkedin-reads.md entry}. Read all three seeds first; they are evidence already gathered, not the answer.

**Read everything they published in the last 12 months, and at least two long-form pieces in full** (podcast transcripts, essays, interviews, their book's introduction, a newsletter run). Skimming show notes is not reading. Quote them, dated.

## Output: `{thread}/{slug}-person.md`

### 1. Identity
Two anchors that prove it's the same person. Label VERIFIED-PRIMARY / SEARCH-ONLY / UNVERIFIED. Collisions ruled out and how.

### 2. The person read (write this as 400–700 words of prose, then the evidence list)
Answer, in this order, with their own words wherever possible:
- **Who are they?** Origin, path, what they built, what they're proud of, what they've failed at or lost, as they tell it. Family, health, faith and community wherever they have put it on the record. This is how you understand motive: who they are around, what they have been through, what they organize their time around. Not deep, and nothing they have not said publicly themselves, but never fenced off, labeled "context only," or ruled out as card material. An on-record fact about their family or faith is handled like any other on-record fact. (Jefferson, 10/14, correcting my v2 rule: "If it's on record it's fair game. How are we supposed to understand motive without understanding their community? That's the whole point.")
- **What do they care about?** The three to five themes they return to, with dated quotes. What they praise. What they mock. What they repeat.
- **Motivations and experiences → current behavior.** Why they do what they're doing now, as an INFERENCE from at least two cited signals each. What their current behavior tells us about what they want next.
- **How they talk.** Register, humor, length, structure, sign-offs, vocabulary they own. A cold email in the wrong register dies on the first line.
- **Where they show up.** Stages, shows, podcasts (host and guest), press, communities, associations, meetups, conferences they attend. With dates.
- **What they consume.** Books, newsletters, podcasts, people they cite or follow, frameworks they borrow, tools they name. Where they read.

### 3. Right now (last 90 days) and what isn't getting public play
- What's new, what shifted, what went quiet in their content and calendar. Compare to the prior 90 days.
- **Signals pass:** hiring posts and job descriptions (what roles, what they say about the company), headcount trend, team arrivals and departures, office or market moves, new offers or products, events announced or cancelled, awards, press, legal or regulatory items, client or member reactions.
- **Engagement:** who comments on their posts and what they ask; who they reply to; who they tag. What their audience is actually responding to vs. what they post.
- **Their people and their clients/members:** employees' or members' own public posts, reviews (Google, Glassdoor, G2, testimonials), case studies, event recaps written by attendees. What are those people thinking about?
- For each item: source, date, and a confidence label (HIGH / MEDIUM / LOW). Inferences about private situations need two signals.

### 4. What they have said they need
The one or two problems they have named in their own words that are unsolved, with dates and URLs. Not angles. Not a pitch. Just the problem as they put it.


**Review sites (Glassdoor, Indeed, G2, Google reviews): the lead reads them in Jefferson's Chrome, not an agent.** Agents get 403s; Chrome (not signed in) shows Glassdoor's headline numbers, category ratings, the six-month trend, and three reviews per page with full text on each review's own page; Indeed shows review text under its sign-in modal. Cadence matters: rapid paging tripped Glassdoor's bot wall on 10/13 and it demanded a login. Never bypass that; stop, note what was read, and ask Jefferson whether he wants to sign in himself in that tab. Subagents write "REVIEW SITES: PENDING — lead reads in Chrome" and move on.

### 5. Humantic
Leave the heading with "PENDING — lead pulls in Chrome". The lead fills in: DISC profile, communication advice, what to lead with and avoid. The lead also records the LinkedIn read here.

### 6. Room or company facts (T1 chapter or group / T2 event series / T3 company)
As in v1: size, calendar, how speakers are booked and paid (grade A–D with source), past speakers and whether they were paid, selling policy from the stage, headcount and founder-led evidence for T3.

### 7. Handles
Consistent usernames across platforms, for Maigret (run by the lead).

### 8. Sources
Every URL used, with what it was used for.

**Bounds:** none on time within reason; the long-form reading is the job. Partial is fine only if the file says exactly what was not read and why. Report back with: identity label, three sentences on who this person is, the "right now" item with the highest confidence, and the problem they named.

---

## Addendum 2026-10-13 (late): the quiet-person kit and the delta rule

Added after the Brickwood next-layer run. Use when sections 2–4 come up thin, and as a standard pass on everyone.

**A. LinkedIn, lead's own tab only (attributable; log every page in `linkedin-reads.md`).** Method note (10/13): the Interests sub-tabs (Companies, Groups, Newsletters, Schools) only re-render when the pill's <label> is clicked, not its checkbox: `[...document.querySelectorAll('label')].find(e=>e.textContent.trim()==='Newsletters').click()`, wait 5 s, then get_page_text. Newsletters is the richest consumption signal on the profile; Companies often lists their clients. `/recent-activity/reactions/`, `/recent-activity/comments/`, `/details/interests/` (Companies, Newsletters, Top Voices, Groups, Schools), `/details/recommendations/` (received and given: their praise of others is their values in their own words), Featured. Note who comments on them repeatedly and whom they congratulate: that is the circle.

**A2. Humantic (lead, in Jefferson's Chrome).** The direct profile URL (`app.humantic.ai/prospects/search/profile?id=<linkedin url>`) only renders profiles that already exist; for a new person it spins on "Reading their public footprint" indefinitely. What works: open `app.humantic.ai/prospects/search`, click the "LinkedIn URL" pill, then set the input with the React-safe setter and submit: `const i=document.querySelector('input'); Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set.call(i,'<url>'); i.dispatchEvent(new Event('input',{bubbles:true})); document.querySelector('button[type=submit]').click()`; wait 30 s; get_page_text. Keyboard typing into that box did not register. Save the full text to `humantic/<slug>.md`. A lowercase badge in Recent Searches (e.g. "si") marks a low-data read.

**B. The firm as proxy, non-attributable, free.** `dig +short TXT <domain>` (SPF includes and vendor verification records = the vendor stack, including AI vendors: `anthropic-domain-verification`, `openai-domain-verification`); `dig MX`; homepage third-party script hosts (marketing automation, chat, visitor de-anonymization such as Apollo/6sense/RB2B, ATS); ATS feeds with publish dates (Workable `apply.workable.com/api/v1/widget/accounts/<slug>?details=true`, Greenhouse `boards-api.greenhouse.io/v1/boards/<slug>/jobs`, Lever `api.lever.co/v0/postings/<slug>`, BambooHR `<slug>.bamboohr.com/careers/list`); Wayback CDX for team, careers, bio and homepage diffs; blog cadence via RSS or `/wp-json/wp/v2/posts`; Glassdoor and Indeed trends (Chrome, slowly, never past a bot wall).

**C. Public record.** ProPublica Nonprofit Explorer full-text search (`projects.propublica.org/nonprofits/full_text_search?q="Name"`) for board seats and fellow directors; state Secretary of State business search for other entities and co-officers; state license boards; FEC contributions: the public demo key on api.open.fec.gov rate-limits after about 25 calls an hour; instead read `fec.gov/data/receipts/?data_type=processed&contributor_name=<Name>&contributor_state=XX&contributor_employer=<Firm>` in Chrome (no key; add `two_year_transaction_period=` for each cycle; click "Toggle details" for employer, occupation and ZIP; filter by employer to beat common names) (in bounds per his 10/13 ruling: "Political giving is absolutely in bounds"); state-level giving via the state ethics/elections portal (Texas Ethics Commission, Ohio SoS, Florida DoE) when federal is thin; court records (flag).

**D. Audio that is already text.** iTunes search API → feed → `podcast:transcript` tags (Buzzsprout, Transistor, Captivate publish them); YouTube auto-captions via `yt-dlp --write-auto-sub --skip-download`; Listen Notes for every guest appearance. Transcribing from scratch is last-ditch (his ruling 10/13).

**E. Their unguarded words elsewhere.** Amazon and Goodreads reviews; Substack profile "Reads" and comments; X replies and following list; Reddit and HN by handle (Maigret); YouTube comments; testimonials they gave to vendors, coaches or programs (`"Name" testimonial`: who they pay); blurbs they wrote for others' books; book acknowledgments pages (Google Books preview) naming their circle; conference bios across years.

**B2. Roster diff, worked method (10/13 late, Vanderbloemen).** `web.archive.org/cdx/search/cdx?url=<domain>/<team-page>&from=2025&filter=statuscode:200&fl=timestamp&collapse=timestamp:6` lists captures; fetch 4–6 spread captures with `http://web.archive.org/web/<ts>id_/<url>` (raw HTML, no toolbar), 4–6 s apart (the archive refuses connections when hammered), plus the live page. Extract names as text lines that repeat twice in a row (photo caption + heading) and match a Name pattern; skip captures that return zero. Write the table of added/gone per capture and the retention count against the oldest capture. Result for Vanderbloemen: 37 names in Feb 2025, 13 still there in Oct 2026, 65 distinct people across five captures.

**F. The delta rule.** For every source with a time axis, pull now and twelve months ago, and write the change, not the state: roster, careers feed, homepage positioning, bios, blog cadence and topics, podcast topics, Glassdoor trend, DNS history (SecurityTrails) for when a vendor appeared, the person's own 90-day content shift. The state is noise; the delta is the signal.

**G. Not used.** Account-existence probes against a person's email (holehe-style): they touch account-recovery flows and can trigger a notice to the person, which violates no-contact. Nothing behind a bot wall. No login other than the lead's own LinkedIn and Glassdoor.
