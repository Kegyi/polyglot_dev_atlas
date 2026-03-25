# file_aggregate

## Overview

Read a score file, group scores by name, compute average score per name, and print results in descending order.

## Implementations

- FileAggregate.cpp
- FileAggregate.go
- FileAggregate.py
- FileAggregate.scala
- FileAggregate.ts

## Input

Default sample input:

```text
input/data.txt
```

Input rules:

- Each data line: <name>, <score>
- Empty lines are ignored
- Lines starting with # are ignored
- Invalid lines are skipped

Bundled sample input:

```text
# sample data
Alice, 90
Bob, 80
Alice, 70
# ignored comment
Charlie, 100
Bob, 60
```

## Expected output with bundled sample input

```text
Charlie: 100.00
Alice: 80.00
Bob: 70.00
```

## Run with project runner

From repository root:

```powershell
& ".\tools\run_example.exe" -p file_aggregate -l cpp20
& ".\tools\run_example.exe" -p file_aggregate -l go
& ".\tools\run_example.exe" -p file_aggregate -l python
& ".\tools\run_example.exe" -p file_aggregate -l scala
& ".\tools\run_example.exe" -p file_aggregate -l typescript
```

## Manual run (without runner)

Python:

```powershell
python .\cheat_sheets\code_examples\problems\file_aggregate\FileAggregate.py .\cheat_sheets\code_examples\problems\file_aggregate\input\data.txt
```

C++20:

```powershell
New-Item -ItemType Directory -Force .\cheat_sheets\code_examples\problems\file_aggregate\out | Out-Null
g++ -std=c++20 -O2 -o .\cheat_sheets\code_examples\problems\file_aggregate\out\manual_run.exe .\cheat_sheets\code_examples\problems\file_aggregate\FileAggregate.cpp
& ".\cheat_sheets\code_examples\problems\file_aggregate\out\manual_run.exe" .\cheat_sheets\code_examples\problems\file_aggregate\input\data.txt
```

Go:

```powershell
go run .\cheat_sheets\code_examples\problems\file_aggregate\FileAggregate.go .\cheat_sheets\code_examples\problems\file_aggregate\input\data.txt
```

TypeScript:

```powershell
npx --yes ts-node .\cheat_sheets\code_examples\problems\file_aggregate\FileAggregate.ts .\cheat_sheets\code_examples\problems\file_aggregate\input\data.txt
```

Scala:

```powershell
scala-cli run .\cheat_sheets\code_examples\problems\file_aggregate\FileAggregate.scala -- .\cheat_sheets\code_examples\problems\file_aggregate\input\data.txt
```

## Notes

- This folder includes package.json with type: module for TypeScript module-mode execution.
- Runner supports C++ language flags: cpp, cpp17, cpp20, c++17, c++20.

## Troubleshooting

### Common errors

Problem not found: file_aggregate

- Cause: runner was started from the wrong directory.
- Fix: run from repository root:

```powershell
& ".\tools\run_example.exe" -p file_aggregate -l <lang> [-t]
```

Error: unable to open file

- Cause: input file path is wrong or not passed for manual runs.
- Fix: pass input explicitly:

```powershell
& ".\cheat_sheets\code_examples\problems\file_aggregate\out\manual_run.exe" .\cheat_sheets\code_examples\problems\file_aggregate\input\data.txt
```

No C++ compiler found (g++/clang++)

- Cause: no C++ compiler on PATH.
- Fix: install MSYS2/MinGW g++ or LLVM clang++ and restart terminal.

Python not found

- Cause: Python is not installed, not on PATH, or Windows App execution aliases are interfering.
- Fix: install Python and enable Add Python to PATH.
- Fix (Windows): open Settings > Apps > App execution aliases and disable Microsoft Store aliases for python.exe/python3.exe if they hijack your command.

No Scala runtime found

- Cause: scala-cli/scalac/scala/sbt are missing.
- Fix: install scala-cli (recommended) or full Scala toolchain.

No TypeScript runtime found

- Cause: ts-node, npx, tsx, and deno are all missing.
- Fix: install Node.js (for npx) or install ts-node/tsx/deno.

nodejs\npm.ps1 cannot be loaded because running scripts is disabled

- Cause: PowerShell execution policy blocks npm.ps1.
- Fix: use npx.cmd (the runner already prefers this on Windows) or use tsx/deno.

### Installation (for missing tools)

If a runtime/compiler is missing, install one of the following (Windows examples):

```powershell
winget install Python.Python.3
winget install GoLang.Go
winget install OpenJS.NodeJS.LTS
winget install ScalaCenter.scala-cli
```

For C++ compiler options on Windows:

- MSYS2/MinGW (g++)
- LLVM (clang++)

After installing tools, open a new terminal and verify:

```powershell
python --version
go version
node --version
npx --version
scala-cli version
g++ --version
```
