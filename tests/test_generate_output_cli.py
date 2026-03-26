import runpy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = PROJECT_ROOT / "generate_output.py"


class GenerateOutputCliTests(unittest.TestCase):
    def _run_cli(self, args):
        argv = [str(SCRIPT_PATH), *args]
        with patch.object(sys, "argv", argv):
            runpy.run_path(str(SCRIPT_PATH), run_name="__main__")

    def test_validate_content_flag_calls_validate_only(self):
        with patch("atlas_builder.orchestrator.validate_content") as validate_mock:
            with patch("atlas_builder.orchestrator.build") as build_mock:
                self._run_cli(["--validate-content"])

        validate_mock.assert_called_once_with()
        build_mock.assert_not_called()

    def test_validate_content_flag_takes_precedence_over_build_flags(self):
        with patch("atlas_builder.orchestrator.validate_content") as validate_mock:
            with patch("atlas_builder.orchestrator.build") as build_mock:
                self._run_cli(["--validate-content", "--skip-gen", "--strict-content"])

        validate_mock.assert_called_once_with()
        build_mock.assert_not_called()

    def test_build_receives_skip_and_strict_flags(self):
        with patch("atlas_builder.orchestrator.validate_content") as validate_mock:
            with patch("atlas_builder.orchestrator.build") as build_mock:
                self._run_cli(["--skip-gen", "--strict-content"])

        validate_mock.assert_not_called()
        build_mock.assert_called_once_with(skip_gen=True, strict_content=True)

    def test_strict_mode_failure_surfaces_from_build(self):
        with patch("atlas_builder.orchestrator.validate_content") as validate_mock:
            with patch("atlas_builder.orchestrator.build", side_effect=RuntimeError("strict failure")) as build_mock:
                with self.assertRaises(RuntimeError):
                    self._run_cli(["--skip-gen", "--strict-content"])

        validate_mock.assert_not_called()
        build_mock.assert_called_once_with(skip_gen=True, strict_content=True)


if __name__ == "__main__":
    unittest.main()
