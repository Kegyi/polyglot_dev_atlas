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
                    {"kw": "Byte", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "8-bit signed integer", "code": "val b: Byte = 1"},
                    {"kw": "Short", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "16-bit signed integer", "code": "val s: Short = 2"},
                    {"kw": "Int", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "32-bit signed integer", "code": "val i: Int = 42"},
                    {"kw": "Long", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "64-bit signed integer", "code": "val l: Long = 123456789L"},
                    {"kw": "Float", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "32-bit floating point", "code": "val f: Float = 3.14f"},
                    {"kw": "Double", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "64-bit floating point", "code": "val d: Double = 2.71828"},
                    {"kw": "Char", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "16-bit Unicode code unit", "code": "val c: Char = 'A'"},
                    {"kw": "Boolean", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "true / false", "code": "val ok: Boolean = true"},
                    {"kw": "String", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "Immutable sequence of characters", "code": "val s: String = \"hello\""},
                    {"kw": "Unit", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "No meaningful value (like void)", "code": "def f(): Unit = println(\"hi\")"},
                    {"kw": "Any / AnyVal / AnyRef", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "Top types and value/reference hierarchy", "code": "val x: Any = 1"},
                    {"kw": "Null / Nothing", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "Null vs bottom type (Nothing)", "code": "def fail(): Nothing = throw new RuntimeException(\"boom\")"},
                ]
            },
            {
                "label": "Control Flow",
                "items": [
                    {"kw": "if / else", "cat": "logic", "ver": "Scala 2/3", "head": "Built-in", "desc": "Conditional expression (returns value)", "code": "val r = if (x > 0) \"pos\" else \"neg\""},
                    {"kw": "match", "cat": "logic", "ver": "Scala 2/3", "head": "Built-in", "desc": "Pattern matching expression", "code": "x match { case 0 => \"zero\"; case n => s\"$n\" }"},
                    {"kw": "for (comprehension)", "cat": "logic", "ver": "Scala 2/3", "head": "Built-in", "desc": "Comprehensions with map/flatMap/filter", "code": "for (i <- 0 until 3) yield i * 2"},
                    {"kw": "while / do-while", "cat": "logic", "ver": "Scala 2/3", "head": "Built-in", "desc": "Loop constructs (used less in idiomatic Scala)", "code": "while (cond) { doSomething() }"},
                    {"kw": "return", "cat": "logic", "ver": "Scala 2/3", "head": "Built-in", "desc": "Return from method (rare in idiomatic code)", "code": "return value"},
                ]
            },
            {
                "label": "Definitions & OOP",
                "items": [
                    {"kw": "val", "cat": "decl", "ver": "Scala 2/3", "head": "Built-in", "desc": "Immutable binding", "code": "val x = 10"},
                    {"kw": "var", "cat": "decl", "ver": "Scala 2/3", "head": "Built-in", "desc": "Mutable variable", "code": "var i = 0; i += 1"},
                    {"kw": "def", "cat": "decl", "ver": "Scala 2/3", "head": "Built-in", "desc": "Method or function definition", "code": "def add(a: Int, b: Int): Int = a + b"},
                    {"kw": "class / case class", "cat": "oop", "ver": "Scala 2/3", "head": "Built-in", "desc": "Class and pattern-friendly case class", "code": "case class Person(name: String, age: Int)"},
                    {"kw": "object", "cat": "oop", "ver": "Scala 2/3", "head": "Built-in", "desc": "Singleton object (module)", "code": "object Main { def main(args: Array[String]): Unit = println(\"hi\") }"},
                    {"kw": "trait", "cat": "oop", "ver": "Scala 2/3", "head": "Built-in", "desc": "Interface-like behavior + defaults", "code": "trait Logger { def log(s: String): Unit }"},
                    {"kw": "extends / with / override", "cat": "oop", "ver": "Scala 2/3", "head": "Built-in", "desc": "Inheritance and mixins", "code": "class C extends Base with Trait { override def m() = {} }"},
                    {"kw": "new", "cat": "oop", "ver": "Scala 2/3", "head": "Built-in", "desc": "Instantiate classes", "code": "val p = new Person(\"A\", 30)"},
                ]
            },
            {
                "label": "Functional Tools",
                "items": [
                    {"kw": "=> (lambda)", "cat": "functional", "ver": "Scala 2/3", "head": "Built-in", "desc": "Anonymous function / lambda", "code": "val f = (x: Int) => x + 1"},
                    {"kw": "map / flatMap / filter / foreach", "cat": "functional", "ver": "Scala 2/3", "head": "scala.collection", "desc": "Common collection operations", "code": "List(1,2,3).map(_ * 2)"},
                    {"kw": "Option / Some / None / getOrElse", "cat": "functional", "ver": "Scala 2/3", "head": "scala", "desc": "Handle optional values without nulls", "code": "opt.getOrElse(default)"},
                    {"kw": "Either / Left / Right", "cat": "functional", "ver": "Scala 2/3", "head": "scala.util", "desc": "Two-sided result type for errors", "code": "Right(42)"},
                ]
            },
            {
                "label": "Concurrency & Futures",
                "items": [
                    {"kw": "scala.concurrent.Future", "cat": "concurrency", "ver": "Scala 2.10+", "head": "scala.concurrent", "desc": "Asynchronous computation with ExecutionContext", "code": "import scala.concurrent.Future\nimport scala.concurrent.ExecutionContext.Implicits.global\nval f = Future { compute() }"},
                    {"kw": "Await / Promise", "cat": "concurrency", "ver": "Scala 2.10+", "head": "scala.concurrent", "desc": "Wait for future or create Promise", "code": "import scala.concurrent.Await\nAwait.result(f, scala.concurrent.duration.Duration.Inf)"},
                ]
            }
        ]
    },
    {
        "section": "2. Advanced & Ecosystem",
        "is_advanced": True,
        "categories": [
            {
                "label": "Collections & Immutability",
                "items": [
                    {"kw": "Seq / List / Vector / Array", "cat": "collection", "ver": "Scala 2/3", "head": "scala.collection", "desc": "Common sequence types (immutable by default)", "code": "val v: Seq[Int] = List(1,2,3)"},
                    {"kw": "Map / Set", "cat": "collection", "ver": "Scala 2/3", "head": "scala.collection", "desc": "Associative containers and sets", "code": "Map(\"a\" -> 1)"},
                    {"kw": "mutable vs immutable collections", "cat": "collection", "ver": "Scala 2/3", "head": "scala.collection", "desc": "Prefer immutable by default", "code": "import scala.collection.mutable.ArrayBuffer"},
                ]
            },
            {
                "label": "Type System & Generics",
                "items": [
                    {"kw": "Generics / [T]", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "Parametric polymorphism", "code": "class Box[T](val value: T)"},
                    {"kw": "implicit (Scala 2) / given (Scala 3)", "cat": "type", "ver": "Scala 2/3", "head": "language", "desc": "Contextual parameters / type class instances", "code": "given intOrd: Ordering[Int] with { def compare(a,b) = a - b }"},
                    {"kw": "type alias / abstract type", "cat": "type", "ver": "Scala 2/3", "head": "Built-in", "desc": "Create synonyms or abstract members", "code": "type StrMap = Map[String, String]"},
                ]
            },
            {
                "label": "Interop & Build",
                "items": [
                    {"kw": "sbt / Mill / Scala CLI", "cat": "tooling", "ver": "N/A", "head": "external", "desc": "Build tools for Scala projects", "code": "sbt run"},
                    {"kw": "Java interop", "cat": "interop", "ver": "Scala 2/3", "head": "Built-in", "desc": "Call Java libraries directly", "code": "val j = new java.util.ArrayList[String]()"},
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
                    {"kw": "scala.collection", "cat": "module", "ver": "Scala 2/3", "head": "scala.collection", "desc": "Collection interfaces and implementations", "code": "import scala.collection._"},
                    {"kw": "scala.concurrent", "cat": "module", "ver": "Scala 2.10+", "head": "scala.concurrent", "desc": "Futures, Promise and utilities", "code": "import scala.concurrent._"},
                    {"kw": "scala.util.Try / Success / Failure", "cat": "module", "ver": "Scala 2.10+", "head": "scala.util", "desc": "Error handling without exceptions", "code": "Try { risky() } match { case Success(v) => v }"},
                    {"kw": "scala.io.Source", "cat": "module", "ver": "Scala 2/3", "head": "scala.io", "desc": "Read files and resources", "code": "val s = scala.io.Source.fromFile(\"file.txt\").mkString"},
                ]
            }
        ]
    }
]

