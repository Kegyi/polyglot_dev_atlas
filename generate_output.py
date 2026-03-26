#!/usr/bin/env python3
"""
Generate a single self-contained HTML file with all Polyglot Dev Atlas content.

Output: polyglot_dev_atlas/output/polyglot_dev_atlas.html

Usage (run from within polyglot_dev_atlas/):
    python generate_output.py               # run per-language generators first, then build
    python generate_output.py --skip-gen    # skip running per-language generators (faster)
"""

import html as html_lib
import os
import subprocess
import sys
import urllib.request

from generator_utils import (
    extract_between,
    load_examples_from_dir,
    markdown_to_html,
    normalize_sheet_body,
    read_file,
    safe_json,
)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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

# ---------------------------------------------------------------------------
# Language definitions: (id, display label, relative path to generated HTML)
# relative path is relative to SHEET_GENERATORS_DIR
# ---------------------------------------------------------------------------

LANGS = [
    ("cpp", "C++", "cpp/cpp_cheat_sheet.html"),
    ("python", "Python", "python/python_cheat_sheet.html"),
    ("go", "Go", "go/go_cheat_sheet.html"),
    ("typescript", "TypeScript", "typescript/typescript_cheat_sheet.html"),
    ("scala2", "Scala 2", "scala/scala2_cheat_sheet.html"),
    ("scala3", "Scala 3", "scala/scala3_cheat_sheet.html"),
]

BASICS_GROUPS = [
    {
        "label": "Project Setup & Environment",
        "keys": ["project_lifecycle", "command_line_args", "environment_variables"],
    },
    {"label": "Control Flow", "keys": ["loops", "conditions", "recursion"]},
    {"label": "Functions & Errors", "keys": ["functions_and_errors", "exceptions_and_recovery"]},
    {"label": "Data Structures", "keys": ["arrays_and_collections", "maps_and_sets", "strings", "collection_mappings"]},
    {
        "label": "OOP & Abstraction",
        "keys": ["classes_and_objects", "interfaces_and_polymorphism", "enums_and_constants"],
    },
    {"label": "Algorithms", "keys": ["sorting_and_searching", "hashing_and_checksums", "random_numbers"]},
    {"label": "Input / Output", "keys": ["file_io", "file_paths_and_directories", "json_and_serialization"]},
    {
        "label": "System & Environment",
        "keys": [
            "dates_and_time",
            "nullable_optional_values",
            "type_system_comparison",
            "scala_migration",
            "memory_management",
            "concurrency_models",
        ],
    },
]

INTERVIEW_GROUPS = [
    {
        "label": "1.x Arrays & Strings",
        "keys": [
            "lcci_01_01_is_unique",
            "lcci_01_02_check_permutation",
            "lcci_01_03_string_to_url",
            "lcci_01_04_palindrome_permutation",
            "lcci_01_05_one_away",
            "lcci_01_06_compress_string",
            "lcci_01_07_rotate_matrix",
            "lcci_01_08_zero_matrix",
            "lcci_01_09_string_rotation",
        ],
    },
    {
        "label": "2.x Linked Lists",
        "keys": [
            "lcci_02_01_remove_duplicate_node",
            "lcci_02_02_kth_node_from_end",
            "lcci_02_03_delete_middle_node",
            "lcci_02_04_partition_list",
            "lcci_02_05_sum_lists",
            "lcci_02_06_palindrome_linked_list",
            "lcci_02_07_intersection_of_two_linked_lists",
            "lcci_02_08_linked_list_cycle",
        ],
    },
    {
        "label": "3.x Stacks & Queues",
        "keys": [
            "lcci_03_01_three_in_one",
            "lcci_03_02_min_stack",
            "lcci_03_03_stack_of_plates",
            "lcci_03_04_queue_via_stacks",
            "lcci_03_05_sort_stack",
            "lcci_03_06_animal_shelter",
        ],
    },
    {
        "label": "4.x Trees & Graphs",
        "keys": [
            "lcci_04_01_route_between_nodes",
            "lcci_04_02_minimum_height_tree",
            "lcci_04_03_list_of_depth",
            "lcci_04_04_check_balance",
            "lcci_04_05_legal_binary_search_tree",
            "lcci_04_06_successor",
            "lcci_04_08_first_common_ancestor",
            "lcci_04_09_bst_sequences",
            "lcci_04_10_check_subtree",
            "lcci_04_12_paths_with_sum",
        ],
    },
    {
        "label": "5.x Bit Manipulation",
        "keys": [
            "lcci_05_01_insert",
            "lcci_05_02_binary_number_to_string",
            "lcci_05_03_flip_bit_to_win",
            "lcci_05_04_closed_number",
            "lcci_05_06_number_of_1",
            "lcci_05_07_exchange",
            "lcci_05_08_draw_line",
        ],
    },
    {
        "label": "8.x Recursion & Dynamic Programming",
        "keys": [
            "lcci_08_01_three_steps",
            "lcci_08_02_robot_in_a_grid",
            "lcci_08_03_magic_index",
            "lcci_08_04_power_set",
            "lcci_08_06_hanota",
            "lcci_08_07_permutation_i",
            "lcci_08_08_permutation_ii",
            "lcci_08_09_bracket",
            "lcci_08_10_color_fill",
            "lcci_08_11_coin",
            "lcci_08_12_eight_queens",
            "lcci_08_13_pile_box",
            "lcci_08_14_boolean_evaluation",
        ],
    },
    {
        "label": "10.x Sorting & Searching",
        "keys": [
            "lcci_10_01_sorted_merge",
            "lcci_10_02_group_anagrams",
            "lcci_10_03_search_rotate_array",
            "lcci_10_05_sparse_array_search",
            "lcci_10_09_sorted_matrix_search",
            "lcci_10_10_rank_from_stream",
            "lcci_10_11_peaks_and_valleys",
        ],
    },
    {
        "label": "16.x Moderate (Part 1)",
        "keys": [
            "lcci_16_01_swap_numbers",
            "lcci_16_02_words_frequency",
            "lcci_16_03_intersection",
            "lcci_16_04_tic_tac_toe",
            "lcci_16_05_factorial_zeros",
            "lcci_16_06_smallest_difference",
            "lcci_16_07_maximum",
            "lcci_16_08_english_int",
            "lcci_16_09_operations",
            "lcci_16_10_living_people",
            "lcci_16_11_diving_board",
            "lcci_16_13_bisect_squares",
            "lcci_16_14_best_line",
        ],
    },
    {
        "label": "16.x Moderate (Part 2)",
        "keys": [
            "lcci_16_15_master_mind",
            "lcci_16_16_sub_sort",
            "lcci_16_17_contiguous_sequence",
            "lcci_16_18_pattern_matching",
            "lcci_16_19_pond_sizes",
            "lcci_16_20_t9",
            "lcci_16_21_sum_swap",
            "lcci_16_22_langtons_ant",
            "lcci_16_24_pairs_with_sum",
            "lcci_16_25_lru_cache",
            "lcci_16_26_calculator",
        ],
    },
    {
        "label": "17.x Hard",
        "keys": [
            "lcci_17_13_re_space",
            "lcci_17_14_smallest_k",
            "lcci_17_15_longest_word",
            "lcci_17_16_the_masseuse",
            "lcci_17_17_multi_search",
            "lcci_17_18_shortest_supersequence",
            "lcci_17_19_missing_two",
            "lcci_17_20_continuous_median",
            "lcci_17_21_volume_of_histogram",
            "lcci_17_22_word_transformer",
        ],
    },
]

DESIGN_PATTERNS_GROUPS = [
    {
        "label": "Creational Patterns",
        "keys": [
            "abstract_factory",
            "builder",
            "factory_method",
            "prototype",
            "singleton",
        ],
    },
    {
        "label": "Structural Patterns",
        "keys": [
            "adapter",
            "bridge",
            "composite",
            "decorator",
            "facade",
            "flyweight",
            "proxy",
        ],
    },
    {
        "label": "Behavioral Patterns",
        "keys": [
            "chain_of_responsibility",
            "command",
            "iterator",
            "mediator",
            "memento",
            "observer",
            "state",
            "strategy",
            "template_method",
            "visitor",
            "interpreter",
        ],
    },
]

MODERN_APPROACH_NOTES = {
    "chain_of_responsibility": {
        "cpp": {
            "classic": "Linked handler subclasses via `setNext`",
            "modern": "`std::vector<Handler>` \u2014 flat chain of `std::function`, each returns `bool`",
        },
        "python": {
            "classic": "Linked `Handler` ABC subclasses with `set_next`",
            "modern": "Flat `list[Callable[[Request], bool]]` \u2014 handlers return `bool` to stop propagation",
        },
    },
    "command": {
        "cpp": {
            "classic": "Command class hierarchy",
            "modern": "`std::vector<std::function<void()>>` with lambdas",
        },
        "python": {
            "classic": "`Command` ABC subclasses",
            "modern": "`list[Callable[[], None]]` \u2014 bound methods or lambdas",
        },
        "typescript": {
            "classic": "`Command` interface + class hierarchy",
            "modern": "`Array<() => void>` closures",
        },
        "go": {
            "classic": "`Command` interface + struct implementations",
            "modern": "`[]func()` closure slice",
        },
    },
    "observer": {
        "cpp": {
            "classic": "Observer interface subclasses",
            "modern": "`std::function` callbacks \u2014 any callable subscribes directly",
        },
        "python": {
            "classic": "`Observer` ABC subclasses",
            "modern": "`list[Callable[[str], None]]` \u2014 any callable subscribes directly",
        },
        "typescript": {
            "classic": "`Observer` interface + class hierarchy",
            "modern": "Generic `Listener<T>` type alias + typed callback array",
        },
        "go": {
            "classic": "`Observer` interface + struct implementations",
            "modern": "`[]func(string)` callback slice",
        },
    },
    "state": {
        "cpp": {
            "classic": "Virtual `handle` + heap-allocated state objects",
            "modern": "`std::variant` \u2014 transitions are value assignments",
        },
        "python": {
            "classic": "`State` ABC + subclasses + `Context`",
            "modern": "Dataclasses + `match` statement (Python 3.10+)",
        },
        "typescript": {
            "classic": "`IState` interface + class hierarchy",
            "modern": "Discriminated union + exhaustive `switch` (compile-time safety)",
        },
        "scala": {
            "classic": "`State` trait + subclasses",
            "modern": "Sealed trait ADT + `match` (compiler-enforced exhaustiveness)",
        },
    },
    "strategy": {
        "cpp": {
            "classic": "Virtual strategy base class",
            "modern": "Policy templates (compile-time) or `std::function` (runtime)",
        },
        "python": {
            "classic": "`Strategy` ABC subclasses",
            "modern": "`Callable[[int, int], int]` type alias \u2014 lambdas or functions directly",
        },
        "typescript": {
            "classic": "`Strategy` interface + class hierarchy",
            "modern": "Function type alias `(a: number, b: number) => number`",
        },
        "go": {
            "classic": "`Strategy` interface + struct implementations",
            "modern": "`type Strategy func(a, b int) int` \u2014 function value field",
        },
        "scala": {
            "classic": "`Strategy` trait + subclasses",
            "modern": "Function value `(Int, Int) => Int` or `given`/`using` type class (Scala 3)",
        },
    },
    "template_method": {
        "cpp": {
            "classic": "Virtual steps in a base class (runtime polymorphism)",
            "modern": "CRTP \u2014 compile-time polymorphism, no vtable",
        },
        "python": {
            "classic": "`@abstractmethod` step methods in base class",
            "modern": "Higher-order function that takes `Callable` steps as parameters",
        },
    },
    "visitor": {
        "cpp": {
            "classic": "Virtual `accept` / `visit` double dispatch",
            "modern": "`std::variant` + `std::visit` + `overload` helper",
        },
        "python": {
            "classic": "`Visitor` / `Element` ABC + `accept` / `visit` double dispatch",
            "modern": "`@functools.singledispatch` \u2014 dispatch on argument type, no base classes",
        },
        "typescript": {
            "classic": "`IVisitor` / `IElement` interfaces + `accept` / `visit` double dispatch",
            "modern": "Discriminated union + exhaustive `switch` \u2014 `never` check enforces completeness",
        },
        "go": {
            "classic": "`Visitor` / `Element` interfaces + `Accept` / `Visit` methods",
            "modern": "Type switch \u2014 `switch s.(type)` dispatches on concrete type",
        },
        "scala": {
            "classic": "`Visitor` / `Element` traits + `accept` / `visit` double dispatch",
            "modern": "Sealed trait ADT + `match` \u2014 exhaustive pattern matching",
        },
    },
}

