Release checklist (lightweight)
=============================

Use this checklist before cutting a release or merging a major phase branch into `main`.

- [ ] All unit tests pass (`python -m unittest discover -s tests -v`)
- [ ] `python generate_output.py --validate-content` passes with `--strict-content` where applicable
- [ ] Performance regression: run `perf/run_profile.py --full` and compare with `performance/baseline.json` (attach artifacts to PR)
- [ ] Update `IMPLEMENTATION_PLAN.md` with closeout note for the phase
- [ ] Update `CHANGELOG.md` (if present) with user-visible changes
- [ ] Confirm CI required checks are configured in repo settings
- [ ] Tag release with semantic version and draft release notes
