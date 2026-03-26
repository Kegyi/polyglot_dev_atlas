import unittest
from pathlib import Path
import sys


BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from content_loader import (
    load_adapter_insights,
    load_adaptation_course,
    load_basics_enhancements,
    load_basics_groups,
    load_course_steps,
    load_course_steps_groups,
    load_design_patterns_groups,
    load_interview_groups,
    load_modern_approach_notes,
    load_principles,
    load_principles_groups,
    load_workflow,
    load_workflow_groups,
    validate_content_manifest,
)


class ContentLoaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_dir = str(BASE_DIR)

    def test_manifest_is_valid(self):
        manifest = validate_content_manifest(self.base_dir)
        self.assertEqual(manifest.get("version"), 1)
        self.assertIn("files", manifest)

    def test_principles_payload(self):
        principles = load_principles(self.base_dir)
        self.assertIn("single_responsibility", principles)

    def test_modern_notes_payload(self):
        notes = load_modern_approach_notes(self.base_dir)
        self.assertIn("strategy", notes)

    def test_course_steps_payload(self):
        steps = load_course_steps(self.base_dir)
        self.assertIn("step_1_memory_layout", steps)

    def test_basics_enhancements_payload(self):
        basics = load_basics_enhancements(self.base_dir)
        self.assertIn("type_system_comparison", basics)

    def test_adapter_insights_payload(self):
        insights = load_adapter_insights(self.base_dir)
        self.assertIn("word_count", insights)

    def test_group_payloads(self):
        self.assertGreaterEqual(len(load_basics_groups(self.base_dir)), 1)
        self.assertGreaterEqual(len(load_interview_groups(self.base_dir)), 1)
        self.assertGreaterEqual(len(load_design_patterns_groups(self.base_dir)), 1)
        self.assertGreaterEqual(len(load_principles_groups(self.base_dir)), 1)
        self.assertGreaterEqual(len(load_course_steps_groups(self.base_dir)), 1)
        self.assertIsInstance(load_workflow_groups(self.base_dir), list)

    def test_adaptation_course_payload(self):
        adaptation = load_adaptation_course(self.base_dir)
        self.assertGreaterEqual(len(adaptation), 1)

    def test_workflow_payload(self):
        workflow = load_workflow(self.base_dir)
        self.assertIn("build_run", workflow)


if __name__ == "__main__":
    unittest.main()
