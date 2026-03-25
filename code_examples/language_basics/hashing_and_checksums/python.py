#!/usr/bin/env python3
import hashlib
import zlib


def main() -> None:
    text = "hello-world"
    encoded = text.encode("utf-8")

    sha256_hex = hashlib.sha256(encoded).hexdigest()
    crc32_value = zlib.crc32(encoded)

    print("text:", text)
    print("sha256:", sha256_hex)
    print("crc32:", crc32_value)


if __name__ == "__main__":
    main()
