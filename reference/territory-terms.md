# Jefferson's territory terms — the Layer 5b search list

**ACTIVE — v1.0, 2026-08-26.** Reviewed by Jefferson and wired into the process doc as `paths.territory_terms`. T7 graded STRONG and T9 corrected by him on the same date.

**What this is for.** Layer 5b classifies a target's subjects as OCCUPIED / PEER / OPEN / VOID. That requires searching *their* corpus for the subjects Jefferson has standing on, and counting hits. This is that list.

**The rule that makes it work:** these are terms a **target** would plausibly write, not Jefferson's phrasing. His coinages ("deficit machine," "the hollow click") return zero on everyone — searching them manufactures a VOID on every theme for every person. Those live in §3 and are never fed to the regex.

**Standing grades.** VOID = "absent subject where Jefferson has demonstrated standing." Standing alone decides the rank: a **STRONG** territory can take the top three whether or not anything published backs it. Where there's no linkable piece, the report says so — "strong standing, no linkable proof" — so he knows he's going in on his own authority rather than on a link. A VOID on a MEDIUM or THIN territory never ranks top three.

Why the grades exist at all: absence in someone else's corpus is trivially easy to find, so without a standing test the process ranks a VOID highest exactly where Jefferson has least to say.

**Precision.** Terms marked ⚠️ are common enough to hit anywhere. A bare hit on a noisy term is not evidence of a theme — require it to co-occur with a second term from the same territory, or discard it.

---

## §1 — Searchable territory terms

### T1. AI adoption & enablement — **STRONG** · backing: "Why AI rollouts fail" (LinkedIn, 2026-06-17)
Standing: has run the rollouts. 10+ client orgs across public affairs, healthcare associations, education, professional services; ~20 staff incl. senior leadership trained at a national lobbying firm plus their custom AI playbook; a cohort serving 6 small businesses; PromptLab reaching ~400+ professionals; DMAS 2024 keynote to 200+.

| regex | note |
|---|---|
| `AI adoption\|adoption curve\|user adoption` | |
| `AI enablement\|enablement program` | |
| `AI rollout\|rollout` | ⚠️ |
| `AI transformation\|digital transformation` | |
| `change management` | |
| `AI literacy\|AI fluency` | |
| `upskilling\|reskilling\|workforce readiness` | |
| `pilot to production\|POC to production\|proof of concept` | |
| `prompt library\|prompt template` | high precision — few write this |
| `internal champion\|power user\|subject matter expert\|SME` | |
| `office hours\|enablement session` | ⚠️ |
| `tool training\|training program` | ⚠️ |

### T2. Org change & leadership fear — **STRONG in practice, THIN in print** (drafts unpublished)
Standing: in the room with executive fear monthly; the 71% CEO imposter-syndrome stat is banked. Drafts exist ("Every leader is quietly afraid AI will expose what they don't know"; the RTO say-do gap) but nothing published — so this supports conversation, not a link.

| regex | note |
|---|---|
| `executive buy-in\|leadership buy-in\|exec sponsorship` | |
| `resistance\|skepticism\|pushback` | ⚠️ |
| `imposter\|impostor` | high precision |
| `psychological safety` | |
| `middle management\|frozen middle` | |
| `return to office\|RTO` | |
| `culture change\|cultural resistance` | |

### T3. Founder-led AI / building without engineers — **STRONG** · backing: Punchcard #1–3; "AI is like GeoCities" (~2025-12)
Standing: non-coder running production agent infrastructure daily; can name exactly where his human gate sits.
⚠️ **Hard rule:** never framed as engineering or as writing code. "Builds with Claude Code," "technology leader," never "engineer."

| regex | note |
|---|---|
| `vibe coding\|vibe-coding` | high precision |
| `non-technical\|non-coder\|citizen developer` | |
| `internal tools\|internal apps` | |
| `agentic\|AI agents?\|autonomous agents?` | ⚠️ |
| `human in the loop\|human-in-the-loop` | |
| `orchestrat` | catches orchestrator/orchestration |
| `multi-agent\|agent pipeline` | |
| `build versus buy\|build vs\.? buy` | |
| `personal software\|software for one` | high precision |

### T4. AI risk & model governance — **STRONG** · backing: "Do As I Say, Not As I Do" (2026-06-24)
Standing: the published rule — prototype on the newest model, ship one release back. First-person tool-seizure story (an export-control pull that took ~90 minutes). Authored a data-security and client-disclosure protocol for a client. Unusually apt for regulated and clinical audiences.

