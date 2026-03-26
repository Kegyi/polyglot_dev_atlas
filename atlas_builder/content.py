from content_loader import (
    load_adapter_insights,
    load_adaptation_course,
    load_basics_enhancements,
    load_basics_groups,
    load_course_steps,
    load_course_steps_groups,
    load_design_patterns_groups,
    load_interview_groups,
    load_modern_approach_notes,
    load_principles,
    load_principles_groups,
    load_workflow,
    load_workflow_groups,
    validate_content_manifest,
)
from legacy_content_defaults import (
    ADAPTER_INSIGHTS,
    ADAPTATION_COURSE,
    BASICS_ENHANCEMENTS,
    BASICS_GROUPS,
    COURSE_STEPS,
    COURSE_STEPS_GROUPS,
    DESIGN_PATTERNS_GROUPS,
    INTERVIEW_GROUPS,
    MODERN_APPROACH_NOTES,
    PRINCIPLES,
    PRINCIPLES_GROUPS,
    WORKFLOW,
    WORKFLOW_GROUPS,
)

CONTENT_CONFIG_SOURCES = [
    ("adapter_insights", "adapter_insights.json", load_adapter_insights, ADAPTER_INSIGHTS),
    ("basics_groups", "basics_groups.json", load_basics_groups, BASICS_GROUPS),
    ("interview_groups", "interview_groups.json", load_interview_groups, INTERVIEW_GROUPS),
    (
        "design_patterns_groups",
        "design_patterns_groups.json",
        load_design_patterns_groups,
        DESIGN_PATTERNS_GROUPS,
    ),
    ("principles_groups", "principles_groups.json", load_principles_groups, PRINCIPLES_GROUPS),
    (
        "course_steps_groups",
        "course_steps_groups.json",
        load_course_steps_groups,
        COURSE_STEPS_GROUPS,
    ),
    ("workflow_groups", "workflow_groups.json", load_workflow_groups, WORKFLOW_GROUPS),
    ("adaptation_course", "adaptation_course.json", load_adaptation_course, ADAPTATION_COURSE),
    ("workflow", "workflow.json", load_workflow, WORKFLOW),
    (
        "modern_approach_notes",
        "modern_approach_notes.json",
        load_modern_approach_notes,
        MODERN_APPROACH_NOTES,
    ),
    (
        "basics_enhancements",
        "basics_enhancements.json",
        load_basics_enhancements,
        BASICS_ENHANCEMENTS,
    ),
    ("course_steps", "course_steps.json", load_course_steps, COURSE_STEPS),
    ("principles", "principles.json", load_principles, PRINCIPLES),
]


def _load_content_item(label, loader, fallback, strict, base_dir):
    try:
        return loader(base_dir)
    except Exception as exc:
        if strict:
            raise RuntimeError(f"content validation failed for {label}: {exc}") from exc
        print(f"  [warn] could not load content/{label}, using in-file fallback ({exc})")
        return fallback


def load_external_content_configs(base_dir, strict=False):
    try:
        validate_content_manifest(base_dir)
    except Exception as exc:
        if strict:
            raise RuntimeError(f"content manifest validation failed: {exc}") from exc
        print(f"  [warn] content manifest validation failed ({exc})")

    return {
        key: _load_content_item(file_name, loader, fallback, strict, base_dir)
        for key, file_name, loader, fallback in CONTENT_CONFIG_SOURCES
    }


def validate_external_content(base_dir):
    load_external_content_configs(base_dir, strict=True)
