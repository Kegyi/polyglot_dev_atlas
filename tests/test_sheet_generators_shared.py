import tempfile
import unittest
from pathlib import Path

from sheet_generators.shared_renderer import (
    build_content_html,
    render_section_table,
    render_sheet_html,
    split_deprecation_note,
    write_sheet_output,
)


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent


class SharedRendererTests(unittest.TestCase):
    def test_split_deprecation_note_extracts_marker(self):
        clean, marker = split_deprecation_note("Old API (deprecated in v2)")

        self.assertEqual(clean, "Old API")
        self.assertEqual(marker, "(deprecated in v2)")

    def test_render_section_table_applies_common_formatting(self):
        section = {
            "section": "Sample",
            "categories": [
                {
                    "label": "Cat A",
                    "items": [
                        {
                            "kw": "foo",
                            "cat": "logic",
                            "ver": "1.0",
                            "head": "Built-in",
                            "desc": "Desc (deprecated in v2)",
                            "code": "foo();",
                        }
                    ],
                }
            ],
        }

        html = render_section_table(
            section,
            lambda item: f"https://example.com/{item['kw']}",
            deprecated_class="deprecated-tag",
        )

        self.assertIn("<h2>Sample</h2>", html)
        self.assertIn('<tr class="category-label"><td colspan="4">Cat A</td></tr>', html)
        self.assertIn('<a href="https://example.com/foo" target="_blank">foo</a>', html)
        self.assertIn('<span class="deprecated-tag">(deprecated in v2)</span>', html)
        self.assertIn('<span class="version-tag">(since 1.0)</span>', html)

    def test_render_sheet_html_uses_shared_template(self):
        generator_path = PROJECT_ROOT / "sheet_generators" / "python" / "generate_python_cheat_sheet.py"
        output_html = render_sheet_html(str(generator_path), "Test Title", "<div>Legend</div>", "<p>Body</p>")

        self.assertIn("Test Title", output_html)
        self.assertIn("<div>Legend</div>", output_html)
        self.assertIn("<p>Body</p>", output_html)
        self.assertNotIn("__TITLE__", output_html)

    def test_build_content_html_inserts_advanced_separator(self):
        sections = [
            {"section": "Core", "categories": []},
            {"section": "Advanced", "is_advanced": True, "categories": []},
        ]

        output = build_content_html(
            sections,
            lambda section: f"<h2>{section['section']}</h2>",
            "Advanced & Ecosystem",
        )

        self.assertIn("<h2>Core</h2>", output)
        self.assertIn('<div class="separator"><span>Advanced &amp; Ecosystem</span></div>', output)
        self.assertIn("<h2>Advanced</h2>", output)

    def test_write_sheet_output_writes_to_generator_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fake_generator = Path(temp_dir) / "generate_fake.py"
            fake_generator.write_text("# fake", encoding="utf-8")

            out_path = write_sheet_output(str(fake_generator), "fake_output.html", "<html>x</html>")
            out_file = Path(out_path)

            self.assertTrue(out_file.exists())
            self.assertEqual(out_file.read_text(encoding="utf-8"), "<html>x</html>")


if __name__ == "__main__":
    unittest.main()
