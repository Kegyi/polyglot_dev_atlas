def insert(N: int, M: int, i: int, j: int) -> int:
    mask = ~(((1 << (j - i + 1)) - 1) << i)
    return (N & mask) | (M << i)


def main() -> None:
    print(insert(1024, 19, 2, 6))
    print(insert(0, 19, 0, 4))


if __name__ == "__main__":
    main()
