import html
import re
import os
import urllib.parse

# --- DATA SECTION: Add or update keywords here ---
KEYWORDS_DATA = [
    {
        "section": "1. Core Essentials",
        "categories": [
            {
                "label": "Fundamental Types",
                "items": [
                    {"kw": "number", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "Numeric values (integers & floats)", "code": "let n: number = 42;"},
                    {"kw": "string", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "Text strings", "code": "let s: string = 'hello';"},
                    {"kw": "boolean", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "true / false", "code": "let ok: boolean = true;"},
                    {"kw": "bigint", "cat": "type", "ver": "ES2020 / TS 3.2", "head": "Built-in", "desc": "Arbitrary-size integers", "code": "let bi: bigint = 123n;"},
                    {"kw": "symbol", "cat": "type", "ver": "ES2015 / TS 2.7", "head": "Built-in", "desc": "Unique opaque identifier", "code": "let sym: symbol = Symbol('id');"},
                    {"kw": "any", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "Opt-out of type checking", "code": "let v: any = JSON.parse(s);"},
                    {"kw": "unknown", "cat": "type", "ver": "TS 3.0", "head": "Built-in", "desc": "Type-safe unknown value", "code": "let u: unknown = fetchVal();"},
                    {"kw": "never", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "Impossible value (e.g., function always throws)", "code": "function fail(): never { throw new Error(''); }"},
                    {"kw": "void", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "No usable return value", "code": "function log(): void { console.log('hi'); }"},
                ]
            },
            {
                "label": "Control Flow",
                "items": [
                    {"kw": "if / else", "cat": "logic", "ver": "JS", "head": "Built-in", "desc": "Conditional branching", "code": "if (x > 0) { } else { }"},
                    {"kw": "switch", "cat": "logic", "ver": "JS", "head": "Built-in", "desc": "Multi-way branch", "code": "switch (v) { case 1: break; }"},
                    {"kw": "for / while / do", "cat": "logic", "ver": "JS", "head": "Built-in", "desc": "Loop constructs", "code": "for (let i = 0; i < 5; i++) { }"},
                    {"kw": "break / continue / return", "cat": "logic", "ver": "JS", "head": "Built-in", "desc": "Flow control statements", "code": "return value;"},
                ]
            },
            {
                "label": "Functions & Modules",
                "items": [
                    {"kw": "function", "cat": "function", "ver": "JS", "head": "Built-in", "desc": "Named function declaration", "code": "function add(a: number, b: number): number { return a + b; }"},
                    {"kw": "=> (arrow)", "cat": "function", "ver": "ES2015", "head": "Built-in", "desc": "Arrow function shorthand", "code": "const f = (x: number) => x + 1;"},
                    {"kw": "async / await", "cat": "concurrency", "ver": "ES2017", "head": "Built-in", "desc": "Async functions using Promises", "code": "async function fetchData() { await fetch(url); }"},
                    {"kw": "import / export", "cat": "module", "ver": "ES2015", "head": "Built-in", "desc": "Module import/export syntax", "code": "import { readFile } from 'fs'; export function x() {}"},
                ]
            },
            {
                "label": "Type System & Annotations",
                "items": [
                    {"kw": "type / interface", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "Type aliases and interfaces", "code": "type Point = { x: number; y: number }; interface I { id: string }"},
                    {"kw": "readonly / public / private / protected / abstract / static", "cat": "modifier", "ver": "TS 1.0", "head": "Built-in", "desc": "Class member modifiers", "code": "class C { public readonly x: number; private y: string; static z = 1; }"},
                    {"kw": "generics <T>", "cat": "generic", "ver": "TS 1.0", "head": "Built-in", "desc": "Parameterize types and functions", "code": "function id<T>(x: T): T { return x; }"},
                    {"kw": "union | / intersection &", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "Combine or intersect types", "code": "type U = A | B; type I = A & B;"},
                    {"kw": "type assertion (as) / <>", "cat": "type", "ver": "TS 1.0", "head": "Built-in", "desc": "Assert a more specific type", "code": "const len = (x as string).length;"},
                ]
            }
        ]
    },
    {
        "section": "2. Advanced & Ecosystem",
        "is_advanced": True,
        "categories": [
            {
                "label": "Advanced Types & Utilities",
                "items": [
                    {"kw": "Mapped Types / Conditional Types / keyof / typeof / infer", "cat": "advanced", "ver": "TS 2.x", "head": "Built-in", "desc": "Type-level computation and transforms", "code": "type ReadOnly<T> = { readonly [K in keyof T]: T[K] }"},
                    {"kw": "Utility Types (Partial, Required, Readonly, Pick, Omit)", "cat": "utility", "ver": "TS 2.1", "head": "lib.d.ts", "desc": "Common helper types provided by TS", "code": "type P = Partial<MyType>;"},
                    {"kw": "type guards / instanceof / typeof / user-defined is", "cat": "guards", "ver": "TS 1.0", "head": "Built-in", "desc": "Narrow types at runtime", "code": "if (typeof x === 'string') { x.toUpperCase(); }"},
                ]
            },
            {
                "label": "Decorators & Metadata",
                "items": [
                    {"kw": "@decorator", "cat": "meta", "ver": "experimental", "head": "Experimental", "desc": "Decorators for classes and members (requires enable)", "code": "@sealed\nclass C {}"},
                ]
            },
            {
                "label": "Tooling & Config",
                "items": [
                    {"kw": "tsconfig.json", "cat": "tooling", "ver": "N/A", "head": "config", "desc": "Compiler and project configuration", "code": "{ \"compilerOptions\": { \"strict\": true } }"},
                    {"kw": "tsc / ts-node / tsc --build", "cat": "tooling", "ver": "N/A", "head": "tooling", "desc": "Compile/run TypeScript", "code": "npx tsc --build"},
                    {"kw": "declaration .d.ts files", "cat": "interop", "ver": "N/A", "head": "typing", "desc": "Provide typings for JS libs", "code": "declare module 'foo';"},
                ]
            }
        ]
    },
    {
        "section": "3. Standard Library Highlights (Non-Keywords)",
        "is_library": True,
        "categories": [
            {
                "label": "Built-ins & DOM / ES APIs",
                "items": [
                    {"kw": "Promise", "cat": "global", "ver": "ES2015", "head": "Global", "desc": "Asynchronous value container", "code": "Promise.resolve(42)"},
                    {"kw": "Array / Map / Set / WeakMap / WeakSet", "cat": "global", "ver": "ES2015", "head": "Global", "desc": "Core JS collections", "code": "const m = new Map<string, number>();"},
                    {"kw": "ReadonlyArray / Tuple", "cat": "global", "ver": "TS 1.0", "head": "Built-in", "desc": "Immutable array types and tuple types", "code": "const t: [string, number] = ['a', 1];"},
                    {"kw": "DOM types (Document, Element, Event)", "cat": "dom", "ver": "lib.dom", "head": "lib.dom.d.ts", "desc": "Browser DOM API typings", "code": "document.querySelector('div')"},
                ]
            }
        ]
    }
]

