def can_permute_palindrome(s: str) -> bool:
    counts: dict[str, int] = {}
    for ch in s.lower():
        if ch.isspace():
            continue
        counts[ch] = counts.get(ch, 0) + 1
    odd = sum(1 for c in counts.values() if c % 2 == 1)
    return odd <= 1


def main() -> None:
    print(f"tact coa -> {can_permute_palindrome('tact coa')}")
    print(f"daily -> {can_permute_palindrome('daily')}")


if __name__ == "__main__":
    main()
