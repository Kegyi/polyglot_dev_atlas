def flip_bit(num: int) -> int:
    # Treat as 32-bit unsigned integer
    if num & 0xFFFFFFFF == 0xFFFFFFFF:
        return 32
    num = num & 0xFFFFFFFF
    cur = prev = 0
    best = 1
    while num > 0:
        if num & 1:
            cur += 1
        else:
            prev = cur
            cur = 0
        best = max(best, prev + 1 + cur)
        num >>= 1
    return best


def main() -> None:
    print(flip_bit(1775))
    print(flip_bit(7))


if __name__ == "__main__":
    main()
