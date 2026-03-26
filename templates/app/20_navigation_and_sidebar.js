    function handleLanguageClick(langKey, targetSlot) {
        appStore.applyLanguageSelection(langKey, targetSlot);
        renderAll();
    }

    function suppressNextLanguageClick(langKey) {
        suppressedLangClick = {
            langKey: langKey,
            expiresAt: Date.now() + 700
        };
    }

    function shouldIgnoreSuppressedLanguageClick(langKey) {
        if (!suppressedLangClick) {
            return false;
        }

        var shouldIgnore = suppressedLangClick.langKey === langKey && Date.now() <= suppressedLangClick.expiresAt;
        suppressedLangClick = null;
        return shouldIgnore;
    }

    function clearLanguageDragPreview() {
        var chips = document.querySelectorAll('#langNav .lang-chip');
        chips.forEach(function (chip) {
            chip.classList.remove('dragging', 'drag-preview-left', 'drag-preview-right');
            chip.style.transform = '';
        });
    }

    function resetLanguageDragState() {
        clearLanguageDragPreview();
        langDragState = null;
    }

    function setLanguageDragPreview(button, slot, deltaX) {
        if (!button) {
            return;
        }

        clearLanguageDragPreview();
        button.classList.add('dragging');
        button.classList.add(slot === 1 ? 'drag-preview-right' : 'drag-preview-left');

        var clampedShift = Math.max(-LANG_DRAG_MAX_SHIFT, Math.min(LANG_DRAG_MAX_SHIFT, deltaX * 0.18));
        button.style.transform = 'translateX(' + clampedShift + 'px)';
    }

    function beginLanguageDrag(event, langKey) {
        if (appStore.getCompareCount() !== 2 || !event.currentTarget) {
            return;
        }

        if (event.pointerType === 'mouse' && event.button !== 0) {
            return;
        }

        langDragState = {
            pointerId: event.pointerId,
            pointerType: event.pointerType,
            langKey: langKey,
            button: event.currentTarget,
            startX: event.clientX,
            startY: event.clientY,
            previewSlot: null,
            dragging: false
        };

        if (typeof event.currentTarget.setPointerCapture === 'function') {
            try {
                event.currentTarget.setPointerCapture(event.pointerId);
            } catch (err) {
                // ignore capture failures
            }
        }
    }

    function updateLanguageDrag(event) {
        if (!langDragState || event.pointerId !== langDragState.pointerId) {
            return;
        }

        var deltaX = event.clientX - langDragState.startX;
        var deltaY = event.clientY - langDragState.startY;
        var absX = Math.abs(deltaX);
        var absY = Math.abs(deltaY);

        if (absX < LANG_DRAG_THRESHOLD || absX <= absY) {
            clearLanguageDragPreview();
            return;
        }

        langDragState.dragging = true;
        langDragState.previewSlot = deltaX > 0 ? 1 : 0;
        setLanguageDragPreview(langDragState.button, langDragState.previewSlot, deltaX);
        event.preventDefault();
    }

    function endLanguageDrag(event, cancelled) {
        if (!langDragState || event.pointerId !== langDragState.pointerId) {
            return;
        }

        var drag = langDragState;

        if (drag.button && typeof drag.button.releasePointerCapture === 'function') {
            try {
                drag.button.releasePointerCapture(event.pointerId);
            } catch (err) {
                // ignore capture failures
            }
        }

        if (!cancelled && drag.dragging && (drag.previewSlot === 0 || drag.previewSlot === 1)) {
            suppressNextLanguageClick(drag.langKey);
            handleLanguageClick(drag.langKey, drag.previewSlot);
            resetLanguageDragState();
            return;
        }

        if (!cancelled && drag.pointerType !== 'mouse') {
            var totalX = Math.abs(event.clientX - drag.startX);
            var totalY = Math.abs(event.clientY - drag.startY);
            if (totalX < 8 && totalY < 8) {
                suppressNextLanguageClick(drag.langKey);
                handleLanguageClick(drag.langKey, 0);
                resetLanguageDragState();
                return;
            }
        }

        resetLanguageDragState();
    }

    function renderLanguageButtons() {
        var nav = document.getElementById('langNav');
        nav.innerHTML = '';

        for (var i = 0; i < LANG_ORDER.length; i += 1) {
            var langKey = LANG_ORDER[i];
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'chip-btn lang-chip';
            btn.textContent = LANG_LABELS[langKey] || langKey;
            btn.setAttribute('data-lang-key', langKey);

            if (selectPrimaryLang() === langKey) {
                btn.classList.add('active');
            } else if (appStore.getCompareCount() === 2 && appStore.getSelectedLang(1) === langKey) {
                btn.classList.add('active-2');
            }

            if (appStore.getCompareCount() === 2) {
                btn.title = 'Tap selects left panel. Drag left or right to choose a side. Right click still selects right panel.';
            }

            (function (capturedKey) {
                btn.addEventListener('click', function (event) {
                    if (shouldIgnoreSuppressedLanguageClick(capturedKey)) {
                        event.preventDefault();
                        return;
                    }
                    handleLanguageClick(capturedKey, 0);
                });

                btn.addEventListener('contextmenu', function (event) {
                    if (appStore.getCompareCount() !== 2) {
                        return;
                    }
                    event.preventDefault();
                    handleLanguageClick(capturedKey, 1);
                });

                btn.addEventListener('pointerdown', function (event) {
                    beginLanguageDrag(event, capturedKey);
                });

                btn.addEventListener('pointermove', function (event) {
                    updateLanguageDrag(event);
                });

                btn.addEventListener('pointerup', function (event) {
                    endLanguageDrag(event, false);
                });

                btn.addEventListener('pointercancel', function (event) {
                    endLanguageDrag(event, true);
                });
            }(langKey));

            nav.appendChild(btn);
        }
    }

    function renderViewButtons() {
        var nav = document.getElementById('viewNav');
        nav.innerHTML = '';

        var currentCategory = VIEW_CATEGORIES[selectCurrentViewCategory()];
        var visibleViews = (currentCategory && currentCategory.views ? currentCategory.views : []).filter(function (viewKey) {
            return !!VIEW_CONFIG[viewKey];
        });

        visibleViews.forEach(function (viewKey) {
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'chip-btn';
            btn.textContent = appStore.getViewConfig(viewKey).label;

            if (selectCurrentView() === viewKey) {
                btn.classList.add('active');
            }

            btn.addEventListener('click', function () {
                appStore.toggleView(viewKey);
                renderAll();
            });

            nav.appendChild(btn);
        });
    }

    function renderViewCategorySelector() {
        var nav = document.getElementById('viewNav');
        var rowTitle = nav.previousElementSibling;
        if (!rowTitle || !rowTitle.classList.contains('row-title')) {
            return;
        }

        var currentCat = VIEW_CATEGORIES[selectCurrentViewCategory()];
        rowTitle.textContent = (currentCat && currentCat.label ? currentCat.label : 'Atlas Views').toUpperCase();
        rowTitle.classList.add('view-category-toggle-title');
        rowTitle.setAttribute('role', 'button');
        rowTitle.setAttribute('tabindex', '0');
        rowTitle.setAttribute('aria-label', 'Toggle view category');

        function toggleViewCategory() {
            appStore.setViewCategory(appStore.getViewCategory() === 'atlas' ? 'learning' : 'atlas');
            localStorage.setItem(VIEW_CATEGORY_STORAGE_KEY, appStore.getViewCategory());
            appStore.setView('');
            renderAll();
        }

        rowTitle.onclick = toggleViewCategory;
        rowTitle.onkeydown = function (event) {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                toggleViewCategory();
            }
        };
    }

    function renderCompareButtons() {
        var toggle = document.getElementById('compareToggle');
        var swap = document.getElementById('swapBtn');
        var course = document.getElementById('courseBtn');
        if (selectCurrentView() === 'principles') {
            toggle.classList.add('hidden');
            swap.classList.add('hidden');
            if (course) {
                course.classList.remove('active');
            }
            return;
        }

        toggle.classList.remove('hidden');
    var isCompare = appStore.getCompareCount() === 2;

        toggle.classList.toggle('active', isCompare);
        toggle.setAttribute('aria-pressed', isCompare ? 'true' : 'false');
        swap.classList.toggle('hidden', !isCompare);

        if (course) {
            course.classList.toggle('active', appStore.isCourseModeEnabled());
            course.setAttribute('aria-pressed', appStore.isCourseModeEnabled() ? 'true' : 'false');
            course.title = appStore.isCourseModeEnabled() ? 'Exit course mode' : 'Start 7-level adaptation course';
        }
    }

    function rememberPreCourseView() {
        appStore.setCourseReturnState(appStore.getSelectionSnapshot());
    }

    function restorePreCourseView() {
        var snapshot = appStore.consumeCourseReturnState();
        if (!snapshot) {
            renderAll();
            return;
        }
        appStore.restoreSelectionSnapshot(snapshot);
        renderAll();
    }

    function exitCourseToLearningBasics() {
        appStore.setCourseMode(false);
        appStore.setCourseLevel(0);
        appStore.setCourseReturnState(null);
        appStore.setViewCategory('learning');
        appStore.setView('basics');
        renderAll();
    }

    function renderPaletteSelector() {
        var previewButtons = document.querySelectorAll('.palette-preview-btn');
        previewButtons.forEach(function (btn) {
            var isActive = btn.getAttribute('data-palette') === appStore.getPalette();
            btn.classList.toggle('active', isActive);
            btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        });
    }

    function exerciseLabelParts(label) {
        var raw = String(label || '');
        var m = raw.match(/^(Beginner|Intermediate|Advanced)\s*:\s*(.+)$/i);
        if (!m) {
            return { level: '', title: raw || '' };
        }

        var levelRaw = (m[1] || '').toLowerCase();
        var title = m[2] || raw;
        return {
            level: levelRaw,
            title: title,
            levelLabel: levelRaw.charAt(0).toUpperCase() + levelRaw.slice(1)
        };
    }

    function setEntryTitleLevel(level) {
        var titleEl = document.getElementById('entryTitle');
        if (!titleEl) {
            return;
        }

        titleEl.classList.remove('entry-level-beginner', 'entry-level-intermediate', 'entry-level-advanced');
        if (level === 'beginner' || level === 'intermediate' || level === 'advanced') {
            titleEl.classList.add('entry-level-' + level);
        }
    }

    function appendSidebarItem(list, key, entry, activeKey) {
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'sidebar-item' + (key === activeKey ? ' active' : '');

        if (selectCurrentView() === 'exercises') {
            var parts = exerciseLabelParts(entry.label || key);
            btn.textContent = parts.title || key;
        } else {
            btn.textContent = entry.label || key;
        }

        btn.setAttribute('data-entry-key', key);
        list.appendChild(btn);
    }

    function renderSidebar() {
        var sidebar = document.getElementById('catalogSidebar');
        var expandBtn = document.getElementById('sidebarExpandBtn');
        var sidebarTitle = document.getElementById('sidebarTitle');
        var list = document.getElementById('sidebarList');
        var sidebarHeader = document.getElementById('topicSidebarHeader');

        var activeView = selectCurrentView();
        var needsSidebar = activeView && activeView !== 'sheets';
        if (!needsSidebar) {
            sidebar.classList.add('hidden');
            expandBtn.classList.add('hidden');
            return;
        }

        var catalog = currentCatalog();
        if (!catalog) {
            sidebar.classList.add('hidden');
            expandBtn.classList.add('hidden');
            return;
        }

        if (appStore.isCourseModeEnabled()) {
            if (appStore.isCourseLevelCollapsed()) {
                sidebar.classList.add('hidden');
                expandBtn.classList.remove('hidden');
                expandBtn.title = 'Expand course levels';
                expandBtn.setAttribute('aria-label', 'Expand course levels');
            } else {
                sidebar.classList.remove('hidden');
                expandBtn.classList.add('hidden');
            }
            if (sidebarHeader) {
                sidebarHeader.classList.add('hidden');
            }
            if (list) {
                list.classList.add('hidden');
                list.innerHTML = '';
            }
            return;
        }

        if (sidebarHeader) {
            sidebarHeader.classList.remove('hidden');
        }
        if (list) {
            list.classList.remove('hidden');
        }

        var entries = catalog.entries || {};
        var groups = catalog.groups || [];
        var activeKey = selectedItemKey();

        // Ensure the selected key is valid; fall back to first available entry
        if (!entries[activeKey]) {
            var fallbackKey = '';
            for (var gi = 0; gi < groups.length; gi++) {
                for (var ki = 0; ki < groups[gi].keys.length; ki++) {
                    if (entries[groups[gi].keys[ki]]) {
                        fallbackKey = groups[gi].keys[ki];
                        break;
                    }
                }
                if (fallbackKey) { break; }
            }
            if (!fallbackKey) {
                var allKeys = Object.keys(entries);
                fallbackKey = allKeys.length > 0 ? allKeys[0] : '';
            }
            if (fallbackKey) {
                setSelectedItemKey(fallbackKey);
                activeKey = fallbackKey;
            }
        }

        if (sidebarTitle) {
            sidebarTitle.textContent = catalog.itemLabel || 'Items';
        }

        if (appStore.isSidebarCollapsed()) {
            sidebar.classList.add('hidden');
            expandBtn.classList.remove('hidden');
        } else {
            sidebar.classList.remove('hidden');
            expandBtn.classList.add('hidden');
        }

        // Build list
        list.innerHTML = '';
        if (groups.length > 0) {
            var seen = {};
            groups.forEach(function (group) {
                var validKeys = group.keys.filter(function (k) { return !!entries[k]; });
                if (validKeys.length === 0) { return; }

                var groupHeader = document.createElement('div');
                groupHeader.className = 'sidebar-group-label';
                groupHeader.textContent = group.label;
                if (selectCurrentView() === 'exercises') {
                    var levelKey = String(group.label || '').toLowerCase();
                    if (levelKey === 'beginner' || levelKey === 'intermediate' || levelKey === 'advanced') {
                        groupHeader.classList.add('exercise-level', 'level-' + levelKey);
                    }
                }
                list.appendChild(groupHeader);

                validKeys.forEach(function (key) {
                    seen[key] = true;
                    appendSidebarItem(list, key, entries[key], activeKey);
                });
            });

            Object.keys(entries).forEach(function (key) {
                if (!seen[key]) {
                    appendSidebarItem(list, key, entries[key], activeKey);
                }
            });
        } else {
            Object.keys(entries).forEach(function (key) {
                appendSidebarItem(list, key, entries[key], activeKey);
            });
        }

        // Scroll active item into view
        setTimeout(function () {
            var active = list.querySelector('.sidebar-item.active');
            if (active) { active.scrollIntoView({ block: 'nearest' }); }
        }, 0);
    }