PRINCIPLES_GROUPS = [
    {
        "label": "Core Design",
        "keys": [
            "single_responsibility",
            "open_closed",
            "liskov_substitution",
            "interface_segregation",
            "dependency_inversion",
            "composition_over_inheritance",
        ],
    },
    {
        "label": "Code Quality",
        "keys": [
            "dry",
            "kiss",
            "yagni",
            "law_of_demeter",
            "separation_of_concerns",
        ],
    },
    {
        "label": "Reliability",
        "keys": [
            "fail_fast",
            "immutability_first",
        ],
    },
    {
        "label": "Language Paradigms",
        "keys": [
            "memory_management",
            "concurrency_models",
            "structural_typing",
            "nominal_typing",
            "duck_typing",
        ],
    },
]

PRINCIPLES = {
    "single_responsibility": {
        "label": "Single Responsibility Principle (SRP)",
        "description": "A module should have one reason to change. Keep unrelated responsibilities in separate units.",
        "sourceLinks": [{"label": "SOLID overview", "url": "https://en.wikipedia.org/wiki/SOLID"}],
        "points": [
            "Split business logic, persistence, and presentation concerns.",
            "Smaller focused units are easier to test and refactor.",
            "Watch for classes that keep growing in unrelated directions.",
        ],
        "notes": [
            "A practical signal of SRP drift is when one change request touches unrelated methods in the same class.",
            "If you cannot explain a module's purpose in one sentence, it probably has mixed responsibilities.",
        ],
        "pitfalls": [
            "Fragmenting code into too many tiny files with unclear ownership.",
            "Confusing utility extraction with true responsibility boundaries.",
            "Splitting by technical layer only and ignoring domain cohesion.",
        ],
    },
    "open_closed": {
        "label": "Open/Closed Principle (OCP)",
        "description": "Software entities should be open for extension, closed for modification.",
        "sourceLinks": [{"label": "SOLID overview", "url": "https://en.wikipedia.org/wiki/SOLID"}],
        "points": [
            "Prefer plugging in new behavior via interfaces or composition.",
            "Avoid changing stable, already-tested code for every new variant.",
            "Use extension points where change is expected.",
        ],
        "notes": [
            "OCP works best when variability is known at seams like pricing rules, providers, or transport adapters.",
            "Start concrete, then extract an extension point after the second real variation appears.",
        ],
        "pitfalls": [
            "Introducing abstraction layers before there is actual variation.",
            "Creating extension hooks that are too generic to be safe.",
            "Treating OCP as never modify existing code under any condition.",
        ],
    },
    "liskov_substitution": {
        "label": "Liskov Substitution Principle (LSP)",
        "description": "Subtypes must be substitutable for their base types without surprising behavior changes.",
        "sourceLinks": [{"label": "SOLID overview", "url": "https://en.wikipedia.org/wiki/SOLID"}],
        "points": [
            "Derived types should honor base contracts and expectations.",
            "Do not strengthen preconditions or weaken postconditions.",
            "If substitution breaks, your abstraction is likely wrong.",
        ],
        "notes": [
            "Document contracts explicitly, especially edge-case behavior and exception semantics.",
            "Favor composition if subtype behavior would need special-case checks by callers.",
        ],
        "pitfalls": [
            "Overriding methods with narrower accepted input ranges.",
            "Throwing new runtime errors where base type never did.",
            "Using inheritance for code reuse when behavioral contracts differ.",
        ],
    },
    "interface_segregation": {
        "label": "Interface Segregation Principle (ISP)",
        "description": "Clients should not depend on methods they do not use.",
        "sourceLinks": [{"label": "SOLID overview", "url": "https://en.wikipedia.org/wiki/SOLID"}],
        "points": [
            "Prefer smaller, role-focused interfaces over one giant interface.",
            "Reduces accidental coupling and implementation burden.",
            "Improves testability with narrower mocks/stubs.",
        ],
        "notes": [
            "Group methods by usage role, not by domain noun alone.",
            "If most implementations throw or no-op on an interface method, split the interface.",
        ],
        "pitfalls": [
            "Creating extremely granular interfaces that become hard to navigate.",
            "Duplicating near-identical interfaces across modules.",
            "Breaking cohesion by splitting methods that belong together.",
        ],
    },
    "dependency_inversion": {
        "label": "Dependency Inversion Principle (DIP)",
        "description": "High-level modules should depend on abstractions, not concrete details.",
        "sourceLinks": [{"label": "SOLID overview", "url": "https://en.wikipedia.org/wiki/SOLID"}],
        "points": [
            "Inject dependencies at boundaries instead of hard-coding them.",
            "Keep infrastructure replaceable (DB, cache, transport).",
            "Makes core logic portable and easier to test.",
        ],
        "notes": [
            "Dependency inversion is most valuable where infrastructure volatility is high.",
            "Keep abstraction ownership close to the high-level policy that consumes it.",
        ],
        "pitfalls": [
            "Using DI containers for trivial modules where simple wiring is enough.",
            "Abstracting everything, including stable concrete dependencies.",
            "Leaking framework-specific types into domain interfaces.",
        ],
    },
    "composition_over_inheritance": {
        "label": "Composition over Inheritance",
        "description": "Favor assembling behavior from components instead of deep inheritance trees.",
        "sourceLinks": [{"label": "Design principle reference", "url": "https://en.wikipedia.org/wiki/Composition_over_inheritance"}],
        "points": [
            "Composition keeps behavior explicit and flexible at runtime.",
            "Avoids fragile base-class problems.",
            "Works especially well with strategy and decorator patterns.",
        ],
        "notes": [
            "Use small collaborating objects when behavior mixes vary per context.",
            "Prefer inheritance only when there is a stable behavioral is-a relationship.",
        ],
        "pitfalls": [
            "Introducing excessive indirection for straightforward type hierarchies.",
            "Hiding composition wiring in magic factories or globals.",
            "Ignoring performance impact of over-layered delegation.",
        ],
    },
    "dry": {
        "label": "DRY (Don't Repeat Yourself)",
        "description": "Each piece of knowledge should have a single, authoritative representation.",
        "sourceLinks": [{"label": "The Pragmatic Programmer (DRY)", "url": "https://en.wikipedia.org/wiki/Don%27t_repeat_yourself"}],
        "points": [
            "Remove duplicated business rules before they diverge.",
            "Prefer shared abstractions only when duplication is meaningful.",
            "Do not over-abstract too early; wait for stable repetition.",
        ],
        "notes": [
            "Duplicate policy logic is more dangerous than duplicate plumbing code.",
            "A good DRY refactor should reduce both code and cognitive load.",
        ],
        "pitfalls": [
            "Merging coincidental similarity that later diverges.",
            "Optimizing for zero duplication at the cost of readability.",
            "Creating shared helpers that become dumping grounds.",
        ],
    },
    "kiss": {
        "label": "KISS (Keep It Simple, Stupid)",
        "description": "Prefer the simplest solution that satisfies current requirements.",
        "sourceLinks": [{"label": "KISS principle", "url": "https://en.wikipedia.org/wiki/KISS_principle"}],
        "points": [
            "Simple code is easier to debug, change, and explain.",
            "Complexity should be justified by measurable value.",
            "Choose readability over cleverness for team code.",
        ],
        "notes": [
            "KISS applies to API shape, naming, and operational flow, not just code length.",
            "When two options work, prefer the one new team members can reason about quickly.",
        ],
        "pitfalls": [
            "Interpreting simplicity as avoiding necessary design structure.",
            "Choosing short code over clear code.",
            "Ignoring operational complexity while simplifying local code.",
        ],
    },
    "yagni": {
        "label": "YAGNI (You Aren't Gonna Need It)",
        "description": "Do not implement speculative features before they are required.",
        "sourceLinks": [{"label": "YAGNI principle", "url": "https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it"}],
        "points": [
            "Build for current use-cases and adapt incrementally.",
            "Premature extensibility increases maintenance cost.",
            "Treat future requirements as hypotheses, not facts.",
        ],
        "notes": [
            "Capture deferred ideas in lightweight notes so they can be revisited intentionally.",
            "YAGNI does not mean ignoring obvious nearby needs already in active planning.",
        ],
        "pitfalls": [
            "Using YAGNI to reject legitimate near-term requirements.",
            "Skipping essential extension points at stable boundaries.",
            "Accumulating debt by repeatedly shipping ad hoc one-offs.",
        ],
    },
    "law_of_demeter": {
        "label": "Law of Demeter",
        "description": "A unit should talk only to its close collaborators, not to distant objects.",
        "sourceLinks": [{"label": "Law of Demeter", "url": "https://en.wikipedia.org/wiki/Law_of_Demeter"}],
        "points": [
            "Avoid long call chains across object graphs.",
            "Expose intent-revealing methods instead of internals.",
            "Reduces ripple effects from internal structure changes.",
        ],
        "notes": [
            "Good Demeter boundaries often align with aggregate/domain boundaries.",
            "Replace chained access with task-level methods that express intent.",
        ],
        "pitfalls": [
            "Adding pass-through methods everywhere without improving design.",
            "Masking poor boundaries behind facade-like wrappers.",
            "Treating every nested access as a violation regardless of context.",
        ],
    },
    "separation_of_concerns": {
        "label": "Separation of Concerns",
        "description": "Organize software so each part addresses a distinct concern.",
        "sourceLinks": [{"label": "Separation of concerns", "url": "https://en.wikipedia.org/wiki/Separation_of_concerns"}],
        "points": [
            "Keep domain logic independent from delivery mechanism.",
            "Use boundaries (layers/modules) to contain change.",
            "Improves parallel development and maintainability.",
        ],
        "notes": [
            "Strong boundaries reduce merge conflicts and clarify team ownership.",
            "Define boundary contracts explicitly to avoid leak-back coupling.",
        ],
        "pitfalls": [
            "Over-layering the architecture without practical benefit.",
            "Leaking concerns through shared mutable models.",
            "Designing boundaries that match org charts rather than domain flows.",
        ],
    },
    "fail_fast": {
        "label": "Fail Fast",
        "description": "Detect invalid state early and stop immediately to avoid corrupted downstream behavior.",
        "sourceLinks": [{"label": "Fail-fast", "url": "https://en.wikipedia.org/wiki/Fail-fast_system"}],
        "points": [
            "Validate inputs and assumptions at boundaries.",
            "Surface precise errors close to root causes.",
            "Prevents subtle latent failures and bad data spread.",
        ],
        "notes": [
            "Fail-fast is strongest when paired with actionable error messages and tracing.",
            "Detecting bad state early saves debugging cost later in the pipeline.",
        ],
        "pitfalls": [
            "Failing deep inside internals with vague error messages.",
            "Turning every recoverable condition into a hard crash.",
            "Skipping observability, making failures hard to diagnose.",
        ],
    },
    "immutability_first": {
        "label": "Immutability First",
        "description": "Prefer immutable data and explicit state transitions where practical.",
        "sourceLinks": [{"label": "Immutable object", "url": "https://en.wikipedia.org/wiki/Immutable_object"}],
        "points": [
            "Reduces shared-state bugs and race conditions.",
            "Makes reasoning, testing, and rollback easier.",
            "Use controlled mutation only where performance requires it.",
        ],
        "notes": [
            "Immutability is especially valuable at API boundaries and cross-thread handoff points.",
            "Prefer immutable defaults, then introduce measured mutation where profiling justifies it.",
        ],
        "pitfalls": [
            "Copying large structures naively and harming performance.",
            "Using immutable shells around hidden mutable internals.",
            "Applying immutability dogmatically in hot paths without profiling.",
        ],
    },
    "memory_management": {
        "label": "Memory Management Model",
        "description": "Understand how each language handles memory allocation, ownership, and deallocation.",
        "sourceLinks": [{"label": "Memory safety", "url": "https://en.wikipedia.org/wiki/Memory_safety"}],
        "points": [
            "C++ exposes the cost model explicitly: stack (LIFO), heap (manual or smart pointers), and move semantics.",
            "Go uses escape analysis: scalars often live on stack; pointers allow heap allocation but garbage collection is automatic.",
            "Python uses reference counting plus a cycle detector for garbage collection.",
            "TypeScript/JavaScript and Scala use full garbage collection (GC)—allocation is automatic.",
        ],
        "notes": [
            "In C++, choose `std::unique_ptr` for exclusive ownership, `std::shared_ptr` for shared ownership, or manual `new`/`delete` for fine-grained control.",
            "In Go, structs are value types by default; use pointers `&` only when you need indirection or mutability across boundaries.",
            "Python's reference counting means circular references can leak—use `weakref` or rely on the cycle collector.",
            "Languages with GC hide allocation details but require tuning GC pause interactions if latency matters.",
        ],
        "pitfalls": [
            "C++: Forgetting to `delete` or using raw pointers where smart pointers fit better.",
            "Go: Overusing pointers when value semantics would simplify code and avoid allocation.",
            "Python: Creating reference cycles with `__del__` methods that aren't called promptly.",
            "GC languages: Assuming GC is free—major collections can pause your program.",
        ],
    },
    "concurrency_models": {
        "label": "Concurrency Models",
        "description": "Compare how each language handles parallel execution: threads, goroutines, async/await, or Futures.",
        "sourceLinks": [{"label": "Concurrency", "url": "https://en.wikipedia.org/wiki/Concurrency_(computer_science)"}],
        "points": [
            "C++ uses OS threads with mutex/condition-variable synchronization or task-based `std::async` with Futures.",
            "Go uses lightweight goroutines (M:N scheduling) coordinated via channels (CSP model).",
            "Python has the Global Interpreter Lock (GIL): use `asyncio` for I/O concurrency or `multiprocessing` for CPU-bound work.",
            "TypeScript/Node is single-threaded with an event loop; `async/await` suspends without blocking other tasks.",
            "Scala uses Futures running on an ExecutionContext (typically thread pool) with monadic composition (`for`-yield).",
        ],
        "notes": [
            "C++ threads map 1:1 to OS threads—context switching and memory overhead scales with thread count.",
            "Go goroutines are user-space; millions can exist with low overhead, coordinated by the scheduler.",
            "Python's GIL means only one Python bytecode runs per process at a time; use it for I/O, not CPU parallelism.",
            "TypeScript event loop is deterministic and single-threaded; reasoning about state is easier but CPU work blocks everyone.",
            "Scala Futures are lazy by default—use `scala.concurrent.ExecutionContext` to control threading.",
        ],
        "pitfalls": [
            "C++: Creating too many threads—context switching overhead dominates. Use thread pools instead.",
            "Go: Channel deadlocks from mismatched send/receive. Use `select` with `default` for non-blocking operations.",
            "Python: Assuming threads give parallelism—the GIL serializes Python bytecode. Use multiprocessing or Cython where needed.",
            "TypeScript: Blocking the event loop with long CPU work (e.g., in loops). Offload to workers or use `setImmediate`.",
            "Scala: Blocking threads in Futures—the ExecutionContext may starve. Use `blocking { ... }` to signal intent.",
        ],
    },
    "structural_typing": {
        "label": "Structural Typing",
        "description": "A type satisfies an interface if it has the required methods/fields, regardless of explicit declaration.",
        "sourceLinks": [{"label": "Structural subtyping", "url": "https://en.wikipedia.org/wiki/Structural_type_system"}],
        "points": [
            "Go interfaces are implicitly satisfied: any type with matching method signatures implements the interface.",
            "TypeScript uses structural compatibility: if two types have the same shape, they are assignable.",
            "Python 3.8+ Protocol classes enable structural typing hints without inheritance.",
            "Advantage: decoupled design; no need to declare intent upfront.",
        ],
        "notes": [
            "Structural typing enables ad-hoc composition: old code can satisfy new interfaces without modification.",
            "Works well for interfaces with a small method set (narrow contracts).",
            "Refactoring method names affects all structural matches silently—tooling must catch mismatches.",
        ],
        "pitfalls": [
            "Accidentally satisfying an interface when you didn't intend to.",
            "Large interfaces become hard to reason about—implementations accidentally match too much.",
            "Renaming a method silently breaks structural contracts; no compiler warning.",
        ],
    },
    "nominal_typing": {
        "label": "Nominal Typing",
        "description": "A type satisfies an interface only if explicitly declared or inherited through its type hierarchy.",
        "sourceLinks": [{"label": "Nominal type system", "url": "https://en.wikipedia.org/wiki/Nominal_type_system"}],
        "points": [
            "C++ uses nominal typing with virtual dispatch: you declare `class Dog : Animal` explicitly.",
            "Scala uses nominal typing with traits: `class Dog extends Animal`.",
            "Advantage: explicit intent; no accidental interface satisfaction.",
            "Compiler enforces declarations—refactoring is safer.",
        ],
        "notes": [
            "Nominal typing requires upfront design: you must anticipate all interfaces your type will implement.",
            "Type hierarchies become rigid if not designed carefully—deep trees are hard to refactor.",
            "Well-suited for closed, stable domains where interfaces are known upfront.",
        ],
        "pitfalls": [
            "Deep inheritance hierarchies that become brittle.",
            "Introducing new interfaces later requires modifying old type definitions.",
            "Tight coupling between interfaces and implementations.",
        ],
    },
    "duck_typing": {
        "label": "Duck Typing",
        "description": "If an object quacks like a duck, it is a duck—type checking happens at runtime via attribute/method access.",
        "sourceLinks": [{"label": "Duck typing", "url": "https://en.wikipedia.org/wiki/Duck_typing"}],
        "points": [
            "Python embraces duck typing: no compile-time type checking; errors surface at runtime.",
            "Advantage: extreme flexibility; code works with any object that has the required methods.",
            "Type hints (PEP 484, `typing` module) add static analysis without enforcement.",
            "No interfaces or base classes needed—just call the method and handle failures.",
        ],
        "notes": [
            "Duck typing is powerful for exploration and dynamic scenarios (e.g., metaprogramming).",
            "Type hints with tools like Mypy catch many errors before runtime without changing the language.",
            "Testing becomes critical—types are not verified until code runs.",
        ],
        "pitfalls": [
            "Runtime errors in production: typos or missing methods fail only when executed.",
            "Hard to refactor: method names are strings; IDEs cannot reliably find usages.",
            "Large codebases become hard to reason about without clear contracts.",
        ],
    },
}

