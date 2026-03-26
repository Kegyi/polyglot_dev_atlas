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
                cpp: '#include <iostream>\n#include <iomanip>\n\nint main() {\n    double celsius = 25.0;\n    double fahrenheit = (celsius * 9/5) + 32;\n    double kelvin = celsius + 273.15;\n    \n    std::cout << std::fixed << std::setprecision(2);\n    std::cout << celsius << "°C = " << fahrenheit << "°F = " << kelvin << "K\\n";\n    return 0;\n}',
                python: 'celsius = 25.0\nfahrenheit = (celsius * 9/5) + 32\nkelvin = celsius + 273.15\n\nprint(f"{celsius}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")',
                go: 'package main\n\nimport "fmt"\n\nfunc main() {\n    celsius := 25.0\n    fahrenheit := (celsius * 9 / 5) + 32\n    kelvin := celsius + 273.15\n    \n    fmt.Printf("%.2f°C = %.2f°F = %.2f K\\n", celsius, fahrenheit, kelvin)\n}',
                typescript: 'const celsius = 25.0;\nconst fahrenheit = (celsius * 9/5) + 32;\nconst kelvin = celsius + 273.15;\n\nconsole.log(`${celsius}°C = ${fahrenheit.toFixed(2)}°F = ${kelvin.toFixed(2)}K`);',
                scala2: 'val celsius = 25.0\nval fahrenheit = (celsius * 9/5) + 32\nval kelvin = celsius + 273.15\n\nprintln(f"$celsius°C = $fahrenheit%.2f°F = $kelvin%.2f K")',
                scala3: 'val celsius = 25.0\nval fahrenheit = (celsius * 9/5) + 32\nval kelvin = celsius + 273.15\n\nprintln(f"$celsius°C = $fahrenheit%.2f°F = $kelvin%.2f K")'
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

    function normalizePaletteKey(paletteName) {
        if (PALETTE_OPTIONS[paletteName]) {
            return paletteName;
        }
        return 'brand';
    }

    function escapeHtml(text) {
        return String(text || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function renderSourceLinks(sourceLinks) {
        if (!sourceLinks || sourceLinks.length === 0) {
            return '';
        }

        return '<div class="entry-source-links">' + sourceLinks.map(function (link) {
            if (!link || !link.url) {
                return '';
            }
            var label = link.label || 'Source';
            return '<a class="entry-source-link" href="' + escapeHtml(link.url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(label) + '</a>';
        }).join('') + '</div>';
    }

    function findEntryReference(entryKey) {
        var catalogs = [
            { view: 'problems', cfg: VIEW_CONFIG.problems },
            { view: 'interview', cfg: VIEW_CONFIG.interview },
            { view: 'basics', cfg: VIEW_CONFIG.basics },
            { view: 'patterns', cfg: VIEW_CONFIG.patterns },
            { view: 'course', cfg: VIEW_CONFIG.course },
            { view: 'exercises', cfg: VIEW_CONFIG.exercises },
            { view: 'workflow', cfg: VIEW_CONFIG.workflow },
            { view: 'principles', cfg: VIEW_CONFIG.principles }
        ];

        for (var i = 0; i < catalogs.length; i += 1) {
            var item = catalogs[i];
            if (item.cfg && item.cfg.entries && item.cfg.entries[entryKey]) {
                return {
                    view: item.view,
                    entry: item.cfg.entries[entryKey]
                };
            }
        }

        return null;
    }

    function renderCompareEntries(compareEntries) {
        if (!compareEntries || compareEntries.length === 0) {
            return '';
        }

        var html = '<div class="entry-compare-links"><strong>Compare with:</strong> ';
        html += compareEntries.map(function (entryKey) {
            var ref = findEntryReference(entryKey);
            if (!ref || !ref.entry) {
                return '';
            }
            var entry = ref.entry;
            var label = entry.label || entryKey;
            return '<a class="entry-compare-link" href="#" data-compare-view="' + escapeHtml(ref.view) + '" data-compare-key="' + escapeHtml(entryKey) + '">' + escapeHtml(label) + '</a>';
        }).join(' | ');
        html += '</div>';
        return html;
    }

    function chooseNextLang(excluded) {
        for (var i = 0; i < LANG_ORDER.length; i += 1) {
            if (LANG_ORDER[i] !== excluded) {
                return LANG_ORDER[i];
            }
        }
        return excluded || '';
    }

    function normalizeSelectedLangs() {
        if (LANG_ORDER.length === 0) {
            state.selectedLangs = ['', ''];
            return;
        }

        if (LANG_ORDER.indexOf(state.selectedLangs[0]) === -1) {
            state.selectedLangs[0] = LANG_ORDER[0];
        }

        if (LANG_ORDER.indexOf(state.selectedLangs[1]) === -1) {
            state.selectedLangs[1] = chooseNextLang(state.selectedLangs[0]);
        }

        if (state.compareCount === 2 && state.selectedLangs[0] === state.selectedLangs[1]) {
            state.selectedLangs[1] = chooseNextLang(state.selectedLangs[0]);
        }
    }

    function isViewInCurrentCategory(viewKey) {
        var category = VIEW_CATEGORIES[state.viewCategory];
        if (!category) {
            return true;
        }
        return category.views.indexOf(viewKey) !== -1;
    }

    function currentCatalog() {
        if (state.view === 'problems') {
            return VIEW_CONFIG.problems;
        }
        if (state.view === 'interview') {
            return VIEW_CONFIG.interview;
        }
        if (state.view === 'patterns') {
            return VIEW_CONFIG.patterns;
        }
        if (state.view === 'basics') {
            return VIEW_CONFIG.basics;
        }
        if (state.view === 'course') {
            return VIEW_CONFIG.course;
        }
        if (state.view === 'exercises') {
            return VIEW_CONFIG.exercises;
        }
        if (state.view === 'workflow') {
            return VIEW_CONFIG.workflow;
        }
        if (state.view === 'principles') {
            return VIEW_CONFIG.principles;
        }
        return null;
    }

    function selectedItemKey() {
        if (state.view === 'problems') {
            return state.selectedProblem;
        }
        if (state.view === 'interview') {
            return state.selectedInterview;
        }
        if (state.view === 'patterns') {
            return state.selectedPattern;
        }
        if (state.view === 'basics') {
            return state.selectedBasic;
        }
        if (state.view === 'course') {
            return state.selectedCourse;
        }
        if (state.view === 'exercises') {
            return state.selectedExercise;
        }
        if (state.view === 'workflow') {
            return state.selectedWorkflow;
        }
        return state.selectedPrinciple;
    }

    function setSelectedItemKey(key) {
        if (state.view === 'problems') {
            state.selectedProblem = key;
        } else if (state.view === 'interview') {
            state.selectedInterview = key;
        } else if (state.view === 'patterns') {
            state.selectedPattern = key;
        } else if (state.view === 'basics') {
            state.selectedBasic = key;
        } else if (state.view === 'course') {
            state.selectedCourse = key;
        } else if (state.view === 'exercises') {
            state.selectedExercise = key;
        } else if (state.view === 'workflow') {
            state.selectedWorkflow = key;
        } else if (state.view === 'principles') {
            state.selectedPrinciple = key;
        }
    }

    function currentEntry() {
        var catalog = currentCatalog();
        if (!catalog) {
            return null;
        }
        var key = selectedItemKey();
        return catalog.entries[key] || null;
    }

    function handleLanguageClick(langKey, targetSlot) {
        if (state.compareCount === 1) {
            state.selectedLangs[0] = langKey;
            renderAll();
            return;
        }

        var slot = targetSlot === 1 ? 1 : 0;
        var other = slot === 0 ? 1 : 0;

        if (state.selectedLangs[slot] === langKey) {
            state.activeSlot = slot;
            renderAll();
            return;
        }

        if (state.selectedLangs[other] === langKey) {
            var tmp = state.selectedLangs[slot];
            state.selectedLangs[slot] = langKey;
            state.selectedLangs[other] = tmp;
        } else {
            state.selectedLangs[slot] = langKey;
            if (state.selectedLangs[slot] === state.selectedLangs[other]) {
                state.selectedLangs[other] = chooseNextLang(state.selectedLangs[slot]);
            }
        }

        state.activeSlot = slot;
        renderAll();
    }

    function suppressNextLanguageClick(langKey) {
        suppressedLangClick = {
            langKey: langKey,
            expiresAt: Date.now() + 700
        };
    }

    function shouldIgnoreSuppressedLanguageClick(langKey) {
        if (!suppressedLangClick) {
            return false;
        }

        var shouldIgnore = suppressedLangClick.langKey === langKey && Date.now() <= suppressedLangClick.expiresAt;
        suppressedLangClick = null;
        return shouldIgnore;
    }

    function clearLanguageDragPreview() {
        var chips = document.querySelectorAll('#langNav .lang-chip');
        chips.forEach(function (chip) {
            chip.classList.remove('dragging', 'drag-preview-left', 'drag-preview-right');
            chip.style.transform = '';
        });
    }

    function resetLanguageDragState() {
        clearLanguageDragPreview();
        langDragState = null;
    }

    function setLanguageDragPreview(button, slot, deltaX) {
        if (!button) {
            return;
        }

        clearLanguageDragPreview();
        button.classList.add('dragging');
        button.classList.add(slot === 1 ? 'drag-preview-right' : 'drag-preview-left');

        var clampedShift = Math.max(-LANG_DRAG_MAX_SHIFT, Math.min(LANG_DRAG_MAX_SHIFT, deltaX * 0.18));
        button.style.transform = 'translateX(' + clampedShift + 'px)';
    }

    function beginLanguageDrag(event, langKey) {
        if (state.compareCount !== 2 || !event.currentTarget) {
            return;
        }

        if (event.pointerType === 'mouse' && event.button !== 0) {
            return;
        }

        langDragState = {
            pointerId: event.pointerId,
            pointerType: event.pointerType,
            langKey: langKey,
            button: event.currentTarget,
            startX: event.clientX,
            startY: event.clientY,
            previewSlot: null,
            dragging: false
        };

        if (typeof event.currentTarget.setPointerCapture === 'function') {
            try {
                event.currentTarget.setPointerCapture(event.pointerId);
            } catch (err) {
                // ignore capture failures
            }
        }
    }

    function updateLanguageDrag(event) {
        if (!langDragState || event.pointerId !== langDragState.pointerId) {
            return;
        }

        var deltaX = event.clientX - langDragState.startX;
        var deltaY = event.clientY - langDragState.startY;
        var absX = Math.abs(deltaX);
        var absY = Math.abs(deltaY);

        if (absX < LANG_DRAG_THRESHOLD || absX <= absY) {
            clearLanguageDragPreview();
            return;
        }

        langDragState.dragging = true;
        langDragState.previewSlot = deltaX > 0 ? 1 : 0;
        setLanguageDragPreview(langDragState.button, langDragState.previewSlot, deltaX);
        event.preventDefault();
    }

    function endLanguageDrag(event, cancelled) {
        if (!langDragState || event.pointerId !== langDragState.pointerId) {
            return;
        }

        var drag = langDragState;

        if (drag.button && typeof drag.button.releasePointerCapture === 'function') {
            try {
                drag.button.releasePointerCapture(event.pointerId);
            } catch (err) {
                // ignore capture failures
            }
        }

        if (!cancelled && drag.dragging && (drag.previewSlot === 0 || drag.previewSlot === 1)) {
            suppressNextLanguageClick(drag.langKey);
            handleLanguageClick(drag.langKey, drag.previewSlot);
            resetLanguageDragState();
            return;
        }

        if (!cancelled && drag.pointerType !== 'mouse') {
            var totalX = Math.abs(event.clientX - drag.startX);
            var totalY = Math.abs(event.clientY - drag.startY);
            if (totalX < 8 && totalY < 8) {
                suppressNextLanguageClick(drag.langKey);
                handleLanguageClick(drag.langKey, 0);
                resetLanguageDragState();
                return;
            }
        }

        resetLanguageDragState();
    }

    function renderLanguageButtons() {
        var nav = document.getElementById('langNav');
        nav.innerHTML = '';

        for (var i = 0; i < LANG_ORDER.length; i += 1) {
            var langKey = LANG_ORDER[i];
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'chip-btn lang-chip';
            btn.textContent = LANG_LABELS[langKey] || langKey;
            btn.setAttribute('data-lang-key', langKey);

            if (state.selectedLangs[0] === langKey) {
                btn.classList.add('active');
            } else if (state.compareCount === 2 && state.selectedLangs[1] === langKey) {
                btn.classList.add('active-2');
            }

            if (state.compareCount === 2) {
                btn.title = 'Tap selects left panel. Drag left or right to choose a side. Right click still selects right panel.';
            }

            (function (capturedKey) {
                btn.addEventListener('click', function (event) {
                    if (shouldIgnoreSuppressedLanguageClick(capturedKey)) {
                        event.preventDefault();
                        return;
                    }
                    handleLanguageClick(capturedKey, 0);
                });

                btn.addEventListener('contextmenu', function (event) {
                    if (state.compareCount !== 2) {
                        return;
                    }
                    event.preventDefault();
                    handleLanguageClick(capturedKey, 1);
                });

                btn.addEventListener('pointerdown', function (event) {
                    beginLanguageDrag(event, capturedKey);
                });

                btn.addEventListener('pointermove', function (event) {
                    updateLanguageDrag(event);
                });

                btn.addEventListener('pointerup', function (event) {
                    endLanguageDrag(event, false);
                });

                btn.addEventListener('pointercancel', function (event) {
                    endLanguageDrag(event, true);
                });
            }(langKey));

            nav.appendChild(btn);
        }
    }

    function renderViewButtons() {
        var nav = document.getElementById('viewNav');
        nav.innerHTML = '';

        var currentCategory = VIEW_CATEGORIES[state.viewCategory];
        var visibleViews = (currentCategory && currentCategory.views ? currentCategory.views : []).filter(function (viewKey) {
            return !!VIEW_CONFIG[viewKey];
        });

        visibleViews.forEach(function (viewKey) {
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'chip-btn';
            btn.textContent = VIEW_CONFIG[viewKey].label;

            if (state.view === viewKey) {
                btn.classList.add('active');
            }

            btn.addEventListener('click', function () {
                state.view = (state.view === viewKey) ? '' : viewKey;
                renderAll();
            });

            nav.appendChild(btn);
        });
    }

    function renderViewCategorySelector() {
        var nav = document.getElementById('viewNav');
        var rowTitle = nav.previousElementSibling;
        if (!rowTitle || !rowTitle.classList.contains('row-title')) {
            return;
        }

        var currentCat = VIEW_CATEGORIES[state.viewCategory];
        rowTitle.textContent = (currentCat && currentCat.label ? currentCat.label : 'Atlas Views').toUpperCase();
        rowTitle.classList.add('view-category-toggle-title');
        rowTitle.setAttribute('role', 'button');
        rowTitle.setAttribute('tabindex', '0');
        rowTitle.setAttribute('aria-label', 'Toggle view category');

        function toggleViewCategory() {
            state.viewCategory = state.viewCategory === 'atlas' ? 'learning' : 'atlas';
            localStorage.setItem(VIEW_CATEGORY_STORAGE_KEY, state.viewCategory);
            state.view = '';
            renderAll();
        }

        rowTitle.onclick = toggleViewCategory;
        rowTitle.onkeydown = function (event) {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                toggleViewCategory();
            }
        };
    }

    function renderCompareButtons() {
        var toggle = document.getElementById('compareToggle');
        var swap = document.getElementById('swapBtn');
        var course = document.getElementById('courseBtn');
        if (state.view === 'principles') {
            toggle.classList.add('hidden');
            swap.classList.add('hidden');
            if (course) {
                course.classList.remove('active');
            }
            return;
        }

        toggle.classList.remove('hidden');
        var isCompare = state.compareCount === 2;

        toggle.classList.toggle('active', isCompare);
        toggle.setAttribute('aria-pressed', isCompare ? 'true' : 'false');
        swap.classList.toggle('hidden', !isCompare);

        if (course) {
            course.classList.toggle('active', !!state.courseMode);
            course.setAttribute('aria-pressed', state.courseMode ? 'true' : 'false');
            course.title = state.courseMode ? 'Exit course mode' : 'Start 7-level adaptation course';
        }
    }

    function rememberPreCourseView() {
        state.courseReturnState = {
            view: state.view,
            viewCategory: state.viewCategory,
            selectedProblem: state.selectedProblem,
            selectedInterview: state.selectedInterview,
            selectedPattern: state.selectedPattern,
            selectedBasic: state.selectedBasic,
            selectedPrinciple: state.selectedPrinciple,
            selectedCourse: state.selectedCourse,
            selectedExercise: state.selectedExercise,
            selectedWorkflow: state.selectedWorkflow
        };
    }

    function restorePreCourseView() {
        var snapshot = state.courseReturnState;
        state.courseReturnState = null;
        if (!snapshot) {
            renderAll();
            return;
        }
        state.view = snapshot.view;
        state.viewCategory = snapshot.viewCategory;
        state.selectedProblem = snapshot.selectedProblem;
        state.selectedInterview = snapshot.selectedInterview;
        state.selectedPattern = snapshot.selectedPattern;
        state.selectedBasic = snapshot.selectedBasic;
        state.selectedPrinciple = snapshot.selectedPrinciple;
        state.selectedCourse = snapshot.selectedCourse;
        state.selectedExercise = snapshot.selectedExercise;
        state.selectedWorkflow = snapshot.selectedWorkflow;
        renderAll();
    }

    function exitCourseToLearningBasics() {
        state.courseMode = false;
        state.courseLevel = 0;
        state.courseReturnState = null;
        state.viewCategory = 'learning';
        state.view = 'basics';
        renderAll();
    }

    function renderPaletteSelector() {
        var previewButtons = document.querySelectorAll('.palette-preview-btn');
        previewButtons.forEach(function (btn) {
            var isActive = btn.getAttribute('data-palette') === state.palette;
            btn.classList.toggle('active', isActive);
            btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
        });
    }

    function exerciseLabelParts(label) {
        var raw = String(label || '');
        var m = raw.match(/^(Beginner|Intermediate|Advanced)\s*:\s*(.+)$/i);
        if (!m) {
            return { level: '', title: raw || '' };
        }

        var levelRaw = (m[1] || '').toLowerCase();
        var title = m[2] || raw;
        return {
            level: levelRaw,
            title: title,
            levelLabel: levelRaw.charAt(0).toUpperCase() + levelRaw.slice(1)
        };
    }

    function setEntryTitleLevel(level) {
        var titleEl = document.getElementById('entryTitle');
        if (!titleEl) {
            return;
        }

        titleEl.classList.remove('entry-level-beginner', 'entry-level-intermediate', 'entry-level-advanced');
        if (level === 'beginner' || level === 'intermediate' || level === 'advanced') {
            titleEl.classList.add('entry-level-' + level);
        }
    }

    function appendSidebarItem(list, key, entry, activeKey) {
        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'sidebar-item' + (key === activeKey ? ' active' : '');

        if (state.view === 'exercises') {
            var parts = exerciseLabelParts(entry.label || key);
            btn.textContent = parts.title || key;
        } else {
            btn.textContent = entry.label || key;
        }

        btn.setAttribute('data-entry-key', key);
        list.appendChild(btn);
    }

    function renderSidebar() {
        var sidebar = document.getElementById('catalogSidebar');
        var expandBtn = document.getElementById('sidebarExpandBtn');
        var sidebarTitle = document.getElementById('sidebarTitle');
        var list = document.getElementById('sidebarList');
        var sidebarHeader = document.getElementById('topicSidebarHeader');

        var needsSidebar = state.view && state.view !== 'sheets';
        if (!needsSidebar) {
            sidebar.classList.add('hidden');
            expandBtn.classList.add('hidden');
            return;
        }

        var catalog = currentCatalog();
        if (!catalog) {
            sidebar.classList.add('hidden');
            expandBtn.classList.add('hidden');
            return;
        }

        if (state.courseMode) {
            if (state.courseLevelCollapsed) {
                sidebar.classList.add('hidden');
                expandBtn.classList.remove('hidden');
                expandBtn.title = 'Expand course levels';
                expandBtn.setAttribute('aria-label', 'Expand course levels');
            } else {
                sidebar.classList.remove('hidden');
                expandBtn.classList.add('hidden');
            }
            if (sidebarHeader) {
                sidebarHeader.classList.add('hidden');
            }
            if (list) {
                list.classList.add('hidden');
                list.innerHTML = '';
            }
            return;
        }

        if (sidebarHeader) {
            sidebarHeader.classList.remove('hidden');
        }
        if (list) {
            list.classList.remove('hidden');
        }

        var entries = catalog.entries || {};
        var groups = catalog.groups || [];
        var activeKey = selectedItemKey();

        // Ensure the selected key is valid; fall back to first available entry
        if (!entries[activeKey]) {
            var fallbackKey = '';
            for (var gi = 0; gi < groups.length; gi++) {
                for (var ki = 0; ki < groups[gi].keys.length; ki++) {
                    if (entries[groups[gi].keys[ki]]) {
                        fallbackKey = groups[gi].keys[ki];
                        break;
                    }
                }
                if (fallbackKey) { break; }
            }
            if (!fallbackKey) {
                var allKeys = Object.keys(entries);
                fallbackKey = allKeys.length > 0 ? allKeys[0] : '';
            }
            if (fallbackKey) {
                setSelectedItemKey(fallbackKey);
                activeKey = fallbackKey;
            }
        }

        if (sidebarTitle) {
            sidebarTitle.textContent = catalog.itemLabel || 'Items';
        }

        if (state.sidebarCollapsed) {
            sidebar.classList.add('hidden');
            expandBtn.classList.remove('hidden');
        } else {
            sidebar.classList.remove('hidden');
            expandBtn.classList.add('hidden');
        }

        // Build list
        list.innerHTML = '';
        if (groups.length > 0) {
            var seen = {};
            groups.forEach(function (group) {
                var validKeys = group.keys.filter(function (k) { return !!entries[k]; });
                if (validKeys.length === 0) { return; }

                var groupHeader = document.createElement('div');
                groupHeader.className = 'sidebar-group-label';
                groupHeader.textContent = group.label;
                if (state.view === 'exercises') {
                    var levelKey = String(group.label || '').toLowerCase();
                    if (levelKey === 'beginner' || levelKey === 'intermediate' || levelKey === 'advanced') {
                        groupHeader.classList.add('exercise-level', 'level-' + levelKey);
                    }
                }
                list.appendChild(groupHeader);

                validKeys.forEach(function (key) {
                    seen[key] = true;
                    appendSidebarItem(list, key, entries[key], activeKey);
                });
            });

            Object.keys(entries).forEach(function (key) {
                if (!seen[key]) {
                    appendSidebarItem(list, key, entries[key], activeKey);
                }
            });
        } else {
            Object.keys(entries).forEach(function (key) {
                appendSidebarItem(list, key, entries[key], activeKey);
            });
        }

        // Scroll active item into view
        setTimeout(function () {
            var active = list.querySelector('.sidebar-item.active');
            if (active) { active.scrollIntoView({ block: 'nearest' }); }
        }, 0);
    }

    function renderModernNotes(modernNotes, langKey) {
        if (!modernNotes || !langKey) {
            return '';
        }
        var resolvedKey = langKey;
        if (!modernNotes[resolvedKey] && (langKey === 'scala2' || langKey === 'scala3')) {
            resolvedKey = 'scala';
        }
        if (!modernNotes[resolvedKey]) {
            return '';
        }
        var note = modernNotes[resolvedKey];

        function fmtText(text) {
            return escapeHtml(text || '').replace(/`([^`]+)`/g, '<code style="display:inline;white-space:normal;background:#0f1720;color:#dbeafe;padding:2px 6px;border-radius:3px;font-family:\'Consolas\',monospace;font-size:0.85em;">$1</code>');
        }

        return '<div class="doc-table-wrap" style="margin-top:8px">'
            + '<table class="doc-table"><thead><tr>'
            + '<th>Classic approach</th><th>Modern approach</th>'
            + '</tr></thead><tbody><tr>'
            + '<td>' + fmtText(note.classic) + '</td>'
            + '<td>' + fmtText(note.modern) + '</td>'
            + '</tr></tbody></table></div>';
    }

    function renderAdapterInsight(insight) {
        if (!insight) {
            return '';
        }

        function fmtText(text) {
            return escapeHtml(text || '').replace(/`([^`]+)`/g, '<code style="display:inline;white-space:normal;background:#0f1720;color:#dbeafe;padding:2px 6px;border-radius:3px;font-family:\'Consolas\',monospace;font-size:0.85em;">$1</code>');
        }

        if (typeof insight === 'object' && insight.rows && insight.rows.length) {
            var headers = insight.headers || [];
            var headerHtml = headers.length
                ? '<thead><tr>' + headers.map(function (h) { return '<th>' + fmtText(h) + '</th>'; }).join('') + '</tr></thead>'
                : '';
            var rowsHtml = '<tbody>' + insight.rows.map(function (row) {
                return '<tr>' + (row || []).map(function (cell) {
                    return '<td>' + fmtText(cell) + '</td>';
                }).join('') + '</tr>';
            }).join('') + '</tbody>';
            var title = insight.title ? '<strong style="color:#ff8c00">' + fmtText(insight.title) + '</strong>' : '<strong style="color:#ff8c00">Adapter Insight:</strong>';

            return '<div class="adapter-insight" style="margin-top:12px">'
                + '<div style="margin-bottom:6px">' + title + '</div>'
                + '<div class="doc-table-wrap"><table class="doc-table">'
                + headerHtml
                + rowsHtml
                + '</table></div>'
                + '</div>';
        }

        return '<div class="adapter-insight" style="margin-top:12px;padding:8px;border-left:3px solid #ffa500;background:rgba(255,165,0,0.05)">'
            + '<strong style="color:#ff8c00">Adapter Insight:</strong> '
            + fmtText(insight)
            + '</div>';
    }

    function updateEntryMeta(title, description, sourceLinks, modernNotes, adapterInsight, compareEntries, langKey) {
        var meta = document.getElementById('entryMeta');
        var titleEl = document.getElementById('entryTitle');
        var descEl = document.getElementById('entryDesc');
        var sourceEl = document.getElementById('entrySourceLinks');
        var modernEl = document.getElementById('entryModernNotes');
        var adapterEl = document.getElementById('entryAdapterInsight');
        var compareEl = document.getElementById('entryCompareLinks');

        if (!title && !description && (!sourceLinks || sourceLinks.length === 0)) {
            meta.classList.add('hidden');
            titleEl.textContent = '';
            descEl.textContent = '';
            sourceEl.innerHTML = '';
            if (modernEl) { modernEl.innerHTML = ''; }
            if (adapterEl) { adapterEl.innerHTML = ''; }
            if (compareEl) { compareEl.innerHTML = ''; }
            return;
        }

        meta.classList.remove('hidden');
        titleEl.textContent = title || '';
        descEl.textContent = description || '';
        sourceEl.innerHTML = renderSourceLinks(sourceLinks);
        if (modernEl) { modernEl.innerHTML = renderModernNotes(modernNotes, langKey); }
        if (adapterEl) { adapterEl.innerHTML = renderAdapterInsight(adapterInsight); }
        if (compareEl) { compareEl.innerHTML = renderCompareEntries(compareEntries); }
    }

    function renderSheetsView() {
        var host = document.getElementById('contentHost');

        if (state.compareCount === 1) {
            var singleLang = state.selectedLangs[0];
            var singleSheet = SHEETS[singleLang];
            var singleBody = singleSheet && singleSheet.body
                ? singleSheet.body
                : '<p class="empty-note">Sheet not found for ' + escapeHtml(singleLang) + '.</p>';

            host.innerHTML = ''
                + '<div class="display-grid">'
                + '  <section class="display-panel">'
                + '    <div class="display-title">' + escapeHtml(LANG_LABELS[singleLang] || singleLang) + '</div>'
                + '    <div class="panel-body sheet-body">' + singleBody + '</div>'
                + '  </section>'
                + '</div>';
            return;
        }

        var leftLang = state.selectedLangs[0];
        var rightLang = state.selectedLangs[1];
        var leftSheet = SHEETS[leftLang];
        var rightSheet = SHEETS[rightLang];
        var leftBody = leftSheet && leftSheet.body
            ? leftSheet.body
            : '<p class="empty-note">Sheet not found for ' + escapeHtml(leftLang) + '.</p>';
        var rightBody = rightSheet && rightSheet.body
            ? rightSheet.body
            : '<p class="empty-note">Sheet not found for ' + escapeHtml(rightLang) + '.</p>';

        host.innerHTML = ''
            + '<div class="display-grid compare">'
            + '  <section class="display-panel compare-panel' + (state.activeSlot === 0 ? ' active-side' : '') + '" data-side="0">'
            + '    <button type="button" class="display-side-btn side-pick-btn' + (state.activeSlot === 0 ? ' active' : '') + '" data-side="0">Left: ' + escapeHtml(LANG_LABELS[leftLang] || leftLang) + '</button>'
            + '    <div class="panel-body sheet-body">' + leftBody + '</div>'
            + '  </section>'
            + '  <section class="display-panel compare-panel' + (state.activeSlot === 1 ? ' active-side' : '') + '" data-side="1">'
            + '    <button type="button" class="display-side-btn side-pick-btn' + (state.activeSlot === 1 ? ' active' : '') + '" data-side="1">Right: ' + escapeHtml(LANG_LABELS[rightLang] || rightLang) + '</button>'
            + '    <div class="panel-body sheet-body">' + rightBody + '</div>'
            + '  </section>'
            + '</div>';
    }

    function renderHomeView() {
        setEntryTitleLevel('');
        var host = document.getElementById('contentHost');
        var baseHtml = HOME_HTML;
        var selected = [];

        function listLabels(viewKeys) {
            return (viewKeys || []).map(function (k) {
                return VIEW_CONFIG[k] ? VIEW_CONFIG[k].label : k;
            }).filter(Boolean);
        }

        function renderUsageGuideGraphic() {
            var atlasViews = listLabels((VIEW_CATEGORIES.atlas && VIEW_CATEGORIES.atlas.views) || []);
            var learningViews = listLabels((VIEW_CATEGORIES.learning && VIEW_CATEGORIES.learning.views) || []);

            var primaryLangKey = LANG_ORDER.indexOf(state.selectedLangs[0]) !== -1
                ? state.selectedLangs[0]
                : (LANG_ORDER[0] || 'cpp');

            var secondaryLangKey = LANG_ORDER.indexOf(state.selectedLangs[1]) !== -1
                ? state.selectedLangs[1]
                : chooseNextLang(primaryLangKey);

            if (!secondaryLangKey || secondaryLangKey === primaryLangKey) {
                secondaryLangKey = chooseNextLang(primaryLangKey);
            }

            var movingLangKey = LANG_ORDER.find(function (k) {
                return k !== primaryLangKey && k !== secondaryLangKey;
            });

            if (!movingLangKey) {
                movingLangKey = chooseNextLang(secondaryLangKey || primaryLangKey);
            }

            var primaryLang = LANG_LABELS[primaryLangKey] || primaryLangKey || 'C++';
            var secondaryLang = LANG_LABELS[secondaryLangKey] || secondaryLangKey || 'Python';
            var movingLang = LANG_LABELS[movingLangKey] || movingLangKey || 'Go';

            var allLangChips = [primaryLang, secondaryLang, movingLang];
            LANG_ORDER.forEach(function (k) {
                if (k === primaryLangKey || k === secondaryLangKey || k === movingLangKey) {
                    return;
                }
                var label = LANG_LABELS[k] || k;
                if (label) {
                    allLangChips.push(label);
                }
            });

            function chipsToHtml(items) {
                if (!items.length) {
                    return '<span class="viewset-view-chip">No Views</span>';
                }
                return items.map(function (v) {
                    return '<span class="viewset-view-chip">' + escapeHtml(v) + '</span>';
                }).join('');
            }

            function renderTargetSequence(direction) {
                var right = direction === 'right';
                var head = allLangChips.slice(0, 2);
                var tail = allLangChips.slice(3);
                var html = '';

                head.forEach(function (label, idx) {
                    var cls = 'usage-chip';
                    cls += idx === 0 ? ' is-left' : ' is-right';
                    html += '<span class="' + cls + '">' + escapeHtml(label) + '</span>';
                });

                html += '<span class="usage-chip ' + (right ? 'is-moving-right' : 'is-moving-left') + '">' + escapeHtml(movingLang) + '</span>';

                tail.forEach(function (label) {
                    html += '<span class="usage-chip">' + escapeHtml(label) + '</span>';
                });

                return html;
            }

            return ''
                + '<section class="usage-guide-graphic">'
                + '  <header class="usage-guide-header">'
                + '    <h2>Graphical Usage Guide</h2>'
                + '    <p>This guide is generated from current project state so labels and views stay up to date.</p>'
                + '  </header>'
                + '  <div class="usage-steps-grid">'
                + '    <article class="usage-step-card">'
                + '      <div class="usage-step-number">1</div>'
                + '      <h3 class="usage-step-title">Selection Controls</h3>'
                + '      <p class="usage-step-text">Compare controls one-panel or two-panel selection. Swap flashes and swaps the language order.</p>'
                + '      <div class="usage-compare-demo">'
                + '        <div class="usage-compare-state state-off">'
                + '          <div class="usage-inline-row"><span class="usage-inline-label">Compare</span><div class="usage-chip-row"><span class="usage-chip is-left">' + escapeHtml(primaryLang) + '</span></div></div>'
                + '        </div>'
                + '        <div class="usage-compare-state state-on">'
                + '          <div class="usage-inline-row"><span class="usage-inline-label is-on">Compare</span><div class="usage-chip-row"><span class="usage-chip is-left">' + escapeHtml(primaryLang) + '</span><span class="usage-chip is-right">' + escapeHtml(secondaryLang) + '</span></div></div>'
                + '          <div class="usage-inline-row selection-swap-demo"><span class="usage-inline-label swap-btn">Swap</span><div class="usage-compare-unified"><div class="usage-target-unified"><div class="usage-target-lang-row"><span class="usage-target-lang-cell panel-left-active swap-side"><span class="swap-label-old">' + escapeHtml(primaryLang) + '</span><span class="swap-label-new">' + escapeHtml(secondaryLang) + '</span></span><span class="usage-target-lang-cell panel-right-active swap-side"><span class="swap-label-old">' + escapeHtml(secondaryLang) + '</span><span class="swap-label-new">' + escapeHtml(primaryLang) + '</span></span></div><div class="usage-target-code-row"><span class="usage-target-code-cell">//code//</span><span class="usage-target-code-cell">//code//</span></div></div></div></div>'
                + '        </div>'
                + '      </div>'
                + '    </article>'
                + '    <article class="usage-step-card">'
                + '      <div class="usage-step-number">2</div>'
                + '      <h3 class="usage-step-title">Language Targeting</h3>'
                + '      <p class="usage-step-text">Moving language replaces the targeted side. Highlight shifts to the new selected pair.</p>'
                + '      <div class="usage-lang-target-demo">'
                + '        <div class="usage-target-block target-right">'
                + '          <h4>Right Target</h4>'
                + '          <div class="usage-chip-row usage-target-seq">' + renderTargetSequence('right') + '</div>'
                + '          <div class="usage-target-result">'
                + '            <div class="usage-target-unified">'
                + '              <div class="usage-target-lang-row">'
                + '                <span class="usage-target-lang-cell panel-left-active">' + escapeHtml(primaryLang) + '</span>'
                + '                <span class="usage-target-lang-cell usage-panel-dynamic panel-right-active">'
                + '                <span class="label-old">' + escapeHtml(secondaryLang) + '</span>'
                + '                <span class="label-new">' + escapeHtml(movingLang) + '</span>'
                + '                </span>'
                + '              </div>'
                + '              <div class="usage-target-code-row">'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '              </div>'
                + '            </div>'
                + '          </div>'
                + '        </div>'
                + '        <div class="usage-target-block target-left">'
                + '          <h4>Left Target</h4>'
                + '          <div class="usage-chip-row usage-target-seq">' + renderTargetSequence('left') + '</div>'
                + '          <div class="usage-target-result">'
                + '            <div class="usage-target-unified">'
                + '              <div class="usage-target-lang-row">'
                + '                <span class="usage-target-lang-cell usage-panel-dynamic panel-left-active">'
                + '                <span class="label-old">' + escapeHtml(primaryLang) + '</span>'
                + '                <span class="label-new">' + escapeHtml(movingLang) + '</span>'
                + '                </span>'
                + '                <span class="usage-target-lang-cell panel-right-active">' + escapeHtml(secondaryLang) + '</span>'
                + '              </div>'
                + '              <div class="usage-target-code-row">'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '                <span class="usage-target-code-cell">//code//</span>'
                + '              </div>'
                + '            </div>'
                + '          </div>'
                + '        </div>'
                + '      </div>'
                + '    </article>'
                + '    <article class="usage-step-card">'
                + '      <div class="usage-step-number">3</div>'
                + '      <h3 class="usage-step-title">Choose View Set</h3>'
                + '      <p class="usage-step-text">Switch between ATLAS VIEWS and LEARNING VIEWS, then read the active view keywords below.</p>'
                + '      <div class="usage-viewset-demo">'
                + '        <div class="usage-viewset-state state-atlas">'
                + '          <span class="viewset-stage-label atlas">ATLAS VIEWS</span>'
                + '          <div class="viewset-view-chips">' + chipsToHtml(atlasViews) + '</div>'
                + '        </div>'
                + '        <div class="usage-viewset-state state-learning">'
                + '          <span class="viewset-stage-label learning">LEARNING VIEWS</span>'
                + '          <div class="viewset-view-chips">' + chipsToHtml(learningViews) + '</div>'
                + '        </div>'
                + '      </div>'
                + '    </article>'
                + '  </div>'
                + '</section>';
        }

        function pushUniqueLang(langKey) {
            var base = langKey;
            if (base === 'scala2' || base === 'scala3') {
                base = 'scala';
            }
            if (!base || selected.indexOf(base) !== -1) {
                return;
            }
            selected.push(base);
        }

        pushUniqueLang(state.selectedLangs[0]);
        if (state.compareCount === 2) {
            pushUniqueLang(state.selectedLangs[1]);
        }

        function snippetLanguage(baseLang) {
            if (baseLang === 'scala') {
                return 'scala';
            }
            return highlightLang(baseLang);
        }

        var cards = '';
        selected.forEach(function (langKey) {
            var profile = LANGUAGE_SPECIFIC_BEGINNER_GUIDE[langKey] || null;
            var points = LANGUAGE_SPECIFIC_FEATURES[langKey] || [];

            if (!profile) {
                var fallbackList = '<ul>' + points.map(function (p) {
                    return '<li>' + escapeHtml(p) + '</li>';
                }).join('') + '</ul>';
                cards += ''
                    + '<article class="lang-feature-card">'
                    + '  <h3 class="lang-feature-lang">' + escapeHtml(LANG_LABELS[langKey] || langKey) + '</h3>'
                    + '  <p class="lang-feature-intro">Detailed beginner guide is not configured yet.</p>'
                    + '  <section class="lang-feature-section">'
                    + '    <h4 class="lang-feature-heading">Key Features</h4>'
                    +      fallbackList
                    + '  </section>'
                    + '</article>';
                return;
            }

            var mindsetHtml = '<ul>' + (profile.mindsets || []).map(function (point) {
                return '<li>' + escapeHtml(point) + '</li>';
            }).join('') + '</ul>';

            var snippetHtml = (profile.snippets || []).map(function (item) {
                return ''
                    + '<section class="lang-feature-snippet">'
                    + '  <h4 class="lang-feature-heading">' + escapeHtml(item.title || 'Snippet') + '</h4>'
                    + '  <p>' + escapeHtml(item.note || '') + '</p>'
                    + '  <pre class="code-block home-code-block"><code class="code-sample language-' + snippetLanguage(langKey) + '">' + escapeHtml(item.code || '') + '</code></pre>'
                    + '</section>';
            }).join('');

            cards += ''
                + '<article class="lang-feature-card">'
                + '  <h3 class="lang-feature-lang">' + escapeHtml(LANG_LABELS[langKey] || langKey) + '</h3>'
                + '  <p class="lang-feature-intro">' + escapeHtml(profile.intro || '') + '</p>'
                + '  <section class="lang-feature-section">'
                + '    <h4 class="lang-feature-heading">Beginner Mindset</h4>'
                +      mindsetHtml
                + '  </section>'
                + '  <section class="lang-feature-section">'
                + '    <h4 class="lang-feature-heading">Code Patterns</h4>'
                +      snippetHtml
                + '  </section>'
                + '</article>';
        });

        if (!cards) {
            cards = ''
                + '<article class="lang-feature-card">'
                + '  <h3 class="lang-feature-lang">No language selected</h3>'
                + '  <p class="lang-feature-intro">Pick one or two languages from the top row to see beginner-friendly language-specific features.</p>'
                + '</article>';
        }

        var dynamicSection = ''
            + '<div class="lang-feature-overview">'
            + '  <p>Some advanced features are intentionally language-specific and should be documented per language instead of forced into one-to-one equivalents. <span class="lang-feature-overview-highlight">This section explains why each feature matters, then shows tiny snippets you can pattern-match while learning.</span></p>'
            + '</div>'
            + '<div class="lang-feature-grid">' + cards + '</div>';

        baseHtml = baseHtml.replace('<h2>Quick Usage Guide</h2>', '<h2>Quick Usage Guide</h2>' + renderUsageGuideGraphic());

        baseHtml = baseHtml.replace('<p>__LANG_SPECIFIC_FEATURES__</p>', dynamicSection);
        baseHtml = baseHtml.replace('__LANG_SPECIFIC_FEATURES__', dynamicSection);

        host.innerHTML = ''
            + '<div class="display-grid">'
            + '  <section class="display-panel">'
            + '    <div class="panel-body doc-body">' + baseHtml + '</div>'
            + '  </section>'
            + '</div>';
    }

    function exercisePanel(entry, langKey, sideIndex) {
        var titleHtml = '';
        var exerciseTitle = exerciseLabelParts(entry.label || '').title || entry.label || '';
        var sectionAttrs = ' class="display-panel"';
        if (sideIndex === 0 || sideIndex === 1) {
            sectionAttrs = ' class="display-panel compare-panel' + (state.activeSlot === sideIndex ? ' active-side' : '') + '" data-side="' + sideIndex + '"';
            titleHtml = '<button type="button" class="display-side-btn side-pick-btn' + (state.activeSlot === sideIndex ? ' active' : '') + '" data-side="' + sideIndex + '">' + escapeHtml((sideIndex === 0 ? 'Left: ' : 'Right: ') + (LANG_LABELS[langKey] || langKey)) + '</button>';
        } else {
            titleHtml = '<div class="display-title">Task: ' + escapeHtml(exerciseTitle) + ' (' + escapeHtml(LANG_LABELS[langKey] || langKey) + ')</div>';
        }

        return ''
            + '<section' + sectionAttrs + '>'
            + titleHtml
            + '  <div class="panel-body exercise-panel-body">'
            + '    <button type="button" class="chip-btn exercise-solution-toggle" aria-expanded="false">Show Solution</button>'
            + '    <div class="exercise-solution hidden">'
            + '      <pre class="code-block"><code class="code-sample language-' + highlightLang(langKey) + '">' + escapeHtml(codeFor(entry, langKey)) + '</code></pre>'
            + '    </div>'
            + '  </div>'
            + '</section>';
    }

    function renderExercisesView() {
        var host = document.getElementById('contentHost');
        var entry = currentEntry();

        if (!entry) {
            updateEntryMeta('', '', [], null, null, null, state.selectedLangs[0]);
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No exercise tasks available.</p></section></div>';
            return;
        }

        var parts = exerciseLabelParts(entry.label || '');
        var exerciseTitle = parts.title || entry.label || '';
        updateEntryMeta(exerciseTitle, entry.description || '', entry.sourceLinks || [], null, null, entry.compareEntries || [], state.selectedLangs[0]);
        setEntryTitleLevel(parts.level || '');

        if (state.compareCount === 1) {
            var lang = state.selectedLangs[0];
            host.innerHTML = ''
                + '<div class="display-grid">'
                + exercisePanel(entry, lang, null)
                + '</div>';
            return;
        }

        var leftLang = state.selectedLangs[0];
        var rightLang = state.selectedLangs[1];
        host.innerHTML = ''
            + '<div class="display-grid compare">'
            + exercisePanel(entry, leftLang, 0)
            + exercisePanel(entry, rightLang, 1)
            + '</div>';
    }

    function codeFor(entry, langKey) {
        if (!entry || !entry.codes) {
            return '// missing';
        }
        return entry.codes[langKey] || '// missing';
    }

    function highlightLang(langKey) {
        return LANG_TO_HL[langKey] || 'plaintext';
    }

    function syncHighlightTheme() {
        var darkTheme = document.getElementById('hljsDarkTheme');
        var lightTheme = document.getElementById('hljsLightTheme');
        if (!darkTheme || !lightTheme) {
            return;
        }

        if (state.theme === 'light') {
            lightTheme.disabled = false;
            darkTheme.disabled = true;
        } else {
            darkTheme.disabled = false;
            lightTheme.disabled = true;
        }
    }

    function updateThemeToggle() {
        var toggle = document.getElementById('themeToggle');
        if (!toggle) {
            return;
        }

        var isDark = state.theme === 'dark';
        toggle.innerHTML = isDark ? '&#9728;' : '&#9790;';
        toggle.title = isDark ? 'Switch to light theme' : 'Switch to dark theme';
        toggle.setAttribute('aria-label', toggle.title);
    }

    function applyTheme(themeName) {
        state.theme = themeName === 'light' ? 'light' : 'dark';

        document.body.classList.remove('theme-light', 'theme-dark');
        document.body.classList.add(state.theme === 'light' ? 'theme-light' : 'theme-dark');

        updateThemeToggle();
        syncHighlightTheme();
        applySyntaxHighlight();

        try {
            window.localStorage.setItem(THEME_STORAGE_KEY, state.theme);
        } catch (err) {
            // storage can be disabled
        }
    }

    function applyPalette(paletteName) {
        state.palette = normalizePaletteKey(paletteName);

        document.body.classList.remove('palette-brand', 'palette-technical', 'palette-soft');
        document.body.classList.add('palette-' + state.palette);

        renderPaletteSelector();

        try {
            window.localStorage.setItem(PALETTE_STORAGE_KEY, state.palette);
        } catch (err) {
            // storage can be disabled
        }
    }

    function codePanel(title, code, sideIndex, langKey, modernCode) {
        var titleHtml = '';
        var sectionAttrs = ' class="display-panel"';
        if (sideIndex === 0 || sideIndex === 1) {
            sectionAttrs = ' class="display-panel compare-panel' + (state.activeSlot === sideIndex ? ' active-side' : '') + '" data-side="' + sideIndex + '"';
            titleHtml = '<button type="button" class="display-side-btn side-pick-btn' + (state.activeSlot === sideIndex ? ' active' : '') + '" data-side="' + sideIndex + '">' + escapeHtml(title) + '</button>';
        } else {
            titleHtml = '<div class="display-title">' + escapeHtml(title) + '</div>';
        }

        var codeClass = 'code-sample language-' + highlightLang(langKey);

        var modernHtml = '';
        if (modernCode) {
            modernHtml = '<div class="display-title display-title-subtle">Modern ' + escapeHtml(LANG_LABELS[langKey] || langKey) + '</div>'
                + '<pre class="code-block"><code class="code-sample language-' + highlightLang(langKey) + '">' + escapeHtml(modernCode) + '</code></pre>';
        }

        return ''
            + '<section' + sectionAttrs + '>'
            + titleHtml
            + '  <pre class="code-block"><code class="' + codeClass + '">' + escapeHtml(code) + '</code></pre>'
            + modernHtml
            + '</section>';
    }

    function courseTopicCollapseKey(topicKey) {
        return String(state.courseLevel) + ':' + String(topicKey || '');
    }

    function isCourseTopicCollapsed(topicKey, topicIndex) {
        var key = courseTopicCollapseKey(topicKey);
        if (Object.prototype.hasOwnProperty.call(state.courseTopicCollapsed, key)) {
            return !!state.courseTopicCollapsed[key];
        }
        return topicIndex > 0;
    }

    function topicBodyGrid(entry) {
        function modernKey(langKey) {
            var base = (langKey === 'scala2' || langKey === 'scala3') ? 'scala' : langKey;
            return base + '_modern';
        }

        if (state.compareCount === 1) {
            var lang = state.selectedLangs[0];
            var modernCode = (entry.codes && entry.codes[modernKey(lang)]) || null;
            return ''
                + '<div class="display-grid">'
                + codePanel('Code: ' + (LANG_LABELS[lang] || lang), codeFor(entry, lang), null, lang, modernCode)
                + '</div>';
        }

        var leftLang = state.selectedLangs[0];
        var rightLang = state.selectedLangs[1];
        var leftModern = (entry.codes && entry.codes[modernKey(leftLang)]) || null;
        var rightModern = (entry.codes && entry.codes[modernKey(rightLang)]) || null;

        return ''
            + '<div class="display-grid compare">'
            + codePanel('Left: ' + (LANG_LABELS[leftLang] || leftLang), codeFor(entry, leftLang), 0, leftLang, leftModern)
            + codePanel('Right: ' + (LANG_LABELS[rightLang] || rightLang), codeFor(entry, rightLang), 1, rightLang, rightModern)
            + '</div>';
    }

    function renderCourseTopicsView() {
        var host = document.getElementById('contentHost');
        var level = ADAPTATION_COURSE[state.courseLevel];
        var entries = (VIEW_CONFIG.basics && VIEW_CONFIG.basics.entries) ? VIEW_CONFIG.basics.entries : {};

        updateEntryMeta('', '', [], null, null, null, state.selectedLangs[0]);

        if (!level) {
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No course level configured.</p></section></div>';
            return;
        }

        var keys = (level.viewItems || []).filter(function (key) {
            return !!entries[key];
        });

        if (keys.length === 0) {
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No basic topics are mapped to this course level yet.</p></section></div>';
            return;
        }

        var html = keys.map(function (key, idx) {
            var entry = entries[key];
            var collapsed = isCourseTopicCollapsed(key, idx);
            var descHtml = entry.description
                ? '<p class="course-topic-desc">' + escapeHtml(entry.description) + '</p>'
                : '';
            var insightHtml = entry.adapterInsight
                ? '<div class="course-topic-insight">' + renderAdapterInsight(entry.adapterInsight) + '</div>'
                : '';
            var compareHtml = renderCompareEntries(entry.compareEntries || []);

            return ''
                + '<section class="course-topic-section">'
                + '  <button type="button" class="course-topic-toggle" data-topic-key="' + escapeHtml(key) + '" data-topic-index="' + idx + '" aria-expanded="' + (collapsed ? 'false' : 'true') + '">'
                + '    <span class="course-topic-title">' + escapeHtml(entry.label || key) + '</span>'
                + '    <span class="course-topic-caret">' + (collapsed ? '\u25BE' : '\u25B4') + '</span>'
                + '  </button>'
                + '  <div class="course-topic-body' + (collapsed ? ' hidden' : '') + '">'
                +       descHtml
                +       insightHtml
                +       compareHtml
                +       topicBodyGrid(entry)
                + '  </div>'
                + '</section>';
        }).join('');

        host.innerHTML = '<div class="course-topics-stack">' + html + '</div>';
    }

    function applySyntaxHighlight() {
        if (!window.hljs || typeof window.hljs.highlightElement !== 'function') {
            return;
        }

        var blocks = document.querySelectorAll('#contentHost .code-sample');
        blocks.forEach(function (block) {
            block.removeAttribute('data-highlighted');
            try {
                window.hljs.highlightElement(block);
            } catch (err) {
                // ignore malformed snippets
            }
        });
    }

    function renderCodeView() {
        setEntryTitleLevel('');
        if (state.courseMode) {
            renderCourseTopicsView();
            return;
        }
        var host = document.getElementById('contentHost');
        var entry = currentEntry();

        if (!entry) {
            updateEntryMeta('', '', [], null, null, null, state.selectedLangs[0]);
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No entries available for this view.</p></section></div>';
            return;
        }

        updateEntryMeta(entry.label || '', entry.description || '', entry.sourceLinks || [], entry.modernNotes || null, entry.adapterInsight || null, entry.compareEntries || [], state.selectedLangs[0]);

        function modernKey(langKey) {
            var base = (langKey === 'scala2' || langKey === 'scala3') ? 'scala' : langKey;
            return base + '_modern';
        }

        if (state.compareCount === 1) {
            var lang = state.selectedLangs[0];
            var modernCode = (entry.codes && entry.codes[modernKey(lang)]) || null;
            host.innerHTML = ''
                + '<div class="display-grid">'
                + codePanel('Code: ' + (LANG_LABELS[lang] || lang), codeFor(entry, lang), null, lang, modernCode)
                + '</div>';
            return;
        }

        var leftLang = state.selectedLangs[0];
        var rightLang = state.selectedLangs[1];
        var leftModern = (entry.codes && entry.codes[modernKey(leftLang)]) || null;
        var rightModern = (entry.codes && entry.codes[modernKey(rightLang)]) || null;
        host.innerHTML = ''
            + '<div class="display-grid compare">'
            + codePanel('Left: ' + (LANG_LABELS[leftLang] || leftLang), codeFor(entry, leftLang), 0, leftLang, leftModern)
            + codePanel('Right: ' + (LANG_LABELS[rightLang] || rightLang), codeFor(entry, rightLang), 1, rightLang, rightModern)
            + '</div>';
    }

    function renderPrinciplesView() {
        setEntryTitleLevel('');
        var host = document.getElementById('contentHost');
        var entry = currentEntry();

        if (!entry) {
            updateEntryMeta('', '', [], null, null, null, state.selectedLangs[0]);
            host.innerHTML = '<div class="display-grid"><section class="display-panel"><p class="empty-note">No principles available.</p></section></div>';
            return;
        }

        updateEntryMeta('', '', [], null, null, null, state.selectedLangs[0]);

        var points = entry.points || [];
        var notes = entry.notes || [
            'Use this principle as a guideline, not an absolute law.',
            'Balance it against delivery speed, performance, and team context.'
        ];
        var pitfalls = entry.pitfalls || [
            'Applying the principle as a rigid rule instead of context-sensitive guidance.',
            'Over-engineering abstractions too early before requirements stabilize.',
            'Ignoring trade-offs in performance, delivery speed, or team familiarity.'
        ];
        var refs = entry.sourceLinks || [];
        var notesHtml = notes.length
            ? '<ul>' + notes.map(function (n) { return '<li>' + escapeHtml(n) + '</li>'; }).join('') + '</ul>'
            : '<p class="empty-note">No notes for this principle yet.</p>';
        var listHtml = points.length
            ? '<ul>' + points.map(function (p) { return '<li>' + escapeHtml(p) + '</li>'; }).join('') + '</ul>'
            : '<p class="empty-note">No practical guidelines listed.</p>';
        var pitfallsHtml = pitfalls.length
            ? '<ul>' + pitfalls.map(function (p) { return '<li>' + escapeHtml(p) + '</li>'; }).join('') + '</ul>'
            : '<p class="empty-note">No pitfalls listed.</p>';
        var refsHtml = refs.length
            ? '<p>' + refs.map(function (r) {
                var label = r && r.label ? r.label : 'Source';
                var url = r && r.url ? r.url : '';
                if (!url) {
                    return escapeHtml(label);
                }
                return '<a href="' + escapeHtml(url) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(label) + '</a>';
            }).join('<br>') + '</p>'
            : '<p class="empty-note">No references listed.</p>';

        host.innerHTML = ''
            + '<div class="display-grid">'
            + '  <section class="display-panel">'
            + '    <div class="panel-body doc-body principles-body">'
            + '      <section class="principles-section principles-header">'
            + '        <h2>' + escapeHtml(entry.label || '') + '</h2>'
            + '        <p>' + escapeHtml(entry.description || '') + '</p>'
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>Notes</h3>'
            +          notesHtml
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>Practical Guidelines</h3>'
            +          listHtml
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>Common Pitfalls</h3>'
            +          pitfallsHtml
            + '      </section>'
            + '      <section class="principles-section">'
            + '        <h3>References</h3>'
            +          refsHtml
            + '      </section>'
            + '    </div>'
            + '  </section>'
            + '</div>';
    }

    function updateStickyOffset() {
        var topStack = document.getElementById('topStack');
        var offset = topStack ? (topStack.offsetHeight + 8) : 0;
        document.documentElement.style.setProperty('--sticky-offset', String(offset) + 'px');
    }

    function renderOfflineWarning() {
        var warning = document.getElementById('runtimeWarning');
        if (!warning) {
            return;
        }

        if (window.__hljsMissingFallback) {
            warning.textContent = 'We are offline and do not have access to fallback folder "assets/hljs" that needs to be next to this HTML file.';
            warning.classList.remove('hidden');
            return;
        }

        warning.classList.add('hidden');
        warning.textContent = '';
    }

    function renderAll() {
        normalizeSelectedLangs();
        renderLanguageButtons();
        renderViewCategorySelector();
        renderViewButtons();
        renderCompareButtons();
        renderPaletteSelector();
        renderOfflineWarning();
            // In course mode, hide only the Views controls — keep style/compare/course visible.
            var viewsSelection = document.getElementById('viewsSelection');
            if (viewsSelection) {
                viewsSelection.classList.toggle('hidden', !!state.courseMode);
        }
        renderCourseLevelPanel();
        renderCourseNavHeader();
        renderSidebar();

        if (state.view === 'sheets') {
            updateEntryMeta('Language Reference Sheet', '', [], null, null, null, state.selectedLangs[0]);
            renderSheetsView();
        } else if (!state.view) {
            updateEntryMeta('', '', [], null, null, null, state.selectedLangs[0]);
            renderHomeView();
        } else if (state.view === 'exercises') {
            renderExercisesView();
        } else if (state.view === 'principles') {
            renderPrinciplesView();
        } else {
            renderCodeView();
        }

        applySyntaxHighlight();
        updateStickyOffset();
    }

    document.getElementById('compareToggle').addEventListener('click', function () {
        state.compareCount = state.compareCount === 2 ? 1 : 2;
        if (state.activeSlot !== 0 && state.activeSlot !== 1) {
            state.activeSlot = 0;
        }
        renderAll();
    });

    document.getElementById('contentHost').addEventListener('click', function (event) {
        var btn = event.target.closest('.side-pick-btn');
        if (!btn || state.compareCount !== 2) {
            return;
        }
        var side = Number(btn.dataset.side);
        if (side !== 0 && side !== 1) {
            return;
        }
        state.activeSlot = side;
        renderAll();
    });

    document.getElementById('contentHost').addEventListener('click', function (event) {
        var toggle = event.target.closest('.exercise-solution-toggle');
        if (!toggle) {
            return;
        }

        var panelBody = toggle.closest('.exercise-panel-body');
        if (!panelBody) {
            return;
        }

        var solution = panelBody.querySelector('.exercise-solution');
        if (!solution) {
            return;
        }

        var willOpen = solution.classList.contains('hidden');
        solution.classList.toggle('hidden', !willOpen);
        toggle.textContent = willOpen ? 'Hide Solution' : 'Show Solution';
        toggle.setAttribute('aria-expanded', willOpen ? 'true' : 'false');

        if (willOpen) {
            applySyntaxHighlight();
        }
    });

    document.getElementById('contentHost').addEventListener('click', function (event) {
        var toggle = event.target.closest('.course-topic-toggle');
        if (!toggle || !state.courseMode) {
            return;
        }
        var topicKey = toggle.getAttribute('data-topic-key');
        var topicIndex = Number(toggle.getAttribute('data-topic-index'));
        if (!topicKey) {
            return;
        }
        var collapseKey = courseTopicCollapseKey(topicKey);
        var collapsed = isCourseTopicCollapsed(topicKey, isNaN(topicIndex) ? 0 : topicIndex);
        state.courseTopicCollapsed[collapseKey] = !collapsed;
        renderAll();
    });

    document.getElementById('swapBtn').addEventListener('click', function () {
        var tmp = state.selectedLangs[0];
        state.selectedLangs[0] = state.selectedLangs[1];
        state.selectedLangs[1] = tmp;
        renderAll();
    });

    document.getElementById('courseBtn').addEventListener('click', function () {
        if (state.courseMode) {
            // Toggle OFF: exit course mode
            state.courseMode = false;
            state.courseLevel = 0;
            restorePreCourseView();
            return;
        }
        // Toggle ON: enter course mode at level 1
        rememberPreCourseView();
        state.courseMode = true;
        state.courseLevel = 0;
        state.viewCategory = 'atlas';
        navigateCourse(0);
    });

    document.getElementById('coursePrevBtn').addEventListener('click', function () {
        if (state.courseMode && state.courseLevel > 0) {
            navigateCourse(state.courseLevel - 1);
        }
    });

    document.getElementById('courseNextBtn').addEventListener('click', function () {
        if (state.courseMode && state.courseLevel < ADAPTATION_COURSE.length - 1) {
            navigateCourse(state.courseLevel + 1);
        }
    });

    document.getElementById('courseExitBtn').addEventListener('click', function () {
        exitCourseToLearningBasics();
    });

    document.getElementById('courseLevelToggleBtn').addEventListener('click', function () {
        state.courseLevelCollapsed = true;
        renderSidebar();
    });

    function navigateCourse(levelIndex) {
        if (!ADAPTATION_COURSE || levelIndex < 0 || levelIndex >= ADAPTATION_COURSE.length) {
            return;
        }
        state.courseLevel = levelIndex;
        var level = ADAPTATION_COURSE[levelIndex];
        var viewItem = level.viewItems && level.viewItems[0] ? level.viewItems[0] : 'project_lifecycle';
        state.selectedBasic = viewItem;
        state.view = 'basics';
        state.viewCategory = 'atlas';
        renderAll();
    }

    window.nextCourseLevel = function () {
        if (state.courseMode && state.courseLevel < ADAPTATION_COURSE.length - 1) {
            navigateCourse(state.courseLevel + 1);
        }
    };

    window.prevCourseLevel = function () {
        if (state.courseMode && state.courseLevel > 0) {
            navigateCourse(state.courseLevel - 1);
        }
    };

    function renderCourseLevelPanel() {
        var panel = document.getElementById('courseLevelPanel');
        if (!panel) { return; }

        if (!state.courseMode || !ADAPTATION_COURSE || ADAPTATION_COURSE.length === 0) {
            panel.classList.add('hidden');
            return;
        }
        panel.classList.remove('hidden');

        var list = document.getElementById('courseLevelList');
        if (!list) { return; }
        var toggleBtn = document.getElementById('courseLevelToggleBtn');

        if (toggleBtn) {
            toggleBtn.innerHTML = '\u00AB';
            toggleBtn.title = 'Collapse course levels';
            toggleBtn.setAttribute('aria-label', 'Collapse course levels');
        }

        list.classList.remove('hidden');
        list.innerHTML = '';

        ADAPTATION_COURSE.forEach(function (lvl, idx) {
            var btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'sidebar-item course-level-item' + (idx === state.courseLevel ? ' active' : '');
            btn.textContent = 'L' + lvl.level + ': ' + lvl.title;
            (function (capturedIdx) {
                btn.addEventListener('click', function () {
                    navigateCourse(capturedIdx);
                });
            }(idx));
            list.appendChild(btn);
        });
    }

    function renderCourseNavHeader() {
        var header = document.getElementById('courseNavHeader');
        if (!header) { return; }

        if (!state.courseMode || !ADAPTATION_COURSE || ADAPTATION_COURSE.length === 0) {
            header.classList.add('hidden');
            return;
        }
        header.classList.remove('hidden');

        var lvl = ADAPTATION_COURSE[state.courseLevel] || ADAPTATION_COURSE[0];
        var titleEl = document.getElementById('courseNavTitle');
        var descEl = document.getElementById('courseNavDesc');
        var prevBtn = document.getElementById('coursePrevBtn');
        var nextBtn = document.getElementById('courseNextBtn');

        if (titleEl) { titleEl.textContent = 'L' + lvl.level + ': ' + lvl.title; }
        if (descEl) { descEl.textContent = lvl.description || ''; }
        if (prevBtn) { prevBtn.disabled = state.courseLevel <= 0; }
        if (nextBtn) { nextBtn.disabled = state.courseLevel >= ADAPTATION_COURSE.length - 1; }
    }

    document.getElementById('themeToggle').addEventListener('click', function () {
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
    });

    document.getElementById('palettePreviews').addEventListener('click', function (event) {
        var btn = event.target.closest('.palette-preview-btn');
        if (!btn) {
            return;
        }
        var paletteName = btn.getAttribute('data-palette');
        applyPalette(paletteName);
        renderAll();
    });

    document.getElementById('sidebarList').addEventListener('click', function (event) {
        var btn = event.target.closest('.sidebar-item');
        if (!btn) { return; }
        var key = btn.getAttribute('data-entry-key');
        if (key) {
            setSelectedItemKey(key);
            renderAll();
        }
    });

    document.getElementById('sidebarToggleBtn').addEventListener('click', function () {
        state.sidebarCollapsed = true;
        try { window.localStorage.setItem(SIDEBAR_STORAGE_KEY, '1'); } catch (e) {}
        renderSidebar();
    });

    document.getElementById('sidebarExpandBtn').addEventListener('click', function () {
        if (state.courseMode) {
            state.courseLevelCollapsed = false;
            renderSidebar();
            return;
        }
        state.sidebarCollapsed = false;
        try { window.localStorage.setItem(SIDEBAR_STORAGE_KEY, '0'); } catch (e) {}
        renderSidebar();
    });

    document.getElementById('entryMeta').addEventListener('click', function (event) {
        var link = event.target.closest('.entry-compare-link');
        if (!link) {
            return;
        }
        event.preventDefault();
        var compareView = link.getAttribute('data-compare-view');
        var compareKey = link.getAttribute('data-compare-key');
        if (compareKey) {
            if (compareView && VIEW_CONFIG[compareView]) {
                state.view = compareView;
            }
            setSelectedItemKey(compareKey);
            renderAll();
        }
    });

    window.addEventListener('hljs-ready', applySyntaxHighlight);
    window.addEventListener('resize', updateStickyOffset);

    var savedTheme = 'dark';
    try {
        savedTheme = window.localStorage.getItem(THEME_STORAGE_KEY) || 'dark';
    } catch (err) {
        savedTheme = 'dark';
    }

    var savedPalette = 'brand';
    try {
        savedPalette = window.localStorage.getItem(PALETTE_STORAGE_KEY) || 'brand';
    } catch (err) {
        savedPalette = 'brand';
    }

    var savedViewCategory = 'atlas';
    try {
        savedViewCategory = window.localStorage.getItem(VIEW_CATEGORY_STORAGE_KEY) || 'atlas';
    } catch (err) {
        savedViewCategory = 'atlas';
    }

    var savedSidebarCollapsed = '0';
    try {
        savedSidebarCollapsed = window.localStorage.getItem(SIDEBAR_STORAGE_KEY) || '0';
    } catch (err) {
        savedSidebarCollapsed = '0';
    }

    applyTheme(savedTheme);
    applyPalette(savedPalette);
    state.viewCategory = savedViewCategory;
    state.sidebarCollapsed = savedSidebarCollapsed === '1';

    renderAll();
}());