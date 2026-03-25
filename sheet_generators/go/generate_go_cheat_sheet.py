import html
import re
import os
import urllib.parse

# --- DATA SECTION: Add or update keywords here ---
KEYWORDS_DATA = [
    {
        "section": "1. Core Keywords & Types",
        "categories": [
            {
                "label": "Fundamental Types",
                "items": [
                    {"kw": "bool", "cat": "type", "ver": "Go 1", "head": "Built-in", "desc": "Boolean type (true/false)", "code": "var b bool = true"},
                    {"kw": "string", "cat": "type", "ver": "Go 1", "head": "Built-in", "desc": "Immutable UTF-8 string", "code": "s := \"hello\""},
                    {"kw": "int / int8 / int16 / int32 / int64", "cat": "type", "ver": "Go 1", "head": "Built-in", "desc": "Signed integer types", "code": "var n int = 42\nvar i8 int8 = -1"},
                    {"kw": "uint / byte / rune", "cat": "type", "ver": "Go 1", "head": "Built-in", "desc": "Unsigned integer / alias types (byte=rune)", "code": "var u uint = 7\nvar r rune = 'ä¸–'"},
                    {"kw": "float32 / float64", "cat": "type", "ver": "Go 1", "head": "Built-in", "desc": "Floating point numbers", "code": "var f float64 = 3.14"},
                    {"kw": "complex64 / complex128", "cat": "type", "ver": "Go 1", "head": "Built-in", "desc": "Complex number types", "code": "z := complex(1, 2)"},
                ]
            },
            {
                "label": "Declarations & Basics",
                "items": [
                    {"kw": "package", "cat": "decl", "ver": "Go 1", "head": "Built-in", "desc": "Define package name for the file", "code": "package main"},
                    {"kw": "import", "cat": "decl", "ver": "Go 1", "head": "Built-in", "desc": "Import packages", "code": "import \"fmt\""},
                    {"kw": "var", "cat": "decl", "ver": "Go 1", "head": "Built-in", "desc": "Declare variables", "code": "var x int = 5"},
                    {"kw": "const", "cat": "decl", "ver": "Go 1", "head": "Built-in", "desc": "Declare constants", "code": "const Pi = 3.14159"},
                    {"kw": "type", "cat": "decl", "ver": "Go 1", "head": "Built-in", "desc": "Define new types", "code": "type Point struct { X, Y int }"},
                    {"kw": "func", "cat": "decl", "ver": "Go 1", "head": "Built-in", "desc": "Define a function", "code": "func Add(a, b int) int { return a + b }"},
                    {"kw": ":=", "cat": "decl", "ver": "Go 1", "head": "Built-in", "desc": "Short variable declaration and type inference", "code": "x := 10"},
                ]
            },
            {
                "label": "Control Flow",
                "items": [
                    {"kw": "if / else", "cat": "logic", "ver": "Go 1", "head": "Built-in", "desc": "Conditional branching", "code": "if x > 0 {\n    // ...\n} else {\n    // ...\n}"},
                    {"kw": "for / range", "cat": "logic", "ver": "Go 1", "head": "Built-in", "desc": "Looping (Go's only loop)", "code": "for i := 0; i < 5; i++ { }\nfor i, v := range slice { }"},
                    {"kw": "switch / case", "cat": "logic", "ver": "Go 1", "head": "Built-in", "desc": "Multi-way branch (supports type switches)", "code": "switch x { case 1: \n    // ...\n}"},
                    {"kw": "select", "cat": "concurrency", "ver": "Go 1", "head": "Built-in", "desc": "Wait on multiple channel operations", "code": "select { case v := <-ch: \n    _ = v\n}"},
                    {"kw": "defer", "cat": "logic", "ver": "Go 1", "head": "Built-in", "desc": "Schedule call to run when function returns", "code": "defer file.Close()"},
                    {"kw": "goto / break / continue / fallthrough", "cat": "logic", "ver": "Go 1", "head": "Built-in", "desc": "Loop and flow control primitives", "code": "break\ncontinue\nfallthrough"},
                ]
            },
            {
                "label": "Memory & Pointers",
                "items": [
                    {"kw": "new", "cat": "memory", "ver": "Go 1", "head": "Built-in", "desc": "Allocate zeroed storage and return pointer", "code": "p := new(int)"},
                    {"kw": "make", "cat": "memory", "ver": "Go 1", "head": "Built-in", "desc": "Create slices, maps, and channels", "code": "s := make([]int, 0, 10)\nm := make(map[string]int)\nch := make(chan int)"},
                    {"kw": "& / *", "cat": "memory", "ver": "Go 1", "head": "Built-in", "desc": "Address-of and pointer dereference", "code": "p := &x\n*x = 10"},
                    {"kw": "nil", "cat": "memory", "ver": "Go 1", "head": "Built-in", "desc": "Zero value for pointers, channels, maps, slices, interfaces", "code": "var p *int = nil"},
                ]
            }
        ]
    },
    {
        "section": "2. Concurrency & Advanced",
        "is_advanced": True,
        "categories": [
            {
                "label": "Goroutines & Channels",
                "items": [
                    {"kw": "go", "cat": "concurrency", "ver": "Go 1", "head": "Built-in", "desc": "Start a new goroutine (lightweight thread)", "code": "go doWork()"},
                    {"kw": "chan", "cat": "concurrency", "ver": "Go 1", "head": "Built-in", "desc": "Channel type for communication between goroutines", "code": "ch := make(chan int)\nch <- 1\nv := <-ch"},
                    {"kw": "close", "cat": "concurrency", "ver": "Go 1", "head": "builtin", "desc": "Close a channel when no more values will be sent", "code": "close(ch)"},
                ]
            },
            {
                "label": "Synchronization",
                "items": [
                    {"kw": "sync.Mutex / sync.RWMutex", "cat": "sync", "ver": "Go 1", "head": "sync", "desc": "Mutual exclusion locks", "code": "var mu sync.Mutex\nmu.Lock()\nmu.Unlock()"},
                    {"kw": "sync.WaitGroup", "cat": "sync", "ver": "Go 1", "head": "sync", "desc": "Wait for a collection of goroutines to finish", "code": "var wg sync.WaitGroup\nwg.Add(1)\ngo func() { defer wg.Done(); ... }()\nwg.Wait()"},
                    {"kw": "context.Context", "cat": "sync", "ver": "Go 1.7", "head": "context", "desc": "Cancellation, deadlines and request-scoped values", "code": "ctx, cancel := context.WithTimeout(context.Background(), time.Second)\ndefer cancel()"},
                ]
            },
            {
                "label": "Interfaces & Types",
                "items": [
                    {"kw": "interface", "cat": "oop", "ver": "Go 1", "head": "Built-in", "desc": "Define behavior via method set", "code": "type Reader interface { Read(p []byte) (n int, err error) }"},
                    {"kw": "struct / methods", "cat": "oop", "ver": "Go 1", "head": "Built-in", "desc": "Block of fields + methods on types", "code": "type S struct { A int }\nfunc (s *S) M() {}"},
                    {"kw": "embedding", "cat": "oop", "ver": "Go 1", "head": "Built-in", "desc": "Compose types by embedding struct/types", "code": "type T struct { S }"},
                ]
            }
        ]
    },
    {
        "section": "3. Standard Library Highlights (Non-Keywords)",
        "is_library": True,
        "categories": [
            {
                "label": "Common Packages",
                "items": [
                    {"kw": "fmt", "cat": "module", "ver": "Go 1", "head": "fmt", "desc": "Formatted I/O (Print, Sprintf)", "code": "fmt.Println(\"hello\")"},
                    {"kw": "net/http", "cat": "module", "ver": "Go 1", "head": "net/http", "desc": "HTTP client and server", "code": "http.ListenAndServe(\":8080\", handler)"},
                    {"kw": "io / io/ioutil", "cat": "module", "ver": "Go 1", "head": "io", "desc": "I/O primitives and helpers", "code": "io.Copy(dst, src)"},
                    {"kw": "encoding/json", "cat": "module", "ver": "Go 1", "head": "encoding/json", "desc": "JSON marshal/unmarshal", "code": "json.Unmarshal(data, &v)"},
                    {"kw": "sync", "cat": "module", "ver": "Go 1", "head": "sync", "desc": "Concurrency primitives (Mutex, WaitGroup)", "code": "var mu sync.Mutex"},
                    {"kw": "time", "cat": "module", "ver": "Go 1", "head": "time", "desc": "Time, timers, sleeping", "code": "time.Sleep(time.Second)"},
                    {"kw": "context", "cat": "module", "ver": "Go 1.7", "head": "context", "desc": "Cancellation and deadlines", "code": "ctx := context.Background()"},
                ]
            }
        ]
    }
]