# Use shared sheet_template.html as single source-of-truth for layout/CSS


def build_doc_url(item):
    """Create a helpful docs URL for each Scala item, with a search fallback."""
    kw = item.get('kw', '')
    head = item.get('head', '')

    explicit_links = {
        'def': 'https://docs.scala-lang.org/tour/basics.html#methods',
        'val': 'https://docs.scala-lang.org/tour/basics.html#values',
        'var': 'https://docs.scala-lang.org/tour/basics.html#values',
        'if / else': 'https://docs.scala-lang.org/tour/basics.html#if-expressions',
        'match': 'https://docs.scala-lang.org/tour/pattern-matching.html',
        'for (comprehension)': 'https://docs.scala-lang.org/tour/for-comprehensions.html',
        'while / do-while': 'https://docs.scala-lang.org/overviews/scala-book/while-loops.html',
        'return': 'https://docs.scala-lang.org/tour/basics.html#methods',
        'class / case class': 'https://docs.scala-lang.org/tour/case-classes.html',
        'object': 'https://docs.scala-lang.org/tour/singleton-objects.html',
        'trait': 'https://docs.scala-lang.org/tour/traits.html',
        'extends / with / override': 'https://docs.scala-lang.org/tour/traits.html',
        'new': 'https://docs.scala-lang.org/tour/classes.html',
        '=> (lambda)': 'https://docs.scala-lang.org/tour/anonymous-functions.html',
        'Option / Some / None / getOrElse': 'https://docs.scala-lang.org/overviews/scala-book/no-null-values.html',
        'Either / Left / Right': 'https://docs.scala-lang.org/overviews/scala-book/functional-error-handling.html',
        'scala.concurrent.Future': 'https://docs.scala-lang.org/overviews/core/futures.html',
        'Await / Promise': 'https://docs.scala-lang.org/overviews/core/futures.html',
        'Generics / [T]': 'https://docs.scala-lang.org/tour/generic-classes.html',
        'implicit (Scala 2) / given (Scala 3)': 'https://docs.scala-lang.org/scala3/book/ca-context-parameters.html',
        'type alias / abstract type': 'https://docs.scala-lang.org/tour/abstract-type-members.html',
        'Java interop': 'https://docs.scala-lang.org/scala3/book/interacting-with-java.html',
    }

    if kw in explicit_links:
        return explicit_links[kw]

    # if the head explicitly references scala packages, link to API root
    if head and head.lower().startswith('scala'):
        return 'https://www.scala-lang.org/api/current/'

    if head == 'Built-in':
        return 'https://docs.scala-lang.org/tour/basics.html'

    # common tooling
    if head == 'external' and 'sbt' in kw.lower():
        return 'https://www.scala-sbt.org/'

    # fallback: site search
    return f"https://www.scala-lang.org/search?q={urllib.parse.quote(kw)}"


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
    title = 'Scala Polyglot Dev Atlas'
    legend_html = '''<div class="legend-row">
        <div class="legend-item"><div class="color-box type"></div> Types</div>
        <div class="legend-item"><div class="color-box logic"></div> Control Flow</div>
        <div class="legend-item"><div class="color-box functional"></div> Functional</div>
        <div class="legend-item"><div class="color-box oop"></div> OOP & Traits</div>
        <div class="legend-item"><div class="color-box concurrency"></div> Concurrency</div>
        <div class="legend-item"><div class="color-box module"></div> Stdlib</div>
    </div>'''

    tpl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'sheet_template.html'))
    with open(tpl_path, 'r', encoding='utf-8') as tplf:
        tpl = tplf.read()
    final_html = tpl.replace('__TITLE__', title).replace('__LEGEND__', legend_html).replace('__CONTENT__', content_html)

    # Produce a generic sheet and explicit Scala 2 / Scala 3 variants. The
    # variants simply adjust version labels where the data contains "Scala 2/3".
    final_html_scala2 = final_html.replace('Scala 2/3', 'Scala 2')
    final_html_scala3 = final_html.replace('Scala 2/3', 'Scala 3')

    out_dir = os.path.dirname(__file__)
    # generic (legacy)
    out_path = os.path.join(out_dir, 'scala_cheat_sheet.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Successfully generated {out_path}")

    # explicit Scala 2 page
    out_path2 = os.path.join(out_dir, 'scala2_cheat_sheet.html')
    html2 = final_html_scala2.replace('<h1>Scala Polyglot Dev Atlas</h1>', '<h1>Scala Polyglot Dev Atlas - Scala 2</h1>\n<div class="version-note">Note: this page targets Scala 2 syntax where it differs from Scala 3.</div>')
    with open(out_path2, 'w', encoding='utf-8') as f:
        f.write(html2)
    print(f"Successfully generated {out_path2}")

    # explicit Scala 3 page
    out_path3 = os.path.join(out_dir, 'scala3_cheat_sheet.html')
    html3 = final_html_scala3.replace('<h1>Scala Polyglot Dev Atlas</h1>', '<h1>Scala Polyglot Dev Atlas - Scala 3</h1>\n<div class="version-note">Note: this page targets Scala 3 (Dotty) syntax where it differs from Scala 2.</div>')
    with open(out_path3, 'w', encoding='utf-8') as f:
        f.write(html3)
    print(f"Successfully generated {out_path3}")


if __name__ == '__main__':
    main()

