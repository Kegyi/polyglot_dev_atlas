#!/usr/bin/env python3
import os


def main() -> None:
    mode = os.getenv("APP_MODE", "development")
    port = os.getenv("APP_PORT", "8080")

    print("mode:", mode)
    print("port:", port)
    print("has APP_MODE:", "APP_MODE" in os.environ)


if __name__ == "__main__":
    main()
