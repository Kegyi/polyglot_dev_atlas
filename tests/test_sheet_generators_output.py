import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

# (generator script, expected output file, expected separator label in escaped HTML)
GENERATOR_CASES = [
    (
        PROJECT_ROOT / "sheet_generators" / "cpp" / "generate_cpp_cheat_sheet.py",
        PROJECT_ROOT / "sheet_generators" / "cpp" / "cpp_cheat_sheet.html",
        "Advanced &amp; Modern",
    ),
    (
        PROJECT_ROOT / "sheet_generators" / "python" / "generate_python_cheat_sheet.py",
        PROJECT_ROOT / "sheet_generators" / "python" / "python_cheat_sheet.html",
        "Advanced &amp; Ecosystem",
    ),
    (
        PROJECT_ROOT / "sheet_generators" / "go" / "generate_go_cheat_sheet.py",
        PROJECT_ROOT / "sheet_generators" / "go" / "go_cheat_sheet.html",
        "Advanced &amp; Concurrency",
    ),
    (
        PROJECT_ROOT / "sheet_generators" / "typescript" / "generate_typescript_cheat_sheet.py",
        PROJECT_ROOT / "sheet_generators" / "typescript" / "typescript_cheat_sheet.html",
        "Advanced &amp; Ecosystem",
    ),
    (
        PROJECT_ROOT / "sheet_generators" / "scala" / "generate_scala_cheat_sheet.py",
        PROJECT_ROOT / "sheet_generators" / "scala" / "scala_cheat_sheet.html",
        "Advanced &amp; Ecosystem",
    ),
]

SCALA_VARIANTS = [
    PROJECT_ROOT / "sheet_generators" / "scala" / "scala2_cheat_sheet.html",
    PROJECT_ROOT / "sheet_generators" / "scala" / "scala3_cheat_sheet.html",
]


class SheetGeneratorOutputTests(unittest.TestCase):
    def test_generators_produce_expected_html_fragments(self):
        for script_path, output_path, separator_label in GENERATOR_CASES:
            with self.subTest(generator=str(script_path)):
                result = subprocess.run(
                    [sys.executable, str(script_path)],
                    cwd=str(script_path.parent),
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(
                    result.returncode,
                    0,
                    msg=f"Generator failed: {script_path}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}",
                )
                self.assertTrue(output_path.exists(), msg=f"Missing output file: {output_path}")

                html = output_path.read_text(encoding="utf-8")
                self.assertIn('<div class="legend-row">', html)
                self.assertIn('<div class="content">', html)
                self.assertIn('Description &amp; Version', html)
                self.assertIn(separator_label, html)
                self.assertNotIn("__TITLE__", html)
                self.assertNotIn("__CONTENT__", html)

    def test_scala_variants_are_written_and_titled(self):
        scala_script = PROJECT_ROOT / "sheet_generators" / "scala" / "generate_scala_cheat_sheet.py"
        result = subprocess.run(
            [sys.executable, str(scala_script)],
            cwd=str(scala_script.parent),
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)

        expected_headings = {
            "scala2_cheat_sheet.html": "Scala Polyglot Dev Atlas - Scala 2",
            "scala3_cheat_sheet.html": "Scala Polyglot Dev Atlas - Scala 3",
        }
        for output_path in SCALA_VARIANTS:
            with self.subTest(output=str(output_path)):
                self.assertTrue(output_path.exists())
                html = output_path.read_text(encoding="utf-8")
                self.assertIn(expected_headings[output_path.name], html)


if __name__ == "__main__":
    unittest.main()
