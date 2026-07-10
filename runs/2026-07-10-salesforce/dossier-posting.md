## DOSSIER: Posting Archaeology
## ROLE: Salesforce — Senior Director, Agentic Transformation Lead (req JR350160)
## COLLECTED: 2026-07-10

### Findings

**Canonical source & liveness**
- Canonical ATS is `salesforce.wd12.myworkdayjobs.com/External_Career_Site` (Workday CXS), mirrored at careers.salesforce.com → redirects to salesforce.com/company/careers/jobs/jr350160/. — https://www.salesforce.com/company/careers/jobs/jr350160/ — H
- Public page returns 403 to automated fetch (bot-block, not dead); canonical liveness rests on the Workday CXS JSON (canApply:true, posted:true, startDate 2026-07-09). — M

**Comp verification**
- No pay range in the Workday JSON body. Reason (structural): all four locations — Indianapolis (IN), Atlanta (GA), Austin (TX), Dallas (TX) — are NON-pay-transparency states; Salesforce discloses bands only when a CA/CO/NY/WA location is attached. Expected omission, not a red flag. — H
- Closest market comparator (Job Category = Software Engineering) — Levels.fyi **Sr Director, Software Engineering Manager**: US avg total **$563,605** (base $330,386 / stock $159,167 / bonus $74,052), range "$444K–$707K+". — https://www.levels.fyi/companies/salesforce/salaries/software-engineering-manager/levels/senior-director — H
- Alternate (Sr Director, Product Manager): US median total **$501,198** (base $315,969). — https://www.levels.fyi/companies/salesforce/salaries/product-manager/levels/senior-director/locations/united-states — H
- Floor check: base alone (~$316K–$330K) clears the $125K pre-filter ~2.5x; total ~$500K–$565K median, upside $700K+. — H

**Repost / freshness history**
- JR350160 appears in ZERO aggregators (LinkedIn/Indeed/Levels/Glassdoor/JobLeads/Lensa) and returns NO Wayback snapshot — consistent with a genuinely FRESH req (startDate 2026-07-09), not yet propagated. — https://archive.org/wayback/available?url=careers.salesforce.com/en/jobs/jr350160/ — H
- No evidence of a prior title, re-level, or predecessor for this exact seat. — M

**Language signals (author fingerprint / politics)**
- Manifesto register ("We solve it for ourselves. Then we sell it for a decade."; "headless model where agents run the work and humans make the judgment calls") maps directly onto Salesforce's **Headless 360** / "System of Agency" narrative — written by/for someone inside that exec framing, not TA boilerplate. — https://www.salesforce.com/headless/ — H
- Names Cursor, Claude, Codex, Agentforce specifically — an unusually tool-specific, first-person voice indicating a single hiring operator drafted it. — M
- "Influence, not headcount" / "not from managing a large team of your own" = a founder-operator seat with no direct-report team at start; signals executive-sponsor urgency + a net-new function. — M (inference from phrasing)

**Duplicate / sibling postings**
- JR350160 is a SINGLE req cross-posted across the four cities (one JR number, Salesforce's standard multi-location pattern), not four separate reqs. — H
- Distinct, non-duplicate siblings in the same theme (Salesforce staffing the space broadly): JR328948 Sr Dir Executive Talent & Succession "Leading the Agentic Transformation"; JR340342 Sr Dir Global Field Readiness Transformation. — https://careers.salesforce.com/en/jobs/jr328948/senior-director-executive-talent-succession/ — M

**Strategic flag — application budget**
- Salesforce recommends applying to a MAX of 3 roles per rolling 12 months ("to ensure you are not duplicating efforts") — stated as a recommendation; community consensus is soft/non-enforced, but scarcity is real. Don't burn one of three on a low-conviction req. — https://www.salesforce.com/company/careers/culture/how-we-hire/ — H

### Not Found
- A stated salary range for JR350160 on any canonical/state-law source — none exists (no CA/CO/NY/WA location attached).
- Any Wayback/archive snapshot of JR350160 — empty.
- JR350160 on any aggregator — no propagation yet.
- Evidence of a prior/earlier version or re-level of this seat — none.
- The named hiring executive by name from the posting itself — inferable as a single operator; identified via org+voice layers as Joe Inzerillo, not stated in the JD.

### Collector Notes
- Comp comparator ambiguity: title "Senior Director" but Job Category "Software Engineering"; the two Levels bands ($444–707K SWE-Mgr vs. $501K PM median) bracket the likely real band. Both clear the floor decisively.
- Absent range is a legal artifact of the non-transparency-state location set, NOT a board discrepancy (nothing to reconcile — req hasn't propagated).
- Freshness strongly triangulated but rests on absence-of-evidence; a same-day repost of an internal-only earlier req can't be fully excluded.
