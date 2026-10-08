# Research tooling — with a detectability rubric

Companion to `org-awareness-play.md`. Built from a complete pass over `jivoi/awesome-osint` (1,813 lines, 74 sections, ~1,450 entries), 2026-08-20, with maintenance verified live via `gh api` on 101 repos that day.

**Jefferson's framing (2026-08-20), which supersedes any pre-filtering on my part:** *"Add to your rubric: is there any way to tell how I get the information? Then give me everything and I'll make the ethical calls."* So every tool below carries a **detectability** classification derived from its actual mechanism — which protocol it speaks, to whose server, with or without credentials. The judgment is his.

## The detectability classes

| Class | Meaning |
|---|---|
| **INVISIBLE** | Reads data someone else already publishes or has already collected. No packet reaches the target or their company. |
| **ANONYMOUS HIT** | His IP touches a page. Appears in analytics as one unattributed visitor. |
| **ATTRIBUTABLE** | The target sees his name — LinkedIn profile views, following, email subscriptions. |
| **NOTIFIES THE TARGET** | The tool pokes something that actively alerts them. |
| **HITS COMPANY INFRA** | Scanning-class traffic against company servers; may trip security monitoring. |

**Two findings from applying this that invert intuition:**
1. **The least detectable category is the most damaging.** Breach brokers are INVISIBLE — he never touches anyone's systems. The cost isn't detection, it's **provenance**: nothing sourced that way can ever be explained out loud.
2. **Hosted beats self-hosted on detectability.** A hosted change-detector polls from the *vendor's* IP — INVISIBLE to the target. Self-hosted polls from his residential IP on a fixed interval, which is a **signature** in a small site's logs, not noise. Default to hosted, or add jitter and a long interval.

---

## The set worth using

### Finding every platform someone publishes on
- **Maigret** — `pip install maigret`. Best in class: extracts bio, real name, and outbound links from each profile found, then chains them. **ANONYMOUS HIT** (unauthenticated GETs to ~3,000 `site/{username}` URLs; does *not* register a LinkedIn profile view). ⚠️ **It is a handle tool, not a name tool** — proven on our own runs: brilliant on someone with one consistent handle, near-useless otherwise.
- **crt.sh / CertKit / Merklemap** — Certificate Transparency. If a target has a personal domain, CT reveals every subdomain a CA ever issued: `blog.`, `newsletter.`, `notes.`. **INVISIBLE — the cleanest discovery mechanism in the entire file.** CT logs are public append-only records published by CAs; reading them never contacts the domain owner.
- **PublicWWW** — searches the *source code* of 500M+ pages. Find a Substack ID, a Beehiiv embed, a shared analytics ID, a Calendly link. **INVISIBLE.** Free tier limited, ~$49/mo.
- **grep.app / GitHub Code Search** — their handle, email, or domain committed anywhere public. **INVISIBLE** / ANONYMOUS HIT on GitHub, not on the person.
- **Hosted resolvers** (IDCrawl, SherlockEye, User Search) — **INVISIBLE to the target**: the vendor's servers do the probing. Trade-off: the vendor logs his query.

