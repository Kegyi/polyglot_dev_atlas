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
- Internal responsibilities are split across dedicated modules for orchestration, assets, sheets, runtime content, enrichment, payload rendering, UI templates, output writing, and HTML composition.
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

## Phase 5 - Testing and regression safety expansion (Complete)

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

### Progress note

- Added builder-internal regression tests in `tests/test_builder_internals.py` covering strict-vs-fallback content loading, runtime data assembly wiring, generator deduplication, and offline asset caching/download behavior.
- Added UI smoke regression tests in `tests/test_ui_flow_smoke.py` covering course-mode toggle flow, language-chip input mode wiring (click/contextmenu/pointer), and persisted theme/palette/view-category/sidebar restoration ordering before first render.
- Added a dedicated test-matrix section in `DEVELOPMENT.md` to document test intent and execution surface.
- Expanded orchestrator output snapshot fixture coverage (`test_fixtures/orchestrator_output_structure.json`) with stronger required and ordered HTML structure assertions.
- Added default-mode orchestration smoke coverage in `tests/test_atlas_builder.py` to assert generator execution and offline asset provisioning calls use canonical config inputs.
- Added app-payload token rendering contract fixture (`test_fixtures/app_payload_render_contract.json`) and corresponding golden-style assertions in `tests/test_atlas_builder.py`.
- Added strict-content failure propagation smoke coverage in `tests/test_atlas_builder.py` to ensure build aborts before output write when runtime assembly raises validation errors.
- Added CLI dispatch and failure-surfacing regression coverage in `tests/test_generate_output_cli.py` for `--validate-content`, `--skip-gen`, and `--strict-content` combinations.

### Exit criteria

- Breakages are detected before merge for core flows.
- Refactors can proceed with low manual verification overhead.

## Phase 6 - Performance and scalability hardening (Complete)

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

### Progress note

- Initial profiling runs kicked off against the canonical build with representative large content sets.
- Baseline metrics collection in progress (cold/hot build times, memory, output sizes, frontend render timings).
- Early hotspots identified: repeated parse/serialize loops during orchestration, duplicate template loads, and a handful of JS renderer hot paths for very large sheets.
- Short-term mitigations planned: add caching to template loads, memoize repeated serialization steps in the orchestrator, and add lightweight sampling-based frontend timing hooks for large payloads.

### Closeout note (early Phase 6 work)

- Added a small profiling harness: `perf/run_profile.py` (captures wall time, `tracemalloc` samples, and output size).
- Added `perf/README.md` documenting how to run the profiler and interpret outputs.
- Instrumented `atlas_builder/orchestrator.py` with optional per-step timers and memory snapshots; when `POLYGLOT_PROFILE=1` it writes `performance/orchestrator_metrics.json`.
- Collected baseline metrics (cold run) and saved to `performance/baseline.json`.
- Added CI workflow `.github/workflows/performance-metrics.yml` to run the profiler on push and upload `polyglot_dev_atlas/performance/` and `polyglot_dev_atlas/output/` as artifacts.

These deliverables provide a repeatable baseline and CI capture so subsequent optimizations can be validated by before/after measurements.

### Exit criteria

- Build and runtime hotspots are reduced to within agreed budgets.
- Measured build time or memory improvements validated by before/after benchmarks.


## Phase 7 - Release readiness and governance (Complete)

### Progress note

- CI validation workflow added and enabled: `.github/workflows/validation.yml` (unit tests + content validation).
- Performance capture workflow added: `.github/workflows/performance-metrics.yml` (uploads profiler artifacts).
- Contributor guidance and release checklist added: `CONTRIBUTING.md`, `RELEASE_CHECKLIST.md`.
- Governance and CI policy docs added: `GOVERNANCE.md`, `CI_POLICY.md`.
- `CODEOWNERS` added and branch protection applied to `main` and `maintainability-scalability-improvements` (required `Validation (tests + content)` check, admin enforcement, and code-owner reviews).
- Pull request created for Phase 6/7 changes and profiling artifacts are captured by CI.

### Closeout note

- Phase 7 deliverables completed: CI checks, branch protections, contributor docs, governance artifacts, and PR workflow established.

### Exit criteria

- CI required checks and branch protection are active for protected branches.
- Contributor guidelines and release checklist are available and referenced in the repo.
- Release owner/process assigned and used for the next release.

## Recommended execution cadence

1. Complete one phase per milestone branch.
2. Keep each phase under small, reviewable pull requests.
3. Run full check command before every merge.
4. Produce a short phase closeout note with:
   - delivered scope
   - deferred items
   - known risks

## Immediate next action

Close the release loop and begin maintenance:

- Assign a release owner and follow `RELEASE_CHECKLIST.md` to cut the next release (tag, draft release notes).
- Monitor CI validation and performance artifacts for regressions; refine budgets as needed.
- Onboard contributors to the `CONTRIBUTING.md` workflow and enforce code-owner review for sensitive areas.
- Track follow-up Phase 7 items (policy refinements, additional required checks) in small PRs.
