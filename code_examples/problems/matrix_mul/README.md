# matrix_mul

## Overview

Multiply two N x N matrices using a straightforward triple-loop implementation.

## Implementations

- cpp.cpp
- go.go
- python.py
- typescript.ts
- scala.scala

## Input

No input file is required.

## Configuration

- N is set to 200.

## Expected output

```text
2646700
```

## Run with project runner

From repository root:

```powershell
& ".\tools\run_example.exe" -p matrix_mul -l cpp20
& ".\tools\run_example.exe" -p matrix_mul -l go
& ".\tools\run_example.exe" -p matrix_mul -l python
& ".\tools\run_example.exe" -p matrix_mul -l scala
& ".\tools\run_example.exe" -p matrix_mul -l typescript
```

## Manual run (without runner)

Python:

```powershell
python .\cheat_sheets\code_examples\problems\matrix_mul\python.py
```

C++20:

```powershell
New-Item -ItemType Directory -Force .\cheat_sheets\code_examples\problems\matrix_mul\out | Out-Null
g++ -std=c++20 -O2 -o .\cheat_sheets\code_examples\problems\matrix_mul\out\manual_run.exe .\cheat_sheets\code_examples\problems\matrix_mul\cpp.cpp
& ".\cheat_sheets\code_examples\problems\matrix_mul\out\manual_run.exe"
```

Go:

```powershell
go run .\cheat_sheets\code_examples\problems\matrix_mul\go.go
```

TypeScript:

```powershell
npx --yes ts-node .\cheat_sheets\code_examples\problems\matrix_mul\typescript.ts
```

Scala:

```powershell
scala-cli run .\cheat_sheets\code_examples\problems\matrix_mul\scala.scala
```

## Notes

- Scala uses explicit main(args: Array[String]) to avoid Scala 3 deprecation warnings.
- This folder includes package.json with type: module for TypeScript module-mode execution.
