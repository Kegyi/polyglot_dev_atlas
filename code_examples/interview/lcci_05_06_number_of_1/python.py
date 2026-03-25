def convert_integer(A: int, B: int) -> int:
    # Work with 32-bit two's complement representation
    x = (A ^ B) & 0xFFFFFFFF
    return bin(x).count('1')


def main() -> None:
    print(convert_integer(29, 15))
    print(convert_integer(1, 5))


if __name__ == "__main__":
    main()
