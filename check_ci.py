#!/usr/bin/env python3
"""Run CI-style checks for atlas content, strict build path, and tests."""

import subprocess
import sys
from pathlib import Path


def run_step(base_dir, args, label):
    print(f"[check] {label}")
    cmd = [sys.executable, "generate_output.py", *args]
    subprocess.run(cmd, cwd=base_dir, check=True)


def run_unittest_step(base_dir, test_targets, label):
    print(f"[check] {label}")
    cmd = [sys.executable, "-m", "unittest", *test_targets]
    subprocess.run(cmd, cwd=base_dir, check=True)


def main():
    base_dir = Path(__file__).resolve().parent

    try:
        run_step(base_dir, ["--validate-content"], "validate external content")
        run_step(base_dir, ["--strict-content", "--skip-gen"], "strict build (skip generators)")
        run_unittest_step(
            base_dir,
            ["test_content_loader.py", "test_atlas_builder.py"],
            "unit tests",
        )
    except subprocess.CalledProcessError as exc:
        print(f"[fail] command exited with code {exc.returncode}")
        return exc.returncode

    print("[ok] atlas checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
