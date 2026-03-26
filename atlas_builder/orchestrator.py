from .app_payload import build_app_payload, render_app_js
from .assets import ensure_offline_assets, run_generators
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
    if not skip_gen:
        print("Running language generators ...")
        run_generators(LANGS, DEFAULT_BUILD_CONTEXT.sheet_generators_dir)
    else:
        print("Skipping language generators (--skip-gen).")

    ensure_offline_assets(DEFAULT_BUILD_CONTEXT.offline_assets_dir, HLJS_ASSET_URLS)

    shared_css = load_shared_css(LANGS, DEFAULT_BUILD_CONTEXT.sheet_generators_dir)
    sheets, lang_labels = load_sheets(LANGS, DEFAULT_BUILD_CONTEXT.sheet_generators_dir)

    runtime_data = assemble_runtime_data(
        DEFAULT_BUILD_CONTEXT.base_dir,
        DEFAULT_BUILD_CONTEXT.code_examples_dir,
        DEFAULT_BUILD_CONTEXT.main_page_doc_path,
        strict_content=strict_content,
    )

    ui_styles, app_template = load_ui_templates(DEFAULT_BUILD_CONTEXT.base_dir)

    app_payload = build_app_payload(sheets, lang_labels, runtime_data)
    app_js = render_app_js(app_template, app_payload)

    output_html = compose_html_document(shared_css, ui_styles, app_js)

    size_kb = write_output(
        DEFAULT_BUILD_CONTEXT.output_dir,
        DEFAULT_BUILD_CONTEXT.output_file,
        output_html,
    )
    print(f"\nDone! Output written to:\n  {DEFAULT_BUILD_CONTEXT.output_file}\n  ({size_kb} KB)")
