import os
import sys
import urllib.parse

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from sheet_generators.shared_renderer import (
    build_content_html,
    render_section_table,
    render_sheet_html,
    write_sheet_output,
)

# --- DATA SECTION: Add or update keywords here ---
KEYWORDS_DATA = [
    {
        "section": "1. Core Essentials",
        "categories": [
            {
                "label": "Fundamental Types",
                "items": [
                    {"kw": "None", "cat": "type", "ver": "Python 3", "head": "Built-in", "desc": "Null / no value", "code": "x = None"},
                    {"kw": "bool", "cat": "type", "ver": "Python 2", "head": "Built-in", "desc": "True or False", "code": "flag = True"},
                    {"kw": "int", "cat": "type", "ver": "Python 3", "head": "Built-in", "desc": "Arbitrary-precision integer", "code": "count = 42"},
                    {"kw": "float", "cat": "type", "ver": "Python 2", "head": "Built-in", "desc": "Floating point number", "code": "pi = 3.14159"},
                    {"kw": "complex", "cat": "type", "ver": "Python 2", "head": "Built-in", "desc": "Complex numbers", "code": "z = 1+2j"},
                    {"kw": "str", "cat": "type", "ver": "Python 3", "head": "Built-in", "desc": "Unicode text", "code": "s = 'hello'"},
                    {"kw": "bytes", "cat": "type", "ver": "Python 3", "head": "Built-in", "desc": "Immutable byte sequence", "code": "b = b'\\x00'"},
                    {"kw": "list", "cat": "type", "ver": "Python 2", "head": "Built-in", "desc": "Mutable sequence", "code": "lst = [1, 2, 3]"},
                    {"kw": "tuple", "cat": "type", "ver": "Python 2", "head": "Built-in", "desc": "Immutable sequence", "code": "t = (1, 2)"},
                    {"kw": "set", "cat": "type", "ver": "Python 2.4", "head": "Built-in", "desc": "Unordered unique items", "code": "s = {1, 2, 3}"},
                    {"kw": "dict", "cat": "type", "ver": "Python 2", "head": "Built-in", "desc": "Key-value mapping", "code": "d = {'a': 1}"},
                ]
            },
            {
                "label": "Control Flow",
                "items": [
                    {"kw": "if / elif / else", "cat": "logic", "ver": "Python 2", "head": "Built-in", "desc": "Conditional branching", "code": "if x > 0:\n    ...\nelif x == 0:\n    ...\nelse:\n    ..."},
                    {"kw": "for", "cat": "logic", "ver": "Python 2", "head": "Built-in", "desc": "Iterator-based loop", "code": "for i in range(5):\n    print(i)"},
                    {"kw": "while", "cat": "logic", "ver": "Python 2", "head": "Built-in", "desc": "Loop while condition holds", "code": "while cond:\n    do_something()"},
                    {"kw": "break", "cat": "logic", "ver": "Python 2", "head": "Built-in", "desc": "Exit loop early", "code": "if done:\n    break"},
                    {"kw": "continue", "cat": "logic", "ver": "Python 2", "head": "Built-in", "desc": "Skip to next iteration", "code": "if skip:\n    continue"},
                    {"kw": "pass", "cat": "logic", "ver": "Python 2", "head": "Built-in", "desc": "No-op placeholder", "code": "def todo():\n    pass"},
                    {"kw": "return", "cat": "logic", "ver": "Python 2", "head": "Built-in", "desc": "Return from function", "code": "return value"},
                ]
            },
            {
                "label": "Functions & Callables",
                "items": [
                    {"kw": "def", "cat": "function", "ver": "Python 2", "head": "Built-in", "desc": "Define a function", "code": "def f(x):\n    return x*2"},
                    {"kw": "lambda", "cat": "function", "ver": "Python 2", "head": "Built-in", "desc": "Anonymous function expression", "code": "f = lambda x: x+1"},
                    {"kw": "yield", "cat": "function", "ver": "Python 2.3", "head": "Built-in", "desc": "Produce generator values", "code": "def gen():\n    yield from range(3)"},
                    {"kw": "async / await", "cat": "concurrency", "ver": "Python 3.5", "head": "Built-in", "desc": "Async functions and suspension", "code": "async def coro():\n    await asyncio.sleep(0)"},
                ]
            },
            {
                "label": "OOP & Classes",
                "items": [
                    {"kw": "class", "cat": "oop", "ver": "Python 2", "head": "Built-in", "desc": "Define a class", "code": "class C:\n    def __init__(self, x):\n        self.x = x"},
                    {"kw": "self", "cat": "oop", "ver": "Python 2", "head": "Convention", "desc": "Instance reference in methods", "code": "def method(self):\n    return self.x"},
                    {"kw": "super", "cat": "oop", "ver": "Python 2.2", "head": "Built-in", "desc": "Call base class methods", "code": "super().method()"},
                    {"kw": "@staticmethod / @classmethod / @property", "cat": "oop", "ver": "Python 2.2", "head": "Built-in", "desc": "Common method decorators", "code": "@staticmethod\ndef f():\n    pass"},
                ]
            }
        ]
    },
    {
        "section": "2. Advanced & Ecosystem",
        "is_advanced": True,
        "categories": [
            {
                "label": "Typing & Annotations",
                "items": [
                    {"kw": "typing.Optional", "cat": "typing", "ver": "Python 3.5", "head": "typing", "desc": "Optional type hint", "code": "from typing import Optional\nval: Optional[int] = None"},
                    {"kw": "typing.List / Dict / Union / Any", "cat": "typing", "ver": "Python 3.5", "head": "typing", "desc": "Common typing utilities", "code": "from typing import List, Dict\nnums: List[int] = []"},
                    {"kw": "from __future__ import annotations", "cat": "typing", "ver": "Python 3.7", "head": "__future__", "desc": "Postpone evaluation of annotations", "code": "from __future__ import annotations"},
                ]
            },
            {
                "label": "Concurrency & Async",
                "items": [
                    {"kw": "threading.Thread", "cat": "concurrency", "ver": "Python 2", "head": "threading", "desc": "Start a background thread", "code": "from threading import Thread\nThread(target=fn).start()"},
                    {"kw": "concurrent.futures", "cat": "concurrency", "ver": "Python 3.2", "head": "concurrent.futures", "desc": "Thread/Process pools", "code": "from concurrent.futures import ThreadPoolExecutor"},
                    {"kw": "asyncio", "cat": "concurrency", "ver": "Python 3.4", "head": "asyncio", "desc": "Async event loop and coroutines", "code": "import asyncio\nasyncio.run(main())"},
                ]
            },
            {
                "label": "Itertools & Functional",
                "items": [
                    {"kw": "itertools.chain / islice / tee", "cat": "iter", "ver": "Python 2.3", "head": "itertools", "desc": "Composable iterator helpers", "code": "import itertools\nlist(itertools.chain(a, b))"},
                    {"kw": "map / filter / zip / enumerate", "cat": "iter", "ver": "Python 2", "head": "Built-in", "desc": "Functional iteration helpers", "code": "for i, v in enumerate(seq):\n    ..."},
                    {"kw": "functools.lru_cache", "cat": "perf", "ver": "Python 3.2", "head": "functools", "desc": "Memoize function results", "code": "from functools import lru_cache\n@lru_cache()\ndef f(x):\n    ..."},
                ]
            }
        ]
    },
    {
        "section": "3. Standard Library Highlights (Non-Keywords)",
        "is_library": True,
        "categories": [
            {
                "label": "Common Modules",
                "items": [
                    {"kw": "pathlib", "cat": "module", "ver": "Python 3.4", "head": "pathlib", "desc": "Object-oriented filesystem paths", "code": "from pathlib import Path\np = Path('.')"},
                    {"kw": "os / sys", "cat": "module", "ver": "Python 2", "head": "os, sys", "desc": "OS and interpreter interfaces", "code": "import os\nimport sys"},
                    {"kw": "subprocess", "cat": "module", "ver": "Python 2.4", "head": "subprocess", "desc": "Spawn and manage subprocesses", "code": "import subprocess\nsubprocess.run(['ls'])"},
                    {"kw": "json / csv", "cat": "module", "ver": "Python 2.6", "head": "json, csv", "desc": "Data interchange helpers", "code": "import json\njson.dumps(obj)"},
                    {"kw": "logging", "cat": "module", "ver": "Python 2.3", "head": "logging", "desc": "Flexible logging infrastructure", "code": "import logging\nlogging.basicConfig(level=logging.INFO)"},
                    {"kw": "argparse", "cat": "module", "ver": "Python 2.7", "head": "argparse", "desc": "CLI argument parsing", "code": "import argparse\nparser = argparse.ArgumentParser()"},
                ]
            }
        ]
    }
]