# Grouped organization for courses
COURSE_STEPS_GROUPS = [
    {"label": "Phase 1 – Foundation",       "keys": ["step_1_memory_layout", "step_2_collections_generics", "step_3_function_paradigm", "step_4_error_philosophies"]},
    {"label": "Phase 2 – Type System & Idioms", "keys": ["step_5_type_system_interfaces", "step_6_strings_pattern_matching"]},
    {"label": "Phase 3 – Concurrency & I/O",  "keys": ["step_7_concurrency_model", "step_8_io_serialization"]},
    {"label": "Phase 4 – Algorithms & Architecture", "keys": ["step_9_sorting_pipelines", "step_10_testability_di"]},
]

# Pro Adaptation Course — 7 Levels
ADAPTATION_COURSE = [
    {
        "level": 1,
        "title": "The Container (Project Anatomy)",
        "description": "Learn how each language structures a project: build system, main entry point, dependencies.",
        "viewItems": ["project_lifecycle", "command_line_args", "environment_variables", "file_paths_and_directories"],
    },
    {
        "level": 2,
        "title": "The Data (Types & Nulls)",
        "description": "Understand fundamental types, null handling, and optional values.",
        "viewItems": ["type_system_comparison", "nullable_optional_values", "arrays_and_collections", "maps_and_sets", "collection_mappings"],
    },
    {
        "level": 3,
        "title": "The Flow (Logic)",
        "description": "Master control flow: conditionals, loops, and recursion.",
        "viewItems": ["conditions", "loops", "recursion", "functions_and_errors"],
    },
    {
        "level": 4,
        "title": "The Ownership (Memory)",
        "description": "Grasp how each language handles memory, allocation, and object lifetime.",
        "viewItems": ["memory_management", "classes_and_objects", "enums_and_constants"],
    },
    {
        "level": 5,
        "title": "The Abstraction (Interfaces)",
        "description": "Learn interfaces, polymorphism, and design patterns for extensibility.",
        "viewItems": ["interfaces_and_polymorphism", "structural_typing", "nominal_typing", "duck_typing", "type_system_comparison"],
    },
    {
        "level": 6,
        "title": "The Error (Reliability)",
        "description": "Handle errors elegantly and build for failure recovery.",
        "viewItems": ["exceptions_and_recovery", "functions_and_errors", "json_and_serialization", "file_io"],
    },
    {
        "level": 7,
        "title": "The Scaling (Concurrency)",
        "description": "Learn the concurrency models for each language and write parallel code.",
        "viewItems": ["concurrency_models", "hashing_and_checksums", "sorting_and_searching", "random_numbers"],
    },
]

