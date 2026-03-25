def compress_string(s: str) -> str:
    if not s:
        return s

    out: list[str] = []
    run = 1

    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            run += 1
            continue

        out.append(s[i - 1])
        out.append(str(run))
        run = 1

    compressed = "".join(out)
    return compressed if len(compressed) < len(s) else s


def main() -> None:
    print(f"aabcccccaaa -> {compress_string('aabcccccaaa')}")
    print(f"abbccd -> {compress_string('abbccd')}")


if __name__ == "__main__":
    main()
