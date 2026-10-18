# Experiment plan: doors versus direct (written 2026-10-18)

**What this is.** A test of one use of the research stack: cold outreach for paid speaking spots in front of founder-led businesses of 25 to 100 people. It answers one question: which route gets an owner's attention, writing to the people they listen to (doors) or writing to them directly. It does not judge the stack. The stack is a toolkit and is paused, incomplete, while this runs. What the test owes the stack at the end is three notes: which parts this use leaned on, which parts it wanted that do not exist yet, and which parts were more than it needed.

**Who does what.** Jefferson unblocks the resources in section 0 and makes the calls marked *his*. An executing Claude session (Opus) runs phases A to F and logs phases G and H. The planning session (this file's author) owns the interactive infographic of the stack; it is not part of the execution. Jefferson is the only sender, always.

---

## 0. Before anything starts: what Jefferson unblocks

| Resource | Needed for | What to do | If left blocked |
|---|---|---|---|
| **Manus** (an autonomous research agent, manus.im) | The fresh T3 founder sweep in phase C. On 10/13 it showed a sign-in page in Chrome and never ran. | Sign in at manus.im/app in Chrome, or say "drop Manus." | ChatGPT Deep Research carries the sweep alone; T3 may fall short of ten. |
| **ChatGPT** (Deep Research) | The T3 sweep | Confirm you are signed in at chatgpt.com and that Deep Research runs are left this month. | No fresh sweep; T3 stays at the thin list on file. |
| **Humantic** (reads personality type from public writing) | The register line on every new draft | Signed in at app.humantic.ai; enough credits for about 23 new people. | Drafts go out without a register line; the notes get more generic. |
| **LinkedIn** in your Chrome, plus the Claude in Chrome extension | The lead's LinkedIn read on every new person, read-only, logged | Signed in; extension connected. | No LinkedIn layer on the new people. The biggest single loss. |
| **Glassdoor** (optional) | Review reads on T2 and T3 firms | Sign in yourself in the tab if you want them; the bot wall is never bypassed. | Review sites skipped, as they were for most of the first nine. |
| **Attio**, your CRM | Checking that no new candidate is someone you already know or contacted | Make sure the Attio connector is enabled in the executing session. | The check is done by hand against your memory in the kill-or-keep step. |
| **Decisions** (yours) | The whole run | (1) 45 sends: 30 direct, ten per thread, plus 15 doors. (2) Brief v3 additions (platform matrix, three nearest voices, network slice) in force for this wave. (3) The "six small businesses" clause in the drafts: keep, cut, or reword. (4) T3 size tolerance: Winters is about 20 people; is 20 to 100 the band? (5) Vanderbloemen and Dixon stay out. | Nothing starts. |
| **Your time** | Days 1, 3, and 3 to 5 | About 30 minutes for kill-or-keep on day 1; three to four hours on day 3 to read each cited source and edit; about an hour a day for three days to send. | The run stalls at drafts. |

---

## 1. Starting the executing session

```bash
cd ~/Sites/adaptiverse-research && claude
```

Start it in `~/Sites/adaptiverse-research`, not in `hm-outreach`: that is where this thread's memory lives (the state-of-play note and Jefferson's standing corrections load automatically). Then, in order:

1. `/join-board "Scout Consultant"` so the session can receive and send board mail.
2. Read, in this order: this file; `SCAN_BRIEF.md` (the person-read brief, v2 with the 10/15 corrections and the proposed v3 sections); `RESEARCH_PROCESS.md`; `TIERS_AND_APPROACH.md` sections 4, 9 and 9b; `PERSON_BRIEFS.md`; `cards/first-touch-v3.md`; `CARD_SHAPE.md` (voice rules only; its pitch shape is retired); `sweeps/STATE.md`; the three candidate files; `sweeps/names-vistage-weintraub-2026-10-15.md`, `sweeps/names-rea-acg-winters-2026-10-15.md`, `sweeps/maigret-coverage-2026-10-15.md`.
3. `git pull --ff-only` in `~/Sites/hm-outreach`; confirm `git status` is clean in the run folder; confirm with `ListAgents` that no other session is working in it.
4. Run phase A. Do not start phase C until phase A is green or Jefferson has waved a blocked item through.

