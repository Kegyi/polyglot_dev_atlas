# concurrency_demo

## Overview

Compute the sum of numbers 1 through 1000 by splitting work into chunks and processing those chunks concurrently.

## Implementations

- cpp.cpp
- go.go
- python.py
- typescript.ts
- scala.scala

## Input

No input file is required.

## Expected output

```text
Total: 500500
```

## Run with project runner

From repository root:

```powershell
& ".\tools\run_example.exe" -p concurrency_demo -l cpp20
& ".\tools\run_example.exe" -p concurrency_demo -l go
& ".\tools\run_example.exe" -p concurrency_demo -l python
& ".\tools\run_example.exe" -p concurrency_demo -l scala
& ".\tools\run_example.exe" -p concurrency_demo -l typescript
```

## Manual run (without runner)

Python:

```powershell
python .\cheat_sheets\code_examples\problems\concurrency_demo\python.py
```

C++20:

```powershell
New-Item -ItemType Directory -Force .\cheat_sheets\code_examples\problems\concurrency_demo\out | Out-Null
g++ -std=c++20 -O2 -o .\cheat_sheets\code_examples\problems\concurrency_demo\out\manual_run.exe .\cheat_sheets\code_examples\problems\concurrency_demo\cpp.cpp
& ".\cheat_sheets\code_examples\problems\concurrency_demo\out\manual_run.exe"
```

Go:

```powershell
go run .\cheat_sheets\code_examples\problems\concurrency_demo\go.go
```

TypeScript:

```powershell
npx --yes ts-node .\cheat_sheets\code_examples\problems\concurrency_demo\typescript.ts
```

Scala:

```powershell
scala-cli run .\cheat_sheets\code_examples\problems\concurrency_demo\scala.scala
```

## Notes

- Scala uses explicit main(args: Array[String]) to stay warning-free on Scala 3 and compatible with Scala 2 style.
- This folder includes package.json with type: module for TypeScript module-mode execution.
