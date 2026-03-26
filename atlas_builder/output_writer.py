import os


def write_output(output_dir, output_file, output_html):
    os.makedirs(output_dir, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as fh:
        fh.write(output_html)

    return os.path.getsize(output_file) // 1024