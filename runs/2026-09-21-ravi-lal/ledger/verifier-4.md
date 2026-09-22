# Adversarial Verification — Verifier 4

Run: 2026-09-21-ravi-lal · Role: adversarial verifier, single claim (Dolphin Haley Ltd financials/officers/PSC + Diageo-timing inference) · Tools used: Bash (python3 for iXBRL/XML parsing, curl for live re-fetch). No Chrome browser tools used (per instruction). All Companies House pages re-fetched live today (2026-09-21) in addition to reading the collector's saved evidence files; the two saved iXBRL files were byte-for-byte MD5-identical to what I independently pulled live, so nothing in the saved evidence has drifted from the live register.

---

## Result block

```
claim: "Dolphin Haley Limited (Companies House 08396885), the registered vehicle trading as Voxly Digital, is solvent and self-funded: filed accounts show shareholders' funds of £632,280 (FYE 31 Mar 2024), £848,101 (FYE 31 Mar 2025) and £859,648 (FYE 31 Mar 2026); cash at bank of £524,881 / £1,011,643 / £784,576 respectively; debtors £320,480 / £9,252 / £141,343; creditors due within one year £213,081 / £172,794 / £66,271; average employees 5 in each year; share capital £1; sole director and PSC Ravinder Singh Lal (b. Feb 1969, American). The FYE Mar 2026 accounts predate the loss of Diageo (which the target said on 2026-09-18 was ~50% of revenue and ended roughly three months earlier), so that loss is not yet visible in any filing."
verdict: CONFIRMED (balance sheet, employees, director/PSC identity, trading-name link, and the "not knowable from filings" caveat) / UNCONFIRMABLE (the Diageo-loss timing and ~50%-of-revenue figures themselves, which are not filing facts at all — see split below)
checked:
  - "dh_accounts_2025-03-31.xhtml (local, MD5 635c1f39...) parsed by hand as XML/iXBRL: every ix:nonFraction tag extracted with its contextRef and cross-walked to the xbrli:context period/instant definitions"
  - "dh_accounts_2026-03-31.xhtml (local, MD5 390efafe...) parsed the same way"
  - "Both files re-fetched live from find-and-update.company-information.service.gov.uk/company/08396885/filing-history/<txid>/document?format=xhtml&download=1 (2026-09-21) — MD5 identical to the saved copies, confirming authenticity and that nothing has been re-filed/superseded"
  - "FYE 31 Mar 2024 figures independently re-derived a THIRD way: fetched the standalone 2024 AA filing (txn MzQ0MjYxMjEwNWFkaXF6a2N4, filed 11 Nov 2024) directly, not just the comparative column inside the 2025 accounts — all five headline numbers matched to the penny"
  - "Companies House filing-history page (both pages, live) re-fetched and read in full, 2013–2026"
  - "Companies House officers page (live) and PSC page (live) re-fetched 2026-09-21"
  - "Companies House charges page (live) re-fetched — 0 charges registered"
  - "Companies House company overview page (live) — status Active, last accounts made up to 31 Mar 2026, confirming no later accounts exist"
  - "voxlydigital.com/about-us re-fetched live 2026-09-21 (separately from the collector's saved copy) — confirms the trading-name sentence verbatim and still current"
  - "Arithmetic cross-check: every creditor sub-line (corp tax, other tax/NI, VAT, other creditors, accruals, amounts owed to directors, bank borrowings, trade creditors) sums to the reported 'Creditors due within one year' total to the penny in both FY2025 (172,794) and FY2026 (66,271) — internal consistency check, not just a copied headline figure"
checked_count: 13 independent checks (7 live Companies House re-fetches, 1 live third-party site re-fetch, 3 independent iXBRL parses/cross-derivations of the same figures, 1 filing-history full read, 1 internal arithmetic reconciliation)
finding: "See the four-part split below. Balance-sheet figures, employee counts, director/PSC identity, and the Dolphin Haley=Voxly trading-name link are all CONFIRMED directly from primary documents I opened myself. Turnover/profit are affirmatively NOT in either filing — the directors formally elected under s444(1)/CA2006 not to deliver a P&L account, so the '~50% of revenue' figure is not a filing fact and cannot be cross-checked against anything Companies House holds; it rests solely on the target's own spoken claim in S0. The timing inference (FYE Mar 2026 accounts predate a mid-June 2026 Diageo loss) is logically sound GIVEN the S0 timeline, and the mechanics check out (accounts cover to 31 Mar 2026, signed 15 Jun 2026, filed 19 Jun 2026, and remain the latest filed — nothing has been filed since), but the underlying premise (Diageo ended ~3 months before 2026-09-18, i.e. ~mid-June 2026) is itself an unverified S0 assertion, not something I can independently confirm from any source in this run."
source_ids: [CH-XBRL-2024, CH-XBRL-2025, CH-XBRL-2026, CH-FILING-HISTORY, CH-OVERVIEW, CH-OFFICERS, CH-PSC, CH-CHARGES, VOXLY-ABOUT, S0]
```