COURSE_STEPS = {
    "step_1_memory_layout": {
        "label": "Step 1: Memory Layout & References",
        "description": "Understand how languages represent objects in memory and expose references/pointers differently.",
        "compareEntries": ["classes_and_objects"],
        "adapterInsight": "Notice how C++ requires explicit `new`/`delete` or smart pointers, Go uses value semantics by default with optional pointers, and Python hides allocation entirely. TypeScript inherits from JavaScript's garbage collection.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Common baseline\nint stack = 7;\nint* p = &stack;                  // explicit address/reference\nstd::unique_ptr<int> sp = std::make_unique<int>(42);\n\n// Additional ownership models\nint* raw = new int(10);           // manual ownership\ndelete raw;\nstd::shared_ptr<int> shared = std::make_shared<int>(9);\n\n// Additional memory-layout cues\nstruct Node { int x; double y; };\nNode n{1, 2.0};                   // value on stack by default",
            "python": "# Common baseline\nx = [1, 2, 3]\ny = x                             # same object reference\ny.append(4)\n\n# Additional identity/reference cues\na = {\"v\": 1}\nb = dict(a)                       # shallow copy\nassert a is not b                 # different object identity\n\n# Additional mutability cues\ncoords = (1, 2)                   # immutable tuple\nitems = [1, 2]                    # mutable list",
            "go": "// Common baseline\nv := 7\np := &v                           // pointer to value\n*p = 9\n\n// Additional value vs reference-like behavior\ntype User struct { Score int }\nu := User{Score: 1}               // copied by value\nup := &u; up.Score = 2            // mutate through pointer\n\n// Additional allocation cues\nb := make([]int, 0, 4)            // runtime-managed backing array",
            "typescript": "// Common baseline\nconst user = { score: 1 }\nconst alias = user                 // same object reference\nalias.score = 2\n\n// Additional primitive vs object behavior\nlet a = 1; let b = a; b = 2        // primitive copy\nconst left = { v: 1 }\nconst right = { ...left }          // shallow copy object\n\n// Additional mutability cues\nconst arr = [1, 2]; arr.push(3)    // mutable object via const binding",
            "scala2": "// Common baseline\nval a = List(1, 2, 3)\nval b = a                           // same immutable value\n\n// Additional immutability/mutability split\nval im = Vector(1, 2, 3)\nval im2 = im :+ 4                   // returns new value\nval mut = scala.collection.mutable.ArrayBuffer(1, 2)\nmut += 3\n\n// Additional reference cue\ncase class Box(var x: Int)",
            "scala3": "// Common baseline\nval a = List(1, 2, 3)\nval b = a                           // same immutable value\n\n// Additional immutability/mutability split\nval im = Vector(1, 2, 3)\nval im2 = im :+ 4                   // returns new value\nval mut = scala.collection.mutable.ArrayBuffer(1, 2)\nmut += 3\n\n// Additional reference cue\ncase class Box(var x: Int)"
        }
    },
    "step_2_collections_generics": {
        "label": "Step 2: Collections & Generics",
        "description": "Learn how each language optimizes arrays, maps, and expresses generic (parameterized) types.",
        "compareEntries": ["arrays_and_collections", "maps_and_sets", "iterator"],
        "adapterInsight": "Compare C++ templates vs Python's duck typing vs TypeScript's generics. See how Go's `interface{}` differs from Java's `Object`-based erasure. Scala uses type classes for ad-hoc polymorphism. Trade-off lens: ordered/tree containers give stable order and typically O(log n) updates; unordered/hash containers prioritize average O(1) lookup; queue/stack families optimize access pattern (FIFO/LIFO) over random access.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Common baseline\nstd::vector<int> nums{1, 2, 3};\nstd::unordered_map<std::string, int> freq{{\"a\", 1}};\ntemplate <typename T> T first(const std::vector<T>& v) { return v[0]; }\n\n// Ordered / tree-based\nstd::map<std::string, int> ordered;\nstd::set<int> uniq{3, 1, 2};\n\n// Unordered / hash-based\nstd::unordered_map<std::string, int> fastFreq;\nstd::unordered_set<int> fastSet{1, 2, 3};\n\n// Queue / stack / sequence extras\nstd::array<int, 3> fixed{1, 2, 3};\nstd::list<int> linked{1, 2, 3};\nstd::queue<int> q; q.push(10);\nstd::stack<int> st; st.push(42);",
            "python": "# Common baseline\nnums: list[int] = [1, 2, 3]\nfreq: dict[str, int] = {\"a\": 1}\ndef first(v): return v[0]\n\n# Ordered-ish / sorted usage\nrecords = [{\"k\": 2}, {\"k\": 1}]\nrecords_sorted = sorted(records, key=lambda x: x[\"k\"])\n\n# Unordered / hash-based\nunique = {1, 2, 3}\nindex = {\"alice\": 0, \"bob\": 1}\n\n# Queue / stack / utility containers\nfrom collections import deque, Counter, defaultdict\nq = deque([1, 2, 3])\nstack = [1, 2, 3]; stack.append(4); stack.pop()\ncnt = Counter([\"a\", \"b\", \"a\"])\ngroups = defaultdict(list)",
            "go": "// Common baseline\nnums := []int{1, 2, 3}\nfreq := map[string]int{\"a\": 1}\nfunc First[T any](v []T) T { return v[0] }\n\n// Ordered / sorted view\nkeys := []string{\"b\", \"a\"}\nsort.Strings(keys) // iterate maps in sorted key order\n\n// Unordered / hash-based\nset := map[int]struct{}{1: {}, 2: {}}\nindex := map[string]int{\"alice\": 0}\n\n// Queue / stack / fixed-size\narr := [3]int{1, 2, 3}\nq := []int{}; q = append(q, 10); q = q[1:]\nst := []int{}; st = append(st, 42); st = st[:len(st)-1]",
            "typescript": "// Common baseline\nconst nums: number[] = [1, 2, 3]\nconst freq: Record<string, number> = { a: 1 }\nfunction first<T>(v: T[]): T { return v[0] }\n\n// Ordered / insertion-ordered maps\nconst ordered = new Map<string, number>()\nordered.set(\"b\", 2); ordered.set(\"a\", 1)\n\n// Unordered/hash-like object index\nconst index: Record<string, number> = { alice: 0, bob: 1 }\nconst unique = new Set<number>([1, 2, 3])\n\n// Queue / stack / tuple extras\nconst tuple: [number, string] = [1, \"x\"]\nconst queue: number[] = []; queue.push(1); queue.shift()\nconst stack: number[] = []; stack.push(1); stack.pop()",
            "scala2": "// Common baseline\nval nums: Vector[Int] = Vector(1, 2, 3)\nval freq: Map[String, Int] = Map(\"a\" -> 1)\ndef first[T](v: Vector[T]): T = v.head\n\n// Ordered / sorted\nval sortedMap = scala.collection.immutable.SortedMap(\"b\" -> 2, \"a\" -> 1)\nval sortedSet = scala.collection.immutable.SortedSet(3, 1, 2)\n\n// Hash-based defaults\nval hashMap = scala.collection.immutable.HashMap(\"a\" -> 1)\nval hashSet = scala.collection.immutable.HashSet(1, 2, 3)\n\n// Queue / stack / sequence extras\nval linked: List[Int] = List(1, 2, 3)\nval queue = scala.collection.immutable.Queue(1, 2, 3)\nval arr: Array[Int] = Array(1, 2, 3)",
            "scala3": "// Common baseline\nval nums: Vector[Int] = Vector(1, 2, 3)\nval freq: Map[String, Int] = Map(\"a\" -> 1)\ndef first[T](v: Vector[T]): T = v.head\n\n// Ordered / sorted\nval sortedMap = scala.collection.immutable.SortedMap(\"b\" -> 2, \"a\" -> 1)\nval sortedSet = scala.collection.immutable.SortedSet(3, 1, 2)\n\n// Hash-based defaults\nval hashMap = scala.collection.immutable.HashMap(\"a\" -> 1)\nval hashSet = scala.collection.immutable.HashSet(1, 2, 3)\n\n// Queue / stack / sequence extras\nval linked: List[Int] = List(1, 2, 3)\nval queue = scala.collection.immutable.Queue(1, 2, 3)\nval arr: Array[Int] = Array(1, 2, 3)"
        }
    },
    "step_3_function_paradigm": {
        "label": "Step 3: The Function Paradigm",
        "description": "Learn how languages treat functions: as first-class values, callable objects, or structured procedures.",
        "compareEntries": ["functions_and_errors", "strategy"],
        "adapterInsight": "In Scala and TypeScript, functions are first-class. In C++, use `std::function`. In Go, functions are values passed as interface{}. Understand closures and how each captures environment.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Common baseline\nint offset = 2;\nstd::function<int(int)> add = [offset](int x) { return x + offset; };\nint y = add(5);\n\n// Additional higher-order use\nauto apply = [](int v, const std::function<int(int)>& f) { return f(v); };\nint z = apply(10, add);\n\n// Additional strategy-style dispatch\nstd::function<int(int, int)> op = [](int a, int b) { return a + b; };",
            "python": "# Common baseline\noffset = 2\nadd = lambda x: x + offset\ny = add(5)\n\n# Additional higher-order use\ndef apply(v, f):\n    return f(v)\nz = apply(10, add)\n\n# Additional strategy-style dispatch\nops = {\"add\": lambda a, b: a + b, \"mul\": lambda a, b: a * b}",
            "go": "// Common baseline\noffset := 2\nadd := func(x int) int { return x + offset }\ny := add(5)\n\n// Additional higher-order use\napply := func(v int, f func(int) int) int { return f(v) }\nz := apply(10, add)\n\n// Additional strategy-style dispatch\nops := map[string]func(int, int) int{\"add\": func(a, b int) int { return a + b }}",
            "typescript": "// Common baseline\nconst offset = 2\nconst add = (x: number) => x + offset\nconst y = add(5)\n\n// Additional higher-order use\nconst apply = (v: number, f: (n: number) => number) => f(v)\nconst z = apply(10, add)\n\n// Additional strategy-style dispatch\nconst ops: Record<string, (a: number, b: number) => number> = { add: (a, b) => a + b }",
            "scala2": "// Common baseline\nval offset = 2\nval add: Int => Int = x => x + offset\nval y = add(5)\n\n// Additional higher-order use\ndef apply(v: Int, f: Int => Int): Int = f(v)\nval z = apply(10, add)\n\n// Additional strategy-style dispatch\nval ops: Map[String, (Int, Int) => Int] = Map(\"add\" -> ((a, b) => a + b))",
            "scala3": "// Common baseline\nval offset = 2\nval add: Int => Int = x => x + offset\nval y = add(5)\n\n// Additional higher-order use\ndef apply(v: Int, f: Int => Int): Int = f(v)\nval z = apply(10, add)\n\n// Additional strategy-style dispatch\nval ops: Map[String, (Int, Int) => Int] = Map(\"add\" -> ((a, b) => a + b))"
        }
    },
    "step_4_error_philosophies": {
        "label": "Step 4: Error Philosophies",
        "description": "Compare how languages handle errors: exceptions, error returns, type-driven approaches, or panics.",
        "compareEntries": ["exceptions_and_recovery"],
        "adapterInsight": "Go and C++23 treat errors as values. Python, TypeScript, and Scala 2 use exceptions. Scala 3 uses Option/Either for type-safe error handling. Pick the right pattern for your context.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Common baseline (value-style)\nstd::optional<int> parse(std::string s) { /* ... */ }\nauto v = parse(\"42\");\nif (!v) { /* handle missing/error */ }\n\n// Additional exception-style\ntry {\n    int n = std::stoi(\"bad\");\n} catch (const std::exception& ex) {\n    /* handle */\n}",
            "python": "# Common baseline (exception-style)\ntry:\n    v = int(text)\nexcept ValueError:\n    v = None\n\n# Additional value-style fallback\ndef parse_int(s: str) -> int | None:\n    return int(s) if s.isdigit() else None",
            "go": "// Common baseline (error return)\nv, err := strconv.Atoi(text)\nif err != nil {\n    // handle error path\n}\n\n// Additional panic/recover boundary (rare)\nfunc safeRun(fn func()) (err error) {\n    defer func() { if r := recover(); r != nil { err = fmt.Errorf(\"panic: %v\", r) } }()\n    fn(); return nil\n}",
            "typescript": "// Common baseline (union result)\nfunction parse(text: string): number | null {\n  const n = Number(text)\n  return Number.isNaN(n) ? null : n\n}\n\n// Additional exception-style\ntry {\n  const n = JSON.parse(payload)\n} catch (e) {\n  // handle parse failure\n}",
            "scala2": "// Common baseline (Try/Option)\nval parsed = scala.util.Try(text.toInt).toOption\nparsed.getOrElse(0)\n\n// Additional Either modeling\nval e: Either[String, Int] = parsed.toRight(\"invalid\")",
            "scala3": "// Common baseline (Either)\nval parsed: Either[String, Int] =\n  text.toIntOption.toRight(\"invalid int\")\n\n// Additional exception bridge\nimport scala.util.Try\nval t = Try(text.toInt).toEither.left.map(_.getMessage)"
        }
    },
    "step_5_type_system_interfaces": {
        "label": "Step 5: Type System & Interfaces",
        "description": "Understand how each language defines contracts between types: nominal vs structural typing, traits, interfaces, and type classes.",
        "compareEntries": ["interfaces_and_polymorphism", "type_system_comparison"],
        "adapterInsight": "C++ uses virtual dispatch (nominal) and concepts (structural, compile-time). Go interfaces are structural — any type satisfying the method set qualifies implicitly. TypeScript is also structural. Scala uses traits with explicit `extends` (nominal) but type classes (`given`/`using`) for ad-hoc structural polymorphism. Python uses duck typing at runtime.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Nominal + virtual dispatch\nstruct Animal { virtual std::string speak() const = 0; };\nstruct Dog : Animal { std::string speak() const override { return \"woof\"; } };\n\n// Structural / concepts (C++20)\ntemplate <typename T>\nconcept Speakable = requires(T t) { { t.speak() } -> std::convertible_to<std::string>; };\n\ntemplate <Speakable T> void greet(T& a) { std::cout << a.speak(); }",
            "python": "# Duck typing — no declaration needed\nclass Dog:\n    def speak(self) -> str: return \"woof\"\n\ndef greet(animal) -> None:\n    print(animal.speak())   # works for anything with speak()\n\n# Structural hint with Protocol (Python 3.8+)\nfrom typing import Protocol\nclass Speakable(Protocol):\n    def speak(self) -> str: ...",
            "go": "// Structural: implicit interface satisfaction\ntype Speakable interface { Speak() string }\n\ntype Dog struct{}\nfunc (Dog) Speak() string { return \"woof\" }\n\nfunc Greet(a Speakable) { fmt.Println(a.Speak()) }\n// Dog satisfies Speakable without 'implements' keyword",
            "typescript": "// Structural: compatible shape satisfies the interface\ninterface Speakable { speak(): string }\n\nclass Dog { speak() { return 'woof' } }\n\nfunction greet(a: Speakable) { console.log(a.speak()) }\ngreet(new Dog())   // OK — shape matches\n\n// Generic constraint\nfunction first<T extends { id: number }>(arr: T[]): T { return arr[0] }",
            "scala2": "// Nominal with traits\ntrait Speakable { def speak(): String }\nclass Dog extends Speakable { def speak() = \"woof\" }\n\n// Type class (ad-hoc polymorphism)\ntrait Show[A] { def show(a: A): String }\nimplicit val showDog: Show[Dog] = (d: Dog) => s\"Dog(${d.speak()})\"",
            "scala3": "// Nominal with traits\ntrait Speakable:\n  def speak(): String\nclass Dog extends Speakable:\n  def speak() = \"woof\"\n\n// Type class with givens\ntrait Show[A]:\n  def show(a: A): String\ngiven Show[Dog] with\n  def show(d: Dog) = s\"Dog(${d.speak()})\""
        }
    },
    "step_6_strings_pattern_matching": {
        "label": "Step 6: Strings & Pattern Matching",
        "description": "Explore string ergonomics and how each language expresses branching on values or structure — from switch/case to destructuring match expressions.",
        "compareEntries": ["strings", "conditions"],
        "adapterInsight": "C++ strings are mutable byte arrays; formatting requires `std::format` (C++20) or `snprintf`. Python and Go treat strings as immutable UTF-8 sequences. TypeScript template literals are concise. Scala/Kotlin pattern matching is exhaustive and works on case classes. Python 3.10+ `match` brings structural matching.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// String basics\nstd::string name = \"Alice\";\nstd::string greeting = \"Hello, \" + name + \"!\";\nstd::string upper = name; std::transform(upper.begin(), upper.end(), upper.begin(), ::toupper);\n\n// Pattern-style branching\nint code = 2;\nswitch (code) {\n  case 1: std::cout << \"one\"; break;\n  case 2: std::cout << \"two\"; break;\n  default: std::cout << \"other\"; break;\n}",
            "python": "# String basics\nname = \"Alice\"\ngreeting = f\"Hello, {name}!\"\nupper = name.upper()\n\n# Pattern matching (Python 3.10+)\nmatch code:\n    case 1: print(\"one\")\n    case 2: print(\"two\")\n    case _: print(\"other\")\n\n# Structural match\nmatch point:\n    case (0, 0): print(\"origin\")\n    case (x, 0): print(f\"on x-axis at {x}\")",
            "go": "// String basics\nname := \"Alice\"\ngreeting := fmt.Sprintf(\"Hello, %s!\", name)\nupper := strings.ToUpper(name)\n\n// Switch (no fallthrough by default)\nswitch code {\ncase 1: fmt.Println(\"one\")\ncase 2: fmt.Println(\"two\")\ndefault: fmt.Println(\"other\")\n}\n\n// Type switch\nswitch v := x.(type) {\ncase int: fmt.Println(\"int\", v)\ncase string: fmt.Println(\"string\", v)\n}",
            "typescript": "// String basics\nconst name = 'Alice'\nconst greeting = `Hello, ${name}!`\nconst upper = name.toUpperCase()\n\n// Switch\nswitch (code) {\n  case 1: console.log('one'); break\n  case 2: console.log('two'); break\n  default: console.log('other')\n}\n\n// Discriminated union narrowing\ntype Shape = { kind: 'circle'; r: number } | { kind: 'rect'; w: number; h: number }\nfunction area(s: Shape) {\n  switch (s.kind) {\n    case 'circle': return Math.PI * s.r ** 2\n    case 'rect':   return s.w * s.h\n  }\n}",
            "scala2": "// String basics\nval name = \"Alice\"\nval greeting = s\"Hello, $name!\"\nval upper = name.toUpperCase\n\n// Pattern match on values\ncode match {\n  case 1 => println(\"one\")\n  case 2 => println(\"two\")\n  case _ => println(\"other\")\n}\n\n// Structural + guard\npoint match {\n  case (0, 0)      => \"origin\"\n  case (x, 0)      => s\"x-axis $x\"\n  case (x, y) if x == y => \"diagonal\"\n}",
            "scala3": "// String basics\nval name = \"Alice\"\nval greeting = s\"Hello, $name!\"\nval upper = name.toUpperCase\n\n// Pattern match on values\ncode match\n  case 1 => println(\"one\")\n  case 2 => println(\"two\")\n  case _ => println(\"other\")\n\n// Structural + guard\npoint match\n  case (0, 0)       => \"origin\"\n  case (x, 0)       => s\"x-axis $x\"\n  case (x, y) if x == y => \"diagonal\""
        }
    },
    "step_7_concurrency_model": {
        "label": "Step 7: Concurrency Model",
        "description": "Compare the core concurrency primitives: OS threads, goroutines, async/await, and Futures/Promises.",
        "compareEntries": [],
        "adapterInsight": "C++ uses OS threads with mutexes/condition variables and `std::async` for task-based work. Go's goroutines are lightweight M:N user-space threads coordinated via channels. Python has the GIL: use `asyncio` for I/O concurrency or `multiprocessing` for CPU work. TypeScript/Node is single-threaded with an event loop — `async/await` suspends without blocking. Scala Futures run on an ExecutionContext (thread pool).",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Thread + mutex\nstd::mutex mu;\nstd::vector<int> results;\nstd::thread t([&]() {\n    std::lock_guard<std::mutex> lk(mu);\n    results.push_back(42);\n});\nt.join();\n\n// Task-based (async / future)\nstd::future<int> f = std::async(std::launch::async, []() { return 7; });\nint v = f.get();",
            "python": "# asyncio — cooperative, single-threaded I/O concurrency\nimport asyncio\nasync def fetch(url: str) -> str:\n    await asyncio.sleep(0)   # yield control\n    return url\n\nasync def main():\n    results = await asyncio.gather(fetch(\"a\"), fetch(\"b\"))\n\n# Thread for CPU / blocking work\nfrom threading import Thread\nt = Thread(target=lambda: print(\"from thread\"))\nt.start(); t.join()",
            "go": "// Goroutine + channel (CSP model)\nch := make(chan int)\ngo func() { ch <- 42 }()\nv := <-ch\n\n// WaitGroup for fan-out\nvar wg sync.WaitGroup\nfor i := 0; i < 3; i++ {\n    wg.Add(1)\n    go func(id int) {\n        defer wg.Done()\n        fmt.Println(id)\n    }(i)\n}\nwg.Wait()",
            "typescript": "// async/await — event-loop, non-blocking I/O\nasync function fetchData(url: string): Promise<string> {\n  const res = await fetch(url)\n  return res.text()\n}\n\n// Concurrent tasks\nconst [a, b] = await Promise.all([fetchData('x'), fetchData('y')])\n\n// Structured sequential chain\nconst result = await Promise.resolve(1)\n  .then(v => v + 1)\n  .then(v => v * 2)",
            "scala2": "import scala.concurrent.{Future, Await}\nimport scala.concurrent.ExecutionContext.Implicits.global\nimport scala.concurrent.duration._\n\n// Future — runs on thread pool\nval f: Future[Int] = Future { 7 + 1 }\nval v = Await.result(f, 2.seconds)\n\n// Parallel composition\nval result = for {\n  a <- Future { 1 }\n  b <- Future { 2 }\n} yield a + b",
            "scala3": "import scala.concurrent.{Future, Await}\nimport scala.concurrent.ExecutionContext.Implicits.global\nimport scala.concurrent.duration.*\n\n// Future — runs on thread pool\nval f: Future[Int] = Future { 7 + 1 }\nval v = Await.result(f, 2.seconds)\n\n// Parallel composition\nval result =\n  for\n    a <- Future { 1 }\n    b <- Future { 2 }\n  yield a + b"
        }
    },
    "step_8_io_serialization": {
        "label": "Step 8: I/O & Serialization",
        "description": "Compare file I/O patterns, standard streams, and JSON serialization across languages.",
        "compareEntries": ["file_io", "json_and_serialization"],
        "adapterInsight": "C++ I/O is buffered stream-based (`fstream`) with manual error checking. Python's `open()` + context manager is idiomatic. Go uses `os.Open` + `bufio` and separates concerns clearly. TypeScript (Node) has `fs.readFileSync`/`fs/promises`. JSON serialization is built-in for Python/TS/Go; C++ requires a library (nlohmann/json, etc.).",
        "sourceLinks": [],
        "codes": {
            "cpp": "// File read\n#include <fstream>\nstd::ifstream ifs(\"data.txt\");\nstd::string line;\nwhile (std::getline(ifs, line)) { /* process */ }\n\n// JSON (nlohmann/json)\n#include <nlohmann/json.hpp>\nauto j = nlohmann::json::parse(R\"({\"name\":\"Ada\"})\");\nstd::string name = j[\"name\"];",
            "python": "# File read\nwith open(\"data.txt\") as f:\n    lines = f.readlines()\n\n# JSON\nimport json\nobj = json.loads('{\"name\": \"Ada\"}')\nname = obj[\"name\"]\nout = json.dumps(obj, indent=2)",
            "go": "// File read\ndata, err := os.ReadFile(\"data.txt\")\nif err != nil { log.Fatal(err) }\nlines := strings.Split(string(data), \"\\n\")\n\n// JSON\ntype User struct { Name string `json:\"name\"` }\nvar u User\njson.Unmarshal([]byte(`{\"name\":\"Ada\"}`), &u)\nout, _ := json.Marshal(u)",
            "typescript": "// File read (Node)\nimport { readFileSync } from 'fs'\nconst text = readFileSync('data.txt', 'utf-8')\nconst lines = text.split('\\n')\n\n// JSON\nconst obj = JSON.parse('{\"name\":\"Ada\"}') as { name: string }\nconst out = JSON.stringify(obj, null, 2)",
            "scala2": "// File read\nimport scala.io.Source\nval lines = Source.fromFile(\"data.txt\").getLines().toList\n\n// JSON (play-json or circe)\nimport play.api.libs.json._\nval j: JsValue = Json.parse(\"{\\\"name\\\":\\\"Ada\\\"}\")",
            "scala3": "// File read\nimport scala.io.Source\nval lines = Source.fromFile(\"data.txt\").getLines().toList\n\n// JSON (circe — Scala 3 idiomatic)\nimport io.circe.parser.*\nval result = parse(\"{\\\"name\\\":\\\"Ada\\\"}\")   // Either[ParsingFailure, Json]"
        }
    },
    "step_9_sorting_pipelines": {
        "label": "Step 9: Sorting & Data Pipelines",
        "description": "Compare how each language chains collection transforms — sorting, filtering, mapping, and reducing — and uses heaps for priority selection.",
        "compareEntries": ["sorting_and_searching", "heaps_and_priority_queues"],
        "adapterInsight": "C++ uses STL algorithms (`std::sort`, `std::transform`, ranges in C++20). Python list/generator comprehensions and `sorted()` are concise. Go favors explicit loops with `sort.Slice`. TypeScript array methods (`.filter`, `.map`, `.reduce`) are chainable. Scala has the most expressive pipeline via `map`/`filter`/`foldLeft` on immutable collections and lazy `LazyList`.",
        "sourceLinks": [],
        "codes": {
            "cpp": "std::vector<int> nums{5, 3, 1, 4, 2};\nstd::sort(nums.begin(), nums.end());\n\n// Transform + filter (C++20 ranges)\nnamespace rv = std::ranges::views;\nauto evens = nums | rv::filter([](int x){ return x % 2 == 0; });\nauto doubled = evens | rv::transform([](int x){ return x * 2; });\n\n// Priority queue (max-heap)\nstd::priority_queue<int> pq;\nfor (int v : nums) pq.push(v);\nint top = pq.top();",
            "python": "nums = [5, 3, 1, 4, 2]\nsorted_nums = sorted(nums)\n\n# Pipeline via comprehension\ndoubled_evens = [x * 2 for x in nums if x % 2 == 0]\n\n# Reduce\nfrom functools import reduce\ntotal = reduce(lambda acc, x: acc + x, nums, 0)\n\n# Min-heap\nimport heapq\nheap = nums[:]\nheapq.heapify(heap)\ntop = heapq.heappop(heap)",
            "go": "nums := []int{5, 3, 1, 4, 2}\nsort.Ints(nums)\n\n// Explicit pipeline via loop\ndoubledEvens := []int{}\nfor _, v := range nums {\n    if v%2 == 0 { doubledEvens = append(doubledEvens, v*2) }\n}\n\n// sort.Slice for custom key\npeople := []struct{ Name string; Age int }{{\"Bob\", 2}, {\"Ana\", 1}}\nsort.Slice(people, func(i, j int) bool { return people[i].Age < people[j].Age })",
            "typescript": "const nums = [5, 3, 1, 4, 2]\nconst sorted = [...nums].sort((a, b) => a - b)\n\n// Chainable pipeline\nconst result = nums\n  .filter(x => x % 2 === 0)\n  .map(x => x * 2)\n  .reduce((acc, x) => acc + x, 0)\n\n// Min-heap via sorted array (no built-in)\nconst heap = [...nums].sort((a, b) => a - b)\nconst top = heap[0]",
            "scala2": "val nums = List(5, 3, 1, 4, 2)\nval sorted = nums.sorted\n\n// Expressive pipeline\nval result = nums\n  .filter(_ % 2 == 0)\n  .map(_ * 2)\n  .foldLeft(0)(_ + _)\n\n// Priority queue\nimport scala.collection.mutable\nval pq = mutable.PriorityQueue[Int]()\nnums.foreach(pq.enqueue(_))\nval top = pq.dequeue()",
            "scala3": "val nums = List(5, 3, 1, 4, 2)\nval sorted = nums.sorted\n\n// Expressive pipeline\nval result = nums\n  .filter(_ % 2 == 0)\n  .map(_ * 2)\n  .foldLeft(0)(_ + _)\n\n// Lazy evaluation\nval lazy = LazyList.from(1).filter(_ % 2 == 0).take(5).toList"
        }
    },
    "step_10_testability_di": {
        "label": "Step 10: Testability & Dependency Inversion",
        "description": "Learn how to design swappable seams: constructor injection, interface mocking, and test doubles — the practical application of SOLID's DIP.",
        "compareEntries": ["interfaces_and_polymorphism"],
        "adapterInsight": "The common thread: inject an abstraction, swap in a test double. C++ uses virtual interfaces or template policy injection. Go's small implicit interfaces make mocking trivial. Python replaces any callable at runtime. TypeScript uses structural interfaces — any matching shape works. Scala leverages traits and implicit/given for type class injection.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Interface + constructor injection\nstruct EmailSender { virtual void send(const std::string& msg) = 0; virtual ~EmailSender() = default; };\nstruct Service {\n    explicit Service(std::shared_ptr<EmailSender> s) : sender_(s) {}\n    void notify() { sender_->send(\"hello\"); }\nprivate:\n    std::shared_ptr<EmailSender> sender_;\n};\n\n// Test double\nstruct FakeSender : EmailSender {\n    std::vector<std::string> sent;\n    void send(const std::string& msg) override { sent.push_back(msg); }\n};",
            "python": "# Protocol-based injection\nfrom typing import Protocol\nclass EmailSender(Protocol):\n    def send(self, msg: str) -> None: ...\n\nclass Service:\n    def __init__(self, sender: EmailSender) -> None:\n        self._sender = sender\n    def notify(self) -> None:\n        self._sender.send(\"hello\")\n\n# Test double\nclass FakeSender:\n    sent: list[str] = []\n    def send(self, msg: str) -> None: self.sent.append(msg)",
            "go": "// Small interface + injection\ntype EmailSender interface { Send(msg string) }\n\ntype Service struct { sender EmailSender }\nfunc (s Service) Notify() { s.sender.Send(\"hello\") }\n\n// Test double — satisfies interface implicitly\ntype fakeSender struct { sent []string }\nfunc (f *fakeSender) Send(msg string) { f.sent = append(f.sent, msg) }\n\n// Usage in test\nsvc := Service{sender: &fakeSender{}}",
            "typescript": "// Interface + injection\ninterface EmailSender { send(msg: string): void }\n\nclass Service {\n  constructor(private sender: EmailSender) {}\n  notify() { this.sender.send('hello') }\n}\n\n// Test double — structural match\nconst fake: EmailSender = { send: jest.fn() }\nconst svc = new Service(fake)\nsvc.notify()\nexpect(fake.send).toHaveBeenCalledWith('hello')",
            "scala2": "// Trait + constructor injection\ntrait EmailSender { def send(msg: String): Unit }\n\nclass Service(sender: EmailSender) {\n  def notify(): Unit = sender.send(\"hello\")\n}\n\n// Test double\nclass FakeSender extends EmailSender {\n  val sent = scala.collection.mutable.Buffer[String]()\n  def send(msg: String): Unit = sent += msg\n}",
            "scala3": "// Trait + constructor injection\ntrait EmailSender:\n  def send(msg: String): Unit\n\nclass Service(sender: EmailSender):\n  def notify(): Unit = sender.send(\"hello\")\n\n// Test double\nclass FakeSender extends EmailSender:\n  val sent = scala.collection.mutable.Buffer[String]()\n  def send(msg: String): Unit = sent += msg"
        }
    }
}

