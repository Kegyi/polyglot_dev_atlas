#!/usr/bin/env python3

def main() -> None:
    first = "hello"
    second = "world"
    joined = first + " " + second

    part = joined[:5]
    replaced = joined.replace("hello", "hi", 1)
    words = joined.split()

    print("joined:", joined)
    print("part:", part)
    print("replaced:", replaced)
    print("tokens:", words)


if __name__ == "__main__":
    main()
