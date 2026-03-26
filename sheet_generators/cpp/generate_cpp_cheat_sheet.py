import os
import sys

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
# Categories: type, logic, storage, oop, memory, modern, template, system
KEYWORDS_DATA = [
    {
        "section": "1. Core Essentials",
        "categories": [
            {
                "label": "Fundamental Types",
                "items": [
                    {"kw": "bool", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "True or false values", "code": "bool isActive = true;"},
                    {"kw": "int", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "Standard integer", "code": "int count = 42;"},
                    {"kw": "short", "cat": "type", "ver": "C++98", "head": "<limits>", "desc": "Small integer (at least 16 bits per standard; actual width is implementation-defined)", "code": "short smallNum = 32767; // check with std::numeric_limits<short>::max()"},
                    {"kw": "long", "cat": "type", "ver": "C++98", "head": "<limits>", "desc": "Large integer (at least 32 bits per standard; actual width is implementation-defined)", "code": "long bigNum = 2147483647L; // check with std::numeric_limits<long>::max()"},
                    {"kw": "long long", "cat": "type", "ver": "C++11", "head": "Built-in", "desc": "Extended large integer (at least 64-bit)", "code": "long long bigNum64 = 9223372036854775807LL;"},
                    {"kw": "unsigned long long", "cat": "type", "ver": "C++11", "head": "Built-in", "desc": "Non-negative large integer", "code": "unsigned long long ubig = 18446744073709551615ULL;"},
                    {"kw": "signed", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "Can hold negative/positive", "code": "signed int temperature = -5;"},
                    {"kw": "char", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "Character type", "code": "char grade = 'A';"},
                    {"kw": "char8_t", "cat": "type", "ver": "C++20", "head": "Built-in", "desc": "UTF-8 code unit", "code": "char8_t c = u8\"A\"[0]; // C++20"},
                    {"kw": "char16_t", "cat": "type", "ver": "C++11", "head": "Built-in", "desc": "UTF-16 code unit", "code": "char16_t u16 = u'A';"},
                    {"kw": "char32_t", "cat": "type", "ver": "C++11", "head": "Built-in", "desc": "UTF-32 code unit", "code": "char32_t u32 = U'A';"},
                    {"kw": "wchar_t", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "Wide character type", "code": "wchar_t wc = L'A';"},
                    {"kw": "double", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "High-precision float", "code": "double pi = 3.14159;"},
                    {"kw": "float", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "Single-precision float", "code": "float temp = 98.6f;"},
                    {"kw": "void", "cat": "type", "ver": "C++98", "head": "Built-in", "desc": "Indicates no value/type", "code": "void printMessage();"},
                ]
            },
            {
                "label": "Control Flow",
                "items": [
                    {"kw": "if", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Execute if condition true", "code": "if (x > 10) { ... }"},
                    {"kw": "else", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alternative branch for if", "code": "else { doSomething(); }"},
                    {"kw": "switch", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Multi-way branch logic", "code": "switch(day) { ... }"},
                    {"kw": "for", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Standard iteration loop", "code": "for(int i=0; i<5; ++i)"},
                    {"kw": "range-based for", "cat": "logic", "ver": "C++11", "head": "Built-in", "desc": "Iterate over elements of a container", "code": "for (auto &e : container) { ... }"},
                    {"kw": "while", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Loop while condition is true", "code": "while(x < 100) { x++; }"},
                    {"kw": "do", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Loop executed at least once", "code": "do { x++; } while(x < 5);"},
                    {"kw": "return", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Exit and return from function", "code": "return result;"},
                    {"kw": "break", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Exit immediate loop/switch", "code": "if(error) break;"},
                    {"kw": "continue", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Skip to next loop iteration", "code": "if(skip) continue;"},
                    {"kw": "case", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Individual label in a switch", "code": "case 1: score += 10; break;"},
                    {"kw": "default", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Catch-all in a switch block", "code": "default: logError(); break;"},
                    {"kw": "goto", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Jump to a labeled statement (Avoid)", "code": "if(err) goto cleanup;"},
                ]
            },
            {
                "label": "Storage & Behavior",
                "items": [
                    {"kw": "const", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Value cannot be changed", "code": "const int MAX = 100;"},
                    {"kw": "static", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Persistent local storage", "code": "static int instances = 0;"},
                    {"kw": "volatile", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Prevent certain optimizations; used for hardware/atomic access", "code": "volatile int flag;"},
                    {"kw": "inline", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Allow inline functions/variables and one-definition across TUs", "code": "inline void f() {}"},
                    {"kw": "register", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Storage-class hint (deprecated in C++17)", "code": "register int r = 0;"},
                    {"kw": "typedef", "cat": "storage", "ver": "pre-C++11", "head": "Built-in", "desc": "Alias for a type (pre C++11)", "code": "typedef unsigned int uint;"},
                    {"kw": "unsigned", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Non-negative integers only", "code": "unsigned int score = 50;"},
                    {"kw": "extern", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Linked to another file", "code": "extern int globalVar;"},
                    {"kw": "mutable", "cat": "storage", "ver": "C++98", "head": "Built-in", "desc": "Modifiable in a const function", "code": "mutable int cacheHitCount;"},
                ]
            },
            {
                "label": "OOP & Classes",
                "items": [
                    {"kw": "class", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "User defined type (private default)", "code": "class Player { ... };"},
                    {"kw": "struct", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "User defined type (public default)", "code": "struct Point { int x, y; };"},
                    {"kw": "friend", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Allow external access to private", "code": "friend class Database;"},
                    {"kw": "explicit", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Prevent implicit conversions", "code": "explicit MyClass(int x);"},
                    {"kw": "operator", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Define custom symbol behavior", "code": "bool operator==(const Obj& x);"},
                    {"kw": "enum", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Set of named integer constants", "code": "enum Color { RED, BLUE };"},
                    {"kw": "enum class", "cat": "oop", "ver": "C++11", "head": "Built-in", "desc": "Scoped and strongly typed enumeration", "code": "enum class Color { RED, BLUE };"},
                    {"kw": "union", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Type that holds one of several members", "code": "union Data { int i; float f; };"},
                    {"kw": "public", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Accessible outside class", "code": "public: int health;"},
                    {"kw": "protected", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Accessible in class and derived classes", "code": "protected: int shield;"},
                    {"kw": "private", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Accessible only within class", "code": "private: int secretKey;"},
                    {"kw": "virtual", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Enables method overriding", "code": "virtual void attack();"},
                    {"kw": "this", "cat": "oop", "ver": "C++98", "head": "Built-in", "desc": "Pointer to current instance", "code": "this->name = \"Hero\";"},
                ]
            },
            {
                "label": "Memory & Safety",
                "items": [
                    {"kw": "new", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Allocate on heap", "code": "int* p = new int(5);"},
                    {"kw": "new[]", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Allocate array on heap", "code": "int* arr = new int[10];"},
                    {"kw": "delete", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Free heap memory", "code": "delete p;"},
                    {"kw": "delete[]", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Free dynamically allocated arrays", "code": "delete[] arr;"},
                    {"kw": "try", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Block to test for errors", "code": "try { riskyLogic(); }"},
                    {"kw": "catch", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Handle error from try block", "code": "catch(...) { recover(); }"},
                    {"kw": "throw", "cat": "memory", "ver": "C++98", "head": "<stdexcept>", "desc": "Throw an exception", "code": "throw std::runtime_error(\"error\");"},
                    {"kw": "sizeof", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Query size of a type or expression in bytes", "code": "size_t s = sizeof(int);"},
                ]
            }
        ]
    },
    {
        "section": "2. Advanced & Modern Extensions",
        "is_advanced": True,
        "categories": [
            {
                "label": "Modern Logic & Deduction",
                "items": [
                    {"kw": "auto", "cat": "modern", "ver": "C++11", "head": "Built-in", "desc": "Deduce type from initializer", "code": "auto x = 3.14; // double"},
                    {"kw": "lambda", "cat": "modern", "ver": "C++11", "head": "Built-in", "desc": "Anonymous function object", "code": "auto f = [](int x){ return x + 1; };"},
                    {"kw": "override", "cat": "modern", "ver": "C++11", "head": "Built-in", "desc": "Explicitly override virtual func", "code": "void run() override;"},
                    {"kw": "final", "cat": "modern", "ver": "C++11", "head": "Built-in", "desc": "Prevent inheritance/overriding", "code": "class Base final { ... };"},
                    {"kw": "constexpr", "cat": "modern", "ver": "C++11", "head": "Built-in", "desc": "Evaluate at compile time", "code": "constexpr int v = 10 * 5;"},
                    {"kw": "consteval", "cat": "modern", "ver": "C++20", "head": "Built-in", "desc": "Function must be evaluated at compile time", "code": "consteval int sq(int x) { return x*x; }"},
                    {"kw": "constinit", "cat": "modern", "ver": "C++20", "head": "Built-in", "desc": "Ensure static initialization", "code": "constinit static int v = 0;"},
                    {"kw": "noexcept", "cat": "modern", "ver": "C++11", "head": "Built-in", "desc": "Guarantee function won't throw", "code": "void log() noexcept;"},
                    {"kw": "decltype", "cat": "modern", "ver": "C++11", "head": "Built-in", "desc": "Extract type from expression", "code": "decltype(1 + 2.0) result; // double"},
                ]
            },
            {
                "label": "Advanced Memory Management & Casting",
                "items": [
                    {"kw": "nullptr", "cat": "memory", "ver": "C++11", "head": "Built-in", "desc": "Safe null pointer literal", "code": "int* p = nullptr;"},
                    {"kw": "alignas", "cat": "memory", "ver": "C++11", "head": "Built-in", "desc": "Specify memory alignment requirement", "code": "alignas(16) int a;"},
                    {"kw": "alignof", "cat": "memory", "ver": "C++11", "head": "<cstddef>", "desc": "Query memory alignment requirement", "code": "std::size_t a = alignof(int);"},
                    {"kw": "static_cast", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Compile-time conversion", "code": "float f = static_cast<float>(i);"},
                    {"kw": "dynamic_cast", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Runtime safe inheritance cast", "code": "Dog* d = dynamic_cast<Dog*>(a);"},
                    {"kw": "const_cast", "cat": "memory", "ver": "C++98", "head": "Built-in", "desc": "Add or remove 'const' property", "code": "int* p = const_cast<int*>(&cVar);"},
                    {"kw": "reinterpret_cast", "cat": "memory", "ver": "C++11", "head": "<cstdint>", "desc": "Low-level bit reinterpretation", "code": "auto addr = reinterpret_cast<std::uintptr_t>(ptr);"},
                    {"kw": "static_assert", "cat": "memory", "ver": "C++11", "head": "Built-in", "desc": "Compile-time validation (often used for sizes)", "code": "static_assert(sizeof(int) >= 4);"},
                ]
            },
            {
                "label": "Templates & Concepts (C++20)",
                "items": [
                    {"kw": "template", "cat": "template", "ver": "C++98", "head": "Built-in", "desc": "Declare generic code", "code": "template <typename T>"},
                    {"kw": "typename", "cat": "template", "ver": "C++98", "head": "Built-in", "desc": "Template type parameter", "code": "template <typename T> class X;"},
                    {"kw": "concept", "cat": "template", "ver": "C++20", "head": "Built-in", "desc": "Define template constraints", "code": "concept Number = requires(T x)"},
                    {"kw": "import", "cat": "template", "ver": "C++20", "head": "Built-in", "desc": "Import module unit", "code": "import std;"},
                    {"kw": "export", "cat": "template", "ver": "C++20", "head": "Built-in", "desc": "Export module names", "code": "export module my_lib;"},
                    {"kw": "namespace", "cat": "template", "ver": "C++98", "head": "Built-in", "desc": "Logical scope grouping", "code": "namespace Graphics { ... }"},
                    {"kw": "using", "cat": "template", "ver": "C++98", "head": "Built-in", "desc": "Alias or namespace import", "code": "using String = std::string;"},
                ]
            },
            {
                "label": "Coroutines & System",
                "items": [
                    {"kw": "co_await", "cat": "system", "ver": "C++20", "head": "<coroutine>", "desc": "Suspend coroutine execution", "code": "auto res = co_await task;"},
                    {"kw": "co_yield", "cat": "system", "ver": "C++20", "head": "<coroutine>", "desc": "Return value + pause generator", "code": "co_yield next_value;"},
                    {"kw": "co_return", "cat": "system", "ver": "C++20", "head": "<coroutine>", "desc": "Return from a coroutine", "code": "co_return value;"},
                    {"kw": "thread_local", "cat": "system", "ver": "C++11", "head": "Built-in", "desc": "Unique instance per thread", "code": "thread_local int threadTotal;"},
                    {"kw": "asm", "cat": "system", "ver": "N/A", "head": "Built-in", "desc": "Inline assembly", "code": "asm(\"nop\");"},
                ]
            },
            {
                "label": "Logical Tokens",
                "items": [
                    {"kw": "and", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for &&", "code": "if (isReady and isOk)"},
                    {"kw": "not", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for !", "code": "if (not isFull)"},
                    {"kw": "or", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for ||", "code": "if (isTrue or isValid)"},
                    {"kw": "xor", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for ^", "code": "bool result = a xor b;"},
                    {"kw": "and_eq", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for &=", "code": "x and_eq y;"},
                    {"kw": "or_eq", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for |=", "code": "x or_eq y;"},
                    {"kw": "not_eq", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for !=", "code": "x not_eq y;"},
                    {"kw": "xor_eq", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for ^=", "code": "x xor_eq y;"},
                    {"kw": "bitand", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for & (bitwise AND)", "code": "int x = a bitand b;"},
                    {"kw": "bitor", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for | (bitwise OR)", "code": "int x = a bitor b;"},
                    {"kw": "compl", "cat": "logic", "ver": "C++98", "head": "Built-in", "desc": "Alias for ~ (bitwise NOT)", "code": "int x = compl a;"},
                ]
            }
        ]
    },
    {
        "section": "3. Essential Standard Library Additions (Non-Keywords)",
        "is_library": True,
        "categories": [
            {
                "label": "Smart Pointers (RAII Classes)",
                "items": [
                    {"kw": "std::unique_ptr", "cat": "memory", "ver": "C++11", "head": "<memory>", "desc": "Exclusive ownership pointer", "code": "auto p = std::make_unique<T>();"},
                    {"kw": "std::shared_ptr", "cat": "memory", "ver": "C++11", "head": "<memory>", "desc": "Shared ownership pointer", "code": "auto p = std::make_shared<T>();"},
                    {"kw": "std::weak_ptr", "cat": "memory", "ver": "C++11", "head": "<memory>", "desc": "Non-owning observer pointer", "code": "std::weak_ptr<T> wp = sp;"},
                ]
            }
        ]
    },
    {
        "section": "4. Preprocessor Directives (Meta-Programming)",
        "is_advanced": True,
        "categories": [
            {
                "label": "Conditional Compilation",
                "items": [
                    {"kw": "if", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Check if a condition is true", "code": "#if DEBUG_LEVEL > 1"},
                    {"kw": "elif", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Else-if condition", "code": "#elif defined(TEST_MODE)"},
                    {"kw": "else", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Alternative branch", "code": "#else"},
                    {"kw": "endif", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "End of conditional block", "code": "#endif"},
                    {"kw": "ifdef", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Check if macro is defined", "code": "#ifdef WIN32"},
                    {"kw": "ifndef", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Check if macro is NOT defined", "code": "#ifndef HEADER_H"},
                    {"kw": "elifdef", "cat": "preprocessor", "ver": "C++23", "head": "Preprocessor", "desc": "Else-if macro is defined", "code": "#elifdef FEATURE_X"},
                    {"kw": "elifndef", "cat": "preprocessor", "ver": "C++23", "head": "Preprocessor", "desc": "Else-if macro is NOT defined", "code": "#elifndef FEATURE_Y"},
                ]
            },
            {
                "label": "Macro Definition",
                "items": [
                    {"kw": "define", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Define a macro or constant", "code": "#define MAX_BUFFER 1024"},
                    {"kw": "undef", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Cancel a macro definition", "code": "#undef MAX_BUFFER"},
                ]
            },
            {
                "label": "Source Control & Diagnostics",
                "items": [
                    {"kw": "include", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Include source file", "code": "#include <vector>"},
                    {"kw": "embed", "cat": "preprocessor", "ver": "C++26", "head": "Preprocessor", "desc": "Binary resource inclusion", "code": "#embed \"image.png\""},
                    {"kw": "line", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Change internal line number/filename", "code": "#line 100 \"custom.cpp\""},
                    {"kw": "error", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Stop compilation with error message", "code": "#error \"Unsupported OS!\""},
                    {"kw": "warning", "cat": "preprocessor", "ver": "C++23", "head": "Preprocessor", "desc": "Issue compilation warning", "code": "#warning \"Using beta feature\""},
                    {"kw": "pragma", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Compiler-specific instructions", "code": "#pragma once"},
                ]
            },
            {
                "label": "Functional Checks",
                "items": [
                    {"kw": "defined", "cat": "preprocessor", "ver": "C++98", "head": "Preprocessor", "desc": "Unary operator to check macro existence", "code": "#if defined(A) && defined(B)"},
                    {"kw": "__has_include", "cat": "preprocessor", "ver": "C++17", "head": "Preprocessor", "desc": "Check if a header file exists", "code": "#if __has_include(<filesystem>)"},
                    {"kw": "__has_cpp_attribute", "cat": "preprocessor", "ver": "C++20", "head": "Preprocessor", "desc": "Check for attribute support", "code": "#if __has_cpp_attribute(nodiscard)"},
                    {"kw": "__has_embed", "cat": "preprocessor", "ver": "C++26", "head": "Preprocessor", "desc": "Check for binary resource existence", "code": "#if __has_embed(\"data.bin\")"},
                ]
            },
            {
                "label": "Module Directives (Preprocessor Context)",
                "items": [
                    {"kw": "export", "cat": "template", "ver": "C++20", "head": "Built-in", "desc": "Export module declaration", "code": "export module math;"},
                    {"kw": "import", "cat": "template", "ver": "C++20", "head": "Built-in", "desc": "Import module declaration", "code": "import std;"},
                    {"kw": "module", "cat": "template", "ver": "C++20", "head": "Built-in", "desc": "Declare module or global fragment", "code": "module; // Global fragment"},
                ]
            }
        ]
    }
]

# Sheet HTML is now rendered from the shared template file `sheet_template.html`.
# This keeps styling and common layout in one place and avoids duplication.

def build_doc_url(item):
    if item['head'] == "Preprocessor":
        return f"https://en.cppreference.com/w/cpp/preprocessor/{item['kw']}"
    if "std::" in item['kw']:
        return f"https://en.cppreference.com/w/cpp/memory/{item['kw'].split('::')[1]}"
    return f"https://en.cppreference.com/w/cpp/keyword/{item['kw'].replace(' ', '_')}"


def generate_table(section):
    return render_section_table(
        section,
        build_doc_url,
        item_header="Keyword",
        context_header="Header",
        col_widths=("15%", "30%", "15%", "40%"),
        deprecated_class="deprecated-tag",
    )

def main():
    content_html = build_content_html(KEYWORDS_DATA, generate_table, 'Advanced & Modern')
    title = 'C++ Polyglot Dev Atlas'
    legend_html = '''<div class="legend-row">
                <div class="legend-item"><div class="color-box type"></div> Data Types</div>
                <div class="legend-item"><div class="color-box logic"></div> Logic / Flow</div>
                <div class="legend-item"><div class="color-box storage"></div> Storage / Modifiers</div>
                <div class="legend-item"><div class="color-box oop"></div> OOP / Classes</div>
                <div class="legend-item"><div class="color-box memory"></div> Memory / Safety</div>
                <div class="legend-item"><div class="color-box modern"></div> Modern C++</div>
                <div class="legend-item"><div class="color-box template-key"></div> Templates & Concepts</div>
                <div class="legend-item"><div class="color-box preprocessor"></div> Preprocessor</div>
                <div class="legend-item"><div class="color-box system"></div> System / Coroutines</div>
        </div>'''

    final_html = render_sheet_html(__file__, title, legend_html, content_html)
    write_sheet_output(__file__, 'cpp_cheat_sheet.html', final_html)

if __name__ == '__main__':
    main()
