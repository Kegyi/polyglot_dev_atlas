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