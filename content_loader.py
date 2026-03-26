import json
import os


EXPECTED_CONTENT_FILES = {
    "principles.json",
    "modern_approach_notes.json",
    "course_steps.json",
    "basics_enhancements.json",
    "adapter_insights.json",
    "adaptation_course.json",
    "workflow.json",
    "basics_groups.json",
    "interview_groups.json",
    "design_patterns_groups.json",
    "principles_groups.json",
    "course_steps_groups.json",
    "workflow_groups.json",
}


def _content_dir(base_dir):
    return os.path.join(base_dir, "content")


def _load_json(base_dir, file_name):
    path = os.path.join(_content_dir(base_dir), file_name)
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_content_manifest(base_dir):
    payload = _load_json(base_dir, "content_manifest.json")

    if not isinstance(payload, dict):
        raise ValueError("Invalid content manifest: expected object")

    if payload.get("version") != 1:
        raise ValueError("Invalid content manifest version: expected 1")

    files = payload.get("files")
    if not isinstance(files, list) or not all(isinstance(item, str) for item in files):
        raise ValueError("Invalid content manifest files: expected list[str]")

    file_set = set(files)
    missing = sorted(EXPECTED_CONTENT_FILES - file_set)
    extras = sorted(file_set - EXPECTED_CONTENT_FILES)
    if missing:
        raise ValueError(f"Manifest missing expected files: {missing}")
    if extras:
        raise ValueError(f"Manifest has unknown files: {extras}")

    content_dir = _content_dir(base_dir)
    for name in EXPECTED_CONTENT_FILES:
        path = os.path.join(content_dir, name)
        if not os.path.exists(path):
            raise ValueError(f"Missing content file: {name}")

    return payload


def _validate_string_list(value, field_name, key):
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(f"Invalid '{field_name}' for principles entry '{key}': expected list[str]")


def validate_principles(principles):
    if not isinstance(principles, dict):
        raise ValueError("Invalid principles payload: expected dict")

    required_fields = ["label", "description", "sourceLinks", "points", "notes", "pitfalls"]

    for key, entry in principles.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid principles entry '{key}': expected dict")

        for field in required_fields:
            if field not in entry:
                raise ValueError(f"Missing field '{field}' in principles entry '{key}'")

        if not isinstance(entry["label"], str) or not isinstance(entry["description"], str):
            raise ValueError(f"Invalid text fields in principles entry '{key}'")

        if not isinstance(entry["sourceLinks"], list):
            raise ValueError(f"Invalid sourceLinks in principles entry '{key}': expected list")

        for link in entry["sourceLinks"]:
            if not isinstance(link, dict):
                raise ValueError(f"Invalid source link in principles entry '{key}': expected dict")
            if not isinstance(link.get("label"), str) or not isinstance(link.get("url"), str):
                raise ValueError(f"Invalid source link shape in principles entry '{key}'")

        _validate_string_list(entry["points"], "points", key)
        _validate_string_list(entry["notes"], "notes", key)
        _validate_string_list(entry["pitfalls"], "pitfalls", key)


def load_principles(base_dir):
    payload = _load_json(base_dir, "principles.json")
    validate_principles(payload)
    return payload


def validate_modern_approach_notes(notes):
    if not isinstance(notes, dict):
        raise ValueError("Invalid modern approach notes payload: expected dict")

    for pattern_key, per_language in notes.items():
        if not isinstance(per_language, dict):
            raise ValueError(f"Invalid modern approach entry '{pattern_key}': expected dict")
        for lang_key, pair in per_language.items():
            if not isinstance(pair, dict):
                raise ValueError(
                    f"Invalid modern approach language entry '{pattern_key}/{lang_key}': expected dict"
                )
            if not isinstance(pair.get("classic"), str) or not isinstance(pair.get("modern"), str):
                raise ValueError(
                    f"Invalid modern/classic values in modern approach entry '{pattern_key}/{lang_key}'"
                )


def load_modern_approach_notes(base_dir):
    payload = _load_json(base_dir, "modern_approach_notes.json")
    validate_modern_approach_notes(payload)
    return payload


def validate_course_steps(course_steps):
    if not isinstance(course_steps, dict):
        raise ValueError("Invalid course steps payload: expected dict")

    required_fields = [
        "label",
        "description",
        "compareEntries",
        "adapterInsight",
        "sourceLinks",
        "codes",
    ]

    for key, entry in course_steps.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid course step '{key}': expected dict")
        for field in required_fields:
            if field not in entry:
                raise ValueError(f"Missing field '{field}' in course step '{key}'")
        if not isinstance(entry["label"], str) or not isinstance(entry["description"], str):
            raise ValueError(f"Invalid text fields in course step '{key}'")
        if not isinstance(entry["adapterInsight"], str):
            raise ValueError(f"Invalid adapterInsight in course step '{key}'")
        if not isinstance(entry["compareEntries"], list):
            raise ValueError(f"Invalid compareEntries in course step '{key}': expected list")
        if not isinstance(entry["sourceLinks"], list):
            raise ValueError(f"Invalid sourceLinks in course step '{key}': expected list")
        if not isinstance(entry["codes"], dict):
            raise ValueError(f"Invalid codes in course step '{key}': expected dict")


