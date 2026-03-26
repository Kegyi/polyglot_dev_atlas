import html as html_lib
import os

from generator_utils import extract_between, normalize_sheet_body, read_file


def load_shared_css(langs, sheet_generators_dir):
    shared_css = ""
    for _lang_id, _label, html_rel in langs:
        path = os.path.join(sheet_generators_dir, html_rel)
        if os.path.exists(path):
            shared_css = extract_between(read_file(path), "style")
            break

    if not shared_css:
        print("  [warn] Could not find shared CSS; falling back to empty styles.")

    return shared_css


def load_sheets(langs, sheet_generators_dir):
    sheets = {}
    lang_labels = {}

    for lang_id, label, html_rel in langs:
        lang_labels[lang_id] = label

        path = os.path.join(sheet_generators_dir, html_rel)
        if os.path.exists(path):
            body = normalize_sheet_body(extract_between(read_file(path), "body"))
        else:
            print(f"  [warn] missing sheet: {path}")
            body = (
                '<p class="empty-note">Sheet not found: '
                + html_lib.escape(label)
                + "<br>Run the generator first.</p>"
            )

        sheets[lang_id] = {"label": label, "body": body}

    return sheets, lang_labels
