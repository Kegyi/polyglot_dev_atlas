def pattern_matching(pattern: str, value: str) -> bool:
    if not pattern:
        return value == ""

    count_a = pattern.count("a")
    count_b = pattern.count("b")

    if count_a < count_b:
        swapped = "".join("b" if c == "a" else "a" for c in pattern)
        return pattern_matching(swapped, value)

    if value == "":
        return count_b == 0

    n = len(value)
    for len_a in range(0, n // count_a + 1):
        rest = n - count_a * len_a
        if count_b == 0:
            if rest != 0:
                continue
            len_b = 0
        else:
            if rest % count_b != 0:
                continue
            len_b = rest // count_b

        pos = 0
        a = None
        b = None
        ok = True
        for ch in pattern:
            if ch == "a":
                sub = value[pos:pos + len_a]
                if a is None:
                    a = sub
                elif a != sub:
                    ok = False
                    break
                pos += len_a
            else:
                sub = value[pos:pos + len_b]
                if b is None:
                    b = sub
                elif b != sub:
                    ok = False
                    break
                pos += len_b
        if ok and a != b:
            return True
    return False


def main() -> None:
    print(pattern_matching("abba", "dogcatcatdog"))
    print(pattern_matching("abba", "dogcatcatfish"))


if __name__ == "__main__":
    main()
