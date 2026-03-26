    function normalizePaletteKey(paletteName) {
        if (PALETTE_OPTIONS[paletteName]) {
            return paletteName;
        }
        return 'brand';
    }

    function escapeHtml(text) {
        return String(text || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function renderSourceLinks(sourceLinks) {
        if (!sourceLinks || sourceLinks.length === 0) {
            return '';
        }

        return '<div class="entry-source-links">' + sourceLinks.map(function (link) {
            if (!link || !link.url) {
                return '';
            }
            var label = link.label || 'Source';
            return '<a class="entry-source-link" href="' + escapeHtml(link.url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(label) + '</a>';
        }).join('') + '</div>';
    }

    function findEntryReference(entryKey) {
        var catalogs = Object.keys(VIEW_REGISTRY).map(function (viewKey) {
            return {
                view: viewKey,
                cfg: appStore.getViewConfig(viewKey)
            };
        });

        for (var i = 0; i < catalogs.length; i += 1) {
            var item = catalogs[i];
            if (item.cfg && item.cfg.entries && item.cfg.entries[entryKey]) {
                return {
                    view: item.view,
                    entry: item.cfg.entries[entryKey]
                };
            }
        }

        return null;
    }

    function renderCompareEntries(compareEntries) {
        if (!compareEntries || compareEntries.length === 0) {
            return '';
        }

        var html = '<div class="entry-compare-links"><strong>Compare with:</strong> ';
        html += compareEntries.map(function (entryKey) {
            var ref = findEntryReference(entryKey);
            if (!ref || !ref.entry) {
                return '';
            }
            var entry = ref.entry;
            var label = entry.label || entryKey;
            return '<a class="entry-compare-link" href="#" data-compare-view="' + escapeHtml(ref.view) + '" data-compare-key="' + escapeHtml(entryKey) + '">' + escapeHtml(label) + '</a>';
        }).join(' | ');
        html += '</div>';
        return html;
    }

    function chooseNextLang(excluded) {
        for (var i = 0; i < LANG_ORDER.length; i += 1) {
            if (LANG_ORDER[i] !== excluded) {
                return LANG_ORDER[i];
            }
        }
        return excluded || '';
    }

    function normalizeSelectedLangs() {
        appStore.normalizeSelectedLangs();
    }

    function isViewInCurrentCategory(viewKey) {
        var category = VIEW_CATEGORIES[appStore.getViewCategory()];
        if (!category) {
            return true;
        }
        return category.views.indexOf(viewKey) !== -1;
    }

    function currentCatalog() {
        return appStore.getCurrentCatalog();
    }

    function selectedItemKey() {
        return appStore.getSelectedItemKey();
    }

    function setSelectedItemKey(key) {
        appStore.setSelectedItemKey(key);
    }

    function currentEntry() {
        return appStore.getCurrentEntry();
    }

