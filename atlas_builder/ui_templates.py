import os

from generator_utils import read_file


def _load_template_asset(base_dir, asset_name, extension):
    file_path = os.path.join(base_dir, "templates", asset_name + extension)
    dir_path = os.path.join(base_dir, "templates", asset_name)

    if os.path.isdir(dir_path):
        parts = []
        for entry in sorted(os.listdir(dir_path)):
            if not entry.endswith(extension):
                continue
            parts.append(read_file(os.path.join(dir_path, entry)))
        if parts:
            return "\n".join(part.rstrip("\r\n") for part in parts) + "\n"

    return read_file(file_path)


def load_ui_templates(base_dir):
    ui_styles = _load_template_asset(base_dir, "ui_styles", ".css")
    app_template = _load_template_asset(base_dir, "app", ".js")
    return ui_styles, app_template
