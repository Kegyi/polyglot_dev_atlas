import os

from generator_utils import read_file


def load_ui_templates(base_dir):
    ui_styles = read_file(os.path.join(base_dir, "templates", "ui_styles.css"))
    app_template = read_file(os.path.join(base_dir, "templates", "app.js"))
    return ui_styles, app_template
