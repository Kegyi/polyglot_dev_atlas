    function selectCurrentView() {
        return appStore.getView();
    }

    function selectCurrentViewCategory() {
        return appStore.getViewCategory();
    }

    function selectPrimaryLang() {
        return appStore.getSelectedLang(0);
    }

    function selectSecondaryLang() {
        return appStore.getSelectedLang(1);
    }

    function selectIsCompareMode() {
        return appStore.getCompareCount() === 2;
    }

    function selectActiveCompareSlot() {
        return appStore.getActiveSlot();
    }

    function selectIsCourseMode() {
        return appStore.isCourseModeEnabled();
    }

    function selectCourseLevel() {
        return appStore.getCourseLevel();
    }