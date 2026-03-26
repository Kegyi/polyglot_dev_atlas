import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from generator_utils import read_file

from atlas_builder import app_payload, orchestrator, template
from atlas_builder.config import DEFAULT_BUILD_CONTEXT
from atlas_builder.enrichment import apply_config_enrichment
from atlas_builder.output_writer import write_output
from atlas_builder.runtime_content import load_home_html
from atlas_builder.sheets import load_sheets
from atlas_builder.ui_templates import load_ui_templates


BASE_DIR = Path(__file__).resolve().parent
DOCUMENT_STRUCTURE_FIXTURE = BASE_DIR / "test_fixtures" / "document_structure.json"
APP_JS_STRUCTURE_FIXTURE = BASE_DIR / "test_fixtures" / "app_js_structure.json"
ORCHESTRATOR_OUTPUT_STRUCTURE_FIXTURE = BASE_DIR / "test_fixtures" / "orchestrator_output_structure.json"


class TemplateTests(unittest.TestCase):
    def test_compose_html_document_matches_structure_fixture(self):
        output = template.compose_html_document("body{}", ".app{}", "console.log('x');")
        fixture = json.loads(read_file(str(DOCUMENT_STRUCTURE_FIXTURE)))

        for substring in fixture["requiredSubstrings"]:
            self.assertIn(substring, output)

        ordered_indexes = [output.index(substring) for substring in fixture["orderedSubstrings"]]
        self.assertEqual(ordered_indexes, sorted(ordered_indexes))


