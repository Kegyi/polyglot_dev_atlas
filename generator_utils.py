import html as html_lib
import json
import os
import re


def read_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def extract_between(html_content, tag):
    """Return the inner content of the first occurrence of <tag ...> ... </tag>."""
    pattern = rf"<{tag}[^>]*>(.*?)</{tag}>"
    match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""


def normalize_sheet_body(body):
    """Remove per-sheet title so the page-level title can be shown once."""
    if not body:
        return body

    replaced = re.sub(r"<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.DOTALL | re.IGNORECASE)
    return replaced.lstrip()


def parse_readme_metadata(readme_path, default_label):
    label = default_label
    description = ""
    source_links = []
    if not os.path.exists(readme_path):
        return label, description, source_links

    try:
        def heading_key(text):
            return text.lstrip("#").strip().lower()

        with open(readme_path, "r", encoding="utf-8") as fh:
            lines = [line.rstrip("\n") for line in fh]

        for line in lines:
            stripped = line.strip()
            key = heading_key(stripped)
            if not stripped:
                continue
            if stripped.startswith("#"):
                label = stripped.lstrip("#").strip()
                break
            if key.startswith("description") or key.startswith("files"):
                continue
            if set(stripped) <= set("-="):
                continue
            label = stripped
            break

        desc_lines = []
        found = False
        for idx, line in enumerate(lines):
            stripped = line.strip()
            key = heading_key(stripped)
            if key.startswith("description"):
                j = idx + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                while j < len(lines):
                    candidate = lines[j].strip()
                    candidate_key = heading_key(candidate)
                    if candidate.startswith("#") or candidate_key.startswith("files") or candidate_key.startswith("source"):
                        break
                    if set(candidate) <= set("-=") and candidate:
                        break
                    if not candidate:
                        if desc_lines:
                            break
                        j += 1
                        continue
                    desc_lines.append(candidate)
                    j += 1
                found = True
                break

        if not found:
            j = 0
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip().startswith("#"):
                j += 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            while j < len(lines):
                candidate = lines[j].strip()
                candidate_key = heading_key(candidate)
                if not candidate:
                    if desc_lines:
                        break
                    j += 1
                    continue
                if candidate.startswith("#") or candidate_key.startswith("files") or candidate_key.startswith("source"):
                    break
                if set(candidate) <= set("-=") and candidate:
                    break
                desc_lines.append(candidate)
                j += 1

        description = " ".join(desc_lines).strip()

        for idx, line in enumerate(lines):
            key = heading_key(line.strip())
            if not (key.startswith("source") or key.startswith("sources")):
                continue

            j = idx + 1
            while j < len(lines) and not lines[j].strip():
                j += 1

            while j < len(lines):
                candidate = lines[j].strip()
                candidate_key = heading_key(candidate)
                if not candidate:
                    if source_links:
                        break
                    j += 1
                    continue
                if candidate.startswith("#") or candidate_key.startswith("implementation") or candidate_key.startswith("file"):
                    break

                text = candidate[2:].strip() if candidate.startswith("- ") else candidate
                md_match = re.match(r"\[([^\]]+)\]\((https?://[^)]+)\)", text)
                label_match = re.match(r"([^:]+):\s*(https?://\S+)$", text)
                url_match = re.match(r"(https?://\S+)$", text)

                if md_match:
                    source_links.append({"label": md_match.group(1).strip(), "url": md_match.group(2).strip()})
                elif label_match:
                    source_links.append({"label": label_match.group(1).strip(), "url": label_match.group(2).strip()})
                elif url_match:
                    source_links.append({"label": "Source", "url": url_match.group(1).strip()})

                j += 1
    except Exception:
        pass

    return label, description, source_links


def language_key_for_extension(ext):
    ext = ext.lower()
    if ext in (".cpp", ".cc", ".cxx"):
        return "cpp"
    if ext == ".py":
        return "python"
    if ext == ".go":
        return "go"
    if ext in (".ts", ".tsx"):
        return "typescript"
    if ext == ".scala":
        return "scala"
    return None


def load_examples_from_dir(examples_dir):
    examples = {}
    if not os.path.isdir(examples_dir):
        return examples

    for name in sorted(os.listdir(examples_dir)):
        entry_dir = os.path.join(examples_dir, name)
        if not os.path.isdir(entry_dir):
            continue

        label, description, source_links = parse_readme_metadata(os.path.join(entry_dir, "README.md"), name)
        codes = {}

        for file_name in sorted(os.listdir(entry_dir)):
            file_path = os.path.join(entry_dir, file_name)
            if os.path.isdir(file_path):
                continue

            stem, ext = os.path.splitext(file_name)
            lang = language_key_for_extension(ext)
            if not lang:
                continue

            # For .scala files the stem itself is the key (scala2, scala3, scala3_modern, …)
            # For all other languages derive the key from the language tag.
            if ext.lower() == ".scala":
                key = stem
            else:
                key = (lang + '_modern') if stem.endswith('_modern') else lang
            try:
                codes[key] = read_file(file_path)
            except Exception:
                codes[key] = ""

        if codes:
            examples[name] = {
                "label": label,
                "description": description,
                "sourceLinks": source_links,
                "codes": codes,
            }

    return examples



def safe_json(value):
    return json.dumps(value).replace("</script>", "<\\/script>")


def markdown_inline(text):
    escaped = html_lib.escape(text)
    result = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    # Standalone X -> visually distinct badge
    result = re.sub(r"<code>X</code>", '<code class="no-equiv">✗</code>', result)
    # Partial (approx): prefix -> split out label so it stands out
    result = re.sub(
        r"<code>Partial \(approx\):\s*",
        '<span class="partial-label">Partial (approx):</span><code>',
        result,
    )
    return result


def markdown_to_html(md_text):
    lines = md_text.splitlines()
    out = []
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("### "):
            out.append(f"<h3>{markdown_inline(stripped[4:])}</h3>")
            i += 1
            continue

        if stripped.startswith("## "):
            out.append(f"<h2>{markdown_inline(stripped[3:])}</h2>")
            i += 1
            continue

        if stripped.startswith("# "):
            out.append(f"<h1>{markdown_inline(stripped[2:])}</h1>")
            i += 1
            continue

        if stripped.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(f"<li>{markdown_inline(lines[i].strip()[2:])}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue

        if "|" in stripped:
            j = i
            table_lines = []
            while j < len(lines) and "|" in lines[j] and lines[j].strip():
                table_lines.append(lines[j].strip())
                j += 1

            if len(table_lines) >= 2 and re.fullmatch(r"\|?\s*[-:| ]+\s*\|?", table_lines[1]):
                def split_row(row_text):
                    row = row_text
                    if row.startswith("|"):
                        row = row[1:]
                    if row.endswith("|"):
                        row = row[:-1]
                    return [c.strip() for c in row.split("|")]

                headers = split_row(table_lines[0])
                body_rows = [split_row(r) for r in table_lines[2:]]

                thead = "<thead><tr>" + "".join(f"<th>{markdown_inline(h)}</th>" for h in headers) + "</tr></thead>"
                tbody_rows = []
                for row in body_rows:
                    row_cells = row + ([""] * max(0, len(headers) - len(row)))
                    tbody_rows.append("<tr>" + "".join(f"<td>{markdown_inline(c)}</td>" for c in row_cells[:len(headers)]) + "</tr>")
                tbody = "<tbody>" + "".join(tbody_rows) + "</tbody>"

                out.append('<div class="doc-table-wrap"><table class="doc-table">' + thead + tbody + "</table></div>")
                i = j
                continue

        out.append(f"<p>{markdown_inline(stripped)}</p>")
        i += 1

    return "\n".join(out)
