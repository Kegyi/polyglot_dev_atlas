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

## Phase 2 - Generator decomposition (Complete)

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

### Progress note

- Entry module is now coordinator-only.
- Internal responsibilities are split across dedicated modules for assets, sheets, runtime content, enrichment, payload rendering, UI templates, output writing, and HTML composition.
- Canonical check pipeline includes focused regression tests for module boundaries and rendered output fragments.

### Exit criteria

- Existing check pipeline remains green.
- No functional regression in produced HTML output.
- Main generator file becomes coordinator-focused rather than content-heavy.

### Closeout note

- Delivered scope:
  - `generate_output.py` reduced to a thin CLI entrypoint.
  - Generator internals decomposed into focused modules for orchestration, assets, sheets, runtime content, enrichment, payload rendering, UI templates, output writing, and HTML composition.
  - Canonical check pipeline expanded with regression tests for module boundaries and rendered output fragments.
- Deferred items:
  - Per-language generator standardization remains for later work.
  - Frontend modularization remains in Phase 3.
- Known risks:
    - Frontend behavior is still coupled through a shared global state object, so future Phase 3 work should separate renderers from state mutation paths.

## Phase 3 - Frontend modularization (Complete)

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

### Progress note

- Builder now assembles ordered frontend fragments from `templates/app/` and `templates/ui_styles/`.
- Former template monoliths have been split into first-pass JS modules and CSS sections without changing the generated HTML contract.
- Regression coverage now checks fragment assembly alongside existing payload rendering tests.
- Frontend control flow now has explicit boundaries for store/state access, routing, and renderer dispatch instead of direct `state.view` branching in the main bootstrap path.
- Compare-mode toggles, language selection, course navigation state, theme/palette selection, and sidebar collapse flows now route through `appStore` instead of mutating shared state directly from bootstrap and navigation handlers.
- Renderer and bootstrap read paths now use `appStore` selectors for language slots, compare state, course state, and theme/palette access, reducing direct shared-state coupling in view code.
- Shared helper/navigation view-category and language normalization paths now delegate to `appStore`; direct access for view/category/compare/lang state is effectively centralized in store internals.
- Sidebar collapsed visibility and course-topic collapse-key presence checks now use explicit `appStore` query methods, further reducing direct state-map access from view code.
- Template-assembly regression tests now assert those new store query method signatures (`isSidebarCollapsed`, `hasCourseTopicCollapseState`) remain present in the assembled app template.
- Template-assembly regression coverage now also checks view-category toggle persistence and sidebar collapsed persistence wiring (`VIEW_CATEGORY_STORAGE_KEY`, `SIDEBAR_STORAGE_KEY`) through `appStore` calls.
- Template-assembly regression coverage now checks course-mode transition wiring (`rememberPreCourseView`/`restorePreCourseView`) and associated `appStore` state transitions for entering and exiting course mode.
- Template-assembly regression coverage now checks compare-mode side-selection wiring (`toggleCompareCount`, `setActiveSlot`, and active-side renderer selection via `activeCompareSlot`).
- Behavior-oriented template regression now asserts ordered event-flow invariants inside key handlers (compare side-pick flow and view-category toggle flow), reducing risk of sequence regressions.
- Added a dedicated selector helper fragment (`templates/app/16_store_selectors.js`) for shared view/category/primary-language reads, and rewired navigation/bootstrap read paths to consume those shared selectors.
- Shared selector helpers now also cover compare/course reads (`selectSecondaryLang`, `selectIsCompareMode`, `selectActiveCompareSlot`, `selectIsCourseMode`, `selectCourseLevel`), and renderer/bootstrap consumers have been rewired to use them.
- Reorganized `appStore` object in `15_store_router.js` into explicit "QUERY METHODS" (read-only access) and "MUTATION METHODS" (state modification) sections with clear comment separators—improves code navigation and documents intent without changing behavior or test coverage.

### Exit criteria

- Existing UI behavior preserved (navigation, compare mode, metadata panel).
- Easier targeted edits for individual views.
- Style regressions minimized and documented.

### Closeout note

- Delivered scope:
  - Frontend monoliths (`templates/app.js`, `templates/ui_styles.css`) decomposed into modular fragments with lexical assembly.
  - Explicit boundaries established: `appStore` (state management), `appRouter` (routing), `VIEW_RENDERERS` (view dispatch).
  - Store reorganized into clear "QUERY METHODS" (read-only) and "MUTATION METHODS" (state modification) sections.
  - Shared selector helpers extracted into dedicated fragment (`templates/app/16_store_selectors.js`) covering view, language, compare, and course reads.
  - All state mutations now route through `appStore`; all state reads in view/navigation code use `appStore` selectors or shared helpers.
  - Template-assembly regression test coverage expanded from 22 to 26 tests, covering structural presence, persistence wiring, course transitions, compare flow, and behavior-order invariants.
  - All tests passing; zero regressions across 4+ full validation runs.
- Deferred items:
  - Per-language generator standardization remains for Phase 4.
  - Theme/palette snapshot reads could be extracted to shared selectors in future work (currently via appStore only).
  - Render-only utilities (`40_view_renderers.js`) could be further modularized by function category.
- Known risks addressed:
  - Frontend was previously coupled through direct global state access → now all access flows through `appStore` selector boundaries.
  - View renderers were mutating state directly → now all mutations go through `appStore` setters in handlers.
  - No assembly-time contract checking → now validated by 26 regression tests covering wiring patterns and invariants.


## Phase 4 - Shared abstractions for language generators (Complete)

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

### Progress note

- Introduced a shared generator toolkit module (`sheet_generators/shared_renderer.py`) for common table rendering, deprecation/version formatting, template loading, and output writing.
- Refactored C++, Python, Go, TypeScript, and Scala generators to consume shared rendering helpers while preserving language-specific documentation link adapters.
- Added dedicated unit coverage for shared toolkit contracts in `test_sheet_generators_shared.py`.
- Added shared section-assembly helper (`build_content_html`) so generators no longer duplicate advanced-separator/content-block orchestration loops.
- Documented a concrete new-language onboarding path in `DEVELOPMENT.md` centered on thin adapter generators plus shared renderer contracts.
- Added snapshot-like regression checks in `test_sheet_generators_output.py` that execute generators and assert key HTML output fragments and Scala variant headings.

### Exit criteria

- Generator scripts become smaller and easier to extend.
- New language onboarding path documented.
- No regression in generated sheet structure.

### Closeout note

- Delivered scope:
  - Shared generator toolkit implemented in `sheet_generators/shared_renderer.py` (table rendering, deprecation/version formatting, section assembly, template rendering, output writing).
  - Per-language generators refactored into thin adapters (language data + doc URL mapping) for C++, Python, Go, TypeScript, and Scala.
  - New-language onboarding workflow documented in `DEVELOPMENT.md`.
  - Regression safety expanded with shared-renderer unit tests and snapshot-like generator output checks (`tests/test_sheet_generators_shared.py`, `tests/test_sheet_generators_output.py`).
  - Test suite reorganized under `tests/` and standardized on unittest discovery (`python -m unittest discover -s tests -v`).
- Deferred items:
  - Additional doc-link adapter normalization can be layered as future cleanup if needed.
- Known risks addressed:
  - Cross-generator formatting drift reduced by centralized shared renderer contracts.
  - Output-structure regression risk reduced by generator output assertions and full-suite validation.

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

Start Phase 3 by decomposing `templates/app.js` into explicit state, routing, renderer, and shared UI utility modules while preserving current behavior.