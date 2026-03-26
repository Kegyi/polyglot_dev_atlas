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

import html as html_lib
import os
import subprocess
import sys
import urllib.request

from content_loader import (
    validate_content_manifest,
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
)

from generator_utils import (
    extract_between,
    load_examples_from_dir,
    markdown_to_html,
    normalize_sheet_body,
    read_file,
    safe_json,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SHEET_GENERATORS_DIR = os.path.join(BASE_DIR, "sheet_generators")
CODE_EXAMPLES_DIR = os.path.join(BASE_DIR, "code_examples")
MAIN_PAGE_DOC_PATH = os.path.join(BASE_DIR, "MAIN_PAGE_README.md")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "polyglot_dev_atlas.html")
OFFLINE_ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets", "hljs")

HLJS_ASSET_URLS = {
    "atom-one-dark.min.css": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/atom-one-dark.min.css",
    "github.min.css": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/github.min.css",
    "highlight.min.js": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js",
    "languages/scala.min.js": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/languages/scala.min.js",
}

# ---------------------------------------------------------------------------
# Language definitions: (id, display label, relative path to generated HTML)
# relative path is relative to SHEET_GENERATORS_DIR
# ---------------------------------------------------------------------------

LANGS = [
    ("cpp", "C++", "cpp/cpp_cheat_sheet.html"),
    ("python", "Python", "python/python_cheat_sheet.html"),
    ("go", "Go", "go/go_cheat_sheet.html"),
    ("typescript", "TypeScript", "typescript/typescript_cheat_sheet.html"),
    ("scala2", "Scala 2", "scala/scala2_cheat_sheet.html"),
    ("scala3", "Scala 3", "scala/scala3_cheat_sheet.html"),
]

