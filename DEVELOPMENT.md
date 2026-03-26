# Polyglot Dev Atlas Development Guide

This document explains how to maintain the externalized content model introduced in Phase 1.

Phase 3 now stores frontend template sources as ordered fragments under:

- `templates/app/`
- `templates/ui_styles/`

The builder assembles these directories in lexical filename order, so keep numeric prefixes on fragments when adding or moving sections.

## Build and validation commands

From repository root:

- `npm run atlas:validate-content`
  - Validates JSON payload shape for all externalized content files.
- `npm run atlas:build:strict`
  - Builds output and fails if content JSON is invalid.
- `npm run atlas:check`
  - Runs validation, strict build, and unit tests in one command.
- `npm run atlas:test`
  - Runs loader-level tests for content contracts and builder-level regression tests.

Direct Python commands (from `polyglot_dev_atlas/`):

- `python generate_output.py --validate-content`
- `python generate_output.py --strict-content --skip-gen`
- `python -m unittest discover -s tests -v`

## Test matrix

- `tests/test_content_loader.py`
  - External content manifest and payload contract checks.
- `tests/test_sheet_generators_shared.py`
  - Shared sheet-renderer helper contracts and formatting behavior.
- `tests/test_sheet_generators_output.py`
  - Snapshot-like HTML fragment checks for per-language generator output.
- `tests/test_atlas_builder.py`
  - Builder composition/orchestration regressions, template assembly invariants, and payload rendering structure checks.
- `tests/test_builder_internals.py`
  - Builder-internal unit/integration checks for content loading strictness, runtime assembly wiring, and offline asset/generator behavior.
- `tests/test_ui_flow_smoke.py`
  - UI event-flow smoke checks over assembled app template wiring and persisted state restoration order.

## External content files

External JSON files live under `polyglot_dev_atlas/content/`.

Manifest file:

- `content_manifest.json`
  - Declares expected content files and manifest schema version.
  - Strict checks fail if expected files are missing or unknown files are declared.

Current files:

- `principles.json`
- `modern_approach_notes.json`
- `course_steps.json`
- `basics_enhancements.json`
- `adapter_insights.json`
- `adaptation_course.json`
- `workflow.json`
- `basics_groups.json`
- `interview_groups.json`
- `design_patterns_groups.json`
- `principles_groups.json`
- `course_steps_groups.json`
- `workflow_groups.json`

## Content contract notes

- `principles.json`
  - map of principle key -> object with: `label`, `description`, `sourceLinks`, `points`, `notes`, `pitfalls`.
- `modern_approach_notes.json`
  - map of pattern key -> map of language -> `{ classic, modern }`.
- `course_steps.json`
  - map of step key -> object with: `label`, `description`, `compareEntries`, `adapterInsight`, `sourceLinks`, `codes`.
- `workflow.json`
  - map of workflow key -> object with: `label`, `description`, `codes`.
- group files (`*_groups.json`)
  - list of objects with: `label`, `keys`.

Validation logic is implemented in `content_loader.py` and used by `generate_output.py`.

## Editing workflow

1. Update content JSON file(s).
2. If you are changing frontend structure, edit the relevant fragment in `templates/app/` or `templates/ui_styles/`.
3. Run `npm run atlas:validate-content`.
4. Run `npm run atlas:test` or `npm run atlas:check`.
5. Open generated output in `output/polyglot_dev_atlas.html` and spot-check affected views.

## Phase 4 generator onboarding

Use this flow when adding a new language sheet generator under `sheet_generators/<lang>/`.

1. Create `generate_<lang>_cheat_sheet.py` and add a root import bootstrap:
  - Resolve `BASE_DIR` from the script location.
  - Insert `BASE_DIR` into `sys.path` if missing.
2. Define `KEYWORDS_DATA` as section/category/item maps matching existing generators.
3. Implement a language-specific `build_doc_url(item)` adapter only.
4. Reuse shared rendering helpers from `sheet_generators/shared_renderer.py`:
  - `render_section_table(...)` for table rendering.
  - `build_content_html(...)` for section assembly and advanced separator injection.
  - `render_sheet_html(...)` and `write_sheet_output(...)` for final output.
5. Add the language entry to builder config (`atlas_builder/config.py`) so orchestrator can load the generated HTML.
6. Run checks:
  - `python -m unittest -q`
  - `python generate_output.py`

Design rule: keep generators as thin adapters (data + doc URL mapping), and place shared formatting/output behavior in the shared renderer module.

## Fallback behavior

Normal build mode still supports fallback to legacy defaults (in `legacy_content_defaults.py`) if a content file fails to load.
Use strict mode in CI or pre-merge checks to enforce JSON correctness.