# Grouped organization for workflows (empty for now)
WORKFLOW_GROUPS = []

WORKFLOW = {
    "package_manager": {
        "label": "Package Manager",
        "description": "How each ecosystem manages third-party dependencies and versions.",
        "codes": {
            "cpp": "vcpkg / conan",
            "python": "pip / poetry",
            "go": "go mod",
            "typescript": "npm / yarn / pnpm",
            "scala2": "sbt / mill",
            "scala3": "sbt / scala-cli"
        }
    },
    "entry_point": {
        "label": "Entry Point & Execution",
        "description": "How to structure a runnable program and define the starting point.",
        "codes": {
            "cpp": "int main(int argc, char** argv) { /* code */ }",
            "python": "if __name__ == '__main__': # code",
            "go": "func main() { /* code */ } // inside package main",
            "typescript": "// Top-level or main() in a script; executed after imports",
            "scala2": "object Main extends App { /* code */ }",
            "scala3": "@main def run(): Unit = /* code */"
        }
    },
    "build_run": {
        "label": "Build & Run Workflow",
        "description": "Compile, link, or interpret; how to prepare code for execution.",
        "codes": {
            "cpp": "g++ main.cpp -o app && ./app",
            "python": "python main.py",
            "go": "go run main.go",
            "typescript": "ts-node main.ts",
            "scala2": "sbt 'run'",
            "scala3": "scala-cli main.scala"
        }
    }
}