Commit after every phase with a descriptive message; push. Deliverables Jefferson reads go to Notion (direct API, never the MCP tools) as child pages of the process page `3f8164c1-810d-8191-8032-c9956ca8e1f8` or into the row bodies of the database below. File links into this folder do not open in his app.

---

## 2. The rules (Jefferson's, and only these)

Research only. Never contact anyone; Jefferson is the only sender. Never log in, never enter credentials, never cross a login wall or a bot wall, never solve a CAPTCHA. Agents never like, comment, connect, follow or message anywhere. LinkedIn is read in Jefferson's Chrome by the lead, read-only, every page logged in the thread's `linkedin-reads.md` as an attributable byproduct; Humantic likewise. Public profile pages on Instagram, Facebook, X, TikTok, Threads, YouTube, Substack, Medium and Reddit are in bounds for agents, logged out, with what is visible recorded and any wall noted. No account-existence probes against a person's email (holehe-style). Nothing about Jefferson or Captain Tomorrow in any person file. On-record health, family, faith and community are in bounds for reads and drafts. Political giving is in bounds. No pitch in a first touch. Every claim carries a source URL or says "not found"; inferences are labeled and rest on two signals. Define every organization and role on first use (he does not know EO, Vistage, TAB, Rea, Withum, Weintraub). Names, never roles. A rule you cannot quote from Jefferson is not a rule; do not add one.

---

## 3. The design

| Arm | Count | Read | Note shape |
|---|---|---|---|
| Direct, deep read | 10 | The seven done (Garrido, Luther, Brickwood, Chediak, Mangano, Flanagan, Winters) plus three new, one per thread | Read-ask first touch (v3) |
| Direct, light read | 20 | New, about an hour of agent time each | Read-ask first touch (v3) |
| Doors | 15 | One verified paragraph each, no full read | Door note (section 9) |

Ten direct per thread (T1 peer rooms, T2 sponsored rooms, T3 founder direct) because the process page already says nothing counts before ten sends per thread. Every send goes out in the same three-day window, so timing cannot bias the routes.

**Fixed for the whole test.** Jefferson sends everything, in his voice. No pitch and no ask for a call in a first touch. Drafts are not rewritten mid-test. No new process design and no new deep reads beyond the three.

**Decision rules, set now so results cannot bend them.**
- A route *wins* if its yes rate (a guest date, a session slot, a call they asked for, an introduction) is at least double the other route's, with at least three yeses.
- If doors win: outreach adds the channels-and-doors work as a standing part of its research; the human read for outreach drops to the light form.
- If direct wins: the deep read stays for outreach, because it earned the replies; the rollup across people is not built for this use.
- If both win: run both, and send deep reads only to people a door has already warmed.
- If neither route reaches three yeses: the problem is the offer or the message, not the research. The next effort is the pitch branch, not more reads.
- Depth, within direct: if the deep arm's reply rate is not at least double the light arm's, outreach uses the light read from then on. The full read stays in the toolkit for uses that need it.

None of these verdicts invalidates a part of the stack. They only say what this use needs.

---

## 4. Phase A: preflight (day 1, about 30 minutes)

Run every check; write `PREFLIGHT_2026-10-XX.md` in the run folder with pass or blocked per line and the evidence; stop and report to Jefferson on any blocked item the day's work depends on. Never work around a block.

