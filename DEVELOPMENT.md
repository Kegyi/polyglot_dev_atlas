# Polyglot Dev Atlas Development Guide

This document explains how to maintain the externalized content model introduced in Phase 1.

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
2. Run `npm run atlas:validate-content`.
3. Run `npm run atlas:build:strict` or `npm run atlas:check`.
4. Open generated output in `output/polyglot_dev_atlas.html` and spot-check affected views.

## Fallback behavior

Normal build mode still supports fallback to legacy defaults (in `legacy_content_defaults.py`) if a content file fails to load.
Use strict mode in CI or pre-merge checks to enforce JSON correctness.
