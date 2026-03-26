from .content import load_external_content_configs
from .enrichment import apply_config_enrichment, print_missing_warnings
from .runtime_content import load_example_catalogs, load_home_html


def assemble_runtime_data(base_dir, code_examples_dir, main_page_doc_path, strict_content=False):
    example_catalogs = load_example_catalogs(code_examples_dir)
    problems = example_catalogs["problems"]
    interview = example_catalogs["interview"]
    basics = example_catalogs["basics"]
    design_patterns = example_catalogs["design_patterns"]

    configs = load_external_content_configs(base_dir, strict=strict_content)
    apply_config_enrichment(problems, basics, design_patterns, configs)
    print_missing_warnings(
        problems,
        interview,
        basics,
        design_patterns,
        configs["principles"],
    )
    home_html = load_home_html(main_page_doc_path)

    return {
        "home_html": home_html,
        "problems": problems,
        "interview": interview,
        "basics": basics,
        "design_patterns": design_patterns,
        "principles": configs["principles"],
        "course_steps": configs["course_steps"],
        "adaptation_course": configs["adaptation_course"],
        "workflow": configs["workflow"],
        "interview_groups": configs["interview_groups"],
        "basics_groups": configs["basics_groups"],
        "design_patterns_groups": configs["design_patterns_groups"],
        "principles_groups": configs["principles_groups"],
        "course_steps_groups": configs["course_steps_groups"],
        "workflow_groups": configs["workflow_groups"],
    }
