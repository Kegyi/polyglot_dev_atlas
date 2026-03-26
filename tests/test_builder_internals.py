import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from atlas_builder import assets, content, data_assembly


class _FakeHttpResponse:
    def __init__(self, payload):
        self._payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return self._payload


class ContentConfigLoadingTests(unittest.TestCase):
    def test_load_external_content_configs_uses_fallback_in_non_strict_mode(self):
        def broken_loader(_base_dir):
            raise ValueError("boom")

        fallback = {"fallback": True}
        with patch.object(content, "CONTENT_CONFIG_SOURCES", [("adapter_insights", "adapter_insights.json", broken_loader, fallback)]):
            with patch("atlas_builder.content.validate_content_manifest") as validate_manifest_mock:
                payload = content.load_external_content_configs("/tmp/base", strict=False)

        validate_manifest_mock.assert_called_once_with("/tmp/base")
        self.assertEqual(payload["adapter_insights"], fallback)

    def test_load_external_content_configs_raises_in_strict_mode(self):
        def broken_loader(_base_dir):
            raise ValueError("boom")

        with patch.object(content, "CONTENT_CONFIG_SOURCES", [("adapter_insights", "adapter_insights.json", broken_loader, {})]):
            with patch("atlas_builder.content.validate_content_manifest"):
                with self.assertRaises(RuntimeError):
                    content.load_external_content_configs("/tmp/base", strict=True)

    def test_validate_external_content_runs_strict_path(self):
        with patch("atlas_builder.content.load_external_content_configs") as load_configs_mock:
            content.validate_external_content("/tmp/base")

        load_configs_mock.assert_called_once_with("/tmp/base", strict=True)


class DataAssemblyTests(unittest.TestCase):
    def test_assemble_runtime_data_passes_strict_flag_and_returns_expected_keys(self):
        catalogs = {
            "problems": {"word_count": {"label": "Word Count"}},
            "interview": {"two_sum": {"label": "Two Sum"}},
            "basics": {"loops": {"label": "Loops"}},
            "design_patterns": {"strategy": {"label": "Strategy"}},
        }
        configs = {
            "principles": {"single_responsibility": {"label": "SRP"}},
            "course_steps": {"step_1": {"label": "Step 1"}},
            "adaptation_course": [{"level": 1, "title": "Foundation"}],
            "workflow": {"build": {"label": "Build"}},
            "interview_groups": [],
            "basics_groups": [],
            "design_patterns_groups": [],
            "principles_groups": [],
            "course_steps_groups": [],
            "workflow_groups": [],
            "modern_approach_notes": {},
            "adapter_insights": {},
            "basics_enhancements": {},
        }

        with patch("atlas_builder.data_assembly.load_example_catalogs", return_value=catalogs) as load_catalogs_mock:
            with patch("atlas_builder.data_assembly.load_external_content_configs", return_value=configs) as load_configs_mock:
                with patch("atlas_builder.data_assembly.apply_config_enrichment") as enrich_mock:
                    with patch("atlas_builder.data_assembly.print_missing_warnings") as warn_mock:
                        with patch("atlas_builder.data_assembly.load_home_html", return_value="<h1>Home</h1>") as home_mock:
                            payload = data_assembly.assemble_runtime_data(
                                "/tmp/base",
                                "/tmp/examples",
                                "/tmp/main.md",
                                strict_content=True,
                            )

        load_catalogs_mock.assert_called_once_with("/tmp/examples")
        load_configs_mock.assert_called_once_with("/tmp/base", strict=True)
        enrich_mock.assert_called_once()
        warn_mock.assert_called_once()
        home_mock.assert_called_once_with("/tmp/main.md")
        self.assertIn("home_html", payload)
        self.assertIn("problems", payload)
        self.assertIn("workflow_groups", payload)


class AssetsTests(unittest.TestCase):
    def test_run_generators_deduplicates_folders(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            cpp_dir = root / "cpp"
            cpp_dir.mkdir(parents=True)
            cpp_script = cpp_dir / "generate_cpp_cheat_sheet.py"
            cpp_script.write_text("print('ok')\n", encoding="utf-8")

            langs = [
                ("cpp", "C++", "cpp/cpp_cheat_sheet.html"),
                ("cpp_alt", "C++ alt", "cpp/cpp_alt.html"),
            ]

            with patch("atlas_builder.assets.subprocess.run") as run_mock:
                assets.run_generators(langs, str(root))

        run_mock.assert_called_once()

    def test_ensure_offline_assets_downloads_missing_and_skips_existing(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            offline_dir = Path(temp_dir)
            existing_path = offline_dir / "assets" / "exists.js"
            existing_path.parent.mkdir(parents=True, exist_ok=True)
            existing_path.write_bytes(b"cached")

            urls = {
                "assets/exists.js": "https://example.com/exists.js",
                "assets/new.js": "https://example.com/new.js",
            }

            with patch("atlas_builder.assets.urllib.request.urlopen", return_value=_FakeHttpResponse(b"downloaded")) as urlopen_mock:
                assets.ensure_offline_assets(str(offline_dir), urls)

            new_path = offline_dir / "assets" / "new.js"
            self.assertTrue(new_path.exists())
            self.assertEqual(new_path.read_bytes(), b"downloaded")
            urlopen_mock.assert_called_once_with("https://example.com/new.js", timeout=20)


if __name__ == "__main__":
    unittest.main()
