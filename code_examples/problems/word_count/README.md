# word_count

## Overview

Tokenize a text file and print words ranked by frequency.

## Implementations

- cpp.cpp
- go.go
- python.py
- typescript.ts
- scala.scala

## Input

Default sample input:

```text
input/data.txt
```

## Expected output with bundled sample input

```text
hello: 2
world: 2
test: 2
this: 1
is: 1
a: 1
of: 1
words: 1
```

## Run with project runner

From repository root:

```powershell
& ".\tools\run_example.exe" -p word_count -l cpp20
& ".\tools\run_example.exe" -p word_count -l go
& ".\tools\run_example.exe" -p word_count -l python
& ".\tools\run_example.exe" -p word_count -l scala
& ".\tools\run_example.exe" -p word_count -l typescript
```

## Manual run (without runner)

Python:

```powershell
python .\cheat_sheets\code_examples\problems\word_count\python.py .\cheat_sheets\code_examples\problems\word_count\input\data.txt
```

C++20:

```powershell
New-Item -ItemType Directory -Force .\cheat_sheets\code_examples\problems\word_count\out | Out-Null
g++ -std=c++20 -O2 -o .\cheat_sheets\code_examples\problems\word_count\out\manual_run.exe .\cheat_sheets\code_examples\problems\word_count\cpp.cpp
& ".\cheat_sheets\code_examples\problems\word_count\out\manual_run.exe" .\cheat_sheets\code_examples\problems\word_count\input\data.txt
```

Go:

```powershell
go run .\cheat_sheets\code_examples\problems\word_count\go.go .\cheat_sheets\code_examples\problems\word_count\input\data.txt
```

TypeScript:

```powershell
npx --yes ts-node .\cheat_sheets\code_examples\problems\word_count\typescript.ts .\cheat_sheets\code_examples\problems\word_count\input\data.txt
```

Scala:

```powershell
scala-cli run .\cheat_sheets\code_examples\problems\word_count\scala.scala -- .\cheat_sheets\code_examples\problems\word_count\input\data.txt
```

## Notes

- Difficulty: easy to moderate depending on tokenization requirements.
- Implementation details may vary: regex vs manual filtering.
- This folder includes package.json with type: module for TypeScript module-mode execution.