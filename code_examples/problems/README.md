# Problems Code Examples

This folder contains language-parallel implementations for each problem.

Current problems:

- file_aggregate
- concurrency_demo
- matrix_mul
- word_count
- balanced_brackets
- grid_shortest_path
- top_k_frequent

## Layout

Current layout is flat per problem:

- cheat_sheets/code_examples/problems/<problem>/
- One source file per language (for example, cpp.cpp, scala.scala, python.py, go.go, typescript.ts)
- input/ (optional)
- out/ (generated artifacts)

Some problems may use problem-specific names such as FileAggregate.*.

## Runner

Runner source: tools/run_example.go
Runner executable: tools/run_example.exe

Build:

```powershell
go build -o .\tools\run_example.exe .\tools\run_example.go
```

Run (from repository root):

```powershell
& ".\tools\run_example.exe" -p <problem> -l <lang> [-t]
& ".\tools\run_example.exe" -pl
& ".\tools\run_example.exe" -pl -l <lang> [-t]
```

Language values:

- scala
- python
- go
- typescript or ts
- cpp, cpp17, cpp20, c++, c++17, c++20
- all (or ALL): run scala, python, cpp, go, typescript sequentially

Timing flag:

- -t (or -time): prints elapsed time for each executed command (compile and run steps)

Examples:

```powershell
& ".\tools\run_example.exe" -p file_aggregate -l typescript
& ".\tools\run_example.exe" -p concurrency_demo -l scala
& ".\tools\run_example.exe" -p matrix_mul -l cpp20
& ".\tools\run_example.exe" -p word_count -l python
& ".\tools\run_example.exe" -p concurrency_demo -l all -t
& ".\tools\run_example.exe" -pl
& ".\tools\run_example.exe" -pl -l ts -t
```

## TypeScript module note

Each problem folder now includes a local package.json with:

```json
{
	"private": true,
	"type": "module"
}
```

This avoids module-mode warnings and keeps settings local to each problem, without affecting the repository root.

## Manual run

See each problem README for direct per-language commands and expected output.
