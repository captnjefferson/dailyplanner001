# Sweep state — CT cold outreach (started 2026-10-13 ~3:05 PM ET)

| Sweep | Tool | Prompt file | Status | Where |
|---|---|---|---|---|
| T3 founders | ChatGPT Deep Research (Jefferson's account, driven in Chrome) | chatgpt-deep-research-T3-founders.md | DONE 8 min; 8 candidates; captured to chatgpt-T3-founders-report.md | https://chatgpt.com/c/6ace8132-176c-83ea-b45c-8d1823005210 |
| T2 sponsors | Manus | manus-T2-sponsors.md | BLOCKED: Manus shows a sign-in page in Chrome; needs Jefferson | https://manus.im/app |
| T2 sponsors (fallback) | ChatGPT Deep Research | manus-T2-sponsors.md (same prompt) | DONE 7 min; 25 firms, mostly large nationals; captured to chatgpt-T2-sponsors-report.md | https://chatgpt.com/c/6ace8194-ef74-83ea-9741-aa0881ad228a |
| T1 chairs | Opus subagent (WebSearch/WebFetch only) | in the agent prompt | DONE 50 min; 20 bookers (14 EO learning chairs, 5 Vistage, 1 TAB) | t1-peer-rooms/t1-candidates.md |
| T2 sponsors | Opus subagent | in the agent prompt | DONE 57 min; 20 firms (9 CPA, 4 insurance, 3 PEO, 3 law, 1 bank); 1 grade A | t2-sponsored-rooms/t2-candidates.md |
| T3 founders | Opus subagent | in the agent prompt | DONE 61 min; 5 found, 2 clean (search budget ran out) | t3-founder-direct/t3-candidates.md |

Rule: everything from a sweep is a lead, not a fact. Verify on the primary page before it reaches a card.

Notion: database "CT cold outreach — experiments" 3f8164c1-810d-81fe-833c-e8930d8ddf52 · process page 3f8164c1-810d-8191-8032-c9956ca8e1f8 (both under Captain Tomorrow General).

## Sweep yield notes (track; decide whether to try another research agent)
- 2026-10-13 ~4:05 PM ET — ChatGPT Deep Research T3 (founders, 25–100 people, public AI-uncertainty statement, last 6 months): **8 verified candidates of 25 asked**, 8 min, 32 citations, 642 searches. Its own note: the headcount + founder-led + reflective-statement combination is a needle search; it refused to pad. T2 (sponsor rooms): 7 min, 38 citations, 737 searches; count TBD on read. Both reports render in a sandboxed frame; export = download icon on the card (Jefferson OK'd 4:08 PM).
- Candidates to try if yield stays low: Manus (needs his sign-in), Gemini Deep Research, Perplexity, Exa (key not set), Parallel.

## Capture note (how to get a Deep Research report out of ChatGPT's new research interface)
The report renders in a sandboxed iframe; page tools can't read it, the chat model can't see it, the card's download icon does nothing, and synthetic copy/paste comes back empty. What works: open the report as a page in ChatGPT Space (chatgpt.com/space), use "Ask about this file", and ask it to print the complete contents verbatim; the reply is plain DOM text (takes 1–3 minutes).

## Yield read, end of wave-1 sweeps (~4:45 PM ET)
- T1: directories work. EO learning chairs are findable but mostly have no public footprint (thin angle); Vistage chairs are gated but the ones on the "Confessions of a Vistage Chair" podcast are rich. Vistage onboards speakers only once a chair sets a date.
- T2: ChatGPT returns big national firms (wrong size). The subagent's regional list is closer. One grade-A room (Weintraub Tobin). Banks/wealth/CRE under-covered; search budget ran out.
- T3: needle search. 21 Hats podcast (owner panel, full transcripts) and Inc. "Founder Group Chat" are the two sources that produce; general search ignores quoted phrases. LinkedIn posts are the untapped surface (lead's lane). Combined usable: ~6 (Vanderbloemen, Flanagan, Winters, Cordeaux, Gascoigne, Fried) before verification.
- Shared web-search budget (200/turn across subagents) was the binding constraint on T2 and T3. Next wave: fewer concurrent search-heavy agents, or stagger them.

## Wave 2 (per-person scans) — status ~6:05 PM ET
- T1 done: Garrido, Luther, Dixon (all VERIFIED-PRIMARY; LinkedIn reads done; Maigret on Luther). Cards v1 in cards/t1-cards-v1.md and in the Notion DB.
- T3 done: Vanderbloemen, Flanagan, Winters (all VERIFIED-PRIMARY; LinkedIn reads done; Inc. quotes for Flanagan and Winters verified on the page in the browser pane). Cards v1 in cards/t3-cards-v1.md and in the DB. Winters is ~20 people (below band), flagged.
- T2 done: Rea (Brickwood; grade raised to A), Weintraub Tobin (Chediak, medium confidence), Withum/JKJ (the human is Chris Mangano, Withum's convener; JKJ has no events lead). Cards v1 in cards/t2-cards-v1.md and in the DB.
- DB rows: 9 drafted (3 per thread). Nothing sent. Wave 2 complete ~6:20 PM ET. Wave 3 (next 7 per thread) waits on Jefferson's edits/kills and go.
- Lesson: the per-person scans are where the angle comes from; every card leads with a verified line of the person's own. ChatGPT/Manus sweeps are for lists only.

## v2 person reads — three samples done (~8:30 PM ET)
- Garrido (T1), Brickwood (T2), Vanderbloemen (T3): `*-person.md` files, each ~8,300 words, eight sections, section 2 prose 660–700 words, section 3 "right now" with confidence labels, section 4 their named problems verbatim, section 5 Humantic + the lead's LinkedIn read + the lead's own long-form read. Humantic: Garrido DI, Vanderbloemen CDI, Brickwood none (insufficient social data).
- Cost: ~20–25 min wall clock and ~400K tokens per person read; plus the lead's own reading of one long-form per person.
- Awaiting Jefferson's call on depth before the other six get the same treatment and before any card is written.