# Sheet rendering now uses the shared `sheet_template.html` in the parent folder.


def build_doc_url(item):
    """Create a helpful docs.python.org URL for an item; fallback to search."""
    kw = item.get('kw', '')
    head = item.get('head', '')
    # quick map for common builtins -> functions.html anchors
    builtins_map = {
        'len': 'len', 'range': 'range', 'enumerate': 'enumerate', 'zip': 'zip', 'map': 'map',
        'filter': 'filter', 'sum': 'sum', 'min': 'min', 'max': 'max', 'open': 'open', 'print': 'print',
        'sorted': 'sorted', 'reversed': 'reversed'
    }
    lower_kw = kw.split()[0].strip().strip('/')
    if lower_kw in builtins_map:
        return f"https://docs.python.org/3/library/functions.html#{builtins_map[lower_kw]}"

    # if head names a module, link to that module's docs
    head_module = head.split()[0].strip().strip('<>,')
    common_modules = ['itertools', 'functools', 'asyncio', 'threading', 'concurrent.futures', 'pathlib', 'os', 'sys', 'subprocess', 'json', 'logging', 'argparse', 'typing']
    if head_module in common_modules:
        module_name = head_module
        # special-case concurrent.futures
        if module_name == 'concurrent.futures':
            return 'https://docs.python.org/3/library/concurrent.futures.html'
        return f"https://docs.python.org/3/library/{module_name}.html"

    # fallback: search the docs for the keyword
    return f"https://docs.python.org/3/search.html?q={urllib.parse.quote(kw)}"


def generate_table(section):
    return render_section_table(section, build_doc_url)


def main():
    content_html = build_content_html(KEYWORDS_DATA, generate_table, 'Advanced & Ecosystem')
    title = 'Python Polyglot Dev Atlas'
    legend_html = '''<div class="legend-row">
        <div class="legend-item"><div class="color-box type"></div> Types</div>
        <div class="legend-item"><div class="color-box logic"></div> Control Flow</div>
        <div class="legend-item"><div class="color-box function"></div> Functions</div>
        <div class="legend-item"><div class="color-box oop"></div> OOP</div>
        <div class="legend-item"><div class="color-box iter"></div> Iteration & Tools</div>
        <div class="legend-item"><div class="color-box module"></div> Stdlib Modules</div>
    </div>'''

    final_html = render_sheet_html(__file__, title, legend_html, content_html)
    write_sheet_output(__file__, 'python_cheat_sheet.html', final_html)


if __name__ == '__main__':
    main()

