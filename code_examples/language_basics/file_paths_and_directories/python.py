#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    base = Path("demo_folder")
    file_path = base / "sub" / "data.txt"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    print("file path:", file_path)
    print("parent path:", file_path.parent)
    print("directory exists:", file_path.parent.exists())


if __name__ == "__main__":
    main()
