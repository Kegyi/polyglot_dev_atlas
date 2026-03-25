#!/usr/bin/env python3


def count_bits(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def main() -> None:
    a, b = 0b1010, 0b1100  # 10, 12
    print(f"a & b:  {a & b:04b}")  # 1000
    print(f"a | b:  {a | b:04b}")  # 1110
    print(f"a ^ b:  {a ^ b:04b}")  # 0110

    n = 0b0101
    print(f"bit 1 set? {(n >> 1) & 1}")  # check -> 0
    n |= (1 << 2)   # set bit 2
    n &= ~(1 << 0)  # clear bit 0
    print(f"after set/clear: {n:04b}")   # 0100

    print(f"count bits in 7: {count_bits(7)}")  # 3


if __name__ == "__main__":
    main()