class UiTemplateTests(unittest.TestCase):
    def test_load_ui_templates_assembles_split_template_directories(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base_dir = Path(temp_dir)
            templates_dir = base_dir / "templates"
            (templates_dir / "app").mkdir(parents=True)
            (templates_dir / "ui_styles").mkdir(parents=True)

            (templates_dir / "app" / "00_head.js").write_text("(function () {\n", encoding="utf-8")
            (templates_dir / "app" / "10_body.js").write_text("console.log('atlas');\n", encoding="utf-8")
            (templates_dir / "app" / "20_tail.js").write_text("}());\n", encoding="utf-8")

            (templates_dir / "ui_styles" / "00_base.css").write_text(":root { --x: 1; }\n", encoding="utf-8")
            (templates_dir / "ui_styles" / "10_body.css").write_text("body { color: black; }\n", encoding="utf-8")

            ui_styles, app_template = load_ui_templates(str(base_dir))

        self.assertEqual(ui_styles, ":root { --x: 1; }\nbody { color: black; }\n")
        self.assertEqual(app_template, "(function () {\nconsole.log('atlas');\n}());\n")

    def test_load_ui_templates_falls_back_to_legacy_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base_dir = Path(temp_dir)
            templates_dir = base_dir / "templates"
            templates_dir.mkdir(parents=True)

            (templates_dir / "app.js").write_text("console.log('legacy');\n", encoding="utf-8")
            (templates_dir / "ui_styles.css").write_text("body{}\n", encoding="utf-8")

            ui_styles, app_template = load_ui_templates(str(base_dir))

        self.assertEqual(ui_styles, "body{}\n")
        self.assertEqual(app_template, "console.log('legacy');\n")

    def test_load_ui_templates_includes_store_router_and_renderer_registry(self):
        _ui_styles, app_template = load_ui_templates(str(BASE_DIR))

        self.assertIn("var appStore = {", app_template)
        self.assertIn("var appRouter = {", app_template)
        self.assertIn("var VIEW_RENDERERS = {", app_template)
        self.assertIn("function selectCurrentView() {", app_template)
        self.assertIn("function selectCurrentViewCategory() {", app_template)
        self.assertIn("function selectPrimaryLang() {", app_template)
        self.assertIn("function selectSecondaryLang() {", app_template)
        self.assertIn("function selectIsCompareMode() {", app_template)
        self.assertIn("function selectActiveCompareSlot() {", app_template)
        self.assertIn("function selectIsCourseMode() {", app_template)
        self.assertIn("function selectCourseLevel() {", app_template)
        self.assertIn("isSidebarCollapsed: function () {", app_template)
        self.assertIn("hasCourseTopicCollapseState: function (collapseKey) {", app_template)

    def test_load_ui_templates_includes_view_category_and_sidebar_persistence_flow(self):
        _ui_styles, app_template = load_ui_templates(str(BASE_DIR))

        self.assertIn("appStore.setViewCategory(appStore.getViewCategory() === 'atlas' ? 'learning' : 'atlas');", app_template)
        self.assertIn("localStorage.setItem(VIEW_CATEGORY_STORAGE_KEY, appStore.getViewCategory());", app_template)
        self.assertIn("savedViewCategory = window.localStorage.getItem(VIEW_CATEGORY_STORAGE_KEY) || 'atlas';", app_template)
        self.assertIn("appStore.setSidebarCollapsed(true);", app_template)
        self.assertIn("appStore.setSidebarCollapsed(false);", app_template)
        self.assertIn("savedSidebarCollapsed = window.localStorage.getItem(SIDEBAR_STORAGE_KEY) || '0';", app_template)
        self.assertIn("appStore.setSidebarCollapsed(savedSidebarCollapsed === '1');", app_template)

    def test_load_ui_templates_includes_course_mode_transition_flow(self):
        _ui_styles, app_template = load_ui_templates(str(BASE_DIR))

        self.assertIn("appStore.setCourseReturnState(appStore.getSelectionSnapshot());", app_template)
        self.assertIn("var snapshot = appStore.consumeCourseReturnState();", app_template)
        self.assertIn("appStore.restoreSelectionSnapshot(snapshot);", app_template)
        self.assertIn("appStore.setCourseMode(false);", app_template)
        self.assertIn("appStore.setCourseLevel(0);", app_template)
        self.assertIn("restorePreCourseView();", app_template)
        self.assertIn("rememberPreCourseView();", app_template)
        self.assertIn("appStore.setCourseMode(true);", app_template)
        self.assertIn("appStore.setViewCategory('atlas');", app_template)
        self.assertIn("navigateCourse(0);", app_template)

    def test_load_ui_templates_includes_compare_side_selection_flow(self):
        _ui_styles, app_template = load_ui_templates(str(BASE_DIR))

        self.assertIn("document.getElementById('compareToggle').addEventListener('click', function () {", app_template)
        self.assertIn("appStore.toggleCompareCount();", app_template)
        self.assertIn("var btn = event.target.closest('.side-pick-btn');", app_template)
        self.assertIn("if (!btn || !selectIsCompareMode()) {", app_template)
        self.assertIn("var side = Number(btn.dataset.side);", app_template)
        self.assertIn("appStore.setActiveSlot(side);", app_template)
        self.assertIn("function activeCompareSlot() {", app_template)
        self.assertIn("return selectActiveCompareSlot();", app_template)

    def test_load_ui_templates_preserves_key_event_flow_order(self):
        _ui_styles, app_template = load_ui_templates(str(BASE_DIR))

        compare_handler_anchor = "document.getElementById('contentHost').addEventListener('click', function (event) {"
        compare_handler_start = app_template.index(compare_handler_anchor)
        compare_flow = [
            "var btn = event.target.closest('.side-pick-btn');",
            "if (!btn || !selectIsCompareMode()) {",
            "var side = Number(btn.dataset.side);",
            "if (side !== 0 && side !== 1) {",
            "appStore.setActiveSlot(side);",
            "renderAll();",
        ]
        compare_indexes = [app_template.index(step, compare_handler_start) for step in compare_flow]
        self.assertEqual(compare_indexes, sorted(compare_indexes))

        view_category_anchor = "function toggleViewCategory() {"
        view_category_start = app_template.index(view_category_anchor)
        view_category_flow = [
            "appStore.setViewCategory(appStore.getViewCategory() === 'atlas' ? 'learning' : 'atlas');",
            "localStorage.setItem(VIEW_CATEGORY_STORAGE_KEY, appStore.getViewCategory());",
            "appStore.setView('');",
            "renderAll();",
        ]
        view_category_indexes = [app_template.index(step, view_category_start) for step in view_category_flow]
        self.assertEqual(view_category_indexes, sorted(view_category_indexes))


class AppPayloadTests(unittest.TestCase):
    def test_build_app_payload_merges_sheets_labels_and_runtime_data(self):
        runtime_data = {"home_html": "<h1>Home</h1>", "problems": {}}
        payload = app_payload.build_app_payload(
            {"cpp": {"label": "C++", "body": "<p>x</p>"}},
            {"cpp": "C++"},
            runtime_data,
        )

        self.assertIn("sheets", payload)
        self.assertIn("lang_labels", payload)
        self.assertEqual(payload["home_html"], "<h1>Home</h1>")

    def test_render_app_js_replaces_all_tokens(self):
        app_template = " ".join(
            token for token, _payload_key in app_payload.APP_TEMPLATE_TOKENS
        )
        payload = {
            "sheets": {"cpp": {"label": "C++", "body": "<p>x</p>"}},
            "home_html": "<h1>Home</h1>",
            "problems": {"word_count": {"label": "Word Count"}},
            "interview": {"two_sum": {"label": "Two Sum"}},
            "basics": {"strings": {"label": "Strings"}},
            "design_patterns": {"strategy": {"label": "Strategy"}},
            "principles": {"srp": {"label": "SRP"}},
            "course_steps": {"step_1": {"label": "Step 1"}},
            "adaptation_course": [{"label": "Level 1"}],
            "workflow": {"build": {"label": "Build"}},
            "interview_groups": [{"label": "Arrays", "keys": ["two_sum"]}],
            "basics_groups": [{"label": "Core", "keys": ["strings"]}],
            "design_patterns_groups": [{"label": "Behavioral", "keys": ["strategy"]}],
            "principles_groups": [{"label": "SOLID", "keys": ["srp"]}],
            "course_steps_groups": [{"label": "Foundations", "keys": ["step_1"]}],
            "workflow_groups": [{"label": "Build", "keys": ["build"]}],
            "lang_labels": {"cpp": "C++"},
        }

        app_js = app_payload.render_app_js(app_template, payload)
        fixture = json.loads(read_file(str(APP_JS_STRUCTURE_FIXTURE)))

        self.assertNotIn("__SHEETS_JSON__", app_js)
        for substring in fixture["requiredSubstrings"]:
            self.assertIn(substring, app_js)


class EnrichmentTests(unittest.TestCase):
    def test_apply_config_enrichment_merges_runtime_content(self):
        problems = {"word_count": {"label": "Word Count"}}
        basics = {"strings": {"label": "Strings"}}
        design_patterns = {"strategy": {"label": "Strategy"}}
        configs = {
            "modern_approach_notes": {"strategy": {"cpp": {"modern": "ranges"}}},
            "adapter_insights": {
                "word_count": {
                    "insight": "Prefer adapters for normalization",
                    "compareEntries": ["map_reduce"],
                }
            },
            "basics_enhancements": {
                "strings": {"notes": ["utf8"]},
                "collections": {"label": "Collections"},
            },
        }

        apply_config_enrichment(problems, basics, design_patterns, configs)

        self.assertIn("modernNotes", design_patterns["strategy"])
        self.assertEqual(problems["word_count"]["adapterInsight"], "Prefer adapters for normalization")
        self.assertEqual(problems["word_count"]["compareEntries"], ["map_reduce"])
        self.assertEqual(basics["strings"]["notes"], ["utf8"])
        self.assertIn("collections", basics)


class DataAssemblyTests(unittest.TestCase):

    def test_load_sheets_uses_fallback_for_missing_sheet(self):
        langs = [("cpp", "C++", "cpp/cpp_cheat_sheet.html")]

        with tempfile.TemporaryDirectory() as temp_dir:
            with patch("atlas_builder.sheets.print") as print_mock:
                sheets, lang_labels = load_sheets(langs, temp_dir)

        self.assertEqual(lang_labels["cpp"], "C++")
        self.assertIn("Sheet not found", sheets["cpp"]["body"])
        self.assertIn("C++", sheets["cpp"]["body"])
        print_mock.assert_called_once()

    def test_load_home_html_uses_fallback_for_missing_doc(self):
        with patch("atlas_builder.runtime_content.print") as print_mock:
            home_html = load_home_html("missing_main_page.md")

        self.assertIn("Main page doc not found", home_html)
        print_mock.assert_called_once()


class OutputWriterTests(unittest.TestCase):
    def test_write_output_creates_file_and_returns_size(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "output"
            output_file = output_dir / "atlas.html"

            size_kb = write_output(str(output_dir), str(output_file), "<html>atlas</html>")

            self.assertTrue(output_file.exists())
            self.assertEqual(output_file.read_text(encoding="utf-8"), "<html>atlas</html>")
            self.assertEqual(size_kb, 0)


class OrchestratorTests(unittest.TestCase):
    @patch("atlas_builder.orchestrator.print")
    @patch("atlas_builder.orchestrator.write_output", return_value=4)
    @patch("atlas_builder.orchestrator.compose_html_document", return_value="<html></html>")
    @patch("atlas_builder.orchestrator.render_app_js", return_value="console.log('ready');")
    @patch(
        "atlas_builder.orchestrator.build_app_payload",
        return_value={"sheets": {"cpp": {}}, "lang_labels": {"cpp": "C++"}, "home_html": "<h1>Home</h1>"},
    )
    @patch("atlas_builder.orchestrator.load_ui_templates", return_value=(".ui{}", "const app = {};"))
    @patch(
        "atlas_builder.orchestrator.assemble_runtime_data",
        return_value={
            "home_html": "<h1>Home</h1>",
            "problems": {},
            "interview": {},
            "basics": {},
            "design_patterns": {},
            "principles": {},
            "course_steps": {},
            "adaptation_course": [],
            "workflow": {},
            "interview_groups": [],
            "basics_groups": [],
            "design_patterns_groups": [],
            "principles_groups": [],
            "course_steps_groups": [],
            "workflow_groups": [],
        },
    )
    @patch("atlas_builder.orchestrator.load_sheets", return_value=({"cpp": {}}, {"cpp": "C++"}))
    @patch("atlas_builder.orchestrator.load_shared_css", return_value="body{}")
    @patch("atlas_builder.orchestrator.ensure_offline_assets")
    @patch("atlas_builder.orchestrator.run_generators")
    def test_build_respects_skip_gen_and_writes_output(
        self,
        run_generators_mock,
        ensure_assets_mock,
        load_shared_css_mock,
        load_sheets_mock,
        assemble_runtime_data_mock,
        load_ui_templates_mock,
        build_app_payload_mock,
        render_app_js_mock,
        compose_html_document_mock,
        write_output_mock,
        print_mock,
    ):
        orchestrator.build(skip_gen=True, strict_content=True)

        run_generators_mock.assert_not_called()
        ensure_assets_mock.assert_called_once()
        assemble_runtime_data_mock.assert_called_once_with(
            DEFAULT_BUILD_CONTEXT.base_dir,
            DEFAULT_BUILD_CONTEXT.code_examples_dir,
            DEFAULT_BUILD_CONTEXT.main_page_doc_path,
            strict_content=True,
        )
        build_app_payload_mock.assert_called_once_with(
            {"cpp": {}},
            {"cpp": "C++"},
            assemble_runtime_data_mock.return_value,
        )
        write_output_mock.assert_called_once_with(
            DEFAULT_BUILD_CONTEXT.output_dir,
            DEFAULT_BUILD_CONTEXT.output_file,
            "<html></html>",
        )
        self.assertGreaterEqual(print_mock.call_count, 2)

    @patch("atlas_builder.orchestrator.print")
    @patch("atlas_builder.orchestrator.write_output", return_value=4)
    @patch("atlas_builder.orchestrator.load_ui_templates", return_value=(".ui{}", "__SHEETS_JSON__ __PROBLEMS_JSON__"))
    @patch(
        "atlas_builder.orchestrator.assemble_runtime_data",
        return_value={
            "home_html": "<h1>Home</h1>",
            "problems": {"word_count": {"label": "Word Count"}},
            "interview": {},
            "basics": {},
            "design_patterns": {},
            "principles": {},
            "course_steps": {},
            "adaptation_course": [],
            "workflow": {},
            "interview_groups": [],
            "basics_groups": [],
            "design_patterns_groups": [],
            "principles_groups": [],
            "course_steps_groups": [],
            "workflow_groups": [],
        },
    )
    @patch(
        "atlas_builder.orchestrator.load_sheets",
        return_value=({"cpp": {"label": "C++", "body": "<p>Sheet</p>"}}, {"cpp": "C++"}),
    )
    @patch("atlas_builder.orchestrator.load_shared_css", return_value="body{}")
    @patch("atlas_builder.orchestrator.ensure_offline_assets")
    @patch("atlas_builder.orchestrator.run_generators")
    def test_build_writes_expected_rendered_output_fragment(
        self,
        run_generators_mock,
        ensure_assets_mock,
        load_shared_css_mock,
        load_sheets_mock,
        assemble_runtime_data_mock,
        load_ui_templates_mock,
        write_output_mock,
        print_mock,
    ):
        orchestrator.build(skip_gen=True, strict_content=False)

        written_output = write_output_mock.call_args[0][2]
        fixture = json.loads(read_file(str(ORCHESTRATOR_OUTPUT_STRUCTURE_FIXTURE)))

        for substring in fixture["requiredSubstrings"]:
            self.assertIn(substring, written_output)
        run_generators_mock.assert_not_called()
        ensure_assets_mock.assert_called_once()

    @patch("atlas_builder.orchestrator.print")
    @patch("atlas_builder.orchestrator.validate_external_content")
    def test_validate_content_delegates_to_content_module(self, validate_mock, print_mock):
        orchestrator.validate_content()

        validate_mock.assert_called_once_with(DEFAULT_BUILD_CONTEXT.base_dir)
        self.assertGreaterEqual(print_mock.call_count, 2)


if __name__ == "__main__":
    unittest.main()