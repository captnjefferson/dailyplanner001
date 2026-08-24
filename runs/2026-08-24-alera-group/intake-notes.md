# INTAKE — Alera Group, Head of AI (req 7564)
## 2026-08-24

Intake discipline per CLAUDE.md rule 2: no working URL → **delete, don't soften.** A wrong specific is fatal; a missing one is not.

---

## DELETED AT INTAKE (no working URL, or contradicted by primary source)

1. **"A Chief of Staff is publicly credited with advancing AI and technology adoption at Alera."**
   Source: the 2026-08-24 gate entry. **DELETED.** Anastasia Busciglio's first-party bio (https://aleragroup.com/profile/anastasia-busciglio) was retrieved in full and contains **zero** mention of AI, artificial intelligence, technology adoption, or innovation. Her Equilar bio likewise. Her LinkedIn returned HTTP 999 and could not be read. person-finder searched five distinct query formulations and found no URL supporting the claim.
   → This was a load-bearing C2 justification in the gate. It does not survive. The Chief of Staff seat is real and first-party confirmed; the AI attribution is not. **Do not carry it into any draft.**

2. **"Kelso & Company minority stake" and the "~$4.2B valuation."**
   **DELETED.** Only surfacing sources were an apparently AI-generated blog and search-engine summarization. kelso.com/news, kelso.com/investments, aleragroup.com/news, the Insurance Journal Alera archive, and Business Insurance were all checked. No primary source exists.

3. **"~4,600 colleagues."**
   **CORRECTED to "more than 4,500 colleagues"** — the figure in Alera's own Sept 30 2025 press boilerplate (https://aleragroup.com/news/alera-group-expands-midwest-presence-strategic-addition-kansas-city-wealth-advisory-and). The 4,600 variant could not be attached to a working URL. Never use 4,600 in a draft.

4. **"Their Workday host 500s."**
   **FACTUALLY WRONG — corrected.** Alera does not run Workday recruiting. `aleragroup.wd1.myworkdayjobs.com/wday/cxs/...` returns HTTP 400, no tenant. Their ATS is a Jibe/iCIMS-style career site at careers.aleragroup.com (plus a separate `agency-aleragroup.icims.com` for the General Agency entity). The gate's failure to reach the req was a **rendering** problem, not a server problem — see the tooling note below.

