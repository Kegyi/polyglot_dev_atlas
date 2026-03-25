#!/usr/bin/env python3


def parse_port(value: str) -> int:
    return int(value)


def main() -> None:
    try:
        port = parse_port("not-a-number")
        print("port:", port)
    except ValueError as error:
        print("parse failed:", error)
        print("fallback port:", 8080)

    print("program continues")


if __name__ == "__main__":
    main()
