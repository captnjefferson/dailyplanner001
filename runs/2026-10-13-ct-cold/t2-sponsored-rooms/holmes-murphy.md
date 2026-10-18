# Holmes Murphy · monthly construction webinar for contractor owners · T2

- **Date:** 2026-10-18 (wave 3, written alongside `jason-mcmurray-person.md`)
- **Seeds:** `pool-2026-10-18.md` (Holmes Murphy block, kept firm #1), `t2-candidates.md` entry 6.
- **Method:** curl, WebFetch, WebSearch (lean), yt-dlp. No logins, no forms, no registration, no contact. Holmes Murphy's public WordPress REST API (`/wp-json/wp/v2/events`, `/news`, `/posts`, `/media`, `/search`) was read for every event (174), news item (290) and relevant post, with creation and edit times. Each live event page was fetched (robots.txt asks for a 10-second crawl delay; pages were fetched 6 seconds apart in one pass) for its date, time and "Event Participants" block. Retired event pages were read from the Wayback Machine. Maxim Consulting Group's public 2026 training catalog (PDF) was read to source the session titles. Holmes Murphy's Workday job board was read through its public JSON endpoint.
- **Blocked or partial:**
  - **Recordings and registration** sit on Zoom Events ticket pages (`events.zoom.us/ev/...`): "Only you can use your ticket - Be sure to log in with the account associated with" the registrant's email. Not crossed. So **attendance, cost, Q&A and who spoke at the Feb–Sep sessions are not public.**
  - Event pages created before Sep 14, 2026 carry **no participant names**; Wayback captures from before those sessions show the same.
  - LinkedIn not opened (the lead's tab). REVIEW SITES: skipped this wave by Jefferson's word.
- **Read before drafting:**
  - **Convener answer.** The named human on the room is **Jason McMurray, Vice President, Property Casualty** (Des Moines), moderator on the Oct 6, Nov 3 and Dec 1, 2026 pages and, in his own words, on the Jun 2 session. VERIFIED-PRIMARY.
  - **Every 2026 session came from one outside firm's catalog.** All titles and descriptions are word for word from **Maxim Consulting Group**'s "2026 Full Training List" (a Denver-area construction management consultancy; its consultants teach for trade associations). McMurray calls Maxim "one of our partners." The three named speakers are all Maxim: Michael Mclin, Stephane McShane, David Morton.
  - **The series is new.** No first-Tuesday owner series appears in 2024 or 2025; the 2026 run began Feb 3, 2026. Its pages for Apr–Aug were created in one 83-minute block on Feb 13, 2026.
  - **No AI session has run in this room.** Maxim's 75-page catalog mentions AI once (inside the peer-groups course description). The firm's AI sessions sit in other tracks (cyber; architects and engineers).

---

## 1. Identity (the people around the room)

### Primary human: Jason McMurray — **VERIFIED-PRIMARY**
- **Room tie:** "Moderator: Jason McMurray · Vice President, PC · Holmes Murphy" (Oct 6, 2026); "Moderator: Jason McMurrary [sic] · Vice President, PC · Holmes Murphy Construction" (Nov 3); "Moderator: Jason McMurray · Vice President, PC · Holmes Murphy Construction" (Dec 1). https://www.holmesmurphy.com/events/key-performance-indicators-5-0-increasing-margin-and-reducing-risk/ · https://www.holmesmurphy.com/events/change-order-management/ · https://www.holmesmurphy.com/events/the-second-in-command/
- **Own words on the room:** "I chatted about this topic on a construction webinar with one of our partners at Maxim Consulting Group—if you learn by listening, check out the recording!" (Aug 13, 2026, about the Jun 2 WIP session) https://www.holmesmurphy.com/blog/how-contractors-can-use-wip-reporting-to-improve-forecasting-and-cash-flow/
- **Title and city:** "Jason McMurray, Vice President, Property Casualty," Des Moines, IA, in the Jun 18, 2026 shareholder release. https://www.holmesmurphy.com/news/holmes-murphy-welcomes-27-new-shareholders-reinforcing-its-independent-advantage/
- Full read: `jason-mcmurray-person.md`.

### The construction practice
- **Dan Etzel**, "SVP, Regional Sales Leader and Construction Leader" (Mar 3, 2026 release). Named to lead Holmes Murphy Construction Jan 10, 2024 ("Starting in the Minneapolis office as its first intern"). On the construction industry page: "Meet Holmes Murphy Sr. Vice President, Construction Leader Dan Etzel." In the firm's construction video he describes the practice: "we hire technical expertise we hire people that have worked for construction companies." https://www.holmesmurphy.com/news/holmes-murphy-announces-advancements-to-key-leadership-positions/ · https://www.holmesmurphy.com/industries/construction/ · https://www.youtube.com/watch?v=7qaiRky2D6Q (captions render the name "Dan etel"). His tie to booking this series: **not found**.
- **Don Appleby**, VP, Surety, shareholder: moderator of the in-person "Get Paid" session, Colorado, Sep 9, 2026. https://www.holmesmurphy.com/events/get-paid-preserving-your-rights-to-payment-on-colorado-construction-projects/
- Others on the construction team named on firm pages (not tied to this series): Jake Schmitz (bylined "Lead, Hire, and Fire," Apr 8, 2026; *Insurance Journal*, Jun 24, 2026), Jason Wilsey (construction project risk video, Sep 8, 2025), Kara Lindstrom (VP of Construction Claims, video Apr 11, 2025), Bryce Craig (builders risk webinar, Mar 10, 2026), Larry Poague (Sr. Risk & Safety Consultant; OSHA courses), Ted Jorgensen (VP, Surety, Construction), Ben Williams (Surety Director, Construction), Mark Julik (hired Mar 2026), Jon Zentner (joined May 2026).

### Events and marketing (names; roles in this series **unverified**)
- **Jessica (Jess) Nickell**, AVP, Event Management, Des Moines; 2026 shareholder; 2026 "Game Changer": "she has helped transform event management into a strategic enterprise capability." Not named on any event page. https://www.holmesmurphy.com/blog/powered-by-our-people-meet-the-2026-game-changers/
- **Amanda Joubert**, Marketing Director, Communications (Sep 28, 2026 post; "Communications & PR Consultant based in our Waukee office" in Jan 2023). Her address wraps the contact link on McMurray's Apr 2025 byline (an Outlook Safe Link carrying "AJoubert@holmesmurphy.com"), which ties her to his blog copy, not to the webinar. https://www.holmesmurphy.com/blog/celebrating-our-heart-soul-caregivers/ · https://www.holmesmurphy.com/blog/5-key-insights-into-construction-market-trends-and-upcoming-renewals/
- **Leslie Babcock** is the printed contact for the architects-and-engineers webinar track ("please contact Leslie Babcock at lbabcock@holmesmurphy.com"), not for this series. https://www.holmesmurphy.com/events/best-practices-for-embracing-ai-in-design/

### The outside presenters (Maxim Consulting Group)
- **Michael Mclin**, Managing Director (Oct 6, 2026, KPIs 5.0).
- **Stephane McShane**, Director (Nov 3, 2026, Change Order Management). She is on SMACNA's speaker pages (search-only: https://smacna.org/speakers/business-management-university/stephane-mcshane) and taught "Key Performance Indicators 5.0" for CFMA Houston in March 2023 (search-only: https://cfma.org/events/details/march-member-meeting-1563).
- **David Morton**, Director (Dec 1, 2026, The Second in Command).
- Maxim describes this line of work: "National and regional construction associations rely on Maxim to deliver educational programs… nearly 100 seminars, workshops, keynote presentations." https://www.maximconsulting.com/training-development/training-development-industry-association-education/
- Maxim's site does not mention Holmes Murphy (site search, Oct 18, 2026).

---

## 2. The room's own words

- On the KPI session: "The pandemic has necessitated new ways to monitor performance at the company, business unit and employee level." (Maxim catalog text, reused)
- On peer groups (Jul 7, 2026), the only AI mention the series has carried: "The fast pace of change in our industry necessitates a broader lens and deep exposure to how other companies are adapting technology, leveraging AI, overcoming workforce shortages, improving margins and increasing the enterprise value of the company." https://www.holmesmurphy.com/events/driving-organizational-performance-and-innovation-through-peer-groups/
- On ownership transitions (May 5, 2026): "Nearly half of all contractors will go through an ownership transition and / or management succession by 2030." https://www.holmesmurphy.com/events/using-re-organization-strategies-for-tax-efficient-ownership-transitions/
- On the Dec 1 session: "a strategic guide for CEOs and entrepreneurs on how to find, hire, and work effectively with a Chief Operating Officer (COO) to scale their business." https://www.holmesmurphy.com/events/the-second-in-command/

---

## 3. Room facts (T2)

### Series: Holmes Murphy construction webinar (no series name is printed; pages are tagged "Construction")
- **Format:** online, first Tuesday of the month, 10:00–11:30 am (time zone not printed on the pages; the firm is Iowa-based), 90 minutes. Registration and recordings through Zoom Events. Each page lists learning objectives. Cost: not stated. Continuing-education credit: not stated (the architects-and-engineers track states CEUs and AIA credit; this series does not).
- **Audience:** contractor owners and leaders, by the copy ("CEOs and entrepreneurs"; "a subcontractor's viewpoint"; "Contractors will be able to…"). Size: **not found**.
- **Who picks topics:** INFERENCE, from Maxim's catalog. Signals: (1) all 2026 titles and descriptions match Maxim's January 2026 training list word for word; (2) McMurray calls Maxim "one of our partners." The Dec 1 course is not in that January list, so at least one session was new.
- **2027 calendar:** not posted (the latest event on the site on Oct 18, 2026 is Dec 9, 2026).

| # | Date | Title | Moderator / speaker | Outside? Paid? | Recording | Page created |
|---|---|---|---|---|---|---|
| 1 | Tue Feb 3, 2026 | Strategic Planning – Putting Strategy First (a second page lists an 11:30 am–12:00 pm slot the same day) | not named | Maxim catalog title; speaker not named; payment not stated | Zoom on-demand | Jan 7, 2026 |
| 2 | Tue Mar 3 | Recruitment & Retention – Keys to Managing Risk & Increasing Profitability | not named | same | link, no on-demand label | Feb 11 |
| 3 | Tue Apr 7 | Improving Cash Flow and Inequitable Payment Practices | not named | same | on-demand | Feb 13 |
| 4 | Tue May 5 | Using Re-Organization Strategies for Tax Efficient Ownership Transitions | not named | same (Maxim catalog: "Ownership Transition Management Succession") | on-demand | Feb 13 |
| 5 | Tue Jun 2 | Cracking the 'WIP' – Driving Predictable Cost Projections | **McMurray** (his words) with "one of our partners at Maxim" | outside; payment not stated | on-demand | Feb 13 |
| 6 | Tue Jul 7 | Driving Organizational Performance and Innovation through Peer Groups | not named | Maxim runs paid peer groups (https://www.maximconsulting.com/peer-groups/) | on-demand | Feb 13 |
| 7 | Tue Aug 4 | Advanced Enterprise Budgeting and Forecasting | not named | same | **no** on-demand button | Feb 13 |
| 8 | Tue Sep 1 | Project Rescue (10:00–11:00) | not named | same | on-demand | May 21 |
| 9 | Tue Oct 6 | Key Performance Indicators 5.0 – Increasing Margin and Reducing Risk | **McMurray** / Michael Mclin, Managing Director, Maxim | outside; payment not stated | on-demand | Sep 14 |
| 10 | Tue Nov 3 | Change Order Management | **McMurray** / Stephane McShane, Director, Maxim | outside; payment not stated | register | Oct 5 |
| 11 | Tue Dec 1 | The Second in Command (built on Cameron Herold's book) | **McMurray** / David Morton, Director, Maxim | outside; payment not stated | register | Oct 12 |

Sources: the event pages under https://www.holmesmurphy.com/events/ (slugs: strategic-planning-putting-strategy-first, recruitment-retention-keys-to-managing-risk-increasing-profitability, improving-cash-flow-and-inequitable-payment-practices, using-re-organization-strategies-for-tax-efficient-ownership-transitions, cracking-the-wip-driving-predictable-cost-projections, driving-organizational-performance-and-innovation-through-peer-groups, advanced-enterprise-budgeting-and-forecasting, project-rescue, key-performance-indicators-5-0-increasing-margin-and-reducing-risk, change-order-management, the-second-in-command); creation times from `wp-json/wp/v2/events`; catalog https://maximconsulting.com/wp-content/uploads/2026/08/2026-Maxim-Full-Training-List-with-Descriptions.pdf

### Before 2026: what the construction track looked like
- 2024–2025 construction events were mostly in-house risk-and-safety webinars and OSHA courses (e.g., "Navigating Contractor Prequalification Platforms," Nov 13, 2024, "led by a Risk & Safety Professional"; "Crisis Management in Construction," Mar 15, 2024; "Strategies for Effective Injury Management," Jul 23, 2025; "Supervising for Safety and Performance Management," Nov 20, 2025), plus partner events: "2024 Economic and Construction Outlook" with BaseRock Partners (Apr 18, 2024, in person), a Travelers lunch-and-learn (Sep 11, 2025, Denver area), a Stinson seminar and rooftop happy hour (Oct 23, 2025; Kansas City per its registration URL `LE-102325-CRT-KC`, search-only), and **Building Forward**, an in-person Twin Cities series with Redpath and Company and Fabyanske, Westra, Hart & Thomson (Jun 18 and Sep 25, 2025; none listed in 2026). Wayback: https://web.archive.org/web/20260511092258/https://www.holmesmurphy.com/events/navigating-contractor-prequalification-platforms/ ; live: https://www.holmesmurphy.com/events/building-forward-managing-uncertainty-in-todays-environment-2/
- **Delta:** 2026 is the first year of a monthly owner-level business series (strategy, cash, succession, KPIs, leadership) as opposed to safety and insurance topics.

### Paid-speaker evidence

| Speaker | Grade | Evidence |
|---|---|---|
| Maxim consultants (Mclin, McShane, Morton) | B | Named outside presenters on every named session; payment not stated anywhere. Maxim sells this curriculum to associations and runs paid peer groups and advisory (capital advisory, ownership transition), so a free broker webinar is plausibly a lead source for Maxim. INFERENCE (signals: Maxim's association-education page; the series titles match its catalog; McMurray's word "partners"): a content partnership, not a booked fee. |
| Series grade | **B** | Outside speaker at every named session; pay not stated. Every 2026 slot went to one partner; no second outside presenter appeared. |

**Selling from the stage:** no stated policy. Each Holmes Murphy page ends in the firm's own calls to action; McMurray's companion post ends "Holmes Murphy's Construction team can help. Reach out today."

### Other rooms at the firm (for scale)
- **"The Power of Independence: Perpetuation of Privately Owned Business,"** Oct 28, 2026, half day, in person, Indian Hills Country Club, Mission Hills, Kansas, for "CFOs, CEOs, and business owners." Moderator Andrew Wank (Sr. Client Executive, Employee Benefits); outside panelists Roy Heinbach (Ryan Lawn & Tree), Shaun Kotwitz (GBA Companies), Kurt Fischer (INTRUST Bank) (pool file). https://www.holmesmurphy.com/events/the-power-of-independence-perpetuation-of-privately-owned-business-2/
- **Employee Benefits roundtables:** Nataliya Boychenko Stone hosted the Feb 2024 edition and wrote up the early-2025 one; the Feb 2024 and early-2025 editions were on AI, with CIO Dave Ashton, Chief Analytics Officer Jeffrey Austin White, Data Analytics Director Joe Schueller (spelled "Schuler" in the 2025 post) and Ali Payne (President, the subsidiary ethos). https://www.holmesmurphy.com/blog/navigating-the-ai-landscape-with-our-employer-roundtable/ · https://www.holmesmurphy.com/blog/exploring-our-future-key-insights-from-our-ai-and-tech-roundtable/
- **Architects and engineers webinar track** (monthly, 12:00–1:00 pm CT, 1 CEU, AIA credit; AXA XL premium-education credit): AI sessions Feb 27, 2025 ("Artificial Intelligence," run by Holmes Murphy Construction for design professionals), Aug 4, 2025 ("The Impacts of Artificial Intelligence") and Oct 22, 2026 ("Best Practices for Embracing AI in Design," Shaun Franklin of AXA XL and Nick Maletta of Holmes Murphy). https://www.holmesmurphy.com/wp-content/uploads/2026/01/AE-Continuing-Education-Webinars-2026-Invite.pdf · https://www.holmesmurphy.com/events/artificial-intelligence/
- **Cyber:** "Emerging AI Exposures," Jul 23, 2026 (Dan Cahlander with Amanda Novak of Constangy and Rich Servillas of RSM). https://www.holmesmurphy.com/events/emerging-ai-exposures-bridging-legal-cyber-security-and-risk-management/

---

## 4. The firm

- **What it is:** "one of the nation's largest privately held insurance brokerages," founded 1932, employee-owned through employee-shareholders; "more than 1,000 employees" (Jan 2023). Chairman and CEO **Dan Keough**; President **Jay Reavis** (named Jul 15, 2026). https://www.holmesmurphy.com/news/jay-reavis-named-holmes-murphy-president/ · https://www.holmesmurphy.com/blog/meet-holmes-murphys-newest-game-changers/
- **Construction practice size:** "over 200 employees across the country that focus exclusively on the industry" (McMurray, Sep 25, 2025).
- **Captive family:** Innovative Captive Strategies and Global Captive Management are Holmes Murphy companies (footer, "PLUS Companies"); in-person captive events in Oct 2026 ("Captives & Clays," Utah, Oct 1; "Captives & Cocktails," Kansas City, Oct 8) list other speakers (Sam Webb, Ryan Moriarty; Brett Stefani, Rocky Lenzini, Drew Ison) (search-only).
- **Hiring (Workday, Oct 18, 2026):** 57 open roles; a construction-focused Sr. Client Service Consultant (Minneapolis, Oct 14); an Event Management Intern for summer 2027 (Oct 15); no AI-adoption role.

### The firm's AI stance (dated)
- **Feb 12, 2024:** Employer Experience Roundtable on AI, hosted by Nataliya Boychenko Stone. https://www.holmesmurphy.com/blog/navigating-the-ai-landscape-with-our-employer-roundtable/
- **Mar 13, 2025:** "At Holmes Murphy, we've seen AI's benefits firsthand with our Hey Holmes internal AI tool, which has helped draft job descriptions, improve email communication, and enhance presentations." https://www.holmesmurphy.com/blog/exploring-our-future-key-insights-from-our-ai-and-tech-roundtable/
- **Mar 5, 2025:** Data Analytics Director Joe Schueller in *Leader's Edge* on hackathons and AI. https://www.holmesmurphy.com/news/holmes-murphy-data-analytics-expert-discusses-ai-in-insurance-with-leaders-edge/
- **Apr 1, 2026:** "in 2025, we completed a comprehensive exercise to identify opportunities for applying AI across the insurance product life cycle… many of the most promising opportunities align with middle- and back-office functions." CIO Dave Ashton: "The next step will be to put more formality around the business case, the business benefits, the savings." https://www.holmesmurphy.com/news/holmes-murphy-cio-dave-ashton-speaks-to-the-use-of-ai-in-the-insurance-industry/
- **Apr 7, 2026:** Holmes Base, a Salesforce Financial Services Cloud platform for property casualty, with "AI‑enabled search." https://www.holmesmurphy.com/news/holmes-murphy-unveils-holmes-base-a-transformational-platform-modernizing-the-future-of-insurance-operations/
- **Undated, live Oct 2026:** a candidate AI policy: AI welcome for preparation, not during live interviews; "We know this is an evolving space, and we are continuing to learn alongside it." https://www.holmesmurphy.com/careers/artificial-intelligence-tools-policy/
- **Aug 31 – Sep 2, 2026:** BrokerTech Connect: Chicago (BrokerTech Ventures; Keough co-CEO), sessions on "artificial intelligence, change management." https://www.holmesmurphy.com/news/brokertech-connect-chicago-announces-growing-sponsor-lineup-and-industry-programming/
- **DNS (holmesmurphy.com TXT, Oct 18, 2026):** Microsoft 365 (SPF `spf.protection.outlook.com`), Salesforce, HubSpot, Mandrill, SendGrid, Qualtrics, Exclaimer, Zywave, DocuSign, Zoom, Apple and Google verification; Cisco IronPort mail gateways (MX `esa1/esa2.holmesmurphy.iphmx.com`). **No `anthropic-domain-verification` or `openai-domain-verification` record.**
- **Read:** the firm is public and specific about AI inside its own operations and in benefits, cyber and design-risk content. Its contractor-owner room has not carried an AI session.

---

## 5. Handles
- **Holmes Murphy:** YouTube `@holmesmurphy` (105 videos); X `holmesmurphyins`; Facebook `holmesmurphyins`; Instagram `holmesmurphyins`; LinkedIn `company/holmes-murphy` (not opened). From the site footer.
- **Jason McMurray:** WordPress author 74 on holmesmurphy.com; headshots `Jason-McMurray_20_PD.jpg` (2023) and `Jason-McMurray_25_PD.jpg` (2026). Personal handles: see the person file, section 7.
- **Maxim Consulting Group:** maximconsulting.com.
