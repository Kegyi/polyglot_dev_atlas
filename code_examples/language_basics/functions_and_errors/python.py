#!/usr/bin/env python3
from typing import Optional


def add(a: int, b: int) -> int:
    return a + b


def safe_div(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def strict_div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def main() -> None:
    print("add(2, 3):", add(2, 3))
    print("safe_div(10, 2):", safe_div(10, 2))

    try:
        print("strict_div(10, 0):", strict_div(10, 0))
    except ValueError as err:
        print("error:", err)


if __name__ == "__main__":
    main()
