# Preflight, 2026-10-18 (phase A of EXPERIMENT_PLAN_2026-10-18.md)

| # | Check | Result | Evidence |
|---|---|---|---|
| A1 | Network | pass | api.notion.com answers (HTTP/2 302) |
| A2 | Notion token | pass | GET /v1/users/me → integration "Claude Code Documentation" |
| A3 | Maigret | pass | tools/venv-maigret, version 0.6.5; the 10/15 second pass ran clean with `--dns-resolver threaded` |
| A4 | yt-dlp | fixed | was missing; installed into tools/venv-ytdlp (2026.08.19) |
| A5 | Claude in Chrome | pass | extension answered; one tab in the session group |
| A6 | Sign-ins (read-only check, nothing typed) | ChatGPT pass (composer present, no sign-in buttons) · Humantic pass (People Search, 29 recent) · LinkedIn pass (feed, notifications, "Me") · **Manus blocked** (manus.im/app redirects to its login page) · Glassdoor skipped by Jefferson's word | tab 1362385087 |
| A7 | Deep Research quota | open | to be read off the ChatGPT UI when the T3 sweep is started |
| A8 | Search budget | planned | no more than three search-heavy agents at once |
| A9 | Attio | pass | API key from ~/Sites/.jmos/.env; GET /v2/self → workspace Captain Tomorrow, active |
| A10 | Folder and sessions | pass | run folder clean after pull; ListAgents shows no other session in it (the 10/15 parent session has closed) |
| A11 | Brief currency | pass | SCAN_BRIEF.md carries the 10/15 rules paragraph |
| A12 | Exclusions | pass | Vanderbloemen and Dixon out; sends 0 of 30; Attio check runs on the keeps in phase C |
| A13 | Scale sign-off | pass | Jefferson, 10/18: 45 sends, v3 additions in force for the wave, "I'd like you to handle everything"; nothing goes out without his eyes |

**Manus.** Not blocking: the plan's fallback is ChatGPT Deep Research alone for the T3 sweep. If Jefferson signs in at manus.im in Chrome, the same sweep prompt (sweeps/manus-T2-sponsors.md shape) can run there too.
