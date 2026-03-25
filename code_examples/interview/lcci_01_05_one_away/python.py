def one_away(a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
        return False

    s1, s2 = (a, b) if len(a) <= len(b) else (b, a)
    i = j = 0
    found = False

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            continue

        if found:
            return False
        found = True

        if len(s1) == len(s2):
            i += 1
        j += 1

    return True


def main() -> None:
    print(f"pale vs ple -> {one_away('pale', 'ple')}")
    print(f"pales vs pale -> {one_away('pales', 'pale')}")
    print(f"pale vs bake -> {one_away('pale', 'bake')}")


if __name__ == "__main__":
    main()
