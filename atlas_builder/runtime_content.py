import os

from generator_utils import load_examples_from_dir, markdown_to_html, read_file


def load_example_catalogs(code_examples_dir):
    return {
        "problems": load_examples_from_dir(os.path.join(code_examples_dir, "problems")),
        "interview": load_examples_from_dir(os.path.join(code_examples_dir, "interview")),
        "basics": load_examples_from_dir(os.path.join(code_examples_dir, "language_basics")),
        "design_patterns": load_examples_from_dir(os.path.join(code_examples_dir, "design_patterns")),
    }


def load_home_html(main_page_doc_path):
    if os.path.exists(main_page_doc_path):
        return markdown_to_html(read_file(main_page_doc_path))

    print(f"  [warn] missing main page doc: {main_page_doc_path}")
    return "<h1>Polyglot Dev Atlas</h1><p>Main page doc not found.</p>"