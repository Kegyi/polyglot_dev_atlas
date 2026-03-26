    function updateStickyOffset() {
        var topStack = document.getElementById('topStack');
        var offset = topStack ? (topStack.offsetHeight + 8) : 0;
        document.documentElement.style.setProperty('--sticky-offset', String(offset) + 'px');
    }

    function renderOfflineWarning() {
        var warning = document.getElementById('runtimeWarning');
        if (!warning) {
            return;
        }

        if (window.__hljsMissingFallback) {
            warning.textContent = 'We are offline and do not have access to fallback folder "assets/hljs" that needs to be next to this HTML file.';
            warning.classList.remove('hidden');
            return;
        }

        warning.classList.add('hidden');
        warning.textContent = '';
    }

    function renderAll() {
        normalizeSelectedLangs();
        renderLanguageButtons();
        renderViewCategorySelector();
        renderViewButtons();
        renderCompareButtons();
        renderPaletteSelector();
        renderOfflineWarning();
        // In course mode, hide only the Views controls and keep style/compare/course visible.
        var viewsSelection = document.getElementById('viewsSelection');
        if (viewsSelection) {
            viewsSelection.classList.toggle('hidden', appStore.isCourseModeEnabled());
        }
        renderCourseLevelPanel();
        renderCourseNavHeader();
        renderSidebar();

        if (selectCurrentView() === 'sheets') {
            updateEntryMeta('Language Reference Sheet', '', [], null, null, null, selectPrimaryLang());
        } else if (!selectCurrentView()) {
            updateEntryMeta('', '', [], null, null, null, selectPrimaryLang());
        }

        appRouter.renderActiveView();

        applySyntaxHighlight();
        updateStickyOffset();
    }

    document.getElementById('compareToggle').addEventListener('click', function () {
        appStore.toggleCompareCount();
        renderAll();
    });

    document.getElementById('contentHost').addEventListener('click', function (event) {
        var btn = event.target.closest('.side-pick-btn');
        if (!btn || !selectIsCompareMode()) {
            return;
        }
        var side = Number(btn.dataset.side);
        if (side !== 0 && side !== 1) {
            return;
        }
        appStore.setActiveSlot(side);
        renderAll();
    });

    document.getElementById('contentHost').addEventListener('click', function (event) {
        var toggle = event.target.closest('.exercise-solution-toggle');
        if (!toggle) {
            return;
        }

        var panelBody = toggle.closest('.exercise-panel-body');
        if (!panelBody) {
            return;
        }

        var solution = panelBody.querySelector('.exercise-solution');
        if (!solution) {
            return;
        }

        var willOpen = solution.classList.contains('hidden');
        solution.classList.toggle('hidden', !willOpen);
        toggle.textContent = willOpen ? 'Hide Solution' : 'Show Solution';
        toggle.setAttribute('aria-expanded', willOpen ? 'true' : 'false');

        if (willOpen) {
            applySyntaxHighlight();
        }
    });

    document.getElementById('contentHost').addEventListener('click', function (event) {
        var toggle = event.target.closest('.course-topic-toggle');
        if (!toggle || !selectIsCourseMode()) {
            return;
        }
        var topicKey = toggle.getAttribute('data-topic-key');
        var topicIndex = Number(toggle.getAttribute('data-topic-index'));
        if (!topicKey) {
            return;
        }
        var collapseKey = courseTopicCollapseKey(topicKey);
        var collapsed = isCourseTopicCollapsed(topicKey, isNaN(topicIndex) ? 0 : topicIndex);
        appStore.setCourseTopicCollapsed(collapseKey, !collapsed);
        renderAll();
    });

    document.getElementById('swapBtn').addEventListener('click', function () {
        appStore.swapSelectedLangs();
        renderAll();
    });

    document.getElementById('courseBtn').addEventListener('click', function () {
        if (selectIsCourseMode()) {
            // Toggle OFF: exit course mode
            appStore.setCourseMode(false);
            appStore.setCourseLevel(0);
            restorePreCourseView();
            return;
        }
        // Toggle ON: enter course mode at level 1
        rememberPreCourseView();
        appStore.setCourseMode(true);
        appStore.setCourseLevel(0);
        appStore.setViewCategory('atlas');
        navigateCourse(0);
    });

    document.getElementById('coursePrevBtn').addEventListener('click', function () {
        if (selectIsCourseMode() && selectCourseLevel() > 0) {
            navigateCourse(selectCourseLevel() - 1);
        }
    });

    document.getElementById('courseNextBtn').addEventListener('click', function () {
        if (selectIsCourseMode() && selectCourseLevel() < ADAPTATION_COURSE.length - 1) {
            navigateCourse(selectCourseLevel() + 1);
        }
    });

    document.getElementById('courseExitBtn').addEventListener('click', function () {
        exitCourseToLearningBasics();
    });

    document.getElementById('courseLevelToggleBtn').addEventListener('click', function () {
        appStore.setCourseLevelCollapsed(true);
        renderSidebar();
    });

    function navigateCourse(levelIndex) {
        if (!ADAPTATION_COURSE || levelIndex < 0 || levelIndex >= ADAPTATION_COURSE.length) {
            return;
        }
        appStore.setCourseLevel(levelIndex);
        var level = ADAPTATION_COURSE[levelIndex];
        var viewItem = level.viewItems && level.viewItems[0] ? level.viewItems[0] : 'project_lifecycle';
        appStore.setSelectedItemKey(viewItem, 'basics');
        appStore.setView('basics');
        appStore.setViewCategory('atlas');
        renderAll();
    }

    window.nextCourseLevel = function () {
        if (selectIsCourseMode() && selectCourseLevel() < ADAPTATION_COURSE.length - 1) {
            navigateCourse(selectCourseLevel() + 1);
        }
    };

    window.prevCourseLevel = function () {
        if (selectIsCourseMode() && selectCourseLevel() > 0) {
            navigateCourse(selectCourseLevel() - 1);
        }
    };

    function renderCourseLevelPanel() {
        var panel = document.getElementById('courseLevelPanel');
        if (!panel) { return; }

        if (!selectIsCourseMode() || !ADAPTATION_COURSE || ADAPTATION_COURSE.length === 0) {
            panel.classList.add('hidden');
            return;
        }
        panel.classList.remove('hidden');

        var list = document.getElementById('courseLevelList');
        if (!list) { return; }
        var toggleBtn = document.getElementById('courseLevelToggleBtn');

        if (toggleBtn) {
            toggleBtn.innerHTML = '\u00AB';
            toggleBtn.title = 'Collapse course levels';
            toggleBtn.setAttribute('aria-label', 'Collapse course levels');
        }

        list.classList.remove('hidden');
        list.innerHTML = '';

        ADAPTATION_COURSE.forEach(function (lvl, idx) {
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'sidebar-item course-level-item' + (idx === selectCourseLevel() ? ' active' : '');
            btn.textContent = 'L' + lvl.level + ': ' + lvl.title;
            (function (capturedIdx) {
                btn.addEventListener('click', function () {
                    navigateCourse(capturedIdx);
                });
            }(idx));
            list.appendChild(btn);
        });
    }

    function renderCourseNavHeader() {
        var header = document.getElementById('courseNavHeader');
        if (!header) { return; }

        if (!selectIsCourseMode() || !ADAPTATION_COURSE || ADAPTATION_COURSE.length === 0) {
            header.classList.add('hidden');
            return;
        }
        header.classList.remove('hidden');

        var lvl = ADAPTATION_COURSE[selectCourseLevel()] || ADAPTATION_COURSE[0];
        var titleEl = document.getElementById('courseNavTitle');
        var descEl = document.getElementById('courseNavDesc');
        var prevBtn = document.getElementById('coursePrevBtn');
        var nextBtn = document.getElementById('courseNextBtn');

        if (titleEl) { titleEl.textContent = 'L' + lvl.level + ': ' + lvl.title; }
        if (descEl) { descEl.textContent = lvl.description || ''; }
        if (prevBtn) { prevBtn.disabled = selectCourseLevel() <= 0; }
        if (nextBtn) { nextBtn.disabled = selectCourseLevel() >= ADAPTATION_COURSE.length - 1; }
    }

    document.getElementById('themeToggle').addEventListener('click', function () {
        applyTheme(appStore.getTheme() === 'dark' ? 'light' : 'dark');
    });

    document.getElementById('palettePreviews').addEventListener('click', function (event) {
        var btn = event.target.closest('.palette-preview-btn');
        if (!btn) {
            return;
        }
        var paletteName = btn.getAttribute('data-palette');
        applyPalette(paletteName);
        renderAll();
    });

    document.getElementById('sidebarList').addEventListener('click', function (event) {
        var btn = event.target.closest('.sidebar-item');
        if (!btn) { return; }
        var key = btn.getAttribute('data-entry-key');
        if (key) {
            setSelectedItemKey(key);
            renderAll();
        }
    });

    document.getElementById('sidebarToggleBtn').addEventListener('click', function () {
        appStore.setSidebarCollapsed(true);
        try { window.localStorage.setItem(SIDEBAR_STORAGE_KEY, '1'); } catch (e) {}
        renderSidebar();
    });

    document.getElementById('sidebarExpandBtn').addEventListener('click', function () {
        if (appStore.isCourseModeEnabled()) {
            appStore.setCourseLevelCollapsed(false);
            renderSidebar();
            return;
        }
        appStore.setSidebarCollapsed(false);
        try { window.localStorage.setItem(SIDEBAR_STORAGE_KEY, '0'); } catch (e) {}
        renderSidebar();
    });

    document.getElementById('entryMeta').addEventListener('click', function (event) {
        var link = event.target.closest('.entry-compare-link');
        if (!link) {
            return;
        }
        event.preventDefault();
        var compareView = link.getAttribute('data-compare-view');
        var compareKey = link.getAttribute('data-compare-key');
        if (compareKey) {
            if (compareView && appStore.getViewConfig(compareView)) {
                appStore.setView(compareView);
            }
            setSelectedItemKey(compareKey);
            renderAll();
        }
    });

    window.addEventListener('hljs-ready', applySyntaxHighlight);
    window.addEventListener('resize', updateStickyOffset);

    var savedTheme = 'dark';
    try {
        savedTheme = window.localStorage.getItem(THEME_STORAGE_KEY) || 'dark';
    } catch (err) {
        savedTheme = 'dark';
    }

    var savedPalette = 'brand';
    try {
        savedPalette = window.localStorage.getItem(PALETTE_STORAGE_KEY) || 'brand';
    } catch (err) {
        savedPalette = 'brand';
    }

    var savedViewCategory = 'atlas';
    try {
        savedViewCategory = window.localStorage.getItem(VIEW_CATEGORY_STORAGE_KEY) || 'atlas';
    } catch (err) {
        savedViewCategory = 'atlas';
    }

    var savedSidebarCollapsed = '0';
    try {
        savedSidebarCollapsed = window.localStorage.getItem(SIDEBAR_STORAGE_KEY) || '0';
    } catch (err) {
        savedSidebarCollapsed = '0';
    }

    applyTheme(savedTheme);
    applyPalette(savedPalette);
    appStore.setViewCategory(savedViewCategory);
    appStore.setSidebarCollapsed(savedSidebarCollapsed === '1');

    renderAll();
}());