# Adapter insights for key problems: highlights language/paradigm differences
ADAPTER_INSIGHTS = {
    "balanced_brackets": {
        "insight": "Compare stack data structures: C++ std::stack vs Python list vs Go slice. Notice recursion vs iteration trade-offs: C++ prefers explicit stacks to avoid stack overflow; Python and JavaScript use call stacks more freely. TypeScript resembles JavaScript; Go's simplicity favors explicit loops.",
        "compareEntries": []
    },
    "word_count": {
        "insight": "Map/dictionary patterns diverge significantly: C++ std::unordered_map, Python dict, Go map, TypeScript Map/Object. Observe how each language handles iteration order, hash collisions, and performance. Python's Counter is idiomatic; C++ requires explicit iteration.",
        "compareEntries": []
    },
    "matrix_mul": {
        "insight": "Nested loops reveal cache and memory patterns. C++ row-major layout; Python NumPy optimizations. Contrast eager 2D arrays (C++, Go) vs built-in matrix libraries (Python). Notice type signatures: C++ templates for generics, Python duck typing, TypeScript compile-time types.",
        "compareEntries": []
    },
    "top_k_frequent": {
        "insight": "Sorting and heap/priority queue usage: C++ priority_queue (max-heap by default), Python heapq (min-heap with negation trick), Go sort.Slice with custom comparator, TypeScript sort. See how each language expresses frequency counting (counter dict/map) vs selection (heap or sort).",
        "compareEntries": []
    }
}