| # | Check | How | Blocks |
|---|---|---|---|
| A1 | Network | `curl -sI https://api.notion.com` returns a status line | everything |
| A2 | Notion token | `GET /v1/users/me` with the token from the global CLAUDE.md | tracker, deliverables |
| A3 | Maigret (username scan) | `~/Sites/hm-outreach/tools/venv-maigret/bin/maigret --version`; smoke run on one known handle with `--dns-resolver threaded --top-sites 50` returns without DNS errors | handles layer |
| A4 | YouTube captions | `which yt-dlp`; on 10/18 it was not on the PATH. Install into `~/Sites/hm-outreach/tools/` (a venv) if missing. | long-form reading of video |
| A5 | Claude in Chrome extension | Load the tools; `tabs_context` lists Jefferson's tabs | LinkedIn, Humantic, FEC, review sites |
| A6 | Sign-ins, read-only | Open each in a new tab and read whether a sign-in page shows; never type credentials: chatgpt.com, manus.im/app, app.humantic.ai, linkedin.com/feed, glassdoor.com. Report which are signed in. | sweep, register, LinkedIn layer |
| A7 | Deep Research quota | Jefferson reports how many runs remain | T3 sweep |
| A8 | Search budget | Plan no more than three search-heavy agents at once (the shared budget is about 200 searches a turn; it starved two sweeps on 10/13) | phases C and E |
| A9 | Attio connector | List the Attio tools; `whoami` | exclusion check |
| A10 | Folder and sessions | `git status` clean after `git pull --ff-only`; `ListAgents` shows no other session on this folder | all writes |
| A11 | Brief currency | `SCAN_BRIEF.md` carries the 10/15 rules paragraph (commit dddfd11 or later) and no rule that cannot be quoted from Jefferson | reads |
| A12 | Exclusions | Vanderbloemen and Dixon out; nobody has been sent anything (sends are 0 of 30); Attio shows no existing relationship with a new candidate | pool |
| A13 | Scale sign-off | Section 12's estimate shown to Jefferson; his go | start |

---

## 5. Phase B: tracker (day 1, 15 minutes)

Database "CT cold outreach — experiments": `3f8164c1-810d-81fe-833c-e8930d8ddf52`. It already has Name, Human, Org, Role, Size, Thread, Status (researching → paid, dropped), Pays evidence (A to D), Angle, Card, Notes, Research file, Sent (date), Replied (date). Add, without renaming anything:

- **Route** (select): Direct, Door.
- **Read depth** (select): Deep, Light, Paragraph.
- **Outcome** (select): No reply, Replied, Yes to something, Intro or room, Declined.
- **Reaches** (text): for a door, which target or room they are a door to.
- **Give** (text): what the note offers.

Set Route = Direct and Read depth = Deep on the seven existing drafted rows. Every new target and door gets a row as soon as it passes verification, Status = researching. The weekly count is already defined on the process page: sent → replied → call → offer → booked → paid.

---

## 6. Phase C: the pool and the kill-or-keep list (days 1 to 2)

**Target:** 23 new direct targets: 8 for T1, 7 for T2, 8 for T3. Verify about 35 so Jefferson's kills still leave 23.

**Sources on file.**
- T1: `t1-peer-rooms/t1-candidates.md`: 14 learning chairs of EO (Entrepreneurs' Organization, a peer network of founders; the learning chair books the chapter's speakers), 5 chairs of Vistage (a paid CEO peer-advisory network; the chair runs a group and picks its speakers), 1 TAB (The Alternative Board, peer boards for small-business owners). Luther, Dixon and Garrido are used; 17 remain.
- T2: `t2-sponsored-rooms/t2-candidates.md`: 20 firms. Three used. Many of the rest are national (Paychex, TriNet, Marsh McLennan Agency, Cherry Bekaert) and the wrong size; the regional CPA, insurance and law firms are closer. A firm only counts once a named human who convenes the room is found.
- T3: `t3-founder-direct/t3-candidates.md` (Gascoigne, Paul Downs, Rob Levin, DHH, with fit notes), `next-wave.md` (Anna Singleton, Noelle Cordeaux), `sweeps/chatgpt-T3-founders-report.md` (eight). T3 is the thin thread and needs a fresh sweep in parallel: ChatGPT Deep Research, and Manus if unblocked, on the 21 Hats podcast owner panel (full transcripts), Inc.'s Founder Group Chat and Inc. 5000 CEO-survey coverage, for founders of 25-to-100-person companies with a public statement of their own uncertainty about AI in the last six months. Aim for twelve verified.

