# Measurement instrument — org-play awareness tracking

**Why this exists:** the play's kill rules (e.g. Tenex 9/10, One Call 9/15: ~4 comments with zero engagement = park the lane) have no data source without it. Jefferson's ruling 2026-08-20: **measure BOTH** profile views (names the person) and comment engagement. Baseline must be captured BEFORE an org's first comment goes up, or the numbers mean nothing.

## Data store

`state/measurement.json` — single JSON file, committed with the repo. Shape:

```json
{
  "profile_views": [
    {"date": "YYYY-MM-DD", "count_90d": 0, "viewers_notable": ["Name — org, how found"]}
  ],
  "orgs": {
    "<org-slug>": {
      "baseline_date": "YYYY-MM-DD",
      "comments": [
        {
          "id": "tenex-01",
          "target_person": "Name",
          "post_url": "",
          "comment_url": "",
          "posted": "YYYY-MM-DD",
          "checks": [
            {"date": "YYYY-MM-DD", "reactions": 0, "replies": 0, "reply_from_target": false, "profile_views_from_org": []}
          ]
        }
      ]
    }
  }
}
```

## Capture procedure (read-only, his logged-in Chrome)

All reads via claude-in-chrome, never headless. Nothing is clicked beyond navigation; no reactions, follows, or messages from the capture pass.

1. **Profile views:** `linkedin.com/analytics/profile-views/` — record the 90-day count and, for each visible viewer, name + org **only when the org matches an active play** (that's the signal: the comment made someone look). Free-tier truncation is fine — record what's visible, note the truncation.
2. **Per-comment engagement:** open each `comment_url` in the log — record reaction count, reply count, and whether the TARGET person replied (the door-opening event).
3. Append a `checks[]` entry per comment and a `profile_views[]` entry per pass. Never overwrite history.

## Cadence

- Baseline: once per org, before comment #1.
- Active window (comments live): every 2–3 days, and always the day before a kill review.
- Kill-review input: the review reads this file; a lane with 4+ comments and all-zero checks = park (his ratified rule).

## Interpretation rules

- Zero engagement ≠ zero awareness (he: "more often than not, they've read my comments") — but the kill rule runs on the numbers anyway; the numbers are the tiebreaker, not the whole story.
- A profile view from the target org within ~72h of a comment counts as engagement for kill-review purposes even if the comment itself shows zero — note it in the check.