# Phase 4: Basics enhancements for mental-model mapping and migration guidance
BASICS_ENHANCEMENTS = {
    "nullable_optional_values": {
        "adapterInsight": {
            "title": "Null / Optional Rosetta",
            "headers": ["Language", "Null Token", "Preferred Optional", "Mini Pattern"],
            "rows": [
                ["C++", "nullptr", "std::optional<T>", "std::optional<int> age = std::nullopt;"],
                ["Python", "None", "None + typing.Optional", "age: int | None = None"],
                ["Go", "nil", "(T, error) / nil pointer", "var p *User = nil"],
                ["TypeScript", "null / undefined", "union types", "let age: number | null = null"],
                ["Scala", "null (interop)", "Option[T] (Some/None)", "val age: Option[Int] = None"]
            ]
        },
    },
    "type_system_comparison": {
        "label": "type_system_comparison",
        "description": "Type system snapshot across languages used in this atlas.",
        "adapterInsight": "Use this as a context switch cheat: nominal vs structural typing, and static vs dynamic guarantees, changes how you design APIs and tests.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// C++: static + nominal + compile-time evaluation\nconstexpr int a = 2;      // compile-time constant\nstruct UserId { int v; }; // nominal wrapper type\n// UserId is not interchangeable with int by default",
            "python": "# Python: dynamic duck typing (hints are optional)\ndef twice(x):\n    return x * 2           # works for int, str, list, ...\nname: str = \"Ada\"        # type hint for tools, not hard runtime enforcement",
            "go": "// Go: static + structural interfaces\ntype Reader interface { Read([]byte) (int, error) }\ntype File struct{}\nfunc (File) Read([]byte) (int, error) { return 0, nil } // File satisfies Reader implicitly",
            "typescript": "// TypeScript: static structural types, JS runtime\ntype HasId = { id: number }\nconst u = { id: 1, name: \"Ada\" }\nconst x: HasId = u         // allowed by structure (extra fields are fine)",
            "scala2": "// Scala 2: static strong typing with inference + implicits\nval n = 2                  // inferred Int\ntrait Show[T] { def show(v: T): String }\nimplicit val showInt: Show[Int] = (v: Int) => v.toString",
            "scala3": "// Scala 3: static strong typing with givens/using\nval n = 2                  // inferred Int\ntrait Show[T]:\n  def show(v: T): String\ngiven Show[Int] with\n  def show(v: Int): String = v.toString"
        }
    },
    "scala_migration": {
        "label": "scala_migration",
        "description": "Scala 2 to Scala 3 bridge: the most visible syntax and abstraction shifts.",
        "adapterInsight": "Treat Scala 3 as an ergonomic evolution: same core FP/OOP model, but cleaner syntax and clearer contextual abstractions.",
        "sourceLinks": [],
        "codes": {
            "scala2": "implicit val ec: ExecutionContext = ExecutionContext.global\n\ntrait Repo(name: String)\n\nval x = {\n  val a = 1\n  a + 1\n}",
            "scala3": "given ExecutionContext = ExecutionContext.global\n\ntrait Repo(name: String)\n\nval x =\n  val a = 1\n  a + 1",
            "cpp": "Bridge note: this entry focuses on Scala 2 -> 3 migration only.",
            "python": "Bridge note: this entry focuses on Scala 2 -> 3 migration only.",
            "go": "Bridge note: this entry focuses on Scala 2 -> 3 migration only.",
            "typescript": "Bridge note: this entry focuses on Scala 2 -> 3 migration only."
        }
    },
    "project_lifecycle": {
        "label": "project_lifecycle",
        "description": "Project structure, build system, and main entry points across languages.",
        "adapterInsight": "Every language has a different philosophy: C++ is modular; Go is simplicity; Python is flexibility; TypeScript mirrors Node conventions; Scala bridges JVM tooling.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// CMakeLists.txt\ncmake_minimum_required(VERSION 3.15)\nproject(MyApp)\nadd_executable(main src/main.cpp)\n\n// src/main.cpp\nint main() { return 0; }\n\n// Build: mkdir build && cd build && cmake .. && make",
            "python": "# pyproject.toml (modern PEP 517)\n[project]\nname = \"my_app\"\nversion = \"0.1.0\"\n\n# main.py\nif __name__ == \"__main__\":\n    print(\"Hello\")\n\n# Run: python main.py",
            "go": "// go.mod\nmodule example.com/my_app\n\ngo 1.21\n\n// main.go\npackage main\n\nfunc main() {\n    println(\"Hello\")\n}\n\n// Run: go run main.go",
            "typescript": "// package.json\n{\n  \"name\": \"my_app\",\n  \"type\": \"module\",\n  \"main\": \"dist/index.js\"\n}\n\n// tsconfig.json\n{ \"compilerOptions\": { \"target\": \"ES2020\" } }\n\n// index.ts\nconsole.log(\"Hello\")",
            "scala2": "// build.sbt\nname := \"my_app\"\nversion := \"0.1.0\"\nscalaVersion := \"2.13.12\"\n\n// src/main/scala/Main.scala\nobject Main {\n  def main(args: Array[String]): Unit = println(\"Hello\")\n}",
            "scala3": "// build.sbt\nname := \"my_app\"\nversion := \"0.1.0\"\nscalaVersion := \"3.3.0\"\n\n// src/main/scala/Main.scala\n@main def hello(): Unit = println(\"Hello\")"
        }
    },
    "collection_mappings": {
        "label": "collection_mappings",
        "description": "Equivalent collection types across languages: the Rosetta Stone for data structures.",
        "adapterInsight": "Use this table to quickly find the right data structure in your target language. Performance characteristics vary: dynamic arrays are fast for append; linked lists are fast for insertion; hash maps prioritize lookup speed.",
        "sourceLinks": [],
        "codes": {
            "cpp": "// Common patterns\nstd::vector<int> v{1, 2, 3};\nstd::unordered_map<std::string, int> m{{\"a\", 1}};\nstd::set<int> s{3, 1, 2};\nstd::list<int> lst{1, 2, 3};\nstd::array<int, 3> arr{1, 2, 3};",
            "python": "# Common patterns\nv = [1, 2, 3]\nm = {\"a\": 1}\ns = {3, 1, 2}\nfrom collections import deque\nq = deque([1, 2, 3])\narr = (1, 2, 3)  # immutable",
            "go": "// Common patterns\nv := []int{1, 2, 3}\nm := map[string]int{\"a\": 1}\ns := map[int]struct{}{1: {}, 2: {}}\n// container/list for linked list\nimport \"container/list\"\nq := list.New()",
            "typescript": "// Common patterns\nconst v: number[] = [1, 2, 3]\nconst m: Record<string, number> = { a: 1 }\nconst s = new Set<number>([1, 2, 3])\nconst tuple: [number, string] = [1, \"x\"]\n// Immutable: readonly number[]",
            "scala2": "// Common patterns\nval v = Vector(1, 2, 3)\nval m = Map(\"a\" -> 1)\nval s = Set(3, 1, 2)\nval l = List(1, 2, 3)\nval q = scala.collection.immutable.Queue(1, 2, 3)",
            "scala3": "// Common patterns\nval v = Vector(1, 2, 3)\nval m = Map(\"a\" -> 1)\nval s = Set(3, 1, 2)\nval l = List(1, 2, 3)"
        }
    },
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def run_generators():
    """Run each per-language generator once (deduplicated by folder)."""
    seen_folders = set()
    for _lang_id, _label, html_rel in LANGS:
        folder = html_rel.split("/")[0]
        if folder in seen_folders:
            continue
        seen_folders.add(folder)

        script = os.path.join(SHEET_GENERATORS_DIR, folder, f"generate_{folder}_cheat_sheet.py")
        if not os.path.exists(script):
            print(f"  [skip] no generator found: {script}")
            continue

        print(f"  [gen] {folder} ...")
        try:
            subprocess.run(
                [sys.executable, script],
                cwd=os.path.dirname(script),
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            print(f"  [warn] generator exited with code {exc.returncode}")
        except Exception as exc:
            print(f"  [warn] {exc}")


def ensure_offline_assets():
    """Ensure local highlight.js fallback files exist under output/assets/hljs."""
    os.makedirs(OFFLINE_ASSETS_DIR, exist_ok=True)

    downloaded = 0
    skipped = 0
    failed = 0

    for rel_path, url in HLJS_ASSET_URLS.items():
        dst = os.path.join(OFFLINE_ASSETS_DIR, *rel_path.split("/"))
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
        except Exception as exc:
            failed += 1
            print(f"  [warn] could not fetch fallback asset: {url} ({exc})")

    print(
        "  [assets] offline hljs fallback -> "
        f"downloaded={downloaded}, existing={skipped}, failed={failed}"
    )



# ---------------------------------------------------------------------------
# Main builder
# ---------------------------------------------------------------------------

def build():
    skip_gen = "--skip-gen" in sys.argv

    if not skip_gen:
        print("Running language generators ...")
        run_generators()
    else:
        print("Skipping language generators (--skip-gen).")

    ensure_offline_assets()

    shared_css = ""
    for _lang_id, _label, html_rel in LANGS:
        path = os.path.join(SHEET_GENERATORS_DIR, html_rel)
        if os.path.exists(path):
            shared_css = extract_between(read_file(path), "style")
            break

    if not shared_css:
        print("  [warn] Could not find shared CSS; falling back to empty styles.")

    sheets = {}
    lang_labels = {}
    for lang_id, label, html_rel in LANGS:
        lang_labels[lang_id] = label

        path = os.path.join(SHEET_GENERATORS_DIR, html_rel)
        if os.path.exists(path):
            body = normalize_sheet_body(extract_between(read_file(path), "body"))
        else:
            print(f"  [warn] missing sheet: {path}")
            body = (
                '<p class="empty-note">Sheet not found: '
                + html_lib.escape(label)
                + "<br>Run the generator first.</p>"
            )

        sheets[lang_id] = {
            "label": label,
            "body": body,
        }

    problems = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "problems"))
    interview = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "interview"))
    basics = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "language_basics"))
    design_patterns = load_examples_from_dir(os.path.join(CODE_EXAMPLES_DIR, "design_patterns"))
    for pattern_key, notes in MODERN_APPROACH_NOTES.items():
        if pattern_key in design_patterns:
            design_patterns[pattern_key]['modernNotes'] = notes
    for problem_key, insight_data in ADAPTER_INSIGHTS.items():
        if problem_key in problems:
            problems[problem_key]['adapterInsight'] = insight_data['insight']
            if insight_data.get('compareEntries'):
                problems[problem_key]['compareEntries'] = insight_data['compareEntries']
    for basic_key, enhancement in BASICS_ENHANCEMENTS.items():
        if basic_key in basics:
            basics[basic_key].update(enhancement)
        else:
            basics[basic_key] = enhancement
    principles = PRINCIPLES

    if not problems:
        print("  [warn] no problem examples found.")
    if not interview:
        print("  [warn] no interview examples found.")
    if not basics:
        print("  [warn] no language basics examples found.")
    if not design_patterns:
        print("  [warn] no design pattern examples found.")
    if not principles:
        print("  [warn] no principles configured.")

    if os.path.exists(MAIN_PAGE_DOC_PATH):
        home_html = markdown_to_html(read_file(MAIN_PAGE_DOC_PATH))
    else:
        print(f"  [warn] missing main page doc: {MAIN_PAGE_DOC_PATH}")
        home_html = "<h1>Polyglot Dev Atlas</h1><p>Main page doc not found.</p>"

    ui_styles = read_file(os.path.join(BASE_DIR, "templates", "ui_styles.css"))
    app_template = read_file(os.path.join(BASE_DIR, "templates", "app.js"))

    app_js = (
        app_template.replace("__SHEETS_JSON__", safe_json(sheets))
        .replace("__HOME_HTML_JSON__", safe_json(home_html))
        .replace("__PROBLEMS_JSON__", safe_json(problems))
        .replace("__INTERVIEW_JSON__", safe_json(interview))
        .replace("__BASICS_JSON__", safe_json(basics))
        .replace("__DESIGN_PATTERNS_JSON__", safe_json(design_patterns))
        .replace("__PRINCIPLES_JSON__", safe_json(principles))
        .replace("__COURSE_STEPS_JSON__", safe_json(COURSE_STEPS))
        .replace("__ADAPTATION_COURSE_JSON__", safe_json(ADAPTATION_COURSE))
        .replace("__WORKFLOW_JSON__", safe_json(WORKFLOW))
        .replace("__INTERVIEW_GROUPS_JSON__", safe_json(INTERVIEW_GROUPS))
        .replace("__BASICS_GROUPS_JSON__", safe_json(BASICS_GROUPS))
        .replace("__DESIGN_PATTERNS_GROUPS_JSON__", safe_json(DESIGN_PATTERNS_GROUPS))
        .replace("__PRINCIPLES_GROUPS_JSON__", safe_json(PRINCIPLES_GROUPS))
        .replace("__COURSE_STEPS_GROUPS_JSON__", safe_json(COURSE_STEPS_GROUPS))
        .replace("__WORKFLOW_GROUPS_JSON__", safe_json(WORKFLOW_GROUPS))
        .replace("__LANG_LABELS_JSON__", safe_json(lang_labels))
    )

    html_parts = [
        "<!doctype html>\n",
        '<html lang="en">\n',
        "<head>\n",
        '  <meta charset="utf-8">\n',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n',
        "  <title>Polyglot Dev Atlas</title>\n",
        '  <link id="hljsDarkTheme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/atom-one-dark.min.css" data-fallback="assets/hljs/atom-one-dark.min.css" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.href=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}">\n',
        '  <link id="hljsLightTheme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/styles/github.min.css" data-fallback="assets/hljs/github.min.css" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.href=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}" disabled>\n',
        "  <style>\n",
        shared_css,
        "\n",
        ui_styles,
        "\n  </style>\n",
        "</head>\n",
        '<body class="theme-dark palette-brand">\n',
        '  <div class="top-stack" id="topStack">\n',
        '    <div class="top-row">\n',
        '      <span class="row-title">Languages</span>\n',
        '      <nav class="chip-row" id="langNav" aria-label="Languages"></nav>\n',
        "    </div>\n",
        '    <div class="top-row" id="viewsRow">\n',
            '      <div class="course-hide-views" id="viewsSelection">\n',
            '        <span class="row-title">Views</span>\n',
            '        <nav class="chip-row" id="viewNav" aria-label="Views"></nav>\n',
            '        <span class="spacer"></span>\n',
            '      </div>\n',
        '      <div class="chip-row compare-row">\n',
        '        <span class="row-title">Style</span>\n',
        '        <div class="palette-previews" id="palettePreviews" aria-label="Palette previews">\n',
        '          <button type="button" class="palette-preview-btn" data-palette="brand" aria-pressed="false" title="Brand Accent">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        '          </button>\n',
        '          <button type="button" class="palette-preview-btn" data-palette="technical" aria-pressed="false" title="Technical">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        '          </button>\n',
        '          <button type="button" class="palette-preview-btn" data-palette="soft" aria-pressed="false" title="Soft Minimal">\n',
        '            <span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span><span class="palette-swatch" aria-hidden="true"></span>\n',
        '          </button>\n',
        '        </div>\n',
        '        <button type="button" class="chip-btn subtle-btn theme-btn" id="themeToggle" aria-label="Switch to light theme" title="Switch to light theme">&#9728;</button>\n',
        '        <button type="button" class="chip-btn" id="compareToggle" aria-pressed="false">Compare</button>\n',
        '        <button type="button" class="chip-btn subtle-btn" id="swapBtn" title="Swap selected languages">Swap</button>\n',
        '        <button type="button" class="chip-btn" id="courseBtn" title="Start 7-level pro adaptation course">📚 Course</button>\n',
        "      </div>\n",
        "    </div>\n",
        "  </div>\n",
        '\n  <main class="main-content">\n',
        '    <section id="runtimeWarning" class="runtime-warning hidden" role="alert"></section>\n',
        '    <div class="catalog-layout" id="catalogLayout">\n',
        '      <aside class="catalog-sidebar hidden" id="catalogSidebar">\n',
        '        <div class="course-level-panel hidden" id="courseLevelPanel">\n',
        '          <div class="sidebar-header course-level-header">\n',
        '            <span class="sidebar-title" id="courseLevelTitle">Course Level</span>\n',
        '            <button type="button" class="sidebar-toggle-btn" id="courseLevelToggleBtn" title="Collapse course levels" aria-label="Collapse course levels">\u00AB</button>\n',
        '          </div>\n',
        '          <div class="course-level-list" id="courseLevelList"></div>\n',
        '        </div>\n',
        '        <div class="sidebar-header" id="topicSidebarHeader">\n',
        '          <span class="sidebar-title" id="sidebarTitle">Items</span>\n',
        '          <button type="button" class="sidebar-toggle-btn" id="sidebarToggleBtn" title="Collapse sidebar" aria-label="Collapse sidebar">\u00AB</button>\n',
        '        </div>\n',
        '        <div class="sidebar-list" id="sidebarList"></div>\n',
        '      </aside>\n',
        '      <button type="button" class="sidebar-expand-btn hidden" id="sidebarExpandBtn" title="Expand sidebar" aria-label="Expand sidebar">\u00BB</button>\n',
        '      <div class="catalog-main">\n',
        '        <section id="courseNavHeader" class="course-nav-header hidden">\n',
        '          <div class="course-nav-bar">\n',
        '            <button type="button" id="coursePrevBtn" class="course-nav-btn">&#8249; Prev</button>\n',
        '            <span id="courseNavTitle" class="course-nav-title"></span>\n',
        '            <button type="button" id="courseNextBtn" class="course-nav-btn">Next &#8250;</button>\n',
        '          </div>\n',
        '          <p id="courseNavDesc" class="course-nav-desc"></p>\n',
        '          <button type="button" id="courseExitBtn" class="course-nav-link">Go to Lang. Basic</button>\n',
        '        </section>\n',
        '        <section id="entryMeta" class="entry-meta hidden">\n',
        '          <h2 id="entryTitle"></h2>\n',
        '          <p id="entryDesc"></p>\n',
        '          <div id="entrySourceLinks"></div>\n',
        '          <div id="entryModernNotes"></div>\n',
        '          <div id="entryAdapterInsight"></div>\n',
        '          <div id="entryCompareLinks"></div>\n',
        '        </section>\n',
        '        <section id="contentHost"></section>\n',
        '      </div>\n',
        '    </div>\n',
        "  </main>\n\n",
        '  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/highlight.min.js" data-fallback="assets/hljs/highlight.min.js" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.src=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}"></script>\n',
        '  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.11.1/languages/scala.min.js" data-fallback="assets/hljs/languages/scala.min.js" onerror="if(!this.dataset.fallbackApplied){this.dataset.fallbackApplied=\'1\';this.src=this.dataset.fallback;}else{window.__hljsMissingFallback=true;}"></script>\n',
        "  <script>\n",
        app_js,
        "\n  </script>\n",
        "</body>\n",
        "</html>\n",
    ]

    output_html = "".join(html_parts)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(output_html)

    size_kb = os.path.getsize(OUTPUT_FILE) // 1024
    print(f"\nDone! Output written to:\n  {OUTPUT_FILE}\n  ({size_kb} KB)")


if __name__ == "__main__":
    build()



