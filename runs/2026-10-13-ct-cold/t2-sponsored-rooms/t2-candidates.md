# T2 — Sponsored rooms: firms that host AI education for business-owner clients

**Date:** 2026-10-13 (work window 15:04–16:01 ET, about 57 minutes)
**Researcher:** T2 subagent (read-only; no contact, no logins, no LinkedIn/Facebook/Instagram/X)
**Result:** 20 firms reached (target 20). Mix: 9 CPA/accounting, 4 business insurance brokers, 3 PEO/HR outsourcing, 3 business law firms, 1 community bank. **0 wealth-management/private-banking firms and 0 commercial real estate brokers** were confirmed.

## What was searched
- Web search across firm types (CPA, regional/community bank, PEO, wealth/private bank, business insurance broker, CRE broker, business law) with AI + "business owners" + webinar/breakfast/roundtable/summit phrasing. The search tool returned mostly conferences for bankers/CPAs, not client events, so most finds came from the second method.
- Direct fetch (curl + WebFetch) of roughly 250 firm "events" pages: ~90 regional CPA firms, ~80 law firms, ~100 community/regional banks, ~25 insurance brokers, ~10 PEOs, ~8 wealth/trust firms. Pages were scanned for AI/ChatGPT/generative terms, and each hit was opened and read on the primary event page.
- Speaker check: only the Weintraub keynote was checked for a speakers-bureau listing (see below). Others are marked "not checked".

## What was blocked or missing
- **HTTP 403 (bot block/Cloudflare):** pbmares.com, keitercpa.com, windes.com, bergankdv.com, weaver.com, armanino.com, citrincooperman.com, yeoandyeo.com, crowe.com, offitkurman.com, icemiller.com, spencerfane.com, polsinelli.com, broadway.bank, pnfp.com (Pinnacle), firstmerchants.com, qcrh.com, cadencebank.com, bankerstrust.com, southstatebank.com, amerisbank.com, ifinancial.com, insperity.com, justworks.com, hubinternational.com.
- **429/522 (rate limit/down):** wipfli.com, pkm.com, lockton.com.
- **JavaScript-only pages (no text came back):** events.trinet.com/summerseries26, webinars.paychex.com/ai-for-small-business-series. Speaker names for TriNet and Paychex could not be read.
- **Not accessible to the search tool:** bizjournals.com.
- **The web-search budget ran out at about 16:00 ET.** After that, only direct fetches of known firm URLs were used. Bank, wealth and CRE coverage is thin because those firms rarely post client events on public pages.
- Most bank `/events` URLs returned 404. Of the ~100 bank pages tried, none listed an AI event except the one below.

## Grade key (paid-speaker evidence)
A = clear outside paid speaker (named outside keynote). B = outside speaker, payment unclear. C = in-house only. D = no evidence (speakers not shown).
"Unverified" = not confirmed on the primary page.

---

