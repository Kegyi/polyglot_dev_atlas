Contributing to Polyglot Dev Atlas
=================================

This document outlines the initial contributor workflow, content guidelines, and expectations for changes to generator code and content.

1. Branches & PRs
- Create a feature branch prefixed with the phase or area: `phase6/*`, `phase7/*`, `perf/*`, `docs/*`.
- Open a PR against `maintainability-scalability-improvements` (or `main` when ready).

2. Required checks
- All PRs should include passing unit tests and validation runs.
- The repository defines two CI checks that should be required for merges:
	- `Validation (tests + content)` (workflow: `.github/workflows/validation.yml`)
	- `Performance metrics` (workflow: `.github/workflows/performance-metrics.yml`) — optional at first, promote to required once budgets are agreed.
- Run locally:
	- `python -m unittest discover -s tests -v`
	- `python generate_output.py --validate-content`
	- `python perf/run_profile.py --full` (to reproduce profiler output)

3. Content changes
- Content files must pass `python generate_output.py --validate-content` in strict mode when editing content.

4. Code style
- Keep changes small and focused. Add unit tests for new logic.

5. Release notes
- Add an entry to `RELEASE_CHECKLIST.md` for noteworthy changes.