**Verification standard (primary source means the source itself, not a page about it).** Identity on their own site or the organization's page; role current; for T1 and T2 the room exists and a pay grade can be given with a source (A: a bureau-represented past speaker or an honorarium line; B: a sponsor-funded keynote or a named outside keynote; C: unknown; D: pay-to-play, do not send); for T3 the size band, founder-led, and the AI statement verbatim with URL and date. Anything from a sweep stays a lead until checked.

**Output:** `POOL_2026-10-XX.md` and a Notion page under the process page, one table: name, organization, role, thread, grade or size, one line of their own words with URL, identity label, recommended keep or kill, and a "deep read?" mark on one per thread (the candidate with the most direct control of a slot). Jefferson kills or keeps in the Notion page. The Attio check runs on the keeps.

---

## 7. Phase D: doors (days 2 to 3, in parallel with phase C)

A door is a named person the target demonstrably listens to (quoted them, hired them, was on their show, reacted to them three or more times, co-presented, or they organize the target's room) who is easier to reach than the target (hosts want guests, organizers field speaker questions, editors want experts). Agents never contact them; the pick is for Jefferson.

**Verified candidates on file (25).** From the names files and plan section 9b:
- Garrido's rooms: Ryan Hogan (host of Confessions of a Vistage Chair; CEO of Talent Harbor; Vistage member), Angie Neal (Speaker Relations Manager, Vistage Florida), Megan Austin (Marketing and Events Coordinator, Vistage Florida), Dean Jackson (host, More Cheese Less Whiskers).
- Luther: Ethan King (his former coach, now teaches AI, guest on his show), Christa Haberstock (speaker manager), George Wright III (host, The Daily Mastermind).
- Brickwood: Deke Bowman (host, Taking Stock with Koble), Becky Boyd (Director of Marketing and Communications, Rea), Tory Spadafora (Chief Growth Officer, Rea), Renee Tyack (Programming Chair, ACG Columbus, the Columbus chapter of the Association for Corporate Growth), Nichole Glenn (Executive Director, ACG Columbus).
- Chediak: Shawna Holley (Weintraub Tobin, organizer of the Business Focus seminar; title to confirm), Scott Syphax (author of Boardroom Notes, PBS host, moderated Business Focus 2020), Todd Michaud (CEO of HuLoop, AI newsletter he subscribes to).
- Mangano: Linda Howard (Withum, organized the Los Angeles stop), Alexandra Bretschneider (JKJ, his Philadelphia co-presenter), Bob Considine (host of Minding Your Business, NJBIA).
- Flanagan: Noelle Cordeaux (CEO, Lumia Coaching; Inc. peer), Clayton Payne (co-founder of Oldfield Pets; host of Pet Business Disruptors), Margo Reign (Delaware SBDC advisor).
- Winters: Michael Hastings-Black (host, Breakfast Club DC), Conor Hoey (founder, First Concepts), Lindsay Kaplan (co-founder, Chief).

**Pick 15.** Hosts, organizers and speaker-relations roles first, because they have a public reason to answer. Default pick, for Jefferson to change: Hogan, Neal, Wright, King, Bowman, Tyack, Boyd, Holley, Syphax, Howard, Considine, Bretschneider, Payne, Cordeaux, Hastings-Black. Confirm each still holds the role on a primary source; confirm a public contact path (a show's guest form, a firm email printed on the site, a public profile that answers comments). Write one paragraph per door: who they are, the evidence of direction toward the target, the public contact path, and the give that fits their audience. One Notion page for all 15, and a row each with Route = Door, Read depth = Paragraph, Reaches filled.

---

## 8. Phase E: reads (day 2, parallel)

**Light read (20 people, about an hour of agent time each, 1,200 to 2,000 words).** File `<thread>/<slug>-person.md` headed "LIGHT READ". Sections:
1. Identity: two anchors, label VERIFIED-PRIMARY / SEARCH-ONLY / UNVERIFIED, collisions ruled out.
2. Who they are: 150 to 250 words of prose in their own words where possible, including on-record family, health, faith and community as motive.
3. What they put out and where: a short platform table (platform, handle, verified how, role producer / participant / consumer / dormant / not found, last date, URL).
4. What they consume: books, newsletters, podcasts, people they cite, with sources.
5. What they have said they need: one or two problems in their own words, dated, with URL.
6. Doors: three named people they listen to who are easier to reach, evidence of direction, contact path. Names, never roles.
7. The room (T1, T2: how speakers are booked and paid, grade, the next slot date) or the company (T3: size, founder-led, the AI statement).
8. Handles, a Maigret run with `--dns-resolver threaded`, and sources.
The lead adds the LinkedIn read and Humantic in Jefferson's Chrome, logged.

**Deep read (3 people).** `SCAN_BRIEF.md` v2 in full, plus the v3 additions (platform matrix 2e, three nearest voices 2f, network slice 2g) once Jefferson confirms they are in force for this wave. About 25 minutes wall clock and 400,000 tokens each.

**Parallelism.** No more than six light reads at once, staggered, and no more than three search-heavy agents at any moment. Maigret runs serially. Every file ends with its sources. Nothing about Jefferson or Captain Tomorrow in any person file.

---

## 9. Phase F: drafts (day 3)

**Direct notes (23 new).** The v3 read-ask shape in `cards/first-touch-v3.md`: one specific thing noticed in their public record; one clause of who you are and why you are asking; two questions only they can answer, about their room or company; an offer to send back what the others say. No pitch, no credential paragraph, no ask for a call, no links, no attachments. Voice from `CARD_SHAPE.md`: warm, direct, contractions, a dash or two, no bullets, under 140 words, never "I hope this finds you well." Register line from Humantic where read. The cited source under each draft.

**Door notes (15).** New shape, same rules: one specific thing noticed about their show, room or event; one clause of who you are and why you are writing; the give, which is a topic or segment for their audience with one line on why it fits, or two questions about their audience and an offer to share back what others say; no credentials paragraph, no ask for a call, no links; under 120 words. For a speaker-relations role (Angie Neal), the two questions can be about how the summits bring in outside speakers. That is a question, not a pitch.

Each draft goes into its row's body as a green callout, with the cited source. Jefferson edits in Notion. Agents never send.

---

## 10. Phase G: sending and logging (days 3 to 5, then two weeks)

Jefferson's protocol: read the cited source yourself first; edit; send about 15 a day for three days, mixing doors and direct each day; after each send, set Status = sent and the Sent date on the row, or tell the session and it does. Replies: forward them, or the session reads your mail (authorized) weekly and sets Replied, Outcome and Status. Nobody but Jefferson replies to anyone.

---

## 11. Phase H: readout (two weeks after the last send; about November 6 if sends finish October 23)

One page under the process page: a table of route by read depth with sent, replied, yes, intro-or-room counts and median days to reply; the verdict against section 3's rules, quoted; what people said they wanted in their replies, verbatim, as input to the pitch branch; and the three notes owed to the stack (parts leaned on, parts wanted, parts over-built). Then Jefferson decides whether and in what order the stack build resumes.

---

## 12. Cost and time, estimated

| | Estimate |
|---|---|
| Agent wall clock | Three working days for phases A to F |
| Tokens | About five to six million: pool verification and the T3 sweep about one million; 20 light reads about 2.5 million; 3 deep reads about 1.2 million; doors and drafts under one million |
| Jefferson's time | About nine hours: 30 minutes kill-or-keep, three to four hours reading sources and editing, three hours sending, plus replies |
| Sends | 45 over three days |
| Readout | Two weeks after the last send |

---

## 13. Not in this plan

- The interactive infographic of the stack (parts by use case, click for output, tool, cost and status): the planning session's deliverable, separate from this execution.
- Building out the stack (preflight as a standing step, the rollup across people, the network slice as a first-class part): paused until the readout.
- The pitch branch (one pitch per play, and the engagement an owner buys after the talk): Jefferson's, informed by the replies.

Drafted with Claude — directed, edited, and approved by Jefferson.