5. **Constructed email addresses** (`john.mollica@aleragroup.com` etc.).
   **RETAINED BUT LABELED AS CONSTRUCTIONS, NOT FACTS.** The *pattern* `First.Last@aleragroup.com` has one documented first-party instance (`Jeff.Silverman@aleragroup.com`, https://benefitslink.com/press-release/55859) plus two aggregator corroborations at ~90%. No published instance of Mollica's own address was located. Any use is a bet, not a verified address.

6. **"Transformation Change Integration Leader" and "Transformation Change Manager (Front Office)" as live reqs.**
   **DOWNGRADED.** Aggregator-only sightings; absent from Alera's authoritative 60-req ATS list and sitemap. Treat as recently closed/filled. Their *existence* is still usable evidence that Alera funded a change-management layer; their *liveness* is not claimable.

7. **Kyle Samuel as sitting COO.**
   **DOWNGRADED to "likely vacant."** Announced COO Jan 2025 (first-party), but absent from the current leadership page, his Alera profile 404s, and his LinkedIn surfaces a Colorado College board chairmanship with no Alera COO title. No departure announcement exists. Do not assert either way in a draft.

---

## SPOT-CHECKS PERFORMED (3 load-bearing citations, fetched directly by the parent agent)

**✅ 1 — Canonical req 7564.** `careers.aleragroup.com/api/jobs?keywords=Head+of+AI&limit=3`
Every load-bearing element confirmed verbatim:
- `$250,000 - $300,000 annually` / `Bonus Eligible: Yes (Performance Based)` — **CONFIRMED**
- `"This position is Remote"` with **no state names and no exclusions anywhere in the posting** — **CONFIRMED**. This resolves the gate's blocking caveat.
- Travel: `"Occasional travel may be required to support office implementations, training, and collaboration with project teams"` — **CONFIRMED**
- Seven partner functions: Finance, Operations, Technology, Legal, Compliance, Communications, Learning & Development — **CONFIRMED** (gate had four)
- `posted_date 2026-08-20` / `posting_expiry_date 2026-09-25T04:00:00+0000` — **CONFIRMED**
- The misspelling "Aritficial" in the employer's own body copy — **CONFIRMED**
- **Applied Epic, BenefitPoint, and "Transformation Office" appear NOWHERE in the req** — **CONFIRMED.** This negative is the load-bearing fact under the One Insight, so it was verified directly rather than taken from a collector.

**✅ 2 — CEO Jim Blue interview.** `insurancebusinessmag.com/us/news/breaking-news/one-alera-ceo-jim-blue-maps-postmanda-playbook-551447.aspx` (Sept 30 2025, by Gia Snape)
All quotes confirmed verbatim: "We were just go, go, go with M&A. Now the goal is to take these 220 partners and see if we can work better together." / "We're running two official pilots aimed at boosting colleague productivity on everyday tasks." / "What's clear is we can take some of the drudgery off desks." / "In a relatively short period, within a couple months, it's down 30-40%, and they feel accuracy is up and quality is higher." / "Some people are picking up five to six hours a week." / "People have always been front and center. But we didn't do a lot with accountability and metrics while we were keeping up with M&A." / "Can we be one Alera Group – operate better together, create efficiencies, sell more business, be more profitable?"
**One additional quote surfaced at spot-check** and is now usable: **"Every team can put in two or three metrics on how they can do something better."**

**✅ 3 — Sibling req 7538 (Implementation Lead – P&C).** `careers.aleragroup.com/api/jobs?keywords=Implementation+Lead+Property+Casualty&limit=3`
- "Transformation Office" confirmed verbatim: *"Join Alera Group's Transformation Office and lead the successful migration of our Property & Casualty offices…"*
- Applied Epic confirmed as the standardized target platform; BenefitPoint confirmed as the EB target platform (req 7537)
- Legacy AMS list confirmed: BenefitPoint, TAM, Zywave/BKB, Dynamics, Gen4 (+ Applied Epic on the EB side) — **six-plus platforms in production**
- "Implementation waves from planning through go-live and stabilization" — confirmed
- **NEW AND SHARPER THAN THE DOSSIER:** the Implementation Lead leads a *"cross-functional implementation pod including Data Migration, Training, Hypercare, and local office Change Champions"* and partners *"to ensure successful office readiness and adoption."*
  → Alera already owns wave-by-wave training machinery with named Change Champions in each office. This upgrades the One Insight from "there's a training gap" to "the adoption machinery already exists and is already funded — it just isn't pointed at AI."
- Reqs 7537/7538 both $100,000–$150,000, Remote, posted 2026-08-12

---

## PRIOR-CONTACT CHECK (parent agent, filesystem)

`grep -ril "alera" runs/ background/ reference/` → **only hit is `runs/gate-ledger.md`** (the 2026-08-24 gate entry itself).
**No prior Jefferson↔Alera contact of any kind. Genuinely cold first approach.**

---

## GATE CAVEAT DISPOSITION

The gate flagged one caveat as blocking the application frame:
> "canonical req NOT reached — careers.aleragroup.com returns 404 on every search path tried and their Workday host 500s… Verify the canonical req + state eligibility before filing (Microsoft 7/28 shape)."

**RESOLVED — the caveat clears, and the app frame is clean.**
- Canonical req = **7564**, live, employer-sourced: https://careers.aleragroup.com/jobs/7564?lang=en-us
- **No state-eligibility restriction exists.** `#Nationwide` + `#LI-Remote` tags, `country: United States`, `full_location: United States`, zero state names in the full text. Maryland is fine.
- Comp confirmed on the employer's own ATS, not just LinkedIn.
- Travel is "occasional," scoped to office implementations — nowhere near the 50% pre-filter.
- **New hard fact the gate did not have: the req expires 2026-09-25 04:00 UTC.**

No pre-filter fires. No caveat blocks. Per the standing order (2026-07-08), this proceeds.

---

## REUSABLE TOOLING FINDING (→ reference/research-tooling.md)

Alera-class ATS (Jibe/iCIMS client-rendered career sites) defeat naive fetching: job pages are JS shells with **no server-side JSON-LD**, so a fetch returns generic careers chrome and reads as a dead link. This is exactly why the gate concluded "404 on every path."

Two working extraction paths:
1. **JSON API:** `GET https://<careers-host>/api/jobs?keywords=<q>&limit=<n>` — returns full descriptions incl. structured `salary_range`, `posted_date`, `posting_expiry_date`, location fields. Relevance-ranked and **caps at ~4–8 records regardless of `limit`** — so absence from a keyword query is NOT evidence a req is closed.
2. **Enumeration:** `https://<careers-host>/sitemap1.xml` lists every live job URL (60 for Alera, reconciling exactly with the ATS total-count field).
3. **Liveness test:** direct fetch of `/company/jobs/<id>?lang=en-us` — live reqs return `<title>` "<Job Title> in <Location> | Alera Group"; closed reqs return HTTP 404 (verified against 7239 → 404, 7344 → 404, 7564 → live).

This is the second time in two weeks a "canonical req unreachable" caveat turned out to be a rendering artifact rather than a missing req (cf. Principal Financial 8/14, "Workday CXS 422, careers site JS shell"). **Worth adding to the gate's own procedure: before writing "canonical req not reached," try the ATS JSON endpoint and the sitemap.**

---

## CARRIED INTO THE GAPS REGISTER (see brief.md)

Reporting line for the seat · team size and budget · which vendors power the two pilots · whether the Transformation Office owns or merely neighbors the AI seat · migration wave count / % complete / target date · Kyle Samuel's COO status · the "12th vs 14th largest" boilerplate conflict · presenter for the Nov 17 2026 AI webinar · sponsorship language (moot — Jefferson is authorized) · whether a published Alera responsible-AI framework exists (none found) · Mollica's public voice (see dossier-voice.md).
