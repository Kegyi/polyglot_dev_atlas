#!/usr/bin/env python3
import json


def main() -> None:
    user = {"name": "Alice", "age": 29}
    text = json.dumps(user)
    parsed = json.loads(text)

    print("json:", text)
    print("parsed name:", parsed["name"])


if __name__ == "__main__":
    main()
