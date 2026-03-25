#!/usr/bin/env python3
import sys


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    excited = len(sys.argv) > 2 and sys.argv[2] == "--excited"

    message = f"Hello, {name}"
    if excited:
        message += "!"
    print(message)


if __name__ == "__main__":
    main()
