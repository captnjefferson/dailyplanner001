# Research process, CT cold outreach (as of 2026-10-15)

The steps in the order they run, from finding people to the drafts Jefferson sends. "The lead" is the main Claude session; "subagent" is a research agent it dispatches. Folder: `~/Sites/hm-outreach/runs/2026-10-13-ct-cold/`.

**Rules on every step.** Research only. Nobody is contacted; Jefferson is the only sender. No logins, no credentials, no crossing a login wall or bot wall, no CAPTCHAs. Agents never like, comment, connect, follow or message. LinkedIn is read only in Jefferson's Chrome, read-only, and every page view is logged.

| # | Step | Tool | Output | How the output is used |
|---|---|---|---|---|
| 1 | Set the frame | Notion process page, written by the lead | Three threads (peer rooms, sponsored rooms, founder direct), the rules, pay-evidence grades A to D | Every sweep prompt and person read is briefed against it |
| 2 | Sweep for lists | ChatGPT Deep Research in Jefferson's Chrome; three Opus subagents on web search; Manus (stopped at its sign-in page) | Candidate lists per thread: `sweeps/` and the three `t*-candidates.md` files | A pool of leads only. Nothing moves on until it is checked on a primary page |
| 3 | Verify and pick | The lead, on primary pages in the browser pane | Nine targets, three per thread; extras parked in `t3-founder-direct/next-wave.md` | Decides who gets a person read |
| 4 | First scan (v1 brief, retired 10/13) | One subagent per person and one per room | A short scan per person; one file per organization: size, calendar, how speakers are booked and paid | Seeds for step 5. Room facts feed the plan. The cards built from it were rejected |
| 5 | Person read (`SCAN_BRIEF.md`, v2) | One Opus subagent per person: web search, page fetches, podcast transcripts, YouTube captions; at least two long-form pieces read in full | `<slug>-person.md`, about 8,000 words, eight sections: identity; who they are; right now; what they said they need; Humantic and LinkedIn; the room; handles; sources | The record every later step cites |
| 6 | Firm signals | Same subagent: domain records, job-board feeds, Wayback Machine captures of team and careers pages, blog feeds | Vendor stack, hiring, who joined and who left, the change over twelve months | The "right now" section of the read |
| 7 | Public record | Subagent for nonprofit filings and state business records; the lead in Chrome for Federal Election Commission donations | Board seats, other companies, political giving | Motive and community in the read |
| 8 | LinkedIn read | The lead in Jefferson's Chrome, read-only, each page logged in `linkedin-reads.md` | Posts and cadence, reactions, comments, newsletters followed, groups, recommendations, the people around them | Section 5 of the read; where to point Jefferson's posts |
| 9 | Humantic (a tool that infers personality type from public writing) | The lead in Jefferson's Chrome | `humantic/<slug>.md`: type, preferred length and tone, what to lead with and what to avoid | The voice line in each brief and draft |
| 10 | Review sites | The lead in Jefferson's Chrome: Glassdoor, Indeed, Google reviews; stops at any bot wall | What their staff and clients say | The "right now" section of the read |
| 11 | Username scan | Maigret (checks one username across about 500 sites), run by the lead on every candidate handle | A hit list per handle in each thread's `maigret/` folder; coverage across all handles in `sweeps/maigret-coverage-2026-10-15.md` | Leads for step 12. A hit is not proof until a profile confirms it |
| 12 | Other platforms | Subagents, logged out: Instagram, Facebook, X, TikTok, Threads, YouTube, Substack, Medium, Reddit | `<slug>-platforms-2026-10-15.md` beside each read: present or not, producer, participant, consumer or dormant, cadence, last post, audience | Where else they post or lurk; a second surface for Jefferson's posts |
| 13 | Merge and correct | The lead | Revised reads, committed to git and copied into each person's row in the Notion database | One source per person |
| 14 | Person briefs | The lead | `PERSON_BRIEFS.md`, about 250 words per person; Notion briefs page | What Jefferson reads before deciding anything about a person |
| 15 | First-touch drafts | The lead | `cards/first-touch-v3.md`; a callout on each Notion row. None sent | Jefferson's to edit and send |
| 16 | Tiers and approach | The lead | `TIERS_AND_APPROACH.md`; Notion plan page | Monitor, Build or Pitch for each person; where each one reads; what the pitch branch must supply |
| 17 | LinkedIn watch | The Fixer, briefing module 55 | New posts from the seven in Jefferson's morning briefing; review on 2026-11-15 | Jefferson's cue to comment, the Monitor move |

## Proposed, not in force (brief v3, waiting on Jefferson's word)

| # | Step | Tool | Output | How the output is used |
|---|---|---|---|---|
| A | Three nearest voices | Subagents, then the lead | Three named people per target whom the target listens to and who are easier to reach, each with evidence and a source. First names pass: `sweeps/names-vistage-weintraub-2026-10-15.md` and `sweeps/names-rea-acg-winters-2026-10-15.md` | A second path into each room that does not run through the target |
| B | Network slice | Subagents, then the lead | Three rings, one line and a source per name: who makes their rooms, who they listen to, who they talk to in public | Shows which slice of their network to work, not the whole map |

Drafted with Claude — directed, edited, and approved by Jefferson.