| regex | note |
|---|---|
| `AI governance\|model governance` | |
| `model deprecation\|model version\|version pinning` | high precision |
| `responsible AI\|AI ethics` | |
| `AI policy\|acceptable use` | |
| `data security\|data privacy` | ⚠️ |
| `client disclosure\|AI disclosure` | high precision |
| `vendor lock-in\|lock-in` | |
| `export control\|sanctions` | high precision |
| `audit trail\|auditability` | |

### T5. Ed-tech & special education — **STRONG** · backing: "The Hollow Click" (2026-07-23)
Standing: Adaptiverse — 500+ users, ~4,000 lessons created, B Corp, zero churn among institutional partners. Built for the population a deficit lens hurts most.
⚠️ Never claim FERPA compliance, NLP/ML/fine-tuning, or that agents auto-execute (they recommend and file; humans decide).

| regex | note |
|---|---|
| `special education\|special ed\b\|IEP\b` | high precision |
| `accessibility\|assistive technolog` | |
| `differentiation\|differentiated instruction` | |
| `teacher\|educator` | ⚠️ |
| `instructional design\|curriculum design` | |
| `K-12\|K12` | |
| `ed-?tech` | |
| `student outcomes\|learning outcomes` | |

### T6. Cost & architecture of AI systems — **STRONG** · backing: the Adaptiverse re-architecture (proof point, unpublished)
Standing: re-architected lesson generation from one long call into 4–12 parallel calls under an orchestrator on a cost-optimized model — a fully-loaded lesson returns for under $0.10, and faster. This is his most distinctive technical standing and it isn't in the theme inventory.

| regex | note |
|---|---|
| `cost per\|unit economics\|token cost\|inference cost` | |
| `cost-optimi[sz]ed\|model selection\|model routing` | |
| `parallel(i[sz]ation)?\|parallel calls` | ⚠️ |
| `latency` | ⚠️ |
| `context window\|prompt caching` | |

### T7. Associations, public affairs & healthcare-adjacent — **STRONG** (Jefferson's ruling, 2026-08-26; thin in print, strong on stage)
Standing: DMAS 2024 keynote to 200+ advocacy and public-affairs professionals; client work across public affairs, healthcare associations, education, professional services; **two sessions at the Iowa Hospital Association Annual Meeting, Oct 6 2026** — classroom breakouts of ~100 hospital leaders each at a 1,000–1,500-attendee conference — on AI leadership and organizational readiness, which arrived INBOUND off his published adoption writing.
⚠️ Graded on the room, not the page — no published piece here, so a T7 VOID ranks on standing alone and its supporting proof is spoken, not linkable.
⚠️ **Framing:** it is two ~100-person breakouts, NOT "a keynote for 1,500." Forward commitment only, no outcome claims.
⚠️ Embargo LIFTED by Jefferson 2026-08-26 — usable in applications, covers, and resumes. See the reserved-fact consequence in the outreach doctrine.
⚠️ Captain Tomorrow clients are never named — anonymized descriptors only.

| regex | note |
|---|---|
| `association\|membership organi[sz]ation` | ⚠️ |
| `public affairs\|advocacy\|government relations` | |
| `hospital\|health system\|clinical` | ⚠️ |
| `credentialing\|continuing education\|\bCE\b` | |
| `member engagement\|member value` | |
| `regulated industr` | |

### T8. Sales & GTM enablement — **MEDIUM** · backing: proof point 6 (unpublished)
Standing: architected and hardened a multi-stage AI sales-plan generation pipeline plus a reusable framework-based prompt-library system; a research-and-outreach engine that produced ~70 unique prospect emails.
⚠️ "Architected and hardened," never "built from scratch." No ROI metrics exist for client work — never claim any.

| regex | note |
|---|---|
| `sales enablement` | |
| `go-to-market\|GTM` | ⚠️ |
| `prospecting\|outbound` | ⚠️ |
| `personali[sz]ation at scale` | |

### T9. Building & leading a technology team — **MEDIUM** · backing: Beekeeper Group (unpublished)
Corrected by Jefferson 2026-08-26: Beekeeper was about **building and leading a technology team**, not martech or creative-ops subject matter. The earlier terms were wrong and are removed.

Standing: grew the team from 1 to 4–5 FTEs with 6+ year retention; directed R&D of Hexagon, a digital production platform — build time down ~50%, expenses down 20–30%, ~$300K capacity gains (2022).
⚠️ Directed and led — never framed as writing the code.

