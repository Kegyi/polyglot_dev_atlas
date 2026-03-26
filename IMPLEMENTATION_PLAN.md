# Polyglot Dev Atlas Implementation Plan

This roadmap defines the execution phases for maintainability and scalability improvements.

## Guiding principles

- Preserve current behavior while refactoring internals.
- Keep each phase independently releasable.
- Add guardrails (validation, tests, checks) before large structural changes.
- Prefer small, verifiable increments over big-bang rewrites.

## Status legend

- Complete: finished and verified.
- In progress: actively being executed.
- Planned: not started yet.

## Phase 0 - Baseline and risk map (Complete)

### Goal

Create a maintainability and scalability baseline and identify highest-risk hotspots.

### Deliverables

- Hotspot inventory with priorities.
- Refactor strategy split into phases.
- Change-risk classification (safe incremental vs heavy refactor).

### Exit criteria

- Clear order of operations documented.
- Agreement that targeted files are too large/complex for one-shot cleanup.

## Phase 1 - Content externalization and quality gates (Complete)

### Goal

Move content/config data out of generator logic and enforce correctness with validation and tests.

### Deliverables

- External JSON content model under content directory.
- Content loader and schema-style validation.
- Manifest governance for expected files.
- Strict mode and validate-only mode.
- CI-style checker script.
- Unit tests for content loader contracts.
- Legacy fallback defaults moved into dedicated module.
- Development documentation and npm script surface.

### Exit criteria

- Validation passes.
- Strict build passes.
- Unit tests pass.
- Single-command quality gate passes consistently.

## Phase 2 - Generator decomposition (Planned)

### Goal

Reduce complexity in generate_output and isolate orchestration from rendering/data wiring.

### Scope

- Split generator responsibilities into focused modules:
  - build orchestration
  - asset preparation
  - data assembly
  - template composition
- Keep CLI behavior unchanged.

### Deliverables

- New module layout with thin entrypoint.
- Reduced file size and cyclomatic complexity for generator entry module.
- Regression-safe adapter layer to preserve public behavior.

### Exit criteria

- Existing check pipeline remains green.
- No functional regression in produced HTML output.
- Main generator file becomes coordinator-focused rather than content-heavy.

## Phase 3 - Frontend modularization (Planned)

### Goal

Break large frontend monoliths into maintainable UI modules.

### Scope

- Decompose templates/app.js into:
  - state/store
  - view registry/router
  - renderers per major view
  - shared UI utilities
- Decompose templates/ui_styles.css into layered sections/components.

### Deliverables

- Modular JS files with explicit boundaries.
- CSS structure (base, layout, components, utilities).
- Build-time assembly step if needed (or generator-side concat).

### Exit criteria

- Existing UI behavior preserved (navigation, compare mode, metadata panel).
- Easier targeted edits for individual views.
- Style regressions minimized and documented.

## Phase 4 - Shared abstractions for language generators (Planned)

### Goal

Eliminate duplication across per-language sheet generators.

### Scope

- Introduce shared generation helpers and contracts.
- Standardize metadata extraction and output formatting.
- Keep language-specific custom behavior in thin adapters.

### Deliverables

- Common generator toolkit module.
- Reduced repeated code across language generator scripts.
- Consistent output invariants across all language sheets.

### Exit criteria

- Generator scripts become smaller and easier to extend.
- New language onboarding path documented.
- No regression in generated sheet structure.

## Phase 5 - Testing and regression safety expansion (Planned)

### Goal

Increase confidence for UI, generator, and integration behavior.

### Scope

- Add targeted unit tests for refactored generator modules.
- Add snapshot-like checks for critical generated sections.
- Add smoke checks for key JS view flows.

### Deliverables

- Expanded automated test suite.
- Golden/snapshot fixtures for deterministic generator output segments.
- Clear test matrix in docs.

### Exit criteria

- Breakages are detected before merge for core flows.
- Refactors can proceed with low manual verification overhead.

## Phase 6 - Performance and scalability hardening (Planned)

### Goal

Keep build/runtime performance stable as content and features grow.

### Scope

- Profile build path bottlenecks.
- Optimize repeated parsing/serialization work.
- Measure frontend runtime hotspots for large datasets.

### Deliverables

- Baseline performance report and target budgets.
- Low-risk optimizations with measured impact.
- Documentation of performance guardrails.

### Exit criteria

- Build time and output-size growth are monitored.
- UI remains responsive under expanded dataset volume.

## Phase 7 - Release readiness and governance (Planned)

### Goal

Finalize long-term maintenance workflow and contribution guardrails.

### Scope

- Enforce check pipeline in CI.
- Add contribution rules for content and generator changes.
- Define versioning/change-log policy for atlas structure updates.

### Deliverables

- CI policy and required checks.
- Contributor workflow doc updates.
- Lightweight release checklist.

### Exit criteria

- Team has a repeatable release process.
- New changes consistently follow validation and test gates.

## Recommended execution cadence

1. Complete one phase per milestone branch.
2. Keep each phase under small, reviewable pull requests.
3. Run full check command before every merge.
4. Produce a short phase closeout note with:
   - delivered scope
   - deferred items
   - known risks

## Immediate next action

Start Phase 2 by extracting generate_output orchestration into a small entry module and move data assembly/render wiring into dedicated modules, while keeping CLI flags and output identical.