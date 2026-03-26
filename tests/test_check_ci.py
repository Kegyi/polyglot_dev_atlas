import subprocess
import unittest
from unittest.mock import patch

from check_ci import main


class CheckCiTests(unittest.TestCase):
    def test_check_ci_runs_all_steps_and_returns_zero_on_success(self):
        calls = []

        def fake_run(cmd, cwd=None, check=None):
            calls.append(cmd)
            return None

        with patch('subprocess.run', side_effect=fake_run) as run_mock:
            rc = main()

        self.assertEqual(rc, 0)
        # validate-content step invoked
        self.assertTrue(any((isinstance(c, list) and '--validate-content' in c) or ('--validate-content' in str(c)) for c in calls))
        # unit tests step invoked
        self.assertTrue(any((isinstance(c, list) and '-m' in c and 'unittest' in c) or ('-m' in str(c) and 'unittest' in str(c)) for c in calls))

    def test_check_ci_returns_nonzero_on_step_failure(self):
        def fail_run(*args, **kwargs):
            raise subprocess.CalledProcessError(returncode=7, cmd=args[0])

        with patch('subprocess.run', side_effect=fail_run):
            rc = main()

        self.assertEqual(rc, 7)


if __name__ == '__main__':
    unittest.main()
