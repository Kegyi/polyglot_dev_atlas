CI Policy (draft)
=================

Purpose
-------
This document defines the initial CI policy to support Phase 7 release readiness and governance.

Required checks (recommended names)
- `Validation (tests + content)` — ensures unit tests pass and `--validate-content` succeeds (workflow: `.github/workflows/validation.yml`).
- `Performance metrics` — captures profiler artifacts for PRs and pushes (workflow: `.github/workflows/performance-metrics.yml`).

Repository settings that an administrator should enable
- Branch protection on `main` and release branches:
  - Require pull request reviews before merging (1+ reviewer)
  - Require status checks to pass before merging: add the two checks above
  - Optionally enable required signed commits or linear history

How to adopt
- Add these two workflow files (validation + performance) to the repo (already included).
- An admin must then configure Branch protection rules in repository settings and select these checks as required.

Notes
- CI enforcement requires repository admin privileges to mark checks as required.
- Performance capture can be set as optional initially, then promoted to required once budgets are agreed.
