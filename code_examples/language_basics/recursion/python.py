#!/usr/bin/env python3

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_recursive(values: list[int], index: int = 0) -> int:
    if index >= len(values):
        return 0
    return values[index] + sum_recursive(values, index + 1)


def main() -> None:
    values = [1, 2, 3, 4]
    print("factorial(5):", factorial(5))
    print("sum_recursive(values):", sum_recursive(values))


if __name__ == "__main__":
    main()
