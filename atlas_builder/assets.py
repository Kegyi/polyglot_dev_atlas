import os
import subprocess
import sys
import urllib.request


def run_generators(langs, sheet_generators_dir):
    """Run each per-language generator once (deduplicated by folder)."""
    seen_folders = set()
    for _lang_id, _label, html_rel in langs:
        folder = html_rel.split("/")[0]
        if folder in seen_folders:
            continue
        seen_folders.add(folder)

        script = os.path.join(sheet_generators_dir, folder, f"generate_{folder}_cheat_sheet.py")
        if not os.path.exists(script):
            print(f"  [skip] no generator found: {script}")
            continue

        print(f"  [gen] {folder} ...")
        try:
            subprocess.run([sys.executable, script], cwd=os.path.dirname(script), check=True)
        except subprocess.CalledProcessError as exc:
            print(f"  [warn] generator exited with code {exc.returncode}")
        except Exception as exc:  # pragma: no cover - defensive handling
            print(f"  [warn] {exc}")


def ensure_offline_assets(offline_assets_dir, asset_urls):
    """Ensure local highlight.js fallback files exist under output/assets/hljs."""
    os.makedirs(offline_assets_dir, exist_ok=True)

    downloaded = 0
    skipped = 0
    failed = 0

    for rel_path, url in asset_urls.items():
        dst = os.path.join(offline_assets_dir, *rel_path.split("/"))
        os.makedirs(os.path.dirname(dst), exist_ok=True)

        if os.path.exists(dst) and os.path.getsize(dst) > 0:
            skipped += 1
            continue

        try:
            with urllib.request.urlopen(url, timeout=20) as resp:
                payload = resp.read()
            with open(dst, "wb") as fh:
                fh.write(payload)
            downloaded += 1
        except Exception as exc:  # pragma: no cover - network/environment dependent
            failed += 1
            print(f"  [warn] could not fetch fallback asset: {url} ({exc})")

    print(
        "  [assets] offline hljs fallback -> "
        f"downloaded={downloaded}, existing={skipped}, failed={failed}"
    )