from legacy_content_defaults import (
    ADAPTER_INSIGHTS,
    ADAPTATION_COURSE,
    BASICS_ENHANCEMENTS,
    BASICS_GROUPS,
    COURSE_STEPS,
    COURSE_STEPS_GROUPS,
    DESIGN_PATTERNS_GROUPS,
    INTERVIEW_GROUPS,
    MODERN_APPROACH_NOTES,
    PRINCIPLES,
    PRINCIPLES_GROUPS,
    WORKFLOW,
    WORKFLOW_GROUPS,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def run_generators():
    """Run each per-language generator once (deduplicated by folder)."""
    seen_folders = set()
    for _lang_id, _label, html_rel in LANGS:
        folder = html_rel.split("/")[0]
        if folder in seen_folders:
            continue
        seen_folders.add(folder)

        script = os.path.join(SHEET_GENERATORS_DIR, folder, f"generate_{folder}_cheat_sheet.py")
        if not os.path.exists(script):
            print(f"  [skip] no generator found: {script}")
            continue

        print(f"  [gen] {folder} ...")
        try:
            subprocess.run(
                [sys.executable, script],
                cwd=os.path.dirname(script),
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            print(f"  [warn] generator exited with code {exc.returncode}")
        except Exception as exc:
            print(f"  [warn] {exc}")


def ensure_offline_assets():
    """Ensure local highlight.js fallback files exist under output/assets/hljs."""
    os.makedirs(OFFLINE_ASSETS_DIR, exist_ok=True)

    downloaded = 0
    skipped = 0
    failed = 0

    for rel_path, url in HLJS_ASSET_URLS.items():
        dst = os.path.join(OFFLINE_ASSETS_DIR, *rel_path.split("/"))
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        if os.path.exists(dst) and os.path.getsize(dst) > 0:
            skipped += 1
            continue

        try:
            with urllib.request.urlopen(url, timeout=20) as resp:
                payload = resp.read()
            with open(dst, "wb") as fh:
                fh.write(payload)
            downloaded += 1
        except Exception as exc:
            failed += 1
            print(f"  [warn] could not fetch fallback asset: {url} ({exc})")

    print(
        "  [assets] offline hljs fallback -> "
        f"downloaded={downloaded}, existing={skipped}, failed={failed}"
    )



# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------


def _load_content_item(label, loader, fallback, strict):
    try:
        return loader(BASE_DIR)
    except Exception as exc:
        if strict:
            raise RuntimeError(f"content validation failed for {label}: {exc}") from exc
        print(f"  [warn] could not load content/{label}, using in-file fallback ({exc})")
        return fallback


CONTENT_CONFIG_SOURCES = [
    ("adapter_insights", "adapter_insights.json", load_adapter_insights, ADAPTER_INSIGHTS),
    ("basics_groups", "basics_groups.json", load_basics_groups, BASICS_GROUPS),
    ("interview_groups", "interview_groups.json", load_interview_groups, INTERVIEW_GROUPS),
    (
        "design_patterns_groups",
        "design_patterns_groups.json",
        load_design_patterns_groups,
        DESIGN_PATTERNS_GROUPS,
    ),
    ("principles_groups", "principles_groups.json", load_principles_groups, PRINCIPLES_GROUPS),
    ("course_steps_groups", "course_steps_groups.json", load_course_steps_groups, COURSE_STEPS_GROUPS),
    ("workflow_groups", "workflow_groups.json", load_workflow_groups, WORKFLOW_GROUPS),
    ("adaptation_course", "adaptation_course.json", load_adaptation_course, ADAPTATION_COURSE),
    ("workflow", "workflow.json", load_workflow, WORKFLOW),
    (
        "modern_approach_notes",
        "modern_approach_notes.json",
        load_modern_approach_notes,
        MODERN_APPROACH_NOTES,
    ),
    (
        "basics_enhancements",
        "basics_enhancements.json",
        load_basics_enhancements,
        BASICS_ENHANCEMENTS,
    ),
    ("course_steps", "course_steps.json", load_course_steps, COURSE_STEPS),
    ("principles", "principles.json", load_principles, PRINCIPLES),
]


def load_external_content_configs(strict=False):
    try:
        validate_content_manifest(BASE_DIR)
    except Exception as exc:
        if strict:
            raise RuntimeError(f"content manifest validation failed: {exc}") from exc
        print(f"  [warn] content manifest validation failed ({exc})")

    return {
        key: _load_content_item(file_name, loader, fallback, strict)
        for key, file_name, loader, fallback in CONTENT_CONFIG_SOURCES
    }


def validate_content():
    print("Validating external content JSON ...")
    load_external_content_configs(strict=True)
    print("  [ok] external content validation passed.")

def build():
    skip_gen = "--skip-gen" in sys.argv
    strict_content = "--strict-content" in sys.argv

    if not skip_gen:
        print("Running language generators ...")
        run_generators()
    else:
        print("Skipping language generators (--skip-gen).")

    ensure_offline_assets()

    shared_css = ""
    for _lang_id, _label, html_rel in LANGS:
        path = os.path.join(SHEET_GENERATORS_DIR, html_rel)
        if os.path.exists(path):
            shared_css = extract_between(read_file(path), "style")
            break

    if not shared_css:
        print("  [warn] Could not find shared CSS; falling back to empty styles.")

    sheets = {}
    lang_labels = {}
    for lang_id, label, html_rel in LANGS:
        lang_labels[lang_id] = label

        path = os.path.join(SHEET_GENERATORS_DIR, html_rel)
        if os.path.exists(path):
            body = normalize_sheet_body(extract_between(read_file(path), "body"))
        else:
            print(f"  [warn] missing sheet: {path}")
            body = (
                '<p class="empty-note">Sheet not found: '
                + html_lib.escape(label)
                + "<br>Run the generator first.</p>"
            )

        sheets[lang_id] = {
            "label": label,
            "body": body,
        }

    problems = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "problems"))
    interview = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "interview"))
    basics = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "language_basics"))
    design_patterns = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "design_patterns"))
    configs = load_external_content_configs(strict=strict_content)
    adapter_insights = configs["adapter_insights"]
    basics_groups = configs["basics_groups"]
    interview_groups = configs["interview_groups"]
    design_patterns_groups = configs["design_patterns_groups"]
    principles_groups = configs["principles_groups"]
    course_steps_groups = configs["course_steps_groups"]
    workflow_groups = configs["workflow_groups"]
    adaptation_course = configs["adaptation_course"]
    workflow = configs["workflow"]
    modern_approach_notes = configs["modern_approach_notes"]
    basics_enhancements = configs["basics_enhancements"]
    course_steps = configs["course_steps"]
    principles = configs["principles"]
    for pattern_key, notes in modern_approach_notes.items():
        if pattern_key in design_patterns:
            design_patterns[pattern_key]['modernNotes'] = notes
    for problem_key, insight_data in adapter_insights.items():
        if problem_key in problems:
            problems[problem_key]['adapterInsight'] = insight_data['insight']
            if insight_data.get('compareEntries'):
                problems[problem_key]['compareEntries'] = insight_data['compareEntries']
    for basic_key, enhancement in basics_enhancements.items():
        if basic_key in basics:
            basics[basic_key].update(enhancement)
        else:
            basics[basic_key] = enhancement

    if not problems:
        print("  [warn] no problem examples found.")
    if not interview:
        print("  [warn] no interview examples found.")
    if not basics:
        print("  [warn] no language basics examples found.")
    if not design_patterns:
        print("  [warn] no design pattern examples found.")
    if not principles:
        print("  [warn] no principles configured.")

    if os.path.exists(MAIN_PAGE_DOC_PATH):
        home_html = markdown_to_html(read_file(MAIN_PAGE_DOC_PATH))
    else:
        print(f"  [warn] missing main page doc: {MAIN_PAGE_DOC_PATH}")
        home_html = "<h1>Polyglot Dev Atlas</h1><p>Main page doc not found.</p>"

    ui_styles = read_file(os.path.join(BASE_DIR, "templates", "ui_styles.css"))
    app_template = read_file(os.path.join(BASE_DIR, "templates", "app.js"))

    app_js = (
        app_template.replace("__SHEETS_JSON__", safe_json(sheets))
        .replace("__HOME_HTML_JSON__", safe_json(home_html))
        .replace("__PROBLEMS_JSON__", safe_json(problems))
        .replace("__INTERVIEW_JSON__", safe_json(interview))
        .replace("__BASICS_JSON__", safe_json(basics))
        .replace("__DESIGN_PATTERNS_JSON__", safe_json(design_patterns))
        .replace("__PRINCIPLES_JSON__", safe_json(principles))
        .replace("__COURSE_STEPS_JSON__", safe_json(course_steps))
        .replace("__ADAPTATION_COURSE_JSON__", safe_json(adaptation_course))
        .replace("__WORKFLOW_JSON__", safe_json(workflow))
        .replace("__INTERVIEW_GROUPS_JSON__", safe_json(interview_groups))
        .replace("__BASICS_GROUPS_JSON__", safe_json(basics_groups))
        .replace("__DESIGN_PATTERNS_GROUPS_JSON__", safe_json(design_patterns_groups))
        .replace("__PRINCIPLES_GROUPS_JSON__", safe_json(principles_groups))
        .replace("__COURSE_STEPS_GROUPS_JSON__", safe_json(course_steps_groups))
        .replace("__WORKFLOW_GROUPS_JSON__", safe_json(workflow_groups))
        .replace("__LANG_LABELS_JSON__", safe_json(lang_labels))
    )

    html_parts = [
        "<!doctype html>\n",
        '<html lang="en">\n',
        "<head>\n",
        '  <meta charset="utf-8">\n',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n',
        "  <title>Polyglot Dev Atlas</title>\n",
        '  <link id="hljsDarkTheme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/atom-one-dark.min.css" data-fallback="assets/hljs/atom-one-dark.min.css" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.href=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}">\n',
        '  <link id="hljsLightTheme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/github.min.css" data-fallback="assets/hljs/github.min.css" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.href=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}" disabled>\n',
        "  <style>\n",
        shared_css,
        "\n",
        ui_styles,
        "\n  </style>\n",
        "</head>\n",
        '<body class="theme-dark palette-brand">\n',
        '  <div class="top-stack" id="topStack">\n',
        '    <div class="top-row">\n',
        '      <span class="row-title">Languages</span>\n',
        '      <nav class="chip-row" id="langNav" aria-label="Languages"></nav>\n',
        "    </div>\n",
        '    <div class="top-row" id="viewsRow">\n',
            '      <div class="course-hide-views" id="viewsSelection">\n',
            '        <span class="row-title">Views</span>\n',
            '        <nav class="chip-row" id="viewNav" aria-label="Views"></nav>\n',
            '        <span class="spacer"></span>\n',
            '      </div>\n',
        '      <div class="chip-row compare-row">\n',
        '        <span class="row-title">Style</span>\n',
        '        <div class="palette-previews" id="palettePreviews" aria-label="Palette previews">\n',
        '          <button type="button" class="palette-preview-btn" data-palette="brand" aria-pressed="false" title="Brand Accent">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        '          </button>\n',
        '          <button type="button" class="palette-preview-btn" data-palette="technical" aria-pressed="false" title="Technical">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        '          </button>\n',
        '          <button type="button" class="palette-preview-btn" data-palette="soft" aria-pressed="false" title="Soft Minimal">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        '          </button>\n',
        '        </div>\n',
        '        <button type="button" class="chip-btn subtle-btn theme-btn" id="themeToggle" aria-label="Switch to light theme" title="Switch to light theme">&#9728;</button>\n',
        '        <button type="button" class="chip-btn" id="compareToggle" aria-pressed="false">Compare</button>\n',
        '        <button type="button" class="chip-btn subtle-btn" id="swapBtn" title="Swap selected languages">Swap</button>\n',
        '        <button type="button" class="chip-btn" id="courseBtn" title="Start 7-level pro adaptation course">?? Course</button>\n',
        "      </div>\n",
        "    </div>\n",
        "  </div>\n",
        '\n  <main class="main-content">\n',
        '    <section id="runtimeWarning" class="runtime-warning hidden" role="alert"></section>\n',
        '    <div class="catalog-layout" id="catalogLayout">\n',
        '      <aside class="catalog-sidebar hidden" id="catalogSidebar">\n',
        '        <div class="course-level-panel hidden" id="courseLevelPanel">\n',
        '          <div class="sidebar-header course-level-header">\n',
        '            <span class="sidebar-title" id="courseLevelTitle">Course Level</span>\n',
        '            <button type="button" class="sidebar-toggle-btn" id="courseLevelToggleBtn" title="Collapse course levels" aria-label="Collapse course levels">\u00AB</button>\n',
        '          </div>\n',
        '          <div class="course-level-list" id="courseLevelList"></div>\n',
        '        </div>\n',
        '        <div class="sidebar-header" id="topicSidebarHeader">\n',
        '          <span class="sidebar-title" id="sidebarTitle">Items</span>\n',
        '          <button type="button" class="sidebar-toggle-btn" id="sidebarToggleBtn" title="Collapse sidebar" aria-label="Collapse sidebar">\u00AB</button>\n',
        '        </div>\n',
        '        <div class="sidebar-list" id="sidebarList"></div>\n',
        '      </aside>\n',
        '      <button type="button" class="sidebar-expand-btn hidden" id="sidebarExpandBtn" title="Expand sidebar" aria-label="Expand sidebar">\u00BB</button>\n',
        '      <div class="catalog-main">\n',
        '        <section id="courseNavHeader" class="course-nav-header hidden">\n',
        '          <div class="course-nav-bar">\n',
        '            <button type="button" id="coursePrevBtn" class="course-nav-btn">&#8249; Prev</button>\n',
        '            <span id="courseNavTitle" class="course-nav-title"></span>\n',
        '            <button type="button" id="courseNextBtn" class="course-nav-btn">Next &#8250;</button>\n',
        '          </div>\n',
        '          <p id="courseNavDesc" class="course-nav-desc"></p>\n',
        '          <button type="button" id="courseExitBtn" class="course-nav-link">Go to Lang. Basic</button>\n',
        '        </section>\n',
        '        <section id="entryMeta" class="entry-meta hidden">\n',
        '          <h2 id="entryTitle"></h2>\n',
        '          <p id="entryDesc"></p>\n',
        '          <div id="entrySourceLinks"></div>\n',
        '          <div id="entryModernNotes"></div>\n',
        '          <div id="entryAdapterInsight"></div>\n',
        '          <div id="entryCompareLinks"></div>\n',
        '        </section>\n',
        '        <section id="contentHost"></section>\n',
        '      </div>\n',
        '    </div>\n',
        "  </main>\n\n",
        '  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js" data-fallback="assets/hljs/highlight.min.js" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.src=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}"></script>\n',
        '  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/languages/scala.min.js" data-fallback="assets/hljs/languages/scala.min.js" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.src=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}"></script>\n',
        "  <script>\n",
        app_js,
        "\n  </script>\n",
        "</body>\n",
        "</html>\n",
    ]

    output_html = "".join(html_parts)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(output_html)

    size_kb = os.path.getsize(OUTPUT_FILE) // 1024
    print(f"\nDone! Output written to:\n  {OUTPUT_FILE}\n  ({size_kb} KB)")


if __name__ == "__main__":
    if "--validate-content" in sys.argv:
        validate_content()
    else:
        build()



