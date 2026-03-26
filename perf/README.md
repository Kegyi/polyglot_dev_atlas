Profiler README
================

What it does
------------
This directory contains a small profiling harness used to collect build-time and memory metrics for the Polyglot Dev Atlas build.

Files
-----
- `run_profile.py` — runs the atlas build and records wall-clock time, tracemalloc memory samples, and produced output size. Writes `performance/baseline.json`.

How to run locally
------------------
From the `polyglot_dev_atlas` directory run:

```bash
python -u perf/run_profile.py        # runs with --skip-gen by default
python -u perf/run_profile.py --full # runs language generators + full build
```

Notes
-----
- The script adds the `polyglot_dev_atlas` package root to `sys.path` so it can be executed from `perf/`.
- For more detailed per-step timings enable orchestrator profiling via env var before running (CI uses this):

```bash
export POLYGLOT_PROFILE=1
python -u perf/run_profile.py --full
```

Outputs
-------
- `performance/baseline.json` — overall timing, tracemalloc peak, output size.
- `performance/orchestrator_metrics.json` — when `POLYGLOT_PROFILE=1`, contains per-step timings and memory snapshots.

CI
--
The GitHub Actions workflow `.github/workflows/performance-metrics.yml` runs the profiler on push, enables `POLYGLOT_PROFILE=1`, and uploads `polyglot_dev_atlas/performance/` and `polyglot_dev_atlas/output/` as artifacts.

Interpreting results
--------------------
- `elapsed_seconds`: total wall time for the script run.
- `tracemalloc_peak_bytes`: peak allocated bytes reported by tracemalloc.
- `timings` in the orchestrator metrics show hot steps to target for optimization (higher time = higher priority).
