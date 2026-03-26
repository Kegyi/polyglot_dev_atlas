    var VIEW_SELECTION_KEYS = {
        problems: 'selectedProblem',
        interview: 'selectedInterview',
        patterns: 'selectedPattern',
        basics: 'selectedBasic',
        course: 'selectedCourse',
        exercises: 'selectedExercise',
        workflow: 'selectedWorkflow',
        principles: 'selectedPrinciple'
    };

    var VIEW_REGISTRY = {
        problems: VIEW_CONFIG.problems,
        interview: VIEW_CONFIG.interview,
        patterns: VIEW_CONFIG.patterns,
        basics: VIEW_CONFIG.basics,
        course: VIEW_CONFIG.course,
        exercises: VIEW_CONFIG.exercises,
        workflow: VIEW_CONFIG.workflow,
        principles: VIEW_CONFIG.principles
    };

    var appStore = {
        // ========================================
        // === QUERY METHODS (Read-Only Access) ===
        // ========================================

        getState: function () {
            return state;
        },

        getSelectedLang: function (slot) {
            var resolvedSlot = slot === 1 ? 1 : 0;
            return state.selectedLangs[resolvedSlot] || '';
        },

        getCompareCount: function () {
            return state.compareCount;
        },

        getActiveSlot: function () {
            return state.activeSlot;
        },

        isCourseModeEnabled: function () {
            return !!state.courseMode;
        },

        getCourseLevel: function () {
            return state.courseLevel;
        },

        isCourseLevelCollapsed: function () {
            return !!state.courseLevelCollapsed;
        },

        getTheme: function () {
            return state.theme;
        },

        getPalette: function () {
            return state.palette;
        },

        getViewConfig: function (viewKey) {
            return VIEW_REGISTRY[viewKey] || null;
        },

        getView: function () {
            return state.view;
        },

        getViewCategory: function () {
            return state.viewCategory;
        },

        getCurrentCatalog: function () {
            return this.getViewConfig(this.getView());
        },

        getSelectedItemKey: function (viewKey) {
            var resolvedView = typeof viewKey === 'string' ? viewKey : state.view;
            var stateKey = VIEW_SELECTION_KEYS[resolvedView];
            return stateKey ? state[stateKey] : '';
        },

        isSidebarCollapsed: function () {
            return !!state.sidebarCollapsed;
        },

        hasCourseTopicCollapseState: function (collapseKey) {
            return Object.prototype.hasOwnProperty.call(state.courseTopicCollapsed, collapseKey);
        },

        isCourseTopicCollapsed: function (collapseKey) {
            return !!state.courseTopicCollapsed[collapseKey];
        },

        getSelectionSnapshot: function () {
            return {
                view: state.view,
                viewCategory: state.viewCategory,
                selectedProblem: state.selectedProblem,
                selectedInterview: state.selectedInterview,
                selectedPattern: state.selectedPattern,
                selectedBasic: state.selectedBasic,
                selectedPrinciple: state.selectedPrinciple,
                selectedCourse: state.selectedCourse,
                selectedExercise: state.selectedExercise,
                selectedWorkflow: state.selectedWorkflow
            };
        },

        getCurrentEntry: function () {
            var catalog = this.getCurrentCatalog();
            if (!catalog) {
                return null;
            }
            var key = this.getSelectedItemKey();
            return catalog.entries[key] || null;
        },

        // ============================================
        // === MUTATION METHODS (State Modification) ===
        // ============================================

        setSelectedItemKey: function (key, viewKey) {
            var resolvedView = typeof viewKey === 'string' ? viewKey : state.view;
            var stateKey = VIEW_SELECTION_KEYS[resolvedView];
            if (stateKey) {
                state[stateKey] = key;
            }
        },

        setSelectedLang: function (slot, langKey) {
            var resolvedSlot = slot === 1 ? 1 : 0;
            state.selectedLangs[resolvedSlot] = langKey;
            return state.selectedLangs[resolvedSlot];
        },

        normalizeSelectedLangs: function () {
            if (LANG_ORDER.length === 0) {
                state.selectedLangs = ['', ''];
                return;
            }

            if (LANG_ORDER.indexOf(state.selectedLangs[0]) === -1) {
                state.selectedLangs[0] = LANG_ORDER[0];
            }

            if (LANG_ORDER.indexOf(state.selectedLangs[1]) === -1) {
                state.selectedLangs[1] = chooseNextLang(state.selectedLangs[0]);
            }

            if (state.compareCount === 2 && state.selectedLangs[0] === state.selectedLangs[1]) {
                state.selectedLangs[1] = chooseNextLang(state.selectedLangs[0]);
            }
        },

        setCompareCount: function (compareCount) {
            state.compareCount = compareCount === 2 ? 2 : 1;
            return state.compareCount;
        },

        toggleCompareCount: function () {
            state.compareCount = state.compareCount === 2 ? 1 : 2;
            if (state.activeSlot !== 0 && state.activeSlot !== 1) {
                state.activeSlot = 0;
            }
            return state.compareCount;
        },

        setActiveSlot: function (slot) {
            state.activeSlot = slot === 1 ? 1 : 0;
            return state.activeSlot;
        },

        swapSelectedLangs: function () {
            var tmp = state.selectedLangs[0];
            state.selectedLangs[0] = state.selectedLangs[1];
            state.selectedLangs[1] = tmp;
        },

        applyLanguageSelection: function (langKey, targetSlot) {
            if (state.compareCount === 1) {
                this.setSelectedLang(0, langKey);
                return;
            }

            var slot = targetSlot === 1 ? 1 : 0;
            var other = slot === 0 ? 1 : 0;

            if (state.selectedLangs[slot] === langKey) {
                this.setActiveSlot(slot);
                return;
            }

            if (state.selectedLangs[other] === langKey) {
                var tmp = state.selectedLangs[slot];
                state.selectedLangs[slot] = langKey;
                state.selectedLangs[other] = tmp;
            } else {
                state.selectedLangs[slot] = langKey;
                if (state.selectedLangs[slot] === state.selectedLangs[other]) {
                    state.selectedLangs[other] = chooseNextLang(state.selectedLangs[slot]);
                }
            }

            this.setActiveSlot(slot);
        },

        setCourseMode: function (enabled) {
            state.courseMode = !!enabled;
            return state.courseMode;
        },

        setCourseLevel: function (levelIndex) {
            state.courseLevel = levelIndex;
            return state.courseLevel;
        },

        setCourseLevelCollapsed: function (collapsed) {
            state.courseLevelCollapsed = !!collapsed;
            return state.courseLevelCollapsed;
        },

        setSidebarCollapsed: function (collapsed) {
            state.sidebarCollapsed = !!collapsed;
            return state.sidebarCollapsed;
        },

        setCourseTopicCollapsed: function (collapseKey, collapsed) {
            state.courseTopicCollapsed[collapseKey] = !!collapsed;
            return state.courseTopicCollapsed[collapseKey];
        },

        restoreSelectionSnapshot: function (snapshot) {
            if (!snapshot) {
                return;
            }
            this.setView(snapshot.view);
            this.setViewCategory(snapshot.viewCategory);
            state.selectedProblem = snapshot.selectedProblem;
            state.selectedInterview = snapshot.selectedInterview;
            state.selectedPattern = snapshot.selectedPattern;
            state.selectedBasic = snapshot.selectedBasic;
            state.selectedPrinciple = snapshot.selectedPrinciple;
            state.selectedCourse = snapshot.selectedCourse;
            state.selectedExercise = snapshot.selectedExercise;
            state.selectedWorkflow = snapshot.selectedWorkflow;
        },

        setCourseReturnState: function (snapshot) {
            state.courseReturnState = snapshot;
        },

        consumeCourseReturnState: function () {
            var snapshot = state.courseReturnState;
            state.courseReturnState = null;
            return snapshot;
        },

        setTheme: function (themeName) {
            state.theme = themeName === 'light' ? 'light' : 'dark';
            return state.theme;
        },

        setPalette: function (paletteName) {
            state.palette = normalizePaletteKey(paletteName);
            return state.palette;
        },

        setView: function (viewKey) {
            state.view = viewKey || '';
        },

        toggleView: function (viewKey) {
            state.view = state.view === viewKey ? '' : viewKey;
            return state.view;
        },

        setViewCategory: function (categoryKey) {
            state.viewCategory = categoryKey;
        }
    };

    var appRouter = {
        resolveRendererKey: function () {
            var view = appStore.getView();
            if (view === 'sheets') {
                return 'sheets';
            }
            if (!view) {
                return 'home';
            }
            if (view === 'exercises') {
                return 'exercises';
            }
            if (view === 'principles') {
                return 'principles';
            }
            return 'catalogCode';
        },

        renderActiveView: function () {
            var renderer = VIEW_RENDERERS[this.resolveRendererKey()];
            if (typeof renderer === 'function') {
                renderer();
            }
        }
    };