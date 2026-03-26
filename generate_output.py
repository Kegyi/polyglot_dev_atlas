#!/usr/bin/env python3
"""
Generate a single self-contained HTML file with all Polyglot Dev Atlas content.

Output: polyglot_dev_atlas/output/polyglot_dev_atlas.html

Usage (run from within polyglot_dev_atlas/):
    python generate_output.py               # run per-language generators first, then build
    python generate_output.py --skip-gen    # skip running per-language generators (faster)
    python generate_output.py --validate-content  # validate externalized content JSON and exit
    python generate_output.py --strict-content     # build and fail fast if content JSON is invalid
"""

import sys
from atlas_builder.orchestrator import build, validate_content


if __name__ == "__main__":
    if "--validate-content" in sys.argv:
        validate_content()
    else:
        build(
            skip_gen="--skip-gen" in sys.argv,
            strict_content="--strict-content" in sys.argv,
        )



