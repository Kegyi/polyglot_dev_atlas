from .app_payload import build_app_payload, render_app_js
from .assets import ensure_offline_assets, run_generators
import os
import time
import json
from pathlib import Path
from .config import (
    DEFAULT_BUILD_CONTEXT,
    HLJS_ASSET_URLS,
    LANGS,
)
from .content import validate_external_content
from .data_assembly import (
    assemble_runtime_data,
)
from .output_writer import write_output
from .sheets import load_shared_css, load_sheets
from .template import compose_html_document
from .ui_templates import load_ui_templates


def validate_content():
    print("Validating external content JSON ...")
    validate_external_content(DEFAULT_BUILD_CONTEXT.base_dir)
    print("  [ok] external content validation passed.")


def build(skip_gen=False, strict_content=False):
    timings = {}
    mem_samples = {}

    def _now():
        return time.perf_counter()

    def _mem_snapshot(key):
        try:
            import tracemalloc

            current, peak = tracemalloc.get_traced_memory()
            mem_samples[key] = {"current": current, "peak": peak}
        except Exception:
            pass

    overall_start = _now()

    if not skip_gen:
        t0 = _now()
        print("Running language generators ...")
        run_generators(LANGS, DEFAULT_BUILD_CONTEXT.sheet_generators_dir)
        timings["run_generators"] = _now() - t0
        _mem_snapshot("after_run_generators")
    else:
        print("Skipping language generators (--skip-gen).")

    t0 = _now()
    ensure_offline_assets(DEFAULT_BUILD_CONTEXT.offline_assets_dir, HLJS_ASSET_URLS)
    timings["ensure_offline_assets"] = _now() - t0
    _mem_snapshot("after_ensure_offline_assets")

    t0 = _now()
    shared_css = load_shared_css(LANGS, DEFAULT_BUILD_CONTEXT.sheet_generators_dir)
    timings["load_shared_css"] = _now() - t0
    _mem_snapshot("after_load_shared_css")

    t0 = _now()
    sheets, lang_labels = load_sheets(LANGS, DEFAULT_BUILD_CONTEXT.sheet_generators_dir)
    timings["load_sheets"] = _now() - t0
    _mem_snapshot("after_load_sheets")

    t0 = _now()
    runtime_data = assemble_runtime_data(
        DEFAULT_BUILD_CONTEXT.base_dir,
        DEFAULT_BUILD_CONTEXT.code_examples_dir,
        DEFAULT_BUILD_CONTEXT.main_page_doc_path,
        strict_content=strict_content,
    )
    timings["assemble_runtime_data"] = _now() - t0
    _mem_snapshot("after_assemble_runtime_data")

    t0 = _now()
    ui_styles, app_template = load_ui_templates(DEFAULT_BUILD_CONTEXT.base_dir)
    timings["load_ui_templates"] = _now() - t0
    _mem_snapshot("after_load_ui_templates")

    t0 = _now()
    app_payload = build_app_payload(sheets, lang_labels, runtime_data)
    timings["build_app_payload"] = _now() - t0
    _mem_snapshot("after_build_app_payload")

    t0 = _now()
    app_js = render_app_js(app_template, app_payload)
    timings["render_app_js"] = _now() - t0
    _mem_snapshot("after_render_app_js")

    t0 = _now()
    output_html = compose_html_document(shared_css, ui_styles, app_js)
    timings["compose_html_document"] = _now() - t0
    _mem_snapshot("after_compose_html_document")

    t0 = _now()
    size_kb = write_output(
        DEFAULT_BUILD_CONTEXT.output_dir,
        DEFAULT_BUILD_CONTEXT.output_file,
        output_html,
    )
    timings["write_output"] = _now() - t0
    _mem_snapshot("after_write_output")

    overall_elapsed = _now() - overall_start
    print(f"\nDone! Output written to:\n  {DEFAULT_BUILD_CONTEXT.output_file}\n  ({size_kb} KB)")

    # If profiling requested via env var, write detailed timings
    try:
        if os.getenv("POLYGLOT_PROFILE") == "1":
            perf_dir = Path(DEFAULT_BUILD_CONTEXT.base_dir) / "performance"
            perf_dir.mkdir(parents=True, exist_ok=True)
            metrics_path = perf_dir / "orchestrator_metrics.json"
            metrics = {"timings": timings, "mem_samples": mem_samples, "overall_seconds": overall_elapsed}
            metrics_path.write_text(json.dumps(metrics, indent=2))
    except Exception:
        pass
