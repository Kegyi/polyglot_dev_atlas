from dataclasses import dataclass
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
SHEET_GENERATORS_DIR = os.path.join(BASE_DIR, "sheet_generators")
CODE_EXAMPLES_DIR = os.path.join(BASE_DIR, "code_examples")
MAIN_PAGE_DOC_PATH = os.path.join(BASE_DIR, "MAIN_PAGE_README.md")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "polyglot_dev_atlas.html")
OFFLINE_ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets", "hljs")

HLJS_ASSET_URLS = {
    "atom-one-dark.min.css": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/atom-one-dark.min.css",
    "github.min.css": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/github.min.css",
    "highlight.min.js": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js",
    "languages/scala.min.js": "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/languages/scala.min.js",
}

# (id, display label, relative path to generated HTML)
LANGS = [
    ("cpp", "C++", "cpp/cpp_cheat_sheet.html"),
    ("python", "Python", "python/python_cheat_sheet.html"),
    ("go", "Go", "go/go_cheat_sheet.html"),
    ("typescript", "TypeScript", "typescript/typescript_cheat_sheet.html"),
    ("scala2", "Scala 2", "scala/scala2_cheat_sheet.html"),
    ("scala3", "Scala 3", "scala/scala3_cheat_sheet.html"),
]


@dataclass(frozen=True)
class BuildContext:
    base_dir: str
    output_dir: str
    sheet_generators_dir: str
    code_examples_dir: str
    main_page_doc_path: str
    output_file: str
    offline_assets_dir: str


DEFAULT_BUILD_CONTEXT = BuildContext(
    base_dir=BASE_DIR,
    output_dir=OUTPUT_DIR,
    sheet_generators_dir=SHEET_GENERATORS_DIR,
    code_examples_dir=CODE_EXAMPLES_DIR,
    main_page_doc_path=MAIN_PAGE_DOC_PATH,
    output_file=OUTPUT_FILE,
    offline_assets_dir=OFFLINE_ASSETS_DIR,
)