| regex | note |
|---|---|
| `engineering leadership\|technical leadership\|technology leader` | |
| `first technical hire\|building a team\|team building` | ⚠️ |
| `retention\|attrition\|turnover` | ⚠️ |
| `team topology\|org design\|reporting structure` | |
| `managing engineers\|leading engineers\|player-coach` | |
| `R&D\|research and development` | ⚠️ |
| `scaling a team\|headcount` | |

---

## §2 — Exclusions (never search, never cite)

- **Docent / the museum thesis.** Internal and unbranded. Never appears in a comment, note, or opening. Not a territory.
- *(Removed 2026-08-26 — the IHA engagement is no longer an exclusion. Jefferson lifted the embargo; it is usable in applications, covers, and resumes. Its correct framing is in T7: two ~100-person breakouts, NOT "a keynote for 1,500." This bullet previously contradicted T7 head-on and governed a rank-1 opening.)*
- **Named Captain Tomorrow clients.** Anonymized descriptors only.
- **Any ROI or outcome claim on Captain Tomorrow client work.** None exist.

---

## §3 — Signature phrases — NOT for the search regex

These are Jefferson's own framings. Searching a target's corpus for them returns zero for everyone and manufactures a false VOID on every theme. Two legitimate uses: picking a hook when the target's own words make his argument, and detecting when someone is already echoing him.

`deficit machine` · `asset-based rollout` · `the hollow click` · `Do As I Say, Not As I Do` · `iterations not time` · `trust not time` · `Black Mirrors` · `AI is like GeoCities` · `PromptLab` · `Punchcard`

---

## §4 — Machine-readable list

One regex per line, case-insensitive, for the Layer 5b null-result count. Territory tag first, tab-separated.

```
T1	AI adoption|adoption curve|user adoption
T1	AI enablement|enablement program
T1	AI rollout|rollout
T1	AI transformation|digital transformation
T1	change management
T1	AI literacy|AI fluency
T1	upskilling|reskilling|workforce readiness
T1	pilot to production|POC to production|proof of concept
T1	prompt library|prompt template
T1	internal champion|power user|subject matter expert|SME
T1	office hours|enablement session
T1	tool training|training program
T2	executive buy-in|leadership buy-in|exec sponsorship
T2	resistance|skepticism|pushback
T2	imposter|impostor
T2	psychological safety
T2	middle management|frozen middle
T2	return to office|RTO
T2	culture change|cultural resistance
T3	vibe coding|vibe-coding
T3	non-technical|non-coder|citizen developer
T3	internal tools|internal apps
T3	agentic|AI agents?|autonomous agents?
T3	human in the loop|human-in-the-loop
T3	orchestrat
T3	multi-agent|agent pipeline
T3	build versus buy|build vs\.? buy
T3	personal software|software for one
T4	AI governance|model governance
T4	model deprecation|model version|version pinning
T4	responsible AI|AI ethics
T4	AI policy|acceptable use
T4	data security|data privacy
T4	client disclosure|AI disclosure
T4	vendor lock-in|lock-in
T4	export control|sanctions
T4	audit trail|auditability
T5	special education|special ed\b|IEP\b
T5	accessibility|assistive technolog
T5	differentiation|differentiated instruction
T5	teacher|educator
T5	instructional design|curriculum design
T5	K-12|K12
T5	ed-?tech
T5	student outcomes|learning outcomes
T6	cost per|unit economics|token cost|inference cost
T6	cost-optimi[sz]ed|model selection|model routing
T6	parallel(i[sz]ation)?|parallel calls
T6	latency
T6	context window|prompt caching
T7	association|membership organi[sz]ation
T7	public affairs|advocacy|government relations
T7	hospital|health system|clinical
T7	credentialing|continuing education|\bCE\b
T7	member engagement|member value
T7	regulated industr
T8	sales enablement
T8	go-to-market|GTM
T8	prospecting|outbound
T8	personali[sz]ation at scale
T9	engineering leadership|technical leadership|technology leader
T9	first technical hire|building a team|team building
T9	retention|attrition|turnover
T9	team topology|org design|reporting structure
T9	managing engineers|leading engineers|player-coach
T9	R&D|research and development
T9	scaling a team|headcount
```

**Classification rule.** Per territory, not per term: high hits across many of the target's documents, and they frame it → **OCCUPIED**. Substantive on both sides → **PEER**. Recurring (≥3 occurrences in the Layer 2–3 window) but never developed → **OPEN**, the wedge. Zero hits across the fetchable corpus where standing is STRONG → **VOID**, always labeled INFERRED-FROM-FETCHABLE with the wall that could be hiding it named. A VOID on a MEDIUM or THIN territory does not rank in the top three. Every ranked row states whether a published piece backs it or the standing is spoken only.
