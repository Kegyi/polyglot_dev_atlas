    function selectedLang(slot) {
        return slot === 1 ? selectSecondaryLang() : selectPrimaryLang();
    }

    function isCompareMode() {
        return selectIsCompareMode();
    }

    function activeCompareSlot() {
        return selectActiveCompareSlot();
    }

    function renderSheetsView() {
        var host = document.getElementById('contentHost');

        if (!isCompareMode()) {
            var singleLang = selectedLang(0);
            var singleSheet = SHEETS[singleLang];
            var singleBody = singleSheet && singleSheet.body
                ? singleSheet.body
                : '<p class="empty-note">Sheet not found for ' + escapeHtml(singleLang) + '.</p>';

            host.innerHTML = ''
                + '<div class="display-grid">'
                + '  <section class="display-panel">'
                + '    <div class="display-title">' + escapeHtml(LANG_LABELS[singleLang] || singleLang) + '</div>'
                + '    <div class="panel-body sheet-body">' + singleBody + '</div>'
                + '  </section>'
                + '</div>';
            return;
        }

        var leftLang = selectedLang(0);
        var rightLang = selectedLang(1);
        var leftSheet = SHEETS[leftLang];
        var rightSheet = SHEETS[rightLang];
        var leftBody = leftSheet && leftSheet.body
            ? leftSheet.body
            : '<p class="empty-note">Sheet not found for ' + escapeHtml(leftLang) + '.</p>';
        var rightBody = rightSheet && rightSheet.body
            ? rightSheet.body
            : '<p class="empty-note">Sheet not found for ' + escapeHtml(rightLang) + '.</p>';

        host.innerHTML = ''
            + '<div class="display-grid compare">'
            + '  <section class="display-panel compare-panel' + (activeCompareSlot() === 0 ? ' active-side' : '') + '" data-side="0">'
            + '    <button type="button" class="display-side-btn side-pick-btn' + (activeCompareSlot() === 0 ? ' active' : '') + '" data-side="0">Left: ' + escapeHtml(LANG_LABELS[leftLang] || leftLang) + '</button>'
            + '    <div class="panel-body sheet-body">' + leftBody + '</div>'
            + '  </section>'
            + '  <section class="display-panel compare-panel' + (activeCompareSlot() === 1 ? ' active-side' : '') + '" data-side="1">'
            + '    <button type="button" class="display-side-btn side-pick-btn' + (activeCompareSlot() === 1 ? ' active' : '') + '" data-side="1">Right: ' + escapeHtml(LANG_LABELS[rightLang] || rightLang) + '</button>'
            + '    <div class="panel-body sheet-body">' + rightBody + '</div>'
            + '  </section>'
            + '</div>';
    }

    function renderHomeView() {
        setEntryTitleLevel('');
        var host = document.getElementById('contentHost');
        var baseHtml = HOME_HTML;
        var selected = [];

        function listLabels(viewKeys) {
            return (viewKeys || []).map(function (k) {
                var viewConfig = appStore.getViewConfig(k);
                return viewConfig ? viewConfig.label : k;
            }).filter(Boolean);
        }

        function renderUsageGuideGraphic() {
            var atlasViews = listLabels((VIEW_CATEGORIES.atlas && VIEW_CATEGORIES.atlas.views) || []);
            var learningViews = listLabels((VIEW_CATEGORIES.learning && VIEW_CATEGORIES.learning.views) || []);

            var primaryLangKey = LANG_ORDER.indexOf(selectedLang(0)) !== -1
                ? selectedLang(0)
                : (LANG_ORDER[0] || 'cpp');

            var secondaryLangKey = LANG_ORDER.indexOf(selectedLang(1)) !== -1
                ? selectedLang(1)
                : chooseNextLang(primaryLangKey);

            if (!secondaryLangKey || secondaryLangKey === primaryLangKey) {
                secondaryLangKey = chooseNextLang(primaryLangKey);
            }

            var movingLangKey = LANG_ORDER.find(function (k) {
                return k !== primaryLangKey && k !== secondaryLangKey;
            });

            if (!movingLangKey) {
                movingLangKey = chooseNextLang(secondaryLangKey || primaryLangKey);
            }

            var primaryLang = LANG_LABELS[primaryLangKey] || primaryLangKey || 'C++';
            var secondaryLang = LANG_LABELS[secondaryLangKey] || secondaryLangKey || 'Python';
            var movingLang = LANG_LABELS[movingLangKey] || movingLangKey || 'Go';

            var allLangChips = [primaryLang, secondaryLang, movingLang];
            LANG_ORDER.forEach(function (k) {
                if (k === primaryLangKey || k === secondaryLangKey || k === movingLangKey) {
                    return;
                }
                var label = LANG_LABELS[k] || k;
                if (label) {
                    allLangChips.push(label);
                }
            });

            function chipsToHtml(items) {
                if (!items.length) {
                    return '<span class="viewset-view-chip">No Views</span>';
                }
                return items.map(function (v) {
                    return '<span class="viewset-view-chip">' + escapeHtml(v) + '</span>';
                }).join('');
            }

            function renderTargetSequence(direction) {
                var right = direction === 'right';
                var head = allLangChips.slice(0, 2);
                var tail = allLangChips.slice(3);
                var html = '';

                head.forEach(function (label, idx) {
                    var cls = 'usage-chip';
                    cls += idx === 0 ? ' is-left' : ' is-right';
                    html += '<span class="' + cls + '">' + escapeHtml(label) + '</span>';
                });

                html += '<span class="usage-chip ' + (right ? 'is-moving-right' : 'is-moving-left') + '">' + escapeHtml(movingLang) + '</span>';

                tail.forEach(function (label) {
                    html += '<span class="usage-chip">' + escapeHtml(label) + '</span>';
                });

                return html;
            }

            return ''
                + '<section class="usage-guide-graphic">'
                + '  <header class="usage-guide-header">'
                + '    <h2>Graphical Usage Guide</h2>'
                + '    <p>This guide is generated from current project state so labels and views stay up to date.</p>'
                + '  </header>'
                + '  <div class="usage-steps-grid">'
                + '    <article class="usage-step-card">'
                + '      <div class="usage-step-number">1</div>'
                + '      <h3 class="usage-step-title">Selection Controls</h3>'
                + '      <p class="usage-step-text">Compare controls one-panel or two-panel selection. Swap flashes and swaps the language order.</p>'
                + '      <div class="usage-compare-demo">'
                + '        <div class="usage-compare-state state-off">'
                + '          <div class="usage-inline-row"><span class="usage-inline-label">Compare</span><div class="usage-chip-row"><span class="usage-chip is-left">' + escapeHtml(primaryLang) + '</span></div></div>'
                + '        </div>'
                + '        <div class="usage-compare-state state-on">'
                + '          <div class="usage-inline-row"><span class="usage-inline-label is-on">Compare</span><div class="usage-chip-row"><span class="usage-chip is-left">' + escapeHtml(primaryLang) + '</span><span class="usage-chip is-right">' + escapeHtml(secondaryLang) + '</span></div></div>'
                + '          <div class="usage-inline-row selection-swap-demo"><span class="usage-inline-label swap-btn">Swap</span><div class="usage-compare-unified"><div class="usage-target-unified"><div class="usage-target-lang-row"><span class="usage-target-lang-cell panel-left-active swap-side"><span class="swap-label-old">' + escapeHtml(primaryLang) + '</span><span class="swap-label-new">' + escapeHtml(secondaryLang) + '</span></span><span class="usage-target-lang-cell panel-right-active swap-side"><span class="swap-label-old">' + escapeHtml(secondaryLang) + '</span><span class="swap-label-new">' + escapeHtml(primaryLang) + '</span></span></div><div class="usage-target-code-row"><span class="usage-target-code-cell">//code//</span><span class="usage-target-code-cell">//code//</span></div></div></div></div>'
                + '        </div>'
                + '      </div>'
                + '    </article>'
                + '    <article class="usage-step-card">'
                + '      <div class="usage-step-number">2</div>'
                + '      <h3 class="usage-step-title">Language Targeting</h3>'
                + '      <p class="usage-step-text">Moving language replaces the targeted side. Highlight shifts to the new selected pair.</p>'
                + '      <div class="usage-lang-target-demo">'
                + '        <div class="usage-target-block target-right">'
                + '          <h4>Right Target</h4>'
                + '          <div class="usage-chip-row usage-target-seq">' + renderTargetSequence('right') + '</div>'
                + '          <div class="usage-target-result">'
                + '            <div class="usage-target-unified">'
                + '              <div class="usage-target-lang-row">'
                + '                <span class="usage-target-lang-cell panel-left-active">' + escapeHtml(primaryLang) + '</span>'
                + '                <span class="usage-target-lang-cell usage-panel-dynamic panel-right-active">'
                + '                <span class="label-old">' + escapeHtml(secondaryLang) + '</span>'
                + '                <span class="label-new">' + escapeHtml(movingLang) + '</span>'
                + '                </span>'
                + '              </div>'
                + '              <div class="usage-target-code-row">'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '              </div>'
                + '            </div>'
                + '          </div>'
                + '        </div>'
                + '        <div class="usage-target-block target-left">'
                + '          <h4>Left Target</h4>'
                + '          <div class="usage-chip-row usage-target-seq">' + renderTargetSequence('left') + '</div>'
                + '          <div class="usage-target-result">'
                + '            <div class="usage-target-unified">'
                + '              <div class="usage-target-lang-row">'
                + '                <span class="usage-target-lang-cell usage-panel-dynamic panel-left-active">'
                + '                <span class="label-old">' + escapeHtml(primaryLang) + '</span>'
                + '                <span class="label-new">' + escapeHtml(movingLang) + '</span>'
                + '                </span>'
                + '                <span class="usage-target-lang-cell panel-right-active">' + escapeHtml(secondaryLang) + '</span>'
                + '              </div>'
                + '              <div class="usage-target-code-row">'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '              </div>'
                + '            </div>'
                + '          </div>'
                + '        </div>'
                + '      </div>'
                + '    </article>'
                + '    <article class="usage-step-card">'
                + '      <div class="usage-step-number">3</div>'
                + '      <h3 class="usage-step-title">Choose View Set</h3>'
                + '      <p class="usage-step-text">Switch between ATLAS VIEWS and LEARNING VIEWS, then read the active view keywords below.</p>'
                + '      <div class="usage-viewset-demo">'
                + '        <div class="usage-viewset-state state-atlas">'
                + '          <span class="viewset-stage-label atlas">ATLAS VIEWS</span>'
                + '          <div class="viewset-view-chips">' + chipsToHtml(atlasViews) + '</div>'
                + '        </div>'
                + '        <div class="usage-viewset-state state-learning">'
                + '          <span class="viewset-stage-label learning">LEARNING VIEWS</span>'
                + '          <div class="viewset-view-chips">' + chipsToHtml(learningViews) + '</div>'
                + '        </div>'
                + '      </div>'
                + '    </article>'
                + '  </div>'
                + '</section>';
        }

        function pushUniqueLang(langKey) {
            var base = langKey;
            if (base === 'scala2' || base === 'scala3') {
                base = 'scala';
            }
            if (!base || selected.indexOf(base) !== -1) {
                return;
            }
            selected.push(base);
        }

        pushUniqueLang(selectedLang(0));
        if (isCompareMode()) {
            pushUniqueLang(selectedLang(1));
        }

        function snippetLanguage(baseLang) {
            if (baseLang === 'scala') {
                return 'scala';
            }
            return highlightLang(baseLang);
        }

        var cards = '';
        selected.forEach(function (langKey) {
            var profile = LANGUAGE_SPECIFIC_BEGINNER_GUIDE[langKey] || null;
            var points = LANGUAGE_SPECIFIC_FEATURES[langKey] || [];

            if (!profile) {
                var fallbackList = '<ul>' + points.map(function (p) {
                    return '<li>' + escapeHtml(p) + '</li>';
                }).join('') + '</ul>';
                cards += ''
                    + '<article class="lang-feature-card">'
                    + '  <h3 class="lang-feature-lang">' + escapeHtml(LANG_LABELS[langKey] || langKey) + '</h3>'
                    + '  <p class="lang-feature-intro">Detailed beginner guide is not configured yet.</p>'
                    + '  <section class="lang-feature-section">'
                    + '    <h4 class="lang-feature-heading">Key Features</h4>'
                    +      fallbackList
                    + '  </section>'
                    + '</article>';
                return;
            }

            var mindsetHtml = '<ul>' + (profile.mindsets || []).map(function (point) {
                return '<li>' + escapeHtml(point) + '</li>';
            }).join('') + '</ul>';

            var snippetHtml = (profile.snippets || []).map(function (item) {
                return ''
                    + '<section class="lang-feature-snippet">'
                    + '  <h4 class="lang-feature-heading">' + escapeHtml(item.title || 'Snippet') + '</h4>'
                    + '  <p>' + escapeHtml(item.note || '') + '</p>'
                    + '  <pre class="code-block home-code-block"><code class="code-sample language-' + snippetLanguage(langKey) + '">' + escapeHtml(item.code || '') + '</code></pre>'
                    + '</section>';
            }).join('');

            cards += ''
                + '<article class="lang-feature-card">'
                + '  <h3 class="lang-feature-lang">' + escapeHtml(LANG_LABELS[langKey] || langKey) + '</h3>'
                + '  <p class="lang-feature-intro">' + escapeHtml(profile.intro || '') + '</p>'
                + '  <section class="lang-feature-section">'
                + '    <h4 class="lang-feature-heading">Beginner Mindset</h4>'
                +      mindsetHtml
                + '  </section>'
                + '  <section class="lang-feature-section">'
                + '    <h4 class="lang-feature-heading">Code Patterns</h4>'
                +      snippetHtml
                + '  </section>'
                + '</article>';
        });

        if (!cards) {
            cards = ''
                + '<article class="lang-feature-card">'
                + '  <h3 class="lang-feature-lang">No language selected</h3>'
                + '  <p class="lang-feature-intro">Pick one or two languages from the top row to see beginner-friendly language-specific features.</p>'
                + '</article>';
        }

        var dynamicSection = ''
            + '<div class="lang-feature-overview">'
            + '  <p>Some advanced features are intentionally language-specific and should be documented per language instead of forced into one-to-one equivalents. <span class="lang-feature-overview-highlight">This section explains why each feature matters, then shows tiny snippets you can pattern-match while learning.</span></p>'
            + '</div>'
            + '<div class="lang-feature-grid">' + cards + '</div>';

        baseHtml = baseHtml.replace('<h2>Quick Usage Guide</h2>', '<h2>Quick Usage Guide</h2>' + renderUsageGuideGraphic());

        baseHtml = baseHtml.replace('<p>__LANG_SPECIFIC_FEATURES__</p>', dynamicSection);
        baseHtml = baseHtml.replace('__LANG_SPECIFIC_FEATURES__', dynamicSection);

        host.innerHTML = ''
            + '<div class="display-grid">'
            + '  <section class="display-panel">'
            + '    <div class="panel-body doc-body">' + baseHtml + '</div>'
            + '  </section>'
            + '</div>';
    }

    function exercisePanel(entry, langKey, sideIndex) {
        var titleHtml = '';
        var exerciseTitle = exerciseLabelParts(entry.label || '').title || entry.label || '';
        var sectionAttrs = ' class="display-panel"';
        if (sideIndex === 0 || sideIndex === 1) {
            sectionAttrs = ' class="display-panel compare-panel' + (activeCompareSlot() === sideIndex ? ' active-side' : '') + '" data-side="' + sideIndex + '"';
            titleHtml = '<button type="button" class="display-side-btn side-pick-btn' + (activeCompareSlot() === sideIndex ? ' active' : '') + '" data-side="' + sideIndex + '">' + escapeHtml((sideIndex === 0 ? 'Left: ' : 'Right: ') + (LANG_LABELS[langKey] || langKey)) + '</button>';
        } else {
            titleHtml = '<div class="display-title">Task: ' + escapeHtml(exerciseTitle) + ' (' + escapeHtml(LANG_LABELS[langKey] || langKey) + ')</div>';
        }

        return ''
            + '<section' + sectionAttrs + '>'
            + titleHtml
            + '  <div class="panel-body exercise-panel-body">'
            + '    <button type="button" class="chip-btn exercise-solution-toggle" aria-expanded="false">Show Solution</button>'
            + '    <div class="exercise-solution hidden">'
            + '      <pre class="code-block"><code class="code-sample language-' + highlightLang(langKey) + '">' + escapeHtml(codeFor(entry, langKey)) + '</code></pre>'
            + '    </div>'
            + '  </div>'
            + '</section>';
    }

    function renderExercisesView() {
        var host = document.getElementById('contentHost');
        var entry = currentEntry();

        if (!entry) {
            updateEntryMeta('', '', [], null, null, null, selectedLang(0));
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No exercise tasks available.</p></section></div>';
            return;
        }

        var parts = exerciseLabelParts(entry.label || '');
        var exerciseTitle = parts.title || entry.label || '';
        updateEntryMeta(exerciseTitle, entry.description || '', entry.sourceLinks || [], null, null, entry.compareEntries || [], selectedLang(0));
        setEntryTitleLevel(parts.level || '');

        if (!isCompareMode()) {
            var lang = selectedLang(0);
            host.innerHTML = ''
                + '<div class="display-grid">'
                + exercisePanel(entry, lang, null)
                + '</div>';
            return;
        }

        var leftLang = selectedLang(0);
        var rightLang = selectedLang(1);
        host.innerHTML = ''
            + '<div class="display-grid compare">'
            + exercisePanel(entry, leftLang, 0)
            + exercisePanel(entry, rightLang, 1)
            + '</div>';
    }

    function codeFor(entry, langKey) {
        if (!entry || !entry.codes) {
            return '// missing';
        }
        return entry.codes[langKey] || '// missing';
    }

    function highlightLang(langKey) {
        return LANG_TO_HL[langKey] || 'plaintext';
    }

    function syncHighlightTheme() {
        var darkTheme = document.getElementById('hljsDarkTheme');
        var lightTheme = document.getElementById('hljsLightTheme');
        if (!darkTheme || !lightTheme) {
            return;
        }

        if (appStore.getTheme() === 'light') {
            lightTheme.disabled = false;
            darkTheme.disabled = true;
        } else {
            darkTheme.disabled = false;
            lightTheme.disabled = true;
        }
    }

    function updateThemeToggle() {
        var toggle = document.getElementById('themeToggle');
        if (!toggle) {
            return;
        }

        var isDark = appStore.getTheme() === 'dark';
        toggle.innerHTML = isDark ? '&#9728;' : '&#9790;';
        toggle.title = isDark ? 'Switch to light theme' : 'Switch to dark theme';
        toggle.setAttribute('aria-label', toggle.title);
    }

    function applyTheme(themeName) {
        appStore.setTheme(themeName);

        document.body.classList.remove('theme-light', 'theme-dark');
        document.body.classList.add(appStore.getTheme() === 'light' ? 'theme-light' : 'theme-dark');

        updateThemeToggle();
        syncHighlightTheme();
        applySyntaxHighlight();

        try {
            window.localStorage.setItem(THEME_STORAGE_KEY, appStore.getTheme());
        } catch (err) {
            // storage can be disabled
        }
    }

    function applyPalette(paletteName) {
        appStore.setPalette(paletteName);

        document.body.classList.remove('palette-brand', 'palette-technical', 'palette-soft');
        document.body.classList.add('palette-' + appStore.getPalette());

        renderPaletteSelector();

        try {
            window.localStorage.setItem(PALETTE_STORAGE_KEY, appStore.getPalette());
        } catch (err) {
            // storage can be disabled
        }
    }

    function codePanel(title, code, sideIndex, langKey, modernCode) {
        var titleHtml = '';
        var sectionAttrs = ' class="display-panel"';
        if (sideIndex === 0 || sideIndex === 1) {
            sectionAttrs = ' class="display-panel compare-panel' + (activeCompareSlot() === sideIndex ? ' active-side' : '') + '" data-side="' + sideIndex + '"';
            titleHtml = '<button type="button" class="display-side-btn side-pick-btn' + (activeCompareSlot() === sideIndex ? ' active' : '') + '" data-side="' + sideIndex + '">' + escapeHtml(title) + '</button>';
        } else {
            titleHtml = '<div class="display-title">' + escapeHtml(title) + '</div>';
        }

        var codeClass = 'code-sample language-' + highlightLang(langKey);

        var modernHtml = '';
        if (modernCode) {
            modernHtml = '<div class="display-title display-title-subtle">Modern ' + escapeHtml(LANG_LABELS[langKey] || langKey) + '</div>'
                + '<pre class="code-block"><code class="code-sample language-' + highlightLang(langKey) + '">' + escapeHtml(modernCode) + '</code></pre>';
        }

        return ''
            + '<section' + sectionAttrs + '>'
            + titleHtml
            + '  <pre class="code-block"><code class="' + codeClass + '">' + escapeHtml(code) + '</code></pre>'
            + modernHtml
            + '</section>';
    }

    function courseTopicCollapseKey(topicKey) {
        return String(appStore.getCourseLevel()) + ':' + String(topicKey || '');
    }

    function isCourseTopicCollapsed(topicKey, topicIndex) {
        var key = courseTopicCollapseKey(topicKey);
        if (appStore.hasCourseTopicCollapseState(key)) {
            return appStore.isCourseTopicCollapsed(key);
        }
        return topicIndex > 0;
    }

    function topicBodyGrid(entry) {
        function modernKey(langKey) {
            var base = (langKey === 'scala2' || langKey === 'scala3') ? 'scala' : langKey;
            return base + '_modern';
        }

        if (!isCompareMode()) {
            var lang = selectedLang(0);
            var modernCode = (entry.codes && entry.codes[modernKey(lang)]) || null;
            return ''
                + '<div class="display-grid">'
                + codePanel('Code: ' + (LANG_LABELS[lang] || lang), codeFor(entry, lang), null, lang, modernCode)
                + '</div>';
        }

        var leftLang = selectedLang(0);
        var rightLang = selectedLang(1);
        var leftModern = (entry.codes && entry.codes[modernKey(leftLang)]) || null;
        var rightModern = (entry.codes && entry.codes[modernKey(rightLang)]) || null;

        return ''
            + '<div class="display-grid compare">'
            + codePanel('Left: ' + (LANG_LABELS[leftLang] || leftLang), codeFor(entry, leftLang), 0, leftLang, leftModern)
            + codePanel('Right: ' + (LANG_LABELS[rightLang] || rightLang), codeFor(entry, rightLang), 1, rightLang, rightModern)
            + '</div>';
    }

    function renderCourseTopicsView() {
        var host = document.getElementById('contentHost');
        var level = ADAPTATION_COURSE[appStore.getCourseLevel()];
        var entries = (VIEW_CONFIG.basics && VIEW_CONFIG.basics.entries) ? VIEW_CONFIG.basics.entries : {};

        updateEntryMeta('', '', [], null, null, null, selectedLang(0));

        if (!level) {
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No course level configured.</p></section></div>';
            return;
        }

        var keys = (level.viewItems || []).filter(function (key) {
            return !!entries[key];
        });

        if (keys.length === 0) {
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No basic topics are mapped to this course level yet.</p></section></div>';
            return;
        }

        var html = keys.map(function (key, idx) {
            var entry = entries[key];
            var collapsed = isCourseTopicCollapsed(key, idx);
            var descHtml = entry.description
                ? '<p class="course-topic-desc">' + escapeHtml(entry.description) + '</p>'
                : '';
            var insightHtml = entry.adapterInsight
                ? '<div class="course-topic-insight">' + renderAdapterInsight(entry.adapterInsight) + '</div>'
                : '';
            var compareHtml = renderCompareEntries(entry.compareEntries || []);

            return ''
                + '<section class="course-topic-section">'
                + '  <button type="button" class="course-topic-toggle" data-topic-key="' + escapeHtml(key) + '" data-topic-index="' + idx + '" aria-expanded="' + (collapsed ? 'false' : 'true') + '">'
                + '    <span class="course-topic-title">' + escapeHtml(entry.label || key) + '</span>'
                + '    <span class="course-topic-caret">' + (collapsed ? '\u25BE' : '\u25B4') + '</span>'
                + '  </button>'
                + '  <div class="course-topic-body' + (collapsed ? ' hidden' : '') + '">'
                +       descHtml
                +       insightHtml
                +       compareHtml
                +       topicBodyGrid(entry)
                + '  </div>'
                + '</section>';
        }).join('');

        host.innerHTML = '<div class="course-topics-stack">' + html + '</div>';
    }

    function applySyntaxHighlight() {
        if (!window.hljs || typeof window.hljs.highlightElement !== 'function') {
            return;
        }

        var blocks = document.querySelectorAll('#contentHost .code-sample');
        blocks.forEach(function (block) {
            block.removeAttribute('data-highlighted');
            try {
                window.hljs.highlightElement(block);
            } catch (err) {
                // ignore malformed snippets
            }
        });
    }

    function renderCodeView() {
        setEntryTitleLevel('');
        if (appStore.isCourseModeEnabled()) {
            renderCourseTopicsView();
            return;
        }
        var host = document.getElementById('contentHost');
        var entry = currentEntry();

        if (!entry) {
            updateEntryMeta('', '', [], null, null, null, selectedLang(0));
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No entries available for this view.</p></section></div>';
            return;
        }

        updateEntryMeta(entry.label || '', entry.description || '', entry.sourceLinks || [], entry.modernNotes || null, entry.adapterInsight || null, entry.compareEntries || [], selectedLang(0));

        function modernKey(langKey) {
            var base = (langKey === 'scala2' || langKey === 'scala3') ? 'scala' : langKey;
            return base + '_modern';
        }

        if (!isCompareMode()) {
            var lang = selectedLang(0);
            var modernCode = (entry.codes && entry.codes[modernKey(lang)]) || null;
            host.innerHTML = ''
                + '<div class="display-grid">'
                + codePanel('Code: ' + (LANG_LABELS[lang] || lang), codeFor(entry, lang), null, lang, modernCode)
                + '</div>';
            return;
        }

        var leftLang = selectedLang(0);
        var rightLang = selectedLang(1);
        var leftModern = (entry.codes && entry.codes[modernKey(leftLang)]) || null;
        var rightModern = (entry.codes && entry.codes[modernKey(rightLang)]) || null;
        host.innerHTML = ''
            + '<div class="display-grid compare">'
            + codePanel('Left: ' + (LANG_LABELS[leftLang] || leftLang), codeFor(entry, leftLang), 0, leftLang, leftModern)
            + codePanel('Right: ' + (LANG_LABELS[rightLang] || rightLang), codeFor(entry, rightLang), 1, rightLang, rightModern)
            + '</div>';
    }

    function renderPrinciplesView() {
        setEntryTitleLevel('');
        var host = document.getElementById('contentHost');
        var entry = currentEntry();

        if (!entry) {
            updateEntryMeta('', '', [], null, null, null, selectedLang(0));
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No principles available.</p></section></div>';
            return;
        }

        updateEntryMeta('', '', [], null, null, null, selectedLang(0));

        var points = entry.points || [];
        var notes = entry.notes || [
            'Use this principle as a guideline, not an absolute law.',
            'Balance it against delivery speed, performance, and team context.'
        ];
        var pitfalls = entry.pitfalls || [
            'Applying the principle as a rigid rule instead of context-sensitive guidance.',
            'Over-engineering abstractions too early before requirements stabilize.',
            'Ignoring trade-offs in performance, delivery speed, or team familiarity.'
        ];
        var refs = entry.sourceLinks || [];
        var notesHtml = notes.length
            ? '<ul>' + notes.map(function (n) { return '<li>' + escapeHtml(n) + '</li>'; }).join('') + '</ul>'
            : '<p class="empty-note">No notes for this principle yet.</p>';
        var listHtml = points.length
            ? '<ul>' + points.map(function (p) { return '<li>' + escapeHtml(p) + '</li>'; }).join('') + '</ul>'
            : '<p class="empty-note">No practical guidelines listed.</p>';
        var pitfallsHtml = pitfalls.length
            ? '<ul>' + pitfalls.map(function (p) { return '<li>' + escapeHtml(p) + '</li>'; }).join('') + '</ul>'
            : '<p class="empty-note">No pitfalls listed.</p>';
        var refsHtml = refs.length
            ? '<p>' + refs.map(function (r) {
                var label = r && r.label ? r.label : 'Source';
                var url = r && r.url ? r.url : '';
                if (!url) {
                    return escapeHtml(label);
                }
                return '<a href="' + escapeHtml(url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(label) + '</a>';
            }).join('<br>') + '</p>'
            : '<p class="empty-note">No references listed.</p>';

        host.innerHTML = ''
            + '<div class="display-grid">'
            + '  <section class="display-panel">'
            + '    <div class="panel-body doc-body principles-body">'
            + '      <section class="principles-section principles-header">'
            + '        <h2>' + escapeHtml(entry.label || '') + '</h2>'
            + '        <p>' + escapeHtml(entry.description || '') + '</p>'
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>Notes</h3>'
            +          notesHtml
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>Practical Guidelines</h3>'
            +          listHtml
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>Common Pitfalls</h3>'
            +          pitfallsHtml
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>References</h3>'
            +          refsHtml
            + '      </section>'
            + '    </div>'
            + '  </section>'
            + '</div>';
    }

