from collections import Counter


def check_permutation(a: str, b: str) -> bool:
    return len(a) == len(b) and Counter(a) == Counter(b)


def main() -> None:
    print(f"abcde vs edcba -> {check_permutation('abcde', 'edcba')}")
    print(f"abc vs abz -> {check_permutation('abc', 'abz')}")


if __name__ == "__main__":
    main()
