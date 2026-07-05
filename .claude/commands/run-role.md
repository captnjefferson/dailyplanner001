Full pipeline run on an authorized role: $ARGUMENTS

1. Fetch the posting (URL or Catalyst Notion page). Confirm it passed the gate; if unscored, score it first and stop for confirmation if it fails.
2. Create runs/YYYY-MM-DD-<org-slug>/.
3. Launch ALL FOUR research subagents IN PARALLEL (org-researcher, posting-archaeologist, person-finder, voice-corpus — voice-corpus may need person-finder's output first; run it second if no HM candidate is obvious from the JD). Save each dossier to the run folder.
4. INTAKE: delete findings without working URLs. Spot-check 2–3 load-bearing citations by fetching them. Carry "Not Found" items into the gaps register.
5. SYNTHESIS (brief.md in run folder): Real Problem Hypothesis (one falsifiable sentence); the One Insight (must fail "could anyone else have written this?"); ONE matched proof point from background/profile.md; warm-path recommendation (intro-first / note-first / parallel); channel recommendation; source ledger; Gaps & Inference Register with [sourced]/[inferred — from X]/[speculation] tags.
6. DRAFT (note.md in run folder): the note per CLAUDE.md rule 3, plus the single value-add follow-up. Flag any sentence not backed by the ledger. End with the top 2 uncertainties a human must verify.
7. STOP. Never send. Tell Jefferson the run folder is ready for review.
