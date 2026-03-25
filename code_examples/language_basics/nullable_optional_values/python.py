#!/usr/bin/env python3
from typing import Optional


def parse_age(text: str) -> Optional[int]:
    if not text:
        return None
    return int(text)


def main() -> None:
    age = parse_age("29")
    missing = parse_age("")

    print("age present:", age is not None)
    print("missing default:", missing or 0)


if __name__ == "__main__":
    main()