## 1. Weintraub Tobin — business law firm
- **Type / region:** Business law firm; Sacramento, CA
- **Website:** https://www.weintraub.com
- **Event:** "2026 Business Focus Seminar – AI and Value Creation: Strategic Considerations for Business Leaders." September 10, 2026, 3:30–6:30 PM PT, Harper Alumni Center, Sacramento State. Free with registration; the first 50 registrants got a copy of the keynote's book. Audience: executives, founders and business leaders.
  - https://www.weintraub.com/2026/06/2026-business-focus-seminar-ai-and-value-creation-strategic-considerations-for-business-leaders/
  - (also posted at https://www.weintraub.com/2026/08/2026-business-focus-seminar-ai-and-value-creation-strategic-considerations-for-business-leaders/)
- **Presenter:** Outside keynote: **Kavita Ganesan, Ph.D.**, author of *The Business Case for AI* and founder of Opinosis Analytics. The page says other "industry experts" will speak but does not name them.
  - **Speakers bureau:** No bureau listing was found. Her own site has a speaking page with a "BOOK KAVITA" call to action (https://kavita-ganesan.com/speaking/), which shows she speaks professionally. Her site does not list this event.
- **Host person:** No host named. Events page: https://www.weintraub.com/category/events/business-focus/
- **Paid-speaker evidence:** **A.** A named outside professional keynote, and the firm bought books for attendees. No fee is stated.
- **Repeat evidence:** This is an annual series. The 2025 page calls it the "11th Annual Business Focus event" (September 24, 2025, co-presented with BFBA and CVF Capital Partners; an M&A panel, not AI): https://www.weintraub.com/2025/09/2025-business-focus-seminar-turning-headwinds-into-tailwinds-mas-resilient-future/
  - Past editions on the category page: 2023 ("Transitioning Your Business in a Volatile Economy") and 2024 ("Preparing a Business Sale to Maximize Value"). 2020 edition: https://www.weintraub.com/?p=11005

## 2. Rea & Associates (Rea Business Advisors) — CPA firm
- **Type / region:** CPA/advisory firm; Ohio (New Philadelphia HQ, with Wooster, Dublin and Cleveland events)
- **Website:** https://www.reacpa.com / https://reaadvisory.com
- **Event 1:** "Building Smarter: Practical AI for the Construction Industry." Webinar, April 28, 2026, 12:00 PM, one hour. Audience: construction owners, project executives, operations leaders.
  - https://reaadvisory.com/events/building-smarter-practical-ai-for-the-construction-industry/
- **Event 2:** "Rea Manufacturing Education Day 2026 — Manufacturing in the Age of AI." Wooster, October 2, 2026 (Arden Shisler Conference Center). The same program runs in Dublin on October 23 and in Cleveland (Independence) on October 30. Audience: manufacturing leaders.
  - https://reaadvisory.com/?p=278478
  - Save-the-date post (August 12, 2026): https://reaadvisory.com/?p=278469
- **Presenters:**
  - Event 1: Rea Information Services (no individual named) plus outside presenter **Alex Ryan, CEO of Ryshe** (a data and AI consultancy). Bureau check not done.
  - Event 2: a featured session from **Heartland Ventures** (an outside organization; presenter not named), plus a "Manufacturing Leaders in Conversation" panel (names not given).
- **Host person:** No host named. The save-the-date post was written by Ryan Brickwood (title not found). Events page: https://www.reacpa.com/events
- **Paid-speaker evidence:** **B.** Outside presenters at both events; payment not stated.
- **Repeat evidence:** Manufacturing Education Day is a yearly event. AI is the 2026 theme.
  - 2024: https://reacpa.com/insight/forge-ahead-rea-manufacturing-education-day-2024
  - 2023: https://go.reacpa.com/LE-2023-10-08-ManufactoringDay_LP-Registration.html
  - 2022: https://mfgday.com/events/rea-mfgday22

## 3. Withum — CPA firm
- **Type / region:** CPA/advisory firm; national, with a Philadelphia event. Freed Maxick's events page now redirects to Withum.
- **Website:** https://www.withum.com
- **Event 1:** "The New Risk Frontier: AI, Cyber Defense and Insurance Strategies." In-person breakfast seminar, free. November 5, 2026, 8:00–10:00 AM ET, Fitler Club, Philadelphia. Co-hosted with Johnson Kendall Johnson (entry 4) "in partnership with the Chamber of Commerce for Greater Philadelphia." Audience: business leaders and decision-makers. **Scheduled, not yet held.**
  - https://www.withum.com/events/the-new-risk-frontier-ai-cyber-defense-and-insurance-strategies/
- **Event 2:** "HLB Global Webinar – AI in Manufacturing: What Works, What Doesn't and What's Next." On-demand; original date not shown.
  - https://www.withum.com/events/ai-in-manufacturing-what-works-what-doesnt/
- **Presenters:**
  - Event 1: Chris Mangano (Withum) and Alexandra Bretschneider (Johnson Kendall Johnson, outside).
  - Event 2: Wally Merkas and Andrea Mondello (Withum), plus Tom Shemanski (Rehmann / HLB USA, outside), plus two unnamed clients.
  - Bureau check not done.
- **Host person:** No host named. Event 2 lists Walter (Wally) Merkas, Partner and Market Leader, Business and Management Consulting Services, as a contact. Events page: https://www.withum.com/events/
- **Paid-speaker evidence:** **B.** Outside speakers are partner firms (co-marketing), and payment is unlikely.
- **Repeat evidence:** The events page lists several other AI sessions ("From Strategy to Adoption: Making AI Work for Not-for-Profits," "Driving AI Transformation," "AI-Powered Legacy Modernization"): https://www.withum.com/events/

## 4. Johnson Kendall Johnson — business insurance broker
- **Type / region:** Insurance broker; Philadelphia area. The firm type was not described on the event page.
- **Website:** not found (unverified)
- **Event:** Co-host of the Withum breakfast, "The New Risk Frontier: AI, Cyber Defense and Insurance Strategies," November 5, 2026, Philadelphia. **Scheduled, not yet held.**
  - https://www.withum.com/events/the-new-risk-frontier-ai-cyber-defense-and-insurance-strategies/
- **Presenter:** Alexandra Bretschneider (JKJ; title not listed), presenting with Withum.
- **Host person:** No host named. Alexandra Bretschneider is the JKJ presenter (title not found). Source as above.
- **Paid-speaker evidence:** **C.** Speakers come from the two co-hosts. The event is co-sponsored, so JKJ is helping pay for the room.
- **Repeat evidence:** not found

## 5. Marsh McLennan Agency (MMA) — business insurance broker
- **Type / region:** Business insurance/benefits broker; national, with regional offices
- **Website:** https://www.marshmma.com
- **Event 1:** "AI Compliance & Cybersecurity: Reducing Risk Across Your Organization." Webinar in the "Law & Policy" series. October 15, 2026, 2 PM ET, 60 minutes. Offers HRCI/SHRM credit. Audience: listed as "HR Leaders"; the description says business leaders and risk professionals. **Scheduled, not yet held.**
  - https://www.marshmma.com/us/events/details/webinar-law-and-policy-october-2026.html
- **Event 2:** "Cyber Liability & AI Roundtable." June 17, 2026, 12–2 PM, at MMA, 1166 6th Avenue, New York. Listed by Whiteford (entry 20); speakers not named.
  - https://www.whitefordlaw.com/news-events/cyber-liability-ai-roundtable
- **Presenters (Event 1):** Mario Paez (EVP, National Cyber Risk Practice Leader), Tom Fuhrman (Senior Cybersecurity Consultant, Marsh), and outside panelist **Karen Bridges** (Counsel, McDonald Hopkins).
  - McDonald Hopkins also lists the webinar: https://www.mcdonaldhopkins.com/events/ai-compliance-cybersecurity-reducing-risk-across-your-organization
  - Bureau check not done.
- **Host person:** No individual host named. The host is MMA's Cybersecurity Advisory Services team. Events page: https://www.marshmma.com/us/events.html
- **Paid-speaker evidence:** **B.** The outside speaker is a law-firm attorney, and payment is unlikely.
- **Repeat evidence:** The Law & Policy webinar is a series; the page shows related sessions in September, November and December 2026 (same URL as above).

## 6. Holmes Murphy — business insurance broker
- **Type / region:** Insurance/risk broker; Des Moines, IA (Midwest)
- **Website:** https://www.holmesmurphy.com
- **Event:** "Emerging AI Exposures: Bridging Legal, Cyber Security, and Risk Management." Webinar, July 23, 2026, 10:30–11:30 AM. Now on demand.
  - https://www.holmesmurphy.com/events/emerging-ai-exposures-bridging-legal-cyber-security-and-risk-management
- **Presenters:**
  - Dan Cahlander, Cyber Risk Practice Leader (Holmes Murphy)
  - Outside: **Amanda Novak**, Senior Counsel, Constangy Brooks Smith & Prophete
  - Outside: **Rich Servillas**, Director, Security Privacy and Risk Consulting, RSM
  - Bureau check not done.
- **Host person:** No host or moderator named. Events page: https://www.holmesmurphy.com/events/
- **Paid-speaker evidence:** **B.** Two outside speakers; payment not stated.
- **Repeat evidence:** An earlier AI webinar, "The Impacts of Artificial Intelligence," was held August 4, 2025 (for architect/engineer clients; just outside the 12-month window): https://www.holmesmurphy.com/events/the-impacts-of-artificial-intelligence
  - A third AI event, "Best Practices for Embracing AI in Design," is listed on the events page (date not checked).

## 7. Newfront — business insurance broker
- **Type / region:** Insurance broker; San Francisco (national)
- **Website:** https://www.newfront.com
- **Event:** "Mind the Gap: Where AI Risk Meets Insurance Coverage." One-hour webinar, June 17, 2026.
  - https://www.newfront.com/events/mind-the-gap-where-ai-risk-meets-insurance-coverage
- **Presenters:**
  - Jennifer Wilson, Head of Cyber (Newfront)
  - Dereick Wood, ERS Head of Claims (Newfront)
  - Outside: **Caitlin Alpern**, Team Lead Large Accounts, AXA XL (an insurance carrier)
- **Host person:** No host named. Events page: https://www.newfront.com/events
- **Paid-speaker evidence:** **B.** The outside speaker is a carrier partner, and payment is unlikely.
- **Repeat evidence:** not found

## 8. Guthrie County State Bank — community bank
- **Type / region:** Community bank; Guthrie Center, Iowa
- **Website:** https://www.gcsbank.com
- **Event:** "Small Business Seminar: Your AI Playbook." October 23, 2025, 6:00–7:30 PM, Guthrie Activity Center. Free. Audience: small business owners.
  - https://www.gcsbank.com/seminar/
- **Presenters:** "Guest speakers and fellow small business owners":
  - **Shadley Grei**, Innovation Strategist, Grei Matter
  - **Andrew Cusack**, Marketing Director, On Pitch
  - Bureau check not done.
- **Host person:** No host named. The only contact is the general page https://www.gcsbank.com/contact-us/
- **Paid-speaker evidence:** **B.** Outside speakers; payment not stated.
- **Repeat evidence:** The bank says it runs "a variety of seminars, including Ag Days, Small Business Days, and fraud information seminars" (same URL). No past AI editions were found.
- **Fit note:** A very small bank. Its clients are likely smaller than 25–100 employees.

## 9. TriNet — PEO
- **Type / region:** PEO; national (Dublin, CA)
- **Website:** https://www.trinet.com
- **Event:** "TriNet Summer Series" (2026), a weekly 30-minute webinar series for small and mid-size business leaders. AI sessions:
  - "How AI Is Transforming HR and Employee Experience" (Week 1; June 23, 2026 per a search-result summary of trinet.com/events — **unverified**)
  - "Electric AI – HR and IT Alignment Can Drive Productivity"
  - "AI & The Planet"
  - On-demand list: https://www.trinet.com/resources/webinars/on-demand-webinars
  - Series page (could not be read; JavaScript only): https://events.trinet.com/summerseries26
- **Presenters:** not found. The page could not be read. The "Electric AI" title suggests an outside IT vendor (Electric) took part — **unverified**.
- **Host person:** No host named. Events page: https://trinet.com/events
- **Paid-speaker evidence:** **D** on what was visible. A partner speaker is possible.
- **Repeat evidence:** Recurring programs:
  - Summer Series 2026 (above)
  - National Small Business Week Summit 2025, with sessions "AI and Privacy Considerations for SMBs" and "Using AI to Make Smarter Healthcare Decisions" (May 6–8, 2025; outside the 12-month window): https://www.trinet.com/resources/webinars/nsbws-2025-ai-and-privacy-considerations-for-smbs

## 10. Paychex — PEO / HR outsourcing
- **Type / region:** Payroll/HR firm with a PEO line (Paychex PEO); Rochester, NY (national)
- **Website:** https://www.paychex.com
- **Event:** "AI for Small Business Series: A Practical Guide." A free 5-part webinar series.
  - Registration link was posted on the Paychex Thrive "Week in Review" podcast page dated May 28, 2026: https://www.paychex.com/worx/podcasts/business/week-in-review-season-6-episode-29
  - Series page (could not be read; JavaScript only): https://webinars.paychex.com/ai-for-small-business-series/
  - Live dates of June 3–July 1, Wednesdays 2 PM ET came from a search-result summary only — **unverified**.
- **Presenters:** not found. The podcast host is Gene Marks; it is **unverified** whether he presented the webinars.
- **Host person:** not found
- **Paid-speaker evidence:** **D**
- **Repeat evidence:** A 5-part series (dates unverified)
- **Fit note:** A very large company. It is a weak sponsor target, but its clients fit.

## 11. G&A Partners — PEO
- **Type / region:** PEO; Houston, TX
- **Website:** https://www.gnapartners.com
- **Event:** "Before You Bring AI Into HR: A Decision Framework." Webinar, September 15, 2026, now a replay. The page says "Business owners and leaders joined…"
  - https://www.gnapartners.com/resources/webinars/before-you-bring-ai-into-hr
- **Presenters:** In-house: Nick Seewer, VP Data, Analytics & AI (featured speaker)
- **Host person:** **Alex Osborne, Vice President, Client Success (named "Host")**. Source: same URL.
- **Paid-speaker evidence:** **C**
- **Repeat evidence:** Filed under "Technology Webinars" on https://www.gnapartners.com/resources/webinars. No other AI editions were found.

## 12. The Bonadio Group — CPA firm
- **Type / region:** CPA/advisory firm; Rochester/Upstate NY and Northeast
- **Website:** https://www.bonadio.com
- **Event 1:** "Practical Ways to Use AI in Your Organization – Are You In the Sweet Spot?" Webinar (Microsoft Teams), November 4, 2026, 12–1 PM. **Scheduled, not yet held.**
  - https://www.bonadio.com/event/practical-ways-to-use-ai-in-your-organization-webinar/
- **Event 2:** "AI at the Edge: How Leaders Stay Ahead Without Going Over the Cliff." "C-Suite Webinar," December 10, 2026, 2–3 PM. **Scheduled, not yet held.**
  - https://www.bonadio.com/event/ai-how-leaders-stay-ahead-webinar/
- **Presenters:** In-house:
  - Chris Salone, Principal, FoxPointe Solutions (both events)
  - Alex Kingston, Principal, Outsource Accounting & Finance (Event 1)
- **Host person:** **Tim Ball, Partner, Leader of Bonadio Advisory & Consulting (moderator of both)**. Source: both URLs.
- **Paid-speaker evidence:** **C**
- **Repeat evidence:** Two AI webinars in one season; no series name. No past AI events were confirmed in the window.

## 13. Abdo — CPA firm
- **Type / region:** CPA/advisory firm; Minneapolis, MN
- **Website:** https://abdosolutions.com
- **Event:** "AI in Plain English: What Real Estate & Construction Owners Need to Know." Zoom webinar, August 6, 2026, 11 AM–12 PM CT. Audience: real estate and construction business owners.
  - https://abdosolutions.com/ai-in-plain-english-what-real-estate-construction-owners-need-to-know/
- **Presenters:** Not named ("our team"). In-house is likely — **unverified**.
- **Host person:** No host named. Contact info@abdosolutions.com. Events page: https://www.abdosolutions.com/events
- **Paid-speaker evidence:** **C** (likely in-house)
- **Repeat evidence:** not found
- **Fit note:** Squarely aimed at business owners.

## 14. SVA Certified Public Accountants — CPA firm
- **Type / region:** CPA firm; Madison, WI
- **Website:** https://www.sva.com
- **Event:** "AI in Your Dental Practice: Practical Ways to Save Time, Reduce Costs, and Improve Operations." Webinar, now offered as a recording. Original date not stated — **unverified whether it falls in the 12-month window**.
  - https://accountants.sva.com/ai-in-your-dental-practice-practical-ways-to-save-time-reduce-costs-and-improve-operations-webinar-download-lp
- **Presenters:** In-house: Evan Conroy (Principal, SVA Consulting) and Caterina Mora (AI & Analytics Consultant, SVA Consulting)
- **Host person:** No host named. Events page: https://www.sva.com/events
- **Paid-speaker evidence:** **C**
- **Repeat evidence:** not found
- **Fit note:** The audience is owner-led dental practices.

## 15. Cherry Bekaert — CPA firm
- **Type / region:** CPA/advisory firm; Southeast (event in Greenville, SC)
- **Website:** https://www.cbh.com
- **Event:** "Scaling AI While Strengthening Cybersecurity: Strategies for Growth and Resilience." In-person breakfast, Wednesday October 21 (year not listed; listed as upcoming, so likely 2026), 8:30–11 AM, Greenville, SC. Audience: executive directors, CFOs, controllers.
  - https://events.cbh.com/scaling-ai-strengthening-cybersecurity-greenville
- **Presenters:** In-house:
  - Supreet Singh, Partner, AI & Automation Leader
  - Jim Holman, Director, Technology Advisory Services
  - Dan Sembler, Partner, Cybersecurity
- **Host person:** **Sarah Easley (event contact; title not found)**. Source: same URL.
- **Paid-speaker evidence:** **C**
- **Repeat evidence:** not found
- **Fit note:** "Executive directors" suggests a mostly nonprofit audience.

## 16. Schneider Downs — CPA firm
- **Type / region:** CPA/advisory firm; Pittsburgh, PA
- **Website:** https://schneiderdowns.com
- **Event:** "From Dispatch to Decisions: Creating an AI-Ready Transportation Organization." Webinar (ON24), November 10, 2026, 1 PM ET. **Scheduled, not yet held.**
  - https://schneiderdowns.com/events/from-dispatch-to-decisions-creating-an-ai-ready-transportation-organization/
- **Presenters:** In-house: Mike Scalamogna and David James (Managers, SD Digital)
- **Host person:** **Lindsay Sherrill (registration contact; title not found)**. Source: same URL.
- **Paid-speaker evidence:** **C**
- **Repeat evidence:** A second AI event is listed, "Putting the AI in AICPA: What the New TQA Means for Your SOC Report" (aimed at SOC clients; not opened): https://schneiderdowns.com/events/aicpa-ai-soc-guidance/

## 17. Elliott Davis — CPA firm
- **Type / region:** CPA/advisory firm; Southeast (Greenville, SC HQ)
- **Website:** https://www.elliottdavis.com
- **Event:** "The Finance Leader's AI Playbook: What's Real, Where to Start, and What to Ask." Interactive webinar, October 29, 2026. Free, 1 hour of CPE. Audience: finance leaders at manufacturing and distribution companies. **Scheduled, not yet held.**
  - https://www.elliottdavis.com/events/the-finance-leaders-ai-playbook-whats-real-where-to-start-and-what-to-ask
- **Presenters:** not found (not named on the page)
- **Host person:** **Laura Preslar (event contact; title not found)**. Source: same URL.
- **Paid-speaker evidence:** **D**
- **Repeat evidence:** not found
- **Fit note:** Aimed at finance leaders (CFOs) rather than owners.

## 18. Quarles & Brady — business law firm
- **Type / region:** Law firm; Milwaukee, WI (Midwest and national)
- **Website:** https://www.quarles.com
- **Event:** "Artificial Intelligence Webinar Series," held quarterly.
  - 2026 sessions (on demand): Q1 "Navigating the Terrain to Bring AI-Enabled Products and Services to Market," Q2 "AI Legislation and Enforcement Update," Q3 "AI Across the Industries"
  - Upcoming: "Everything You Wanted to Know About AI but Were Afraid to Ask," November 12, 2026, 12–1 PM CT
  - https://www.quarles.com/newsroom/events/artificial-intelligence-webinar-series
- **Presenters:** In-house Quarles AI team (e.g., Heather Buchta, Meghan O'Connor, Jonathan Stone)
- **Host person:** No moderator named. **Event contacts: Lauren Klika and Alexa Curto (events@quarles.com; titles not found)**. Source: same URL.
- **Paid-speaker evidence:** **C**
- **Repeat evidence:** Strong. Four parts in 2025 (including "The Breakfast Club: AI 101" and "Practically Implementing AI") and quarterly sessions in 2026 (same URL).
- **Fit note:** Offers CLE credit, so the audience is mixed (in-house counsel and businesses).

## 19. Bose McKinney & Evans — business law firm
- **Type / region:** Law firm; Indianapolis, IN
- **Website:** https://www.boselaw.com
- **Event:** "Managing Risk in the Modern Workplace: Discrimination, AI, Criminal Issues and Remote Work." Employer seminar, November 13, 2026, 8:45 AM–2 PM, 502 East Event Centre, Carmel, IN. $99 including lunch. **Scheduled, not yet held.** AI is one of four topics.
  - https://www.boselaw.com/2026/10/bose-mckinney-evans-hosting-seminar-for-employers-managing-risk-in-the-modern-workplace-discrimination-ai-criminal-issues-and-remote-work/
- **Presenters:** Firm attorneys (Labor & Employment Group; not named)
- **Host person:** **Kaitlyn Brown (contact, kbrown@boselaw.com; title not found)**. Source: same URL.
- **Paid-speaker evidence:** **C**
- **Repeat evidence:** not found
- **Fit note:** The audience is employers/HR; AI is only partly the theme.

## 20. Whiteford, Taylor & Preston — business law firm
- **Type / region:** Law firm; Baltimore, MD (Mid-Atlantic); event held in New York
- **Website:** https://www.whitefordlaw.com
- **Event:** "Cyber Liability & AI Roundtable." June 17, 2026, 12–2 PM, at Marsh McLennan Agency, 1166 6th Avenue, New York.
  - https://www.whitefordlaw.com/news-events/cyber-liability-ai-roundtable
  - The page does not say whether MMA co-hosted (unverified).
- **Presenters:** not found
- **Host person:** No host named. Contact: events@whitefordlaw.com. Events page: https://www.whitefordlaw.com/events
- **Paid-speaker evidence:** **D**
- **Repeat evidence:** not found. Whiteford also sponsors outside AI events, e.g., "AI & A2J Summit – Whiteford Sponsoring" (listed on the events page).

---

## Adjacent leads (not counted — the firm sponsored or spoke but did not host, or the firm type is outside scope)
- **Johnson Financial Group** (bank/wealth/insurance, Wisconsin; firm type unverified on page) is the **Reception sponsor** of the Fox Cities Chamber "2026 AI Business Summit," November 3, 2026, Appleton, WI. The keynote is futurist Rebecca Ryan. https://members.foxcc.net/chamber-events/Details/2026-ai-business-summit-1553598?sourceTypeId=Website
- **First Community Bank, FNBC Bank, Bank OZK, First Security Bank, Simmons Bank** co-sponsored the Arkansas SBTDC free seminar "harnessing the power of AI in business," December 4, 2025, Jonesboro, AR. The speaker was Alyson Lewis. The host was the SBTDC, not a bank. https://jonesbororightnow.com/news/268862-a-state-hosting-free-seminar-on-ai-in-business/
- **Expansion Capital Group** (fintech lender, not a bank) hosted "Beyond the Hype – A Panel Discussion on AI for Small Business," May 7, 2026, Sioux Falls, SD. Four outside panelists; the host was CEO Tim Mages. https://siouxfalls.business/upcoming-event-to-help-small-business-owners-go-beyond-the-hype-with-ai/
- **McDonald Hopkins** (law firm) is a speaker at the MMA webinar, not a host. https://www.mcdonaldhopkins.com/events
- **Koley Jessen** (law firm, Omaha) gave the seminar "Beyond the Chatbot: Exploring Opportunities and Risks of Agentic AI" (May 6, 2026) inside the 3rd Annual IDEA Forum. It was not a firm-hosted room. https://www.koleyjessen.com/insights/events/beyond-the-chatbot-exploring-opportunities-and-risks-of-agentic-ai

## Gaps
- **Wealth management / private banking:** none confirmed. Event pages checked: mariner.com/events, fiduciarytrust.com/events, bessemertrust.com/events (no AI events). Glenmede, Brown Advisory, Chevy Chase Trust, Wilmington Trust and Northern Trust had no public events page or returned 404.
- **Commercial real estate brokers:** none confirmed. Search found only industry conferences (CREtech, SIOR), not client events.
- **Banks:** only one confirmed host (entry 8). Rockland Trust has a "Business Strategy Series" for owners with outside experts, but it had no AI session in 2025–26: https://www.rocklandtrust.com/small-business/rockland-trust-business-strategy-series

---

## Sources
- https://www.weintraub.com/2026/06/2026-business-focus-seminar-ai-and-value-creation-strategic-considerations-for-business-leaders/
- https://www.weintraub.com/2026/08/2026-business-focus-seminar-ai-and-value-creation-strategic-considerations-for-business-leaders/
- https://www.weintraub.com/2025/09/2025-business-focus-seminar-turning-headwinds-into-tailwinds-mas-resilient-future/
- https://www.weintraub.com/category/events/business-focus/
- https://www.weintraub.com/?p=11005
- https://kavita-ganesan.com/speaking/
- https://kavita-ganesan.com/
- https://reaadvisory.com/events/building-smarter-practical-ai-for-the-construction-industry/
- https://reaadvisory.com/?p=278478
- https://reaadvisory.com/?p=278469
- https://www.reacpa.com/events
- https://reacpa.com/insight/forge-ahead-rea-manufacturing-education-day-2024
- https://go.reacpa.com/LE-2023-10-08-ManufactoringDay_LP-Registration.html
- https://mfgday.com/events/rea-mfgday22
- https://www.withum.com/events/the-new-risk-frontier-ai-cyber-defense-and-insurance-strategies/
- https://www.withum.com/events/ai-in-manufacturing-what-works-what-doesnt/
- https://www.withum.com/events/
- https://www.freedmaxick.com/events/
- https://www.marshmma.com/us/events/details/webinar-law-and-policy-october-2026.html
- https://www.marshmma.com/us/events.html
- https://www.mcdonaldhopkins.com/events/ai-compliance-cybersecurity-reducing-risk-across-your-organization
- https://www.mcdonaldhopkins.com/events
- https://www.whitefordlaw.com/news-events/cyber-liability-ai-roundtable
- https://www.whitefordlaw.com/events
- https://www.holmesmurphy.com/events/emerging-ai-exposures-bridging-legal-cyber-security-and-risk-management
- https://www.holmesmurphy.com/events/the-impacts-of-artificial-intelligence
- https://www.holmesmurphy.com/events/
- https://www.newfront.com/events/mind-the-gap-where-ai-risk-meets-insurance-coverage
- https://www.newfront.com/events
- https://www.gcsbank.com/seminar/
- https://www.gcsbank.com/contact-us/
- https://trinet.com/events
- https://www.trinet.com/resources/webinars/on-demand-webinars
- https://events.trinet.com/summerseries26 (JavaScript only; unreadable)
- https://www.trinet.com/resources/webinars/nsbws-2025-ai-and-privacy-considerations-for-smbs
- https://www.paychex.com/worx/podcasts/business/week-in-review-season-6-episode-29
- https://webinars.paychex.com/ai-for-small-business-series/ (JavaScript only; unreadable)
- https://www.gnapartners.com/resources/webinars/before-you-bring-ai-into-hr
- https://www.gnapartners.com/resources/webinars
- https://www.bonadio.com/event/practical-ways-to-use-ai-in-your-organization-webinar/
- https://www.bonadio.com/event/ai-how-leaders-stay-ahead-webinar/
- https://www.bonadio.com/events/
- https://abdosolutions.com/ai-in-plain-english-what-real-estate-construction-owners-need-to-know/
- https://www.abdosolutions.com/events
- https://accountants.sva.com/ai-in-your-dental-practice-practical-ways-to-save-time-reduce-costs-and-improve-operations-webinar-download-lp
- https://www.sva.com/events
- https://events.cbh.com/scaling-ai-strengthening-cybersecurity-greenville
- https://www.cbh.com/events/
- https://schneiderdowns.com/events/from-dispatch-to-decisions-creating-an-ai-ready-transportation-organization/
- https://schneiderdowns.com/events/aicpa-ai-soc-guidance/
- https://schneiderdowns.com/events/
- https://www.elliottdavis.com/events/the-finance-leaders-ai-playbook-whats-real-where-to-start-and-what-to-ask
- https://www.elliottdavis.com/events/
- https://www.quarles.com/newsroom/events/artificial-intelligence-webinar-series
- https://www.boselaw.com/2026/10/bose-mckinney-evans-hosting-seminar-for-employers-managing-risk-in-the-modern-workplace-discrimination-ai-criminal-issues-and-remote-work/
- https://www.boselaw.com/events
- https://members.foxcc.net/chamber-events/Details/2026-ai-business-summit-1553598?sourceTypeId=Website
- https://jonesbororightnow.com/news/268862-a-state-hosting-free-seminar-on-ai-in-business/
- https://siouxfalls.business/upcoming-event-to-help-small-business-owners-go-beyond-the-hype-with-ai/
- https://www.koleyjessen.com/insights/events/beyond-the-chatbot-exploring-opportunities-and-risks-of-agentic-ai
- https://www.rocklandtrust.com/small-business/rockland-trust-business-strategy-series
- https://www.zionsbank.com/personal/community/business-educational-webinars/
- https://greenareachamber.org/quarterly-lunch/
- https://www.eventbrite.com/e/bbo-breakfast-for-business-owners-with-sean-kouplen-ceo-of-regent-bank-tickets-1984058370997
- https://www.mariner.com/events/
- https://www.fiduciarytrust.com/events
- https://www.bessemertrust.com/events
