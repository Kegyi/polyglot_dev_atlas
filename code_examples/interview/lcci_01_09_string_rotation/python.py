def is_string_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in (s1 + s1)


def main() -> None:
    print(f"waterbottle vs erbottlewat -> {is_string_rotation('waterbottle', 'erbottlewat')}")
    print(f"aa vs aba -> {is_string_rotation('aa', 'aba')}")


if __name__ == "__main__":
    main()