# Use shared sheet_template.html for layout/CSS


def build_doc_url(item):
    """Create a helpful TypeScript docs URL; fallback to site search."""
    kw = item.get('kw', '')
    key = kw.split()[0].strip().strip('/,()<>')
    basic_types = {'number', 'string', 'boolean', 'bigint', 'symbol', 'any', 'unknown', 'never', 'void'}
    if key in basic_types:
        return 'https://www.typescriptlang.org/docs/handbook/basic-types.html'

    if 'interface' in key.lower():
        return 'https://www.typescriptlang.org/docs/handbook/interfaces.html'
    if 'class' in key.lower():
        return 'https://www.typescriptlang.org/docs/handbook/classes.html'
    if 'generic' in kw.lower() or '<T>' in kw:
        return 'https://www.typescriptlang.org/docs/handbook/2/generics.html'
    if 'utility' in kw.lower() or 'partial' in kw.lower() or 'readonly' in kw.lower():
        return 'https://www.typescriptlang.org/docs/handbook/utility-types.html'

    # tool/config links
    if key == 'tsconfig.json' or 'tsconfig' in key:
        return 'https://www.typescriptlang.org/tsconfig'

    # fallback to site search
    return f"https://www.typescriptlang.org/search?q={urllib.parse.quote(kw)}"


