def is_unique(s: str) -> bool:
    seen: set[str] = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True


def main() -> None:
    print(f"leetcode -> {is_unique('leetcode')}")
    print(f"abc -> {is_unique('abc')}")


if __name__ == "__main__":
    main()
