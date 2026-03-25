# Polyglot Dev Atlas

This atlas helps compare practical code patterns across C++, Python, Go, TypeScript, and Scala.

## Quick Usage Guide

If this is your first time here, use this flow:

1. Choose one or two languages from the `LANGUAGES` row.
2. Click `ATLAS VIEWS` / `LEARNING VIEWS` (the colored row title) to switch the whole view set.
3. Pick a view chip from the same row (for example `Keywords`, `Workflow`, `Exercises`, `Interview`).
4. Use the item dropdown (`Problem`, `Question`, `Task`, etc.) to select a specific entry.
5. Toggle `Compare 2` to see side-by-side code in two languages.
6. Use `Swap` to quickly switch left/right compared languages.
7. Use style controls:
	- Palette buttons: `Brand`, `Technical`, `Soft`
	- Theme toggle: dark/light
8. In `Exercises`, click `Show Solution` to reveal code per language panel.

### What Each View Set Contains

- `ATLAS VIEWS`: `Keywords`, `Workflow`, `Design Patterns`, `Principles`
- `LEARNING VIEWS`: `Lang. Basic`, `Course`, `Exercises`, `Problems`, `Interview`

### Practical Tips

- Start with `Keywords` for quick syntax recall.
- Use `Problems` or `Interview` for realistic coding patterns.
- Use `Exercises` for guided practice from beginner to advanced.
- Keep compare mode on when you want to map the same concept across languages.

## Cross-language Advanced Patterns

Legend: `X` means no close built-in equivalent. `Partial (approx)` means conceptually similar, but semantics are different.

| Pattern | C++ | Go | Python | TypeScript | Scala |
| --- | --- | --- | --- | --- | --- |
| Generics / templates | `template<class T> T max2(T a,T b)` | `func Max2[T constraints.Ordered](a,b T) T` | `T = TypeVar('T'); def max2(a:T,b:T)->T` | `function max2<T>(a:T,b:T):T` | `def max2[T: Ordering](a:T,b:T):T` |
| Closures / lambdas | `[&](int x){ return x + bias; }` | `func(x int) int { return x + bias }` | `lambda x: x + bias` | `(x:number) => x + bias` | `x => x + bias` |
| Iteration pipelines | `ranges::copy_if(v, out, p); ranges::transform(out, out2, f)` | `slices.DeleteFunc(xs, pred)` + `for _,x := range xs` | `[f(x) for x in xs if p(x)]` | `xs.filter(p).map(f)` | `xs.filter(p).map(f)` |
| Async / concurrency | `std::async(std::launch::async, work)` | `go work(); select { case v := <-ch: ... }` | `await asyncio.gather(*tasks)` | `await Promise.all(tasks)` | `Future.traverse(xs)(work)` |
| Error propagation | `std::expected<T,E>` or `try { ... } catch (...) {}` | `v, err := fn(); if err != nil { ... }` | `try: ... except ValueError: ...` | `Partial (approx): Result<T,E> object with ok/value or ok/error branches` | `Either[E, A]` or `Try[A]` |
| Access modifiers | `public`, `protected`, `private` | `X` | `Partial (approx): convention _name and __name mangling` | `public`, `protected`, `private` | `private`, `protected` |
| Algebraic data types | `std::variant<A,B>` + `std::visit` | `X` | `Partial (approx): typing.Union[A,B]` | `Partial (approx): type Shape = Circle or Rect` | `sealed trait Shape` + `case class` |
| Pattern matching | `X` | `X` | `match value: case ...` | `Partial (approx): switch over discriminated union tags` | `value match { case ... => ... }` |
| Type-level programming | templates and `constexpr` constraints | `X` | `X` | conditional and mapped types | implicits or givens plus type classes |
| Resource cleanup pattern | RAII and destructors | `defer cleanup()` | `with resource as r:` | `Partial (approx): try { ... } finally { cleanup(); }` | `Using(resource) { r => ... }` |
| Immutability-first collections | `Partial (approx): const with persistent libraries optional` | `X` | `Partial (approx): tuples, frozen dataclasses optional` | `Partial (approx): ReadonlyArray<T> and as const` | immutable `List`, `Vector`, `Map` |

## Language-specific Features

__LANG_SPECIFIC_FEATURES__

Use this page as orientation, then move into `ATLAS VIEWS` or `LEARNING VIEWS` for side-by-side code exploration.