def generate_table(section):
    rows = []
    for cat in section['categories']:
        rows.append(f'<tr class="category-label"><td colspan="4">{html.escape(cat["label"])}</td></tr>')
        for item in cat['items']:
            url = build_doc_url(item)
            header_class = 'header-note' if item.get('head', '') not in ('Built-in', '') else ''
            desc_text = item.get('desc', '')
            dep_match = re.search(r"\([^)]*deprecated[^)]*\)", desc_text, re.I)
            deprecated_html = ''
            if dep_match:
                dep_text = dep_match.group(0).strip()
                desc_text = desc_text.replace(dep_match.group(0), '').strip()
                deprecated_html = f' <span class="header-note">{html.escape(dep_text)}</span>'
            version_html = f' <span class="version-tag">(since {item.get("ver", "")})</span>' if item.get('ver') else ''
            desc_escaped = html.escape(desc_text)

            row = f"""
            <tr class="{html.escape(item.get('cat',''))}">
                <td><a href="{url}" target="_blank">{html.escape(item['kw'])}</a></td>
                <td>{desc_escaped}{deprecated_html}{version_html}</td>
                <td><span class="{header_class}">{html.escape(item.get('head',''))}</span></td>
                <td><code>{html.escape(item.get('code',''))}</code></td>
            </tr>
            """
            rows.append(row)

    return f"""
    <h2>{html.escape(section['section'])}</h2>
    <table>
        <thead>
            <tr>
                <th style="width: 18%;">Item</th>
                <th style="width: 42%;">Description & Version</th>
                <th style="width: 15%;">Context</th>
                <th style="width: 25%;">Snippet</th>
            </tr>
        </thead>
        <tbody>
            {''.join(rows)}
        </tbody>
    </table>
    """


def main():
    content_blocks = []
    for section in KEYWORDS_DATA:
        if section.get('is_advanced'):
            content_blocks.append('<div class="separator"><span>Advanced & Ecosystem</span></div>')
        content_blocks.append(generate_table(section))

    content_html = ''.join(content_blocks)
    title = 'TypeScript Polyglot Dev Atlas'
    legend_html = '''<div class="legend-row">
        <div class="legend-item"><div class="color-box type"></div> Types & Interfaces</div>
        <div class="legend-item"><div class="color-box logic"></div> Control Flow</div>
        <div class="legend-item"><div class="color-box function"></div> Functions</div>
        <div class="legend-item"><div class="color-box module"></div> Modules</div>
        <div class="legend-item"><div class="color-box generic"></div> Generics</div>
        <div class="legend-item"><div class="color-box modifier"></div> Modifiers</div>
        <div class="legend-item"><div class="color-box advanced"></div> Advanced / Utility</div>
        <div class="legend-item"><div class="color-box tooling"></div> Tooling / Config</div>
        <div class="legend-item"><div class="color-box dom"></div> DOM & Global APIs</div>
    </div>'''

    tpl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'sheet_template.html'))
    with open(tpl_path, 'r', encoding='utf-8') as tplf:
        tpl = tplf.read()
    final_html = tpl.replace('__TITLE__', title).replace('__LEGEND__', legend_html).replace('__CONTENT__', content_html)

    out_dir = os.path.dirname(__file__)
    out_path = os.path.join(out_dir, 'typescript_cheat_sheet.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Successfully generated {out_path}")


if __name__ == '__main__':
    main()

