from generator_utils import safe_json


APP_TEMPLATE_TOKENS = [
    ("__SHEETS_JSON__", "sheets"),
    ("__HOME_HTML_JSON__", "home_html"),
    ("__PROBLEMS_JSON__", "problems"),
    ("__INTERVIEW_JSON__", "interview"),
    ("__BASICS_JSON__", "basics"),
    ("__DESIGN_PATTERNS_JSON__", "design_patterns"),
    ("__PRINCIPLES_JSON__", "principles"),
    ("__COURSE_STEPS_JSON__", "course_steps"),
    ("__ADAPTATION_COURSE_JSON__", "adaptation_course"),
    ("__WORKFLOW_JSON__", "workflow"),
    ("__INTERVIEW_GROUPS_JSON__", "interview_groups"),
    ("__BASICS_GROUPS_JSON__", "basics_groups"),
    ("__DESIGN_PATTERNS_GROUPS_JSON__", "design_patterns_groups"),
    ("__PRINCIPLES_GROUPS_JSON__", "principles_groups"),
    ("__COURSE_STEPS_GROUPS_JSON__", "course_steps_groups"),
    ("__WORKFLOW_GROUPS_JSON__", "workflow_groups"),
    ("__LANG_LABELS_JSON__", "lang_labels"),
]


def build_app_payload(sheets, lang_labels, runtime_data):
    return {
        "sheets": sheets,
        "lang_labels": lang_labels,
        **runtime_data,
    }


def render_app_js(app_template, payload):
    app_js = app_template
    for token, payload_key in APP_TEMPLATE_TOKENS:
        app_js = app_js.replace(token, safe_json(payload[payload_key]))
    return app_js