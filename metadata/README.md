Repository metadata and documentation for Polyglot Dev Atlas.

This directory groups non-code artifacts that describe project policies, governance, and release practices.

Files
- `CI_POLICY.md` — CI policy and required checks guidance.
- `CONTRIBUTING.md` — contributor workflow, local test commands, and required checks.
- `GOVERNANCE.md` — roles and release process.
- `IMPLEMENTATION_PLAN.md` — project roadmap and phase closeouts.
- `RELEASE_CHECKLIST.md` — lightweight release checklist.
- `MAIN_PAGE_README.md` — main project landing page content (used by the generator).
- `proposal.md` — design/proposal notes captured during planning.
- `payload.json`, `payload_branch.json` — JSON payloads used to configure branch-protection API calls (kept here for reference).

Notes
- If other code in the repository references these files by name, update the code to reference the `metadata/` path.
- `MAIN_PAGE_README.md` is referenced by `atlas_builder/config.py` and has been updated accordingly.
