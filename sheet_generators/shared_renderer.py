import html
import os
import re
from typing import Callable, Iterable


def split_deprecation_note(desc_text: str):
    """Split deprecation marker from description text for dedicated styling."""
    dep_match = re.search(r"\([^)]*deprecated[^)]*\)", desc_text, re.I)
    if not dep_match:
        return desc_text, ""

    dep_text = dep_match.group(0).strip()
    clean_desc = desc_text.replace(dep_match.group(0), "").strip()
    return clean_desc, dep_text


def format_description_cell(desc_text: str, version: str, deprecated_class: str = "header-note") -> str:
    clean_desc, deprecated_text = split_deprecation_note(desc_text or "")
    desc_escaped = html.escape(clean_desc)

    deprecated_html = ""
    if deprecated_text:
        deprecated_html = f' <span class="{deprecated_class}">{html.escape(deprecated_text)}</span>'

    version_html = f' <span class="version-tag">(since {html.escape(version)})</span>' if version else ""
    return f"{desc_escaped}{deprecated_html}{version_html}"


def render_section_table(
    section: dict,
    build_doc_url: Callable[[dict], str],
    *,
    item_header: str = "Item",
    description_header: str = "Description & Version",
    context_header: str = "Context",
    snippet_header: str = "Snippet",
    col_widths: Iterable[str] = ("18%", "42%", "15%", "25%"),
    builtin_context_labels: tuple[str, ...] = ("Built-in", ""),
    deprecated_class: str = "header-note",
) -> str:
    widths = list(col_widths)
    if len(widths) != 4:
        raise ValueError("col_widths must contain exactly 4 values")

    rows = []
    for category in section["categories"]:
        rows.append(
            f'<tr class="category-label"><td colspan="4">{html.escape(category["label"])}</td></tr>'
        )

        for item in category["items"]:
            url = build_doc_url(item)
            context = item.get("head", "")
            header_class = "header-note" if context not in builtin_context_labels else ""
            description_cell = format_description_cell(
                item.get("desc", ""),
                item.get("ver", ""),
                deprecated_class=deprecated_class,
            )

            row = f"""
            <tr class="{html.escape(item.get('cat', ''))}">
                <td><a href="{url}" target="_blank">{html.escape(item['kw'])}</a></td>
                <td>{description_cell}</td>
                <td><span class="{header_class}">{html.escape(context)}</span></td>
                <td><code>{html.escape(item.get('code', ''))}</code></td>
            </tr>
            """
            rows.append(row)

    return f"""
    <h2>{html.escape(section['section'])}</h2>
    <table>
        <thead>
            <tr>
                <th style="width: {widths[0]};">{html.escape(item_header)}</th>
                <th style="width: {widths[1]};">{html.escape(description_header)}</th>
                <th style="width: {widths[2]};">{html.escape(context_header)}</th>
                <th style="width: {widths[3]};">{html.escape(snippet_header)}</th>
            </tr>
        </thead>
        <tbody>
            {''.join(rows)}
        </tbody>
    </table>
    """


def build_content_html(sections: list[dict], render_table: Callable[[dict], str], advanced_separator_label: str) -> str:
    blocks = []
    for section in sections:
        if section.get("is_advanced"):
            blocks.append(
                f'<div class="separator"><span>{html.escape(advanced_separator_label)}</span></div>'
            )
        blocks.append(render_table(section))
    return "".join(blocks)


def load_sheet_template(generator_file: str) -> str:
    tpl_path = os.path.abspath(os.path.join(os.path.dirname(generator_file), "..", "..", "sheet_template.html"))
    with open(tpl_path, "r", encoding="utf-8") as tplf:
        return tplf.read()


def render_sheet_html(generator_file: str, title: str, legend_html: str, content_html: str) -> str:
    template = load_sheet_template(generator_file)
    return template.replace("__TITLE__", title).replace("__LEGEND__", legend_html).replace("__CONTENT__", content_html)


def write_sheet_output(generator_file: str, filename: str, output_html: str) -> str:
    out_dir = os.path.dirname(generator_file)
    out_path = os.path.join(out_dir, filename)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(output_html)
    print(f"Successfully generated {out_path}")
    return out_path
