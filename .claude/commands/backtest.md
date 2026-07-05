Backtest the gate against a role set (no research): $ARGUMENTS

1. Load the role set (Catalyst query via Notion MCP, or a provided list/file).
2. Apply pre-filters, then score every survivor per reference/rubric.md. No mid-test rubric adjustments.
3. Output the scored table sorted PASS → NEAR-MISS → FAIL, then prompt Jefferson for the gut pass ("would take the call" Y/N per PASS/NEAR-MISS).
4. On receiving gut answers: compute agreement rate, identify which criterion drives each disagreement, and propose (do not apply) rubric adjustments.
