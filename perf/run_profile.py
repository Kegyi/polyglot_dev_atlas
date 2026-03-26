#!/usr/bin/env python3
import time
import tracemalloc
import json
from pathlib import Path
import sys
from pathlib import Path as _P

# Ensure the repository package root (polyglot_dev_atlas) is on sys.path
_ROOT = _P(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

OUT_DIR = Path("output")
OUT_FILE = OUT_DIR / "polyglot_dev_atlas.html"
METRICS_DIR = Path("performance")
METRICS_DIR.mkdir(exist_ok=True)
METRICS_FILE = METRICS_DIR / "baseline.json"

def main():
    skip_gen = True
    if "--full" in sys.argv or "--no-skip" in sys.argv:
        skip_gen = False
    metrics = {"skip_gen": skip_gen}
    try:
        tracemalloc.start()
        t0 = time.time()
        # Import here so module resolution uses the local package layout
        from atlas_builder.orchestrator import build

        build(skip_gen=skip_gen, strict_content=False)

        elapsed = time.time() - t0
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        metrics.update({
            "elapsed_seconds": elapsed,
            "tracemalloc_current_bytes": current,
            "tracemalloc_peak_bytes": peak,
        })

        if OUT_FILE.exists():
            metrics["output_path"] = str(OUT_FILE)
            metrics["output_size_bytes"] = OUT_FILE.stat().st_size
        else:
            metrics["output_path"] = str(OUT_FILE)
            metrics["output_size_bytes"] = None

        METRICS_FILE.write_text(json.dumps(metrics, indent=2))
        print(json.dumps(metrics, indent=2))

    except Exception as e:
        metrics["error"] = str(e)
        METRICS_FILE.write_text(json.dumps(metrics, indent=2))
        print(json.dumps(metrics, indent=2))
        raise

if __name__ == "__main__":
    main()