def load_course_steps(base_dir):
    payload = _load_json(base_dir, "course_steps.json")
    validate_course_steps(payload)
    return payload


def validate_basics_enhancements(enhancements):
    if not isinstance(enhancements, dict):
        raise ValueError("Invalid basics enhancements payload: expected dict")
    for key, entry in enhancements.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid basics enhancement '{key}': expected dict")


def load_basics_enhancements(base_dir):
    payload = _load_json(base_dir, "basics_enhancements.json")
    validate_basics_enhancements(payload)
    return payload


def validate_adapter_insights(adapter_insights):
    if not isinstance(adapter_insights, dict):
        raise ValueError("Invalid adapter insights payload: expected dict")
    for key, entry in adapter_insights.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid adapter insight '{key}': expected dict")
        if not isinstance(entry.get("insight"), str):
            raise ValueError(f"Invalid insight text in adapter insight '{key}'")
        compare_entries = entry.get("compareEntries", [])
        if not isinstance(compare_entries, list):
            raise ValueError(f"Invalid compareEntries in adapter insight '{key}': expected list")


def load_adapter_insights(base_dir):
    payload = _load_json(base_dir, "adapter_insights.json")
    validate_adapter_insights(payload)
    return payload


def validate_groups(groups, group_name):
    if not isinstance(groups, list):
        raise ValueError(f"Invalid {group_name} payload: expected list")
    for idx, group in enumerate(groups):
        if not isinstance(group, dict):
            raise ValueError(f"Invalid {group_name}[{idx}]: expected dict")
        if not isinstance(group.get("label"), str):
            raise ValueError(f"Invalid label in {group_name}[{idx}]")
        if not isinstance(group.get("keys"), list):
            raise ValueError(f"Invalid keys in {group_name}[{idx}]: expected list")


def load_basics_groups(base_dir):
    payload = _load_json(base_dir, "basics_groups.json")
    validate_groups(payload, "basics_groups")
    return payload


def load_interview_groups(base_dir):
    payload = _load_json(base_dir, "interview_groups.json")
    validate_groups(payload, "interview_groups")
    return payload


def load_design_patterns_groups(base_dir):
    payload = _load_json(base_dir, "design_patterns_groups.json")
    validate_groups(payload, "design_patterns_groups")
    return payload


def load_principles_groups(base_dir):
    payload = _load_json(base_dir, "principles_groups.json")
    validate_groups(payload, "principles_groups")
    return payload


def load_course_steps_groups(base_dir):
    payload = _load_json(base_dir, "course_steps_groups.json")
    validate_groups(payload, "course_steps_groups")
    return payload


def load_workflow_groups(base_dir):
    payload = _load_json(base_dir, "workflow_groups.json")
    if not isinstance(payload, list):
        raise ValueError("Invalid workflow_groups payload: expected list")
    return payload


def validate_adaptation_course(adaptation_course):
    if not isinstance(adaptation_course, list):
        raise ValueError("Invalid adaptation course payload: expected list")
    for idx, level in enumerate(adaptation_course):
        if not isinstance(level, dict):
            raise ValueError(f"Invalid adaptation course entry {idx}: expected dict")
        if not isinstance(level.get("level"), int):
            raise ValueError(f"Invalid level in adaptation course entry {idx}")
        if not isinstance(level.get("title"), str) or not isinstance(level.get("description"), str):
            raise ValueError(f"Invalid title/description in adaptation course entry {idx}")
        if not isinstance(level.get("viewItems"), list):
            raise ValueError(f"Invalid viewItems in adaptation course entry {idx}: expected list")


def load_adaptation_course(base_dir):
    payload = _load_json(base_dir, "adaptation_course.json")
    validate_adaptation_course(payload)
    return payload


def validate_workflow(workflow):
    if not isinstance(workflow, dict):
        raise ValueError("Invalid workflow payload: expected dict")
    for key, entry in workflow.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid workflow entry '{key}': expected dict")
        if not isinstance(entry.get("label"), str) or not isinstance(entry.get("description"), str):
            raise ValueError(f"Invalid label/description in workflow entry '{key}'")
        codes = entry.get("codes")
        if not isinstance(codes, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in codes.items()):
            raise ValueError(f"Invalid codes in workflow entry '{key}': expected dict[str, str]")


def load_workflow(base_dir):
    payload = _load_json(base_dir, "workflow.json")
    validate_workflow(payload)
    return payload
