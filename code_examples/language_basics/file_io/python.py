#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    path = Path("file_io_demo.txt")
    path.write_text("apple\nbanana\ncarrot\n", encoding="utf-8")

    lines = path.read_text(encoding="utf-8").splitlines()
    print("read lines:", lines)


if __name__ == "__main__":
    main()
