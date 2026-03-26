def _build_head(shared_css, ui_styles):
    return [
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
    ]


def _build_top_stack():
    return [
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
        "      </div>\n",
        '      <div class="chip-row compare-row">\n',
        '        <span class="row-title">Style</span>\n',
        '        <div class="palette-previews" id="palettePreviews" aria-label="Palette previews">\n',
        '          <button type="button" class="palette-preview-btn" data-palette="brand" aria-pressed="false" title="Brand Accent">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        "          </button>\n",
        '          <button type="button" class="palette-preview-btn" data-palette="technical" aria-pressed="false" title="Technical">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        "          </button>\n",
        '          <button type="button" class="palette-preview-btn" data-palette="soft" aria-pressed="false" title="Soft Minimal">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        "          </button>\n",
        "        </div>\n",
        '        <button type="button" class="chip-btn subtle-btn theme-btn" id="themeToggle" aria-label="Switch to light theme" title="Switch to light theme">&#9728;</button>\n',
        '        <button type="button" class="chip-btn" id="compareToggle" aria-pressed="false">Compare</button>\n',
        '        <button type="button" class="chip-btn subtle-btn" id="swapBtn" title="Swap selected languages">Swap</button>\n',
        '        <button type="button" class="chip-btn" id="courseBtn" title="Start 7-level pro adaptation course">&#127891; Course</button>\n',
        "      </div>\n",
        "    </div>\n",
        "  </div>\n",
    ]


def _build_main_content():
    return [
        "\n  <main class=\"main-content\">\n",
        '    <section id="runtimeWarning" class="runtime-warning hidden" role="alert"></section>\n',
        '    <div class="catalog-layout" id="catalogLayout">\n',
        '      <aside class="catalog-sidebar hidden" id="catalogSidebar">\n',
        '        <div class="course-level-panel hidden" id="courseLevelPanel">\n',
        '          <div class="sidebar-header course-level-header">\n',
        '            <span class="sidebar-title" id="courseLevelTitle">Course Level</span>\n',
        '            <button type="button" class="sidebar-toggle-btn" id="courseLevelToggleBtn" title="Collapse course levels" aria-label="Collapse course levels">\u00AB</button>\n',
        "          </div>\n",
        '          <div class="course-level-list" id="courseLevelList"></div>\n',
        "        </div>\n",
        '        <div class="sidebar-header" id="topicSidebarHeader">\n',
        '          <span class="sidebar-title" id="sidebarTitle">Items</span>\n',
        '          <button type="button" class="sidebar-toggle-btn" id="sidebarToggleBtn" title="Collapse sidebar" aria-label="Collapse sidebar">\u00AB</button>\n',
        "        </div>\n",
        '        <div class="sidebar-list" id="sidebarList"></div>\n',
        "      </aside>\n",
        '      <button type="button" class="sidebar-expand-btn hidden" id="sidebarExpandBtn" title="Expand sidebar" aria-label="Expand sidebar">\u00BB</button>\n',
        '      <div class="catalog-main">\n',
        '        <section id="courseNavHeader" class="course-nav-header hidden">\n',
        '          <div class="course-nav-bar">\n',
        '            <button type="button" id="coursePrevBtn" class="course-nav-btn">&#8249; Prev</button>\n',
        '            <span id="courseNavTitle" class="course-nav-title"></span>\n',
        '            <button type="button" id="courseNextBtn" class="course-nav-btn">Next &#8250;</button>\n',
        "          </div>\n",
        '          <p id="courseNavDesc" class="course-nav-desc"></p>\n',
        '          <button type="button" id="courseExitBtn" class="course-nav-link">Go to Lang. Basic</button>\n',
        "        </section>\n",
        '        <section id="entryMeta" class="entry-meta hidden">\n',
        '          <h2 id="entryTitle"></h2>\n',
        '          <p id="entryDesc"></p>\n',
        '          <div id="entrySourceLinks"></div>\n',
        '          <div id="entryModernNotes"></div>\n',
        '          <div id="entryAdapterInsight"></div>\n',
        '          <div id="entryCompareLinks"></div>\n',
        "        </section>\n",
        '        <section id="contentHost"></section>\n',
        "      </div>\n",
        "    </div>\n",
        "  </main>\n\n",
    ]


def _build_scripts(app_js):
    return [
        '  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js" data-fallback="assets/hljs/highlight.min.js" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.src=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}"></script>\n',
        '  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/languages/scala.min.js" data-fallback="assets/hljs/languages/scala.min.js" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.src=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}"></script>\n',
        "  <script>\n",
        app_js,
        "\n  </script>\n",
        "</body>\n",
        "</html>\n",
    ]


def compose_html_document(shared_css, ui_styles, app_js):
    html_parts = []
    html_parts.extend(_build_head(shared_css, ui_styles))
    html_parts.extend(_build_top_stack())
    html_parts.extend(_build_main_content())
    html_parts.extend(_build_scripts(app_js))

    return "".join(html_parts)