# Sheet now rendered from shared sheet_template.html


def build_doc_url(item):
    kw = item.get('kw', '')
    head = item.get('head', '')
    # map common builtins to builtin package anchors
    builtins = {'append', 'cap', 'close', 'complex', 'copy', 'imag', 'len', 'make', 'new', 'panic', 'recover', 'real', 'delete'}
    first = kw.split()[0].strip().strip('/,()')
    lower = first.lower()
    if lower in builtins:
        return f'https://pkg.go.dev/builtin#{lower}'

    # keywords and language constructs -> spec
    keywords = {'if', 'for', 'switch', 'select', 'defer', 'go', 'range', 'return', 'goto', 'fallthrough'}
    if lower in keywords:
        return 'https://go.dev/ref/spec'

    # if head names a standard package, link to its docs on pkg.go.dev
    head_module = head.split()[0].strip().strip('<>,')
    common_modules = ['fmt', 'net/http', 'io', 'encoding/json', 'context', 'sync', 'time', 'os', 'path/filepath', 'regexp']
    if head_module in common_modules:
        # allow module names like net/http
        return f'https://pkg.go.dev/{head_module}'

    # fallback: search pkg.go.dev
    return f'https://pkg.go.dev/search?q={urllib.parse.quote(kw)}'


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
            content_blocks.append('<div class="separator"><span>Advanced & Concurrency</span></div>')
        content_blocks.append(generate_table(section))

    content_html = ''.join(content_blocks)
    title = 'Go Polyglot Dev Atlas'
    legend_html = '''<div class="legend-row">
        <div class="legend-item"><div class="color-box syntax"></div> Syntax</div>
        <div class="legend-item"><div class="color-box concurrency"></div> Concurrency</div>
        <div class="legend-item"><div class="color-box module"></div> Stdlib & Tools</div>
    </div>'''

    tpl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'sheet_template.html'))
    with open(tpl_path, 'r', encoding='utf-8') as tplf:
        tpl = tplf.read()
    final_html = tpl.replace('__TITLE__', title).replace('__LEGEND__', legend_html).replace('__CONTENT__', content_html)

    out_dir = os.path.dirname(__file__)
    out_path = os.path.join(out_dir, 'go_cheat_sheet.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Successfully generated {out_path}")


if __name__ == '__main__':
    main()