### Cadence and what they post
- **Filmot** — full-text search inside YouTube captions, 573M captions. Searching a name finds every panel, podcast, and talk where someone *said* it. **INVISIBLE.** Nothing else on the list does this.
- **yt-dlp** — `--write-auto-subs --skip-download` pulls the transcript so he can quote accurately. **ANONYMOUS HIT on YouTube.**
- **Arctic Shift / PullPush** — complete Reddit history with timestamps: topics, cadence, *and which subreddits* (which is the joinable-surfaces answer). **INVISIBLE** — independent mirrors, reddit.com never touched. (Pushshift's public API died in 2023; the list still presents it as current.)
- **Wayback Machine** — their blog three years ago: deleted posts, old bios, prior positioning. **INVISIBLE.**
- **SlideShare / Scribd / DocumentCloud** — conference decks people uploaded and forgot. **ANONYMOUS HIT.**

### Being alerted the day they post
- **Google Alerts** — free, zero install, instant or daily. One per person, one per company. **INVISIBLE.** ⚠️ Laggy on low-volume queries and **blind to LinkedIn**.
- **Hosted change detection** (visualping, FollowThatPage, OnWebChange, changedetection.io's hosted tier ~$8.99/mo) — **INVISIBLE to the target**; their logs show the vendor's crawler. **Prefer this over self-hosting**, for the reason above.
- **Feedly** — every Substack (`/feed`), Ghost, Medium, WordPress, and GitHub user (`.atom`) publishes RSS. **INVISIBLE** — Feedly's servers fetch, his IP never touches the origin, and a feed fetch carries no identity.
- **`github.com/<user>.atom`** — native Atom feed of all public activity. Free, no install, **INVISIBLE**. The list offers a 53-star polling script instead and never mentions this.
- **MyTweetAlerts** — email alert on any X search including `from:handle`. **INVISIBLE.**

### Reqs that aren't on the public board
- **waybackurls** — dumps every URL archive.org has recorded for a domain: which ATS they use, which job paths existed, what was posted and pulled. **INVISIBLE — zero packets reach the company.** Best value-to-risk ratio in the file. (2.3yr stale, but it wraps a stable API and still works.)
- **Google dorks** — `site:jobs.ashbyhq.com company`, `site:boards.greenhouse.io "Company"`, `site:company.com inurl:careers`. **INVISIBLE.**
- **Change detection pointed at the ATS JSON endpoint, not the rendered page** — diffs JSON natively, catches the req at creation. **ANONYMOUS HIT on the ATS vendor** (Greenhouse/Lever/Ashby), *not* on the company's own servers — materially quieter.
- **BuiltWith** — which ATS a careers page runs, so you know the endpoint shape. **INVISIBLE** (serves from their crawl history).
- **Amass `-passive` only** — finds `careers.`/`jobs.` subdomains from CT logs. **INVISIBLE in passive.** ⚠️ Default mode is NOT passive.

### Company trajectory
**SEC EDGAR** (use **sec.gov/edgar**, not the commercial mirror the list links) — 8-K **Item 5.02** states officer departures and appointments in the company's own words, which often explains exactly why a seat opened. **OpenCorporates** is the private-company equivalent (officer changes over time). **GuideStar** 990s for nonprofits — likely the highest-yield entry in that section given his sector. **Judyrecords** (free, 400M+ US court cases). **Crunchbase**, **SimilarWeb/SpyFu**. All **INVISIBLE**.

### His own findability — the underrated half
The **Expert Search** section (22 entries) is a list of directories he *adds himself to* so journalists and conference programmers find him: HARO, Sources.com, Experts.com, Newswise, National Speakers Association, Zintro, Maven, plus a **MuckRack** profile. **ATTRIBUTABLE by design — being found is the point.** Complements the Google lane already in the six-lane taxonomy.
Also: run Maigret on himself (find the 2011 profile outranking his good work), **justdelete.me** to clean up, **ExifTool** to strip metadata from his résumé before sending — a PDF routinely carries author name, template origin, and sometimes a previous employer in the Company field.

---

## The traps — mechanism spelled out, decision his

- **holehe — NOTIFIES THE TARGET.** It POSTs an email to each site's **password-reset endpoint** and reads the response differential. On many sites that **sends the person a real "someone requested a password reset" email.** The one action in the file that puts a message in a target's inbox. Also ~2 years stale, so its adapters have decayed.
- **the-endorser — ATTRIBUTABLE.** Drives a *logged-in* browser through LinkedIn profiles, which generates profile-view events: the target literally sees his name.
- **LinkedInDumper — the mirror image.** Same platform, opposite exposure: it calls LinkedIn's internal Voyager API with his session cookie. The *company* sees nothing, but **LinkedIn** sees a session pulling an entire employee roster — their anti-scraping signature. The risk lands on his account, which is the asset the whole play depends on.
- **Instagram tooling flips on one setting.** Vendor-token mode = INVISIBLE. His own logged-in session = **ATTRIBUTABLE** (Instagram shows story-view identities by design).
- **Breach brokers** (DeHashed, LeakCheck, h8mail, Hudson Rock, infostealers) — **INVISIBLE, and that's the trap.** Unexplainable provenance; several are paid, meaning the broker holds his query history tied to a payment identity.
- **PimEyes can NOTIFY THE TARGET.** They sell a "PROtect" product that alerts individuals when their face is searched. Useless here regardless — he already knows who the person is.
- **urlscan.io — public by default.** Doesn't reveal him, but broadcasts that *someone* looked at that exact URL at that time, and companies monitor urlscan for their own domains. Set visibility to unlisted.
- **Email verifiers** (Hunter, Snov, Reacher) — **HITS COMPANY INFRA, low severity.** Opens an SMTP conversation with the company's MX and issues `RCPT TO:` without delivering. Appears in their mail logs; Google Workspace and Proofpoint log and rate-limit exactly this. Hosted keeps his IP out; self-hosted Reacher does not.
- **Recon frameworks** (theHarvester, SpiderFoot, ReconFTW, Amass default, Subhunt) — **HITS COMPANY INFRA / MAY TRIP SECURITY.** Amass default brute-forces tens of thousands of DNS labels (an NXDOMAIN flood is a standard IDS signature); SpiderFoot's default profile enables active modules unless "Passive" is explicitly chosen. Returns attack-surface data with zero job-search value, from an action that looks exactly like pre-attack recon. **If a security team ever correlates that scan with an application two weeks later, the conversation is over.**
- **HTTrack / WebCopy** — recursively downloads a whole site from his IP at crawler speed. The loudest single action available against a small company's server.

---

## What the list does NOT cover

1. **LinkedIn monitoring — the gap that matters most.** Two entries, both scrapers, one 18 months stale. **Nothing in ~1,450 links alerts on a person's LinkedIn posts.** The native bell is ATTRIBUTABLE (following is visible). The Chrome-based briefing watch remains the least-detectable option.
2. **Substack/newsletter discovery.** No directory, no search. Workaround: every Substack exposes `/feed`. ⚠️ Detectability split — **reading the RSS is effectively INVISIBLE; subscribing by email is ATTRIBUTABLE** (Substack shows authors their subscriber names).
3. **Bluesky and Mastodon** — listed as networks, zero tooling. Bluesky is the easiest platform in existence to monitor (public AT Protocol firehose).
4. **ATS endpoints** — no Greenhouse, Lever, Ashby, Workday, SmartRecruiters anywhere. The literal core of the hidden-req need, absent.
5. **Podcast search** — no ListenNotes, Podscan, Podchaser. Filmot is YouTube-captions only, so podcast-only appearances stay invisible.
6. **Events, meetups, CFPs — the worst-served need.** No Meetup, Eventbrite, Luma, or Sessionize. Sessionize speaker profiles in particular would be a goldmine (what someone talks about and where they'll be next).
7. **Any pricing or maintenance signal** — roughly 30% of what was checked is stale or dead.

## Errors in the list itself
`lukeslp/antisocial` **404s**. **MuckRack** is described as MuckRock (FOIA) — different service; MuckRack is the journalist database and the more useful one. **EDGAR** links to a commercial mirror instead of sec.gov. **Pushshift** presented as current (public API died 2023). `sub3suite` and `BuscaPaginasBlancas` are **archived** despite fresh-looking push dates. Still listed but dead: Yahoo Answers, Newseum, Open Grey, Microsoft Academic, Bottlenose, SocialBakers, Trooclick.

## Dead — don't waste time
Zen (7.3yr) · SerpScan (5.2) · FOCA (3.7) · fb_friend_list_scraper (3.7) · h8mail (3.0) · **nexfil (2.9 — use Maigret)** · waybackpy (2.5) · glit (2.3) · holehe (1.9) · toutatis (1.7) · the-endorser (1.5) · LinkScope (1.5) · **blackbird (1.1 — Maigret is fresher and better)**. Exception: **waybackurls** is 2.3yr stale but recommended anyway — thin wrapper on a stable API, unmatched value-to-risk.

---

# The stack as a pipeline

The catalogue above is sorted by *need*. This section sorts the same tools by *sequence* — how they chain across a single person-discovery run, mapped to the layers of `individual-discovery-process.md`. Read top to bottom: each stage feeds the next, and each tool carries its detectability class so the ethical call stays visible at the point of use.

```
① IDENTITY ─▶ ② PUBLISHING ─▶ ③ CONSUMPTION ─▶ ④ CIRCLES ─▶ ⑤ LIVE REQ ─▶ ⑥ STANDING WATCH ─▶ ⑦ SYNTHESIS
   name→accounts   where they PUT   where they READ    who's around   the hidden seat   alert on the day    openings + his own hygiene
```

**Optional broad first pass — Manus (or any autonomous research agent).** Runs the open-web sweep from the vendor's cloud IPs and returns a compiled dossier. Useful to seed Stage ① and ② fast, but everything it returns is a *lead, not a fact* — re-verify each claim through the named tool below before it enters a report (composes with the adversarial-verification layer). Detectability: **INVISIBLE to the target** (vendor browses), but the **vendor logs the full query** — treat like a breach broker on provenance.

## ① Identity resolution — name → every account (Layer 0–1)

| Tool | Purpose | Detectability |
|---|---|---|
| Maigret | Chase a known handle across ~3,000 platforms; chains bio/real-name/outbound links | ANONYMOUS HIT — handle tool, near-useless on a bare name |
| crt.sh / CT logs | Personal domain → every subdomain a CA ever issued (`blog.`, `newsletter.`) | INVISIBLE — cleanest discovery mechanism in the file |
| Hosted resolvers (IDCrawl, SherlockEye) | Name → candidate accounts; vendor's servers do the probing | INVISIBLE to target (vendor logs the query) |
| grep.app / GitHub Code Search | Handle, email, or domain committed in any public repo | INVISIBLE |
| Authenticated browser (LinkedIn) | Anchor identity; Schools tab carries Layer-1 anchors | ATTRIBUTABLE — profile views show his name |

## ② Publishing map — where they PUT content (Layer 2)

| Tool | Purpose | Detectability |
|---|---|---|
| PublicWWW | Find Substack/Beehiiv/Calendly/analytics embeds in page source | INVISIBLE |
| Feedly / RSS (`/feed`, `.atom`) | Every Substack, Ghost, Medium, WordPress, GitHub user publishes a feed | INVISIBLE — vendor fetches, feed carries no identity |
| Filmot | Full-text YouTube-caption search — every panel/podcast/talk they spoke on | INVISIBLE |
| yt-dlp | Pull the transcript so he can quote accurately | ANONYMOUS HIT on YouTube |
| Wayback Machine | Their blog three years ago: deleted posts, prior positioning | INVISIBLE |
| SlideShare / Scribd | Conference decks they uploaded and forgot | ANONYMOUS HIT |

## ③ Consumption and register — where they READ (Layer 3)

| Tool | Purpose | Detectability |
|---|---|---|
| Substack `public_profile` API | `.subscriptions[]` — what they actually read (use the SLUG, not the id) | INVISIBLE |
| LinkedIn Interests tab (authenticated) | Follows, Groups (= communities), Newsletters, Companies | ATTRIBUTABLE |
| Arctic Shift / PullPush | Full Reddit history + *which subreddits* (the joinable-surfaces answer) | INVISIBLE — independent mirrors |
| Citation mining (their own corpus) | Outbound-link ratio: real SOURCE vs vendors/their own properties | INVISIBLE |
| GitHub stars/follows (`.atom`) | 30-second read; excellent for engineers, dead end otherwise | INVISIBLE |

## ④ Circles and inroads — who's around them (Layer 4)

| Tool | Purpose | Detectability |
|---|---|---|
| Authenticated browser | Commenters, mutuals; on an inward-facing target, invert to THEIR commenters + recent hires | ATTRIBUTABLE |
| Maigret chaining | Cross-platform circle from a resolved handle | ANONYMOUS HIT |
| Show-notes / speaker-bio bridge | Highest-yield single step — surfaces the best finding even when identity is resolved | INVISIBLE / ANONYMOUS HIT |

## ⑤ Live requisition — the hidden seat (Layer 6)

| Tool | Purpose | Detectability |
|---|---|---|
| waybackurls | Every archived job path + which ATS existed and was pulled | INVISIBLE — best value-to-risk in the file |
| BuiltWith | Which ATS the careers page runs, so you know the endpoint shape | INVISIBLE |
| Google dorks | `site:boards.greenhouse.io "Company"`, `site:jobs.ashbyhq.com company` | INVISIBLE |
| ATS APIs (Workday CXS, Greenhouse, Ashby, Lever) | The live req + every screening question with its exact options | ANONYMOUS HIT on the ATS vendor, NOT the company |
| Change detection → ATS JSON endpoint | Catches the req at creation, diffs JSON natively | ANONYMOUS HIT on vendor — materially quieter than the rendered page |
| SEC EDGAR 8-K Item 5.02 / OpenCorporates / GuideStar 990 | Why the seat opened, in the company's own words | INVISIBLE |

## ⑥ Standing watch — alert the day they move (Layer 7 + presence loop)

| Tool | Purpose | Detectability |
|---|---|---|
| Google Alerts | One per person, one per company | INVISIBLE — but laggy and BLIND to LinkedIn |
| Hosted change detection (visualping, changedetection.io hosted) | Watch a page; polls from the vendor's crawler | INVISIBLE to target — prefer over self-hosting |
| MyTweetAlerts | Email alert on any X search incl. `from:handle` | INVISIBLE |
| LinkedIn briefing watch (Chrome) | The gap the whole catalogue can't fill — nothing alerts on a person's LinkedIn posts | Least-detectable LinkedIn option (native bell is ATTRIBUTABLE) |

## ⑦ Synthesis — openings + his own hygiene (Layer 5b/5)

| Tool | Purpose | Detectability |
|---|---|---|
| Humantic AI | DISC/buyer-personality read from a LinkedIn URL, to tune register | INVISIBLE to target (vendor pulls public profile); vendor logs his query |
| Subject-term match (Layer 5b) | Sort their surface into OCCUPIED/PEER/OPEN/MENTIONED-UNDEVELOPED/VOID | INVISIBLE — runs against the already-collected corpus |
| ExifTool | Strip author/template/prior-employer metadata from his résumé before sending | INVISIBLE |
| Maigret on himself + justdelete.me | Find the stale profile outranking his good work; clean it up | mixed — his own accounts |
| MuckRack / HARO / Expert directories | Add himself so journalists and programmers find him | ATTRIBUTABLE by design — being found is the point |

**The through-line:** the quietest tools (INVISIBLE) do the discovery; the one unavoidable ATTRIBUTABLE step is the authenticated LinkedIn browser, which is why it's spent deliberately and late. The loud recon frameworks (theHarvester, SpiderFoot, Amass-default, HTTrack) appear nowhere in this pipeline — they return attack-surface data with zero job-search value from an action that looks exactly like pre-attack recon.
