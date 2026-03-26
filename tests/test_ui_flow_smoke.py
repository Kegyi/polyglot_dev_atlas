import unittest
from pathlib import Path

from atlas_builder.ui_templates import load_ui_templates


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _assert_ordered_substrings(test_case, haystack, ordered_parts, anchor=None):
    start_at = 0
    if anchor is not None:
        start_at = haystack.index(anchor)

    indexes = []
    cursor = start_at
    for part in ordered_parts:
        idx = haystack.index(part, cursor)
        indexes.append(idx)
        cursor = idx + len(part)
    test_case.assertEqual(indexes, sorted(indexes))


class UiFlowSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _ui_styles, cls.app_template = load_ui_templates(str(PROJECT_ROOT))

    def test_course_toggle_flow_is_wired_in_order(self):
        anchor = "document.getElementById('courseBtn').addEventListener('click', function () {"
        _assert_ordered_substrings(
            self,
            self.app_template,
            [
                "if (selectIsCourseMode()) {",
                "appStore.setCourseMode(false);",
                "appStore.setCourseLevel(0);",
                "restorePreCourseView();",
                "rememberPreCourseView();",
                "appStore.setCourseMode(true);",
                "appStore.setCourseLevel(0);",
                "navigateCourse(0);",
            ],
            anchor=anchor,
        )

    def test_language_chip_input_modes_are_present(self):
        required_parts = [
            "btn.addEventListener('click', function (event) {",
            "handleLanguageClick(capturedKey, 0);",
            "btn.addEventListener('contextmenu', function (event) {",
            "handleLanguageClick(capturedKey, 1);",
            "btn.addEventListener('pointerdown', function (event) {",
            "beginLanguageDrag(event, capturedKey);",
            "btn.addEventListener('pointermove', function (event) {",
            "updateLanguageDrag(event);",
            "btn.addEventListener('pointerup', function (event) {",
            "endLanguageDrag(event, false);",
        ]

        for part in required_parts:
            self.assertIn(part, self.app_template)

    def test_theme_palette_and_view_category_restore_happens_before_initial_render(self):
        _assert_ordered_substrings(
            self,
            self.app_template,
            [
                "savedTheme = window.localStorage.getItem(THEME_STORAGE_KEY) || 'dark';",
                "savedPalette = window.localStorage.getItem(PALETTE_STORAGE_KEY) || 'brand';",
                "savedViewCategory = window.localStorage.getItem(VIEW_CATEGORY_STORAGE_KEY) || 'atlas';",
                "savedSidebarCollapsed = window.localStorage.getItem(SIDEBAR_STORAGE_KEY) || '0';",
                "applyTheme(savedTheme);",
                "applyPalette(savedPalette);",
                "appStore.setViewCategory(savedViewCategory);",
                "appStore.setSidebarCollapsed(savedSidebarCollapsed === '1');",
                "renderAll();",
            ],
        )


if __name__ == "__main__":
    unittest.main()
