    function renderModernNotes(modernNotes, langKey) {
        if (!modernNotes || !langKey) {
            return '';
        }
        var resolvedKey = langKey;
        if (!modernNotes[resolvedKey] && (langKey === 'scala2' || langKey === 'scala3')) {
            resolvedKey = 'scala';
        }
        if (!modernNotes[resolvedKey]) {
            return '';
        }
        var note = modernNotes[resolvedKey];

        function fmtText(text) {
            return escapeHtml(text || '').replace(/`([^`]+)`/g, '<code style="display:inline;white-space:normal;background:#0f1720;color:#dbeafe;padding:2px 6px;border-radius:3px;font-family:\'Consolas\',monospace;font-size:0.85em;">$1</code>');
        }

        return '<div class="doc-table-wrap" style="margin-top:8px">'
            + '<table class="doc-table"><thead><tr>'
            + '<th>Classic approach</th><th>Modern approach</th>'
            + '</tr></thead><tbody><tr>'
            + '<td>' + fmtText(note.classic) + '</td>'
            + '<td>' + fmtText(note.modern) + '</td>'
            + '</tr></tbody></table></div>';
    }

    function renderAdapterInsight(insight) {
        if (!insight) {
            return '';
        }

        function fmtText(text) {
            return escapeHtml(text || '').replace(/`([^`]+)`/g, '<code style="display:inline;white-space:normal;background:#0f1720;color:#dbeafe;padding:2px 6px;border-radius:3px;font-family:\'Consolas\',monospace;font-size:0.85em;">$1</code>');
        }

        if (typeof insight === 'object' && insight.rows && insight.rows.length) {
            var headers = insight.headers || [];
            var headerHtml = headers.length
                ? '<thead><tr>' + headers.map(function (h) { return '<th>' + fmtText(h) + '</th>'; }).join('') + '</tr></thead>'
                : '';
            var rowsHtml = '<tbody>' + insight.rows.map(function (row) {
                return '<tr>' + (row || []).map(function (cell) {
                    return '<td>' + fmtText(cell) + '</td>';
                }).join('') + '</tr>';
            }).join('') + '</tbody>';
            var title = insight.title ? '<strong style="color:#ff8c00">' + fmtText(insight.title) + '</strong>' : '<strong style="color:#ff8c00">Adapter Insight:</strong>';

            return '<div class="adapter-insight" style="margin-top:12px">'
                + '<div style="margin-bottom:6px">' + title + '</div>'
                + '<div class="doc-table-wrap"><table class="doc-table">'
                + headerHtml
                + rowsHtml
                + '</table></div>'
                + '</div>';
        }

        return '<div class="adapter-insight" style="margin-top:12px;padding:8px;border-left:3px solid #ffa500;background:rgba(255,165,0,0.05)">'
            + '<strong style="color:#ff8c00">Adapter Insight:</strong> '
            + fmtText(insight)
            + '</div>';
    }

    function updateEntryMeta(title, description, sourceLinks, modernNotes, adapterInsight, compareEntries, langKey) {
        var meta = document.getElementById('entryMeta');
        var titleEl = document.getElementById('entryTitle');
        var descEl = document.getElementById('entryDesc');
        var sourceEl = document.getElementById('entrySourceLinks');
        var modernEl = document.getElementById('entryModernNotes');
        var adapterEl = document.getElementById('entryAdapterInsight');
        var compareEl = document.getElementById('entryCompareLinks');

        if (!title && !description && (!sourceLinks || sourceLinks.length === 0)) {
            meta.classList.add('hidden');
            titleEl.textContent = '';
            descEl.textContent = '';
            sourceEl.innerHTML = '';
            if (modernEl) { modernEl.innerHTML = ''; }
            if (adapterEl) { adapterEl.innerHTML = ''; }
            if (compareEl) { compareEl.innerHTML = ''; }
            return;
        }

        meta.classList.remove('hidden');
        titleEl.textContent = title || '';
        descEl.textContent = description || '';
        sourceEl.innerHTML = renderSourceLinks(sourceLinks);
        if (modernEl) { modernEl.innerHTML = renderModernNotes(modernNotes, langKey); }
        if (adapterEl) { adapterEl.innerHTML = renderAdapterInsight(adapterInsight); }
        if (compareEl) { compareEl.innerHTML = renderCompareEntries(compareEntries); }
    }