---

## Split verdict, as requested

### (a) Balance-sheet numbers — CONFIRMED, to the penny, three independent ways

Re-parsed the raw `ix:nonFraction` tags myself (not trusting the collector's transcription) and mapped each `contextRef` to its `xbrli:context` period:

| | FYE 31 Mar 2024 | FYE 31 Mar 2025 | FYE 31 Mar 2026 |
|---|---|---|---|
| Net assets / "Shareholders' funds" (`frs-core:NetAssetsLiabilities`, and the accounts literally print "SHAREHOLDERS' FUNDS" on that line) | 632,280 | 848,101 | 859,648 |
| Cash at bank (`frs-core:CashBankOnHand`) | 524,881 | 1,011,643 | 784,576 |
| Debtors (`frs-core:Debtors`) | 320,480 | 9,252 | 141,343 |
| Creditors due within 1 yr (`frs-core:Creditors`) | 213,081 | 172,794 | 66,271 |
| Share capital (`frs-core:Equity`, ShareCapital context) | 1 | 1 | 1 |

Every one of these matches the claim exactly. I did not rely only on the comparative column inside the 2025/2026 filings (which is all the collector cited) — I additionally pulled the **standalone FYE-2024 AA filing** (filed 11 Nov 2024, a document the collector didn't cite) directly from Companies House live and got 632,280 / 524,881 / 320,480 / 213,081 / employees=5 independently, so the FY2024 figures are corroborated by two separate filings, not just one column.

I also reconciled the creditors sub-schedule arithmetically as an internal-consistency attack: for FY2026, CorpTax 18,170 + other tax/NI 7,511 + VAT 32,677 + other creditors 514 + accruals 1,000 + amounts owed to directors 2,887 + bank borrowings 3,512 = 66,271 exactly. Same for FY2025 (172,794 exactly, including trade creditors 4,258). No rounding slop, no plug figures — this is a real, internally-consistent balance sheet, not a fabricated summary.

Both saved `.xhtml` evidence files are **MD5-byte-identical** to what I pulled live from Companies House today, so there's no risk the collector edited or mis-saved them.

### (b) Employees / director / PSC — CONFIRMED

- `frs-core:AverageNumberEmployeesDuringPeriod` = 5 for FY2024, FY2025, and FY2026 (and even the prior year, FY2023, was 4) — matches "average employees 5 in each year" exactly.
- Live officers register (re-fetched 2026-09-21): **1 officer, 0 resignations** — Ravinder Singh Lal, Director, DOB February 1969, Nationality American, appointed 11 February 2013 (i.e., since incorporation — this has always been a one-man-band company). Identity verification: Verified.
- Live PSC register (re-fetched 2026-09-21): **1 active PSC, 0 active statements** — Mr Ravinder Singh Lal, DOB February 1969, Nationality American, notified 11 February 2017, nature of control "Has significant influence or control" (worth flagging as a nuance: this is the general-influence PSC category rather than an explicit >75%-shares tier, but it does not contradict "sole director and PSC" — he is the only person on either register).
- Zero charges registered against the company (0 outstanding, 0 satisfied, 0 part-satisfied) — supports "solvent," no secured lender with a claim on assets.

### (c) The timing inference re: Diageo — mechanically sound, but resting on an unverifiable premise

What I *can* confirm from Companies House: the FYE 31 Mar 2026 accounts were **signed by the director 15 June 2026** and **filed 19 June 2026**, and — re-checked live today, 2026-09-21 — **nothing has been filed since**; the company overview page confirms "Last accounts made up to 31 March 2026" and status Active. So structurally, the claim's framing is correct: these are the newest financial data Companies House has, the balance-sheet date (31 Mar 2026) is fixed, and small-company "total exemption full accounts" carry no subsequent-events/post-balance-sheet-events note (I searched both filings for "subsequent event," "post balance sheet," "events after," "material uncertainty," and "going concern" — zero hits in either). So if a client loss happened after 31 March 2026, this filing set structurally cannot show it, and nothing in the document even attempts to.

What I *cannot* confirm: the premise itself — that Diageo was ~50% of revenue and departed roughly three months before 2026-09-18 (i.e., around mid-June 2026) — is not a filing fact. Per layer0-frame.md, that is Ravi Lal's own spoken claim in the S0 transcript (AI Jam, 2026-09-18). No Companies House document, and nothing else in the evidence set I was given, corroborates the size or timing of that loss. The claim text itself already scopes this correctly ("which the target said") — I'm not refuting it, I'm confirming that this specific sub-fact is, and will remain, unconfirmable from any document-based source; it is a self-report, not a filing fact, and should be labeled that way wherever this claim is used downstream.

One point worth flagging to the team: **voxlydigital.com/about-us, re-fetched live by me just now, still says "Our clients include Diageo (multiple brands including Don Julio, Baileys, etc.)"** — present tense, as of today. That doesn't disprove the loss (marketing pages routinely lag reality), but it's a live, dated data point that a downstream reader should know about rather than assume the website already reflects the claimed client loss.

### (d) Is revenue knowable from these filings? — REFUTED (i.e., the claim's own caveat that it is NOT knowable is CONFIRMED correct)

Both filings are Companies House Type "AA — Total exemption full accounts" filed under FRS102 Section 1A for a small company, and both contain the explicit director's statement: *"The company has taken advantage of section 444(1) of the Companies Act 2006 and opted not to deliver to the registrar a copy of the company's Profit and Loss Account."* (tagged `frs-direp:StatementThatDirectorsHaveElectedNotToDeliverProfitLossAccountUnderSection4445ACompaniesAct2006` in both years' iXBRL.)

I grepped every occurrence of "Turnover," "Revenue," "Profit," and "Loss" in both raw files: all of them fall inside generic FRS102 1A accounting-policy boilerplate (e.g., "Turnover is measured at the fair value of the consideration received or receivable...") or inside the balance-sheet equity line literally labelled "Profit and Loss Account" (which is the retained-earnings reserve, not an income statement — it's 859,647 / 848,100, the same number already counted in shareholders' funds above). There is no turnover figure, no P&L, no gross-profit or net-profit line anywhere in either document. So: **the ~50% Diageo revenue-concentration figure cannot be cross-checked against anything Companies House holds, in any year, filed or unfiled.** The claim is correct to attribute that number solely to the target's spoken word.

## Additional material findings not in the claim, but relevant

1. **Trading-name link independently confirmed, live** — voxlydigital.com/about-us (fetched by me directly, separate from the collector's saved copy) states verbatim: *"Voxly is a trading name owned by Dolphin Haley LTD."* This directly supports the claim's opening premise. **Flag for the team:** this appeared to contradict Verifier 1's ledger entry, which had reached a REFUTED verdict on "Dolphin Haley Ltd = Voxly Digital" — Verifier 1's own source list quoted the same about-us page ("Led by Ravi Lal and Elliot Brock...") but stopped one sentence short of the trading-name disclosure that immediately follows it in the same paragraph.
   - **RESOLVED 2026-09-21**: flagged to Verifier 1 directly. They independently re-verified (grepped the saved evidence file for the exact sentence, then did a second, independent live check: voxlydigital.com's "Trust Center" link resolves to `dolphinhaley-com.trustcenter.scytale.ai`, corroborating the trading-name link from a different angle) and confirmed their original WebFetch pass had silently dropped that sentence when summarizing the page. Verifier 1 has updated `ledger/verifier-1.md`: the Dolphin Haley=Voxly sub-finding flipped REFUTED → CONFIRMED, the circumstantial evidence (SIC mismatch, Uxbridge address, no cross-mention in the accounts) reframed as "explained, not contradicted," and their overall verdict on their assigned claim moved REFUTED → UNCONFIRMABLE accordingly (original reasoning kept, not deleted, for the audit trail). No further action needed on this thread.
2. **Registered office moved during FY2026**: AD01 filed 20 Mar 2026 changed the registered office from Bentinck House, Bentinck Road, West Drayton (a Local-newsagent-style formation-agent address used since 3 Jan 2024) to Boundary House, Cricket Field Road, Uxbridge — the address that now appears on the FYE Mar 2026 accounts, on the live officers/PSC pages, and on the company overview. A near-duplicate AD01 was also filed 11 Mar 2026 (address unchanged, just re-filed/corrected), and PSC04 detail-change filings accompanied both office changes (11 Mar and 24 Mar 2026) — routine administrative updates tied to the office move, not a change of PSC identity.
3. **Capital reorganisation in Aug–Sep 2025** not mentioned in the claim: SH02 sub-division of shares (26 Aug 2025) plus two shareholder resolutions (RES13 — new class of share, 29 Aug 2025; RES10/RES11 — allotment of securities and removal of pre-emption rights, filed 1–3 Sep 2025). None of this moved the nominal share capital figure (still £1 in both the FY2025 and FY2026 accounts, consistent with a pure sub-division/new-class-creation rather than a capital raise), but it is a real, dated corporate event on the public record that a background check on this target should probably know about — possibly relevant if the target is planning to bring on investors or partners.
4. **Zero registered charges**, ever, across the company's full history back to 2013 incorporation — no secured lender, no debenture. Consistent with "self-funded."
5. Company incorporated 11 Feb 2013 (13 years old); Ravinder Singh Lal has been sole director since incorporation and sole PSC since the PSC register began (11 Feb 2017) — no historical co-directors or co-owners on file at any point I could see in the filing history back to 2013.
6. SIC code on file is 47910 ("Retail sale via mail order houses or via internet") — does not obviously match a digital-agency/AI-compliance business description. Not something the claim asserts, but worth flagging as a minor register-hygiene oddity if anyone downstream leans on the SIC code for classification.

## Source list

- `dh_accounts_2025-03-31.xhtml` (local evidence, MD5 635c1f398edf2be31e984a26344635b4) — accessed 2026-09-21 09:04 (collector) / re-verified 2026-09-21 (me). Full iXBRL, FYE 31 Mar 2025 with FY2024 comparatives.
- `dh_accounts_2026-03-31.xhtml` (local evidence, MD5 390efafe9c048f83823e1b6d54cf7add) — accessed 2026-09-21 09:04 (collector) / re-verified 2026-09-21 (me). Full iXBRL, FYE 31 Mar 2026 with FY2025 comparatives.
- `https://find-and-update.company-information.service.gov.uk/company/08396885/filing-history/MzUyNzMwMDc4OWFkaXF6a2N4/document?format=xhtml&download=1` — fetched live 2026-09-21 by me; MD5-identical to the FYE2026 file above.
- `https://find-and-update.company-information.service.gov.uk/company/08396885/filing-history/MzQ3MjQ5NzcyN2FkaXF6a2N4/document?format=xhtml&download=1` — fetched live 2026-09-21 by me; MD5-identical to the FYE2025 file above.
- `https://find-and-update.company-information.service.gov.uk/company/08396885/filing-history/MzQ0MjYxMjEwNWFkaXF6a2N4/document?format=xhtml&download=1` — fetched live 2026-09-21 by me (standalone FYE 31 Mar 2024 filing, filed 11 Nov 2024, not part of the collector's cited evidence). Confirms 632,280 / 524,881 / 320,480 / 213,081 / employees=5 independently of the 2025 accounts' comparative column.
- `https://find-and-update.company-information.service.gov.uk/company/08396885/filing-history` (pages 1 and 2) — fetched live 2026-09-21. Full filing history 2013–2026: confirms AA filed 19 Jun 2026 for FYE 31 Mar 2026 is the latest filing of any type; confirms office move 20 Mar 2026; confirms Aug–Sep 2025 share reorganisation; confirms zero "Charges" category items across the full history.
- `https://find-and-update.company-information.service.gov.uk/company/08396885` (overview) — fetched live 2026-09-21. Status Active; Last accounts made up to 31 March 2026; incorporated 11 February 2013; SIC 47910.
- `https://find-and-update.company-information.service.gov.uk/company/08396885/officers` — fetched live 2026-09-21. 1 officer, 0 resignations: Ravinder Singh Lal, Feb 1969, American, appointed 11 Feb 2013, Verified.
- `https://find-and-update.company-information.service.gov.uk/company/08396885/persons-with-significant-control` — fetched live 2026-09-21. 1 active PSC, 0 active statements: Ravinder Singh Lal, Feb 1969, American, notified 11 Feb 2017, "significant influence or control," Verified.
- `https://find-and-update.company-information.service.gov.uk/company/08396885/charges` — fetched live 2026-09-21. "0 charges registered / 0 outstanding, 0 satisfied, 0 part satisfied."
- `voxlydigital.com/about-us` — fetched live by me 2026-09-21 (independent of the collector's saved `voxly-about-us-2026-09-21.html`, which I also cross-checked and matches). States: "Voxly is a trading name owned by Dolphin Haley LTD" and "Our clients include Diageo (multiple brands including Don Julio, Baileys, etc.), the UK Royal Navy, and Bristol Airport in the UK."
- `layer0-frame.md` (this run's ledger) — S0 definition: AI Jam transcript 2026-09-18, source of the "Diageo ≈ 50% of revenue, lost ~3 months before 2026-09-18" claim. I did not re-open the transcript myself (out of scope for this claim's assigned sources); flagging that this whole sub-fact traces to a single self-report with no document corroboration anywhere in this run.
