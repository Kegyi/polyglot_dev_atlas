(function () {
    var SHEETS = __SHEETS_JSON__;
    var HOME_HTML = __HOME_HTML_JSON__;
    var PROBLEMS = __PROBLEMS_JSON__;
    var INTERVIEW = __INTERVIEW_JSON__;
    var BASICS = __BASICS_JSON__;
    var DESIGN_PATTERNS = __DESIGN_PATTERNS_JSON__;
    var PRINCIPLES = __PRINCIPLES_JSON__;
    var COURSE_STEPS = __COURSE_STEPS_JSON__;
    var ADAPTATION_COURSE = __ADAPTATION_COURSE_JSON__;
    var WORKFLOW = __WORKFLOW_JSON__;
    var INTERVIEW_GROUPS = __INTERVIEW_GROUPS_JSON__;
    var BASICS_GROUPS = __BASICS_GROUPS_JSON__;
    var DESIGN_PATTERNS_GROUPS = __DESIGN_PATTERNS_GROUPS_JSON__;
    var PRINCIPLES_GROUPS = __PRINCIPLES_GROUPS_JSON__;
    var COURSE_STEPS_GROUPS = __COURSE_STEPS_GROUPS_JSON__;
    var WORKFLOW_GROUPS = __WORKFLOW_GROUPS_JSON__;
    var LANG_LABELS = __LANG_LABELS_JSON__;
    var LANG_ORDER = Object.keys(LANG_LABELS);
    var LANG_TO_HL = {
        cpp: 'cpp',
        python: 'python',
        go: 'go',
        typescript: 'typescript',
        scala2: 'scala',
        scala3: 'scala'
    };
    var THEME_STORAGE_KEY = 'polyglot_dev_atlas_theme';
    var PALETTE_STORAGE_KEY = 'polyglot_dev_atlas_palette';
    var VIEW_CATEGORY_STORAGE_KEY = 'polyglot_dev_atlas_view_category';
    var SIDEBAR_STORAGE_KEY = 'polyglot_dev_atlas_sidebar_collapsed';
    var PALETTE_OPTIONS = {
        brand: true,
        technical: true,
        soft: true
    };
    var LANG_DRAG_THRESHOLD = 24;
    var LANG_DRAG_MAX_SHIFT = 12;
    var langDragState = null;
    var suppressedLangClick = null;
    var VIEW_CATEGORIES = {
        atlas: {
            label: 'Atlas Views',
            views: ['sheets', 'patterns', 'principles', 'workflow']
        },
        learning: {
            label: 'Learning Views',
            views: ['exercises', 'course', 'basics', 'interview', 'problems']
        }
    };
    var LANGUAGE_SPECIFIC_FEATURES = {
        cpp: [
            'Access control nuances (`protected`, friend declarations, inheritance visibility)',
            'RAII and deterministic destruction for resource safety',
            'Move semantics (`T&&`, move constructors, perfect forwarding)',
            'Allocator-aware containers and custom memory ownership models',
            'Template metaprogramming and compile-time constraints'
        ],
        python: [
            'Decorators for wrapping and registering behavior',
            'Descriptors (`__get__`, `__set__`, `__set_name__`) for attribute protocol hooks',
            'Metaclasses for class creation customization',
            'Data model dunder methods (`__iter__`, `__enter__`, `__call__`, etc.)',
            'Runtime introspection and monkey patching patterns'
        ],
        go: [
            'Goroutines and scheduler-driven concurrency model',
            'Channels with select-based coordination and cancellation',
            '`defer` for scoped cleanup and post-return hooks',
            'Implicit interface satisfaction and composition-first APIs',
            'Error wrapping (`%w`) and idiomatic sentinel handling'
        ],
        typescript: [
            'Conditional and distributive types for type-level branching',
            'Mapped types and key remapping over object structures',
            'Template literal types for string-shape constraints',
            'Declaration merging and module augmentation',
            'Control-flow narrowing with custom type guards'
        ],
        scala: [
            'Implicits / givens and context parameters',
            'Type classes for ad-hoc polymorphism',
            'Higher-kinded types and variance design',
            'Exhaustive pattern matching and extractors',
            'Effect-style composition with monads and for-comprehensions'
        ]
    };

    var LANGUAGE_SPECIFIC_BEGINNER_GUIDE = {
        cpp: {
            intro: 'C++ gives you direct control over memory and object lifetime. That makes performance strong, but it also means ownership rules matter from day one.',
            mindsets: [
                'Think in terms of object lifetime: stack, heap, and who owns cleanup.',
                'Prefer value semantics first, then add pointers when sharing or polymorphism is needed.',
                'Use RAII wrappers so cleanup happens automatically.'
            ],
            snippets: [
                {
                    title: 'RAII cleanup (automatic)',
                    note: 'When scope ends, destructors run. No manual close call needed.',
                    code: 'struct FileGuard {\n  ~FileGuard() { /* close file */ }\n};\n\nvoid readConfig() {\n  FileGuard guard;\n  // use file\n} // guard cleanup happens here'
                },
                {
                    title: 'Move semantics (transfer ownership)',
                    note: 'Use std::move to transfer expensive resources instead of copying.',
                    code: 'std::vector<int> build() {\n  std::vector<int> data{1,2,3};\n  return data; // moved (or elided)\n}\n\nstd::vector<int> numbers = build();'
                }
            ]
        },
        python: {
            intro: 'Python is optimized for readability and quick iteration. Many advanced patterns are runtime-based, so you can build power incrementally.',
            mindsets: [
                'Start with clear functions and classes before advanced magic methods.',
                'Use decorators for cross-cutting behavior like logging or timing.',
                'Think in protocols: if it behaves like the needed interface, it usually works.'
            ],
            snippets: [
                {
                    title: 'Decorator for reusable behavior',
                    note: 'Wrap a function once, then reuse that behavior everywhere.',
                    code: 'def logged(fn):\n    def wrapper(*args, **kwargs):\n        print("calling", fn.__name__)\n        return fn(*args, **kwargs)\n    return wrapper\n\n@logged\ndef add(a, b):\n    return a + b'
                },
                {
                    title: 'Context manager style cleanup',
                    note: 'Use with to guarantee cleanup even when errors happen.',
                    code: 'with open("notes.txt", "r", encoding="utf-8") as f:\n    text = f.read()\n# file is closed automatically'
                }
            ]
        },
        go: {
            intro: 'Go keeps the language small and predictable. Concurrency and explicit error handling are core habits, not optional extras.',
            mindsets: [
                'Return errors as values and handle them immediately.',
                'Use goroutines for concurrent work and channels for coordination.',
                'Use defer right after acquiring a resource.'
            ],
            snippets: [
                {
                    title: 'Error-first flow',
                    note: 'Go favors explicit branches over exceptions.',
                    code: 'n, err := strconv.Atoi(input)\nif err != nil {\n    return fmt.Errorf("invalid number: %w", err)\n}\nfmt.Println("parsed", n)'
                },
                {
                    title: 'Goroutine + channel',
                    note: 'Start work concurrently and receive the result through a channel.',
                    code: 'ch := make(chan string)\ngo func() {\n    ch <- "done"\n}()\nmsg := <-ch\nfmt.Println(msg)'
                }
            ]
        },
        typescript: {
            intro: 'TypeScript adds a strong static type layer on top of JavaScript. It is excellent for making APIs self-documenting and safer to refactor.',
            mindsets: [
                'Use union types to model possible states clearly.',
                'Narrow types with guards before using specific fields.',
                'Let interfaces describe behavior, then implement with any matching shape.'
            ],
            snippets: [
                {
                    title: 'Discriminated union',
                    note: 'Model variants and handle each one safely in switch.',
                    code: 'type Result =\n  | { ok: true; value: number }\n  | { ok: false; error: string }\n\nfunction show(r: Result) {\n  return r.ok ? `value=${r.value}` : `error=${r.error}`\n}'
                },
                {
                    title: 'Type guard narrowing',
                    note: 'A guard helps TypeScript infer the precise type.',
                    code: 'function isText(v: unknown): v is string {\n  return typeof v === "string"\n}\n\nconst value: unknown = "hello"\nif (isText(value)) console.log(value.toUpperCase())'
                }
            ]
        },
        scala: {
            intro: 'Scala blends object-oriented and functional styles. You can start simple, then gradually adopt stronger abstractions like Options, Eithers, and type classes.',
            mindsets: [
                'Prefer immutable collections and expression-style code.',
                'Use Option instead of null for absent values.',
                'Treat pattern matching as a primary control-flow tool.'
            ],
            snippets: [
                {
                    title: 'Option instead of null',
                    note: 'Represent missing values explicitly and handle both cases.',
                    code: 'val maybeAge: Option[Int] = Some(20)\nval label = maybeAge match\n  case Some(age) => s"age=$age"\n  case None => "age=unknown"'
                },
                {
                    title: 'Collection pipeline',
                    note: 'Transform data with small composable steps.',
                    code: 'val nums = List(1, 2, 3, 4, 5)\nval result = nums\n  .filter(_ % 2 == 1)\n  .map(_ * 10)\n  .sum'
                }
            ]
        }
    };

    var EXERCISE_GROUPS = [
        {
            label: 'Beginner',
            keys: ['exercise_hello_world', 'exercise_fizzbuzz', 'exercise_even_odd']
        },
        {
            label: 'Intermediate',
            keys: ['exercise_word_frequency', 'exercise_fibonacci', 'exercise_palindrome', 'exercise_array_reverse', 'exercise_temperature_converter']
        },
        {
            label: 'Advanced',
            keys: ['exercise_parallel_aggregator', 'exercise_tree_traversal', 'exercise_stream_processor']
        }
    ];

    var EXERCISES = {
        exercise_hello_world: {
            label: 'Beginner: Print out Hello World!',
            description: 'Write a program that prints "Hello, World!" to standard output. Keep it minimal and runnable from the command line.',
            codes: {
                cpp: '#include <iostream>\n\nint main() {\n    std::cout << "Hello, World!\\n";\n    return 0;\n}',
                python: 'print("Hello, World!")',
                go: 'package main\n\nimport "fmt"\n\nfunc main() {\n    fmt.Println("Hello, World!")\n}',
                typescript: 'console.log("Hello, World!");',
                scala2: 'object Main extends App {\n  println("Hello, World!")\n}',
                scala3: '@main def hello(): Unit =\n  println("Hello, World!")'
            }
        },
        exercise_fizzbuzz: {
            label: 'Beginner: FizzBuzz',
            description: 'Print numbers 1 to 100. For multiples of 3 print "Fizz", for 5 print "Buzz", for both print "FizzBuzz".',
            codes: {
                cpp: '#include <iostream>\n\nint main() {\n    for (int i = 1; i <= 100; ++i) {\n        if (i % 15 == 0) std::cout << "FizzBuzz\\n";\n        else if (i % 3 == 0) std::cout << "Fizz\\n";\n        else if (i % 5 == 0) std::cout << "Buzz\\n";\n        else std::cout << i << "\\n";\n    }\n    return 0;\n}',
                python: 'for i in range(1, 101):\n    if i % 15 == 0: print("FizzBuzz")\n    elif i % 3 == 0: print("Fizz")\n    elif i % 5 == 0: print("Buzz")\n    else: print(i)',
                go: 'package main\n\nimport "fmt"\n\nfunc main() {\n    for i := 1; i <= 100; i++ {\n        switch {\n        case i%15 == 0:\n            fmt.Println("FizzBuzz")\n        case i%3 == 0:\n            fmt.Println("Fizz")\n        case i%5 == 0:\n            fmt.Println("Buzz")\n        default:\n            fmt.Println(i)\n        }\n    }\n}',
                typescript: 'for (let i = 1; i <= 100; i++) {\n  if (i % 15 === 0) console.log("FizzBuzz");\n  else if (i % 3 === 0) console.log("Fizz");\n  else if (i % 5 === 0) console.log("Buzz");\n  else console.log(i);\n}',
                scala2: '(1 to 100).foreach { i =>\n  if (i % 15 == 0) println("FizzBuzz")\n  else if (i % 3 == 0) println("Fizz")\n  else if (i % 5 == 0) println("Buzz")\n  else println(i)\n}',
                scala3: '(1 to 100).foreach { i =>\n  if i % 15 == 0 then println("FizzBuzz")\n  else if i % 3 == 0 then println("Fizz")\n  else if i % 5 == 0 then println("Buzz")\n  else println(i)\n}'
            }
        },
        exercise_even_odd: {
            label: 'Beginner: Check Even or Odd',
            description: 'Read a number and determine if it is even or odd. Print the result.',
            codes: {
                cpp: '#include <iostream>\n\nint main() {\n    int n;\n    std::cout << "Enter a number: ";\n    std::cin >> n;\n    \n    if (n % 2 == 0)\n        std::cout << n << " is even\\n";\n    else\n        std::cout << n << " is odd\\n";\n    return 0;\n}',
                python: 'n = int(input("Enter a number: "))\nif n % 2 == 0:\n    print(f"{n} is even")\nelse:\n    print(f"{n} is odd")',
                go: 'package main\n\nimport (\n    "fmt"\n)\n\nfunc main() {\n    var n int\n    fmt.Print("Enter a number: ")\n    fmt.Scan(&n)\n    \n    if n%2 == 0 {\n        fmt.Printf("%d is even\\n", n)\n    } else {\n        fmt.Printf("%d is odd\\n", n)\n    }\n}',
                typescript: 'import * as readline from "readline";\nconst rl = readline.createInterface({ input: process.stdin, output: process.stdout });\nrl.question("Enter a number: ", (input) => {\n  const n = parseInt(input);\n  console.log(n % 2 === 0 ? `${n} is even` : `${n} is odd`);\n  rl.close();\n});',
                scala2: 'val n = scala.io.StdIn.readInt()\nif (n % 2 == 0) println(s"$n is even")\nelse println(s"$n is odd")',
                scala3: 'val n = scala.io.StdIn.readInt()\nif n % 2 == 0 then println(s"$n is even")\nelse println(s"$n is odd")'
            }
        },
        exercise_word_frequency: {
            label: 'Intermediate: Word Frequency Counter',
            description: 'Given a sentence, count how many times each word appears (case-insensitive), then print the counts sorted by highest frequency.',
            codes: {
                cpp: '#include <algorithm>\n#include <cctype>\n#include <iostream>\n#include <sstream>\n#include <string>\n#include <unordered_map>\n#include <vector>\n\nint main() {\n    std::string line = "This is a test. This test is simple.";\n    for (char& c : line) {\n        if (std::ispunct(static_cast<unsigned char>(c))) c = \' \';\n        else c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));\n    }\n\n    std::unordered_map<std::string, int> freq;\n    std::istringstream in(line);\n    std::string word;\n    while (in >> word) freq[word]++;\n\n    std::vector<std::pair<std::string, int>> items(freq.begin(), freq.end());\n    std::sort(items.begin(), items.end(), [](auto& a, auto& b) {\n        return a.second == b.second ? a.first < b.first : a.second > b.second;\n    });\n\n    for (const auto& [w, n] : items) {\n        std::cout << w << ": " << n << "\\n";\n    }\n}',
                python: 'from collections import Counter\nimport re\n\ntext = "This is a test. This test is simple."\nwords = re.findall(r"[a-zA-Z]+", text.lower())\ncounts = Counter(words)\n\nfor word, count in sorted(counts.items(), key=lambda p: (-p[1], p[0])):\n    print(f"{word}: {count}")',
                go: 'package main\n\nimport (\n    "fmt"\n    "regexp"\n    "sort"\n    "strings"\n)\n\nfunc main() {\n    text := "This is a test. This test is simple."\n    re := regexp.MustCompile(`[A-Za-z]+`)\n    words := re.FindAllString(strings.ToLower(text), -1)\n\n    freq := map[string]int{}\n    for _, w := range words {\n        freq[w]++\n    }\n\n    type pair struct {\n        word  string\n        count int\n    }\n\n    items := make([]pair, 0, len(freq))\n    for w, c := range freq {\n        items = append(items, pair{w, c})\n    }\n\n    sort.Slice(items, func(i, j int) bool {\n        if items[i].count == items[j].count {\n            return items[i].word < items[j].word\n        }\n        return items[i].count > items[j].count\n    })\n\n    for _, it := range items {\n        fmt.Printf("%s: %d\\n", it.word, it.count)\n    }\n}',
                typescript: 'const text = "This is a test. This test is simple.";\nconst words = (text.toLowerCase().match(/[a-z]+/g) ?? []);\n\nconst freq = new Map<string, number>();\nfor (const w of words) {\n  freq.set(w, (freq.get(w) ?? 0) + 1);\n}\n\nconst items = [...freq.entries()]\n  .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));\n\nfor (const [word, count] of items) {\n  console.log(`${word}: ${count}`);\n}',
                scala2: 'object Main extends App {\n  val text = "This is a test. This test is simple."\n  val words = "[A-Za-z]+".r.findAllIn(text.toLowerCase).toList\n  val counts = words.groupBy(identity).view.mapValues(_.size).toMap\n\n  counts.toList\n    .sortBy { case (w, c) => (-c, w) }\n    .foreach { case (w, c) => println(s"$w: $c") }\n}',
                scala3: '@main def main(): Unit =\n  val text = "This is a test. This test is simple."\n  val words = "[A-Za-z]+".r.findAllIn(text.toLowerCase).toList\n  val counts = words.groupBy(identity).view.mapValues(_.size).toMap\n\n  counts.toList\n    .sortBy((w, c) => (-c, w))\n    .foreach((w, c) => println(s"$w: $c"))'
            }
        },
        exercise_fibonacci: {
            label: 'Intermediate: Fibonacci Sequence',
            description: 'Generate the first N Fibonacci numbers, where N is given as input. The sequence starts: 0, 1, 1, 2, 3, 5, 8, ...',
            codes: {
                cpp: '#include <iostream>\n\nint main() {\n    int n;\n    std::cout << "Enter number of terms: ";\n    std::cin >> n;\n    \n    long long a = 0, b = 1;\n    for (int i = 0; i < n; ++i) {\n        std::cout << a << " ";\n        long long temp = a + b;\n        a = b;\n        b = temp;\n    }\n    std::cout << "\\n";\n    return 0;\n}',
                python: 'n = int(input("Enter number of terms: "))\na, b = 0, 1\nfor _ in range(n):\n    print(a, end=" ")\n    a, b = b, a + b\nprint()',
                go: 'package main\nimport ("fmt")\nfunc main() {\n    var n int\n    fmt.Print("Enter number of terms: ")\n    fmt.Scan(&n)\n    a, b := 0, 1\n    for i := 0; i < n; i++ {\n        fmt.Print(a, " ")\n        a, b = b, a+b\n    }\n    fmt.Println()\n}',
                typescript: 'const n = parseInt(process.argv[2] || "10");\nlet a = 0, b = 1;\nfor (let i = 0; i < n; i++) {\n  process.stdout.write(a + " ");\n  [a, b] = [b, a + b];\n}\nconsole.log();',
                scala2: 'val n = scala.io.StdIn.readInt()\nvar a = 0L\nvar b = 1L\nfor (_ <- 0 until n) {\n  print(a + " ")\n  val temp = a + b\n  a = b\n  b = temp\n}\nprintln()',
                scala3: 'val n = scala.io.StdIn.readInt()\nvar a = 0L\nvar b = 1L\nfor _ <- 0 until n do\n  print(a + " ")\n  val temp = a + b\n  a = b\n  b = temp\nprintln()'
            }
        },
        exercise_palindrome: {
            label: 'Intermediate: Palindrome Checker',
            description: 'Check if a given string is a palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.',
            codes: {
                cpp: '#include <algorithm>\n#include <cctype>\n#include <iostream>\n#include <string>\n\nint main() {\n    std::string s = "A man, a plan, a canal: Panama";\n    std::string cleaned;\n    for (char c : s) {\n        if (std::isalnum(c)) {\n            cleaned += std::tolower(c);\n        }\n    }\n    \n    bool isPalin = std::string(cleaned.rbegin(), cleaned.rend()) == cleaned;\n    std::cout << (isPalin ? "Palindrome" : "Not a palindrome") << "\\n";\n    return 0;\n}',
                python: 's = "A man, a plan, a canal: Panama"\ncleaned = "".join(c.lower() for c in s if c.isalnum())\nis_palin = cleaned == cleaned[::-1]\nprint("Palindrome" if is_palin else "Not a palindrome")',
                go: 'package main\n\nimport (\n    "fmt"\n    "regexp"\n    "strings"\n)\n\nfunc main() {\n    s := "A man, a plan, a canal: Panama"\n    re := regexp.MustCompile(`[^a-zA-Z0-9]`)\n    cleaned := strings.ToLower(re.ReplaceAllString(s, ""))\n    \n    rev := ""\n    for _, c := range cleaned {\n        rev = string(c) + rev\n    }\n    \n    if cleaned == rev {\n        fmt.Println("Palindrome")\n    } else {\n        fmt.Println("Not a palindrome")\n    }\n}',
                typescript: 'const s = "A man, a plan, a canal: Panama";\nconst cleaned = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();\nconst isPalin = cleaned === cleaned.split("").reverse().join("");\nconsole.log(isPalin ? "Palindrome" : "Not a palindrome");',
                scala2: 'val s = "A man, a plan, a canal: Panama"\nval cleaned = s.filter(_.isLetterOrDigit).toLowerCase\nval isPalin = cleaned == cleaned.reverse\nprintln(if (isPalin) "Palindrome" else "Not a palindrome")',
                scala3: 'val s = "A man, a plan, a canal: Panama"\nval cleaned = s.filter(_.isLetterOrDigit).toLowerCase\nval isPalin = cleaned == cleaned.reverse\nprintln(if isPalin then "Palindrome" else "Not a palindrome")'
            }
        },
        exercise_array_reverse: {
            label: 'Intermediate: Reverse an Array',
            description: 'Reverse the elements of an array or list in-place (or return a new reversed collection).',
            codes: {
                cpp: '#include <iostream>\n#include <vector>\n\nint main() {\n    std::vector<int> arr = {1, 2, 3, 4, 5};\n    std::reverse(arr.begin(), arr.end());\n    \n    for (int x : arr) {\n        std::cout << x << " ";\n    }\n    std::cout << "\\n";\n    return 0;\n}',
                python: 'arr = [1, 2, 3, 4, 5]\narr.reverse()  # or arr = arr[::-1]\nprint(arr)',
                go: 'package main\n\nimport "fmt"\n\nfunc main() {\n    arr := []int{1, 2, 3, 4, 5}\n    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {\n        arr[i], arr[j] = arr[j], arr[i]\n    }\n    fmt.Println(arr)\n}',
                typescript: 'const arr = [1, 2, 3, 4, 5];\narr.reverse();\nconsole.log(arr);',
                scala2: 'val arr = List(1, 2, 3, 4, 5)\nval reversed = arr.reverse\nprintln(reversed)',
                scala3: 'val arr = List(1, 2, 3, 4, 5)\nval reversed = arr.reverse\nprintln(reversed)'
            }
        },
        exercise_temperature_converter: {
            label: 'Intermediate: Temperature Unit Converter',
            description: 'Convert between Celsius, Fahrenheit, and Kelvin. Accept a temperature and unit, output conversions to the other two.',
            codes: {
                cpp: '#include <iostream>\n#include <iomanip>\n\nint main() {\n    double celsius = 25.0;\n    double fahrenheit = (celsius * 9/5) + 32;\n    double kelvin = celsius + 273.15;\n    \n    std::cout << std::fixed << std::setprecision(2);\n    std::cout << celsius << " deg C = " << fahrenheit << " deg F = " << kelvin << "K\\n";\n    return 0;\n}',
                python: 'celsius = 25.0\nfahrenheit = (celsius * 9/5) + 32\nkelvin = celsius + 273.15\n\nprint(f"{celsius} deg C = {fahrenheit:.2f} deg F = {kelvin:.2f}K")',
                go: 'package main\n\nimport "fmt"\n\nfunc main() {\n    celsius := 25.0\n    fahrenheit := (celsius * 9 / 5) + 32\n    kelvin := celsius + 273.15\n    \n    fmt.Printf("%.2f deg C = %.2f deg F = %.2f K\\n", celsius, fahrenheit, kelvin)\n}',
                typescript: 'const celsius = 25.0;\nconst fahrenheit = (celsius * 9/5) + 32;\nconst kelvin = celsius + 273.15;\n\nconsole.log(`${celsius} deg C = ${fahrenheit.toFixed(2)} deg F = ${kelvin.toFixed(2)}K`);',
                scala2: 'val celsius = 25.0\nval fahrenheit = (celsius * 9/5) + 32\nval kelvin = celsius + 273.15\n\nprintln(f"$celsius deg C = $fahrenheit%.2f deg F = $kelvin%.2f K")',
                scala3: 'val celsius = 25.0\nval fahrenheit = (celsius * 9/5) + 32\nval kelvin = celsius + 273.15\n\nprintln(f"$celsius deg C = $fahrenheit%.2f deg F = $kelvin%.2f K")'
            }
        },
        exercise_parallel_aggregator: {
            label: 'Advanced: Parallel API Result Aggregator',
            description: 'Fetch data from multiple endpoints concurrently, merge successful responses, and continue even if one request fails. Return both data and per-endpoint error summary.',
            codes: {
                cpp: '#include <future>\n#include <iostream>\n#include <string>\n#include <vector>\n\nstruct Result {\n    std::string endpoint;\n    bool ok;\n    std::string payloadOrError;\n};\n\nResult fetch(const std::string& endpoint) {\n    if (endpoint.find("fail") != std::string::npos) {\n        return {endpoint, false, "timeout"};\n    }\n    return {endpoint, true, "{\\"endpoint\\":\\"" + endpoint + "\\"}"};\n}\n\nint main() {\n    std::vector<std::string> endpoints{ "users", "orders", "fail-metrics" };\n    std::vector<std::future<Result>> jobs;\n\n    for (const auto& ep : endpoints) {\n        jobs.push_back(std::async(std::launch::async, fetch, ep));\n    }\n\n    std::vector<std::string> data;\n    std::vector<std::string> errors;\n\n    for (auto& j : jobs) {\n        Result r = j.get();\n        if (r.ok) data.push_back(r.payloadOrError);\n        else errors.push_back(r.endpoint + ": " + r.payloadOrError);\n    }\n\n    std::cout << "data=" << data.size() << ", errors=" << errors.size() << "\\n";\n}',
                python: 'import asyncio\n\nasync def fetch(endpoint: str) -> tuple[str, bool, str]:\n    await asyncio.sleep(0.05)\n    if "fail" in endpoint:\n        return endpoint, False, "timeout"\n    return endpoint, True, f"{{\\"endpoint\\": \\"{endpoint}\\"}}"\n\nasync def main() -> None:\n    endpoints = ["users", "orders", "fail-metrics"]\n    results = await asyncio.gather(*(fetch(ep) for ep in endpoints), return_exceptions=False)\n\n    data = [payload for _, ok, payload in results if ok]\n    errors = [f"{ep}: {payload}" for ep, ok, payload in results if not ok]\n\n    print({"data": data, "errors": errors})\n\nasyncio.run(main())',
                go: 'package main\n\nimport (\n    "fmt"\n    "strings"\n    "sync"\n)\n\ntype result struct {\n    endpoint string\n    ok       bool\n    payload  string\n}\n\nfunc fetch(ep string) result {\n    if strings.Contains(ep, "fail") {\n        return result{ep, false, "timeout"}\n    }\n    return result{ep, true, fmt.Sprintf("{\\"endpoint\\":\\"%s\\"}", ep)}\n}\n\nfunc main() {\n    endpoints := []string{"users", "orders", "fail-metrics"}\n    ch := make(chan result, len(endpoints))\n    var wg sync.WaitGroup\n\n    for _, ep := range endpoints {\n        wg.Add(1)\n        go func(e string) {\n            defer wg.Done()\n            ch <- fetch(e)\n        }(ep)\n    }\n\n    wg.Wait()\n    close(ch)\n\n    var data []string\n    var errors []string\n    for r := range ch {\n        if r.ok {\n            data = append(data, r.payload)\n        } else {\n            errors = append(errors, r.endpoint+": "+r.payload)\n        }\n    }\n\n    fmt.Printf("data=%d errors=%d\\n", len(data), len(errors))\n}',
                typescript: 'type Result = { endpoint: string; ok: boolean; payload: string };\n\nasync function fetchEndpoint(endpoint: string): Promise<Result> {\n  await new Promise((r) => setTimeout(r, 50));\n  if (endpoint.includes("fail")) return { endpoint, ok: false, payload: "timeout" };\n  return { endpoint, ok: true, payload: JSON.stringify({ endpoint }) };\n}\n\nasync function main() {\n  const endpoints = ["users", "orders", "fail-metrics"];\n  const results = await Promise.all(endpoints.map(fetchEndpoint));\n\n  const data = results.filter(r => r.ok).map(r => r.payload);\n  const errors = results.filter(r => !r.ok).map(r => `${r.endpoint}: ${r.payload}`);\n\n  console.log({ data, errors });\n}\n\nvoid main();',
                scala2: 'import scala.concurrent._\nimport scala.concurrent.duration._\nimport ExecutionContext.Implicits.global\n\ncase class Result(endpoint: String, ok: Boolean, payload: String)\n\ndef fetch(endpoint: String): Future[Result] = Future {\n  if (endpoint.contains("fail")) Result(endpoint, ok = false, "timeout")\n  else Result(endpoint, ok = true, s"{\\"endpoint\\":\\"$endpoint\\"}")\n}\n\nobject Main extends App {\n  val endpoints = List("users", "orders", "fail-metrics")\n  val results = Await.result(Future.sequence(endpoints.map(fetch)), 3.seconds)\n\n  val data = results.collect { case Result(_, true, payload) => payload }\n  val errors = results.collect { case Result(ep, false, payload) => s"$ep: $payload" }\n\n  println(s"data=${data.size}, errors=${errors.size}")\n}',
                scala3: 'import scala.concurrent.*\nimport scala.concurrent.duration.*\nimport scala.concurrent.ExecutionContext.Implicits.global\n\ncase class Result(endpoint: String, ok: Boolean, payload: String)\n\ndef fetch(endpoint: String): Future[Result] = Future {\n  if endpoint.contains("fail") then Result(endpoint, ok = false, "timeout")\n  else Result(endpoint, ok = true, s"{\\"endpoint\\":\\"$endpoint\\"}")\n}\n\n@main def main(): Unit =\n  val endpoints = List("users", "orders", "fail-metrics")\n  val results = Await.result(Future.sequence(endpoints.map(fetch)), 3.seconds)\n\n  val data = results.collect { case Result(_, true, payload) => payload }\n  val errors = results.collect { case Result(ep, false, payload) => s"$ep: $payload" }\n\n  println(s"data=${data.size}, errors=${errors.size}")'
            }
        },
        exercise_tree_traversal: {
            label: 'Advanced: Binary Tree Traversal',
            description: 'Implement in-order, pre-order, and post-order traversal of a binary tree. Display the traversal results.',
            codes: {
                cpp: '#include <iostream>\n#include <vector>\n\nstruct Node {\n    int val;\n    Node* left;\n    Node* right;\n    Node(int v) : val(v), left(nullptr), right(nullptr) {}\n};\n\nvoid inorder(Node* root, std::vector<int>& res) {\n    if (!root) return;\n    inorder(root->left, res);\n    res.push_back(root->val);\n    inorder(root->right, res);\n}\n\nint main() {\n    Node* root = new Node(1);\n    root->left = new Node(2);\n    root->right = new Node(3);\n    root->left->left = new Node(4);\n    \n    std::vector<int> res;\n    inorder(root, res);\n    \n    for (int x : res) std::cout << x << " ";\n    std::cout << "\\n";\n    return 0;\n}',
                python: 'class Node:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\ndef inorder(root, res):\n    if not root:\n        return\n    inorder(root.left, res)\n    res.append(root.val)\n    inorder(root.right, res)\n\nroot = Node(1)\nroot.left = Node(2)\nroot.right = Node(3)\nroot.left.left = Node(4)\n\nres = []\ninorder(root, res)\nprint(res)',
                go: 'package main\n\nimport "fmt"\n\ntype Node struct {\n    val   int\n    left  *Node\n    right *Node\n}\n\nfunc inorder(root *Node, res *[]int) {\n    if root == nil {\n        return\n    }\n    inorder(root.left, res)\n    *res = append(*res, root.val)\n    inorder(root.right, res)\n}\n\nfunc main() {\n    root := &Node{val: 1}\n    root.left = &Node{val: 2}\n    root.right = &Node{val: 3}\n    root.left.left = &Node{val: 4}\n    \n    var res []int\n    inorder(root, &res)\n    fmt.Println(res)\n}',
                typescript: 'class Node {\n  val: number;\n  left: Node | null;\n  right: Node | null;\n  constructor(val: number) {\n    this.val = val;\n    this.left = null;\n    this.right = null;\n  }\n}\n\nfunction inorder(root: Node | null, res: number[]): void {\n  if (!root) return;\n  inorder(root.left, res);\n  res.push(root.val);\n  inorder(root.right, res);\n}\n\nconst root = new Node(1);\nroot.left = new Node(2);\nroot.right = new Node(3);\nroot.left.left = new Node(4);\n\nconst res: number[] = [];\ninorder(root, res);\nconsole.log(res);',
                scala2: 'case class Node(val: Int, var left: Option[Node] = None, var right: Option[Node] = None)\n\ndef inorder(root: Option[Node], res: scala.collection.mutable.Buffer[Int]): Unit = {\n  root.foreach { node =>\n    inorder(node.left, res)\n    res += node.val\n    inorder(node.right, res)\n  }\n}\n\nval root = Node(1, Some(Node(2, Some(Node(4)))), Some(Node(3)))\nval res = scala.collection.mutable.Buffer[Int]()\ninorder(Some(root), res)\nprintln(res)',
                scala3: 'case class Node(val: Int, var left: Option[Node] = None, var right: Option[Node] = None)\n\ndef inorder(root: Option[Node], res: scala.collection.mutable.Buffer[Int]): Unit =\n  root.foreach { node =>\n    inorder(node.left, res)\n    res += node.val\n    inorder(node.right, res)\n  }\n\nval root = Node(1, Some(Node(2, Some(Node(4)))), Some(Node(3)))\nval res = scala.collection.mutable.Buffer[Int]()\ninorder(Some(root), res)\nprintln(res)'
            }
        },
        exercise_stream_processor: {
            label: 'Advanced: Stream Data Processor',
            description: 'Process a stream of numbers: filter evens, square them, sum the results, and handle empty streams gracefully.',
            codes: {
                cpp: '#include <iostream>\n#include <vector>\n#include <numeric>\n#include <algorithm>\n\nint main() {\n    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8};\n    \n    auto sum = 0;\n    std::for_each(nums.begin(), nums.end(), [&sum](int n) {\n        if (n % 2 == 0) {\n            sum += n * n;\n        }\n    });\n    \n    std::cout << "Sum of squares of even numbers: " << sum << "\\n";\n    return 0;\n}',
                python: 'nums = [1, 2, 3, 4, 5, 6, 7, 8]\nresult = sum(n**2 for n in nums if n % 2 == 0)\nprint(f"Sum of squares of even numbers: {result}")',
                go: 'package main\n\nimport "fmt"\n\nfunc main() {\n    nums := []int{1, 2, 3, 4, 5, 6, 7, 8}\n    \n    sum := 0\n    for _, n := range nums {\n        if n%2 == 0 {\n            sum += n * n\n        }\n    }\n    \n    fmt.Printf("Sum of squares of even numbers: %d\\n", sum)\n}',
                typescript: 'const nums = [1, 2, 3, 4, 5, 6, 7, 8];\nconst result = nums\n  .filter(n => n % 2 === 0)\n  .map(n => n * n)\n  .reduce((a, b) => a + b, 0);\n\nconsole.log(`Sum of squares of even numbers: ${result}`);',
                scala2: 'val nums = List(1, 2, 3, 4, 5, 6, 7, 8)\nval result = nums\n  .filter(_ % 2 == 0)\n  .map(n => n * n)\n  .sum\n\nprintln(s"Sum of squares of even numbers: $result")',
                scala3: 'val nums = List(1, 2, 3, 4, 5, 6, 7, 8)\nval result = nums\n  .filter(_ % 2 == 0)\n  .map(n => n * n)\n  .sum\n\nprintln(s"Sum of squares of even numbers: $result")'
            }
        }
    };

    var VIEW_CONFIG = {
        sheets: {
            label: 'Keywords'
        },
        problems: {
            label: 'Problems',
            itemLabel: 'Problem',
            entries: PROBLEMS,
            groups: null
        },
        interview: {
            label: 'Interview',
            itemLabel: 'Question',
            entries: INTERVIEW,
            groups: INTERVIEW_GROUPS
        },
        patterns: {
            label: 'Design Patterns',
            itemLabel: 'Pattern',
            entries: DESIGN_PATTERNS,
            groups: DESIGN_PATTERNS_GROUPS
        },
        basics: {
            label: 'Lang. Basic',
            itemLabel: 'Topic',
            entries: BASICS,
            groups: BASICS_GROUPS
        },
        course: {
            label: 'Course',
            itemLabel: 'Step',
            entries: COURSE_STEPS,
            groups: COURSE_STEPS_GROUPS
        },
        exercises: {
            label: 'Exercises',
            itemLabel: 'Task',
            entries: EXERCISES,
            groups: EXERCISE_GROUPS
        },
        workflow: {
            label: 'Workflow',
            itemLabel: 'Concept',
            entries: WORKFLOW,
            groups: WORKFLOW_GROUPS
        },
        principles: {
            label: 'Principles',
            itemLabel: 'Principle',
            entries: PRINCIPLES,
            groups: PRINCIPLES_GROUPS
        }
    };

    var state = {
        view: '',
        viewCategory: 'atlas',
        compareCount: 1,
        activeSlot: 0,
        theme: 'dark',
        palette: 'brand',
        selectedLangs: [LANG_ORDER[0] || '', LANG_ORDER[1] || LANG_ORDER[0] || ''],
        selectedProblem: Object.keys(PROBLEMS)[0] || '',
        selectedInterview: Object.keys(INTERVIEW)[0] || '',
        selectedPattern: Object.keys(DESIGN_PATTERNS)[0] || '',
        selectedBasic: Object.keys(BASICS)[0] || '',
        selectedPrinciple: Object.keys(PRINCIPLES)[0] || '',
        selectedCourse: Object.keys(COURSE_STEPS)[0] || '',
        selectedExercise: Object.keys(EXERCISES)[0] || '',
        selectedWorkflow: Object.keys(WORKFLOW)[0] || '',
        sidebarCollapsed: false,
        courseLevelCollapsed: false,
        courseMode: false,
        courseLevel: 0,
        courseReturnState: null,
        courseTopicCollapsed: {}
    };

