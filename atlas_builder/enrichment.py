def apply_config_enrichment(problems, basics, design_patterns, configs):
    for pattern_key, notes in configs["modern_approach_notes"].items():
        if pattern_key in design_patterns:
            design_patterns[pattern_key]["modernNotes"] = notes

    for problem_key, insight_data in configs["adapter_insights"].items():
        if problem_key in problems:
            problems[problem_key]["adapterInsight"] = insight_data["insight"]
            if insight_data.get("compareEntries"):
                problems[problem_key]["compareEntries"] = insight_data["compareEntries"]

    for basic_key, enhancement in configs["basics_enhancements"].items():
        if basic_key in basics:
            basics[basic_key].update(enhancement)
        else:
            basics[basic_key] = enhancement


def print_missing_warnings(problems, interview, basics, design_patterns, principles):
    if not problems:
        print("  [warn] no problem examples found.")
    if not interview:
        print("  [warn] no interview examples found.")
    if not basics:
        print("  [warn] no language basics examples found.")
    if not design_patterns:
        print("  [warn] no design pattern examples found.")
    if not principles:
        print("  [warn] no principles configured.")
